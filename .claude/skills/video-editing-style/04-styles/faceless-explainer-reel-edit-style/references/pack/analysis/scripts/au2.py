import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import stft
sr, x = wavfile.read(sys.argv[1]); x = x.astype(np.float32)/32768.0; m=x.mean(axis=1)
f,t,Z = stft(m, sr, nperseg=4096, noverlap=4096-441); A=np.abs(Z)
# gaps between VO phrases: dominant spectral peaks
gaps=[(1.95,2.55),(4.95,5.3),(7.6,8.0),(9.45,9.98),(13.2,13.6),(14.5,14.82),(17.7,18.2),(19.3,19.8),(21.55,21.85),(23.3,23.88),(27.3,27.66),(29.55,29.85)]
for a,b in gaps:
    i=(t>=a)&(t<b); sp=A[:,i].mean(axis=1)
    lvl=20*np.log10(np.sqrt((m[int(a*sr):int(b*sr)]**2).mean())+1e-9)
    pk=np.argsort(sp)[::-1]; out=[]
    for k in pk:
        if all(abs(f[k]-o)>25 for o in out): out.append(f[k])
        if len(out)==6: break
    cent=(f*sp).sum()/sp.sum()
    print(f"gap {a:5.2f}-{b:5.2f} rms {lvl:6.1f} dB centroid {cent:6.0f}Hz peaks {[int(o) for o in sorted(out)]}")
# fine band envelope around transitions
def env(lo,hi):
    i=(f>=lo)&(f<hi); return 20*np.log10(A[i].mean(axis=0)+1e-7)
sub=env(20,90); air=env(5000,16000); mid=env(300,3000)
for c in [2.667,5.333,8.0,11.03,11.33,14.87,15.17,18.1,19.8,22.2,23.5,23.8,28.1]:
    print(f"\ncut {c:.2f}: t / sub / mid / air")
    for s in np.arange(c-0.4,c+0.45,0.1):
        i=(t>=s)&(t<s+0.1); print(f"  {s:6.2f} {sub[i].mean():6.1f} {mid[i].mean():6.1f} {air[i].mean():6.1f}")
