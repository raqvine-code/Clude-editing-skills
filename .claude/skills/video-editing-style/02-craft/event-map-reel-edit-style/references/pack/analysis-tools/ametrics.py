# usage: python3 -I ametrics.py <reel_dir>
import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import stft, find_peaks
D=sys.argv[1]
sr,x=wavfile.read(f'{D}/data/a44.wav'); x=x.astype(np.float32)/32768.0
L,R=x[:,0],x[:,1]; m=(L+R)/2; side=(L-R)/2
o=[]
o.append("stereo side/mid rms ratio: %.3f"%(np.sqrt((side**2).mean())/np.sqrt((m**2).mean()+1e-12)))
f,t,Z=stft(m,sr,nperseg=2048,noverlap=2048-441); A=np.abs(Z)
def band(lo,hi):
    i=(f>=lo)&(f<hi); return 20*np.log10(A[i].mean(axis=0)+1e-7)
B={"sub20-80":band(20,80),"bass80-250":band(80,250),"mid250-2k":band(250,2000),"pres2k-6k":band(2000,6000),"air6k-16k":band(6000,16000)}
dur=len(m)/sr
o.append("t      "+"  ".join(f"{k:>10}" for k in B))
for s in np.arange(0,dur,0.5):
    i=(t>=s)&(t<s+0.5)
    if i.any(): o.append(f"{s:5.1f}  "+"  ".join(f"{B[k][i].mean():10.1f}" for k in B))
def ons(lo,hi,name,thr,dist=8):
    i=(f>=lo)&(f<hi); S=np.log1p(50*A[i]); fl=np.maximum(0,np.diff(S,axis=1)).sum(axis=0); fl/=fl.max()+1e-9
    p,_=find_peaks(fl,height=thr,distance=dist)
    o.append(name+" "+" ".join(f"{t[k+1]:.2f}" for k in p)); return fl
fl_low=ons(20,150,"LOW onsets(>0.35):",0.35)
ons(6000,16000,"AIR onsets(>0.35):",0.35)
fl_all=ons(20,16000,"FULL onsets(>0.4):",0.40)
# tempo from full-band flux autocorrelation (60-200 bpm)
for nm,fl in (("low",fl_low),("full",fl_all)):
    e=fl-fl.mean(); ac=np.correlate(e,e,'full')[len(e)-1:]; lags=np.arange(30,101)  # 0.30-1.00 s
    best=lags[np.argsort(ac[lags])[::-1][:4]]
    o.append(f"tempo candidates ({nm}): "+", ".join(f"{60/(b*0.01):.0f}bpm(r={ac[b]/ac[0]:.2f})" for b in best))
rms=np.array([np.sqrt((m[int(s*sr):int((s+0.1)*sr)]**2).mean()) for s in np.arange(0,dur-0.1,0.1)])
db=20*np.log10(rms+1e-7); o.append("rms dB min/median/max: %.1f %.1f %.1f"%(db.min(),np.median(db),db.max()))
o.append("quiet(<-40dB) 0.1s windows: "+str([round(float(s),1) for s,d in zip(np.arange(0,dur-0.1,0.1),db) if d<-40]))
# spectral flatness/tonality in mid band as music indicator, per second
i=(f>=200)&(f<4000); P=A[i]**2+1e-12
flat=np.exp(np.log(P).mean(axis=0))/P.mean(axis=0)
o.append("mid-band spectral flatness per 2s (low=tonal): "+" ".join(f"{flat[(t>=s)&(t<s+2)].mean():.3f}" for s in np.arange(0,dur,2)))
open(f'{D}/data/audio.txt','w').write("\n".join(o)); print("\n".join(o[:1]+o[-9:]))
