#!/usr/bin/env python3
"""Move with Raghu "back to facts" update: sound design from real recordings (owner's rule: no BGM, real sounds only).
Every cue sits on a spoken key word or a picture move from hc/timeline.json. Writes proj/edl.json (shortkit audio + the
pre-edit gate) and proj/sfx_credits.md. Files: the bank (Openverse/Freesound by role), Ghost Editor CC0, Mixkit by id, new clock ticks."""
import json, os, glob, collections
P = os.path.dirname(os.path.abspath(__file__)); S = os.path.dirname(P)
SK = "/home/user/Clude-editing-skills/.claude/skills/video-editing-style"
BANK = SK + "/03-sound-type-assets/sound-and-music-design/assets"
PROJ = P + "/proj"; os.makedirs(PROJ + "/analysis", exist_ok=True); os.makedirs(PROJ + "/audio", exist_ok=True)
tl = json.load(open(P + "/hc/timeline.json")); K = tl["K"]; DUR = tl["dur"]; SC = {s["id"]: s for s in tl["scenes"]}

cat = json.load(open(BANK + "/openverse-real/catalog.json")); credit = {}
OV = collections.defaultdict(list)
for r in cat:
    f = BANK + "/openverse-real/" + r["file"]; OV[r["role"]].append(f); credit[f] = r
G = lambda n: BANK + "/ghost-cc0/" + n + ".mp3"
MX = {os.path.basename(f).rsplit("_", 1)[0]: f for f in glob.glob(S + "/mixkit/*.mp3")}
POOL = {
  "whoosh": OV["whoosh"] + [MX[k] for k in ("whoosh-1", "whoosh-2", "whoosh-3", "tech-digital-whoosh", "cinematic-film-flash") if k in MX],
  "whoosh_rev": [G("whoosh-reverse")] + [f for f in OV["whoosh"] if "Backwards" in credit[f]["title"]] + OV["slide"][-2:],
  "slide": OV["slide"], "paper": OV["paper"] + [G("paper-riffle"), G("paper-flip")],
  "click": OV["click"], "key": OV["key"], "pop": OV["pop"],
  "impact": OV["impact"] + [MX[k] for k in ("wood-hit", "impact-1", "impact-2") if k in MX],
  "deep": [G("deep-boom")] + [MX[k] for k in ("cinematic-deep-boom", "cinematic-cine-hit") if k in MX],
  "riser": OV["riser"] + [G("riser-short"), G("swell-short")] + [MX[k] for k in ("riser-1", "cinematic-rumble-riser") if k in MX],
  "shutter": OV["shutter"], "chime": OV["chime"], "knock": OV["knock"],
  "marker": OV["marker"] + [MX[k] for k in ("marker-scribble", "pencil-write") if k in MX],
  "scratch": [G("vinyl-scratch")] + OV["scratch"], "cash": [MX["kaching-1"]] if "kaching-1" in MX else OV["chime"],
  "heartbeat": OV["heartbeat"] + [MX[k] for k in ("cinematic-heartbeat",) if k in MX],
  "glitch": [G("glitch-hit")] + [MX[k] for k in ("tech-glitch-2",) if k in MX],
}
use = collections.Counter()
def pick(role):
    pool = [f for f in POOL[role] if os.path.exists(f)]
    f = min(pool, key=lambda x: (use[x], pool.index(x)))
    assert use[f] < 3, ("pool exhausted", role); use[f] += 1; return f
E = []
HIT = {"shutter", "impact", "pop", "click", "knock", "cash", "deep", "scratch", "chime", "glitch"}
def cue(t, role, db, **kw):
    if db > -25: db += 2                                                          # v2 (owner: "improve sound effects"): main cues 2 dB hotter
    if role in HIT: kw.setdefault("align", "peak"); db = min(-9, db + 4)          # hits 4 dB hotter so they read as attacks over continuous speech
    E.append(dict(t=round(t, 3), role=role, file=pick(role), db=db, **kw))
st = lambda i: SC[i]["t0"]

# every cue sits on a spoken key word or a picture move from hc/timeline.json (no music: owner's rule)
# 1 hook: riser into a soft impact on "support"
cue(K["support1"], "riser", -20, align="peak"); cue(K["support1"], "impact", -19)
# 2 wait: reverse whoosh on "Guys", four different hits, one per "wait", each with a punch-in
cue(K["guys"], "whoosh_rev", -20, align="peak")
cue(K["wait1"], "impact", -18); cue(K["wait2"], "knock", -17); cue(K["wait3"], "impact", -17); cue(K["wait4"], "deep", -14)
# 3 toggle: the knob clicks on each word, a pop on "kada"
cue(st("toggle"), "whoosh", -22, align="peak"); cue(K["unnava"], "click", -14); cue(K["poyava"], "click", -14); cue(K["kada"], "pop", -18)
# 4 comments: the list slides in, a pop per row, the marker swipes the quote
cue(st("comments"), "slide", -20); cue(K["comments"], "pop", -19)
for j in range(1, 4): cue(K["chaala"] + (j - 1) * .16, "pop", -22)
cue(K["bro"], "marker", -17)
# 5 thanks
cue(st("thanks"), "knock", -15); cue(K["thank"], "impact", -19); cue(K["thank"] + .4, "chime", -24)
# 6 stats: three cards, the numbers tick up and ding as he says them
cue(st("stats"), "whoosh", -21, align="peak")
for a, b in (("insta", "k10a"), ("first", "k27"), ("second", "k10b")):
    cue(K[a] - .12, "slide", -21); cue(K[b] - .45, "key", -22, dur=.45); cue(K[b], "chime", -21)
# 7 you: full-screen type on black, a big hit on "mee valle"
cue(st("you"), "whoosh", -20, align="peak"); cue(K["mee"], "deep", -13); cue(K["mee"] + .18, "impact", -18)
# 8 why: back to his face, pop on "enduku", the yellow line fills into the cut
cue(st("why"), "knock", -15); cue(K["enduku"], "pop", -18); cue(K["yes"], "pop", -21); cue(st("channels"), "riser", -23, align="peak")
# 9 channels: the cards land, the arrow travels from FACTS to CHALLENGE & ENTERTAINMENT
cue(st("channels"), "whoosh", -19, align="peak"); cue(K["facts1"], "click", -16); cue(K["challenge"] - .1, "slide", -20); cue(K["challenge"], "marker", -19); cue(K["entertain"], "click", -16)
# 10 back to facts: the arrow swings back, a hit on "facts"
cue(st("back"), "whoosh_rev", -18, align="peak"); cue(K["facts2"], "impact", -16)
# 11 support: soft pops on each "support", hearts rise on the second
cue(st("support"), "knock", -15); cue(K["support3"], "pop", -21); cue(K["support4"], "pop", -19); cue(K["support4"] + .2, "chime", -26)
# 12 poll: the card slides in, the cursor moves and taps YES
cue(st("poll"), "whoosh", -20, align="peak"); cue(K["support5"] - .45, "slide", -24); cue(K["support5"] + .42, "click", -14); cue(K["support5"] + .5, "chime", -21)
# 13 finally
cue(st("finally") - .02, "whoosh_rev", -20, align="peak"); cue(K["finallyw"] + .05, "knock", -16)
# 14 follow: the card rises, the cursor presses Follow -> Following
cue(K["follow"] - .55, "whoosh", -22, align="peak"); cue(K["follow"], "pop", -19); cue(K["follow"] + .2, "click", -18); cue(K["follow"] + .32, "chime", -23)
cue(K["nextv"], "whoosh_rev", -26, align="peak")

# gate: soft sounds where a new phrase lands, so no stretch runs over 1.3 s without an event, and a sound on every cut
cue(1.42, "whoosh", -27, align="peak"); cue(5.24, "slide", -25); cue(9.70, "key", -28, dur=.3); cue(11.80, "whoosh", -27, align="peak"); cue(12.12, "pop", -25)
cue(24.10, "whoosh", -27, align="peak"); cue(25.46, "pop", -25); cue(st("follow"), "knock", -16)
# more gap fillers, each on a phrase change or a stressed word (quiet, -25 to -28 dB)
cue(6.00, "click", -27); cue(11.22, "pop", -27); cue(26.96, "slide", -26); cue(29.21, "key", -28, dur=.25); cue(29.79, "slide", -22); cue(31.69, "click", -27); cue(32.90, "whoosh", -28, align="peak")
cue(34.99, "whoosh", -27, align="peak"); cue(38.15, "whoosh", -27, align="peak"); cue(38.99, "key", -28, dur=.25); cue(39.99, "whoosh", -28, align="peak"); cue(42.71, "click", -26)
cue(45.85, "pop", -25); cue(46.37, "whoosh", -27, align="peak"); cue(49.01, "knock", -29)
# v2 sound upgrade (owner 2026-11-28 "improve sound effects"; earshot: thin bottom, weak low end)
for k in ("support1", "facts2", "follow"): cue(K[k], "deep", -21)                 # a low layer under the three big reveals
for j in (2, 3): cue(K["chaala"] + (j - 1) * .16 + .2, "marker", -24)            # the marker swipes each comment, not only the first
cue(K["support4"] + .1, "heartbeat", -20)                                          # a heartbeat under the rising hearts

# ---------------- EDL for shortkit audio and the gate
sfx = [dict(t=e["t"], file=e["file"], db=e["db"], **{k: e[k] for k in ("sweep", "align", "dur") if e.get(k) is not None}) for e in E]
DESIGNED = {"toggle": "mg_unnava_poyava_switch", "comments": "mg_comment_list", "stats": "mg_stat_cards_counters", "you": "mg_fullscreen_type",
            "channels": "mg_channel_cards_arrow", "back": "mg_back_to_facts", "poll": "mg_community_poll", "follow": "mg_follow_card"}
layers = [dict(key=v, dir="-", t0=SC[k]["t0"], t1=SC[k]["t1"], behind=False) for k, v in DESIGNED.items()]
layers += [dict(key="txt_lk_%d" % j, dir="-", t0=L["t0"], t1=L["t1"], behind=False) for j, L in enumerate(tl["lockups"])]
layers += [dict(key="hl_comment_marker", dir="-", t0=K["bro"], t1=SC["comments"]["t1"], behind=False),
           dict(key="mc_arrow_swings_back", dir="-", t0=SC["back"]["t0"], t1=SC["back"]["t1"], behind=False),
           dict(key="mg_progress_line", dir="-", t0=K["yes"], t1=SC["why"]["t1"], behind=False),
           dict(key="mg_hearts", dir="-", t0=K["support4"], t1=SC["support"]["t1"], behind=False)]
edl = dict(name="mwr_back_to_facts", src=P + "/src/master.mov", fps=60, project=PROJ, keeps=[[0.0, DUR]],
           camera=[[0.0, 1.0, "linear"]], broll=[], layers=layers, captions=[], sfx=sfx,
           style=dict(cap_font=P + "/hc/fonts/Montserrat.ttf", key_font=P + "/hc/fonts/Montserrat.ttf", serif_font=P + "/hc/fonts/CormorantItalic.ttf"),
           meta=dict(mg_events=sorted({round(e["t"], 2) for e in E}), renderer="mwr/hc (browser compositor)", layout="B framed window",
                     captions="Tenglish phrase lockups, two lines max (owner 2026-11-28)", broll="none: designed graphics from his own screenshots, as he asked"))
json.dump(edl, open(PROJ + "/edl.json", "w"), indent=1)
used = sorted({e["file"] for e in E})
lines = ["# Sound credits: Move with Raghu, back to facts", "", "All sound effects are real recordings (no music, no synthesised sounds). CC0 files need no credit; CC BY files are credited here.", ""]
for f in used:
    r = credit.get(f)
    if r and r["license"].startswith("by"): lines.append("- \"%s\" by %s (%s), %s" % (r["title"], r["creator"], r["license"].upper(), r["landing"]))
lines += ["", "Mixkit sounds (Mixkit Sound Effects Free License): " + ", ".join(sorted({os.path.basename(f) for f in used if "/mixkit/" in f})),
          "Ghost Editor CC0 sounds: " + ", ".join(sorted({os.path.basename(f) for f in used if "/ghost-cc0/" in f}))]
open(PROJ + "/sfx_credits.md", "w").write("\n".join(lines) + "\n")
c = collections.Counter(e["file"] for e in E)
print("cues", len(E), "| distinct files", len(c), "| max uses", max(c.values()), "| by role", dict(collections.Counter(e["role"] for e in E)))
