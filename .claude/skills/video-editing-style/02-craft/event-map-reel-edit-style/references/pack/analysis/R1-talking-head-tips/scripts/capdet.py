# Count near-white neutral pixels in caption band per frame; print frames where count jumps (new word) or drops (clear).
import cv2, numpy as np, sys, json
V=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]); thr=int(sys.argv[4]) if len(sys.argv)>4 else 225
cap=cv2.VideoCapture(V); cap.set(cv2.CAP_PROP_POS_FRAMES,a)
cnt=[]
for f in range(a,b+1):
    ok,im=cap.read()
    if not ok: break
    H,W=im.shape[:2]; band=im[int(H*0.40):int(H*0.85)].astype(np.int16)
    mn=band.min(2); mx=band.max(2)
    m=(mn>thr)&((mx-mn)<18)
    cnt.append(int(m.sum()))
cnt=np.array(cnt)
out=[]
for i in range(1,len(cnt)):
    d=cnt[i]-cnt[i-1]
    if abs(d)>max(150,0.25*cnt[i-1]): out.append("%d:%+d(%d)"%(a+i,d,cnt[i]))
print(" ".join(out))
