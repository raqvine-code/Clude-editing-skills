# WORKED EXAMPLE (2026-11-27): the redo of "The story you tell yourself" built with this skill. Read it as a template.
# Set the environment variables below (or edit the constants) before running; the paths of the original session are not kept.
#   PROJECT = the edit's folder (src30.mp4, analysis/, assets/moves/, edl.json go there)   SKILL_ROOT = the folder that holds SKILL.md
#   ASSETS = folder with broll/, sfx_synth/, sfx_pick/ (Mixkit clips and the synthesised cues)   FACE_TRACK = json {"cx": [...]} per frame at the EDL fps
#!/usr/bin/env python3
"""QC of the render: colour fidelity vs source (no-grade check), caption block position, phone-size contact sheet inputs."""
import json, sys, os, subprocess, importlib.util
import numpy as np, cv2

P = os.path.dirname(os.path.abspath(__file__))
SK = os.environ.get("SKILL_ROOT", "../../../..")
spec = importlib.util.spec_from_file_location("shortkit", SK + "/02-craft/shorts-editing-pro/tools/shortkit.py"); sk = importlib.util.module_from_spec(spec); spec.loader.exec_module(sk)
e = sk.load(P + "/edl.json"); fps = e["fps"]
cap = cv2.VideoCapture(e["src"])
print("== colour fidelity (render vs source warped with the same camera), face/wall patch y<900")
d_all = []
for t in (3.0, 7.0, 10.0, 20.0, 27.0, 32.0, 43.0):
    fi = round(t * fps); cap.set(cv2.CAP_PROP_POS_FRAMES, fi); ok, src = cap.read()
    r = cv2.imread(f"{P}/work/frames/{fi:06d}.jpg")
    sc = sk.cam_scale(e, t); M, fx, fy = sk.cam_matrix(e, sc, 1080, 1920, 1080, 1920, 1, t)
    w = cv2.warpAffine(src, M, (1080, 1920), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    a = r[250:900, 150:930].astype(float).reshape(-1, 3).mean(0); b = w[250:900, 150:930].astype(float).reshape(-1, 3).mean(0)
    d = a - b; d_all.append(d); print(f"  t={t:5.1f}  render BGR {a.round(1)}  source BGR {b.round(1)}  diff {d.round(1)}")
print("  mean diff per channel (B,G,R):", np.mean(d_all, 0).round(2))

print("== caption block centre (haldi / cream pixels in y 950-1500, frames with a chest caption and no card)")
ys = []
for t in (2.6, 3.9, 7.4, 10.5, 13.9 - 0.9, 15.5, 19.3, 21.0, 25.4, 31.7, 33.2, 35.9, 42.9, 44.9):
    fi = round(t * fps); r = cv2.imread(f"{P}/work/frames/{fi:06d}.jpg")
    if r is None: continue
    z = r[950:1500].astype(int); b, g, rr = z[..., 0], z[..., 1], z[..., 2]
    mk = ((rr > 215) & (g > 150) & (b < 120)) | ((rr > 235) & (g > 232) & (b > 215))         # haldi or cream text pixels
    yy = np.where(mk.sum(1) > 6)[0]
    if len(yy): ys.append((t, 950 + yy.min(), 950 + yy.max())); print(f"  t={t:5.1f}  text rows y {950 + yy.min()}-{950 + yy.max()}  centre {(950 + (yy.min() + yy.max()) / 2) / 19.2:.1f} % of height")
c = [((a + b) / 2) / 19.2 for _, a, b in ys]; print("  median centre %.1f %%  (target 58-65 %%); lowest text row y %d (limit 1470)" % (np.median(c), max(b for _, _, b in ys)))
