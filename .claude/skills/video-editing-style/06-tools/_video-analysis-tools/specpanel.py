"""Spectrogram panels (accompaniment stem) around given event times, red line = picture event.
usage: specpanel.py no_vocals.wav out.jpg "t1:label1,t2:label2,..." [pre=1.2] [post=1.8]"""
import sys, numpy as np, soundfile as sf
from scipy import signal as sg
from PIL import Image, ImageDraw, ImageFont
wav, out, spec = sys.argv[1], sys.argv[2], sys.argv[3]
pre = float(sys.argv[4]) if len(sys.argv) > 4 else 1.2; post = float(sys.argv[5]) if len(sys.argv) > 5 else 1.8
x, sr = sf.read(wav, dtype="float32"); x = x.mean(1) if x.ndim > 1 else x
items = [(float(s.split(":")[0]), s.split(":", 1)[1]) for s in spec.split(",")]
W, Hh, LH = 900, 170, 20
try: fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 14); fs = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 11)
except Exception: fb = fs = ImageFont.load_default()
sheet = Image.new("RGB", (W, len(items) * (Hh + LH)), (15, 15, 15)); d = ImageDraw.Draw(sheet)
for k, (t, lab) in enumerate(items):
    a = int(max(0, t - pre) * sr); b = int((t + post) * sr); seg = x[a:b]
    f, tt, Z = sg.stft(seg, sr, nperseg=1024, noverlap=1024 - 128)
    S = 20 * np.log10(np.abs(Z) + 1e-7)
    fmax = 14000; keep = f <= fmax; S = S[keep]; f = f[keep]
    # log-frequency remap to Hh rows (60 Hz .. fmax)
    rows = np.geomspace(60, fmax, Hh)[::-1]; idx = np.clip(np.searchsorted(f, rows), 0, len(f) - 1)
    img = S[idx]; lo, hi = np.percentile(img, 35), np.percentile(img, 99.7)
    img = np.clip((img - lo) / (hi - lo), 0, 1)
    rgb = np.stack([img ** 0.7 * 255, img ** 1.3 * 220, img ** 2.5 * 120], -1).astype(np.uint8)
    im = Image.fromarray(rgb).resize((W, Hh)); y = k * (Hh + LH)
    sheet.paste(im, (0, y + LH))
    ex = int((t - max(0, t - pre)) / (pre + post) * W); d.line([(ex, y + LH), (ex, y + LH + Hh)], fill=(255, 40, 40), width=2)
    for s in np.arange(-np.floor(pre * 10) / 10, post, 0.1):
        xx = int((t + s - max(0, t - pre)) / (pre + post) * W)
        d.line([(xx, y + LH + Hh - (8 if abs(round(s * 10) % 5) == 0 else 4)), (xx, y + LH + Hh)], fill=(200, 200, 200))
    for fq in (200, 1000, 5000):
        yy = y + LH + int(np.searchsorted(-rows, -fq) / len(rows) * Hh); d.text((W - 40, yy - 6), f"{fq//1000 if fq>=1000 else fq}{'k' if fq>=1000 else ''}", fill=(120, 200, 255), font=fs)
    d.text((6, y + 3), f"{int(t//60)}:{t%60:05.2f}  {lab}   (ticks = 0.1 s, red = picture event)", fill=(255, 214, 0), font=fb)
sheet.save(out, quality=88); print(out)
