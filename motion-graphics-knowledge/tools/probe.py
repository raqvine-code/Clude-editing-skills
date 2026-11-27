import json,subprocess,sys,os
from concurrent.futures import ThreadPoolExecutor
base=sys.argv[1]
d=json.load(open(os.path.join(base,'data.json')))
def probe(r):
    p=os.path.join(base,'videos',r['slug']+'.mp4')
    o=subprocess.run(['ffprobe','-v','error','-print_format','json','-show_format','-show_streams',p],capture_output=True,text=True).stdout
    j=json.loads(o)
    v=[s for s in j['streams'] if s['codec_type']=='video'][0]
    a=[s for s in j['streams'] if s['codec_type']=='audio']
    num,den=v['r_frame_rate'].split('/')
    return r['slug'],{'dur':float(j['format']['duration']),'fps':round(float(num)/float(den),2),'vw':v['width'],'vh':v['height'],'audio':bool(a),'size':int(j['format']['size'])}
with ThreadPoolExecutor(8) as ex:
    res=dict(ex.map(probe,d))
for r in d: r.update(res[r['slug']])
json.dump(d,open(os.path.join(base,'data.json'),'w'),ensure_ascii=False,indent=1)
import collections
print('total dur min',sum(r['dur'] for r in d)/60)
print(sorted(round(r['dur']) for r in d))
print(collections.Counter(r['fps'] for r in d))
print('audio',sum(r['audio'] for r in d))
