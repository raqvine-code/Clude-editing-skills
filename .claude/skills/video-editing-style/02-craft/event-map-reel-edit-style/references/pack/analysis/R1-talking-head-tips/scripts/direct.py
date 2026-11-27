# Direct (non-chained) similarity fit between shot-start frame and later frames, captions masked out.
import cv2, numpy as np, sys
V=sys.argv[1]
shots=[(0,99),(220,313),(367,451),(473,583),(613,770),(833,1020)]
want={}
for a,b in shots:
    for f in sorted(set(list(range(a,b+1,10))+[b])): want[f]=a
cap=cv2.VideoCapture(V); i=0; g={}
while True:
    ok,im=cap.read()
    if not ok: break
    if i in want: g[i]=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    i+=1
H,W=next(iter(g.values())).shape
mask=np.full((H,W),255,np.uint8); mask[int(H*0.40):int(H*0.80),:]=0  # caption band
clahe=cv2.createCLAHE(clipLimit=4.0,tileGridSize=(8,8))
sift=cv2.SIFT_create(nfeatures=5000,contrastThreshold=0.008); bf=cv2.BFMatcher()
kd={f:sift.detectAndCompute(clahe.apply(im),mask) for f,im in g.items()}
for a,b in shots:
    ka,da=kd[a]; row=[]
    for f in sorted(x for x in g if want[x]==a):
        if f==a: continue
        kb,db=kd[f]; m=bf.knnMatch(da,db,k=2); good=[x for x,y in m if x.distance<0.75*y.distance]
        pa=np.float32([ka[x.queryIdx].pt for x in good]); pb=np.float32([kb[x.trainIdx].pt for x in good])
        M,inl=cv2.estimateAffinePartial2D(pa,pb,method=cv2.RANSAC,ransacReprojThreshold=3.0)
        s=np.hypot(M[0,0],M[1,0]); row.append("%d:%.3f/%d"%(f,s,inl.sum()))
    print("shot",a,b," ".join(row))
