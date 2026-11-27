# Within-shot chained similarity transform (frame n-1 -> n) to get zoom curve per shot.
import cv2, numpy as np, json, sys
V=sys.argv[1]
shots=[(0,99),(220,313),(367,451),(473,583),(613,770),(833,1020)]
cap=cv2.VideoCapture(V); sift=cv2.SIFT_create(nfeatures=4000,contrastThreshold=0.008); bf=cv2.BFMatcher()
clahe=cv2.createCLAHE(clipLimit=4.0,tileGridSize=(8,8))
res={}
i=0; prev=None; shot_of={}
for a,b in shots:
    for f in range(a,b+1): shot_of[f]=a
while True:
    ok,im=cap.read()
    if not ok: break
    if i in shot_of:
        g=clahe.apply(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)); k,d=sift.detectAndCompute(g,None)
        if prev is not None and shot_of.get(i-1)==shot_of[i] and d is not None and prev[1] is not None:
            m=bf.knnMatch(prev[1],d,k=2); good=[x for x,y in m if x.distance<0.7*y.distance]
            if len(good)>=10:
                pa=np.float32([prev[0][x.queryIdx].pt for x in good]); pb=np.float32([k[x.trainIdx].pt for x in good])
                M,inl=cv2.estimateAffinePartial2D(pa,pb,method=cv2.RANSAC,ransacReprojThreshold=2.0)
                if M is not None:
                    res[i]=(float(np.hypot(M[0,0],M[1,0])),float(np.degrees(np.arctan2(M[1,0],M[0,0]))),float(M[0,2]),float(M[1,2]),int(inl.sum()),len(good))
        prev=(k,d)
    else: prev=None
    i+=1
json.dump(res,open(sys.argv[2],'w'))
for a,b in shots:
    s=1.0; rot=0.0; curve=[]
    for f in range(a,b+1):
        if f in res: s*=res[f][0]; rot+=res[f][1]
        curve.append((f,s,rot,res[f][4] if f in res else 0))
    print(f"shot f{a}-{b}: total scale x{curve[-1][1]:.3f} over {(b-a)/30:.2f}s, net rot {curve[-1][2]:+.2f} deg")
    step=3 if (b-a)<120 else 6
    print("   "+"  ".join(f"{f}:{s:.3f}" for f,s,r,n in curve[::step]))
    # largest single-frame scale jumps
    jumps=sorted([(abs(res[f][0]-1),f,res[f][0]) for f in range(a+1,b+1) if f in res],reverse=True)[:6]
    print("   biggest per-frame scale steps:", [(f,round(s,4)) for _,f,s in jumps])
