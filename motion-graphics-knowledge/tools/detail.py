# Detail sheet per video: 18 evenly spaced frames + 6-frame burst in the busiest sustained-motion window
import json,subprocess,sys,os
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from PIL import Image,ImageDraw,ImageFont
base=sys.argv[1]; ids=[int(x) for x in sys.argv[2].split(',')]
d=json.load(open(os.path.join(base,'data.json')))
out=os.path.join(base,'detail'); os.makedirs(out,exist_ok=True)
fr=os.path.join(base,'frames_detail'); os.makedirs(fr,exist_ok=True)
TW=256; TH=144; COLS=6; N=18; LH=20
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',14)
def grab(slug,t,name):
    p=os.path.join(fr,name)
    if not os.path.exists(p):
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{max(t,0):.3f}','-i',os.path.join(base,'videos',slug+'.mp4'),'-frames:v','1','-vf',f'scale={TW}:{TH}:force_original_aspect_ratio=decrease','-q:v','4',p])
    return p
def make(k):
    r=d[k-1]; slug=r['slug']; dur=r['dur']
    ts=[dur*(i+0.5)/N for i in range(N)]
    df=np.load(os.path.join(base,'diffs',slug+'.npy'))
    # sustained-motion window: 5 samples at 12fps (~0.42s), maximise the minimum diff in window (robust to single cuts)
    best=0;bi=0
    lo=int(0.08*len(df)); hi=int(0.92*len(df))-5
    for i in range(lo,max(hi,lo+1)):
        w=df[i:i+5]
        if len(w)<5: break
        s=float(np.sort(w)[1])  # 2nd smallest
        if s>best: best=s;bi=i
    t0=bi/12.0
    bs=[t0+j*0.07 for j in range(6)]
    im=Image.new('RGB',(COLS*TW,4*TH+2*LH),(24,24,24)); dr=ImageDraw.Draw(im)
    lab=f"#{k} {slug} | {r['title']} | {dur:.0f}s {r['vw']}x{r['vh']} {r['fps']}fps {'A' if r['audio'] else 'noA'} | med{r['m_med']} static{r['m_static']} cuts/10s {r['m_cuts10']}"
    dr.text((4,2),lab[:200],fill=(255,230,120),font=font)
    for i,t in enumerate(ts):
        f=Image.open(grab(slug,t,f'{slug}_e{i}.jpg')); x=(i%COLS)*TW; y=LH+(i//COLS)*TH
        im.paste(f,(x+(TW-f.width)//2,y+(TH-f.height)//2))
    y=LH+3*TH
    dr.text((4,y+2),f"burst @ {t0:.1f}s, 70ms steps (in-betweens)",fill=(120,220,255),font=font)
    for j,t in enumerate(bs):
        f=Image.open(grab(slug,t,f'{slug}_b{j}.jpg')); im.paste(f,(j*TW+(TW-f.width)//2,y+LH+(TH-f.height)//2))
    im.save(os.path.join(out,f'{k:03d}.jpg'),quality=80)
with ThreadPoolExecutor(4) as ex: list(ex.map(make,ids))
print('ok',len(ids))
