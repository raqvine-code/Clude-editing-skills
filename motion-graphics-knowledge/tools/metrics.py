import json,subprocess,sys,os
import numpy as np
from concurrent.futures import ThreadPoolExecutor
base=sys.argv[1]
d=json.load(open(os.path.join(base,'data.json')))
os.makedirs(os.path.join(base,'diffs'),exist_ok=True)
W,H,FPS=160,90,12
def run(r):
    out=os.path.join(base,'diffs',r['slug']+'.npy')
    if os.path.exists(out): return
    p=subprocess.run(['ffmpeg','-v','error','-i',os.path.join(base,'videos',r['slug']+'.mp4'),'-vf',f'fps={FPS},scale={W}:{H},format=gray','-f','rawvideo','-'],capture_output=True)
    a=np.frombuffer(p.stdout,dtype=np.uint8)
    n=len(a)//(W*H)
    a=a[:n*W*H].reshape(n,H,W).astype(np.int16)
    df=np.abs(a[1:]-a[:-1]).mean(axis=(1,2))
    np.save(out,df.astype(np.float32))
with ThreadPoolExecutor(4) as ex: list(ex.map(run,d))
for r in d:
    df=np.load(os.path.join(base,'diffs',r['slug']+'.npy'))
    if len(df)<5: continue
    med=float(np.median(df)); 
    cuts=int(((df>18)&(df>4*np.median(df)+6)).sum())
    r['m_med']=round(med,2); r['m_mean']=round(float(df.mean()),2)
    r['m_static']=round(float((df<0.15).mean()),3)
    r['m_cuts10']=round(cuts/(r['dur']/10),2)
json.dump(d,open(os.path.join(base,'data.json'),'w'),ensure_ascii=False,indent=1)
print('done')
