#!/usr/bin/env python3
"""Tenglish caption lines -> hc/timeline.json["caps"]. Pairs that must not break: GTA + number, 13 + years."""
import json, re, sys
sys.path.insert(0, "."); from tenglish import TE
tl = json.load(open("hc/timeline.json")); W = tl["words"]; DUR = tl["dur"]
words = []
for k, (tok, (t, te)) in enumerate(zip(TE, W)):
    if tok == "": continue
    parts = tok.split("|"); nxt = W[k + 1][0] if k + 1 < len(W) else DUR
    for j, p in enumerate(parts):
        m = re.match(r"(.*)@([\d.]+)$", p); txt, tt = (m.group(1), float(m.group(2))) if m else (p, t + (nxt - t) * j / len(parts))
        words.append([round(tt, 3), txt])
glue = lambda a, b: (a == "GTA" and re.match(r"\d", b)) or (a == "13" and b.startswith("years"))
units = []                                   # glued words travel together
for t, w in words:
    if units and glue(units[-1][-1][1], w): units[-1].append([t, w])
    else: units.append([[t, w]])
groups, cur = [], []
for u in units:
    nw = sum(len(x) for x in cur) + len(u); txt = " ".join(w for x in cur + [u] for _, w in x)
    if cur and (nw > 3 or len(txt) > 22): groups.append([w for x in cur for w in x]); cur = []
    cur.append(u)
    if re.search(r"[,.?]$", u[-1][1]): groups.append([w for x in cur for w in x]); cur = []
if cur: groups.append([w for x in cur for w in x])
tl["caps"] = [dict(t0=g[0][0], t1=round(groups[i + 1][0][0] if i + 1 < len(groups) else DUR, 3), words=g) for i, g in enumerate(groups)]
json.dump(tl, open("hc/timeline.json", "w"), ensure_ascii=False)
print(len(words), "words,", len(groups), "lines")
for c in tl["caps"]: print("%6.2f-%6.2f  %s" % (c["t0"], c["t1"], " ".join(w for _, w in c["words"])))
