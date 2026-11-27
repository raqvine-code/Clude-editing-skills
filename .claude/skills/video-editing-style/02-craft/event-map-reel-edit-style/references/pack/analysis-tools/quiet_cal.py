import sys, cv2, numpy as np
def act(video, crop=None, lag=3, width=360):
    cap=cv2.VideoCapture(video); buf=[]; a=[]
    while True:
        ok,im=cap.read()
        if not ok: break
        if crop: w,h,x,y=crop; im=im[y:y+h,x:x+w]
        h0,w0=im.shape[:2]; im=cv2.resize(im,(width,int(round(h0*width/w0))),interpolation=cv2.INTER_AREA)
        g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32); buf.append(g)
        if len(buf)>lag:
            d=np.abs(g-buf[-1-lag]); b=cv2.resize(d,(6,10),interpolation=cv2.INTER_AREA); a.append(float(b.max()))
        else: a.append(0.0)
        if len(buf)>lag+1: buf.pop(0)
    return np.array(a)
for name,video,crop in [("r0","r0/src/reel.mp4",None),("r1","r1/src/reel.mp4",None),("r2","r2/src/reel.mp4",None),("r3","r3/src/reel.mp4",None),("r4c","r4/src/reel.mp4",(392,696,285,291)),("r4full","r4/src/reel.mp4",None)]:
    a=act(video,crop); n=len(a); out=[f"{name}: p10 {np.percentile(a,10):5.1f} p50 {np.percentile(a,50):5.1f} p90 {np.percentile(a,90):5.1f}"]
    for th in (3,5,8,12):
        q=a<th; best=cur=0; start=0; bs=0
        for i,v in enumerate(q):
            if v:
                if cur==0: start=i
                cur+=1
                if cur>best: best=cur; bs=start
            else: cur=0
        out.append(f"θ{th}: quiet {100*q.mean():4.1f}% longest {best/30:4.2f}s@{bs/30:5.1f}")
    print(" | ".join(out))
