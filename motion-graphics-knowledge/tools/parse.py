import re,glob,html,json,sys,os
pages=sys.argv[1]; out=sys.argv[2]
def strip(x): return html.unescape(re.sub(r'<[^>]+>','',x))
def vis(s):
    t=re.sub(r'<script[^>]*>.*?</script>','',s,flags=re.S)
    t=re.sub(r'<style[^>]*>.*?</style>','',t,flags=re.S)
    t=re.sub(r'<[^>]+>','\n',t)
    t=html.unescape(t)
    return [l.strip() for l in t.split('\n') if l.strip()]
TAGS={'Product UI','Phone','Charts','Diagrams','Kinetic type','Shapes','Particles','Characters','Photos','Music','Code'}
rows=[]
for f in sorted(glob.glob(os.path.join(pages,'*.html'))):
    s=open(f,encoding='utf-8').read()
    slug=os.path.basename(f)[:-5]
    ld=None
    for m in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',s,flags=re.S):
        try:
            j=json.loads(m)
            if j.get('@type')=='VideoObject': ld=j
        except Exception as e: pass
    L=vis(s)
    r={'slug':slug,'url':'https://prompt-motion.com/'+slug}
    if ld:
        r['title']=ld.get('name'); r['video']=ld.get('contentUrl'); r['poster']=(ld.get('thumbnailUrl') or [None])[0]
        r['date']=ld.get('uploadDate'); r['w']=ld.get('width'); r['h']=ld.get('height')
        r['creator']=ld.get('creator',{}).get('name'); r['creator_url']=ld.get('creator',{}).get('url')
        r['duration']=ld.get('duration')
    m=re.search(r'<div id="entry-prompt"[^>]*>(.*?)</div>',s,flags=re.S)
    if m:
        inner=m.group(1)
        r['prompt_has_tags']=bool(re.search(r'<[a-z]',inner))
        r['prompt']=html.unescape(re.sub(r'<!-- -->','',inner)) if not r['prompt_has_tags'] else html.unescape(re.sub(r'<[^>]+>','',inner))
    r['tags']=[x for x in L if x in TAGS]
    # dedupe tags preserving order
    seen=[];[seen.append(x) for x in r['tags'] if x not in seen]; r['tags']=seen
    r['kind']='Skill' if 'Skill' in L[:40] and 'entry-prompt' not in s else ('Prompt' if m else '?')
    # meta fields
    meta={}
    keys=['Model','Effort','Iterations','Stack','Posted','Tool','Harness','Duration','Time','Cost','Tokens']
    for i,x in enumerate(L):
        if x in keys and i+1<len(L): meta[x]=L[i+1]
    r['meta']=meta
    pm=re.search(r'href="(https://(?:x|twitter)\.com/[^"]+/status/\d+)"',s)
    r['post']=pm.group(1) if pm else None
    r['lines']=L
    rows.append(r)
json.dump(rows,open(out,'w'),ensure_ascii=False,indent=1)
print(len(rows))
