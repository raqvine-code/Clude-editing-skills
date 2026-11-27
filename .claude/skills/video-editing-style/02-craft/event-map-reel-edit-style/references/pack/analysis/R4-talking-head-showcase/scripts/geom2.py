import cv2, numpy as np, sys
R=sys.argv[1]
cap=cv2.VideoCapture(R+'/src/reel.mp4')
cap.set(cv2.CAP_PROP_POS_FRAMES,660); ok,f=cap.read(); f=f.astype(int)
bg=230; d=np.abs(f-bg).sum(2)>40
c=d[:,600]; ys=np.where(c[285:1050])[0]+285; print('EDITED panel y',ys.min(),ys.max())
c=d[:,100]; ys=np.where(c)[0]; print('RAW panel y (x=100)',ys.min(),ys.max())
r=d[600,:]; print('row600 x first/last',np.where(r)[0].min(),np.where(r)[0].max())
# RAW label
sub=(f[290:345,100:280].sum(2)<200); ys,xs=np.where(sub); print('RAW label x',100+xs.min(),100+xs.max(),'y',290+ys.min(),290+ys.max())
# DM and FOR WORK separately
sub=(f[1050:1170,150:370].sum(2)<200); ys,xs=np.where(sub); print('DM x',150+xs.min(),150+xs.max(),'y',1050+ys.min(),1050+ys.max())
sub=(f[1050:1170,370:600].sum(2)<200); ys,xs=np.where(sub); print('FOR WORK x',370+xs.min(),370+xs.max(),'y',1050+ys.min(),1050+ys.max())
# row profile of FOR WORK to split lines
prof=sub.sum(1); rows=np.where(prof>0)[0]; gaps=np.where(np.diff(rows)>1)[0]; print('FORWORK row groups',[(1050+rows[0], 1050+rows[g]) for g in gaps][:1], [1050+rows[g+1] for g in gaps], 1050+rows[-1])
# RAW panel corner radius
for k in range(0,16,3):
    r=d[365+k,40:80]; xs=np.where(r)[0]; print('RAW row',365+k,'first x',40+xs.min() if len(xs) else None)
# EDITED panel shadow? check pixels just outside right edge
print('outside right edge x680..690 at y640',f[640,678:692,0])
print('below edited panel y 985..1000 at x500',f[984:1000,500,0])
# Is the RAW panel overlapped by the EDITED: compare raw region right edge at x 280-286
print('row 640 x 278..292',f[640,278:292,0])
