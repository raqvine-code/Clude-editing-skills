import sys, glob, json, numpy as np, cv2
R=sys.argv[1]
def series(d):
    files=sorted(glob.glob(f'{R}/{d}/*.jpg')); prev=None; ph=None; out=[]
    for i,f in enumerate(files):
        im=cv2.imread(f); g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32)
        hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
        h=cv2.calcHist([hsv],[0,1,2],None,[8,8,8],[0,180,0,256,0,256]).flatten(); h/=h.sum()
        d_=float(np.abs(g-prev).mean()) if prev is not None else 0.0
        hd=float(np.abs(h-ph).sum()/2) if ph is not None else 0.0
        out.append(dict(f=i,diff=d_,hist=hd,luma=float(np.median(g)),lmean=float(g.mean()),sat=float(hsv[...,1].mean()/255)))
        prev=g; ph=h
    return out
ed=series('ed'); raw=series('raw')
json.dump(dict(ed=ed,raw=raw),open(f'{R}/data/panel_frames.json','w'))
N=len(ed)
def cuts(s,name,dthr,hthr):
    d=np.array([x['diff'] for x in s]); h=np.array([x['hist'] for x in s])
    # local-contrast: spike vs median of neighbours
    c=[]
    for i in range(2,N-2):
        nb=np.median(np.r_[d[max(0,i-6):i],d[i+1:i+7]])
        if (d[i]>dthr and d[i]>3.0*nb) or h[i]>hthr: c.append(i)
    print(name,'static frames(diff<0.15):',int((d[1:]<0.15).sum()),'median diff %.2f'%np.median(d[1:]))
    cl=[]
    for x in c:
        if cl and x-cl[-1][-1]<=3: cl[-1].append(x)
        else: cl.append([x])
    last=0
    for g in cl:
        print(f"  {name} f{g[0]:4d}-{g[-1]:4d} t={g[0]/30:6.2f}s len_before {(g[0]-last)/30:5.2f}s  diff {d[g].max():5.1f} hist {h[g].max():.2f}")
        last=g[0]
    return cl
ce=cuts(ed,'ED',6.0,0.35); cr=cuts(raw,'RAW',6.0,0.35)
# per-second table for ED
print('sec: ED luma_med sat diff | RAW diff')
for s in range(0,N//30+1):
    a=ed[s*30:(s+1)*30]; b=raw[s*30:(s+1)*30]
    if a: print(f"{s:3d}: {np.mean([x['luma'] for x in a]):6.1f} {np.mean([x['sat'] for x in a]):.2f} {np.mean([x['diff'] for x in a]):5.2f} | {np.mean([x['diff'] for x in b]):5.2f}")
