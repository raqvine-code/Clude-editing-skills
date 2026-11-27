#!/usr/bin/env python3
"""Review boards for the owner: 1 important footage frames, 2 design system, 3-4 storyboard (numbered components)."""
import os
from PIL import Image, ImageDraw, ImageFont
P = os.path.dirname(os.path.abspath(__file__)); S = P + "/prev4"; O = P + "/boards"; os.makedirs(O, exist_ok=True)
AR = P + "/hc/fonts/Arimo.ttf"; GV = P + "/hc/fonts/GreatVibes-Regular.ttf"
def f(size, bold=False):
    ft = ImageFont.truetype(AR, size)
    if bold:
        try: ft.set_variation_by_axes([700])
        except Exception: pass
    return ft
BG, INK, MUTE, AMB, CREAM, DEEP = (18, 27, 23), (243, 234, 219), (176, 184, 178), (233, 184, 111), (243, 234, 219), (30, 43, 38)
import glob as _g
_ST = {float(os.path.basename(x)[2:-4]): x for x in _g.glob(S + "/s_*.jpg")}
still = lambda t: Image.open(_ST[min(_ST, key=lambda k: abs(k - t))])

def wrap(d, text, font, w):
    out, line = [], ""
    for word in text.split():
        test = (line + " " + word).strip()
        if d.textlength(test, font=font) > w and line: out.append(line); line = word
        else: line = test
    if line: out.append(line)
    return out

# ---------------- board 1: important frames of the footage
src = P + "/hc/frames/main/%05d.jpg"
moments = [(0.3, "0.3 s", "opens with the right hand up: the hook word lands here"), (2.5, "2.5 s", "small smile on 'self-creating'"), (13.0, "13.0 s", "head tilt on 'research'"),
           (19.4, "19.4 s", "questioning look: 'how am I?'"), (29.5, "29.5 s", "both hands open: 'patterns repeating'"), (34.6, "34.6 s", "hand thrown forward: 'if they want to change it'"),
           (39.5, "39.5 s", "palms down on the desk: 'really the only way'"), (45.6, "45.6 s", "points at the viewer: 'share it'")]
W1, TW, TH = 1900, 450, 800
b1 = Image.new("RGB", (W1, 160 + 2 * (TH + 150)), BG); d = ImageDraw.Draw(b1)
d.text((50, 40), "1  The footage: moments the edit is built around", font=f(46, True), fill=INK)
d.text((50, 100), "One static medium shot, natural colour kept (no grade). Times are in the original 47.6 s recording.", font=f(28), fill=MUTE)
for k, (t, lab, note) in enumerate(moments):
    x, y = 30 + (k % 4) * (TW + 15), 160 + (k // 4) * (TH + 150)
    b1.paste(Image.open(src % (int(round(t * 30)) + 1)).resize((TW, TH)), (x, y))
    d.text((x, y + TH + 12), lab, font=f(30, True), fill=AMB)
    for j, ln in enumerate(wrap(d, note, f(26), TW)): d.text((x, y + TH + 52 + j * 32), ln, font=f(26), fill=INK)
b1.save(O + "/1_footage_moments.jpg", quality=88)

# ---------------- board 2: design system
b2 = Image.new("RGB", (1900, 1500), BG); d = ImageDraw.Draw(b2)
d.text((50, 40), "2  Design system (the 'house look' that stays the same all video)", font=f(46, True), fill=INK)
y = 130
d.text((50, y), "FONTS (from R8)", font=f(30, True), fill=AMB); y += 50
d.text((50, y), "Great Vibes", font=ImageFont.truetype(GV, 120), fill=CREAM); d.text((700, y + 40), "script: the one feeling word (yourself, thinking, frames, aware)", font=f(28), fill=MUTE); y += 160
d.text((50, y), "Arimo Bold", font=f(96, True), fill=CREAM); d.text((700, y + 30), "sans bold: keywords and statements (R7 / R6)", font=f(28), fill=MUTE); y += 120
d.text((50, y), "Arimo Regular", font=f(70), fill=CREAM); d.text((700, y + 20), "sans: the small linking words, 56 px, full strength", font=f(28), fill=MUTE); y += 120
d.text((50, y), "COLOURS (taken from his room)", font=f(30, True), fill=AMB); y += 50
sw = [((233, 184, 111), "#E9B86F", "amber: his lamp glow, lifted. Keywords, pills, highlights"), ((30, 43, 38), "#1E2B26", "deep green: his wall slats. Cards and boards"),
      ((243, 234, 219), "#F3EADB", "cream: the lit wall. Paper cards, light text"), ((255, 255, 255), "#FFFFFF", "white: captions on the footage, soft shadow")]
for k, (c, hx, txt) in enumerate(sw):
    x = 50 + k * 460; d.rounded_rectangle((x, y, x + 120, y + 120), 18, fill=c, outline=(90, 100, 95)); d.text((x + 140, y + 10), hx, font=f(30, True), fill=INK)
    for j, ln in enumerate(wrap(d, txt, f(24), 290)): d.text((x + 140, y + 52 + j * 28), ln, font=f(24), fill=MUTE)
y += 190
for ln in wrap(d, "PLACEMENT (R7 / R6): caption block centre = chin + 17 % of the height (60-65 % here), inside x 30-70 %; nothing above his head except the small bubble icon.", f(28), 1800): d.text((50, y), ln, font=f(28), fill=INK); y += 38
y += 10
d.text((50, y), "CAPTION TREATMENTS (rotate; never the same one twice in a row)", font=f(30, True), fill=AMB); y += 50
treat = [(0.90, "A  R7 keyword", "small words + ONE amber bold keyword, blur-in 4-5 frames"), (1.62, "B  R8 script + sans", "script word writes on left to right, small sans tucked in"),
         (4.10, "C  R7 white bold", "a white bold stress word between small lines"), (2.75, "D  R6 converge", "two halves slide in from the edges and meet"),
         (18.47, "E  R6 pill", "dark pill, amber glow, icon, wipes in on the words"), (42.47, "F  R8 bold line", "one bold line, words blur in one by one")]
for k, (t, name, txt) in enumerate(treat):
    x = 50 + k * 305; im = still(t).crop((60, 900, 1020, 1500)).resize((290, 181)); b2.paste(im, (x, y))
    d.text((x, y + 192), name, font=f(25, True), fill=AMB)
    for j, ln in enumerate(wrap(d, txt, f(22), 290)): d.text((x, y + 226 + j * 26), ln, font=f(22), fill=INK)
b2.save(O + "/2_design_system.jpg", quality=88)

# ---------------- boards 3 + 4: storyboard, one panel per component
SB = [
 ("1", 0.90, "0.0-1.8 s", "Hook (R7)", "Starts out of focus and sharpens; 'Story' in amber; a glass speech bubble (the inner voice) floats beside his head", "soft whoosh-in, glass tap on the bubble"),
 ("2", 2.75, "1.8-2.9 s", "Converge (R6)", "'SELF-' slides in from the left, 'CREATING' from the right, they meet on the word", "two whooshes panned L and R, soft impact on the meet"),
 ("3", 5.90, "4.4-6.0 s", "Camera card (R6) + B-roll", "the sunset B-roll whips in, then shrinks into a camera-app card; pill 'you are very lucky'", "whoosh, card slide, shutter click, soft pop on the pill"),
 ("4", 8.45, "7.7-8.6 s", "Middle-box frame (R7)", "on 'luck frame' the room tints and an amber frame snaps round him; script 'luck frame'", "shutter / frame snap, 1-frame flash with a tick"),
 ("5", 12.97, "8.6-13.2 s", "Device board (R7) + B-roll", "he shrinks into a card on cream paper; 'research' slides in the book B-roll card", "slide, paper, soft whoosh on the second card"),
 ("6", 14.97, "13.2-15.8 s", "Type card (R5)", "full deep-green card, 'FACTS' ghost-to-solid, tiny lines tucked in", "low thud on FACTS, soft paper"),
 ("7", 16.60, "15.8-16.8 s", "Colour inversion (R5)", "hard flip to cream on 'frames'; script writes on; his moments as film frames slide past", "paper flip on the inversion, film tick"),
 ("8", 21.97, "17.9-22.7 s", "Question pills (R6) + B-roll", "'HOW AM I?' pill on him, then partner and colleague B-roll stack the questions", "soft clicks per pill, whooshes into B-roll"),
 ("9", 27.10, "26.6-27.6 s", "Match cut 'PATTERNS'", "one pinned word while 7 real clips flash behind it every 4 frames", "riser into it, a tick on every flash"),
 ("10", 28.75, "27.6-29.0 s", "Dominoes + echo (R5)", "dominoes B-roll; 'repeating' in amber; each 'over' repeats below itself, fading, like a pattern", "domino clatter feel: wood knocks, whoosh"),
 ("11", 32.70, "31.5-33.1 s", "Eye B-roll + script (R8)", "the eye B-roll opens on 'seeing'; the word writes on in script", "blur-zoom whoosh, soft chime"),
 ("12", 34.47, "33.1-34.7 s", "Zoom-blur punch (R6)", "the camera punches in on his forward hand with 'change' in amber", "short hit + air flick"),
 ("13", 39.27, "38.1-39.4 s", "Dark card + HL (R6/R5)", "near-black card, amber glow, glass 'two voices' icon; the highlight wipes under 'self-conversation' as he says it", "riser, marker stroke on the highlight, low hit"),
 ("14", 41.50, "39.4-41.9 s", "Script line (R8)", "calm: 'aware' writes on, small words tucked; empty beats between lines", "quiet, a single soft tick"),
 ("15", 42.47, "41.9-42.6 s", "Bold line + callback", "'you are talking to yourself' word by word; the bubble from the hook returns", "glass tap (callback to the hook)"),
 ("16", 44.70, "42.6-45.0 s", "Phone share (R5)", "he shrinks into a phone, a share sheet slides up, two quiet boxed lines", "slide, UI pop on the sheet, soft chime on 'Send'"),
]
def board(items, name, title):
    TW, TH, cols = 430, 764, 4
    rows = (len(items) + cols - 1) // cols
    b = Image.new("RGB", (40 + cols * (TW + 30), 130 + rows * (TH + 260)), BG); d = ImageDraw.Draw(b)
    d.text((40, 40), title, font=f(44, True), fill=INK)
    for k, (num, t, span, nm, look, snd) in enumerate(items):
        x, y = 30 + (k % cols) * (TW + 30), 120 + (k // cols) * (TH + 260)
        b.paste(still(t).resize((TW, TH)), (x, y)); d.rounded_rectangle((x + 12, y + 12, x + 72, y + 62), 12, fill=AMB); d.text((x + 24 if len(num) > 1 else x + 32, y + 18), num, font=f(32, True), fill=DEEP)
        d.text((x, y + TH + 10), f"{span}  {nm}", font=f(25, True), fill=AMB)
        yy = y + TH + 46
        for ln in wrap(d, look, f(23), TW): d.text((x, yy), ln, font=f(23), fill=INK); yy += 27
        for ln in wrap(d, "Sound: " + snd, f(21), TW): d.text((x, yy + 4), ln, font=f(21), fill=MUTE); yy += 25
    b.save(O + "/" + name, quality=88)
board(SB[:8], "3_storyboard_1-8.jpg", "3  Storyboard 1-8 (each panel is a real render on his footage)")
board(SB[8:], "4_storyboard_9-16.jpg", "4  Storyboard 9-16")
print(sorted(os.listdir(O)))
