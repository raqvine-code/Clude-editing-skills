import cv2, numpy as np, sys
R=sys.argv[1]
ed=lambda n: cv2.imread(R+'/ed/%04d.jpg'%n)
raw=lambda n: cv2.imread(R+'/raw/%04d.jpg'%n)
s,tx,ty=1.302,-7,-5
M=np.float32([[s,0,tx],[0,s,ty]])
warp=lambda img: cv2.warpAffine(img,M,(392,696),flags=cv2.INTER_CUBIC)
valid=warp(np.full((550,232,3),255,np.uint8))[:,:,0]>250
valid[:,285:]=False; valid[:8]=False
A=[];B=[]
for f in [130,160,340,660,700,760,800,960,1000,1040]:
    e=ed(f); w=warp(raw(f)); m=valid.copy()
    # exclude caption pixels: large diff
    d=np.abs(e.astype(int)-w.astype(int)).sum(2); m&=d<60
    m[400:560,:]=False
    A.append(w[m]); B.append(e[m])
A=np.concatenate(A).astype(float); B=np.concatenate(B).astype(float)
print('n px',len(A))
for i,c in enumerate('BGR'):
    print(c,'raw mean %.1f ed mean %.1f'%(A[:,i].mean(),B[:,i].mean()), ' pct raw',np.percentile(A[:,i],[2,25,50,75,98]).round(0),' ed',np.percentile(B[:,i],[2,25,50,75,98]).round(0))
    p=np.polyfit(A[:,i],B[:,i],1); print('   linear fit ed=%.3f*raw%+.1f'%(p[0],p[1]))
# tone curve: binned luma
la=A@[0.114,0.587,0.299]; lb=B@[0.114,0.587,0.299]
print('luma curve (raw->ed):')
for lo in range(0,250,16):
    k=(la>=lo)&(la<lo+16)
    if k.sum()>200: print('  %3d-%3d  ed %.1f  (n=%d)'%(lo,lo+16,lb[k].mean(),k.sum()))
def sat(X):
    mx=X.max(1); mn=X.min(1); return np.where(mx>0,(mx-mn)/np.maximum(mx,1),0)
print('sat raw %.3f ed %.3f'%(sat(A).mean(),sat(B).mean()))
# example hex of wall slats and skin
def hx(v): return '#%02x%02x%02x'%(int(v[2]),int(v[1]),int(v[0]))
e=ed(660); w=warp(raw(660))
for name,(y,x) in {'wall slat':(60,250),'skin cheek':(240,150),'shirt':(600,180),'plant':(200,30)}.items():
    print(name,'raw',hx(w[y-4:y+4,x-4:x+4].reshape(-1,3).mean(0)),'ed',hx(e[y-4:y+4,x-4:x+4].reshape(-1,3).mean(0)))
# radial vignette check: ratio of ed/raw luma vs position
le=cv2.cvtColor(e,cv2.COLOR_BGR2GRAY).astype(float)+1; lw=cv2.cvtColor(w,cv2.COLOR_BGR2GRAY).astype(float)+1
for (y0,y1,x0,x1,n) in [(10,100,10,90,'top-left'),(300,380,120,200,'centre'),(600,690,10,90,'bottom-left'),(10,100,200,280,'top-mid')]:
    print('ratio ed/raw',n,'%.3f'%(le[y0:y1,x0:x1].mean()/lw[y0:y1,x0:x1].mean()))
# sharpness: laplacian var
print('lap var raw %.1f ed %.1f'%(cv2.Laplacian(cv2.cvtColor(w,cv2.COLOR_BGR2GRAY),cv2.CV_64F)[valid].var(), cv2.Laplacian(cv2.cvtColor(e,cv2.COLOR_BGR2GRAY),cv2.CV_64F)[valid].var()))
