"""Aspect-agnostic labelled contact sheets (16:9, 1:1 and 9:16). (refs 70-74, 2026-10-09)
usage: FF=<ffmpeg path> python -I gsheet.py video t0 t1 fps cols tile_w outprefix [rows=5]
Each tile is labelled with its time in seconds; writes outprefix_NN.jpg sheets of cols x rows tiles. Needs PIL."""
import sys, os, subprocess, tempfile, shutil
from PIL import Image, ImageDraw, ImageFont
FF = os.environ["FF"]
src, t0, t1, fps, cols, tw, outp = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
rows = int(sys.argv[8]) if len(sys.argv) > 8 else 5
tmp = tempfile.mkdtemp()
subprocess.run([FF, "-v", "error", "-ss", f"{t0:.4f}", "-i", src, "-t", f"{t1 - t0:.4f}", "-vf", f"fps={fps},scale={tw}:-2", "-q:v", "3", f"{tmp}/%05d.jpg"], check=True)
fs = sorted(os.listdir(tmp)); LH = 14; per = cols * rows
th = Image.open(f"{tmp}/{fs[0]}").size[1]
fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 12)
for si in range(0, len(fs), per):
    chunk = fs[si:si + per]; R = (len(chunk) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, R * (th + LH)), (30, 30, 30)); d = ImageDraw.Draw(sh)
    for k, f in enumerate(chunk):
        i = si + k; t = t0 + i / fps; x, y = (k % cols) * tw, (k // cols) * (th + LH)
        sh.paste(Image.open(f"{tmp}/{f}"), (x, y + LH))
        d.text((x + 3, y + 1), f"{t:06.2f}s", fill=(255, 214, 0), font=fb)
    name = f"{outp}_{si // per + 1:02d}.jpg"; sh.save(name, quality=80); print(name, len(chunk))
shutil.rmtree(tmp)
