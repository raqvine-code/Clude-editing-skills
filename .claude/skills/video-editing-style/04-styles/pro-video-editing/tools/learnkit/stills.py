"""stills.py <video> <out.jpg> <cols> <tile_w> t1 t2 ...  -> one sheet of full-quality stills from the ORIGINAL file (time-labelled)."""
import sys, subprocess, tempfile, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
FF = imageio_ffmpeg.get_ffmpeg_exe(); V, out, C, TW = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); ts = [float(x) for x in sys.argv[5:]]
fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 14); tmp = tempfile.mkdtemp(); ims = []
for i, t in enumerate(ts):
    subprocess.run([FF, "-v", "error", "-y", "-ss", str(t), "-i", V, "-frames:v", "1", "-q:v", "2", f"{tmp}/{i}.jpg"], check=True); ims.append(Image.open(f"{tmp}/{i}.jpg"))
TH = int(TW * ims[0].height / ims[0].width); R = (len(ims) + C - 1) // C
sh = Image.new("RGB", (C * TW, R * TH), (0, 0, 0)); d = ImageDraw.Draw(sh)
for i, im in enumerate(ims):
    x, y = (i % C) * TW, (i // C) * TH; sh.paste(im.resize((TW, TH), Image.LANCZOS), (x, y)); d.text((x + 4, y + 2), f"{ts[i]:.2f}", fill=(255, 230, 80), font=fb)
sh.save(out, quality=86); print(out, sh.size)
