# cross-reel pacing + sync statistics.  usage: python3 -I cross.py <v2_dir>
import sys, re, json, numpy as np
from scipy.io import wavfile
from scipy.signal import stft, find_peaks
V=sys.argv[1]
def words(r):
    W=[]; S=[]
    for l in open(f'{V}/{r}/data/transcript.txt'):
        m=re.match(r'\[([\d.]+)-([\d.]+)\]\s*(.*)',l)
        if m: S.append((float(m.group(1)),float(m.group(2)),m.group(3)))
        elif l.startswith('   '):
            for p in l.strip().split(' | '):
                a=p.split(' ',1)
                if len(a)==2:
                    try: W.append((float(a[0]),a[1]))
                    except: pass
    return W,S
print("=== VO pacing")
print("reel dur words wpm_total | sentences(by . ? !) mean_words | gaps>0.25s: n median max | speech-gap ratio")
R={}
for r in ['r0','r1','r2','r3','r4']:
    W,S=words(r); fr=json.load(open(f'{V}/{r}/data/frames.json')); dur=len(fr)/30
    # sentence split on punctuation
    sent=[]; cur=[]
    for t,w in W:
        cur.append((t,w))
        if re.search(r'[.?!]$',w): sent.append(cur); cur=[]
    if cur: sent.append(cur)
    ws=[t for t,_ in W]; gaps=np.diff(ws)
    # a "gap" = inter-word onset interval minus typical word length ~ use >0.6 s onset spacing as a pause marker
    pauses=[(ws[i],gaps[i]) for i in range(len(gaps)) if gaps[i]>0.60]
    R[r]=dict(W=W,S=S,dur=dur,sent=sent,pauses=pauses,fr=fr)
    print(f"{r} {dur:5.1f} {len(W):4d} {len(W)/dur*60:5.0f} | {len(sent):2d} {np.mean([len(s) for s in sent]):4.1f} | onset-spacing>0.6s: {len(pauses):2d} med {np.median([g for _,g in pauses]) if pauses else 0:.2f} max {max([g for _,g in pauses]) if pauses else 0:.2f} | first sentence: {len(sent[0])} words, ends ~{sent[0][-1][0]+0.35:.1f}s")
print("\n=== Visual change rate (frame-diff based)")
print("reel  median_diff  p90_diff  motion_peaks/s  hard-ish cuts(scene>0.25)  static%  first big change (s)")
for r,d in R.items():
    fr=d['fr']; diff=np.array([f['diff'] for f in fr]); sc=np.array([f['scene'] for f in fr])
    pk,_=find_peaks(diff,height=np.percentile(diff,85),distance=6)
    cuts=[i for i in range(1,len(sc)) if sc[i]>0.25 and sc[i]>=sc[max(0,i-3):i+4].max()]
    d['cuts']=cuts; d['peaks']=pk
    first=next((i for i in range(15,len(diff)) if diff[i]>np.percentile(diff,95)),None)
    print(f"{r}  {np.median(diff):6.2f}  {np.percentile(diff,90):6.2f}  {len(pk)/d['dur']:5.2f}  {len(cuts):3d}  {100*(diff[1:]<0.05).mean():4.1f}%  {first/30 if first else -1:.2f}")
print("\n=== Audio bed vs voice, onsets vs cuts")
for r,d in R.items():
    sr,x=wavfile.read(f'{V}/{r}/data/a44.wav'); x=x.astype(np.float32)/32768.0; m=x.mean(axis=1)
    f,t,Z=stft(m,sr,nperseg=2048,noverlap=2048-441); A=np.abs(Z)
    W=d['W']; ws=np.array([w for w,_ in W])
    # speech mask: within [onset, onset+0.30] of any word ; gap mask: >0.35 s after a word onset and >0.12 s before next
    sp=np.zeros(len(t),bool); gp=np.zeros(len(t),bool)
    for i,w in enumerate(ws):
        nxt=ws[i+1] if i+1<len(ws) else d['dur']
        sp|=(t>=w)&(t<min(w+0.28,nxt))
        if nxt-w>0.75: gp|=(t>=w+0.55)&(t<nxt-0.10)
    def lvl(mask,lo,hi):
        i=(f>=lo)&(f<hi); 
        return 20*np.log10(np.sqrt((A[i][:,mask]**2).mean())+1e-9) if mask.any() else float('nan')
    out=[]
    for nm,lo,hi in (("full",60,12000),("voice 300-3k",300,3000),("air 6-14k",6000,14000),("sub 30-90",30,90)):
        out.append(f"{nm}: speech {lvl(sp,lo,hi):6.1f} gap {lvl(gp,lo,hi):6.1f} Δ {lvl(sp,lo,hi)-lvl(gp,lo,hi):5.1f}")
    print(f"{r} gap-time {gp.mean()*d['dur']:.1f}s | "+" | ".join(out))
    # onsets (air + full) vs cuts
    def onset_times(lo,hi,thr):
        i=(f>=lo)&(f<hi); S_=np.log1p(50*A[i]); fl=np.maximum(0,np.diff(S_,axis=1)).sum(axis=0); fl/=fl.max()+1e-9
        p,_=find_peaks(fl,height=thr,distance=8); return t[p+1]
    air=onset_times(6000,16000,0.30)
    ct=np.array(d['cuts'])/30
    if len(ct):
        off=[float(air[np.argmin(np.abs(air-c))]-c) if len(air) else 9 for c in ct]
        hit=np.mean([abs(o)<=0.10 for o in off])
        print(f"   cuts {len(ct)} | air-band onset within ±0.10 s of cut: {100*hit:.0f}% | offsets(s): "+" ".join(f"{o:+.2f}" for o in off))
    # cut vs nearest word onset: do cuts land in VO gaps / on sentence starts?
    S=d['S']; starts=np.array([s[0] for s in S])
    if len(ct):
        o2=[float(c-starts[np.argmin(np.abs(starts-c))]) for c in ct]
        print(f"   cut minus nearest whisper-segment start (s): "+" ".join(f"{o:+.2f}" for o in o2))
    d['air']=air
