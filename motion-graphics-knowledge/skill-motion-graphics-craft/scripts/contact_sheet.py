#!/usr/bin/env python3
"""Contact sheet of evenly spaced frames from a video, with a timecode on every frame.
usage: contact_sheet.py video.mp4 out.jpg [--n 24] [--cols 6] [--width 320] [--burst T]
--burst T adds a row of 6 consecutive frames, 70 ms apart, starting at T seconds (to inspect easing and motion blur).
Needs ffmpeg/ffprobe and Pillow."""
import argparse,subprocess,json,os,tempfile
from PIL import Image,ImageDraw
ap=argparse.ArgumentParser(); ap.add_argument('video'); ap.add_argument('out')
ap.add_argument('--n',type=int,default=24); ap.add_argument('--cols',type=int,default=6); ap.add_argument('--width',type=int,default=320); ap.add_argument('--burst',type=float)
a=ap.parse_args()
dur=float(json.loads(subprocess.run(['ffprobe','-v','error','-print_format','json','-show_format',a.video],capture_output=True,text=True).stdout)['format']['duration'])
tmp=tempfile.mkdtemp()
def grab(t,i):
    p=os.path.join(tmp,f'{i}.jpg')
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{max(t,0):.3f}','-i',a.video,'-frames:v','1','-vf',f'scale={a.width}:-2','-q:v','3',p],check=True)
    return Image.open(p).convert('RGB')
ts=[dur*(i+0.5)/a.n for i in range(a.n)]
if a.burst is not None: ts+= [a.burst+j*0.07 for j in range(6)]
ims=[grab(t,i) for i,t in enumerate(ts)]
w,h=ims[0].size; rows=-(-len(ims)//a.cols)
sheet=Image.new('RGB',(a.cols*w,rows*h),(20,20,20)); d=ImageDraw.Draw(sheet)
for i,(im,t) in enumerate(zip(ims,ts)):
    x,y=(i%a.cols)*w,(i//a.cols)*h; sheet.paste(im,(x,y))
    d.rectangle([x+3,y+3,x+62,y+17],fill=(0,0,0)); d.text((x+6,y+4),f'{t:6.2f}s',fill=(255,255,255))
os.makedirs(os.path.dirname(os.path.abspath(a.out)),exist_ok=True)
sheet.save(a.out,quality=85); print('wrote',a.out,sheet.size)
