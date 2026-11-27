#!/usr/bin/env python3
"""Write skill-motion-graphics-craft/references/picks.md from data/entries-all-242.json (prompts copied verbatim)."""
import json,re,sys,os
root=sys.argv[1]
rows=json.load(open(os.path.join(root,'data/entries-all-242.json'))); prof=json.load(open(os.path.join(root,'data/profiles.json')))['profiles']
picks=sorted([r for r in rows if r['pick']],key=lambda r:r['pick']['order'])
def fence(t):
    n=max([len(x) for x in re.findall(r'`+',t)]+[2])+1; return '`'*n
L=['# The 33 picks and their original prompts\n',
'Source: prompt-motion.com, reviewed 27 Nov 2026, chosen from all 242 entries. Prompts are copied character for character from each entry page; English translations are the site\'s own. Videos and prompts belong to their creators.\n',
'`Profile` is the style profile from `style-profiles.md` (M1-M7). `Entry` is the row number in `data/entries-all-242.csv`. Open `visual-reference/detail/<entry>-<slug>.jpg` to see the frames.\n']
for p,v in prof.items():
    L.append(f'- **{p}** {v["name"]}: entries '+', '.join(str(k) for k in v['entries']))
L.append('')
for r in picks:
    k=r['pick']['order']; m=[r['model'],('effort '+r['effort'].lower()) if r['effort'] else None,(r['iterations'] or '').lower() or None,('stack: '+r['stack']) if r['stack'] else None,'posted '+r['posted']]
    L.append(f'\n## {k}. {r["title"]} ({r["creator_handle"]})\n')
    L.append(f'- Profile {r["profile"]} · entry {r["n"]} · {r["duration_s"]:.0f}s · {r["width"]}x{r["height"]} · {r["fps"]:g} fps · '+' · '.join(x for x in m if x))
    L.append(f'- Watch: {r["url"]}\n- Original post: {r["post"]}')
    L.append(f'- Why it is here: {r["pick"]["why"]}\n')
    if r['site_note_above_prompt']: L.append(f'Site note shown above the prompt: "{r["site_note_above_prompt"]}"\n')
    f=fence(r['prompt']); L.append('Original prompt'+(f' ({r["prompt_language"]})' if r['prompt_language'] else '')+':\n'); L.append(f'{f}text\n{r["prompt"]}\n{f}\n')
    if r['prompt_translation_en']:
        t=r['prompt_translation_en']; f=fence(t); L.append('English translation (from the site):\n'); L.append(f'{f}text\n{t}\n{f}\n')
open(os.path.join(root,'skill-motion-graphics-craft/references/picks.md'),'w',encoding='utf-8').write('\n'.join(L))
print('picks',len(picks))
