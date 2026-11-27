import sys,numpy as np
from scipy.io import wavfile
D=sys.argv[1]
sr,x=wavfile.read(f'{D}/data/a44.wav'); x=x.astype(np.float32)/32768; mid=x.mean(1); side=(x[:,0]-x[:,1])/2
def spec(a,b,sig=mid):
    s=sig[int(a*sr):int(b*sr)]; s=s*np.hanning(len(s)); F=np.abs(np.fft.rfft(s,n=1<<16)); f=np.fft.rfftfreq(1<<16,1/sr); return f,F
for a,b in [(6.86,7.22),(9.42,9.80),(20.22,20.44),(30.10,30.56),(31.90,32.38),(40.45,40.85)]:
    f,F=spec(a,b); band=(f>30)&(f<1500); idx=np.where(band)[0]; top=idx[np.argsort(F[idx])[::-1]]
    out=[]
    for k in top:
        if all(abs(f[k]-o)>8 for o in out): out.append(f[k])
        if len(out)==6: break
    e_lo=20*np.log10(np.sqrt((F[(f>30)&(f<300)]**2).sum())+1e-9); e_hi=20*np.log10(np.sqrt((F[(f>2000)&(f<8000)]**2).sum())+1e-9)
    print(f"gap {a:5.2f}-{b:5.2f}: peaks Hz {sorted(int(o) for o in out)}  low(30-300) {e_lo:.1f}  hi(2-8k) {e_hi:.1f}")
# overall level of mid in 0-0.05s windows below VO: 5th percentile per 2 s block
hop=int(0.05*sr)
env=np.array([20*np.log10(np.sqrt((mid[i:i+hop]**2).mean())+1e-9) for i in range(0,len(mid)-hop,hop)])
print("mid 50ms floor (p5) per 4 s:", [round(float(np.percentile(env[int(i/0.05):int((i+4)/0.05)],5)),1) for i in range(0,40,4)])
