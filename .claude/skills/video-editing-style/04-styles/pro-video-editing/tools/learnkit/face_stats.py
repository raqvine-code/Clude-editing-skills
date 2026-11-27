"""Framing sizes, punch-in ratio, slow push and A-roll share from faces.txt (5 fps) + shots/shots.json. Run in the study folder."""
import json, numpy as np
sh = json.load(open('shots/shots.json')); dur = sh['dur']; sh = sh['shots']
F = {}
for l in open('faces.txt'):
    p = l.split()
    if len(p) == 5: F[(int(p[0][:5]) - 1) / 5.0] = [float(x) for x in p[1:]]
rows = []
for s in sh:
    ts = sorted(t for t in F if s['s'] + 0.1 <= t <= s['e'] - 0.1)
    if not ts: continue
    w = np.array([F[t][2] for t in ts])
    ramp = (w[-1] / w[0] - 1) * 100 / max(0.2, ts[-1] - ts[0]) if len(ts) >= 5 else None
    rows.append((s['i'], s['d'], float(np.median(w)), float(np.median([F[t][0] + F[t][2] / 2 for t in ts])), float(np.median([F[t][1] + F[t][3] / 2 for t in ts])), ramp, s['sat']))
ar = [r for r in rows if r[6] > 0.25]
if len(ar) < 5: print('too few colour shots with a face:', len(ar)); raise SystemExit
Wa = np.array([r[2] for r in ar]); base = np.percentile(Wa, 10)
print('frames with a face:', round(len(F) / (dur * 5) * 100), '%;  A-roll (colour shot with face):', round(sum(r[1] for r in ar) / dur * 100), '% of runtime')
print('face width / frame width: p10', round(float(base), 3), 'median', round(float(np.median(Wa)), 3), 'p90', round(float(np.percentile(Wa, 90)), 3), 'max', round(float(Wa.max()), 3))
ids = {r[0]: r for r in ar}; j = np.array([ids[i + 1][2] / ids[i][2] for i in ids if i + 1 in ids])
if len(j):
    pin = j[j > 1.1]
    print('consecutive A-roll cuts:', len(j), '| punch in', round(float((j > 1.1).mean()) * 100), '% | pull back', round(float((j < 0.91).mean()) * 100), '% | same', round(float(((j <= 1.1) & (j >= 0.91)).mean()) * 100), '%')
    if len(pin): print('punch-in ratio: median', round(float(np.median(pin)), 2), 'middle half', np.round(np.percentile(pin, [25, 75]), 2))
r_ = np.array([r[5] for r in ar if r[5] is not None and r[1] >= 2.0])
if len(r_): print('slow push on takes >=2 s: median', round(float(np.median(r_)), 2), '%/s; share pushing in', round(float((r_ > 0.3).mean()), 2), '(face-box measure, noisy)')
print('face centre: x', round(float(np.median([r[3] for r in ar])), 2), 'y', round(float(np.median([r[4] for r in ar])), 2))
