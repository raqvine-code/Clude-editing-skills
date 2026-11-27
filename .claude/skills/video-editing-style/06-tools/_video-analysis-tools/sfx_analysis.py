"""SFX / music forensic analysis of a reference video from Demucs stems + a frame-difference visual event track.
usage: sfx_analysis.py video.mp4 stems_dir cuts.txt out_prefix
Writes out_prefix.json (onsets with class, level vs bed, nearest visual event) and prints a summary."""
import sys, json, subprocess, numpy as np, soundfile as sf
from scipy import signal as sg
def _find_ffmpeg():
    import os, shutil
    for c in (os.environ.get("FFMPEG"), shutil.which("ffmpeg"), "/opt/homebrew/bin/ffmpeg", "/usr/local/bin/ffmpeg"):
        if c and os.path.exists(c):
            return c
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        raise SystemExit("ffmpeg not found: set FFMPEG=/path/to/ffmpeg or pip install imageio-ffmpeg")
FF = _find_ffmpeg()
vid, stems, cutf, outp = sys.argv[1:5]
v, sr = sf.read(stems + "/vocals.wav", dtype="float32"); m, _ = sf.read(stems + "/no_vocals.wav", dtype="float32")
v = v.mean(1); m = m.mean(1); n = min(len(v), len(m)); v, m = v[:n], m[:n]
db = lambda x: 20 * np.log10(np.maximum(x, 1e-9))
H = int(0.01 * sr)
def env(x):
    k = len(x) // H; return db(np.sqrt((x[:k * H].reshape(k, H) ** 2).mean(1)))
band = lambda x, lo, hi: sg.sosfilt(sg.butter(4, [lo, hi], "bandpass", fs=sr, output="sos") if lo else sg.butter(4, hi, "lowpass", fs=sr, output="sos"), x)
Ev, Em = env(v), env(m); Emh = env(band(m, 3000, 16000)); Eml = env(band(m, 0, 150)); Emm = env(band(m, 300, 3000))
T = len(Em)
bed = sg.medfilt(Em, 201)                       # 2 s running median = music bed
speech = Ev > np.percentile(Ev, 60) - 12
print(f"dur {n/sr:.1f}s | vocals 80th pct {np.percentile(Ev,80):.1f} dBFS | accompaniment median {np.median(Em):.1f} dBFS, 80th {np.percentile(Em,80):.1f}")
print(f"music-bed present (bed > -55 dBFS): {100*np.mean(bed > -55):.0f}% of time | voice minus bed under speech: median {np.median((Ev-bed)[speech]):.1f} dB, 10-90 pct {np.percentile((Ev-bed)[speech],10):.1f}..{np.percentile((Ev-bed)[speech],90):.1f}")
# onsets: spectral flux on the accompaniment
f, t, Z = sg.stft(m, sr, nperseg=1024, noverlap=1024 - 441); S = np.log1p(np.abs(Z) * 50)
flux = np.maximum(np.diff(S, axis=1), 0).sum(0); flux = np.r_[0, flux]
fl = flux / (sg.medfilt(flux, 101) + 1e-6)
pk, _ = sg.find_peaks(fl, height=3.0, distance=8)
ons = []
for p in pk:
    tt = t[p]; i = int(tt * 100)
    if i + 30 >= T or i < 30: continue
    peak = Em[i:i + 8].max(); loc_bed = np.median(Em[max(0, i - 150):i - 5])
    rise = peak - loc_bed
    if rise < 6: continue
    j = i; pkv = Em[i:i + 8].max()
    while j < min(T - 1, i + 300) and Em[j] > pkv - 12: j += 1
    durs = (j - i) / 100
    hi = Emh[i:i + 6].max() - Emh[max(0, i - 50):i - 2].mean(); lo = Eml[i:i + 10].max() - Eml[max(0, i - 50):i - 2].mean(); mid = Emm[i:i + 6].max() - Emm[max(0, i - 50):i - 2].mean()
    seg = m[int(tt * sr):int((tt + 0.12) * sr)]; sp = np.abs(np.fft.rfft(seg * np.hanning(len(seg)))); fr = np.fft.rfftfreq(len(seg), 1 / sr)
    cen = float((sp * fr).sum() / (sp.sum() + 1e-9))
    pre = Em[max(0, i - 60):i].mean() - Em[max(0, i - 150):i - 60].mean()   # rising energy before = whoosh/riser lead-in
    if lo > 10 and cen < 900: cls = "impact"
    elif durs < 0.09 and cen > 2500: cls = "click"
    elif durs < 0.15: cls = "pop/tick"
    elif pre > 4 or durs > 0.35: cls = "whoosh/riser"
    else: cls = "swell/hit"
    ons.append({"t": round(float(tt), 3), "rise_db": round(float(rise), 1), "dur": durs, "cen": int(cen), "lo": round(float(lo), 1), "hi": round(float(hi), 1), "cls": cls, "vs_voice": round(float(peak - np.percentile(Ev[max(0, i - 100):i + 100], 75)), 1)})
cuts = [float(x) for x in open(cutf).read().split()]
# visual event track: mean abs frame difference at 160x90
p = subprocess.Popen([FF, "-v", "error", "-i", vid, "-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
fps = float(subprocess.run([FF, "-i", vid], capture_output=True, text=True).stderr.split(" fps,")[0].split(",")[-1])
prev = None; diffs = []
while True:
    b = p.stdout.read(160 * 90)
    if len(b) < 160 * 90: break
    a = np.frombuffer(b, np.uint8).astype(np.int16)
    diffs.append(0 if prev is None else float(np.abs(a - prev).mean())); prev = a
diffs = np.array(diffs); vt = np.arange(len(diffs)) / fps
vpk, _ = sg.find_peaks(diffs, height=np.percentile(diffs, 90) + 1.0, distance=int(fps * 0.15))
vis = vt[vpk]
for o in ons:
    d = vis - o["t"]; k = int(np.argmin(np.abs(d))) if len(d) else 0
    o["vis_dt"] = round(float(-d[k]), 3) if len(d) else None          # onset minus visual event (+ = sound after picture)
    dc = np.array(cuts) - o["t"]; kc = int(np.argmin(np.abs(dc))); o["cut_dt"] = round(float(-dc[kc]), 3)
res = {"onsets": ons, "cuts": cuts, "vis_events": [round(float(x), 3) for x in vis], "fps": fps}
json.dump(res, open(outp + ".json", "w"), indent=0)
dur = n / sr
from collections import Counter
print(f"SFX-like onsets: {len(ons)} = {len(ons)/(dur/60):.1f}/min | classes {dict(Counter(o['cls'] for o in ons))}")
print(f"visual events (frame-diff peaks): {len(vis)} = {len(vis)/(dur/60):.1f}/min | scene cuts {len(cuts)} = {len(cuts)/(dur/60):.1f}/min")
near = [o for o in ons if abs(o['vis_dt']) <= 0.2]
print(f"onsets within 200 ms of a visual event: {len(near)}/{len(ons)} | median (sound - picture) {np.median([o['vis_dt'] for o in near]) if near else 'n/a'} s")
cut_hit = [min(abs(c - o['t']) for o in ons) <= 0.25 if ons else False for c in cuts]
print(f"scene cuts with an SFX onset within 250 ms: {sum(cut_hit)}/{len(cuts)}")
lv = np.array([o['vs_voice'] for o in ons]); print(f"SFX peak vs local voice (10 ms RMS, 75th pct): median {np.median(lv):.1f} dB, 10-90 {np.percentile(lv,10):.1f}..{np.percentile(lv,90):.1f}")
