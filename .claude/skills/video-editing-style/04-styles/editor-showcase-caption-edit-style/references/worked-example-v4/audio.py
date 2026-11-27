#!/usr/bin/env python3
"""Sound design for v4: real recordings from the bank, chosen per role (least-used first), at most 3 uses per file.
Writes proj/edl_v4.json (shortkit audio + the pre-edit gate) and proj/sfx_credits.md."""
import json, os, glob, subprocess, collections
P = os.path.dirname(os.path.abspath(__file__)); S = os.path.dirname(P)
SK = "/home/user/Clude-editing-skills/.claude/skills/video-editing-style"
BANK = SK + "/03-sound-type-assets/sound-and-music-design/assets"
PROJ = P + "/proj"; os.makedirs(PROJ + "/analysis", exist_ok=True); os.makedirs(PROJ + "/audio", exist_ok=True)
tl = json.load(open(P + "/hc/timeline.json")); K = json.load(open(P + "/keeps.json"))
items = tl["items"]; DUR = tl["dur"]
it = lambda kind, k=0: [x for x in items if x["kind"] == kind][k]
word = lambda x, w, n=0: [g for g in sum(x["groups"], []) if g[1].lower().strip("-") == w][n][0]

# ---------------- pools (real recordings): the bank by role, the CC0 ghost set, the Mixkit set fetched by id
cat = json.load(open(BANK + "/openverse-real/catalog.json")); credit = {}
OV = collections.defaultdict(list)
for r in cat:
    f = BANK + "/openverse-real/" + r["file"]; OV[r["role"]].append(f); credit[f] = r
G = lambda n: BANK + "/ghost-cc0/" + n + ".mp3"
MX = {os.path.basename(f).rsplit("_", 1)[0]: f for f in glob.glob(S + "/mixkit/*.mp3")}
POOL = {
  "whoosh": OV["whoosh"] + [MX[k] for k in ("whoosh-1", "whoosh-2", "whoosh-3") if k in MX],
  "whoosh_big": [MX[k] for k in ("whoosh-cine", "tech-digital-whoosh", "cinematic-film-flash") if k in MX] + OV["whoosh"][:2],
  "whoosh_rev": [G("whoosh-reverse")] + [f for f in OV["whoosh"] if "Backwards" in credit[f]["title"]] + OV["slide"][-2:],
  "slide": OV["slide"], "paper": OV["paper"] + [G("paper-riffle")], "paperflip": [G("paper-flip")] + OV["paper"][:2],
  "click": OV["click"] + OV["key"][:2], "key": OV["key"] + OV["click"][:2], "pop": OV["pop"],
  "impact": OV["impact"] + ([MX["wood-hit"]] if "wood-hit" in MX else []), "deep": [G("deep-boom")] + [MX[k] for k in ("cinematic-deep-boom", "impact-2", "impact-1") if k in MX],
  "riser": OV["riser"] + [G("riser-short"), G("swell-short")] + [MX[k] for k in ("riser-1", "cinematic-rumble-riser") if k in MX],
  "shutter": OV["shutter"], "chime": OV["chime"], "knock": OV["knock"], "marker": OV["marker"] + [MX[k] for k in ("marker-scribble", "pencil-write") if k in MX],
  "cloth": OV["cloth"],
}
use = collections.Counter()
def pick(role):
    pool = [f for f in POOL[role] if os.path.exists(f)]
    f = min(pool, key=lambda x: (use[x], pool.index(x)))
    assert use[f] < 3, ("pool exhausted", role); use[f] += 1; return f
E = []
def cue(t, role, db, **kw): E.append(dict(t=round(t, 3), role=role, file=pick(role), db=db, **kw))

# ---------------- events (each insert, move and stressed word gets the sound of what moves)
cue(0.00, "whoosh", -17, sweep=[0.45, 0.0]); cue(0.03, "impact", -19); cue(0.17, "chime", -21)
cue(word(it("r8"), "yourself"), "paper", -23)
cv = it("converge"); cue(word(cv, "self"), "whoosh", -16, sweep=[-0.85, -0.1]); cue(word(cv, "creating"), "whoosh", -16, sweep=[0.85, 0.1])
cue(word(cv, "creating") + 0.26, "impact", -14); cue(word(cv, "creating") + 0.28, "chime", -23)
cue(it("r7", 1)["t0"], "cloth", -20); cue(word(it("r7", 1), "yourself"), "knock", -22)
c3 = it("C3"); tB = word(c3, "good") - 0.08
cue(tB, "whoosh_big", -14); cue(word(c3, "good") + 0.42, "chime", -20); cue(word(c3, "lucky"), "pop", -19); cue(c3["t1"], "whoosh_rev", -19)
cue(word(it("r7", 2), "world"), "knock", -22)
c4 = it("C4"); tS = c4["groups"][0][1][0] - 0.04
cue(tS, "shutter", -14); cue(tS + 0.14, "key", -25); cue(word(c4, "luck"), "marker", -23); cue(c4["t1"] - 0.05, "click", -20)
c5 = it("C5"); cue(c5["t0"], "slide", -16); cue(word(c5, "thinking"), "marker", -24); tBook = word(c5, "research") - 0.18
cue(tBook, "slide", -16); cue(tBook + 0.06, "paper", -23); cue(word(c5, "research"), "pop", -21)
c6 = it("C6"); cue(c6["t0"], "deep", -13); cue(c6["t0"] + 0.02, "whoosh", -19); cue(word(c6, "facts"), "impact", -12)
cue(word(c6, "frames"), "paperflip", -14); cue(word(c6, "frames") + 0.10, "key", -24); cue(c6["t1"], "whoosh_rev", -19)
cue(word(it("r7", 3), "think"), "knock", -22)
c7a = it("C7a"); cue(c7a["groups"][0][0][0], "click", -18)
cue(word(it("r8", 1), "interpreting"), "paper", -24)
c7b = it("C7b"); tP = c7b["groups"][0][0][0]; tC = c7b["groups"][0][4][0]
cue(tP, "whoosh", -15, sweep=[0.7, -0.2]); cue(tP + 0.05, "click", -19); cue(tC, "whoosh", -15, sweep=[-0.7, 0.2]); cue(tC + 0.05, "click", -19); cue(c7b["t1"], "whoosh_rev", -20)
cue(word(it("r7", 4), "patterns"), "pop", -20)
r75 = it("r7", 5); cue(r75["t0"], "cloth", -20); cue(24.80, "cloth", -19); cue(word(r75, "if"), "click", -23); cue(word(r75, "truly"), "knock", -22); cue(word(r75, "see"), "cloth", -20)
c8 = it("C8"); cue(c8["t0"], "riser", -16, align="peak"); cue(c8["t0"], "impact", -15)
tRep = word(c8, "repeating")
for j in range(1, int((tRep - 0.02 - c8["t0"]) * 30 / 4) + 1):
    cue(c8["t0"] + j * 4 / 30, "key" if j % 2 else "click", -20)
cue(tRep - 0.02, "whoosh", -16); cue(tRep + 0.12, "knock", -21); cue(word(c8, "over"), "knock", -20); cue(word(c8, "over", 1), "knock", -20)
cue(word(c8, "again"), "impact", -16); cue(c8["t1"], "whoosh_rev", -20)
cue(word(it("r8", 2), "understanding"), "paper", -24)
c9 = it("C9"); tE = word(c9, "seeing") - 0.07; cue(tE, "whoosh_big", -15); cue(tE + 0.08, "chime", -21); cue(c9["t1"], "whoosh_rev", -20)
cuts = tl["cuts"]; cue([x for x in cuts if 33 < x < 34][0], "whoosh", -19, align="peak")
tCh = word(it("r7", 6), "change"); cue(tCh, "impact", -12); cue(tCh + 0.02, "whoosh", -18, sweep=[0.2, 0.7])
cue(word(it("r8", 3), "self-narrative"), "marker", -22); cue([x for x in cuts if 36 < x < 37.5][0], "whoosh", -19, align="peak")
cue(word(it("r7", 7), "only"), "impact", -17)
c10 = it("C10"); cue(c10["t0"], "riser", -16, align="peak"); cue(c10["t0"] + 0.01, "slide", -16); cue(c10["t0"] + 0.16, "pop", -20)
cue(word(c10, "self"), "paper", -24); cue(word(c10, "conversation"), "marker", -15); cue(c10["t1"], "whoosh_rev", -20)
cue(word(it("r8", 4), "aware"), "chime", -22); cue([x for x in cuts if 41 < x < 42][0], "cloth", -20)
rb = it("r8bold"); cue(rb["t0"] + 0.2, "chime", -23)
c12 = it("C12"); cue(c12["t0"] + 0.05, "pop", -20); tSome = word(c12, "someone")
cue([x for x in cuts if 42.5 < x < 43.2][0], "whoosh", -19, align="peak"); cue(tSome - 0.05, "whoosh", -16, sweep=[-0.2, -1.0]); cue(tSome + 0.05, "chime", -22); cue(word(c12, "this"), "deep", -17)

# ---------------- room-tone bed so nothing is ever silent (no music: client rule)
rt = OV["roomtone"][0]; bed = PROJ + "/audio/roomtone_bed.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "2", "-i", rt, "-t", str(DUR + 0.5), "-af", "highpass=f=80,lowpass=f=9000,afade=t=in:d=0.4,afade=t=out:st=%.2f:d=0.6" % (DUR - 0.2), "-ac", "2", "-ar", "48000", bed], check=True)
credit[bed] = credit[rt]

# ---------------- EDL for shortkit audio and for the gate
sfx = [dict(t=e["t"], file=e["file"], db=e["db"], **{k: e[k] for k in ("sweep", "align") if k in e}) for e in E]
sfx.append(dict(t=0.0, file=bed, db=-31))
mg = lambda key, a, b: dict(key=key, dir="-", t0=round(a, 3), t1=round(b, 3), behind=False)
layers = [mg("mg_hook_bubble", 0.15, it("converge")["t0"]), mg("txt_converge", it("converge")["t0"], it("converge")["t1"]), mg("mg_attract_lights", tB, c3["t1"]),
          mg("mg_luck_frame", tS, c4["t1"]), mg("mg_paper_board", c5["t0"], c5["t1"]), mg("mg_facts_frames", c6["t0"], c6["t1"]), mg("mg_pill_list", c7a["groups"][0][0][0], c7a["t1"]),
          mg("mg_pill_list_broll", c7b["t0"], c7b["t1"]), mg("mc_patterns", c8["t0"], tRep - 0.02), mg("txt_echo", tRep, c8["t1"]), mg("hl_self_conversation", c10["t0"], c10["t1"]),
          mg("mg_change_loop", tCh + 0.02, it("r7", 6)["t1"]), mg("mg_share_bubble", c12["t0"] + 0.05, tSome + 0.85)]
B = lambda key, a, b: dict(key=key, file="hc/frames/" + key, t0=round(a, 3), t1=round(b, 3), src=0)
broll = [B("sunset", tB, c3["t1"]), B("book", tBook, c5["t1"]), B("couple", tP, tC), B("coworkers", tC, c7b["t1"]), B("dominoes", tRep - 0.02, c8["t1"]), B("eye", tE, c9["t1"])]
caps = []                                   # every spoken word is on screen (captions and the words inside components)
for x in items:
    caps.append(dict(t0=x["t0"], t1=x["t1"], words=[[w[0], w[1], "k" if w[2] else "n"] for w in sum(x["groups"], [])]))
FONTS = P + "/hc/fonts/"
edl = dict(name="story_you_tell_yourself_v4", src=os.environ.get("SRC30", S + "/redo/src30.mp4"), fps=30, project=PROJ, keeps=K,
           camera=[[s[0], s[2], "linear"] for s in tl["shots"]], broll=broll, layers=layers, captions=caps, sfx=sfx,
           flashes=[dict(t=round(c4["t1"] - 0.05, 3), type="white")],
           style=dict(cap_font=FONTS + "Arimo.ttf", key_font=FONTS + "Arimo.ttf", serif_font=FONTS + "GreatVibes-Regular.ttf"),
           meta=dict(mg_events=sorted({round(e["t"], 2) for e in E}), renderer="v4/hc (browser compositor)"))
json.dump(edl, open(PROJ + "/edl_v4.json", "w"), indent=1)
src_facts = S + "/redo/analysis/facts.json"
if os.path.exists(src_facts): json.dump(json.load(open(src_facts)), open(PROJ + "/analysis/facts.json", "w"))
# credits: every CC BY file used
used = sorted({e["file"] for e in E} | {bed})
lines = ["# Sound credits (v4)", "", "All sound effects are real recordings. CC0 files need no credit; CC BY files are credited here.", ""]
for f in used:
    r = credit.get(f)
    if r and r["license"].startswith("by"): lines.append("- \"%s\" by %s (%s), %s" % (r["title"], r["creator"], r["license"].upper(), r["landing"]))
lines += ["", "Mixkit sounds (Mixkit Sound Effects Free License): " + ", ".join(sorted({os.path.basename(f) for f in used if "/mixkit/" in f})),
          "Ghost Editor CC0 sounds: " + ", ".join(sorted({os.path.basename(f) for f in used if "/ghost-cc0/" in f}))]
open(PROJ + "/sfx_credits.md", "w").write("\n".join(lines) + "\n")
c = collections.Counter(e["file"] for e in E)
print("cues", len(E), "+ bed | distinct files", len(c), "| max uses", max(c.values()), "| by role", dict(collections.Counter(e["role"] for e in E)))
