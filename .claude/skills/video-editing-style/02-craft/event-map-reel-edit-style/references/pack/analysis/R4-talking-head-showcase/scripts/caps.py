import cv2, numpy as np, sys
R=sys.argv[1]
ed=lambda n: cv2.imread(R+'/ed/%04d.jpg'%n)
raw=lambda n: cv2.imread(R+'/raw/%04d.jpg'%n)
s,tx,ty=1.302,-7,-5
M=np.float32([[s,0,tx],[0,s,ty]])
warp=lambda img: cv2.warpAffine(img,M,(392,696),flags=cv2.INTER_CUBIC)
valid=warp(np.full((550,232,3),255,np.uint8))[:,:,0]>250; valid[:,284:]=False
hx=lambda v:'#%02x%02x%02x'%(int(v[2]),int(v[1]),int(v[0]))
frames=[int(a) for a in sys.argv[2].split(',')]
y0,y1=int(sys.argv[3]),int(sys.argv[4])
for f in frames:
    e=ed(f); hsv=cv2.cvtColor(e,cv2.COLOR_BGR2HSV).astype(int)
    H,S,V=hsv[...,0],hsv[...,1],hsv[...,2]
    mn=e.min(2).astype(int); mx=e.max(2).astype(int)
    white=(mn>200)&(mx-mn<45)
    orange=(H>=8)&(H<=30)&(S>120)&(V>170)
    red=((H<=7)|(H>=170))&(S>150)&(V>110)
    diff=np.abs(e.astype(int)-warp(raw(f)).astype(int)).sum(2)>70
    gate=np.where(valid,diff,True)
    band=np.zeros_like(white); band[y0:y1]=True
    out=[]
    for name,m in [('white',white),('orange',orange),('red',red)]:
        m=m&gate&band
        m=cv2.morphologyEx(m.astype(np.uint8),cv2.MORPH_OPEN,np.ones((2,2),np.uint8))>0
        rows=np.where(m.sum(1)>=3)[0]
        if len(rows)<3: continue
        # split into line groups by gaps>3
        groups=[]; st=rows[0]; pr=rows[0]
        for r in rows[1:]:
            if r-pr>3: groups.append((st,pr)); st=r
            pr=r
        groups.append((st,pr))
        for a,b in groups:
            if b-a<4: continue
            sub=m[a:b+1]; cols=np.where(sub.sum(0)>0)[0]
            px=e[a:b+1][sub]
            out.append('%s y%d-%d h%d x%d-%d w%d(%.0f%%) c=%s'%(name,a,b,b-a+1,cols.min(),cols.max(),cols.max()-cols.min()+1,100*(cols.max()-cols.min()+1)/392,hx(np.median(px,0))))
    print(f, ' | '.join(out))
