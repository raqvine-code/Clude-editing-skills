"""Overview sheets of a video with SRT text under each frame: 1 frame per STEP s, 6x5 tiles.
usage: vidsheet.py video.mp4 script.srt outdir [step=4] [t0] [t1]"""
import sys, os, subprocess
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
src, srt, out = sys.argv[1], sys.argv[2], sys.argv[3]
step = float(sys.argv[4]) if len(sys.argv) > 4 else 4.0
t0 = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
t1 = float(sys.argv[6]) if len(sys.argv) > 6 else 1e9
cues = []
for b in open(srt, encoding="utf-8").read().strip().split("\n\n"):
    L = b.split("\n"); a, e = L[1].split(" --> ")
    ts = lambda x: int(x[:2]) * 3600 + int(x[3:5]) * 60 + float(x[6:].replace(",", "."))
    cues.append((ts(a), ts(e), " ".join(L[2:])))
os.makedirs(out + "/raw", exist_ok=True)
if not os.listdir(out + "/raw"):
    args = [FF, "-v", "error", "-ss", str(t0)] + (["-to", str(t1)] if t1 < 1e8 else []) + ["-i", src, "-vf", f"fps=1/{step},scale=384:216", "-q:v", "3", out + "/raw/%05d.jpg"]
    subprocess.run(args, check=True)
files = sorted(os.listdir(out + "/raw"))
try: fnt = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 12); fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 14)
except Exception: fnt = fb = ImageFont.load_default()
C, R, W, H, LH = 6, 5, 384, 216, 32; per = C * R
for si in range(0, len(files), per):
    sh = Image.new("RGB", (C * W, R * (H + LH)), (22, 22, 22)); d = ImageDraw.Draw(sh)
    for k, f in enumerate(files[si:si + per]):
        i = si + k; t = t0 + i * step; x, y = (k % C) * W, (k // C) * (H + LH)
        sh.paste(Image.open(f"{out}/raw/{f}"), (x, y + LH))
        said = next((c[2] for c in cues if c[0] <= t < c[1]), "")
        d.text((x + 4, y + 1), f"{int(t // 60)}:{t % 60:04.1f}", fill=(255, 214, 0), font=fb)
        d.text((x + 4, y + 17), said[:64], fill=(215, 215, 215), font=fnt)
    sh.save(f"{out}/sheet_{si // per + 1:02d}.jpg", quality=80)
print("sheets", (len(files) + per - 1) // per, "frames", len(files))
