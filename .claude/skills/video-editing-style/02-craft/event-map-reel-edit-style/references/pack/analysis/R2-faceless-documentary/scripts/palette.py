import sys,cv2,numpy as np
D=sys.argv[1]
scenes=[("hospital ext",30),("surgery",85),("sky+card",130),("sky ticker",200),("study",280),("1840s grid",306),("photo on grid",336),("graph",420),
("corridor",540),("sink",660),("deathrate",745),("clipboard",800),("newspaper",890),("microscope",960),("spotlight",1040),("cta text",1105),("laptop",1215)]
def hx(c): return '#%02X%02X%02X'%(int(c[2]),int(c[1]),int(c[0]))
print("scene           f     mean     luma  sat  | k-means 4 (share)")
for name,n in scenes:
    im=cv2.imread(f'{D}/fr/{n:04d}.jpg'); sm=cv2.resize(im,(90,160),interpolation=cv2.INTER_AREA)
    px=sm.reshape(-1,3).astype(np.float32)
    crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.5)
    _,lab,cen=cv2.kmeans(px,4,None,crit,4,cv2.KMEANS_PP_CENTERS)
    cnt=np.bincount(lab.ravel(),minlength=4); o=np.argsort(cnt)[::-1]
    hsv=cv2.cvtColor(sm,cv2.COLOR_BGR2HSV); luma=cv2.cvtColor(sm,cv2.COLOR_BGR2GRAY).mean()
    print(f"{name:14s} {n:5d}  {hx(px.mean(0))}  {luma:5.0f} {hsv[...,1].mean()/255:.2f} | "+"  ".join(f"{hx(cen[k])}({100*cnt[k]/cnt.sum():.0f}%)" for k in o))
# black / white points per scene
print("\nscene  p1 luma  p99 luma (full-res frames from fr/)")
for name,n in scenes:
    g=cv2.imread(f'{D}/fr/{n:04d}.jpg',0); print(f"{name:14s} {np.percentile(g,1):5.0f} {np.percentile(g,99):5.0f}")
