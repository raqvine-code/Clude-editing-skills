#!/usr/bin/env python3
"""GTA 6 facts video: key word times (snapped to the audio), scene windows, camera, written to hc/timeline.json."""
import json, numpy as np
from scipy.io import wavfile
P = "/tmp/claude-0/-home-user-Clude-editing-skills/caacd18d-b81c-5599-b53c-5554b0dc2c6c/scratchpad/gta6/"
W = json.load(open(P + "src/words_master.json")); words = W["words"]; DUR = W["duration"]; FPS = 60; N = int(round(DUR * FPS))
sr, a = wavfile.read(P + "src/master16.wav"); a = a.astype(np.float32) / 32768; hop = 160; n = len(a) // hop
db = 20 * np.log10(np.sqrt((a[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-7); ref = np.percentile(db, 90)
def snap(t):
    for i in range(max(1, int((t - 0.15) * 100)), min(n - 1, int((t + 0.10) * 100))):
        if db[i] - ref > -22 and db[i - 1] - ref <= -22: return round(i / 100, 3)
    return round(t, 3)
T = [snap(w[0]) for w in words]
# key words by index in words_master.json (Telugu transcript, checked by hand against the translation)
KEYS = dict(gta1=1, release=3, famous=6, everyone=7, many=10, gta2=12, n13a=16, yearsA=17, whyA=18, whyB=21, story=23, not1=25, maps=26, not2=28,
            graphics=29, atall=32, not3=33, then=34, whatfor=35, money=39, timing=41, normally=43, game=44, release2=45, sells=51, after=53, hype=55,
            gradually=56, decrease=58, devs=61, nextgame=63, work=66, but=68, gta5=69, didnt=73, whenever=74, newg=75, oldg=77, more=80, profit=81,
            brings=82, onlythen=83, release3=85, so=86, gta6b=88, develop=91, n13b=93, didnttake=95, gta5c=96, gta6c=99, profit2=102, until=103,
            n13c=105, wait=107, meaning=109, moreimp=110, channel=115, subscribe=116)
K = {k: T[i] for k, i in KEYS.items()}; K["end"] = DUR
S = [  # scene id, start, end  (scene starts land on the word, or 2-6 frames before it)
 ("hook", 0.0, K["famous"] - 0.02), ("famous", K["famous"] - 0.02, K["everyone"]), ("spk1", K["everyone"], K["n13a"] - 0.60),
 ("n13", K["n13a"] - 0.60, K["whyB"]), ("why", K["whyB"], K["story"] - 0.30), ("notlist", K["story"] - 0.30, K["then"]),
 ("reason", K["then"], K["money"] - 0.06), ("moneytime", K["money"] - 0.06, K["normally"]), ("chart1", K["normally"], K["hype"] - 0.20),
 ("hype", K["hype"] - 0.20, K["devs"] - 0.30), ("chart2", K["devs"] - 0.30, K["but"]), ("but", K["but"], K["gta5"] - 0.04),
 ("vcover", K["gta5"] - 0.04, K["didnt"] - 0.40), ("vline", K["didnt"] - 0.40, K["newg"] - 0.10), ("scale", K["newg"] - 0.10, K["onlythen"]),
 ("delays", K["onlythen"], K["so"]), ("dev13", K["so"], K["gta5c"] - 0.06), ("vs", K["gta5c"] - 0.06, K["until"]), ("timeline", K["until"], K["moreimp"] - 0.10),
 ("outro", K["moreimp"] - 0.10, DUR)]
scenes = [dict(id=i, t0=round(a_, 3), t1=round(b_, 3)) for i, a_, b_ in S]
ft = json.load(open(P + "face_track.json"))
tl = dict(fps=FPS, dur=DUR, n=N, K=K, scenes=scenes, face=dict(cx=ft["cx"], cy=ft["cy"], fw=ft["fw"]), words=[[T[i], w[2]] for i, w in enumerate(words)])
json.dump(tl, open(P + "hc/timeline.json", "w"), ensure_ascii=False)
for s in scenes: print("%-10s %6.2f - %6.2f  (%.2f s)" % (s["id"], s["t0"], s["t1"], s["t1"] - s["t0"]))
