import json, re, collections, numpy as np
fr = {}
for l in open('ocr5.jsonl'):
    d = json.loads(l); fr[(int(d['f'][:5]) - 1) / 5.0] = [o for o in d['o'] if o['c'] >= 0.4 and len(o['t'].strip()) >= 2]
T = sorted(fr); N = len(T)
norm = lambda s: re.sub(r'[^a-z0-9 ]', '', s.lower()).strip()
# background text = same string in > 4% of frames (room poster etc.)
cnt = collections.Counter(norm(o['t']) for t in T for o in fr[t])
bg = {s for s, c in cnt.items() if c > 0.04 * N}
print('background strings dropped:', sorted(bg)[:20])
for t in T: fr[t] = [o for o in fr[t] if norm(o['t']) not in bg and norm(o['t'])]
# events: link an observation to the previous frame's observation at the same place (text equal or grown)
ev, open_ = [], []
for t in T:
    nxt = []
    for o in fr[t]:
        n = norm(o['t']); m = None
        for e in open_:
            if abs(e['y'] - o['y']) < 0.04 and abs(e['x'] - o['x']) < 0.06 and (n.startswith(e['n'][:max(3, len(e['n']) - 2)]) or e['n'].startswith(n[:max(3, len(n) - 2)])):
                m = e; break
        if m:
            open_.remove(m)
            if len(n) > len(m['n']): m['grow'] += 1; m['n'] = n; m['t'] = o['t']; m['tfull'] = t
            m['e'] = t; m['w'] = max(m['w'], o['w']); nxt.append(m)
        else:
            e = dict(s=t, e=t, n=n, t=o['t'], x=o['x'], y=o['y'], w=o['w'], h=o['h'], grow=0, tfull=t); ev.append(e); nxt.append(e)
    open_ = nxt
ev = [e for e in ev if e['e'] - e['s'] >= 0.2 or e['h'] > 0.12]
json.dump(ev, open('text_events.json', 'w'))
H = np.array([e['h'] for e in ev])
cls = lambda e: 'HEAD' if e['h'] >= 0.16 else ('big' if e['h'] >= 0.075 else ('cap' if e['h'] >= 0.035 else 'small'))
print('events', len(ev), collections.Counter(cls(e) for e in ev))
anytext = np.array([len(fr[t]) > 0 for t in T]); print('share of frames with overlay text:', round(float(anytext.mean()), 2))
for m in range(int(T[-1] // 60) + 1): print(f'min{m}: {round(float(anytext[m * 300:(m + 1) * 300].mean()), 2)}', end=' ')
print()
caps = [e for e in ev if cls(e) == 'cap']
print('caption events: median duration', round(float(np.median([e['e'] - e['s'] + 0.2 for e in caps])), 2), 's; type-on (text grew) share', round(float(np.mean([e['grow'] > 0 for e in caps])), 2),
      '; median words', int(np.median([len(e['n'].split()) for e in caps])), '; height median', round(float(np.median([e['h'] for e in caps])), 3))
xc = np.array([e['x'] + e['w'] / 2 for e in caps]); yc = np.array([e['y'] + e['h'] / 2 for e in caps])
print('caption x-centre: left(<0.4)', int((xc < 0.4).sum()), 'centre', int(((xc >= 0.4) & (xc <= 0.6)).sum()), 'right(>0.6)', int((xc > 0.6).sum()))
print('caption y-centre hist (top->bottom, 10 bins):', np.histogram(yc, bins=10, range=(0, 1))[0].tolist())
with open('text_timeline.txt', 'w') as f:
    for e in sorted(ev, key=lambda e: e['s']):
        f.write(f"{int(e['s'] // 60)}:{e['s'] % 60:04.1f} {e['e'] - e['s'] + 0.2:4.1f}s {cls(e):5s} x{e['x']:.2f} y{e['y']:.2f} h{e['h']:.3f} {'T' if e['grow'] else ' '} {e['t']}\n")
with open('headlines.txt', 'w') as f:
    for e in ev:
        if cls(e) == 'HEAD': f.write(f"{int(e['s'] // 60)}:{e['s'] % 60:04.1f} {e['e'] - e['s'] + 0.2:.1f}s h{e['h']:.2f} {e['t']}\n")
print('big-text moments (h>=0.16) written to headlines.txt; full list in text_timeline.txt')
