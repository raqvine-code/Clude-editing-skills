# WORKED EXAMPLE (2026-11-27): the redo of "The story you tell yourself" built with this skill. Read it as a template.
# Set the environment variables below (or edit the constants) before running; the paths of the original session are not kept.
#   PROJECT = the edit's folder (src30.mp4, analysis/, assets/moves/, edl.json go there)   SKILL_ROOT = the folder that holds SKILL.md
#   ASSETS = folder with broll/, sfx_synth/, sfx_pick/ (Mixkit clips and the synthesised cues)   FACE_TRACK = json {"cx": [...]} per frame at the EDL fps
#!/usr/bin/env python3
"""Project build: writes moves.json (caption_moves layers), edl.json (shortkit) and analysis/facts.json.
Client bar (Naveen bro, newest first): no BGM, no grade, Poppins + Playfair only, captions on the chest, haldi / kumkum / cream / ink."""
import json, os, re, subprocess
import numpy as np

P = os.environ.get("PROJECT", ".")
SK = os.environ.get("SKILL_ROOT", "../../../..")
ASSETS = os.environ.get("ASSETS", "./assets_in")
FACE_TRACK = os.environ.get("FACE_TRACK", P + "/analysis/face_track.json")
F = SK + "/03-sound-type-assets/fonts-and-colours/assets/fonts"
B = ASSETS + "/broll"
SFXD = ASSETS
OUT = 47.6
HALDI, KUMKUM, CREAM, INK, PAPER, DHALDI = "#E2AA2C", "#C8372D", "#F4EFE3", "#1A1410", "#EFE7D6", "#B9831A"
POP, SHIM, WOOSH_S, WOOSH_M, WOOSH_A, TICK_L, TICK_M, TICK_H = "sfx_synth/pop.wav", "sfx_synth/shimmer.wav", "sfx_synth/whoosh_short.wav", "sfx_synth/whoosh_med.wav", "sfx_pick/whoosh_a.wav", "sfx_synth/tick_lo.wav", "sfx_synth/tick_mid.wav", "sfx_synth/tick_hi.wav"
BOOM_S, BOOM_SOFT, IMPACT, SHUTTER, SCRATCH, PAPERS, PAGE, SLIDE, RISER, WBOOM = "sfx_synth/boom_sub.wav", "sfx_synth/boom_soft.wav", "sfx_pick/impact.wav", "sfx_pick/shutter.wav", "sfx_synth/scratch.wav", "sfx_synth/paper.wav", "sfx_pick/page.wav", "sfx_pick/slide.wav", "sfx_synth/riser.wav", "sfx_synth/whoosh_boom.wav"

# ---------------------------------------------------------------- caption-move layers (global times -> relative to each layer's t0)
CARD_RECT = [150, 230, 930, 1060]
L = {}      # key -> (t0, t1)
moves = []


def add(key, t0, t1, **kw):
    L[key] = (t0, t1); moves.append(dict(key=key, dur=round(t1 - t0, 3), **kw)); return t0


def R(t0, t):
    return round(t - t0, 3)


t0 = add("mg_hook_card", 0.0, 2.30, kind="typecard", bg=INK, fg=CREAM,
         heroes=[dict(text="STORY", t=0.0, width=0.80, y=1235, color=HALDI)],
         lines=[dict(text="you tell yourself", t=R(0, 0.35), t1=R(0, 1.17), pos="under-right", font="script", size=62),
                dict(text="about yourself", t=R(0, 1.19), pos="under-right", font="script", size=62)],
         window=dict(rect=CARD_RECT, radius=56, shrink=0.28, release=0.28, border=dict(width=0, color=HALDI)))
t0 = add("mg_good_things", 4.30, 6.25, kind="typecard", bg=PAPER, fg=INK,
         heroes=[dict(text="GOOD THINGS", t=R(4.30, 4.56), width=0.86, y=1235, color=DHALDI),
                 dict(text="LUCKY", t=R(4.30, 5.43), solid_t=R(4.30, 5.82), width=0.66, y=1235, color=DHALDI)],
         lines=[dict(text="attract", t=R(4.30, 4.33), hero=0, pos="over-left", font="script", size=64),
                dict(text="you are very", t=R(4.30, 5.43), hero=1, pos="over-left", font="script", size=64)],
         window=dict(rect=CARD_RECT, radius=56, shrink=0.25, release=0.22))
t0 = add("mg_luck_frame", 8.10, 9.45, kind="typecard", bg=INK, fg=CREAM, bg_alpha=0.84,
         heroes=[dict(text="FRAME", t=R(8.10, 8.50), width=0.56, y=1330, color=HALDI)],
         lines=[dict(text="through a luck", t=R(8.10, 8.28), pos="over-left", font="script", size=62, color=CREAM)],
         window=dict(rect=[120, 300, 960, 1190], radius=40, shrink=0.26, release=0.25, border=dict(width=14, color=HALDI)))
t0 = add("mg_facts", 15.70, 16.82, kind="typecard", bg=INK, fg=CREAM,
         heroes=[dict(text="FACTS", t=R(15.70, 15.76), width=0.78, y=1235, color=CREAM)],
         lines=[dict(text="of our life", t=R(15.70, 16.03), pos="under-right", font="script", size=60)],
         strike=dict(t=R(15.70, 16.36), c=KUMKUM, h=20), window=dict(rect=CARD_RECT, radius=56, shrink=0.18))
t0 = add("mg_frames", 16.82, 18.45, kind="typecard", bg=PAPER, fg=INK,
         heroes=[dict(text="FRAMES", t=R(16.82, 17.35), width=0.80, y=1235, color=DHALDI)],
         lines=[dict(text="it's about the", t=R(16.82, 16.82), pos="over-left", font="script", size=62),
                dict(text="of your life", t=R(16.82, 17.75), pos="under-right", font="script", size=60)],
         window=dict(rect=CARD_RECT, radius=56, shrink=0.18, release=0.25, border=dict(width=14, color=HALDI)))
t0 = add("mg_questions", 19.70, 24.58, kind="tiles", x=540, y=1388, n=3, size=84, gap=128, fill=HALDI, rim="#F6D27A", text=INK,
         pop=[R(19.70, 19.80), R(19.70, 22.74), R(19.70, 23.62)], labels=["ME", "PARTNER", "COLLEAGUE"], label_size=28, label_color=CREAM)
t0 = add("mc_patterns", 28.10, 29.05, kind="mc", hold=4, word="PATTERNS", width=0.82, y=960)
t0 = add("hl_quote", 36.45, 41.62, kind="quote", x=540, y=880, w=930, size=80, pad=60, pulses=[R(36.45, 38.86), R(36.45, 39.97)],
         lines=[[[R(36.45, 36.61), "the", 0], [R(36.45, 36.61), "only", 1, 0.30], [R(36.45, 36.97), "way", 1, 0.30]],
                [[R(36.45, 37.09), "to", 0], [R(36.45, 37.22), "change", 1, 0.25], [R(36.45, 37.44), "your", 0]],
                [[R(36.45, 37.61), "self-narrative", 1, 0.70]],
                [[R(36.45, 39.97), "is", 0], [R(36.45, 40.16), "through", 0]],
                [[R(36.45, 40.32), "self-conversation.", 1, 1.05]]])
t0 = add("mg_share", 45.45, 47.6, kind="typecard", bg=INK, fg=CREAM,
         heroes=[dict(text="SHARE", t=R(45.45, 45.53), width=0.60, y=1235, color=HALDI, dx=-60)],
         lines=[dict(text="it with someone", t=R(45.45, 45.72), pos="over-left", font="script", size=62),
                dict(text="who needs to hear this", t=R(45.45, 46.19), pos="under-right", font="script", size=58)],
         icons=[dict(kind="plane", t=R(45.45, 46.05), x=905, y=1215, size=118, color=CREAM)],
         window=dict(rect=CARD_RECT, radius=56, shrink=0.28, border=dict(width=0, color=HALDI)))
json.dump({"fps": 30, "fonts": {"bold": F + "/Poppins-ExtraBold.ttf", "sans": F + "/Poppins-SemiBold.ttf", "script": F + "/PlayfairDisplay-ExtraBoldItalic.ttf"},
           "moves": moves}, open(P + "/moves.json", "w"), indent=1)

# ---------------------------------------------------------------- captions (chest, P19 base): n = small lead-ins, k = hero keyword
def n(t, w): return [t, w, "n"]
def k(t, w, serif=False, c=None):
    o = {}
    if serif: o["font"] = "serif"
    if c: o["c"] = c
    return [t, w, "k", o] if o else [t, w, "k"]


caps = []
def grp(t0, t1, *words): caps.append({"t0": t0, "t1": t1, "words": list(words)})

grp(2.21, 3.12, k(2.21, "SELF-CREATING"))
grp(3.30, 4.28, n(3.30, "if"), n(3.30, "you"), n(3.54, "tell"), n(3.69, "yourself"), n(4.08, "that"), n(4.23, "you"))
grp(6.51, 8.05, n(6.51, "you"), n(6.51, "are"), n(6.70, "more"), n(6.89, "likely"), n(7.13, "to"), n(7.31, "see"), n(7.46, "the"), k(7.60, "WORLD"))
grp(9.48, 11.17, n(9.48, "and"), n(9.64, "what"), n(10.16, "if"), n(10.41, "really"), n(10.81, "have"), n(11.04, "been"))
grp(11.17, 11.42, k(11.17, "thinking", serif=True))
grp(11.42, 12.34, n(11.42, "about"), n(11.67, "a"), n(11.85, "lot"))
grp(12.38, 13.38, n(12.38, "and"), n(12.71, "there's"), n(12.99, "the"), k(13.05, "RESEARCH"))
grp(13.38, 14.22, n(13.38, "around"), n(13.76, "this"))
grp(14.36, 15.70, n(14.36, "whereas"), n(14.84, "this"), n(15.08, "is"), k(15.33, "NOT", c=KUMKUM))
grp(18.49, 19.78, n(18.49, "when"), n(18.49, "you"), n(18.70, "begin"), n(18.91, "to"), k(19.12, "think", serif=True))
grp(19.80, 20.55, k(19.80, "how am I?", serif=True))
grp(20.57, 21.10, n(20.57, "I'm"), k(20.76, "interpreting", serif=True))
grp(21.12, 22.62, n(21.12, "the"), n(21.43, "facts"), n(21.87, "of"), n(22.08, "my"), n(22.22, "life"))
grp(22.74, 23.60, n(22.74, "how"), n(22.74, "is"), n(22.96, "my"), k(23.10, "PARTNER"))
grp(23.62, 24.62, n(23.62, "how"), n(23.73, "is"), n(23.84, "my"), k(23.99, "COLLEAGUE"))
grp(24.66, 26.15, n(24.66, "you"), n(24.66, "begin"), n(24.94, "to"), n(25.08, "see"), k(25.26, "PATTERNS"))
grp(26.19, 27.25, n(26.19, "and"), n(26.56, "if"), n(26.81, "you"), n(26.89, "can"), n(27.05, "truly"))
grp(27.27, 28.08, n(27.27, "see"), n(27.53, "people"), n(27.79, "for"), n(27.97, "the"))
grp(29.03, 29.36, k(29.03, "REPEATING"))
grp(29.36, 30.65, n(29.34, "over"), n(29.79, "and"), n(29.95, "over"), n(30.18, "again"))
grp(31.02, 31.98, n(31.02, "we"), n(31.02, "are"), n(31.26, "truly"), k(31.53, "understanding", serif=True))
grp(32.00, 32.58, n(32.00, "them"))
grp(32.60, 33.50, n(32.60, "we"), n(32.60, "are"), n(32.78, "truly"), k(33.06, "SEEING"))
grp(33.52, 34.90, n(33.52, "them"), n(33.71, "for"), n(33.88, "who"), n(34.07, "they"), n(34.38, "are"))
grp(35.16, 36.08, n(35.16, "if"), n(35.29, "they"), n(35.47, "want"), n(35.67, "to"), k(35.87, "CHANGE"))
grp(36.09, 36.45, n(36.09, "it"))
grp(41.86, 42.75, n(41.86, "so"), n(41.86, "always"), n(42.38, "be"), k(42.57, "aware", serif=True))
grp(42.77, 44.22, n(42.77, "of"), n(43.17, "how"), n(43.67, "and"), n(43.96, "what"))
grp(44.22, 45.45, n(44.22, "you"), n(44.34, "are"), n(44.41, "talking"), n(44.56, "to"), k(44.71, "yourself", serif=True))

# ---------------------------------------------------------------- camera: hard jumps every 1-2.5 s (change >= 15 %), slow drift inside each shot
shots = [(0.00, 2.21, 1.14, 1.22), (2.21, 3.30, 1.42, 1.47), (3.30, 4.30, 1.14, 1.18), (4.30, 6.51, 1.30, 1.34), (6.51, 8.00, 1.16, 1.22),
         (8.00, 9.48, 1.40, 1.44), (9.48, 11.17, 1.14, 1.20), (11.17, 12.38, 1.42, 1.48), (12.38, 14.36, 1.20, 1.24), (14.36, 15.70, 1.40, 1.44),
         (15.70, 16.82, 1.30, 1.34), (16.82, 18.49, 1.16, 1.20), (18.49, 19.80, 1.40, 1.44), (19.80, 22.74, 1.16, 1.22), (22.74, 24.66, 1.40, 1.44),
         (24.66, 26.19, 1.14, 1.20), (26.19, 28.10, 1.42, 1.48), (28.10, 31.02, 1.20, 1.24), (31.02, 32.60, 1.16, 1.22), (32.60, 35.16, 1.40, 1.46),
         (35.16, 36.45, 1.14, 1.20), (36.45, 41.86, 1.30, 1.38), (41.86, 43.17, 1.18, 1.22), (43.17, 44.40, 1.40, 1.44), (44.40, 45.45, 1.46, 1.50), (45.45, OUT, 1.20, 1.14)]
camera = []
for a, b, s0, s1 in shots:
    camera += [[a, s0, "linear"], [b, s1, "linear"]]

# ---------------------------------------------------------------- B-roll (footage), literal per noun
def br(key, f, t0, t1, src, entry="whip", cx=0.5, z=(1.0, 1.07), **kw):
    d = dict(key=key, file=f"{B}/{f}", src=src, t0=t0, t1=t1, entry=entry, cx=cx, z=list(z)); d.update(kw); return d
broll = [br("sunset_good_things", "B1b_sunset_sun.mp4", 4.30, 6.25, 1.0, entry="blurzoom", shade=False, z=(1.30, 1.38), dy=560),
         br("book_research", "B3a_book_in_hands.mp4", 12.90, 14.22, 2.2),
         br("couple_partner", "B5f_couple_at_bar.mp4", 22.85, 23.65, 3.9, entry="whip"),
         br("coworkers_colleague", "B5a_coworkers_laughing.mp4", 23.65, 24.62, 3.0, entry="whipL", cx=0.25),
         br("dominoes_repeating", "B6a_dominoes_dark.mp4", 29.00, 30.55, 3.9, entry="whip", shade=False),
         br("eye_seeing", "B7a_eye_blinking.mp4", 32.95, 34.15, 1.6, entry="blurzoom", cx=0.5, shade=False)]

# ---------------------------------------------------------------- layers, dims (UI band + focus pulls), desat, mirror, ring, flashes
layers = [dict(key=k_, dir=f"{P}/assets/moves/{k_}", t0=a, t1=b, behind=False) for k_, (a, b) in L.items()]
def pull(t, w=0.30): return dict(t0=round(t - w, 2), t1=round(t + w, 2), amt=1.0, blur=16, fade=w)
dims = [dict(t0=36.45, t1=41.62, amt=0.40, blur=11, fade=0.25)] + [pull(t) for t in (2.30, 6.25, 9.45, 14.22, 18.45, 24.62, 30.55, 34.15, 41.65)]
desat = [dict(t0=15.70, t1=16.82, fade=0.12)]
mirror = [dict(t0=44.40, t1=45.45)]
brackets = [dict(t0=11.17, t1=12.30, w=520, h=640, dy=40, shape="ring")]
flashes = [dict(t=18.46, type="white"), dict(t=35.12, type="neg")]

# ---------------------------------------------------------------- sound (voice + effects only; no BGM)
sfx_rows = [
    (0.00, WOOSH_S, -14), (0.04, BOOM_S, -9), (0.35, TICK_H, -22), (1.19, TICK_H, -22),
    (2.00, WOOSH_M, -15), (2.21, IMPACT, -11), (2.55, SHIM, -19),
    (3.30, WOOSH_S, -20),
    (4.28, WOOSH_M, -14), (4.56, POP, -14), (5.82, SHIM, -16), (6.10, WOOSH_S, -17),
    (7.60, POP, -15),
    (8.10, WOOSH_S, -14), (8.50, SHUTTER, -12), (9.22, WOOSH_M, -15), (9.48, TICK_H, -21),
    (11.14, SHIM, -17), (11.17, POP, -15),
    (12.38, WOOSH_S, -17), (12.90, PAGE, -13), (13.05, POP, -16),
    (15.33, SCRATCH, -14), (15.70, IMPACT, -9), (15.72, WOOSH_S, -14), (16.36, SCRATCH, -15),
    (16.82, SHUTTER, -11), (16.84, WOOSH_M, -13), (17.35, POP, -15), (18.22, WOOSH_M, -16), (18.46, WBOOM, -10),
    (19.12, POP, -16), (19.80, POP, -14), (22.74, POP, -14), (22.85, WOOSH_A, -14), (23.62, POP, -14), (23.65, WOOSH_S, -14),
    (25.26, POP, -19),
    (28.10, RISER, -13, "peak"), (28.10, TICK_L, -17), (28.23, TICK_M, -17), (28.37, TICK_H, -17), (28.50, TICK_L, -17), (28.63, TICK_M, -17), (28.77, TICK_H, -17), (28.90, TICK_L, -17),
    (29.00, WOOSH_A, -14), (29.03, POP, -15), (30.50, WOOSH_S, -18),
    (31.53, POP, -16), (32.95, WOOSH_A, -14), (33.06, POP, -15), (34.15, WOOSH_S, -18),
    (35.12, WBOOM, -9), (34.80, RISER, -14, "peak"), (35.87, POP, -16),
    (36.45, SLIDE, -13), (36.61, PAPERS, -18), (37.61, PAPERS, -18), (38.86, PAPERS, -17), (40.32, PAPERS, -17), (41.55, WOOSH_M, -15),
    (42.57, POP, -16), (43.17, TICK_H, -19),
    (44.40, RISER, -15, "peak"), (44.40, BOOM_SOFT, -10), (44.71, SHIM, -17),
    (45.45, WOOSH_M, -14), (45.53, BOOM_SOFT, -10), (46.05, POP, -15), (47.15, IMPACT, -16),
]
sfx = []
for r in sfx_rows:
    d = {"t": r[0], "file": f"{SFXD}/{r[1]}", "db": r[2]}
    if len(r) > 3: d["align"] = r[3]
    sfx.append(d)

# ---------------------------------------------------------------- beats inside the layers (for the gate's event-gap / pause checks)
mg_events = [0.03, 0.35, 0.68, 1.19, 1.5, 1.88, 4.33, 4.56, 5.43, 5.82, 8.28, 8.5, 9.2, 15.76, 16.03, 16.36, 16.82, 17.35, 17.75,
             36.61, 36.97, 37.22, 37.61, 38.2, 38.86, 39.97, 40.32, 40.85, 41.3, 45.53, 45.72, 46.05, 46.19, 46.9]

# ---------------------------------------------------------------- face follow
ft = json.load(open(FACE_TRACK)); cx = np.array(ft["cx"], float)
sm = np.convolve(np.pad(cx, 30, mode="edge"), np.ones(61) / 61, mode="valid")
anchor_track = [[round(i / 30, 3), round(float(sm[i]), 1)] for i in range(0, len(sm), 6)]

edl = dict(name="story_you_tell_yourself", src=P + "/src30.mp4", fps=30, project=P, keeps=[[0.0, OUT]],
           anchor=[480, 715], eye_y=600, anchor_track=anchor_track, camera=camera,
           grade=dict(exp=0, contrast=1.0, pivot=0.45, sat=1.0, warm=0, teal=0, face=0, vignette=0, grain=0, black=0),
           broll=broll, flashes=flashes, captions=caps, desat=desat, layers=layers, dims=dims, mirror=mirror, brackets=brackets,
           style=dict(accent=HALDI, cap_font=F + "/Poppins-SemiBold.ttf", key_font=F + "/Poppins-ExtraBold.ttf", giant_font=F + "/Poppins-Black.ttf",
                      serif_font=F + "/PlayfairDisplay-ExtraBoldItalic.ttf", stack_font=F + "/Poppins-ExtraBold.ttf", stack_small_font=F + "/Poppins-SemiBold.ttf",
                      cap_color=CREAM, ghost=0.30, reveal="blur", stroke=4, cap_size=60, key_size=124, cap_y=1175, key_max_w=860),
           sfx=sfx, meta=dict(mg_events=mg_events))
json.dump(edl, open(P + "/edl.json", "w"), indent=1)

# facts.json: pauses from the audio (silences >= 0.45 s) for the gate
r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", P + "/src30.mp4", "-af", "silencedetect=noise=-30dB:d=0.45", "-f", "null", "-"], capture_output=True, text=True).stderr
st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]; en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
os.makedirs(P + "/analysis", exist_ok=True)
json.dump({"silences": [[a, b] for a, b in zip(st, en)], "duration": 47.624}, open(P + "/analysis/facts.json", "w"))
print("layers", len(layers), "captions", len(caps), "sfx", len(sfx), "silences", [(round(a, 2), round(b, 2)) for a, b in zip(st, en)])
