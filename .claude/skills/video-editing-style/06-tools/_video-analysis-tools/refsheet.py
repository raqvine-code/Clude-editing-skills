"""Overview sheets for a reference video: 1 frame per STEP s, 6x5 tiles, each labelled with its time and the words spoken
in that window (from YouTube json3 auto-captions).  usage: refsheet.py ref.mp4 captions.json3 outdir [step=1] [t0] [t1]"""
import sys, os, json, subprocess
from PIL import Image, ImageDraw, ImageFont
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
src, cap, out = sys.argv[1], sys.argv[2], sys.argv[3]
step = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
t0 = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
t1 = float(sys.argv[6]) if len(sys.argv) > 6 else 1e9
os.makedirs(out + "/raw", exist_ok=True)
words = []
for ev in json.load(open(cap)).get("events", []):
    if "segs" not in ev: continue
    base = ev.get("tStartMs", 0)
    for s in ev["segs"]:
        w = s.get("utf8", "").strip()
        if w: words.append(((base + s.get("tOffsetMs", 0)) / 1000, w))
dur = float(subprocess.run([FF, "-i", src], capture_output=True, text=True).stderr.split("Duration: ")[1].split(",")[0].split(":")[-1]) + 60 * int(subprocess.run([FF, "-i", src], capture_output=True, text=True).stderr.split("Duration: ")[1].split(":")[1])
t1 = min(t1, dur)
if not os.listdir(out + "/raw"):
    subprocess.run([FF, "-v", "error", "-ss", str(t0), "-to", str(t1), "-i", src, "-vf", f"fps=1/{step},scale=384:216", "-q:v", "3", out + "/raw/%05d.jpg"], check=True)
files = sorted(os.listdir(out + "/raw"))
try: fnt = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13); fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 15)
except Exception: fnt = fb = ImageFont.load_default()
C, R, W, H, LH = 6, 5, 384, 216, 34
per = C * R
for si in range(0, len(files), per):
    sh = Image.new("RGB", (C * W, R * (H + LH)), (22, 22, 22)); d = ImageDraw.Draw(sh)
    for k, f in enumerate(files[si:si + per]):
        i = si + k; t = t0 + i * step; x, y = (k % C) * W, (k // C) * (H + LH)
        sh.paste(Image.open(f"{out}/raw/{f}"), (x, y + LH))
        said = " ".join(w for tt, w in words if t - step / 2 <= tt < t + step / 2)
        d.text((x + 4, y + 2), f"{int(t // 60)}:{t % 60:04.1f}", fill=(255, 214, 0), font=fb)
        d.text((x + 4, y + 18), said[:60], fill=(220, 220, 220), font=fnt)
    sh.save(f"{out}/sheet_{si // per + 1:02d}.jpg", quality=80)
print("sheets", (len(files) + per - 1) // per, "frames", len(files))
