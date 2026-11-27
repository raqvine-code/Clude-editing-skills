# Build triage sheets: N frames per video, several videos per sheet
import json,subprocess,sys,os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image,ImageDraw,ImageFont
base=sys.argv[1]; N=int(sys.argv[2]); TW=int(sys.argv[3]); PER=int(sys.argv[4]); outdir=os.path.join(base,sys.argv[5])
os.makedirs(outdir,exist_ok=True); fr=os.path.join(base,'frames_triage'); os.makedirs(fr,exist_ok=True)
d=json.load(open(os.path.join(base,'data.json')))
TH=int(TW*9/16)
def grab(r):
    out=[]
    for i in range(N):
        t=r['dur']*(i+0.5)/N
        p=os.path.join(fr,f"{r['slug']}_{N}_{i}.jpg")
        if not os.path.exists(p):
            subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.3f}','-i',os.path.join(base,'videos',r['slug']+'.mp4'),'-frames:v','1','-vf',f'scale={TW}:{TH}:force_original_aspect_ratio=decrease','-q:v','4',p])
        out.append(p)
    return out
with ThreadPoolExecutor(4) as ex: frames=list(ex.map(grab,d))
try: font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15)
except Exception: font=ImageFont.load_default()
LH=20
idx=[]
for s in range(0,len(d),PER):
    chunk=list(range(s,min(s+PER,len(d))))
    W=N*TW; H=len(chunk)*(TH+LH)
    im=Image.new('RGB',(W,H),(24,24,24)); dr=ImageDraw.Draw(im)
    for row,k in enumerate(chunk):
        r=d[k]; y=row*(TH+LH)
        lab=f"#{k+1} {r['slug']} | {r['title']} | {r['dur']:.0f}s {r['vw']}x{r['vh']} {'A' if r['audio'] else 'noA'} | {','.join(r['tags'])}"
        dr.text((4,y+2),lab[:190],fill=(255,230,120),font=font)
        for i,p in enumerate(frames[k]):
            if os.path.exists(p):
                f=Image.open(p); im.paste(f,(i*TW+(TW-f.width)//2,y+LH+(TH-f.height)//2))
    name=os.path.join(outdir,f"sheet_{s//PER+1:02d}.jpg"); im.save(name,quality=82); idx.append(name)
print(len(idx),'sheets',im.size)
