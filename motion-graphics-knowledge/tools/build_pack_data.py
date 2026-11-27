import json,os,sys,csv,shutil,statistics as st,collections
base='.'; out=sys.argv[1]
d=json.load(open('data.json')); picks=json.load(open('picks.json'))
PROFILES={
 'M1':('Narrative short / cinematic world',[109,68,186,173,32,154,59]),
 'M2':('One-idea concept piece / data poem / 3D explainer',[28,156,82,142,95,195]),
 'M3':('Format-play and chaptered pieces',[63,130,41,187]),
 'M4':('Type-and-shape showreel',[69,161,197,131]),
 'M5':('Look-driven piece (one strong visual medium)',[151,177,125,191]),
 'M6':('One-take UI motion',[226,183,230]),
 'M7':('Product / brand launch film',[225,227,139,202,200]),
}
prof_of={k:p for p,(n,ks) in PROFILES.items() for k in ks}
# my grades from the review (A = strongest). Entries not listed were not examined closely.
G={3:('B+','Celld neo-brutalist explainer, clear step logic'),7:('A-','hand-drawn watercolor world, match-cut zooms, 78s story'),8:('A-','60fps dark technical HUD, glitch-slice type, 3D phone'),
14:('A','particle sun, orbiting text rings, whip-blur camera'),22:('B+','3D diorama mascot, charming, low resolution (720x900)'),24:('A-','Scrabble-tile 3D characters, depth of field, vertical'),
28:('A','one concept with payoff line "YOU BLINKED"'),32:('A','real-time 3D, flares, depth of field, sunset'),36:('A-','168s 3D stadium explainer, ambitious'),38:('A-','editorial serif, dot dissolves, music sync, restrained'),
41:('A','new palette and type system per chapter'),47:('A-','fire particles plus calligraphy in one scene, no audio'),54:('not picked','clay-style music video; looks like generated video rather than code-built motion graphics, so outside this study'),
58:('A-','sports-broadcast type over game footage'),59:('A','one continuous dusk-to-night scene with verse typography'),61:('A-','stick figures and torn-paper transitions, 60fps'),63:('A','nine genre pastiches in 75s, most inventive concept'),
68:('A','4-minute animated short, storm sequence, consistent colour script'),69:('A','strict two-colour editorial system, 60fps'),72:('A','iris wipes, isometric 3D room, premium brand'),77:('A-','psychedelic collage, vertical, unusual'),
79:('B+','beat-synced 3D ball'),82:('A','point to line to circle to sphere to world, book-figure restraint'),92:('B+','paper-style product launch'),95:('A','particle murmuration data-viz in one flowing take'),
97:('A-','four seasons through a train window, tunnel transition'),99:('B+','branding agency showreel, ends on black frames'),100:('A-','cartoon character acting (skill entry, no prompt)'),107:('A','raymarched chrome blob, radial type tunnel'),
109:('A','letterboxed silhouette short, light and fog'),111:('A-','firefly bug in a code world, 90s story'),116:('A-','172s history of AI, dark with orange accent, slow pacing'),124:('A-','Swiss-style showreel, strong system, 60fps'),
125:('A','engraving imagery plus serif type, vertical'),130:('A','age counter and heartbeat HUD, art style changes per life stage'),131:('A','widest technique range of the showreels'),139:('A','halftone dots, globe, orange system'),
142:('A','epicycles draw pi, Julia set, Euler identity'),144:('A-','98s 3D exploded-view explainer (same film as 195)'),148:('A-','chrome 3D anime hype edit, vertical, beat-synced'),151:('A','shader kaleidoscopic eye tunnel, liquid metal'),
152:('A-','concentric type rings, vibrant, 60fps'),154:('A','one continuous aerial take, painterly clouds, camera roll'),155:('B+','stop-motion style DeFi explainer, 12fps, no audio'),156:('A','Earth/Sun renders plus counters'),
161:('A','Swiss/Bauhaus poster type breaking its grid'),173:('A','5-minute black hole lensing render, contemplative'),174:('A-','mono type experiments with spectrum bursts'),177:('A','risograph halftone, misregistration, Korean type'),
178:('A-','phosphor oscilloscope look'),182:('A-','Apple-style launch film, rapid photo cuts, 60fps'),183:('A','one white ball through a UI, one take, loops'),186:('A','5-minute 3D cartoon episode'),
187:('A','real footage cut out into eight style worlds'),190:('A-','extruded 3D type, chrome blobs, voxel grid'),191:('A','lyrics typography on sun/eclipse imagery'),192:('A','chrome sphere, modular geometry, serif plus grotesk'),
195:('A-','same film as 144 (earlier post); soundtrack nearly silent'),197:('A','lime glass-and-chrome 3D, heavy kinetic type'),200:('A','3D props against light-trail vortex, glitch type'),201:('A-','the original viral showreel, polished classic'),
202:('A','polished dark SaaS film, globe, dashboards'),222:('B+','anime character dance showreel'),225:('A','keynote-style single-take launch film'),226:('A','one shape morphing through UI states'),
227:('A','dark minimal product film, 3D portrait carousel'),228:('A-','3D fly-over of a landing page, depth of field'),229:('A-','minimal food-ordering launch film, rotated gradient type'),230:('A','one orange dot links every scene'),
233:('A-','polished launch film, photo grids, no audio'),238:('B+','shadow-theatre vertical story'),241:('A-','low-poly sphere to blob, Bauhaus portal through the O')}
short=[3,7,8,9,14,15,17,22,24,27,28,29,32,36,38,41,42,47,54,57,58,59,61,63,68,69,72,74,77,79,82,92,94,95,97,99,100,107,109,110,111,116,120,122,124,125,129,130,131,134,138,139,142,144,148,151,152,154,155,156,161,166,168,173,174,177,178,182,183,186,187,190,191,192,197,200,201,202,222,225,226,227,228,229,230,233,236,238,241]
pick_info={}
n=0
for c in picks:
    for it in c['items']:
        n+=1; pick_info[it['k']]={'order':n,'site_category':c['cat'],'why':it['why']}
rows=[]
for i,r in enumerate(d,1):
    st_='picked' if i in pick_info else ('examined' if i in G else ('shortlisted-not-examined' if i in short else 'triage-only'))
    row={'n':i,'slug':r['slug'],'url':r['url'],'title':r['title'],'creator':r.get('creator'),'creator_handle':'@'+r['creator_url'].rstrip('/').split('/')[-1],
      'post':r.get('post'),'kind':r['kind'],'tags':r['tags'],'posted':r['meta'].get('Posted'),'model':r['meta'].get('Model'),'effort':r['meta'].get('Effort'),
      'iterations':r['meta'].get('Iterations'),'stack':r['meta'].get('Stack'),
      'duration_s':round(r['dur'],1),'fps':r['fps'],'width':r['vw'],'height':r['vh'],'has_audio_track':r['audio'],'size_mb':round(r['size']/1e6,1),
      'median_frame_diff':r.get('m_med'),'static_share':r.get('m_static'),'spikes_per_10s':r.get('m_cuts10'),
      'prompt':r.get('prompt'),'prompt_translation_en':(r.get('translation') or {}).get('prompt'),'prompt_language':(r.get('translation') or {}).get('language'),
      'site_note_above_prompt':('using any reference with a fast edit (5s video is enough)' if r['slug']=='lexnlin-038035' else None),
      'review_status':st_,'review_grade':G.get(i,(None,None))[0],'review_note':G.get(i,(None,None))[1],
      'profile':prof_of.get(i),'pick':pick_info.get(i)}
    rows.append(row)
os.makedirs(out+'/data',exist_ok=True)
json.dump(rows,open(out+'/data/entries-all-242.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
with open(out+'/data/entries-all-242.csv','w',newline='',encoding='utf-8') as f:
    cols=['n','slug','title','creator_handle','kind','tags','posted','effort','iterations','stack','duration_s','fps','width','height','has_audio_track','median_frame_diff','static_share','spikes_per_10s','review_status','review_grade','profile','url','post']
    w=csv.writer(f); w.writerow(cols)
    for r in rows: w.writerow([('; '.join(r[c]) if c=='tags' else r[c]) for c in cols])
json.dump({'profiles':{k:{'name':v[0],'entries':v[1]} for k,v in PROFILES.items()}},open(out+'/data/profiles.json','w'),indent=1)
print(collections.Counter(r['review_status'] for r in rows))
print('profile coverage',sorted(prof_of)==sorted(pick_info),len(prof_of))
# per-profile stats
for p,(name,ks) in PROFILES.items():
    R=[d[k-1] for k in ks]
    print(p,name,len(R),'dur med',round(st.median(r['dur'] for r in R)),'60fps',sum(1 for r in R if r['fps']>=59),'/',len(R),
      'diff med',round(st.median(r['m_med'] for r in R),2),'static',round(st.median(r['m_static'] for r in R),3),'spikes/10s',round(st.median(r['m_cuts10'] for r in R),1),
      'aspects',collections.Counter(('16:9' if abs(r['vw']/r['vh']-16/9)<0.1 else '1:1' if abs(r['vw']/r['vh']-1)<0.05 else '9:16' if r['vw']<r['vh']*0.7 else 'wide' ) for r in R))
