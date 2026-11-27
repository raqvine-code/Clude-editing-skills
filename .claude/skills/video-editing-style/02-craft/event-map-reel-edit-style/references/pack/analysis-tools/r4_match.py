# Estimate similarity transform RAW panel -> EDITED panel per frame (scale, tx, ty, rotation, inliers)
import sys, json, numpy as np, cv2
R=sys.argv[1]
sift=cv2.SIFT_create(nfeatures=1500)
bf=cv2.BFMatcher(cv2.NORM_L2)
out=[]
for n in range(0,1068,2):
    a=cv2.imread(f'{R}/raw/{n:04d}.jpg',0); b=cv2.imread(f'{R}/ed/{n:04d}.jpg',0)
    a2=cv2.resize(a,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)  # upsample raw x2 for features
    ka,da=sift.detectAndCompute(a2,None); kb,db=sift.detectAndCompute(b,None)
    rec=dict(f=n,s=None)
    if da is not None and db is not None and len(ka)>10 and len(kb)>10:
        m=bf.knnMatch(da,db,k=2); good=[p for p,q in m if p.distance<0.72*q.distance]
        if len(good)>=8:
            pa=np.float32([ka[g.queryIdx].pt for g in good])/2.0; pb=np.float32([kb[g.trainIdx].pt for g in good])
            M,inl=cv2.estimateAffinePartial2D(pa,pb,method=cv2.RANSAC,ransacReprojThreshold=3.0)
            if M is not None and inl is not None and inl.sum()>=8:
                s=float(np.hypot(M[0,0],M[1,0])); rot=float(np.degrees(np.arctan2(M[1,0],M[0,0])))
                rec=dict(f=n,s=round(s,4),rot=round(rot,2),tx=round(float(M[0,2]),1),ty=round(float(M[1,2]),1),inl=int(inl.sum()),good=len(good))
    out.append(rec)
json.dump(out,open(f'{R}/data/raw_to_ed.json','w'))
# print compact table: every 10 frames
base=696/550.0
print('baseline scale if identical framing (panel heights 696/550): %.3f'%base)
for r in out:
    if r['f']%10==0:
        if r['s']: print(f"f{r['f']:4d} t={r['f']/30:5.2f} s={r['s']:.3f} punch={r['s']/base:.3f} rot={r['rot']:+.2f} tx={r['tx']:7.1f} ty={r['ty']:7.1f} inl={r['inl']}")
        else: print(f"f{r['f']:4d} t={r['f']/30:5.2f} no match")
