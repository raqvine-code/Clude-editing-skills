import cv2, numpy as np, sys
R=sys.argv[1]
cap=cv2.VideoCapture(R+'/src/reel.mp4')
def frame(n):
    cap.set(cv2.CAP_PROP_POS_FRAMES,n); ok,f=cap.read(); return f
f=frame(660).astype(int)
bg=np.median(f[50:150,50:150].reshape(-1,3),axis=0); print('bg BGR',bg, 'hex #%02x%02x%02x'%(int(bg[2]),int(bg[1]),int(bg[0])))
d=np.abs(f-bg).sum(2)>40
# EDITED panel: column 500
col=d[:,500]; ys=np.where(col)[0]; print('col500 non-bg y',ys.min(),ys.max())
row=d[640,:]; xs=np.where(row)[0]; print('row640 non-bg x',xs.min(),xs.max())
# find edges of edited panel at row 640 right side
runs=np.diff(row.astype(int)); print('row640 transitions',np.where(runs!=0)[0])
for x in [60,150,250]:
    ys=np.where(d[:,x])[0]; print('col',x,'y range',ys.min(),ys.max())
# label text
for name,(y0,y1,x0,x1) in {'RAW':(280,345,40,300),'EDITED':(230,290,300,700),'DM':(1050,1170,100,650)}.items():
    sub=(f[y0:y1,x0:x1].sum(2)<200)
    ys,xs=np.where(sub)
    if len(ys): print(name,'ink bbox x',x0+xs.min(),x0+xs.max(),'y',y0+ys.min(),y0+ys.max(),'h',ys.max()-ys.min()+1)
# panel corner radius: check EDITED top-left corner
for k in range(0,20,2):
    r=d[291+k, 280:320]; xs=np.where(r)[0]; print('row',291+k,'first non-bg x', 280+xs.min() if len(xs) else None)
# grain/noise in background
print('bg std',f[50:150,50:150].std(axis=(0,1)))
# DM text colour
sub=f[1060:1160,160:360]; dark=sub[sub.sum(2)<150]; print('DM ink BGR median',np.median(dark,axis=0))
