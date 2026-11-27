import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import stft, find_peaks
D=sys.argv[1]
sr,x=wavfile.read(f'{D}/data/a44.wav'); x=x.astype(np.float32)/32768.0
L,R=x[:,0],x[:,1]; m=(L+R)/2; side=(L-R)/2
hop=sr//30
f,t,Z=stft(m,sr,nperseg=2048,noverlap=2048-hop,boundary=None,padded=False); A=np.abs(Z)
fs,ts,Zs=stft(side,sr,nperseg=2048,noverlap=2048-hop,boundary=None,padded=False); As=np.abs(Zs)
def band(A,lo,hi):
    i=(f>=lo)&(f<hi); return 20*np.log10(np.sqrt((A[i]**2).mean(axis=0))+1e-7)
sub=band(A,20,90); low=band(A,90,300); vo=band(A,300,3400); hi=band(A,5000,16000); sideall=band(As,200,16000); midall=band(A,200,16000)
fr=(t*30).round().astype(int)   # frame index of window centre
print("frames:",len(t), "t0",t[0])
# 1) per-frame table compact: print every frame's hi and sub around transitions
def flux(lo,hi_):
    i=(f>=lo)&(f<hi_); S=np.log1p(80*A[i]); fl=np.maximum(0,np.diff(S,axis=1)).sum(axis=0); return np.r_[0,fl]/ (fl.max()+1e-9)
fh=flux(5000,16000); fl_=flux(20,120); fa=flux(300,16000)
pk,_=find_peaks(fh,height=0.18,distance=3)
print("HI-band transient frames (flux>0.18): "+" ".join(f"{fr[k]}({fh[k]:.2f})" for k in pk))
pk,_=find_peaks(fl_,height=0.30,distance=4)
print("SUB transient frames (flux>0.30): "+" ".join(f"{fr[k]}({fl_[k]:.2f})" for k in pk))
# 2) sub-bass envelope: segments where sub > -24 dB
on=sub>-24; segs=[]; s=None
for i,v in enumerate(on):
    if v and s is None: s=i
    if (not v) and s is not None:
        if i-s>=4: segs.append((fr[s],fr[i-1],float(sub[s:i].max())))
        s=None
print("SUB-bass loud segments (>-24dB, frames a-b, peak dB):",[(a,b,round(p,1)) for a,b,p in segs])
# 3) hi-band sustained (whoosh) segments: hi > -62 dB for >=4 frames
on=hi>-60; segs=[]; s=None
for i,v in enumerate(on):
    if v and s is None: s=i
    if (not v) and s is not None:
        if i-s>=3: segs.append((fr[s],fr[i-1],float(hi[s:i].max())))
        s=None
print("HI-band loud segments (>-60dB):",[(a,b,round(p,1)) for a,b,p in segs])
# 4) VO activity: vo band > -48 dB; list speech segments in frames
on=vo>-46; segs=[]; s=None
for i,v in enumerate(on):
    if v and s is None: s=i
    if (not v) and s is not None:
        if i-s>=2: segs.append((int(fr[s]),int(fr[i-1])))
        s=None
# merge gaps <=3 frames
mg=[]
for a,b in segs:
    if mg and a-mg[-1][1]<=4: mg[-1][1]=b
    else: mg.append([a,b])
print("VO-band active segments (frames):",[(a,b) for a,b in mg])
gaps=[(mg[i][1]+1,mg[i+1][0]-1) for i in range(len(mg)-1) if mg[i+1][0]-mg[i][1]>6]
print("VO gaps > 6 frames:",[(a,b,round((b-a+1)/30,2)) for a,b in gaps])
# 5) stereo width per second
print("side-mid dB per 2s:", " ".join(f"{(sideall[(t>=s)&(t<s+2)].mean()-midall[(t>=s)&(t<s+2)].mean()):.0f}" for s in np.arange(0,42,2)))
# 6) spectrum peaks in VO gaps (music/drone?)
f2,t2,Z2=stft(m,sr,nperseg=8192,noverlap=8192-441); A2=np.abs(Z2)
for a,b in gaps:
    i=(t2>=a/30+0.05)&(t2<b/30-0.05)
    if i.sum()<3: continue
    sp=A2[:,i].mean(axis=1); pk=np.argsort(sp)[::-1]; out=[]
    for k in pk:
        if f2[k]>30 and all(abs(f2[k]-o)>0.06*o for o in out): out.append(f2[k])
        if len(out)==7: break
    lvl=20*np.log10(np.sqrt((m[int(a/30*sr):int(b/30*sr)]**2).mean())+1e-9)
    print(f"gap f{a}-{b} ({a/30:.2f}-{b/30:.2f}s) rms {lvl:.1f} dB peaks Hz {[int(o) for o in sorted(out)]}")
# 7) overall: VO level vs bed level
vo_on=np.zeros(len(t),bool)
for a,b in mg: vo_on[(fr>=a)&(fr<=b)]=True
rmsf=np.array([np.sqrt((m[int(k*hop):int(k*hop)+hop]**2).mean()) for k in range(len(t))]); db=20*np.log10(rmsf+1e-9)
print("median level during VO %.1f dB, during gaps %.1f dB"%(np.median(db[vo_on]),np.median(db[~vo_on])))
print("peak sample abs:",float(np.abs(x).max()), "clipped samples (>=0.999):", int((np.abs(x)>=0.999).sum()))
np.save(f'{D}/data/aud_frames.npy',np.vstack([fr,sub,low,vo,hi,fh,fl_]))
