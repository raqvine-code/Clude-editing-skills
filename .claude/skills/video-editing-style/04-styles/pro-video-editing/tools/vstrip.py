"""Aspect-correct frame strip (works for 9:16 and 16:9): every frame from t0 to t1 at the source fps (or FPS),
labelled with time and frame index.  usage: vstrip.py video t0 t1 out.jpg [fps=src] [tile_w=150] [cols=10]"""
import sys, os, subprocess, tempfile, shutil, re
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refscan import FF, probe
src, t0, t1, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
m = probe(src)
fps = float(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[5] != "src" else m["fps"]
tw = int(sys.argv[6]) if len(sys.argv) > 6 else 150
C = int(sys.argv[7]) if len(sys.argv) > 7 else 10
crop = os.environ.get("CROP")  # e.g. CROP=1080:608:0:656 for 16:9 letterboxed inside 9:16
cw, ch = (int(crop.split(":")[0]), int(crop.split(":")[1])) if crop else (m["w"], m["h"])
th = int(tw * ch / cw)
tmp = tempfile.mkdtemp()
vf = (f"crop={crop}," if crop else "") + f"fps={fps},scale={tw}:{th}"
subprocess.run([FF, "-v", "error", "-ss", f"{t0:.3f}", "-i", src, "-t", f"{t1 - t0:.3f}", "-vf", vf,
                "-q:v", "3", f"{tmp}/%04d.jpg"], check=True)
fs = sorted(os.listdir(tmp)); R = (len(fs) + C - 1) // C; LH = 14
sh = Image.new("RGB", (C * tw, R * (th + LH)), (20, 20, 20)); d = ImageDraw.Draw(sh)
try: fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 11)
except Exception: fb = ImageFont.load_default()
for i, f in enumerate(fs):
    x, y = (i % C) * tw, (i // C) * (th + LH); sh.paste(Image.open(f"{tmp}/{f}"), (x, y + LH))
    d.text((x + 2, y + 1), f"{t0 + i / fps:.2f}s f{int(round((t0 + i / fps) * m['fps']))}", fill=(255, 214, 0), font=fb)
sh.save(out, quality=85); shutil.rmtree(tmp); print(out, len(fs), "frames @", fps)
