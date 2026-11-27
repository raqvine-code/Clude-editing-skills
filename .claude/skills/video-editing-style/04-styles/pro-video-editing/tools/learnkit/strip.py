"""strip.py name:start:dur:fps ...  -> strips/<name>.jpg (6 cols, time-labelled)"""
import sys, os, subprocess, tempfile, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
FF = imageio_ffmpeg.get_ffmpeg_exe(); os.makedirs('strips', exist_ok=True)
fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 12)
import re
_e = subprocess.run([FF, '-hide_banner', '-i', 'proxy.mp4'], capture_output=True, text=True).stderr
_m = re.search(r'Video: .*?(\d{3,5})x(\d{3,5})', _e); PW, PH = int(_m[1]), int(_m[2])
C, TW, LH = (12, 128, 14) if PH > PW else (6, 256, 14)
TH = int(TW * PH / PW / 2) * 2
for spec in sys.argv[1:]:
    name, st, du, fps = spec.split(':'); st, du, fps = float(st), float(du), float(fps)
    tmp = tempfile.mkdtemp()
    subprocess.run([FF, "-v", "error", "-ss", str(st), "-i", "proxy.mp4", "-t", str(du), "-vf", f"fps={fps},scale={TW}:{TH}", "-q:v", "3", f"{tmp}/%04d.jpg"], check=True)
    fs = sorted(os.listdir(tmp)); R = (len(fs) + C - 1) // C
    sh = Image.new("RGB", (C * TW, R * (TH + LH)), (20, 20, 20)); d = ImageDraw.Draw(sh)
    for k, f in enumerate(fs):
        x, y = (k % C) * TW, (k // C) * (TH + LH)
        sh.paste(Image.open(f"{tmp}/{f}"), (x, y + LH)); t = st + k / fps
        d.text((x + 3, y), f"{int(t // 60)}:{t % 60:05.2f}", fill=(255, 230, 80), font=fb)
    sh.save(f"strips/{name}.jpg", quality=80); print(name, len(fs), sh.size)
