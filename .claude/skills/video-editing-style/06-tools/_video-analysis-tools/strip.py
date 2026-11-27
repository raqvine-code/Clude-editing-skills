"""Frame-accurate strip: frames from t0 to t1 at FPS, 8 per row, each labelled with its time (s, 2 decimals).
usage: strip.py video.mp4 t0 t1 fps out.jpg [tile_w=320]"""
import sys, os, subprocess, tempfile, shutil
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
src, t0, t1, fps, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
tw = int(sys.argv[6]) if len(sys.argv) > 6 else 320; th = tw * 9 // 16
tmp = tempfile.mkdtemp()
subprocess.run([FF, "-v", "error", "-ss", f"{t0:.3f}", "-i", src, "-t", f"{t1 - t0:.3f}", "-vf", f"fps={fps},scale={tw}:{th}", "-q:v", "3", f"{tmp}/%04d.jpg"], check=True)
fs = sorted(os.listdir(tmp)); C = 8; R = (len(fs) + C - 1) // C; LH = 18
sh = Image.new("RGB", (C * tw, R * (th + LH)), (20, 20, 20)); d = ImageDraw.Draw(sh)
try: fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 13)
except Exception: fb = ImageFont.load_default()
for i, f in enumerate(fs):
    x, y = (i % C) * tw, (i // C) * (th + LH); sh.paste(Image.open(f"{tmp}/{f}"), (x, y + LH))
    t = t0 + i / fps; d.text((x + 4, y + 2), f"{int(t // 60)}:{t % 60:05.2f}", fill=(255, 214, 0), font=fb)
sh.save(out, quality=82); shutil.rmtree(tmp); print(out, len(fs))
