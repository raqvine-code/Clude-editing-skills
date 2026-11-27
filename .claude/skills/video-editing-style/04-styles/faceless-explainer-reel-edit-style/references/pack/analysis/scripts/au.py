import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import stft, find_peaks
sr, x = wavfile.read(sys.argv[1]); x = x.astype(np.float32)/32768.0
L,R = x[:,0], x[:,1]; m = (L+R)/2; side=(L-R)/2
print("stereo side/mid rms ratio: %.3f" % (np.sqrt((side**2).mean())/np.sqrt((m**2).mean())))
f,t,Z = stft(m, sr, nperseg=2048, noverlap=2048-441)  # 10ms hop
A = np.abs(Z)
def band(lo,hi): 
    i=(f>=lo)&(f<hi); return 20*np.log10(A[i].mean(axis=0)+1e-7)
bands = {"sub(20-80)":band(20,80),"bass(80-250)":band(80,250),"mid(250-2k)":band(250,2000),"pres(2k-6k)":band(2000,6000),"air(6k-16k)":band(6000,16000)}
# per 0.25s table
print("t     " + "  ".join(f"{k:>12}" for k in bands))
for s in np.arange(0,30,0.5):
    i=(t>=s)&(t<s+0.5)
    print(f"{s:5.1f} " + "  ".join(f"{bands[k][i].mean():12.1f}" for k in bands))
# onsets per band via flux
def onsets(lo,hi,name,thr):
    i=(f>=lo)&(f<hi); S=np.log1p(50*A[i]); fl=np.maximum(0,np.diff(S,axis=1)).sum(axis=0); fl/=fl.max()
    p,_=find_peaks(fl,height=thr,distance=8)
    print(name, " ".join(f"{t[k+1]:.2f}" for k in p))
    return t[p+1]
lo=onsets(20,150,"LOW onsets:",0.30)
hi=onsets(6000,16000,"AIR onsets:",0.35)
# tempo estimate from low-band onset envelope autocorrelation
i=(f>=20)&(f<200); S=np.log1p(50*A[i]); fl=np.maximum(0,np.diff(S,axis=1)).sum(axis=0); fl-=fl.mean()
ac=np.correlate(fl,fl,'full')[len(fl)-1:]
lags=np.arange(len(ac)); bpm=60/(lags[30:150]*0.01)
best=np.argsort(ac[30:150])[::-1][:5]
print("tempo candidates:", [(round(float(bpm[b]),1), round(float(ac[30+b]/ac[0]),3)) for b in best])
# overall rms envelope & silence
rms=np.array([np.sqrt((m[int(s*sr):int((s+0.1)*sr)]**2).mean()) for s in np.arange(0,29.9,0.1)])
db=20*np.log10(rms+1e-7); print("rms dB min/median/max: %.1f %.1f %.1f"%(db.min(),np.median(db),db.max()))
print("quiet(<-35dB) windows:", [round(float(s),1) for s,d in zip(np.arange(0,29.9,0.1),db) if d<-35])
