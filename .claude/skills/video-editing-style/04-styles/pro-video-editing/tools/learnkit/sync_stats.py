"""Speech stats, caption-vs-speech sync, caption coverage, SFX-vs-graphics alignment. Writes transcript.txt and captions_compact.txt. Run in the study folder."""
import json, re, numpy as np, collections
ev = json.load(open('text_events.json')); tr = json.load(open('transcript.json')); W = [w for s in tr['segs'] for w in s['w']]
if not W: print('no speech found'); raise SystemExit
norm = lambda s: re.sub(r'[^a-z0-9 ]', '', s.lower()).strip()
g = np.array([b[0] - a[1] for a, b in zip(W[:-1], W[1:])])
print('words', len(W), '| wpm', round(len(W) / max(1, W[-1][1] - W[0][0]) * 60), '| median gap', round(float(np.median(g)), 2), '| gaps >=0.5 s', int((g >= 0.5).sum()), '| pauses >=1 s', int((g >= 1).sum()))
print('pauses >=1 s at:', [f"{int(a[1] // 60)}:{a[1] % 60:04.1f}({b[0] - a[1]:.1f})" for a, b in zip(W[:-1], W[1:]) if b[0] - a[1] >= 1.0][:30])
with open('transcript.txt', 'w') as f:
    line, t0 = [], None
    for s in tr['segs']:
        if t0 is None: t0 = s['s']
        line.append(s['t'])
        if s['e'] - t0 >= 12: f.write(f"[{int(t0 // 60)}:{int(t0 % 60):02d}] " + ' '.join(line) + "\n"); line, t0 = [], None
    if line: f.write(f"[{int(t0 // 60)}:{int(t0 % 60):02d}] " + ' '.join(line) + "\n")
caps = [e for e in ev if 0.035 <= e['h'] < 0.16 and e['e'] - e['s'] >= 0.2]
wt = collections.defaultdict(list)
for a, b, w in W: wt[norm(w)].append(a)
lags = []
for e in caps:
    ws = e['n'].split()
    if not ws or len(ws[0]) < 4: continue
    c = [t for t in wt.get(ws[0], []) if abs(t - e['s']) <= 1.5]
    if c: lags.append(e['s'] - min(c, key=lambda t: abs(t - e['s'])))
if lags: print('caption first word vs speech (s, + = after the word starts): n', len(lags), 'median', round(float(np.median(lags)), 2), 'middle half', np.round(np.percentile(lags, [25, 75]), 2))
on = collections.defaultdict(list)
for e in ev:
    for w in e['n'].split(): on[w].append((e['s'], e['e']))
hit = [any(s - 1.5 <= a <= e_ + 1.5 for s, e_ in on.get(norm(w), [])) for a, b, w in W if len(norm(w)) >= 4]
if hit: print('spoken words (4+ letters) shown on screen:', round(float(np.mean(hit)) * 100), '%')
try:
    b = np.array(json.load(open('audio_ev.json'))['bursts'])
    near = lambda a, w: round(float(np.mean([np.abs(b - t).min() <= w for t in a])) * 100) if len(a) and len(b) else 0
    heads = sorted({round(e['s'], 1) for e in ev if e['h'] >= 0.25}); hs = heads[:1]
    for h in heads:
        if h - hs[-1] > 1.5: hs.append(h)
    sh = json.load(open('shots/shots.json')); dark = [s['s'] for s in sh['shots'] if s['sat'] < 0.2 and s['luma'] < 60]
    print('stereo bursts within 0.3 s of: big text moments', len(hs), '->', near(hs, 0.3), '% | cuts into dark scenes', len(dark), '->', near(dark, 0.3), '% | all cuts ->', near(sh['cuts'], 0.3), '% | caption pops ->', near([e['s'] for e in caps], 0.3), '% | chance ->', near(np.random.default_rng(1).uniform(0, sh['dur'], 400), 0.3), '%')
except Exception as ex: print('no audio events:', ex)
buck = collections.defaultdict(list)
for e in sorted(caps, key=lambda e: e['s']):
    if e['e'] - e['s'] < 0.4: continue
    side = 'L' if e['x'] + e['w'] / 2 < 0.4 else ('R' if e['x'] + e['w'] / 2 > 0.6 else 'C'); t = e['t'].strip(); k = int(e['s'] // 15)
    if not buck[k] or buck[k][-1][2:] != t: buck[k].append(f"{side}:{t}")
with open('captions_compact.txt', 'w') as f:
    for k in sorted(buck): f.write(f"{k * 15 // 60}:{k * 15 % 60:02d} " + ' | '.join(buck[k]) + "\n")
