#!/usr/bin/env python3
"""Extract master frames (60 fps index) as 1080x1368 crops of the picture window: frames.py t1,t2,... or frames.py all"""
import sys, os, cv2
P = os.path.dirname(os.path.abspath(__file__)); out = P + "/hc/frames/main/"; os.makedirs(out, exist_ok=True)
cap = cv2.VideoCapture(P + "/src/master.mov"); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
want = range(n) if sys.argv[1] == "all" else sorted({min(n - 1, int(round(float(t) * 60))) for t in sys.argv[1].split(",")})
for i in want:
    fn = out + "%05d.jpg" % i
    if os.path.exists(fn): continue
    cap.set(cv2.CAP_PROP_POS_FRAMES, i); ok, f = cap.read()
    if ok: cv2.imwrite(fn, f[253:1621], [cv2.IMWRITE_JPEG_QUALITY, 94])
print(len(os.listdir(out)), "frames in", out)
