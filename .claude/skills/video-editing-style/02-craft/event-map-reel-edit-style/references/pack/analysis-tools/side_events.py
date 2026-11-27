# Side-channel (L-R) event detector: isolates stereo SFX/music from centred voice.
# usage: python3 -I side_events.py <reel_dir>
import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import stft, find_peaks
D=sys.argv[1]
sr,x=wavfile.read(f'{D}/data/a44.wav'); x=x.astype(np.float32)/32768.0
mid=(x[:,0]+x[:,1])/2; side=(x[:,0]-x[:,1])/2
hop=441
f,t,Zs=stft(side,sr,nperseg=2048,noverlap=2048-hop); As=np.abs(Zs)
_,_,Zm=stft(mid,sr,nperseg=2048,noverlap=2048-hop); Am=np.abs(Zm)
def db(a): return 20*np.log10(a+1e-9)
env=np.sqrt((As**2).sum(axis=0)); envdb=db(env)
menv=np.sqrt((Am**2).sum(axis=0))
print(f"side rms {db(np.sqrt((side**2).mean())):.1f} dBFS | mid rms {db(np.sqrt((mid**2).mean())):.1f} dBFS | side floor(p10) {np.percentile(envdb,10):.1f} median {np.median(envdb):.1f} p95 {np.percentile(envdb,95):.1f}")
# events: side envelope rising > 8 dB above running median (2 s window)
from scipy.ndimage import median_filter
base=median_filter(envdb,size=201,mode='nearest')
above=envdb-base
pk,pr=find_peaks(above,height=7,distance=12,prominence=5)
cent=(f[:,None]*As).sum(axis=0)/(As.sum(axis=0)+1e-9)
out=[]
for p in pk:
    # duration: contiguous frames around p with above>3
    a=p
    while a>0 and above[a-1]>3: a-=1
    b=p
    while b<len(above)-1 and above[b+1]>3: b+=1
    dur=(b-a+1)*hop/sr
    seg=As[:,a:b+1]; tot=(seg**2).sum()+1e-12
    def frac(lo,hi): i=(f>=lo)&(f<hi); return float((seg[i]**2).sum()/tot)
    c0=float(cent[a:a+max(1,(b-a)//3)+1].mean()); c1=float(cent[b-max(1,(b-a)//3):b+1].mean())
    sub=frac(20,120); lowmid=frac(120,1000); hi=frac(4000,16000)
    if dur<0.09 and hi>0.35: cls='tick/click'
    elif sub>0.45: cls='boom/impact'
    elif dur>=0.6 and c1>c0*1.25: cls='riser'
    elif dur>=0.15 and hi>0.25: cls='whoosh/air'
    elif dur>=0.6: cls='swell/pad'
    else: cls='hit'
    out.append((t[a],t[p],dur,above[p],c0,c1,sub,hi,cls))
print("start  peak   dur   +dB  centroid(start->end Hz)  sub%  hi%  class")
for o in out: print(f"{o[0]:6.2f} {o[1]:6.2f} {o[2]:5.2f} {o[3]:5.1f}  {o[4]:6.0f}->{o[5]:6.0f}   {100*o[6]:3.0f}  {100*o[7]:3.0f}  {o[8]}")
print(f"events {len(out)} | per 10 s: {len(out)/(len(side)/sr)*10:.1f}")
# rhythmic periodicity of side envelope (music with beat?)
e=np.maximum(0,np.diff(envdb)); e-=e.mean(); ac=np.correlate(e,e,'full')[len(e)-1:]
lags=np.arange(30,121); best=lags[np.argsort(ac[lags])[::-1][:3]]
print("side-env tempo candidates: "+", ".join(f"{60/(b*hop/sr):.0f}bpm(r={ac[b]/ac[0]:.2f})" for b in best))
