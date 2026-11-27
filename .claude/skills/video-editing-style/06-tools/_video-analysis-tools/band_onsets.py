"""usage: python -I band_onsets.py <mono wav>. Loudness, energy share per band, per-band onset times (20 ms hop), 1 s RMS profile. (ref69, 2026-10-09)"""
import sys, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, find_peaks
x, sr = sf.read(sys.argv[1]); 
bands = {'sub<150':(20,150),'low150-500':(150,500),'mid0.5-2k':(500,2000),'hi2-6k':(2000,6000),'air6k+':(6000,16000)}
hop = int(sr*0.02)
n = len(x)//hop
def env(sig):
    return np.sqrt(np.mean(sig[:n*hop].reshape(n,hop)**2,axis=1))+1e-9
tot = env(x)
print('dur %.2f s'%(len(x)/sr), 'rms mean dBFS %.1f'%(20*np.log10(np.sqrt(np.mean(x**2)))), 'peak %.1f'%(20*np.log10(np.max(np.abs(x)))))
E={}
for k,(lo,hi) in bands.items():
    sos=butter(4,[lo,min(hi,sr/2-100)],btype='band',fs=sr,output='sos'); E[k]=env(sosfilt(sos,x))
e_tot=sum(v**2 for v in E.values())
for k in E: print('%-12s share %.1f%%'%(k,100*np.sum(E[k]**2)/np.sum(e_tot)))
# spectral-flux-like onset on dB of total env per band
def onsets(e, thr_db=6, min_gap=0.12, floor=-60):
    d=20*np.log10(e); 
    flux=np.maximum(0,d[1:]-d[:-1])
    pk,_=find_peaks(flux,height=thr_db,distance=int(min_gap/0.02))
    return [(round((p+1)*0.02,2),round(d[p+1],1),round(flux[p],1)) for p in pk if d[p+1]>floor]
for k in ['sub<150','hi2-6k','air6k+']:
    print('--',k); print(onsets(E[k],8))
# 1 s loudness profile
print('1s RMS dBFS:',[round(20*np.log10(np.sqrt(np.mean(x[int(i*sr):int((i+1)*sr)]**2))+1e-9),1) for i in range(int(len(x)/sr))])
# silence
db=20*np.log10(tot); print('frames below -50 dB: %.1f%%'%(100*np.mean(db<-50)))
