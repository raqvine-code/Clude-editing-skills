# r2 — Semmelweis faceless documentary short: frame-level notes

Source: `src/reel.mp4`, 40.87 s, 720x1280, 30 fps, 1226 frames. Frame numbers (fNNN) are 0-based source frames; at 30 fps, t = f/30.
Evidence: `d/*.jpg` (frame-numbered sheets), `sheets/overview_1fps.jpg`, `n_typography_crops.jpg`. Measurements: `data/camseg.txt` (camera per segment), `data/cam_hook.txt`, `data/cam_portal_out.txt`, `data/cam_1840s_in.txt`, `data/iris.txt`, `data/textmeasure.txt`, `data/palette.txt`, `data/hex.txt`, `data/halftone.txt`, `data/contrast.txt`, `data/gaps.txt`, `data/side_detail.txt`, `data/bed.txt`; scripts are in `data/scripts/` plus the earlier `cam.py`, `iris.py`, `textmeasure.py`, `gaps.py`, `side.py`.
Conventions: px values are at 720 px wide unless marked "@360". `≈` = estimated from sheets, not measured. Font names are visual guesses only.

---

## 0 Identity

A 41-second, faceless, 150-wpm narrated history short. Every shot is a generated still or short loop, built into a 2.5D "diorama" layer stack and shot with a virtual camera that never stops moving. There are 16 visual beats, roughly one per VO sentence or clause. There are only 2 true content hard cuts (32.5 s, 35.5 s). Every other change is a motivated spatial move: a zoom through a window, light/portal/object irises, blur-rotation bridges, a floor wipe, a vertical whip, or a microscope-eyepiece wipe. Text is never a caption. It is placed in the world as an object (3D letters in the sky, a torn-paper name strip, typewriter on slate, print on a clipboard, highlighter on a newspaper, serif words on graph paper) and is withheld in the hook. Colour follows meaning: red means death or danger, green means life or improvement, teal-grey means clinical, neutral paper means evidence or moral. A static 45° halftone screen over every frame turns the mixed AI imagery into one "printed" look. Sound is SFX-led rather than music-led. A wide-stereo whoosh plus sub boom marks every spatial transition, a high tick marks every small event, and there is no melodic bed. The last 5.4 s are an ad (earnedits.com) built in the same visual language.

---

## 1 Beat sheet

| # | t (s) | frames | VO line (Whisper) | Visual | On-screen text | Transition in | Audio event (side = SFX channel) |
|---|---|---|---|---|---|---|---|
| 1 | 0.00–1.63 | 0–49 | "Doctors were unknowingly killing" | Storm night, red-lit hospital. Opens on an ECU of the glowing red cross, tilted ≈28°, then rotates and pulls back 2.5x to a level frontal facade. Ambulance drives in bottom-left (f26) | none | cold open, VO on f0 | side boom 0.17 s; mono sub hit 0.14 s (−18 dBFS, 0.61 s) |
| 2 | 1.67–3.10 | 50–93 | "…killing their own patients" | Zoom-through into the centre window, which holds the OR plate. 8.5x in 44 f, radial blur f52–58, then a decaying push on the surgeon over bloody drapes | none | window zoom-through f50–72 | side boom 1.56 s (f47, peaks f50/56/60); sub 1.97 s (−16 dBFS, 1.21 s) |
| 3 | 3.13–7.37 | 94–221 | "until one man discovered a simple habit that could save lives." | Blue-sky disc grows out of the OR ceiling lamp with a white bloom; sky and grass field. Red portrait card of "one man" page-curls in (f109–122), light sweep (f123–135). Camera trucks right along a 3D word line (≈450 px/s) while pulling back −10.6 %/s | DISCOVERED (red) A SIMPLE HABIT THAT COULD SAVE LIVES (navy), 3D extruded heavy caps | light iris f94–106 (animated on twos) | whoosh→boom 3.25 s (+32 dB, 7262→945 Hz), peaks f105 as sky fills; sub 3.72 s; soft hit 5.67 s (≈ HABIT) |
| 4 | 7.40–9.97 | 222–299 | "His name was Igna(z) Semmelweis." | A dot in the sky becomes a portal circle (16 f) while the sky spins −25°. Semmelweis waves in a 19th-c study. Incoming tilt ≈27°→0 by f267, pull-back −20 %/s, deep background blur. Exit: defocus plus fast pull-out f294–299 | torn black paper strip, red condensed serif "Ignaz Semmelweis" (f254–299) | spin-portal | boom 7.37 s (5453→322 Hz), sub 7.49 s; exit boom 9.57 s + sub 9.79 s |
| 5 | 10.00–12.47 | 300–374 | "In the 1840s, he noticed women were dying" | Top-down grid paper with window-gobo light. "1840s" printed on it. Sepia photo of women drops in from top-left (f308–322), masking-tape strips pop on (f340–350), framed slate slides in from the right (f346–372). Pull-back 0.55x, rotation settles ≈−14°→0 by f348 | "1840s" bold italic serif | blur-rotation cut f294→306 (hard cut at f300) | thud 10.36 s; sub 10.65 s = photo lands (f320) |
| 6 | 12.50–15.40 | 375–462 | "from childbirth fever at alarming rates." | Close on the slate graph, "Women Deaths" vs "Years" 1846–1860. Red line draws on f384–456. Camera follows the pen head: 784 px right pan, rotation 0→−11° | diegetic axis labels | hard punch-in cut f375 (same layout, ≈2.5x) | tick 12.46 s (f374, 1 f before cut) |
| 7 | 15.43–20.47 | 463–614 | "He discovered that doctors were going from autopsies to patients without washing their hands." | Dark floor plane wipes over the frame and drops away to a corridor. A doctor walks in place at centre while the wall and doors truck past (≈35–42 % W/s). "Autopsy Room" door f486–534, "Patient Room" door f550–598; he turns and enters (f600, pose swap). Exit: pull-back −32 %/s, defocus, floor rises f600–614 | diegetic door plaques (sans, 4.3 % W) | floor/pedestal wipe f463–480 | boom 15.37 s (+29 dB), peaks over the black hold; sub 15.75 s; sub 19.99 s on the turn (f600) |
| 8 | 20.50–22.93 | 615–688 | "So he introduced hand disinfection." | Top-down sink, hands rubbing palm to palm, sanitiser bottles. Defocus→focus f615–630, pull-back −21 %/s | none | blur-match hard cut f615 | tick 20.50 s (exactly f615) |
| 9 | 22.97–25.00 | 689–750 | "The death rate dropped dramatically," | A black dot opens from the point between the palms (14 f) onto a dark slate with a stepped falling green line. Area fill floods in at f710. Top haze light, rotation −16° | THE DEATH RATE (grey-white) / DROPPED DRAMATICALY (green, typo), mono, typed, underline | object iris from hands | tick 23.09 s (dot start f693); mono sub drop 23.81 s (−15 dBFS, 1.02 s) on the fill |
| 10 | 25.03–27.03 | 751–811 | "but doctors rejected his idea." | A glowing pinpoint at the end of the green line blooms white and opens a wood-desk circle (15 f). Clipboard slides in rotated (f757–780), pull-back −19 %/s | DOCTORS / REJECTED (red) / HIS IDEA., heavy caps printed on paper | glow-pinpoint iris | tick 25.04 s (f751 pinpoint); boom 25.38 s; sub 25.85 s = clipboard lands |
| 11 | 27.07–30.80 | 812–924 | "Years later, germ theory proved why he was right." | Vertical whip over the desk edge, wood→red mat (≈1240 px/s, 15 f). Newspaper "The Daily Chronicle: Scientific evidence confirms microbes cause disease", with stethoscope and thermometer as edge props. Highlighter sweeps 3 lines f838–890 | diegetic headline + yellow highlight | vertical whip along stacked surfaces | sub 27.38 s (mid-whip, f821); no side boom |
| 12 | 30.83–32.47 | 925–974 | "He didn't know about bacteria," | Black microscope-eyepiece ring slides in from the right (21 f), centring on "bacteria" (31.34 s = f940). Red bacteria plate, round lens falloff | none | eyepiece object wipe | boom 30.54 s (+33 dB), sub 30.92 s; hit 32.10 s |
| 13 | 32.50–35.47 | 975–1064 | "but he discovered that clean hands could save lives." | Black→white hard cut. Graph paper, spotlight cone and window-pane gobo, one word at a time; a clean open hand rises into the light (f1017–1040). Pull-back −23 %/s, rotation −18°. "lives." defocuses f1059–1064 | he / discovered / that / clean / hands / could / save / lives., bold italic serif | contrast hard cut (luma 31→203) | high ticks before word swaps: 32.45, 33.12, 33.47, 33.70, 34.29, 34.91 s |
| 14 | 35.50–37.30 | 1065–1119 | "The editors making work like this" | Blank linen-paper wall, empty for 10 f, then 6 words fade and blur in at a 5.2 f stagger. Static (+1.7 %/s) | THE EDITORS (red) / MAKING WORK / LIKE THIS (grey), heavy caps | white-to-white hard cut (blurred "lives." → clean paper) | quietest moment of the reel at 35.6 s (−40 dB) |
| 15 | 37.33–39.00 | 1120–1170 | "started with a project file from" | Lines stack upward and the block flies off the top with blur. A laptop on a wood plinth rises from the bottom (≈538 px/s tilt). Site screen recording scrolls | screen UI | collapse + vertical whip | boom 37.44 s (+30 dB), sub 37.91 s = laptop lands (f1137) |
| 16 | 39.03–40.87 | 1171–1225 | "earnedits.com." | A cursor line above the laptop expands into a navy search pill (12 f) and the URL types in. Ends without a loop | EarnEdits.com (UI sans) | in-frame build | hit 40.20 s (URL "." typed, f1206) |

Rhythm: 16 beats, mean beat length 2.55 s (range 1.63–5.03 s). There are ≈80 discrete visual events (word reveals, prop drops, transitions), so one every ≈0.5 s on average. The longest stretches without a new element are 21.0–22.97 s (sink, 2.0 s; per-second diff_mean 3.37 at 22 s, the reel's second-lowest) and 29.1–30.8 s (newspaper hold).

---

## 2 Hook dissection (0–3.4 s)

| frames | t | VO | What happens | Measured |
|---|---|---|---|---|
| 0–8 | 0–0.27 | "Doctors" (0.00) | ECU of a glowing red cross disc (#E71930) in the bottom-left corner, storm clouds (#1C1D28), frame rotated ≈28°. Already moving: scale −0.1 %/f, rotation −0.1°/f | VO starts on f0, no lead-in silence. Side boom from 0.17 s (f5), sub hit 0.14 s at −18 dBFS |
| 8–24 | 0.27–0.8 | "were unknowingly" | Fast rotate-and-pull-back reveals a facade with blood-red windows (#CC3E4A). The "HOSPITAL" sign appears at f14–16 | Peak step at f12: scale 0.905/f (−9.5 %/f), rotation −2°/f. Cumulative by f24: 0.45x, −23° |
| 24–39 | 0.8–1.3 | "unknowingly" | Eases to a level, symmetrical frontal. Ambulance enters bottom-left at f26 (secondary motion, a story cue) | f0→f39 total: 0.398x (2.5x pull-back), −28.5° rotation, exponential ease-out |
| 39–50 | 1.3–1.67 | "killing" (1.42) | Slow push-in, ≈0.37 s "breath" | +5 %/s rising to +5.5 %/f by f51 |
| 50–60 | 1.67–2.0 | "killing their" | Zoom-through: the centre window (the OR plate, pre-composited) rushes at camera with radial/zoom blur on f52–58 | Peak +15.3 %/f at f54. Side whoosh/boom starts f47 (3 f before the move); mono sub 1.97 s, −16 dBFS, 1.21 s long, the biggest hook hit |
| 60–74 | 2.0–2.47 | "own" | The window frame passes the frame edges (frame-in-frame), red windows exit top and bottom | +8 %/f → +4 %/f |
| 74–94 | 2.47–3.13 | "patients" (2.48) | Inside the OR: surgeon over bloody drapes, teal (#334D5F). Decaying push | +3 %/f → +0.5 %/f. Total f50→f94 = 8.5x |
| 94–106 | 3.13–3.53 | "until" (3.04) | The ceiling lamp turns into a light iris: a sky-blue disc (#0B98F0) with a white bloom grows from top-centre and the surgeon washes to white | r @360: 13→28→45→78→125→168 px every 2 f (on twos, ≈×1.6 per step). Whoosh-down impact 3.25 s (+32 dB, centroid 7.3 kHz→945 Hz), peaking at f105 when the sky fills |

Why it works:
- Four "spaces" (night exterior → window → OR → sky) in 3.5 s with zero hard cuts. The eye is always following one continuous camera, so there is no cut that signals "you can leave now".
- The opening frame is pure graphic (red cross, tilt, darkness) and resolves into context within 0.8 s. The first 8 frames are an abstract shape, the reveal comes at f24.
- The zoom into the window lands on "killing" (1.42–1.86 s). The accusation word triggers the intrusion into the building.
- The light iris on "until" is the turn from problem to hope. Luma per second goes 49→62→62→134 and saturation 0.41→0.59. The hook's colour and luma flip is the story turn.
- Text is withheld for 4.5 s. Image plus voice carry the claim, and the first text (DISCOVERED, 4.53 s) arrives as the reward. (For sound-off viewers this is a cost; see section 10.)

---

## 3 Typography and on-screen text

### 3.1 Inventory (sizes from `data/textmeasure.txt`, at 720 px wide)

| Scene | Font (visual guess) | Colour | Size | Placement | Material logic |
|---|---|---|---|---|---|
| Sky ticker (4.5–7.8 s) | ultra-black rounded display caps (≈ Bowlby One / Rubik Black class), 3D extruded with a darker side face | keyword DISCOVERED #F61D27; rest navy #2A4254 | DISCOVERED cap height 56 px = 7.8 % W, word 527 px = 73 % W; later words shrink to ≈3.6 % W as the camera pulls back | centre ≈41–43 % H, one horizontal line in 3D space | Sky has no surface, so the letters must be objects. Out-of-focus words ahead and behind give depth of field |
| Name (8.5–10 s) | condensed transitional serif (≈ Times/Libre Caslon Condensed) | #AC1D20 on torn black paper #131B23 with white torn edges | text cap 32 px = 4.4 % W; strip 520 px = 72 % W × 140 px | 42 % H, laid across the coat | Period-correct serif for a 19th-c name; the torn-paper "label" is collage |
| "1840s" (10.0–10.7 s) | high-contrast bold italic serif (≈ Playfair Display Black Italic) | soft black ≈#4C494A | ≈ 30 % W wide, tilted with the paper | ≈28 % H | A date printed on the evidence board |
| Graph labels (12.5–15.4 s) | small serif (≈ Times) | white on slate #191D21 | ≈ 1.5 % W | axes | Diegetic chart |
| Door plaques (15.7–20.5 s) | bold sans (≈ Arial/Roboto Bold) | #24241F on white plaque | 214 px = 30 % W wide, cap 31 px = 4.3 % W | 16 % H | Real-world signage |
| Death rate (23.3–25.3 s) | monospace typewriter (≈ Courier Prime) | line 1 #C8C7C5, line 2 #3AB339, underline #E6E8E2 3 px | cap 30–32 px = 4.2–4.4 % W; lines 54 % / 74 % W; underline 75 % W | top 18–24 % H (the graph owns the lower 2/3) | Report/record typed on a slate |
| Clipboard (25.8–27.4 s) | same ultra-black display caps as the sky, with print-grain texture | dark grey ≈#3A3A3A, REJECTED #D2353A | block 380 px = 53 % W; REJECTED 296 px = 41 % W | 43 % H, rotates with the paper | Stamped/printed verdict on a document |
| Newspaper (27.5–30.8 s) | diegetic bold news serif (generated) + highlighter | highlight #EFC114 | headline block 428 px = 59 % W | 33–49 % H | Proof as a found artefact |
| Moral (32.5–35.4 s) | bold italic serif (≈ Playfair Display Bold Italic) | #161A1C on lit paper #DEE0E3 (13.2:1) | "discovered" 292 px = 41 % W; "lives." 104 px = 14 % W, x-height ≈5.6 % W | 34–39 % H, centred | Elegant editorial voice for the thesis |
| CTA (35.8–37.4 s) | same display caps, tight leading (lines overlap ≈10 %) | THE EDITORS #D3292D; lines 2–3 #524F50 | 535 px = 74 % W; cap 56 px = 7.8 % W; block 202 px = 15.8 % H | 41–46 % H | "Poster" voice, same as DISCOVERED and REJECTED |
| URL (39.6–40.9 s) | UI sans (≈ Inter/SF Pro) | #E5E5E5 on pill #28425B | pill 411 px = 57 % W × 102 px; text 260 px = 36 % W | 21 % H | A browser search box |

### 3.2 The rule behind the fonts

Only 3 voices plus diegetic text:
1. **Verdict voice**: ultra-black caps with one red word per block. Used for the three statements that carry judgement or change: DISCOVERED, REJECTED, THE EDITORS. The red word is always the verb or actor of the turn.
2. **Archive voice**: serif (name, 1840s, moral). Used where the line is about history or the lesson.
3. **Record voice**: typewriter on slate. Used for data ("the death rate dropped").
4. Signage, newspaper and graph labels are generated into the plate (diegetic) and never animated, except for the highlighter.

The surface decides how the text appears. Text on paper is printed and rotates with the paper (clipboard, 1840s, moral). Text on slate is typed. Text in air is 3D extruded. Text on a person is a torn label. No text ever floats as a flat caption over an image. This is the "material" rule the brief suspected. The clipboard is not marker but the same display face as the sky and CTA, which makes the verdict voice consistent across 4.5 s, 26 s and 36 s.

### 3.3 Where text is withheld

- 0–4.53 s (hook): no text at all.
- 20.5–23.3 s (sink): the action is the answer, so no label.
- 30.8–32.5 s (bacteria): image only.

Readable text is on screen for ≈70 % of the runtime, but non-diegetic overlay text only ≈37 % (≈15.3 s). The VO is never captioned except in the climax line (32.5–35.4 s), where every word appears. Full word-by-word captions are kept for the moral, which makes that line feel different and important.

### 3.4 Entrance styles (frame counts)

| Device | Entrance |
|---|---|
| 3D ticker | Each word fades in and racks from blur to sharp over ≈6–8 f in its slot on the line while the camera trucks. Stagger ≈6–8 f per word |
| Name strip | Slides in from the right ≈10 f (f254–264), text legible from f262 |
| Typewriter | ≈1 char/f for "THE DEATH RATE" (f699–711). "DROPPED" is 7 chars in 9 f (f713–721), "DRAMATICALY" 11 chars in 18 f (≈1.6 f/char). Blinking block cursor; underline draws with the green line |
| Clipboard words | Per word, fade + blur→sharp over ≈5–6 f (DOCTORS f774–779, REJECTED f782–786, HIS f788, IDEA. f793) |
| Moral words | Hard swap, one word replaces the previous one with no transition. The first two words ("he", "discovered") blur/scale in over ≈4 f. The last word blurs out over 6 f (f1059–1064) |
| CTA words | Fade + blur in ≈6 f each at a constant 5.2 f stagger (f1075, 1082, 1088, 1093, 1097, 1101) |
| URL | Pill grows from a cursor line (f1172–1184, 12 f); 13 chars in ≈22 f (≈1.7 f/char) |

### 3.5 Per-word sync vs Whisper (32 words; onset frame = round(t×30); first-visible frames from the 1–2 f sheets c3, d, e, h2, i, j, l2, m, m3)

| Word | Whisper t | Whisper f | First visible f | Δ frames |
|---|---|---|---|---|
| DISCOVERED (sky) | 4.18 | 125 | 136–138 | +12 |
| A | 4.58 | 137 | 159 | +22 |
| SIMPLE | 4.82 | 145 | 163 | +18 |
| HABIT | 5.14 | 154 | 169 | +15 |
| THAT | 5.58 | 167 | 176 | +9 |
| COULD | 5.84 | 175 | 184 | +9 |
| SAVE | 5.98 | 179 | 192 | +13 |
| LIVES | 6.38 | 191 | 197 | +6 |
| Semmelweis (strip) | 8.68 | 260 | 254 (strip) / 262 (text) | −6 / +2 |
| 1840s | 10.22 | 307 | 300 (sharp 306) | −7 / −1 |
| RATE ("R") | 23.34 | 700 | 708 | +8 |
| DROPPED | 23.56 | 707 | 713 | +6 |
| DRAMATICALY | 24.02 | 721 | 723 | +2 |
| DOCTORS (clipboard) | 25.32 | 760 | 774 | +14 (clipboard still entering) |
| REJECTED | 25.68 | 770 | 782 | +12 |
| HIS | 26.26 | 788 | 788 | 0 |
| IDEA. | 26.58 | 797 | 793 | −4 |
| he (moral) | 32.54 | 976 | 977 | +1 |
| discovered | 32.66 | 980 | 980 | 0 |
| that | 33.10 | 993 | 995 | +2 |
| clean | 33.38 | 1001 | 1005 | +4 |
| hands | 33.74 | 1012 | 1012 | 0 |
| could | 34.26 | 1028 | 1030 | +2 |
| save | 34.52 | 1036 | 1035 | −1 |
| lives. | 34.86 | 1046 | 1050 | +4 |
| THE (CTA) | 35.70 | 1071 | 1075 | +4 |
| EDITORS | 35.80 | 1074 | 1082 | +8 |
| MAKING | 36.14 | 1084 | 1088 | +4 |
| WORK | 36.48 | 1094 | 1093 | −1 |
| LIKE | 36.78 | 1103 | 1097 | −6 |
| THIS | 37.00 | 1110 | 1101 | −9 |
| EarnEdits (URL) | 39.14 | 1174 | 1190 | +16 |

Two sync regimes:
- **"The word is the shot"** (name, date, moral line): 0 to +4 f after the spoken onset (mean +1.5 f). Each of these swaps has a side-channel tick 1–2 f before it (section 8).
- **"Recap phrase"** (sky ticker, clipboard, CTA, URL): constant-rate stagger of 5–8 f/word, decoupled from VO. It trails speech by 6–22 f (ticker mean +13 f ≈ 0.43 s) or drifts −9…+8 f (CTA). This reads as an echo of the voice, not a caption.

---

## 4 Motion and camera

### 4.1 House move: "rotate + pull-back settle" (measured, `data/camseg.txt`)

Nearly every scene arrives zoomed in and tilted, then eases out (exponential ease-out) toward wider and level, or drifts through level.

| Scene | Frames | Scale change | Rate | Rotation | Translation |
|---|---|---|---|---|---|
| Hook exterior | 0–39 | 0.398x | −50.7 %/s (peak −9.5 %/f) | −28.5° to level | 387 px/s |
| Sky + card | 112–150 | 0.80x | −16 %/s | −2° | 161 px/s |
| Sky ticker | 150–220 | 0.77x | −10.6 %/s | −2° | 1055 px L→R truck = 452 px/s |
| Study | 240–294 | 0.67x | −20 %/s | ≈27°→0 (Hough), then ±4° | 115 px/s |
| 1840s board | 300–372 | 0.55x | −22 %/s | +26° total (≈−14° to level by f348) | 147 px/s |
| Graph | 375–460 | 1.02x | ≈0 | 0→−11° | follows pen, 291 px/s |
| Corridor exit | 600–614 | 0.83x | −32 %/s | 0 | pedestal down |
| Sink | 618–688 | 0.58x | −21 %/s | 0 | 150 px/s |
| Death-rate slate | 704–750 | 0.89x | −7 %/s | −16° | 36 px/s |
| Clipboard | 770–811 | 0.76x | −19 %/s | ≈22°→−11° (through level) | 132 px/s |
| Newspaper | 830–920 | 0.83x | −6 %/s | ≈12°→−10° (through level) | 45 px/s |
| Spotlight | 982–1060 | 0.51x | −23 %/s | −18° | 135 px/s |
| CTA text | 1075–1118 | 1.02x | +1.7 %/s | 0 | static (≈) |
| Laptop | 1140–1225 | 1.01x | ≈0 | 0 | 163 px/s (content scroll + pill) |

Rules extracted:
- Default scene move is a pull-back of −16 to −23 %/s with 10–26° of rotation over the scene, ease-out.
- Only two push-ins: the hook zoom-through, and none afterwards except tiny drifts. Pulling back every shot "reveals" more of the diorama, hides the low resolution of generated plates (you start tight, where the detail is), and gives a constant sense of opening up.
- Rotation is the signature. Scenes rotate toward level (hook, study, 1840s) or past level (clipboard, newspaper, graph). Rotation is what makes stills feel shot handheld or by crane, not slideshowed.
- The CTA is the only static section (diff_mean 1.57 at 36 s, the lowest in the reel). Motion drops out when the selling starts. This is a weakness (section 10).

### 4.2 2.5D build per scene (layers, parallax, depth of field)

| Scene | Layers (front→back) | Depth tricks |
|---|---|---|
| Hospital | ambulance (own move, L→R) / facade plate / storm sky (drifts) / OR plate composited into the centre window | edge lens blur (tilt-shift style) on facade corners; zoom-blur during the dive |
| Sky | portrait card (3D page-curl, specular sweep) / 3D extruded word line / grass plate / sky plate | words ahead and behind the focus plane are blurred, focus "racks" along the line as the camera trucks; grass motion-blurred |
| Study | name strip / Semmelweis cut-out (waving) / blurred desk foreground (bottom-left) / heavily blurred study background | shallow DoF on the background throughout; global defocus as the exit |
| Desk boards (1840s, graph, clipboard, newspaper) | props (photo, tape, slate, clipboard, newspaper, stethoscope, thermometer) / surface (grid paper, wood, red cutting mat) / window-gobo light layer | soft drop shadows under every prop (≈ offset down-right, large blur); diagonal window-light streaks from the upper left; edge props cropped by the frame imply a larger table |
| Corridor | dark floor foreground strip / walker (centred, walk-cycle loop) + floor shadow / doors (move with the wall) / wall gradient #CDD3D8→ floor #60717B | treadmill parallax: the walker stays at ≈45–50 % W while the wall trucks ≈35–42 % W/s; foreground floor darker and blurred |
| Sink | top-down plate with a short hands loop | defocus-in; background (bottles) sharp, so ≈ flat |
| Death rate | type layer / green area graph (glow) / slate texture / top haze-light beam | volumetric light from top-centre; graph edge glow |
| Microscope | black eyepiece ring / red bacteria plate (slow drift) | circular lens falloff at the ring edge |
| Spotlight | words / rising hand / graph paper / spotlight cone + window-pane gobo shadows | lit cone vs shadow #A0A9AF gives a stage; the hand enters from the bottom into the light |
| CTA | text block / linen paper wall; laptop on plinth / wall | text collapses into depth; laptop rises on its own layer |

### 4.3 Motion continuing across scene changes

Measured examples:
- **Sky → study.** The outgoing sky spins with ease-in: rotation steps −0.5, −1.1, −1.8, −2.9, −4.7, −8.0° per 2 frames (f224–233, animated on twos). The incoming study starts ≈27° tilted and unwinds to 0 by ≈f267, so the spin hands over.
- **Study → 1840s.** The outgoing pull-out runs at −4 %/f with +2.5°/f rotation. The incoming starts at +0.9°/f and −2.2 %/f and decays to +0.27°/f and −0.6 %/f by f330. Same direction of spin and the same pull-back on both sides of the f300 cut.
- **Corridor → sink.** The outgoing pulls back (−3.4 %/f) and pedestals down. The incoming continues pulling back (−21 %/s). Both sides are defocused.
- **Clipboard → newspaper.** A single vertical whip over a continuous "table" (wood slab edge, then red mat below) carries one camera move through two sets.
- **CTA text → laptop.** Text exits upward at the same moment the laptop rises from the bottom. One tilt-down reads as a continuous move.

---

## 5 Transitions catalogue

| # | f range | Len | Name | Recipe | Why used there |
|---|---|---|---|---|---|
| T1 | 50–72 (scale until 94) | 22 f (+22 settle) | Window zoom-through | Composite the next plate inside a window of the current plate. Scale 8.5x over 44 f, exponential decay from a +15.3 %/f peak (f54) to +0.5 %/f. Radial zoom blur on f52–58. Whoosh starts 3 f before, sub boom (1.2 s) underneath | "Doctors were… killing": going inside the building is the accusation. No cut means no exit point in the hook |
| T2 | 94–106 (+ white band to 114) | 12 f | Light iris (lamp→sky) | Disc of the next scene grows from an existing light source (OR ceiling lamp, top-centre) with a white bloom rim; radius ×≈1.6 per 2 f, animated on twos; the outgoing plate washes towards white (#EBECEF). Bottom white band sweeps down f104–114 to reveal the grass | Problem→hope turn on "until". Light literally breaks in |
| T3 | 223–239 (+ settle to ≈267) | 16 f | Spin-portal | A 1-px dark dot in empty sky grows exponentially to full frame (r @360 ≈ 52 px at f231, 133 px at f234, full at f235–237). The outgoing plate rotates −25° ease-in (on twos). The incoming plate starts ≈27° tilted and unwinds. The circle has a soft drop shadow, so it reads as a hole | "His name was…": a door into the man's world. Placed on the sentence onset (+6 f) |
| T4 | 294–306 (cut at 300) | 5 + 6 f | Blur-rotation cut | Out: defocus to full blur in 5 f + fast pull-out −4 %/f + rotation +2.5°/f. Hard cut. In: starts blurred, same rotation sign (+0.9°/f decaying), sharp by f306 | Era jump (person → 1840s evidence). The blur hides an otherwise jarring material change (oil-paint study → paper) |
| T5 | 375 | 0 f | Punch-in cut | Hard cut from the wide board (photo + slate) to ≈2.5x on the slate, same layout and rotation. Tick SFX 1 f before | Lands the graph for "childbirth fever at alarming rates". Same-space cut, so no reorientation cost |
| T6 | 463–480 | 17 f (4 in, 3 hold, 10 out) | Floor/pedestal wipe | Incoming dark floor plane rises from the bottom edge to full cover in 4 f (ease-in), holds black 3 f (f467–469), then drops away revealing the corridor in ≈11 f (camera craning up past the floor edge). Boom peaks during the hold | New location and new sentence ("He discovered…"). The black hold gives a micro-reset before the longest beat |
| T7 | 600–630 (cut at 615) | 15 + 15 f | Defocus match cut | Out: pull-back −3.4 %/f + defocus + dark floor rising. Hard cut on "So". In: defocus→focus over 15 f while pulling back. Tick exactly on f615 | Solution beat starts. The blur equalises a cool corridor and a warm sink |
| T8 | 689–703 | 14 f | Object iris (black dot) | A black dot is born at the meaningful point (between the praying/washing palms) and grows exponentially (r @360 51→69→93→127→183→211 on f696–701, ×≈1.35/f). Inside: the next scene. Tick at the dot birth | "The death rate dropped": the result comes out of the act. Cause→effect is shown as a spatial link |
| T9 | 751–766 | 15 f | Glow pinpoint iris | A white pinpoint appears at the end of the green line, blooms (white = 37 % of the frame at f757, #F9F9F9) and contains the wood scene, which keeps growing ease-out. Tick at the pinpoint (f751), boom at fill (25.38 s) | "but doctors rejected…": the end point of the good result becomes the door to the twist. Bloom = a flash of "but" |
| T10 | 812–827 | 15 f | Vertical whip on stacked surfaces | The camera tilts so content moves down ≈1240 px/s with vertical motion blur; the wood desk slab's edge passes and reveals a red mat below; the newspaper rotates in from the top-right. Sub at mid-whip | "Years later": time skip as a fast move across one continuous table |
| T11 | 925–946 | 21 f | Eyepiece object wipe | A black microscope-eyepiece ring (outer black annulus, inner red bacteria) slides in from the right edge and centres, reaching centre on the word "bacteria" (f940). Boom 30.54 s | Literal: "He didn't know about bacteria" seen through a microscope he never had |
| T12 | 975 | 0 f | Contrast hard cut | Black-red microscope (luma 31) → white paper (luma 203). Tick 1 f before | Tonal reset to frame the moral. The only hard content cut in the story |
| T13 | 1059–1065 | 6 + 10 f | Blur-out to blank | Last word defocuses 6 f, cut to empty paper, 10 f of nothing | Clean separation of story and ad. Uses the quietest audio moment (−40 dB at 35.6 s) |
| T14 | 1120–1140 | 20 f | Collapse + rise | Text lines stack upward into line 1 and fly off the top with blur while the laptop on a plinth rises from the bottom (≈538 px/s) | Hands from "like this" to the product. Boom + sub on the landing |
| T15 | 1172–1184 | 12 f | Cursor→pill build | A cursor line appears, expands horizontally into a pill, then types | Diegetic UI that reads as "search this" |

Placement rule (measured): 14 of 15 transitions start within −0.22 to +0.25 s of a VO sentence or clause onset (median ≈ +3 f). Examples: T2 3.13 s vs "until" 3.04; T3 7.43 vs "His" 7.24; T4 cut 10.00 vs "In" 9.82; T5 12.50 vs "from" 12.72; T6 15.43 vs "He" 15.40; T7 20.50 vs "So" 20.46; T8 22.97 vs "The" 22.96; T9 25.03 vs "but" 25.16; T10 27.07 vs "Years" 26.90; T11 30.83 vs "He" 30.58; T12 32.50 vs "but" 32.40; T13 35.50 vs "The" 35.70; T14 37.33 vs "started" 37.36. The new picture arrives with the new sentence, so the picture is the sentence. The exception is T1, which is locked to the keyword "killing" (1.42–1.86 s) rather than to a sentence onset. T11 starts on its sentence but completes on its keyword ("bacteria", f940).

Circle motif: the red cross disc (f0) → lamp iris → sky portal → black dot → glow pinpoint → microscope eyepiece → spotlight → search pill. Five of the 15 transitions are circles. The circle is the reel's transition shape.

---

## 6 Motion-graphic devices and metaphors

| Device | How it is built | Why it works |
|---|---|---|
| Rising red graph | Framed slate (#191D21) with diegetic axes "Women Deaths" 0–500 and "Years" 1846–1860. Red stroke (#9E0F0B, ≈4–5 px) is trim-path drawn over 72 f (f384–456, 12.8–15.2 s), exactly spanning "from childbirth fever at alarming rates". Convex exponential curve. The camera pans ≈290 px/s and rotates 0→−11° to keep the pen head near 45–60 % W | The viewer watches the line accelerate. The curve shape is the word "alarming". Following the head turns a chart into a chase |
| Falling green graph | Stepped "crash" line from upper-left to lower-right on dark slate (#302D2E). First a thin line only (inside the iris, f696–709), then at f710 the area under it floods green (#043A03→#0E5D0A, glow) in one frame, with a mono sub drop (23.81 s, 1.0 s, −15 dBFS). Typewriter text on top | Colour and direction are the exact inverse of the red graph (red up = bad, green down = good). The one-frame fill + bass drop makes "dropped" physical. It borrows stock-crash shape but recolours it as good news |
| Treadmill walk between labelled doors | Centred walker loop. Background with two plaques ("Autopsy Room" → "Patient Room") trucks past. Door timing matches the VO: Autopsy door in frame while "autopsies" is said (17.24 s = f517), Patient door enters on "patients" (18.18 s = f545 → f550). He turns and enters at f600 without passing a sink | Literal path diagram of the cause. The audience sees the contamination route, so the later sink reads as the fix |
| Hands → result iris | The death-rate scene opens from the exact point between the washing palms | Visual causality: washing produces the drop |
| Pinpoint at line end → twist | The new scene is born at the end of the good-news line | The good result is "cut off" by rejection. The flash of white = shock |
| Clipboard verdict | Paper on a clipboard on a warm wood desk (#934629), window-light streak. Words printed with ink grain, REJECTED in red. Clipboard enters rotated from the bottom-right ≈23 f, settles, keeps drifting through level | Institutional "document" = medical establishment. The red verb carries the conflict |
| Newspaper + highlighter | Generated broadsheet "The Daily Chronicle" on a red cutting mat (#591B1B) with stethoscope and thermometer cropped at the edges. Yellow #EFC114 highlight sweeps 1 line per ≈16 f (L1 f838–856, L2 f858–872, L3 f874–890) during "germ theory proved why he was right" | Found-evidence aesthetic. The highlighter is a reading guide that holds attention on a dense prop for 1.7 s |
| Microscope eyepiece | Black ring object with the bacteria plate inside, slid on as a wipe | "Didn't know about bacteria" is shown as the view he never had. The darkest, most saturated frame (luma 31, sat 0.67) before the white moral |
| Spotlight + rising hand | Graph paper, a top spotlight cone, window-pane gobo shadows. A bare open hand rises from the bottom into the light while the words "clean hands could save lives" appear | The clean hand is literally "in the light". Single-word pacing slows the viewer for the thesis |
| Portrait card | Red-backed portrait (#FB0D24) flips in with page curl (f109–122) and a specular sweep (f123–135) on "one man" (3.56–3.96 s) | Introduces the hero as a collectible "card". The gloss sweep draws the eye before the camera pans to DISCOVERED |
| Torn-paper name strip | Black torn paper with white fibre edges, red serif, slides in from the right over the coat | Documentary lower-third without a lower-third template; collage material matches the desk scenes |
| Typewriter | Mono font, ≈1 char/f setup then ≈1.6 f/char payoff, block cursor, underline growing under line 2 | "Record" voice; motion inside a nearly static frame (diff_mean 2.23 at 24 s) |
| Search pill | Cursor → pill → typed URL above the laptop | A familiar UI action = an instruction ("search this") without saying "link in bio" |

Literal-visualisation logic (VO → picture):

| VO | Picture | Mapping |
|---|---|---|
| "Doctors were unknowingly killing their own patients" | Red-lit hospital in a storm; dive into the window onto a surgeon | doctors = surgeon; killing = blood-red light, storm, bloody drapes; "unknowingly" = the routine calm of the OR |
| "until one man discovered a simple habit that could save lives" | Light breaks into blue sky/green field; one man's card; DISCOVERED… | until = light iris; one man = single portrait; life = green field |
| "His name was Ignaz Semmelweis" | Portal to the man in his study, name strip | name = label |
| "In the 1840s, he noticed women were dying" | "1840s" on paper; photo of women in period dress | date = stamp; women = the photo |
| "from childbirth fever at alarming rates" | Women Deaths graph rising | rates = graph |
| "doctors were going from autopsies to patients" | Walk from the Autopsy door to the Patient door | going from X to Y = literal walk |
| "without washing their hands" | He enters the patient room straight away (no sink) | absence shown by action |
| "So he introduced hand disinfection" | Hands washing at a sink | literal |
| "The death rate dropped dramatically" | Falling green chart + typed words | literal + colour flip |
| "but doctors rejected his idea" | Clipboard: DOCTORS REJECTED HIS IDEA | words-as-object |
| "Years later, germ theory proved why he was right" | Newspaper "Scientific evidence confirms microbes cause disease", highlighted | proof = press |
| "He didn't know about bacteria" | Microscope view of red bacteria | literal |
| "but he discovered that clean hands could save lives" | Words one by one, a clean hand rising into the light | thesis = isolated words + symbol |

The rule: one concrete noun or verb per sentence becomes the picture. Abstract words (unknowingly, alarming, rejected, proved) are carried by colour, direction and props.

---

## 7 Colour and finishing

### 7.1 Colour script (per-second luma/sat from `data/cuts.txt`; k-means from `data/palette.txt`)

| t | Scene | Mean luma | Sat | Key hexes | Meaning |
|---|---|---|---|---|---|
| 0–3 | Hospital/OR | 49–62 | 0.38–0.41 | storm #1C1D28, window red #CC3E4A, cross #E71930, OR teal #334D5F | danger, night |
| 3–7 | Sky | 129–168 | 0.43–0.75 | sky #0B98F0, grass #4C8B03, card red #FB0D24, white bloom #EBECEF | hope, life (sat peak 0.75 at 6 s) |
| 8–9 | Study | 40–44 | 0.39 | #1A181A, #513433, #9D675B | the man, warm/dark interior |
| 10–12 | 1840s board | 174–182 | 0.05–0.09 | grid paper #BCB8B6, sepia #333131/#D5CEC8 | archive, evidence (near-mono) |
| 13–15 | Graph | 79–137 | 0.15–0.23 | slate #191D21, red line #9E0F0B | data, danger |
| 15–20 | Corridor | 137–165 | 0.16–0.23 | wall #CDD3D8, floor #60717B, doors ≈#7A3020 | clinical cool |
| 20–22 | Sink | 165–190 | 0.14–0.16 | basin #E1DAD6, skin #C0947D | clean, bright |
| 23–24 | Death rate | 43–87 | 0.22–0.47 | slate #302D2E, green #043A03/#0E5D0A, type green #3AB339 | good result in the dark |
| 25–27 | Clipboard | 79–92 | 0.46–0.49 | wood #934629, paper #E2D9D3, red #D2353A | establishment, warm |
| 27–30 | Newspaper | 85–91 | 0.49–0.54 | red mat #591B1B, paper #E1D4C7, highlight #EFC114 | proof, urgency |
| 31 | Microscope | 31 | 0.67 | black #070001, bacteria #A4181A | the invisible enemy |
| 32–35 | Spotlight | 178–203 | 0.06–0.12 | paper #DEE0E3, shadow #A0A9AF, ink #161A1C | clarity, moral |
| 35–37 | CTA text | 188–214 | 0.02–0.08 | paper #C1BFC0, red #D3292D, grey #524F50 | neutral "poster" |
| 38–40 | Laptop | 77–107 | 0.20–0.27 | plinth #5A3D28, screen #0C0F0E, UI green #1DCB1E, pill #28425B | product |

Pattern:
- Luma flips by more than 80 levels at 3, 8, 10, 23 and 32 s, each at an act boundary (problem → hope → person → evidence → result → moral). The contrast change itself tells the viewer "new chapter".
- Saturation runs in waves: 0.41 → 0.75 → 0.39 → 0.05 → 0.47 → 0.67 → 0.02. Saturated "emotional" scenes alternate with desaturated "evidence" scenes.
- Red is reserved for death, danger and the turn word (cross, windows, graph line, REJECTED, bacteria, the "one man" card, DISCOVERED). Green is reserved for life and improvement (field, falling death rate). The CTA reuses red for "THE EDITORS" and green for the product UI, borrowing the story's good/bad coding.

### 7.2 Finishing

- **Global halftone screen** (`data/halftone.txt`): a 45° dot lattice with a 4.47 px period (at 720 px wide) is present on every tested scene: storm, sky, paper, slate, microscope, CTA. FFT peak/median 138–320. It is screen-locked (temporal diff on static paper 0.64 levels). Amplitude ≈ ±5–8 levels (≈2–3 %). This is the glue that makes mixed AI renders read as one printed piece. It is also visible on the type (`d/n_typography_crops.jpg`).
- **Black/white points per scene**: p1 luma 0–67, p99 luma 139–248. Each scene keeps its own range; there is no global crush. The desk/paper scenes lift blacks (p1 58–67): a matte paper look.
- **Vignette**: no global vignette (the all-frames mean corner/centre ratio is 0.94). Falloff is baked into each composition (spotlight cone, OR, microscope ring, window gobos).
- **Bloom/glow**: used only on transitions (lamp iris, pinpoint iris at 37 % of the frame white) and the graph glow. It is not a constant effect.
- **Depth-of-field blur**: used as a transition (T4, T7, T13) and as a 3D type cue (sky ticker).
- **Light**: all desk scenes share an ≈upper-left key with window-pane gobo shadows, so different sets feel like one room.

---

## 8 Sound

### 8.1 Mix and level (`data/loudness.txt`, `data/side_detail.txt`, `data/bed.txt`)

- Integrated −14.9 LUFS, LRA 4.2 LU, true peak +1.3 dBTP. Sample peaks hit 1.000 on both channels, so the file clips (see section 10).
- VO is dead centre. Side/mid is −15 to −27 dB whenever only VO plays. Side-channel RMS overall −20.2 dBFS vs mid −15.6 (side/mid 0.59) only because the SFX are very wide: in the seconds with booms (0, 1, 3, 7, 10, 15, 25, 30, 37) side ≈ mid (−0.6 to +0.5 dB).
- **No melodic music bed.** Sustained side-channel tonal content sits at ≈−70 dB. In VO gaps the spectral peaks are inconsistent from gap to gap (no drone pitch), and the tempo autocorrelation is weak (r ≤ 0.07).
- The bed is low-frequency ambience/rumble (storm in the hook) that thins out over the reel: mid 50 ms floor (p5) is −25.5 dBFS in 0–4 s, −30 in 12–16 s, −37.9 in 28–32 s.
- The reel gets quieter and more intimate towards the moral, and the CTA cut sits on the single quietest moment (35.6 s, below −40 dB, 0.13 s).
- VO median RMS −19.2 dB. 20 ms envelope p5/p50/p95 = −34.6 / −19.9 / −8.7 dB. VO starts at 0.00 s; the gaps between sentences are 0.18–0.56 s.

### 8.2 SFX classes (side_events.txt + mono sub-bass hits from gaps.txt)

| Class | Spec | Used on |
|---|---|---|
| Whoosh→boom | 0.46–0.77 s, +26–33 dB above the side floor, 73–95 % energy below 200 Hz, centroid sweeping downward (e.g. 7262→945 Hz, 5453→322 Hz), very wide stereo, multi-peak (3 peaks ≈0.15–0.25 s apart) | every spatial transition: T1 1.56 s, T2 3.25 s, T3 7.37 s, T4 9.57 s, T6 15.37 s, T9 25.38 s, T11 30.54 s, T14 37.44 s; plus hook open 0.17 s |
| Sub "landing" (mono) | 20–70 Hz peak −15 to −23 dBFS, −12 dB width ≈0.48 s (0.11–1.21 s) | object lands or settles: photo f320 (10.65 s), floor-wipe reveal (15.75), turn to door (19.99), green fill (23.81, 1.02 s), clipboard (25.85), mid-whip (27.38), eyepiece (30.92), laptop (37.91), window dive (1.97) |
| Tick/click | 30–130 ms, centroid 7–11 kHz, +8–14 dB | punch-in cut f374 (12.46), hard cut f615 (20.50 exact), iris births f693 (23.09) and f751 (25.04 exact), moral-word swaps (32.45, 33.12, 33.47, 33.70, 34.29, 34.91) |
| Soft hit | ≈0.1 s mid-band | 5.67 s (≈ HABIT in the ticker), 32.10 s (pre-cut), 40.20 s (URL "." typed) |

### 8.3 SFX-to-visual alignment (frame offsets)

| Visual event | Frame | SFX onset (frame) | Offset |
|---|---|---|---|
| Hook first frame | 0 | boom 0.17 s (f5), sub 0.14 s (f4) | +4…5 f |
| Window dive peak | 54 | whoosh f47 (peaks f50/56/60), sub f59 | lead 7 f, peaks straddle the move |
| Lamp iris fill | 104–105 | boom f97.5, peak f105.6 | peak on fill ±1 f |
| Portal | 223–239 | boom f221, peaks f228–235; sub f225 | −2 f start |
| Study blur-out | 294–299 | boom f287, peak f292; sub f294 | leads cut by 13 f; sub on blur start |
| Photo lands | ≈320 | thud f311, peaks f315–325; sub f320 | 0 f |
| Punch-in cut | 375 | tick f374 | −1 f |
| Floor wipe black hold | 467–469 | boom f461, peaks f468–477; sub f472 | peaks during hold |
| Doctor turns | 600 | sub f600 | 0 f |
| Cut to sink | 615 | tick f615 | 0 f |
| Black-dot iris birth | 689–693 | tick f693 | 0…+4 f |
| Green area fill | 710 | sub f714 (1.02 s) | +4 f |
| Pinpoint iris birth | 751 | tick f751 | 0 f |
| Clipboard settles | ≈775 | boom f761, peaks f768–778; sub f775 | 0 f |
| Whip midpoint | ≈820 | sub f821 | +1 f |
| Eyepiece centres | 940 | boom f916, peaks f923–933; sub f928 | boom leads by ≈10 f |
| Moral cut / words | 975, 995, 1005, 1012, 1030, 1050 | ticks f974, 994, 1004, 1011, 1029, 1047 | −1…−3 f (tick leads the word) |
| CTA collapse / laptop lands | 1120–1137 | boom f1123, peaks f1130–1140; sub f1137 | 0 f on landing |
| URL "." typed | 1206 | hit f1206 | 0 f |

Inferred design:
- Big wide whoosh-boom for a change of world.
- Mono sub for "weight" when something lands.
- Tiny tick for small events: cuts within a space, iris births, word swaps.
- The words in the 3D ticker, typewriter, clipboard and CTA have no ticks. Ticks are saved for the moral, where every word gets one, so that line sounds different.
- Scorecard: 85.7 % of hard cuts have SFX; counting seamless transitions, 15/15 have one.

---

## 9 Storytelling and retention devices

| t (s) | Device | Detail |
|---|---|---|
| 0.00 | Paradox cold open | "Doctors were unknowingly killing their own patients". The trusted figure is the villain. VO and boom on frame 0–5, no logo or title |
| 0–3.1 | Continuous-camera hook | 4 spaces, 0 cuts, 2.5x pull-back then 8.5x dive. The viewer is carried, not shown |
| 3.04 | Open loop #1 | "until one man discovered a simple habit". What habit? Reinforced on screen at 5.3–6 s ("A SIMPLE HABIT") and paid off at 20.5 s (sink): a 17.5 s loop, the main retention engine. The words "washing… hands" are withheld until 19.1–19.8 s |
| 4.5–7.4 | Keyword echo | DISCOVERED in red trails the voice by ≈0.4 s: a second hit of the same idea |
| 8.7 | Concreteness | Name strip. 10.0: date stamp. 10.3: photo of real-looking women. The credibility stack arrives within 2 s |
| 12.8–15.2 | Escalating stakes | Graph line accelerating on "alarming rates" |
| 15.4–20.5 | Mechanism before solution | Autopsy → patient walk shows the cause, so the viewer solves it a beat before the VO ("washing their hands" at 19.1 s; the sink at 20.5 s). The viewer feels smart |
| 20.5 | Payoff #1 | Hand washing |
| 23.0 | Reward | Green drop + bass drop |
| 25.2 | Twist / open loop #2 | "but doctors rejected his idea": injustice. Pinpoint flash on "but". Resolved at 27–30 s ("germ theory proved why he was right") |
| 30.6 | Set-up for the moral | "He didn't know about bacteria" |
| 32.5 | Pattern break | Darkest, most saturated frame → whitest frame. Hard cut, single words, ticks, a hand rising into a spotlight. Every device changes at once to say "this is the point" |
| 34.5–35.0 | Callback | "save lives" returns from 6 s, now as quiet serif instead of loud 3D caps. Bookends the story |
| 35.5 | Reframe CTA | "The editors making work like this…" turns the reel itself into the product demo. Same visual language, so the ad doesn't feel like a channel change |

Structure: problem (0–3) → hope (3–7) → person (7–10) → evidence (10–15) → cause (15–20) → fix (20–23) → result (23–25) → rejection (25–27) → vindication (27–31) → moral (32–35) → CTA (35.5–41). That is 10 story beats in 35.5 s, ≈3.5 s each.

---

## 10 Weaknesses and mistakes (to surpass)

1. **Typo on screen.** "DROPPED DRAMATICALY" (f720–765). It is the only text in the reel's single most important data beat. Anyone who notices loses trust in the "historical" content.
2. **Audio clips.** True peak +1.3 dBTP and sample peaks at 1.000. Booms will crunch after Instagram's AAC transcode. Target ≤ −1 dBTP.
3. **Sound-off viewers get nothing in the hook.** No text for 4.5 s and no captions for the VO outside 32.5–35.4 s. Only ≈37 % of runtime has overlay text, and the story-carrying lines (killing patients, autopsies → patients, years later) are never written.
4. **Ticker legibility.** The sky line is longer than the frame, so you never read it whole ("ISCOVERED A", "AT COULD SAVE LIVES"). Words trail the VO by up to 22 f. DISCOVERED red on sky is 1.3:1 luminance contrast (it works only through hue and extrusion); navy on blue is 3.4:1.
5. **Plate artefacts.** The sky/grass plate shows mirrored tiling (symmetrical chevron clouds and kaleidoscope grass, visible from ≈f165 to f235) because the truck runs past the plate edge with mirror edges on. Generated newspaper body text is gibberish. The name-strip text is 4.4 % W at 2.4:1 contrast for 1.5 s.
6. **Data inconsistency.** The red "Women Deaths" curve keeps rising through 1860, after the 1847 intervention the VO later celebrates. The green falling chart has no axes, years or numbers, so the "dramatic" drop is unquantified (the real figure is roughly 18 % → ≈1–2 %; a number would hit harder).
7. **Pacing sag.** The sink beat (20.5–23.0 s) has no new element for 2.0 s (diff_mean 3.37 at 22 s). The newspaper holds 1.7 s after the highlight finishes (29.1–30.8 s).
8. **CTA loses the house move.** CTA text is static (diff_mean 1.57 at 36 s, the reel minimum). The CTA is 5.4 s (13 % of runtime) with the URL typed 0.5 s after it is spoken. The reel ends on a laptop with no loop back to the hospital/red-cross opening, so a replay starts from a cold, unrelated frame.
9. **Ambiguous gestures.** The washing hands are held in a prayer pose (they read as praying). The raised hand in the moral reads as "stop/wave" as much as "clean".
10. **Mixed frame rates.** The first two transitions are animated on twos (15 fps) and the later irises on ones. This is barely noticeable but inconsistent.
11. **Pronunciation/ASR.** The VO says "Igna(z)" softly (Whisper hears "Igna"). The strip fixes it, but this shows that the on-screen name is doing repair work.

---

## 11 Steal list (recipes with numbers)

1. **Rotate-and-pull-back on every still.** Start each scene 1.3–2.5x in and tilted 15–30°. Ease out (exponential) to level over 1.3–2.5 s at −16 to −23 %/s scale (hook version: 2.5x and −28.5° in 39 f, peak −9.5 %/f at f12). Let some scenes drift through level by 10° instead of stopping. Stills never sit, and you start where the generated detail is best.
2. **Window zoom-through.** Composite the next shot inside a window or screen of the current plate. Scale 8.5x over 44 f with a peak of +15 %/f on frame 4 of the move, decaying to +0.5 %/f. Add radial blur for 6–8 f and a whoosh starting 3 f before plus a 1.2 s sub. Put it on the shock word.
3. **Light iris.** Grow the next scene as a disc out of an existing light source (a lamp) in the current plate. White bloom rim, radius ×1.6 per 2 f (exponential), 12 f total. Fade the outgoing plate to #EBECEF-ish white. Use it on the "until/but then" hope turn.
4. **Spin-portal.** A 1 px dot in empty space grows to full frame in 16 f. The outgoing plate spins −25° with ease-in (−0.5 → −8° per step). The incoming plate starts ≈27° tilted and unwinds in ≈25 f. Give the circle a soft drop shadow so it reads as a hole.
5. **Object iris from the meaningful point.** Birth the transition dot at the exact spot that causes the next idea (between washing palms → result chart; end of the good line → the twist). Use 14–15 f exponential growth (×1.35/f). Black dot for a dark incoming scene, glowing pinpoint + bloom (≈37 % of the frame white at peak) for a bright one. Put a 30–80 ms tick on the birth frame and a boom on the fill.
6. **Blur-rotation cut.** Out: 5 f to full defocus with −4 %/f pull-out and +2.5°/f spin. Hard cut. In: start blurred, continue the same spin direction at +0.9°/f decaying to 0.3°/f, sharp by 6 f. Use it for era or material jumps.
7. **Floor/pedestal wipe.** The incoming scene's dark foreground plane covers the frame from the bottom in 4 f, holds black 3 f, then drops away in ≈11 f. Peak the boom on the black hold.
8. **Vertical whip on stacked surfaces.** Build two tabletops on one tall canvas (wood slab over a red mat). Tilt 15 f at ≈1200 px/s with vertical motion blur, the next prop rotating in, and a mono sub at mid-whip. Use it for "years later".
9. **Graph that the camera chases.** Draw-on stroke timed to the exact clause (72 f for "from childbirth fever at alarming rates"). Pan ≈290 px/s and rotate ≈−11° to keep the pen head at 45–60 % W. Later, show the inverse: a green falling stepped line whose area fill floods in one frame on "dropped" with a 1 s mono sub drop at ≈−15 dBFS.
10. **Font-by-surface rule.** Three voices only. Verdict = ultra-black caps at 7.8 % W cap height, one red word (#D-range red) per block. Archive/moral = bold italic serif. Data = typewriter at ≈4.3 % W cap height, ≈1 char/f setup, ≈1.6 f/char payoff, with underline. Text must sit on, or be, a physical object; never a flat caption.
11. **Moral line in single words.** On the thesis sentence only, show one bold italic serif word at a time at 34–39 % H. Swap within 0–4 f after the word onset, with a 7–11 kHz tick 1–2 f before each swap. Add a spotlight cone, a −23 %/s pull-back, and 6 f of defocus on the last word before the cut. Precede it with a hard luma flip (≈31 → ≈203).
12. **One picture per sentence, landing with the sentence.** Start each transition within −0.2 to +0.25 s of the sentence onset (median +3 f). In the hook, lock the move to the shock keyword instead. If a transition must run long, let it complete on the keyword (eyepiece centres on "bacteria").
13. **SFX grammar.**
    - World change: wide whoosh-into-boom, 0.5–0.77 s, centroid sweeping ≈7 kHz→≈500 Hz, +26–33 dB over the side floor.
    - Object lands: mono 20–70 Hz sub at −15 to −18 dBFS, ≈0.5 s.
    - Small event: 30–130 ms tick at 7–11 kHz.
    - No melodic bed; let the ambience floor fall from ≈−25 to ≈−37 dBFS towards the moral, and put the CTA cut on the quietest moment.
14. **Halftone glue.** Overlay a static 45° dot screen at ≈4.5 px period (at 720 px wide), ≈2–3 % amplitude, on every shot. Mixed AI plates then read as one printed piece.
15. **Colour = meaning, luma = chapter.** Red only for danger and the turn word, green only for life and improvement. Flip mean luma by more than 80 levels at each act boundary (here at 3, 8, 10, 23 and 32 s), and alternate saturated emotional scenes (0.6–0.75) with near-mono evidence scenes (0.02–0.1).

Do better than r2 on these points: spell-check every overlay, keep true peak at ≤ −1 dBTP, caption or label the hook for sound-off viewers, keep the house move alive in the CTA, and loop the last frame back to the first (e.g. end on a red circle that matches the opening red cross).
