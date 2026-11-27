import sys,cv2,numpy as np
D=sys.argv[1]
cap=cv2.VideoCapture(f'{D}/src/reel.mp4')
def fr(n):
    cap.set(cv2.CAP_PROP_POS_FRAMES,n); ok,im=cap.read(); return im
for n,(x,y,w,h),lab in [(1070,(200,500,256,256),'blank CTA paper'),(200,(200,150,256,256),'sky'),(745,(300,700,256,256),'slate'),(306,(300,800,256,256),'grid paper'),(30,(100,50,256,256),'storm sky'),(960,(250,500,256,256),'microscope')]:
    g=cv2.cvtColor(fr(n),cv2.COLOR_BGR2GRAY)[y:y+h,x:x+w].astype(float)
    g=g-cv2.GaussianBlur(g,(0,0),6)  # high-pass
    F=np.abs(np.fft.fftshift(np.fft.fft2(g*np.hanning(h)[:,None]*np.hanning(w)[None,:])))
    c=h//2; F[c-6:c+7,c-6:c+7]=0
    idx=np.argsort(F.ravel())[::-1][:6]
    pk=[(int(i//w)-c,int(i%w)-c) for i in idx]
    per=[ (round(w/np.hypot(a,b),2), round(np.degrees(np.arctan2(a,b)),0)) for a,b in pk]
    ratio=F.ravel()[idx[0]]/np.median(F[F>0])
    print(f"f{n} {lab:16s} hp-std {g.std():5.2f}  top peaks (period px, angle): {per}  peak/median {ratio:.1f}")
# frame-to-frame grain: difference of two consecutive static-ish frames in flat area
a=cv2.cvtColor(fr(1068),cv2.COLOR_BGR2GRAY).astype(float); b=cv2.cvtColor(fr(1069),cv2.COLOR_BGR2GRAY).astype(float)
print("f1068->1069 blank paper temporal diff std:",np.std((a-b)[400:800,100:600]).round(2))
