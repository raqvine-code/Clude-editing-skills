# usage: python3 -I vmetrics.py <reel_dir>
import sys, re, glob, json, numpy as np, cv2
D=sys.argv[1]
# scene scores
t=None; sc=[]
for l in open(f'{D}/data/scene_raw.txt'):
    m=re.search(r'pts_time:([\d.]+)',l)
    if m: t=float(m.group(1))
    m=re.search(r'scene_score=([\d.]+)',l)
    if m: sc.append(float(m.group(1)))
files=sorted(glob.glob(f'{D}/fr/*.jpg')); N=len(files)
prev=None; rows=[]
for i,f in enumerate(files):
    im=cv2.imread(f); g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32)
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    d=float(np.abs(g-prev).mean()) if prev is not None else 0.0
    # global motion via phase correlation on downscaled gray (dx,dy) + response
    if prev is not None:
        (dx,dy),resp=cv2.phaseCorrelate(prev,g)
    else: dx=dy=resp=0.0
    rows.append(dict(f=i,t=round(i/30,3),diff=round(d,2),luma=round(float(np.median(g)),1),lmean=round(float(g.mean()),1),
                     sat=round(float(hsv[...,1].mean())/255,3),dx=round(dx,2),dy=round(dy,2),resp=round(resp,3),
                     scene=round(sc[i],3) if i<len(sc) else 0))
    prev=g
json.dump(rows,open(f'{D}/data/frames.json','w'))
diff=np.array([r['diff'] for r in rows]); scene=np.array([r['scene'] for r in rows])
# cut candidates: scene score peaks
cuts=[i for i in range(1,N) if scene[i]>0.25]
# cluster consecutive
cl=[]; 
for c in cuts:
    if cl and c-cl[-1][-1]<=6: cl[-1].append(c)
    else: cl.append([c])
out=[]
for g in cl:
    kind='hard cut' if len(g)<=2 else f'transition ~{g[-1]-g[0]+1}f'
    out.append((g[0],g[-1],kind,float(scene[g].max())))
with open(f'{D}/data/cuts.txt','w') as fo:
    fo.write(f"frames {N} dur {N/30:.2f}s | static frames (diff<0.05): {int((diff[1:]<0.05).sum())} | median diff {np.median(diff[1:]):.2f}\n")
    last=0
    for a,b,k,s in out:
        fo.write(f"f{a:4d}-{b:4d} t={a/30:6.2f}s  {k:18s} peak {s:.2f}  shot_len_before {(a-last)/30:5.2f}s\n"); last=b
    fo.write(f"last shot {(N-last)/30:.2f}s | events {len(out)} | avg spacing {N/30/max(1,len(out)+1):.2f}s\n")
    # luma/sat per second
    fo.write("sec: luma_median sat diff_mean\n")
    for s in range(0,int(N/30)+1):
        seg=rows[s*30:(s+1)*30]
        if seg: fo.write(f"{s:3d}: {np.mean([r['luma'] for r in seg]):6.1f} {np.mean([r['sat'] for r in seg]):.2f} {np.mean([r['diff'] for r in seg]):5.2f}\n")
print(open(f'{D}/data/cuts.txt').read())
