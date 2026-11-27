# Track camera scale/translation of the talking-head shots relative to a common wide reference frame.
import cv2, numpy as np, json, sys
V=sys.argv[1]; REF=int(sys.argv[2])
cap=cv2.VideoCapture(V); frames={}
N=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
shots=[(0,99),(220,313),(367,451),(473,583),(613,770),(833,1020)]
want=set()
for a,b in shots: want.update(range(a,b+1))
want.add(REF)
i=0; gray={}
while True:
    ok,im=cap.read()
    if not ok: break
    if i in want: gray[i]=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    i+=1
sift=cv2.SIFT_create(nfeatures=3000,contrastThreshold=0.01)
def feats(g):
    # boost shadows so the dark background contributes features
    g2=cv2.createCLAHE(clipLimit=4.0,tileGridSize=(8,8)).apply(g)
    return sift.detectAndCompute(g2,None)
kr,dr=feats(gray[REF]); bf=cv2.BFMatcher()
out={}
def match(ka,da,kb,db):
    m=bf.knnMatch(da,db,k=2); good=[x for x,y in m if x.distance<0.75*y.distance]
    if len(good)<8: return None
    pa=np.float32([ka[x.queryIdx].pt for x in good]); pb=np.float32([kb[x.trainIdx].pt for x in good])
    M,inl=cv2.estimateAffinePartial2D(pb,pa,method=cv2.RANSAC,ransacReprojThreshold=4.0)  # maps REF -> frame
    if M is None: return None
    s=float(np.hypot(M[0,0],M[1,0])); rot=float(np.degrees(np.arctan2(M[1,0],M[0,0])))
    return s,rot,float(M[0,2]),float(M[1,2]),int(inl.sum()),len(good)
for a,b in shots:
    for f in range(a,b+1):
        k,d=feats(gray[f]); r=match(k,d,kr,dr)
        out[f]=r
json.dump(out,open(sys.argv[3],'w'))
for a,b in shots:
    print(f"shot f{a}-{b}")
    for f in list(range(a,b+1,6))+[b]:
        r=out[f]
        print("   f%4d t=%6.2f "%(f,f/30)+("scale %.3f rot %+.2f tx %+7.1f ty %+7.1f inl %d/%d"%r if r else "no match"))
