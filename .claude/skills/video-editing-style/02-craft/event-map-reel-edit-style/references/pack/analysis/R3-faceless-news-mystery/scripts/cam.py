# per-frame similarity transform (scale, rotation, tx, ty) between consecutive frames using ORB+RANSAC
import sys, glob, json, numpy as np, cv2
D=sys.argv[1]
files=sorted(glob.glob(f'{D}/fr/*.jpg'))
orb=cv2.ORB_create(1500); bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
prev=None; rows=[]
for i,f in enumerate(files):
    g=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
    kp,des=orb.detectAndCompute(g,None)
    r=dict(f=i,s=None,rot=None,tx=None,ty=None,n=0)
    if prev is not None and des is not None and prev[1] is not None and len(kp)>20 and len(prev[0])>20:
        m=bf.match(prev[1],des)
        if len(m)>=12:
            a=np.float32([prev[0][x.queryIdx].pt for x in m]); b=np.float32([kp[x.trainIdx].pt for x in m])
            M,inl=cv2.estimateAffinePartial2D(a,b,method=cv2.RANSAC,ransacReprojThreshold=2.0)
            if M is not None and inl is not None and inl.sum()>=10:
                s=float(np.hypot(M[0,0],M[1,0])); rot=float(np.degrees(np.arctan2(M[1,0],M[0,0])))
                # translation of frame centre
                c=np.array([180,320,1.0]); p=M@c
                r=dict(f=i,s=round(s,5),rot=round(rot,3),tx=round(float(p[0]-180),2),ty=round(float(p[1]-320),2),n=int(inl.sum()))
    rows.append(r); prev=(kp,des)
json.dump(rows,open(f'{D}/data/cam.json','w'))
print('done',len(rows))
