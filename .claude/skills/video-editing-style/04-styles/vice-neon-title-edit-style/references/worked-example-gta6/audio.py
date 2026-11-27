#!/usr/bin/env python3
"""GTA 6 facts video: sound design from real recordings (owner's rule: no BGM, real sounds only).
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
clk = json.load(open(P + "/sfx_new/clock_catalog.json"))
for x in clk:
    if x.get("file"): credit[P + "/sfx_new/" + x["file"]] = dict(title=x["title"], creator=x["creator"], license=x["license"], landing=x["landing"])
CLOCK = [P + "/sfx_new/clock_3.mp3", P + "/sfx_new/clock_2.mp3", P + "/sfx_new/clock_0.mp3"]      # earshot rank: real ticks (clock_5 was synthesised: excluded)
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
  "scratch": [G("vinyl-scratch")] + OV["scratch"], "cash": [MX["kaching-1"]] if "kaching-1" in MX else OV["chime"], "clock": CLOCK,
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
    if role in HIT: kw.setdefault("align", "peak"); db = min(-9, db + 4)          # hits 4 dB hotter so they read as attacks over continuous speech
    E.append(dict(t=round(t, 3), role=role, file=pick(role), db=db, **kw))
st = lambda i: SC[i]["t0"]

# 1-2 hook: riser into the logo on "GTA 6", sub hit, the cover lands on "release" with a stamp
cue(0.0, "whoosh", -22, sweep=[.6, -.2]); cue(K["gta1"], "riser", -15, align="peak"); cue(K["gta1"], "deep", -12, align="peak")
cue(K["release"] - .05, "whoosh", -19, align="peak", sweep=[-.4, .4]); cue(K["release"] - .02, "impact", -16)
# 3 famous: one shutter per official clip
seg = (SC["famous"]["t1"] - st("famous")) / 4
for k in range(4): cue(st("famous") + k * seg, "shutter", -15)
# 4 speaker
cue(st("spk1"), "whoosh_rev", -22, align="peak"); cue(K["many"], "chime", -26)
# 5 neon 13
cue(st("n13"), "whoosh", -21, align="peak"); cue(K["n13a"], "riser", -14, align="peak"); cue(K["n13a"], "deep", -11, align="peak"); cue(K["yearsA"], "whoosh", -20, sweep=[-.5, .5])
cue(K["whyA"], "marker", -19); cue(SC["n13"]["t1"] - .1, "whoosh", -20, align="peak", sweep=[-.6, .6])
# 6 why
cue(K["whyB"], "pop", -17)
# 7 not for story / maps / graphics: card slides, a marker strike on each "kaadu", a stamp on "assalu kaadu"
cue(st("notlist"), "whoosh_rev", -21, align="peak")
for w in ("story", "maps", "graphics"): cue(K[w] - .14, "slide", -20)
for w in ("not1", "not2", "not3"): cue(K[w], "marker", -15)
cue(K["not3"], "impact", -16)
# 8 the real reason
cue(K["whatfor"], "whoosh_rev", -17, align="peak")
# 9 money / timing
cue(K["money"], "cash", -15); cue(K["timing"] - .12, "slide", -20); cue(K["timing"], "clock", -17, dur=1.0)
# 10-12 the normal game chart
cue(st("chart1"), "whoosh", -20, align="peak"); cue(K["release2"], "pop", -21); cue(K["sells"], "riser", -24, align="peak"); cue(K["sells"] - .05, "pop", -20)
cue(st("hype") + .02, "slide", -21); cue(K["decrease"], "whoosh_rev", -18, align="peak"); cue(K["decrease"] - .1, "pop", -23)
cue(st("chart2"), "whoosh", -20, align="peak"); cue(K["devs"], "marker", -20); cue(K["nextgame"], "pop", -20); cue(K["nextgame"] + .1, "chime", -25)
# 13-15 but... GTA V
cue(K["but"] - .12, "scratch", -19, align=None); cue(K["but"], "pop", -24)
cue(K["gta5"], "deep", -12, align="peak"); cue(K["gta5"] + .45, "shutter", -20); cue(K["gta5"] + .95, "cash", -16)
cue(st("vline"), "whoosh", -20, align="peak"); cue(K["didnt"] - .1, "key", -21, dur=1.3)
cue(SC["vline"]["t1"] - 1.0, "paper", -17); cue(SC["vline"]["t1"] - .6, "marker", -20)
# 16 profit bars
cue(st("scale"), "whoosh", -20, align="peak"); cue(K["oldg"] - .1, "slide", -22); cue(K["newg"], "slide", -22)
cue(K["profit"] - .03, "pop", -18); cue(K["brings"] + .3, "riser", -22, align="peak"); cue(K["brings"] + .2, "chime", -18); cue(K["brings"] + .2, "impact", -20)
# 17 timing proof
cue(st("delays"), "whoosh", -20, align="peak"); cue(st("delays") + .05, "paper", -18); cue(K["release3"] - .2, "paper", -18)
for j in range(2): cue(K["release3"] + .35 + j * .32 + .18, "marker", -18)
cue(K["release3"] + .35 + 2 * .32, "impact", -18); cue(K["release3"] + 1.3, "pop", -20)
# 18 not development
cue(st("dev13"), "whoosh_rev", -22, align="peak"); cue(K["develop"] - .05, "pop", -18); cue(K["didnttake"], "marker", -15); cue(K["didnttake"] + .1, "marker", -17); cue(K["didnttake"], "impact", -18)
# 19 V vs VI
cue(st("vs"), "whoosh", -20, align="peak"); cue(K["gta5c"] - .04, "impact", -20); cue(K["gta6c"] - .04, "impact", -19)
cue(K["profit2"] - .5, "pop", -20); cue(K["profit2"] - .45, "slide", -22)
# 20 payoff: year counter, neon 13, of waiting, milestones
cue(st("timeline"), "whoosh", -21, align="peak"); cue(st("timeline") + .01, "click", -22); cue(st("timeline") + .05, "key", -21, dur=.85)
cue(K["n13c"], "deep", -11, align="peak"); cue(K["n13c"] + .5, "whoosh", -21, sweep=[-.5, .5]); cue(K["wait"], "marker", -19)
for j in range(4): cue(st("timeline") + .1 + j * .2, "click", -24)
# attacks on cuts and card arrivals (earshot: visual events without an onset), foley on counters and meters
cue(st("spk1"), "knock", -14); cue(st("n13") + .01, "glitch", -13); cue(st("chart2"), "click", -14); cue(st("vline"), "click", -14)
cue(st("delays") + .01, "click", -14); cue(K["release3"] - .12, "knock", -13); cue(st("vcover") + .01, "impact", -14); cue(st("vs") + .01, "click", -14)
cue(st("reason") + .01, "knock", -14)
for w in ("maps", "graphics"): cue(K[w] - .1, "knock", -24)
cue(K["gradually"], "key", -25, dur=1.0)
for j in range(3): cue(K["release3"] + .35 + j * .32, "knock", -23)
# 21 outro
cue(st("outro"), "whoosh_rev", -22, align="peak"); cue(K["moreimp"], "chime", -25)
cue(K["subscribe"] - .05, "pop", -17); cue(K["subscribe"] + .45, "click", -15); cue(K["subscribe"] + .55, "chime", -18)

# ---------------- EDL for shortkit audio and the gate
sfx = [dict(t=e["t"], file=e["file"], db=e["db"], **{k: e[k] for k in ("sweep", "align", "dur") if e.get(k) is not None}) for e in E]
DESIGNED = {"hook": "mg_official_logo_cover", "famous": "mg_character_montage", "n13": "mg_neon_13", "notlist": "mg_not_for_cards", "moneytime": "mg_money_timing",
            "chart1": "mg_normal_game_chart", "hype": "mg_hype_meter", "chart2": "mg_next_game_curve", "vcover": "mg_gtav_cover_record", "vline": "mc_chart_gtav",
            "scale": "mg_profit_bars", "delays": "hl_delay_headlines", "vs": "mg_v_vs_vi", "timeline": "mg_13_years_timeline"}
layers = [dict(key=v, dir="-", t0=SC[k]["t0"], t1=SC[k]["t1"], behind=False) for k, v in DESIGNED.items()]
layers += [dict(key="txt_" + k, dir="-", t0=SC[k]["t0"], t1=SC[k]["t1"], behind=False) for k in ("spk1", "why", "reason", "but", "dev13", "outro")]
layers += [dict(key="hl_pcgamer_220m", dir="-", t0=round(SC["vline"]["t1"] - .6, 3), t1=SC["vline"]["t1"], behind=False),
           dict(key="mg_strike_development", dir="-", t0=K["didnttake"], t1=SC["dev13"]["t1"], behind=False),
           dict(key="mg_subscribe_button", dir="-", t0=round(K["subscribe"] - .05, 3), t1=DUR, behind=False)]
B = lambda key, a, b: dict(key=key, file="official/" + key, t0=round(a, 3), t1=round(b, 3), src=0)
broll = [B("cover_animation", 0, st("famous")), B("character_clips", st("famous"), SC["famous"]["t1"]),
         B("story_jason_lucia", K["story"] - .14, SC["notlist"]["t1"]), B("leonida_map", K["maps"] - .14, SC["notlist"]["t1"]), B("vice_city_skyline", K["graphics"] - .14, SC["notlist"]["t1"]),
         B("heist_vault", st("moneytime"), SC["moneytime"]["t1"]), B("vice_city_night", K["timing"] - .12, SC["moneytime"]["t1"]), B("gtav_cover", st("vcover"), SC["vcover"]["t1"]), B("v_and_vi_covers", st("vs"), SC["vs"]["t1"])]
caps = [dict(t0=c["t0"], t1=c["t1"], words=[[w[0], w[1], "n"] for w in c["words"]]) for c in tl["caps"]]
FONTS = P + "/hc/fonts/"
edl = dict(name="gta6_13_years", src=P + "/src/master.mov", fps=60, project=PROJ, keeps=[[0.0, DUR]],
           camera=[[0.0, 1.0, "linear"]], broll=broll, layers=layers, captions=caps, sfx=sfx,
           style=dict(cap_font=FONTS + "InterTight.ttf", key_font=FONTS + "PricedownBl.otf", serif_font=FONTS + "NotoSerifDisplay.ttf"),
           meta=dict(mg_events=sorted({round(e["t"], 2) for e in E}), renderer="gta6/hc (browser compositor)", layout="B framed window", captions="Tenglish"))
json.dump(edl, open(PROJ + "/edl.json", "w"), indent=1)
used = sorted({e["file"] for e in E})
lines = ["# Sound credits: GTA 6, 13 years", "", "All sound effects are real recordings (no music, no synthesised sounds). CC0 files need no credit; CC BY files are credited here.", ""]
for f in used:
    r = credit.get(f)
    if r and r["license"].startswith("by"): lines.append("- \"%s\" by %s (%s), %s" % (r["title"], r["creator"], r["license"].upper(), r["landing"]))
lines += ["", "CC0 clock ticks via Openverse/Freesound: " + "; ".join("\"%s\" by %s" % (credit[f]["title"], credit[f]["creator"]) for f in used if "/sfx_new/" in f),
          "Mixkit sounds (Mixkit Sound Effects Free License): " + ", ".join(sorted({os.path.basename(f) for f in used if "/mixkit/" in f})),
          "Ghost Editor CC0 sounds: " + ", ".join(sorted({os.path.basename(f) for f in used if "/ghost-cc0/" in f}))]
open(PROJ + "/sfx_credits.md", "w").write("\n".join(lines) + "\n")
c = collections.Counter(e["file"] for e in E)
print("cues", len(E), "| distinct files", len(c), "| max uses", max(c.values()), "| by role", dict(collections.Counter(e["role"] for e in E)))
