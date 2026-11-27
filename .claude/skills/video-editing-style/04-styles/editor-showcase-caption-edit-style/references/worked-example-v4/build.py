#!/usr/bin/env python3
"""v4 timeline: words (snapped to audio onsets), camera + face follow per frame, caption groups and the 12 components.
Writes hc/timeline.json for the browser compositor (hc/engine.js)."""
import json, os, re
import numpy as np
from scipy.io import wavfile

P = os.path.dirname(os.path.abspath(__file__))
FPS = 30
K = json.load(open(P + "/keeps.json"))
SRC_N = 1427      # face track length (the 1428th frame reuses the last)

# ---------------------------------------------------------------- output <-> source time
seg, of = [], 0.0
for a, b in K: seg.append((of, a, b)); of += b - a
DUR = round(of, 3); N = int(round(DUR * FPS))
def o2s(t):
    for o, a, b in seg:
        if t < o + (b - a) + 1e-9: return a + (t - o)
    return K[-1][1]
src_frame = [min(SRC_N - 1, int(round(o2s(i / FPS) * FPS))) for i in range(N)]
cuts = [round(o, 3) for o, a, b in seg[1:]]

# ---------------------------------------------------------------- words, onsets snapped to the trimmed audio
W = json.load(open(P + "/analysis/words_trim.json"))
sr, a = wavfile.read(P + "/analysis/voice_trim16.wav"); a = a.astype(np.float32) / 32768
hop = int(0.01 * sr); n = len(a) // hop; db = 20 * np.log10(np.sqrt((a[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-6)
ref = np.percentile(db[db > -50], 90)
def snap(t):
    i0, i1 = max(1, int((t - 0.15) * 100)), min(n - 1, int((t + 0.10) * 100))
    for i in range(i0, i1):
        if db[i] - ref > -24 and db[i - 1] - ref <= -24: return round(i / 100, 3)
    return t
words = []
for s, e, w, p in W:
    t = snap(s); t = max(t, words[-1][0] + 0.06) if words else t
    words.append([round(t, 3), re.sub(r"^-", "", w)])
norm = lambda s: re.sub(r"[^a-z']", "", s.lower())

# ---------------------------------------------------------------- the story as items that consume words in order
# word marks: *key (accent bold)  ~script (Great Vibes)  ^white bold  ;  item kinds: r7 r8 r8bold + components
ITEMS = [
    ("r7",       "*Story you tell yourself"),
    ("r8",       "about ~yourself"),
    ("converge", "is self creating"),
    ("r7",       "If you tell ^yourself that you"),
    ("C3",       "attract good things you are very lucky"),
    ("r7",       "You are more likely to see the *world"),
    ("C4",       "through a luck frame"),
    ("C5",       "And what I really | have been ~thinking about a lot | and there is the *research around this"),
    ("C6",       "This is not about the facts of our life It's about the frames of your life"),
    ("r7",       "When you begin to *think"),
    ("C7a",      "how am i"),
    ("r8",       "I'm ~interpreting the facts of my life"),
    ("C7b",      "how is my partner how is my colleague"),
    ("r7",       "You begin to see *patterns"),
    ("r7",       "And if you can ^truly see people for the"),
    ("C8",       "patterns that are repeating over and over again"),
    ("r8",       "We are truly ~understanding them"),
    ("C9",       "We are truly seeing them for who they are"),
    ("r7",       "If they want to *change it"),
    ("r8",       "the only way to change your ~self+narrative"),
    ("r7",       "really the *only *way is"),
    ("C10",      "through self conversation"),
    ("r8",       "So always be ~aware of how and what"),
    ("r8bold",   "you are talking to yourself"),
    ("C12",      "Share it with someone who needs to hear this"),
]
wi = 0; items = []
for kind, text in ITEMS:
    parts = [p.strip() for p in text.split("|")]; groups = []
    for part in parts:
        g = []
        for tok in part.split():
            mark = tok[0] if tok[0] in "*~^" else ""; tw = tok.lstrip("*~^"); t_first = None
            for sub_ in tw.split("+"):
                assert wi < len(words) and norm(words[wi][1]) == norm(sub_), (kind, sub_, words[wi] if wi < len(words) else None)
                t_first = words[wi][0] if t_first is None else t_first; wi += 1
            g.append([t_first, tw.replace("+", "-"), mark])
        groups.append(g)
    items.append(dict(kind=kind, groups=groups))
assert wi == len(words), ("unused words", words[wi:])
for i, it in enumerate(items):
    it["t0"] = it["groups"][0][0][0]
    nxt = items[i + 1]["groups"][0][0][0] if i + 1 < len(items) else DUR
    it["t1"] = round(nxt, 3)
items[0]["t0"] = 0.0
# a component starts a few frames before its first word so the picture lands on the word
LEAD = {"C3": 0.0, "C4": 0.10, "C5": 0.0, "C6": 0.0, "C7a": 0.03, "C7b": 0.0, "C8": 0.03, "C9": 0.0, "C10": 0.06, "C12": 0.0}
for it in items:
    if it["kind"] in LEAD: it["t0"] = round(it["t0"] - LEAD[it["kind"]], 3)
for i in range(1, len(items)): items[i - 1]["t1"] = min(items[i - 1]["t1"], items[i]["t0"])
CAPS = ("r7", "r8", "r8bold")
for i in range(len(items) - 1):
    a_, b_ = items[i], items[i + 1]
    if a_["kind"] not in CAPS: continue
    last = a_["groups"][-1][-1]
    if not (b_["kind"] in CAPS or (last[2] != "" and last[2] in "*~^") or a_["kind"] == "r8bold"): continue   # a small last word may cut on a component
    need = last[0] + 0.34; first = b_["groups"][0][0][0]
    if need > first:
        a_["t1"] = round(min(need, first + 0.30), 3); b_["show0"] = a_["t1"]

# ---------------------------------------------------------------- camera (output time): [t0, t1, s0, s1]
T = {it["kind"] + str(i): it for i, it in enumerate(items)}
def at(kind, k=0):
    return [it for it in items if it["kind"] == kind][k]
shots = []
def shot(t0, t1, s0, s1): shots.append([round(t0, 3), round(t1, 3), s0, s1])
c = lambda kind, k=0: at(kind, k)
shot(0.0, c("converge")["t0"], 1.14, 1.20)
shot(c("converge")["t0"], c("r7", 1)["t0"], 1.42, 1.46)
shot(c("r7", 1)["t0"], c("C3")["t0"], 1.16, 1.20)
shot(c("C3")["t0"], c("r7", 2)["t0"], 1.28, 1.28)
shot(c("r7", 2)["t0"], c("C4")["t0"], 1.38, 1.42)
shot(c("C4")["t0"], c("C5")["t0"], 1.12, 1.14)
shot(c("C5")["t0"], c("C6")["t1"], 1.10, 1.10)
shot(c("C6")["t1"], c("C7a")["t0"], 1.16, 1.20)
shot(c("C7a")["t0"], c("r8", 1)["t0"], 1.44, 1.46)
shot(c("r8", 1)["t0"], c("C7b")["t0"], 1.18, 1.22)
shot(c("C7b")["t0"], c("C7b")["t1"], 1.20, 1.20)
shot(c("C7b")["t1"], c("r7", 5)["t0"], 1.40, 1.44)
t_see = [w for w in c("r7", 5)["groups"][0] if w[1] == "see"][0][0]
shot(c("r7", 5)["t0"], t_see, 1.14, 1.18)
shot(t_see, c("C8")["t0"], 1.46, 1.48)
shot(c("C8")["t0"], c("C8")["t1"], 1.20, 1.20)
shot(c("C8")["t1"], c("C9")["t0"], 1.16, 1.22)
t_seeing = c("C9")["groups"][0][3][0]
shot(c("C9")["t0"], t_seeing, 1.42, 1.44)
shot(t_seeing, c("C9")["t1"], 1.20, 1.20)
cut33 = [x for x in cuts if 33 < x < 34][0]
shot(c("C9")["t1"], cut33, 1.14, 1.16)
t_change = [w for w in c("r7", 6)["groups"][0] if w[2] == "*"][0][0]
shot(cut33, t_change, 1.34, 1.36)
shot(t_change, c("r8", 3)["t0"], 1.48, 1.50)
cut36 = [x for x in cuts if 36 < x < 37.5][0]
shot(c("r8", 3)["t0"], cut36, 1.18, 1.22)
shot(cut36, c("C10")["t0"], 1.40, 1.42)
shot(c("C10")["t0"], c("C10")["t1"], 1.20, 1.20)
t_of = [w for w in c("r8", 4)["groups"][0] if w[1] == "of"][0][0]
shot(c("C10")["t1"], t_of, 1.40, 1.44)
cut41 = [x for x in cuts if 41 < x < 42][0]
shot(t_of, cut41, 1.16, 1.18)
shot(cut41, c("C12")["t0"], 1.42, 1.46)
shot(c("C12")["t0"], DUR, 1.10, 1.10)
punch = [t_change]                       # zoom-blur punch (R6)
focus = [0.0, c("C3")["t1"], c("C6")["t1"], c("C7b")["t1"], c("C8")["t1"], c("C9")["t1"], c("C10")["t1"]]

# ---------------------------------------------------------------- per-frame camera with face follow (shortkit maths)
ft = json.load(open(os.path.join(P, "..", "edit", "work", "face_track.json")))
cx = np.convolve(np.pad(np.array(ft["cx"], float), 30, mode="edge"), np.ones(61) / 61, mode="valid")
chin = np.convolve(np.pad(np.array(ft["bottom"], float), 15, mode="edge"), np.ones(31) / 31, mode="valid")
AY, EY = 715.0, 600.0
def scale_at(t):
    for t0, t1, s0, s1 in shots:
        if t0 <= t < t1: p = (t - t0) / max(1e-3, t1 - t0); return s0 + (s1 - s0) * p
    return shots[-1][3]
cam = []
for i in range(N):
    t = i / FPS; s = scale_at(t); f = src_frame[i]
    x0 = min(max(cx[f] - 540 / s, 0), 1080 - 1080 / s); y0 = min(max(AY - EY / s, 0), 1920 - 1920 / s)
    cam.append([round(s, 4), round(x0, 1), round(y0, 1), round((chin[f] - y0) * s, 1)])

# caption block centre = chin + 17 % of the height (R7), clamped to the chest band (58-65 %)
for it in items:
    f0 = min(N - 1, int(it["t0"] * FPS)); it["y"] = round(min(1250, max(1110, cam[f0][3] + 326)))

tl = dict(fps=FPS, dur=DUR, n=N, src_frame=src_frame, cam=cam, cuts=cuts, shots=shots, punch=punch, focus=focus, items=items,
          broll=dict(sunset=72, book=60, couple=49, coworkers=48, dominoes=60, eye=55))
json.dump(tl, open(P + "/hc/timeline.json", "w"))
print("duration %.2f s, %d frames, %d items, cuts %s" % (DUR, N, len(items), cuts))
for it in items: print("  %-8s %6.2f-%6.2f y=%d  %s" % (it["kind"], it["t0"], it["t1"], it["y"], " | ".join(" ".join(w[2] + w[1] for w in g) for g in it["groups"])))
