"""usage: python -I spectrogram_log.py <mono wav> <out.png>. Log-frequency spectrogram with second ticks, plus a low-band tempo guess and onset list. (ref69, 2026-10-09)"""
import sys, numpy as np, soundfile as sf
from scipy.signal import spectrogram, butter, sosfilt, find_peaks
from PIL import Image, ImageDraw
x,sr=sf.read(sys.argv[1])
f,t,S=spectrogram(x,sr,nperseg=2048,noverlap=1536)
S=10*np.log10(S+1e-12)
m=f<12000; f=f[m]; S=S[m]
# log-ish freq axis
H=360; W=1450
img=np.zeros((H,W),dtype=np.uint8)
fl=np.geomspace(40,12000,H)
for r,fv in enumerate(fl):
    i=np.argmin(abs(f-fv)); row=S[i]
    cols=np.interp(np.linspace(0,t[-1],W),t,row)
    img[H-1-r]=np.clip((cols+100)/70*255,0,255)
im=Image.fromarray(img).convert('RGB')
from PIL import ImageOps
im=ImageOps.colorize(Image.fromarray(img),'#000010','#ffe080',mid='#3050c0')
d=ImageDraw.Draw(im)
for s in range(0,15):
    xx=int(s/t[-1]*W); d.line([(xx,0),(xx,H)],fill=(80,80,80)); d.text((xx+2,2),str(s),fill=(255,255,0))
for hz in (100,500,2000,8000):
    yy=H-1-int(np.argmin(abs(fl-hz))); d.line([(0,yy),(W,yy)],fill=(60,60,60)); d.text((2,yy-10),'%dHz'%hz,fill=(0,255,255))
im.save(sys.argv[2])
# tempo from sub+low band envelope
sos=butter(4,[40,300],btype='band',fs=sr,output='sos'); y=sosfilt(sos,x)
hop=int(sr*0.01); n=len(y)//hop; e=np.sqrt(np.mean(y[:n*hop].reshape(n,hop)**2,axis=1))
fl_=np.maximum(0,np.diff(e)); fl_-=fl_.mean()
ac=np.correlate(fl_,fl_,'full')[len(fl_)-1:]
best=[(round(60/(l*0.01),1),round(ac[l]/ac[0],2)) for l in range(25,100) if ac[l]>ac[l-1] and ac[l]>ac[l+1]]
print('tempo candidates (bpm, ac):',sorted(best,key=lambda a:-a[1])[:6])
pk,_=find_peaks(fl_,height=np.percentile(fl_,92),distance=15)
print('low-band onsets (s):',[round((p+1)*0.01,2) for p in pk])
