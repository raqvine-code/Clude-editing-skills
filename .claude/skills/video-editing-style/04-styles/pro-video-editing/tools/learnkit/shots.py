"""shots.py <proxy> <outdir>: cuts (frame-diff, same rule as refscan), per-frame colour stats,
one mid-frame per shot (1280 wide jpg), and labelled contact sheets of every shot."""
import sys, os, json, subprocess, numpy as np
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
FF = imageio_ffmpeg.get_ffmpeg_exe()
p, out = sys.argv[1], sys.argv[2]
os.makedirs(out + "/mids", exist_ok=True)
import re as _re
_e = subprocess.run([FF, '-hide_banner', '-i', p], capture_output=True, text=True).stderr
_m = _re.search(r'Video: .*?(\d{3,5})x(\d{3,5}).*?([\d.]+) fps', _e); PW, PH, FPS = int(_m[1]), int(_m[2]), float(_m[3])
PORT = PH > PW
W = 64 if PORT else 128; H = int(round(W * PH / PW / 2) * 2)
pr = subprocess.Popen([FF, "-v", "error", "-i", p, "-vf", f"scale={W}:{H}", "-pix_fmt", "rgb24", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
prev, diffs, stats = None, [], []
while True:
    b = pr.stdout.read(W * H * 3)
    if len(b) < W * H * 3: break
    a = np.frombuffer(b, np.uint8).reshape(H, W, 3).astype(np.float32)
    g = a.mean(2)
    diffs.append(0.0 if prev is None else float(np.abs(g - prev).mean())); prev = g
    mx, mn = a.max(2), a.min(2)
    sat = float(((mx - mn) / (mx + 1)).mean())
    r, gg, bl = a[..., 0].mean(), a[..., 1].mean(), a[..., 2].mean()
    stats.append([float(g.mean()), sat, float(r - bl), float((g > 235).mean()), float((g < 40).mean()), float(r), float(gg), float(bl)])
diffs = np.array(diffs); stats = np.array(stats)
np.save(out + "/framediff.npy", diffs); np.save(out + "/stats.npy", stats)
k = max(3, int(FPS))
med = np.array([np.median(diffs[max(0, i - k):i + k]) for i in range(len(diffs))])
idx = [i for i in range(1, len(diffs)) if diffs[i] > max(14, 5 * med[i]) and diffs[i] >= diffs[max(0, i - 1):i + 2].max()]
cuts = []
for i in idx:
    c = round(i / FPS, 3)
    if not cuts or c - cuts[-1] > 0.2: cuts.append(c)
dur = len(diffs) / FPS
edges = [0.0] + cuts + [dur]
shots = []
for n, (a, b) in enumerate(zip(edges[:-1], edges[1:])):
    f0, f1 = int(a * FPS), max(int(a * FPS) + 1, int(b * FPS))
    s = stats[f0:f1].mean(0)
    shots.append({"i": n, "s": a, "e": b, "d": round(b - a, 2), "luma": round(float(s[0]), 1), "sat": round(float(s[1]), 3),
                  "warm": round(float(s[2]), 1), "white": round(float(s[3]), 3), "black": round(float(s[4]), 3)})
json.dump({"dur": dur, "cuts": cuts, "shots": shots}, open(out + "/shots.json", "w"))
for sh in shots:
    mid = sh["s"] + min(sh["d"] / 2, max(0.2, sh["d"] - 0.12))
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{mid:.3f}", "-i", p, "-frames:v", "1", "-q:v", "3", f"{out}/mids/{sh['i']:04d}.jpg"])
C, R, TW, LH = (10, 3, 156, 16) if PORT else (6, 7, 260, 16)
TH = int(TW * PH / PW)
fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 13)
for s0 in range(0, len(shots), C * R):
    sheet = Image.new("RGB", (C * TW, R * (TH + LH)), (20, 20, 20)); d = ImageDraw.Draw(sheet)
    for k_, sh in enumerate(shots[s0:s0 + C * R]):
        x, y = (k_ % C) * TW, (k_ // C) * (TH + LH)
        try: sheet.paste(Image.open(f"{out}/mids/{sh['i']:04d}.jpg").resize((TW, TH)), (x, y + LH))
        except Exception: pass
        m, s_ = divmod(sh["s"], 60)
        d.text((x + 3, y + 1), f"#{sh['i']} {int(m)}:{s_:04.1f} {sh['d']}s", fill=(255, 230, 80), font=fb)
    sheet.save(f"{out}/shots_{s0 // (C * R):02d}.jpg", quality=80)
ds = np.array([s["d"] for s in shots])
print("shots", len(shots), "per_min", round(len(shots) / dur * 60, 1), "mean", round(ds.mean(), 2), "median", round(float(np.median(ds)), 2),
      "p10", round(float(np.percentile(ds, 10)), 2), "p90", round(float(np.percentile(ds, 90)), 2), "max", ds.max())
print("<1s", int((ds < 1).sum()), "1-3s", int(((ds >= 1) & (ds < 3)).sum()), "3s+", int((ds >= 3).sum()))
for m in range(0, int(dur // 60) + 1):
    print(f"min{m}: {sum(1 for c in cuts if m * 60 <= c < m * 60 + 60)} cuts", end=" | ")
print()
