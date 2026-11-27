"""Track one shape per frame at 60 fps and classify its easing. (refs 70-74, 2026-10-09)
usage: FF=<ffmpeg path> python -I track.py video t0 t1 mode metric [thr]
  mode:   light | dark | nonwhite | green | bluepx | sat | luma   (luma = whole-frame brightness, metric ignored)
  metric: w | h | cx | cy | area | x0 | x1 | y0 | y1   (all 0-1 of the frame)
Pick t0/t1 tight around ONE move. Prints per-frame values (every 2nd frame), the start/end/duration of the move,
t10/t50/t90 as a fraction of the move against easing templates, and the overshoot.
Gotchas: noisy when the shape blurs into the background or changes colour mid-move (then read it by eye);
the 1st/99th percentile box ignores specks but also clips thin shapes; needs a clear start and end level."""
import sys, os, re, subprocess, numpy as np

FF = os.environ["FF"]
vid, t0, t1, mode, metric = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], sys.argv[5]
thr = float(sys.argv[6]) if len(sys.argv) > 6 else 128
W = 184
q = subprocess.run([FF, "-hide_banner", "-i", vid], capture_output=True, text=True).stderr
m = re.search(r"(\d{3,4})x(\d{3,4})", q)
ow, oh = int(m.group(1)), int(m.group(2))
H = int(round(W * oh / ow / 2) * 2)
p = subprocess.run([FF, "-v", "error", "-ss", str(t0), "-i", vid, "-t", str(t1 - t0),
                    "-vf", "fps=60,scale=%d:%d,format=rgb24" % (W, H), "-f", "rawvideo", "-"], capture_output=True)
raw = np.frombuffer(p.stdout, np.uint8)
n = len(raw) // (W * H * 3)
fr = raw[: n * W * H * 3].reshape(n, H, W, 3).astype(np.float32)

res = []
for i in range(n):
    a = fr[i]
    g = a.mean(2)
    if mode == "luma":
        res.append((i / 60 + t0, 0, 1, 0, 1, g.mean() / 255))
        continue
    sat = (a.max(2) - a.min(2)) / (a.max(2) + 1e-3)
    if mode == "light": mk = (g > thr) & (sat < 0.15)
    elif mode in ("dark", "nonwhite"): mk = g < thr
    elif mode == "green": mk = (a[:, :, 1] > a[:, :, 0] + 40) & (a[:, :, 1] > a[:, :, 2] + 40)
    elif mode == "bluepx": mk = a[:, :, 2] > a[:, :, 0] + 60
    elif mode == "sat": mk = sat > thr
    else: mk = g > 0
    ys, xs = np.nonzero(mk)
    if len(xs) < 4:
        res.append((i / 60 + t0, np.nan, np.nan, np.nan, np.nan, 0.0))
        continue
    res.append((i / 60 + t0, np.percentile(xs, 1) / W, np.percentile(xs, 99) / W,
                np.percentile(ys, 1) / H, np.percentile(ys, 99) / H, mk.mean()))
res = np.array(res)
t, x0, x1, y0, y1, ar = (res[:, k] for k in range(6))
M = {"w": x1 - x0, "h": y1 - y0, "cx": (x0 + x1) / 2, "cy": (y0 + y1) / 2,
     "area": ar, "x0": x0, "x1": x1, "y0": y0, "y1": y1}[metric]
if mode == "luma":
    M = ar
print("t:", " ".join("%.2f" % v for v in t[::2]))
print(metric + ":", " ".join("%.3f" % v if v == v else "nan" for v in M[::2]))
v = M[~np.isnan(M)]
if len(v) > 6:
    a, b = np.mean(v[:3]), np.mean(v[-3:])
    rng = b - a
    if abs(rng) > 0.02:
        pr = (M - a) / rng

        def cross(f):
            for k in range(len(pr) - 1):
                if not np.isnan(pr[k]) and pr[k] >= f:
                    return t[k]
            return np.nan

        s, e = cross(0.03), cross(0.97)
        d = e - s
        print("start %.3f end %.3f duration %.3f s (%.0f frames); from %.3f to %.3f" % (s, e, d, d * 60, a, b))
        if d > 0:
            print("t10 %.2f  t50 %.2f  t90 %.2f of the move  (linear .10/.50/.90 | outQuad .05/.29/.68 | outCubic .03/.21/.54 | "
                  "outQuart .02/.16/.44 | inOutCubic .29/.50/.71 | inOutQuad .16/.50/.78 | inCubic .46/.79/.97)"
                  % ((cross(0.1) - s) / d, (cross(0.5) - s) / d, (cross(0.9) - s) / d))
        ov = np.nanmax(pr)
        print("overshoot %.1f %%" % (100 * (ov - 1)) if ov > 1.02 else "no overshoot (peak %.2f)" % ov)
