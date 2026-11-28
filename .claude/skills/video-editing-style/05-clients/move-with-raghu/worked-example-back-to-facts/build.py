#!/usr/bin/env python3
"""Move with Raghu "I'm back to facts" update (Telugu, 49.85 s): key-word times, scenes and Tenglish caption words.
Word times come from per-clip Whisper (clip 2's second half re-decoded in short windows). Writes hc/timeline.json."""
import json, re
P = "/tmp/claude-0/-home-user-Clude-editing-skills/caacd18d-b81c-5599-b53c-5554b0dc2c6c/scratchpad/mwr/"
DUR = 49.85; FPS = 60; N = int(round(DUR * FPS))
# Tenglish script, one entry per spoken word: [time on the joined video, word]; *word = yellow highlight
W = [
 [0.00, "Ee"], [0.18, "video"], [0.42, "ki"], [0.60, "andaru"], [1.04, "*support"], [1.42, "chestharu"], [1.90, "anukuntunnanu."],
 [2.40, "Guys,"], [3.02, "*wait"], [3.24, "*wait"], [3.42, "*wait"], [3.58, "*wait."],
 [3.70, "Nuvvu"], [4.06, "*unnava"], [4.70, "*poyava"], [5.24, "cheppu"], [5.68, "ani"], [6.00, "alochistharu"], [6.66, "kada?"],
 [7.10, "Endukante"], [7.36, "*comments"], [7.78, "lo"], [7.90, "ippati"], [8.18, "varaku"], [8.38, "chaala"], [8.62, "mandi"],
 [8.86, "\"Bro"], [9.00, "*unnava"], [9.34, "*poyava"], [9.60, "cheppu\""], [9.86, "ani comment"], [10.16, "chesaru."],
 [10.48, "Nannu"], [11.22, "ippati"], [11.54, "varaku"], [11.80, "meeru"], [12.12, "*support"], [12.50, "chesinanduku"],
 [12.94, "*thank"], [13.34, "*you"], [13.48, "so"], [13.60, "much!"],
 [13.90, "Manaki"], [14.32, "approximately"], [15.06, "Instagram"], [15.82, "lo"], [15.92, "*10K"], [16.24, "followers"], [16.74, "unnaru,"],
 [17.06, "first"], [17.44, "channel"], [17.68, "ki"], [17.74, "*27K"], [18.32, "subscribers"], [18.78, "unnaru,"],
 [19.06, "second"], [19.70, "channel"], [19.94, "ki"], [20.06, "*10K"], [20.42, "subscribers"], [20.96, "unnaru."],
 [21.10, "Idantha"], [21.86, "kooda"], [22.04, "*mee"], [22.22, "*valle"], [22.52, "vachindi."],
 [24.10, "Ivanni"], [24.60, "enduku"], [25.00, "cheptunnanu"], [25.46, "anukuntaru"], [25.90, "kada?"], [26.12, "Yes,"], [26.52, "akkadike"], [26.96, "vasthunnanu."],
 [27.63, "First"], [27.80, "lo"], [27.95, "nenu"], [28.19, "*facts"], [28.73, "channel"], [29.21, "chesevaadini."],
 [29.79, "Second"], [30.39, "channel lo"], [30.71, "*challenge"], [31.69, "and"], [32.11, "*entertainment"], [32.71, "content"], [33.13, "chesanu."],
 [33.69, "Ippudu"], [34.31, "malli"], [34.53, "*facts"], [34.99, "channel ki"], [35.45, "vasthunnanu."],
 [36.01, "So"], [36.49, "nannu"], [36.83, "ippati"], [37.11, "varaku"], [37.27, "*support"], [37.75, "chesina"], [38.15, "vallu"], [38.55, "evaraithe unnaro,"],
 [38.99, "ippudu"], [39.57, "kooda"], [39.77, "nannu"], [39.99, "alage"], [40.33, "*support"], [40.77, "chestharani"],
 [41.67, "*expect"], [42.31, "chesthunnanu."], [42.71, "Mari"], [43.25, "meeru"], [43.49, "nannu"], [43.69, "*support"], [44.21, "chestara"], [44.55, "leda?"],
 [44.73, "Mari"], [45.13, "finally ga"], [45.63, "nenu cheppalanukunnadi"], [46.37, "enti ante,"], [46.81, "first"], [47.81, "*follow"], [48.09, "chesukondi."],
 [48.49, "Next"], [48.77, "video lo"], [49.01, "matladatham."],
]
K = dict(support1=1.04, guys=2.40, wait1=3.02, wait2=3.24, wait3=3.42, wait4=3.58, unnava=4.06, poyava=4.70, kada=6.66, comments=7.36, chaala=8.38,
         bro=8.86, thank=12.94, insta=15.06, k10a=15.92, first=17.06, k27=17.74, second=19.06, k10b=20.06, idantha=21.10, mee=22.04,
         enduku=24.60, yes=26.12, akkadike=26.52, facts1=28.19, second2=29.79, challenge=30.71, entertain=32.11, ippudu=33.69, facts2=34.53,
         support3=37.27, support4=40.33, expect=41.67, mari=42.71, support5=43.69, leda=44.55, finallyw=45.13, follow=47.81, nextv=48.49)
S = [("hook", 0.0, 2.40), ("wait", 2.40, 3.70), ("toggle", 3.70, 7.10), ("comments", 7.10, 10.48), ("thanks", 10.48, 13.90),
     ("stats", 13.90, 21.10), ("you", 21.10, 22.90), ("why", 22.90, 27.63), ("channels", 27.63, 33.69), ("back", 33.69, 36.01),
     ("support", 36.01, 41.67), ("poll", 41.67, 45.13), ("finally", 45.13, 46.81), ("follow", 46.81, DUR)]
# caption lines: break after punctuation; at most 3 words and 22 characters
words = [[t, w.lstrip("*"), w.startswith("*")] for t, w in W]
groups, cur = [], []
for t, w, h in words:
    if cur and (len(cur) >= 3 or len(" ".join(x[1] for x in cur) + " " + w) > 22): groups.append(cur); cur = []
    cur.append([t, w, h])
    if re.search(r"[,.?!]$", w): groups.append(cur); cur = []
if cur: groups.append(cur)
caps = [dict(t0=g[0][0], t1=round(groups[i + 1][0][0] if i + 1 < len(groups) else DUR, 3), words=g) for i, g in enumerate(groups)]
ft = json.load(open(P + "face_track.json"))
tl = dict(fps=FPS, dur=DUR, n=N, K=K, scenes=[dict(id=i, t0=a, t1=b) for i, a, b in S], caps=caps, face=dict(cx=ft["cx"], cy=ft["cy"], fw=ft["fw"]))
json.dump(tl, open(P + "hc/timeline.json", "w"), ensure_ascii=False)
print(len(words), "words,", len(caps), "caption lines,", len(S), "scenes")

# ---------------- typography v2 (owner's reference, 2026-11-28): phrase lockups
# roles: B bold key (Montserrat 700, big)  b bold  l light (Montserrat 400)  s script (Great Vibes)  i italic serif (Cormorant)  ; "*" = yellow
LK = [
 # owner 2026-11-28: TWO LINES AT MOST per phrase ("3 lines look like more fonts, disturbing"). A phrase that needs more is split in two, so no word is lost.
 # t0, t1, centre-y, scale, lines: [[time, word, role], ...]
 (0.00, 1.42, 1235, 1.0, [[[0.00, "Ee", "l"], [0.18, "video", "l"], [0.42, "ki", "l"]], [[0.60, "andaru", "s"], [1.04, "support", "B*"]]]),
 (1.42, 2.40, 1235, 1.0, [[[1.42, "chestharu", "i"]], [[1.90, "anukuntunnanu", "b"]]]),
 (2.40, 3.70, 1235, 1.0, [[[2.40, "Guys,", "s"], [3.02, "wait", "B"]], [[3.24, "wait", "B"], [3.42, "wait", "B"], [3.58, "wait.", "B*"]]]),
 (10.48, 11.80, 1235, 1.0, [[[10.48, "Nannu", "s"]], [[11.22, "ippati", "l"], [11.54, "varaku", "l"]]]),
 (11.80, 12.94, 1235, 1.0, [[[11.80, "meeru", "l"], [12.12, "support", "B"]], [[12.50, "chesinanduku", "i"]]]),
 (12.94, 13.90, 1235, 1.0, [[[12.94, "Thank", "B"]], [[13.34, "you", "s"], [13.48, "so much!", "i"]]]),
 (21.10, 22.04, 960, 1.35, [[[21.10, "Idantha", "l"], [21.86, "kooda", "l"]]]),
 (22.04, 22.90, 960, 1.35, [[[22.04, "mee", "s"], [22.22, "valle", "B"]], [[22.52, "vachindi.", "i"]]]),
 (24.10, 25.46, 1235, 1.0, [[[24.10, "Ivanni", "l"], [24.60, "enduku", "B"]], [[25.00, "cheptunnanu", "i"]]]),
 (25.46, 26.12, 1235, 1.0, [[[25.46, "anukuntaru", "l"]], [[25.90, "kada?", "s"]]]),
 (26.12, 27.63, 1180, 1.0, [[[26.12, "Yes,", "s"], [26.52, "akkadike", "B"]], [[26.96, "vasthunnanu", "l"]]]),
 (33.69, 34.99, 1420, 0.9, [[[33.69, "Ippudu", "l"], [34.31, "malli", "s"]], [[34.53, "facts", "B*"]]]),
 (34.99, 36.01, 1420, 0.9, [[[34.99, "channel ki", "l"]], [[35.45, "vasthunnanu.", "i"]]]),
 (36.01, 38.15, 1235, 1.0, [[[36.01, "So", "l"], [36.49, "nannu", "l"], [36.83, "ippati varaku", "l"]], [[37.27, "support", "B"], [37.75, "chesina", "i"]]]),
 (38.15, 38.99, 1235, 1.0, [[[38.15, "vallu", "s"]], [[38.55, "evaraithe unnaro,", "l"]]]),
 (38.99, 39.99, 1235, 1.0, [[[38.99, "ippudu", "l"], [39.57, "kooda", "l"], [39.77, "nannu", "l"]]]),
 (39.99, 41.67, 1235, 1.0, [[[39.99, "alage", "s"], [40.33, "support", "B"]], [[40.77, "chestharani", "i"]]]),
 (45.13, 46.37, 1235, 1.0, [[[45.13, "finally ga", "s"]], [[45.63, "nenu", "l"], [45.85, "cheppalanukunnadi", "b"]]]),
 (46.37, 48.49, 1150, 1.0, [[[46.37, "enti ante,", "i"], [46.81, "first", "l"]], [[47.81, "follow", "B*"], [48.09, "chesukondi.", "s"]]]),
 (48.49, DUR, 1180, 1.0, [[[48.49, "Next", "s"], [48.77, "video lo", "l"]], [[49.01, "matladatham.", "B"]]]),
]
tl = json.load(open(P + "hc/timeline.json"))
tl["lockups"] = [dict(t0=a, t1=b, y=y, scale=sc, lines=ln) for a, b, y, sc, ln in LK]
json.dump(tl, open(P + "hc/timeline.json", "w"), ensure_ascii=False)
print(len(LK), "lockups")
