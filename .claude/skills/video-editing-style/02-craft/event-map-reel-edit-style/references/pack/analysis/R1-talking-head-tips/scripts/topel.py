# Track the warm bokeh cluster near the top: centroid, area, colour; compare with chained global translation.
import cv2, numpy as np, json, sys
V=sys.argv[1]; ch={int(k):v for k,v in json.load(open(sys.argv[2])).items()}
cap=cv2.VideoCapture(V); i=0; rows=[]
while True:
    ok,im=cap.read()
    if not ok: break
    top=im[:330].astype(np.float32); b,g,r=top[...,0],top[...,1],top[...,2]
    m=(r>150)&(g>110)&(b<g*0.85)&(r>b+60)
    n=int(m.sum())
    if n>30:
        ys,xs=np.nonzero(m); cx,cy=xs.mean(),ys.mean()
        core=(r>235)&(g>220)&m
        col=np.median(im[:330][core],0) if core.sum()>5 else np.median(im[:330][m],0)
        rows.append((i,round(cx,1),round(cy,1),n,[int(c) for c in col[::-1]]))
    else: rows.append((i,None,None,n,None))
    i+=1
def p(a,b):
    seg=[r for r in rows if a<=r[0]<=b]
    vis=[r for r in seg if r[1] is not None]
    print(f"f{a}-{b}: visible {len(vis)}/{len(seg)}", end=" ")
    if vis:
        xs=np.array([r[1] for r in vis]); ys=np.array([r[2] for r in vis])
        # frame-to-frame jitter vs global camera translation
        dj=np.diff(xs); 
        gx=np.array([ch.get(r[0],[1,0,0,0])[2] for r in vis[1:]])
        print(f"x {xs.min():.0f}-{xs.max():.0f} y {ys.min():.0f}-{ys.max():.0f} | elem dx sd {dj.std():.2f}px, global dx sd {gx.std():.2f}px, corr {np.corrcoef(dj,gx)[0,1] if gx.std()>0 else 0:.2f} | rgb {vis[len(vis)//2][4]}")
    else: print()
for a,b in [(0,99),(220,313),(367,451),(473,583),(613,770),(833,1020)]: p(a,b)
print([r[:4] for r in rows[900:912]])
