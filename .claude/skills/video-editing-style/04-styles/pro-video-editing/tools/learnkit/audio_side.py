import json, numpy as np
from scipy.io import wavfile
from scipy.signal import stft
sr, x = wavfile.read('st.wav'); x = x.astype(np.float32) / 32768
L, R = x[:, 0], x[:, 1]; mid, side = (L + R) / 2, (L - R) / 2
db = lambda v: 20 * np.log10(np.sqrt(np.mean(v ** 2)) + 1e-9)
print('RMS dBFS mid', round(db(mid), 1), 'side', round(db(side), 1), 'L/R corr', round(float(np.corrcoef(L, R)[0, 1]), 3))
if np.corrcoef(L, R)[0, 1] > 0.999: print('NOTE: source is (near) mono - side-channel music/SFX numbers below are NOT valid')
hop = int(sr * 0.05)
n = len(side) // hop
se = np.array([db(side[i * hop:(i + 1) * hop]) for i in range(n)])
me = np.array([db(mid[i * hop:(i + 1) * hop]) for i in range(n)])
np.save('side_env.npy', se); np.save('mid_env.npy', me)
print('side level per 10 s (dBFS, median of 50 ms frames):')
row = []
for t in range(0, int(n * 0.05), 10):
    row.append(f"{int(np.median(se[t * 20:(t + 10) * 20]))}")
for i in range(0, len(row), 12): print(f"  {i * 10 // 60}:{i * 10 % 60:02d}  " + ' '.join(row[i:i + 12]))
# music gaps: side below -60 dB for >= 0.4 s
quiet = se < (np.median(se) - 15)
gaps, st_ = [], None
for i, q in enumerate(quiet):
    if q and st_ is None: st_ = i
    if not q and st_ is not None:
        if (i - st_) * 0.05 >= 0.4: gaps.append((round(st_ * 0.05, 2), round((i - st_) * 0.05, 2)))
        st_ = None
print('side-channel dropouts >=0.4 s (start,len):', gaps[:60], 'n', len(gaps))
# bursts on side: frame > local median(4 s) + 9 dB, rising edge
k = 40
med = np.array([np.median(se[max(0, i - k):i + k]) for i in range(n)])
hot = se > med + 9
ev = [round(i * 0.05, 2) for i in range(1, n) if hot[i] and not hot[i - 1]]
ev2 = []
for e in ev:
    if not ev2 or e - ev2[-1] > 0.3: ev2.append(e)
print('side bursts (+9 dB over local median):', len(ev2))
cuts = np.array(json.load(open('shots/shots.json'))['cuts']); evs = np.array(ev2)
near = lambda a, b, w: np.array([np.abs(b - t).min() <= w for t in a])
c_hit = near(cuts, evs, 0.2); e_hit = near(evs, cuts, 0.2)
print('cuts with a burst within 0.2 s:', int(c_hit.sum()), 'of', len(cuts), '=', round(c_hit.mean() * 100), '%;  bursts landing on a cut:', round(e_hit.mean() * 100), '%')
rng = np.random.default_rng(0); fake = rng.uniform(0, len(side) / sr, len(cuts))
print('chance level (random times):', round(near(fake, evs, 0.2).mean() * 100), '%')
json.dump({'bursts': ev2, 'gaps': gaps}, open('audio_ev.json', 'w'))
# spectral character of side: band energies
f, t, Z = stft(side, sr, nperseg=2048, noverlap=1024); P = (np.abs(Z) ** 2).mean(1)
tot = P.sum(); bands = [(20, 120), (120, 400), (400, 2000), (2000, 6000), (6000, 11000)]
print('side spectrum share:', {f'{a}-{b}Hz': round(float(P[(f >= a) & (f < b)].sum() / tot), 2) for a, b in bands})
f, t, Z = stft(mid, sr, nperseg=2048, noverlap=1024); P = (np.abs(Z) ** 2).mean(1); tot = P.sum()
print('mid spectrum share:', {f'{a}-{b}Hz': round(float(P[(f >= a) & (f < b)].sum() / tot), 2) for a, b in bands})
