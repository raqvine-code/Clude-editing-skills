# Pull prompt + translation straight from the page's data payload and compare with the visible prompt block
import json,re,sys,os,html
base=sys.argv[1]
d=json.load(open(os.path.join(base,'data.json')))
def payload(s):
    out=[]
    for m in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)',s):
        try: out.append(json.loads(m.group(1)))
        except Exception as e: pass
    return ''.join(out)
dec=json.JSONDecoder()
mism=0; tr=0
for r in d:
    s=open(os.path.join(base,'pages',r['slug']+'.html'),encoding='utf-8').read()
    p=payload(s)
    i=p.find('"prompt":"')
    r['rsc_prompt']=None; r['translation']=None
    # find the prompt that precedes a "translation" key (the entry's own prompt block)
    for m in re.finditer(r'"note":("\$undefined"|"(?:[^"\\]|\\.)*"|null),"prompt":',p):
        val,end=dec.raw_decode(p,m.end())
        r['rsc_prompt']=val
        note=json.loads(m.group(1)) if m.group(1)!='null' else None
        r['note']=None if note in ('$undefined',None) else note
        rest=p[end:end+15]
        if rest.startswith(',"translation":'):
            st=end+len(',"translation":')
            if p[st]=='{':
                obj,_=dec.raw_decode(p,st); r['translation']=obj; tr+=1
        break
    if r.get('prompt') is not None and r['rsc_prompt'] is not None and r['prompt']!=r['rsc_prompt']:
        mism+=1; print('MISMATCH',r['slug'],len(r['prompt']),len(r['rsc_prompt']))
print('translations',tr,'mismatch',mism,'no rsc',sum(1 for r in d if r['kind']=='Prompt' and r['rsc_prompt'] is None),'notes',sum(1 for r in d if r.get('note')))
json.dump(d,open(os.path.join(base,'data.json'),'w'),ensure_ascii=False,indent=1)
