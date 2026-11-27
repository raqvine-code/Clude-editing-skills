import numpy as np, sys
from scipy.io import wavfile
from scipy.signal import stft
sr,a=wavfile.read(sys.argv[1]); a=a.astype(float)/32768
L,R=a[:,0],a[:,1]; S=(L-R)/2; Mid=(L+R)/2
f,t,Z=stft(S,sr,nperseg=8192,noverlap=8192-2400)
P=np.abs(Z)**2
def band(lo,hi): k=(f>=lo)&(f<hi); return 10*np.log10(P[k].sum(0)+1e-12)
lo=band(30,150); md=band(150,1500); hi=band(1500,8000)
print('side level per 1s (30-150 | 150-1.5k | 1.5-8k dB):')
for s in range(0,36,1):
    k=(t>=s)&(t<s+1)
    if k.any(): print(' %2ds  %6.1f %6.1f %6.1f'%(s,lo[k].mean(),md[k].mean(),hi[k].mean()))
# tonal persistence: in 150-1500 Hz, fraction of energy in top 10 bins per frame, averaged per 2 s
k=(f>=80)&(f<1500)
Q=P[k]
peak=np.sort(Q,0)[-8:].sum(0)/Q.sum(0)
print('side tonal peak ratio per 2s:',[round(peak[(t>=s)&(t<s+2)].mean(),2) for s in range(0,36,2)])
# dominant side pitch classes over whole clip (chroma)
fr=f[k]; pc=(np.round(12*np.log2(fr/440))+9)%12
ch=np.array([Q[pc==i].sum() for i in range(12)]); ch/=ch.sum()
names='C C# D D# E F F# G G# A A# B'.split()
print('side chroma:',' '.join('%s%.2f'%(names[i],ch[i]) for i in np.argsort(-ch)[:6]))
