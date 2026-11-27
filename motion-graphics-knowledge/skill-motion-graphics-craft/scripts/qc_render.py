#!/usr/bin/env python3
"""Cheap checks on a rendered motion video, using the failure modes the reference prompts warn about.
usage: qc_render.py video.mp4 [--pop-ratio 3] [--min-diff 6] [--strips DIR]
Reports: size / fps / duration / audio track, loop-boundary difference (first vs last frame), loudness, and CANDIDATE
single-frame pops (frame difference at least pop-ratio x both neighbours). A deliberate hard cut also shows up as a
candidate, so judge each by its timestamp; with --strips DIR a 3-frame strip (before / pop / after) is saved per candidate.
Needs ffmpeg/ffprobe, numpy, Pillow."""
import argparse,subprocess,json,re,os
import numpy as np
from PIL import Image
ap=argparse.ArgumentParser(); ap.add_argument('video'); ap.add_argument('--pop-ratio',type=float,default=3.0); ap.add_argument('--min-diff',type=float,default=6.0); ap.add_argument('--strips')
a=ap.parse_args()
j=json.loads(subprocess.run(['ffprobe','-v','error','-print_format','json','-show_format','-show_streams',a.video],capture_output=True,text=True).stdout)
v=[s for s in j['streams'] if s['codec_type']=='video'][0]; au=[s for s in j['streams'] if s['codec_type']=='audio']
n,dn=map(int,v['r_frame_rate'].split('/')); fps=n/dn; dur=float(j['format']['duration'])
print(f"{v['width']}x{v['height']} {fps:g} fps {dur:.2f}s audio={'yes' if au else 'NO'}")
W,H=192,108
raw=subprocess.run(['ffmpeg','-v','error','-i',a.video,'-vf',f'scale={W}:{H},format=gray','-f','rawvideo','-'],capture_output=True).stdout
fr=np.frombuffer(raw,dtype=np.uint8); N=len(fr)//(W*H); fr=fr[:N*W*H].reshape(N,H,W).astype(np.int16)
loop=float(np.abs(fr[0]-fr[-1]).mean())
print(f"frames {N}; loop boundary (first vs last frame) mean abs diff {loop:.2f} of 255  -> {'matches (loops cleanly)' if loop<2 else 'differs (fine if it is not meant to loop)'}")
df=np.abs(fr[1:]-fr[:-1]).mean(axis=(1,2)); c=[]
for i in range(1,len(df)-1):
    if df[i]>=a.min_diff and df[i]>=a.pop_ratio*max(df[i-1],df[i+1]): c.append(i+1)
print(f"single-frame pop candidates: {len(c)}")
for k in c[:40]: print(f"  frame {k}  t={k/fps:.3f}s  diff {df[k-1]:.1f} (neighbours {df[k-2]:.1f}, {df[k] if k<len(df) else 0:.1f})")
if a.strips and c:
    os.makedirs(a.strips,exist_ok=True)
    for k in c[:40]:
        ims=[]
        for f in (k-1,k,k+1):
            p=os.path.join(a.strips,'_t.jpg')
            subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{max(f,0)/fps:.4f}','-i',a.video,'-frames:v','1','-vf','scale=480:-2',p],check=True)
            ims.append(Image.open(p).convert('RGB'))
        s=Image.new('RGB',(sum(i.width for i in ims),ims[0].height)); x=0
        for i in ims: s.paste(i,(x,0)); x+=i.width
        s.save(os.path.join(a.strips,f'pop_{k:06d}.jpg'),quality=82)
    os.remove(os.path.join(a.strips,'_t.jpg'))
if au:
    o=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',a.video,'-vn','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    I=re.findall(r'I:\s+(-?[\d.]+) LUFS',o); P=re.findall(r'Peak:\s+(-?[\d.]+) dBFS',o)
    if I: print(f"loudness {I[-1]} LUFS integrated (reference prompts target -14), true peak {P[-1] if P else '?'} dBFS")
