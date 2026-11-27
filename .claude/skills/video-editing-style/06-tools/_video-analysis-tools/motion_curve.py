"""usage: python -I motion_curve.py <ffmpeg path> <video>. Frame-difference at 60 fps, luma and saturation per second, biggest jumps (= hard cuts). (ref69, 2026-10-09)"""
import sys, subprocess, numpy as np
ff, vid = sys.argv[1], sys.argv[2]
W,H=135,240
p=subprocess.Popen([ff,'-v','error','-i',vid,'-vf','fps=60,scale=%d:%d,format=rgb24'%(W,H),'-f','rawvideo','-'],stdout=subprocess.PIPE)
prev=None; d=[]; luma=[]; sat=[]
while True:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    a=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(np.float32)
    g=a.mean(2); luma.append(g.mean()); 
    mx=a.max(2); mn=a.min(2); sat.append(np.mean((mx-mn)/(mx+1e-3)))
    if prev is not None: d.append(np.mean(np.abs(g-prev)))
    prev=g
d=np.array(d); luma=np.array(luma); sat=np.array(sat)
print('frames',len(luma))
# hard cuts: large jump
idx=np.argsort(-d)[:8]; print('biggest frame jumps (t, diff):',sorted([(round((i+1)/60,3),round(float(d[i]),1)) for i in idx]))
# per 0.5 s average motion
print('motion per 0.5s:',[round(float(d[int(i*30):int((i+1)*30)].mean()),1) for i in range(int(len(d)/30))])
print('luma per 1s (0-255):',[round(float(luma[i*60:(i+1)*60].mean()),0) for i in range(int(len(luma)/60)+1)])
print('sat per 1s (0-1):',[round(float(sat[i*60:(i+1)*60].mean()),2) for i in range(int(len(sat)/60)+1)])
pass
