# r4 — "RAW vs EDITED" agency showcase (realtor / ChatGPT talking head)

35.6 s · 720x1280 · 30 fps · 1068 frames · VO 121 words = 204 wpm · −14.7 LUFS / +2.9 dBTP / LRA 3.9 LU.
Frame numbers = source frames (t = f/30). "ED" = EDITED panel crop 392x696 @ (285,291); scale factors are relative to the RAW framing.
Values marked ≈ are visual estimates; everything else was measured with cv2/numpy (scripts in `data/scripts/`, data in `data/`).
Font names are visual guesses only.

Evidence: `d/hook_f000-039_30fps.jpg`, `d/hook_f036-112_15fps.jpg`, `d/s2…s12_*.jpg`, `d/ed_3fps_a/b/c.jpg` (ED at 3 fps), `d/cap_f692-790_15fps.jpg`, `d/cap_f930-1066_10fps.jpg`, `d/caption_bboxes_15frames.jpg`, `d/raw_vs_edited_aligned_f660.jpg`, `st/geom.jpg`; `data/raw_to_ed.json` (per-2-frame RAW→ED similarity transform = the zoom curve), `data/panel_frames.json` (per-frame diff/luma for both panels).

---

## 0 Identity

A static before/after ad for an editing agency: a light-grey (#e6e6e6) card with a small "RAW" talking-head panel on the left, partly tucked behind a larger "EDITED" panel on the right, and a big black "DM FOR WORK" footer. Both panels play the same take, frame-locked. The edit is a "premium dark-orange motion-graphics talking head". It is a low-key warm A-roll (black shirt, brown slat wall) and every 1.5–2.5 s it switches between three modes: (A) speaker full-frame with a two-tier caption (small white line + big gold keyword); (B) speaker rotoscoped or scaled into a graphic world (neon frame, ChatGPT app UI, crowd + giant title behind her, 3D logo behind her head, chess overlay); (C) full-screen 3D/stock metaphors (brain in robot hands on red, glowing pedestals). Transitions are short flashes (5-frame invert or exposure strobes, light leaks) and zoom-throughs, and each one hides a jump cut in the A-roll. Almost every visual event has a sound. The palette is black/brown with gold-orange as the brand accent; red is kept for threat words.

---

## 1 Beat sheet

Modes: **A** = speaker full-frame (+captions/overlay) · **B** = speaker composited in or with graphics · **C** = full-screen graphic · **T** = flash transition.
Audio events come from `side_events.txt` (stereo side channel = SFX/music only).

| t (s) | frames | VO | mode / visual | caption (keyword in CAPS) | transition in | audio event |
|---|---|---|---|---|---|---|
| 0.00–1.20 | 0–36 | "Agents keep asking me" | A: punch 1.35x→1.0x; orange neon rounded frame flies in around her head (settled f14) | AGENTS (gold, 3D tilt) / keep asking me | cold open; invert strobe f2–6 | whoosh/air 0.02 (+19.7 dB, 0.44 s) |
| 1.20–3.53 | 36–106 | "how do I show up on chatGPT searches?" | B: whole plate shrinks to 0.35x into a dark glass ChatGPT app UI; chrome knot behind her card; query types in sync | typed query in UI bar (7 words) | 14-frame scale-down with bulge warp | booms 1.18, 1.41; sub riser 2.91→peak 3.41 |
| 3.53–3.73 | 106–112 | (pause 3.34–3.80) | T: light leak purple→peach | — | leak 6 f | hi hit 3.52 |
| 3.73–5.40 | 112–162 | "And honestly that's a question" | A | And / Honestly · That's a / QUEST?ON | hard cut under the leak (RAW jump cut f112) | boom 4.83 = QUESTION lands |
| 5.40–7.47 | 162–224 | "that every single realtor should be asking right now" | B: background replaced: stock crowd of suited agents slams in behind the rotoscoped speaker on orange; giant REALTOR title wipes in behind the crowd; push 1.0→1.26x f210–222 | REALTOR title, then should be / ASKING / right now | crowd f162–170, title f176–184 | booms 5.32–5.91 (4 peaks), 7.28–7.49 |
| 7.47–10.03 | 224–301 | "because AI isn't coming, it's already here" | C: teal brain, robot hands slide in diagonally, red grid disc; background grey→red | Because AI isn't coming / its already HERE (top of frame, red) | zoom-in cut | ticks 8.14 (AI box), 9.39 (HERE); boom 9.83–10.09 |
| 10.03–11.67 | 301–350 | "Consumers are literally asking chatGPT" | A: 1.34x→1.0x settle in 16 f | Consumers are literally / Asking CHATGPT (letter scramble + glint) | zoom-through (hides RAW cut f303) | tick 11.30, hi hit 11.71 = glint |
| 11.67–14.03 | 350–421 | "who are the best agents in their city" | B: 3D chrome ChatGPT knot rises behind her head; orange search bar types the query at chest height; slow push 1.0→1.19x | search-bar text (8 words) | knot rise ≈20 f; bar slides in f370 | — |
| 14.03–14.20 | 421–426 | "and" | T: invert strobe I-I-N-I-I | — | 5 f (hides RAW cut f426) | hits 14.05, 14.22 |
| 14.20–15.37 | 426–461 | "it's pulling results" | A, then B: orange-lit dome rises from her chest, a black portal opens and swallows the frame | and it's / PULLING RESULTS | — | booms 14.87–15.27, 15.45 |
| 15.37–21.07 | 461–632 | "based off of who's consistent, who's creating content and who's actually showing up online consistently" | C: 3D pedestal stage; 3 pedestals rise, icons drop (clock, play card, social card); camera dolly | text printed on the pedestals only | portal | 16.25/16.40 clock lands; 17.20/17.32 play lands; 18.16 card; 20.82 exit push |
| 21.07–23.07 | 632–692 | "If you are ignoring the shift as an agent" | A: 1.36x→1.0x settle | If you are ignoring this shift / AS AN AGENT | zoom-through (hides RAW cut f632) | boom 22.40 |
| 23.07–24.43 | 692–733 | "you're already falling behind" | A | you're already / FALLING / BEHIND | caption swap | tick 23.76 |
| 24.43–25.97 | 733–779 | "and it's only going to get worse." | A | and it's only going to get / WORSE (red, letters drop in) | caption swap | — |
| 25.70–26.00 | 771–780 | (pause 25.78–26.00) | T: warm leak ramp + 2 white frames | — | 10 f (hides RAW cut f779) | hit 26.00 |
| 26.00–26.73 | 780–802 | "But the crazy thing is" | A | But the / Crazy Thing / is (white + orange bar) | flash cut | — |
| 26.73–28.30 | 802–850 | "you still have the upper hand." | B: speaker dims to 46 % luma and defocuses; suited hand holding a glass "AI" pawn enters top-right | you still have the ("upper hand" is never written; the hand shows it) | dim 30 f, hand slide ≈16 f | boom 27.16–27.50 |
| 28.30–31.00 | 850–927 | "Most agents have no idea how to use AI yet." | B: chessboard with businessman-shaped pieces rises under the blurred speaker | MOST AGENTS (white + red) · Have no idea / How to use AI yet | board rises ≈8 f | boom 28.32–28.66 |
| 30.90–31.07 | 927–932 | — | T: exposure strobe B-B-N-B-B | — | 5 f (hides RAW cut f932) | hit 31.02 |
| 31.07–32.57 | 932–977 | "Which means if you learn it now" | A (static 1.0x) | which means / if you learn it now (orange bar) | strobe cut | — |
| 32.57–33.53 | 977–1006 | "you're positioning" | A | You're / POSITIONING | plain jump cut f977, covered only by the caption swap | boom 32.78 (+25 dB) = POSITIONING lands |
| 33.53–35.60 | 1006–1068 | "yourself miles ahead of everyone else." | A | Yourself / MILES AHEAD / of everyone else | caption swap | boom 33.93, hit 34.10, booms 35.18, 35.52 |

**Mode totals (frames, measured on the beat boundaries above):** A 445 f = 14.8 s (41.7 %) · B 349 f = 11.6 s (32.7 %) · C 248 f = 8.3 s (23.2 %) · T 26 f = 0.9 s (2.4 %). 14 A/B/C stretches, mean 2.5 s.
**Switching rhythm:** about 10 mode changes in the first 17.8 s (one every ≈1.8 s) but only about 4 in the second 17.8 s. From 31.07 s to the end (4.5 s) it stays in mode A with zero zoom.
Pattern: A → B → A → B → C → A → B → A → B → C → A → B → A. B or C never repeats back-to-back, and C (full graphic) appears only twice, both times on the explanatory lines (the "AI is here" claim and the 3-item list).

---

## 2 Hook dissection (0–3.73 s, f0–112)

| frame | what is on screen (ED panel) | ED mean luma | audio |
|---|---|---|---|
| f0–1 | speaker punched in about 1.35x with motion blur; "AGENTS" giant gold word tilted in 3D; orange neon frame visible as a perspective ellipse around the caption (≈ it swings in in 3D) | 72, 65 | VO "Agents" starts at 0.00 (no lead-in); whoosh 0.02 |
| f2–3 | full-frame **colour invert** (cyan face, white shirt, blue AGENTS) | 173, 171 | |
| f4 | normal, zoom 1.16x | 59 | |
| f5–6 | invert again | 169, 168 | |
| f7–14 | normal; neon frame shrinks from oversize to its final rect (top edge starts outside the panel at f7–9 and has settled by f14); zoom 1.10→1.03x | 56→52 | |
| f14–34 | settled shot: neon frame (#d55e21 core, #e07634 bright, outer glow) around head and shoulders; AGENTS (cap 43 px = 11 % of panel width, 65 % wide) + "keep asking me" (white); zoom tail 1.03→1.00 by f30 | ≈52 | "keep asking me" 0.62–1.20 |
| f34–48 | entire plate (footage + frame + caption) scales 1.0→0.35x, ease-in-out (1.29, 1.23, 1.12, 0.98, 0.84, 0.68, 0.54, 0.456/1.302 in 2-frame steps); card edges bulge or pinch (≈ lens warp) as a dark app UI with orange rim light appears around it | — | booms 1.18, 1.41 |
| f44–94 | the query "how do i show up on chatgpt searches" types into the top bar, 36 chars in ≈50 f = ≈22 chars/s, tracking the VO 1.40–3.34 s; chrome ChatGPT knot builds behind the speaker card (f54–64); sparkle glints; the camera pulls back on the UI (z-dolly) f48–70 | 39 | "how do I show up on chatGPT searches?" |
| f95–105 | hold with the query complete; speaker card at 0.35x, offset +125/+227 px | 39 | sub boom 2.91, peaks 3.41 (+24 dB) |
| f105–111 | light leak: orange bloom (f106) → magenta/purple #b665c7 (f107–108) → peach #efaca2/#f6ddb0 full frame (f109–110) → residue (f111) | 53, 68, 64, 153, 199, 203, 128 | hi hit 3.52 |
| f112 | speaker full-frame at 1.0x, "And / Honestly" | 50 | "And" 3.80 |

Why it works: (1) Frame 0 already has the face, the motion and the audience call-out word, so there is no dead frame. (2) Three luminance inversions in 0.2 s are a pattern interrupt against the calm grey wrapper, and the eye goes to the EDITED panel rather than the RAW. (3) The spoken question is shown literally as a ChatGPT search being typed. The viewer reads along, the open question is made visible and the topic is clear in 2 s without a title card. (4) Four distinct visual states in 3.7 s (strobe/punch → neon frame → app UI → leak) before the first plain shot.

---

## 3 Typography and captions

**System: a two-tier "small line + keyword" card.** Each card has exactly one big keyword, with 1–2 small white lines as lead-in or tail.

| element | font (visual guess) | measured size in ED panel (392 px wide) | colour |
|---|---|---|---|
| small line | neo-grotesque medium, Inter or SF Pro style, mixed case | line box 13–16 px (cap ≈ 11 px ≈ **2.8 % of panel width**) | #ffffff core (p95), no stroke; soft shadow ≈ |
| keyword | geometric extra-bold caps, Montserrat ExtraBold or Poppins Bold style | cap 20–28 px = **5–7 % of panel width** (1.7–2.0x the small line), 34–68 % of panel width | gold #e8a64e core, highlights to #f4c976 (metallic sheen, no strong vertical gradient) |
| hook keyword AGENTS | same, heavier orange | 43 px = 11 % of width, 65 % wide | #ed882f, highlight #f8cd67 |
| emphasis keyword (ASKING, WORSE, Crazy Thing) | same | 39–40 px = 10 % of width | ASKING gold; WORSE red #da1e34 (highlight #eb475e); Crazy Thing white |
| pivot lines (Crazy Thing; if you learn it now) | bold mixed-case white | 26–39 px | white #fffaf3 with an orange bar #e6823f/#e88640, 15 px tall, through the x-height |
| graphic-scene captions | brain: "AI" in a red box + HERE red, Montserrat Black style; chess: MOST white / AGENTS red | AI/HERE rows 82–148 (top 12–21 %); AGENTS cap 51 px = 13 % | #d50009 / #e5001a |
| set titles | REALTOR: condensed extra-bold gold, bleeds off both edges | cap ≈ 70–76 px = 19 % of width, 98 % wide | #ec8e31 → #edbb61 on #642104 |

**Position:** keyword centre y = 441/696 = **63 % from top** (±2.5 % across 13 measured cards); small line about 59 %. That is chest level, below the chin. Exceptions: the brain scene puts captions at the top (12–21 %) because the graphic fills the centre; MOST AGENTS sits at 70–75 % on the chessboard.
**Layout:** a staggered "ladder". Line 1 is left-shifted, the keyword is indented, and an optional line 3 is right-aligned under the keyword's end (should be / ASKING / right now; you're already / FALLING / BEHIND; But the / Crazy Thing / is; Yourself / MILES AHEAD / of everyone else).
**Colour logic:** gold = the topic or the viewer's opportunity (AGENTS, Honestly, QUESTION, ASKING, CHATGPT, PULLING RESULTS, AGENT, FALLING, BEHIND, POSITIONING, MILES AHEAD). Red = threat or the out-group (AI in the "already here" scene, HERE, WORSE, AGENTS in "most agents", the AI dot in "how to use AI yet"). White + orange bar = the two argument pivots ("But the crazy thing is", "which means if you learn it now"). Glyph trick: QUEST?ON (the "I" replaced by "?").
**Words per card:** 19 text cards carry 96 of the 121 words, mean 5.1, median 5, range 2–8. Words never captioned are replaced by visuals: "every single realtor" (crowd + REALTOR title), the consistency/content/online list (pedestal labels), "upper hand" (a literal hand). Card hold is 0.7–2.5 s, mean ≈1.4 s.

**In-animations (frame counts from the 15–30 fps sheets):**
- Small line typewriter: letter by letter at ≈1 char/frame (30 chars "If you are ignoring this shift" in f632–660 = 28 f; "which means" in 9 f).
- Keyword tracking-in: letters start spaced ≈+100 % and dim, then condense to normal spacing in **6–8 f** (QUEST?ON f142–146, ASKING f202–204, PULLING RESULTS f433–438, AGENT f654–666, FALLING f698–704, BEHIND f702–708, POSITIONING f981–987).
- Letter scramble: CHATGPT letters appear in random order over f326–336 (10 f), then a yellow glint sweeps across at f346–352 (hi hit at 11.71).
- Per-letter drop and bounce: WORSE f736–760, one letter every ≈5 f, staggered heights settling onto the baseline.
- 3D swing: AGENTS f0–10.
- Bar wipe: orange bar wipes left to right through "Crazy Thing" f789–800 (strike-through look) and "if you learn it now" f942–948, with the words rising in from below f945–954.
- Out: a hard 1-frame cut-off in about 12 of 14 speaker cards, usually on a pause or caption swap; 3–5 blank frames before the next card types in (f134–138, f1002–1008). Exceptions: AGENTS rides the plate shrink; WORSE washes out in the leak.

**Sync vs Whisper (Δ = caption first visible − word onset, frames; + = late):**

| word | onset f | Δ first visible / settled |
|---|---|---|
| Agents | 0 | 0 |
| And | 114 | −4 |
| That's | 130 | **+8** |
| question | 145 | −3 / +1 |
| should | 190 | 0 |
| be | 196 | −1 |
| asking | 200 | +2 / +4 |
| now | 218 | −10 |
| Because | 223 | +5 |
| AI | 233 | **+10** |
| coming | 257 | −2 |
| here | 289 | −7 |
| Consumers | 305 | −1 |
| literally | 323 | −7 |
| ChatGPT | 346 | −18 / −10 |
| who (search bar) | 370 | 0 |
| pulling | 437 | −4 / +1 |
| If | 634 | −2 |
| agent | 683 | −29 / −17 |
| falling | 710 | −12 / −6 |
| worse | 765 | −29 / −7 |
| But | 780 | 0 |
| which | 935 | −2 |
| positioning | 987 | −6 / 0 |
| yourself | 1004 | +4 |
| miles | 1017 | 0 |
| everyone else | 1042 | −13 |

Small or connector words: median Δ ≈ −1 f, 67 % within ±5 f; the worst are "That's" +8 and "AI" +10 (late). Keywords start animating a median ≈8 f (0.27 s) **before** they are spoken and settle about on the word. The reveal anticipates the stress, so the word is readable when it lands.

---

## 4 Motion and camera

All speaker motion is **centre-anchored scale**. The RAW→ED transform gives rotation 0.0° and steady offsets of exactly (−7, −5) px, so the edit adds **no shake, drift or rotation**. Base ED framing = RAW framing (ED shows 97 % of the RAW height; no reframe).

| event | frames | scale (rel. to RAW framing) | curve |
|---|---|---|---|
| hook settle | f0–30 | ≈1.35 → 1.16 (f4) → 1.065 (f10) → 1.012 (f20) → 1.00 | expo ease-out, long tail |
| plate shrink into UI | f34–48 | 1.0 → 0.35 | ease-in-out, centre moves +125/+227 px |
| hold in UI | f48–108 | 0.35 static (UI camera pulls back ≈ f48–70) | — |
| push into brain | f210–222 | 1.00 → 1.26 | ease-in (accelerating), motion blur on f220–223 |
| settle out of brain | f302–318 | 1.337 → 1.00 | expo-out: excess falls about 36 % every 2 f (0.44, 0.28, 0.18, 0.12, 0.07, 0.04, 0.02) |
| slow push under the knot | f372–420 | 1.00 → 1.19 | ease-in-out over 48 f (1.6 s), ends in the invert strobe |
| push before the portal | f446–458 | 1.00 → 1.07 | then warp/portal |
| settle out of pedestals | f632–648 | 1.356 → 1.00 | same expo-out, 16 f |
| f650–1068 | — | 1.00 constant | no zoom in the last 13.9 s |

Inside graphics: the UI does a z-dolly; the brain plate does a 4-frame push-in (f297–300) before the cut; the pedestal scene has a slow 3D camera dolly plus a rotation (≈), then an accelerating push f620–631; robot hands, the chess hand and the search bar slide in with motion blur (≈12–16 f each). Bulge or pinch distortion is used twice as an "entering another world" cue (UI f40–56, portal f455–460).

---

## 5 Transitions catalogue

| # | at | frames | recipe | luma trace (ED mean) | why there |
|---|---|---|---|---|---|
| T1 invert strobe | f0–7 | 7 (N N I I N I I N) | full-frame RGB invert on 2 frames, 1 normal, 2 inverted, then normal; over a punch-in with motion blur | 72, 65, 173, 171, 59, 169, 168, 56 | Pattern interrupt on frame 0; makes the EDITED panel the brightest, most-moving thing on screen. |
| T2 plate shrink | f34–48 | 14 | scale 1.0→0.35 ease-in-out, edge bulge, UI fades or builds around the card | — | Moves from "person talking" to "the thing she's talking about" (ChatGPT) without a cut; RAW has no cut here. |
| T3 light-leak flash | f105–112 | 6–7 | orange bloom → purple #b665c7 → peach #efaca2 full frame (2 f at luma ≈200) → hard cut | 53, 68, 64, 153, 199, 203, 128, 50 | Leaves a complex UI and covers RAW jump cut f112 inside a 0.46 s VO pause. |
| T4 zoom-in cut | f210–224 | 12 + cut | 1.0→1.26 accelerating, motion blur, cut to full-screen graphic | 55→62→115 | "because AI…": the push signals "look closer" and the cut lands on "because" (f223). |
| T5 zoom-through | f297–318 | 4 + 16 | graphic pushes in 4 f → cut → speaker starts at 1.34x and settles to 1.0x in 16 f, expo-out, motion blur on the first frame (f300) | 61→76→54 | Returns from the graphic with energy; hides RAW jump cut f303. |
| T6 invert strobe | f421–426 | 5 (I I N I I) + cut | inverted outgoing ×2, normal ×1, inverted incoming ×2 | 177, 177, 62, 202, 202, 47 | Ends the 1.6 s push; hides RAW cut f426; reuses the hook's grammar. |
| T7 dome portal | f440–461 | 21 | an orange-lit hemisphere rises from the bottom (f440–450); a black disc opens in it and grows to fill the frame (f452–461) with a lens warp; cut into the 3D scene | 53→63→24 | "pulling results": you are pulled into the results; the move into C mode is motivated, not a cut. |
| T8 push-out + settle | f620–648 | 12 + 16 | 3D camera accelerating push, cut, speaker at 1.356x settling to 1.0x | 37→48→56 | Same zoom-through grammar; hides RAW cut f632. |
| T9 leak + white flash | f771–781 | 7 + 2 + 1 | warm leak ramp (#a24539/#c9624e/#ec8468) over the outgoing shot, 2 pure #ffffff frames, 1 leak-residue frame on the incoming shot | 49, 59, 76, 91, 117, 151, 176, 195, 255, 255, 113, 53 | Chapter break, problem → solution ("…worse." / "But the crazy thing is"); hides RAW cut f779. |
| T10 dim + overlay build | f802–860 | 30 (dim) | speaker luma ramps to 0.46x of RAW and defocuses; hand slides in from top-right ≈16 f; board and pieces rise ≈8 f | ratio 1.00→0.80→0.52→0.46 | Moves into a metaphor without leaving the speaker, so she stays present while the graphic carries the line. |
| T11 exposure strobe | f927–932 | 5 (B B N B B) + cut | brightened, blurred glow version of the frame ×2, normal ×1, ×2, cut | 67, 126, 126, 67, 126, 127, 48 | Leaves chess; hides RAW cut f932. |
| T12 plain jump cut | f977 | 0 | cut only, caption cleared on the same frame | — | The only RAW cut left without a device; masked weakly by the caption change. |

Grammar: **5-frame strobe = 2 on / 1 off / 2 on**. Zoom-throughs are **12 f in / 16 f out**. Leaks run **6–10 f** with **2 frames at peak**.

---

## 6 Motion-graphic devices and metaphors

| device | VO at that moment | how it is built | enter / exit | why it works |
|---|---|---|---|---|
| Neon frame | "Agents keep asking me" | orange rounded rect (#d55e21, glow #e07634), radius ≈20 px, behind the caption; probably composited behind her hair (≈) | swings in in 3D during the strobe, settled by f14; leaves with the plate shrink | Frames the face as "the subject" and introduces the orange brand colour in the first second. |
| ChatGPT app UI | "how do I show up on ChatGPT searches?" | dark glassmorphic phone screen (#18130d / #3c240f) with orange rim light, top query bar, bottom input pill with orange send dot; chrome 3D knot behind the speaker card; speaker card with orange border; sparkle glints | plate shrink f34–48 + UI build; exits by leak | The question is acted out (typing synced to speech), so the viewer reads the hook twice. |
| Crowd + REALTOR title | "every single realtor should be asking" | rotoscoped speaker (front) / stock crowd of ≈20 suited people (middle) / REALTOR gold title (behind the crowd, letters cut by heads) / orange backdrop #642104 (back): a 4-layer depth sandwich | crowd slams in from the top in pieces f162–170 (multi-boom); title wipes in f176–184 on "realtor" (5.90 s = f177); exits by push into brain | Viewer identification ("that's me"); the title on the exact spoken word acts as a caption. |
| Brain in robot hands | "AI isn't coming, it's already here" | 3D teal brain (#546f71) in the centre; two white robot hands slide diagonally from top-left and bottom-right f228–240; dark red disc with grid behind it grows f240–252; background radial goes grey #9c9698 → red #b10006/#390002 over f243–285; caption at top with "AI" in a red box (black box placeholder first, ≈ f225–240) | zoom-in cut; zoom-through out | Abstract claim turned into an image ("AI has the brain in its hands"); the colour drifting to red during the sentence builds urgency without a cut. |
| 3D knot behind the speaker | "asking ChatGPT who are the best agents" | chrome OpenAI-style knot with orange rim light rising from behind her shoulders (rotoscoped speaker in front), f350–370 | rise ≈20 f, then the search bar slides in at f370 | Puts the brand being discussed physically behind her head, like a halo; the roto depth feels expensive. |
| Search bar | "who are the best agents in their city" | orange gradient pill #c35814 with "+" and "↑" icons, full panel width at the caption band (60–67 % of height); text types in sync and the bar scrolls left as text overflows | slides in from the left f370; exits by invert strobe | The consumer behaviour is shown as UI; the bar doubles as the caption. |
| Dome portal | "pulling results" | orange-lit hemisphere + growing black disc + barrel warp | f440–461 | Literal "pull" into the next world. |
| Pedestal stage | "consistent / creating content / showing up online" | 3D dark matte pedestals (#3d3834 / #1c1714) on glossy black floor, black lattice beams with orange rim (#a86535); labels printed on the pedestals: "01 Consistency SHOWUP REPEAT IMPROVE", "02 Creating Content TURN IDEAS INTO VISUALS", "03 showing up online BE SEEN BUILD TRUST GROW"; icons: clock with orange arrow, video play card, social post card | pedestals rise from below (f472–484, f496–512, f532–548); icons drop on the keyword ("consistent" 16.28 s = f488 → clock f492; "creating content" f517–527 → play f520–524; card ≈f552); 5.7 s; accelerating push out | Rule of three made physical; each drop is a micro-reward with its own boom + hit; a trophy/podium metaphor = ranking in ChatGPT. |
| Hand with AI pawn | "you still have the upper hand" | speaker dimmed to 46 % and defocused; 3D suited arm (black sleeve, white cuff) holding a glass and gold "AI" pawn from top-right | slide ≈f808–824, held to f931 | A visual pun; the words "upper hand" are never typed, so the image is the caption. |
| Chessboard of agents | "Most agents have no idea how to use AI yet" | b/w checkerboard, chess pieces shaped like businessmen rising from the bottom; MOST (white) AGENTS (red) cap 51 px | rise f852–860; exit exposure strobe | "Most agents" = pawns; AI = the piece in the expert's hand. Status contrast. |
| Highlight bar | the two pivots | orange bar wipes left to right through the white text | 6–11 f | Marks the logical turns of the script (problem → twist → payoff). |

---

## 7 Colour and finishing (hex)

- **Wrapper:** background #e6e6e6 with fine noise (σ 2.3), fully static all 35.6 s; labels and footer #000000.
- **A-roll (unchanged by the edit):** wall slats #3e1e15, skin #5a3723, shirt #1b1a1f, plant #25200b; ED speaker luma median 39–50 / 255 (low-key, warm). The panels' rounded corners are ≈14 px (EDITED) and ≈10 px (RAW).
- **Accent system:** gold keyword #e8a64e (highlight #f4c976) · hook orange #ed882f · neon frame #d55e21 / #e07634 · search bar #c35814 · orange bar #e6823f · pedestal rim #a86535 · REALTOR #ec8e31 / #edbb61 on #642104.
- **Threat red:** #da1e34 (WORSE) · #e5001a (AGENTS on chess) · #d50009 (AI box, HERE) · brain stage #b10006 → #390002.
- **Graphic worlds:** UI #18130d / #3c240f / #6c4425 · brain grey stage #9c9698 / #cbc5c8 · pedestals #3d3834 / #1c1714 / #040202 · chess #e5ded6 / #1e140e.
- **Flashes:** leak 1 #b665c7 → #efaca2 / #f6ddb0; leak 2 #a24539 / #c9624e / #ec8468; white #ffffff (2 f); invert frames ≈ #e6edf0 / #a4c0d5; exposure strobe ≈ #d1a772 / #eee6ce.
- Everything orbits **black + brown + one orange/gold accent**, matching the warm A-roll wall, so graphics and footage read as one world. Red appears only where the script is negative, and the cool teal brain is the only cool element (= "machine").

---

## 8 Sound

- **VO:** 204 wpm; Whisper pauses ≤0.46 s (longest at 3.34–3.80, 20.74–21.14); quiet share 4.7 %.
- **Loudness:** −14.7 LUFS integrated, **+2.9 dBTP true peak** (overs), LRA 3.9 LU (heavily compressed); rms median −19.3 dB.
- **Music:** a low-level tonal bed, no beat. Side-channel mids sit at ≈−40 dB continuously (median side −38.5 dBFS vs mid −16.8); tonal peak ratio 0.45–0.6; chroma diffuse (F/F#/G/A ≈ dark cinematic pad); tempo autocorrelation r ≤ 0.21, so no usable pulse. Cuts follow the speech, not a beat. The bed's low end **drops out at 31–34.5 s** (sub band −57 → −87 dB at 33 s) under "if you learn it now… positioning yourself", then returns with the final booms at 35.18 / 35.52 (≈ breakdown before the payoff).
- **SFX:** 42 side-channel events = **11.8 per 10 s**. Classes: sub-heavy booms 0.3–0.7 s (transitions, objects landing), bright hits (flashes, glint), ticks (text pops: 8.14 "AI" box, 9.39 HERE, 11.30, 23.76).
- **SFX-to-visual alignment:** 11 of 12 transitions carry an event within ±0.1 s of the key frame (T1 0.02 · T2 1.18 / 1.41 · T3 riser 2.91 → 3.41 + hit 3.52 · T4 7.28 / 7.49 · T5 9.83–10.09 · T6 14.05 / 14.22 · T7 14.87–15.45 · T8 20.82 · T9 26.00 exactly on f780 · T10 27.16 · chess 28.32 · T11 31.02). The only miss is the plain jump cut f977. Object-landing booms: clock 16.25–16.40 (clock lands f492 = 16.40), play card 17.20–17.32 (f520), keyword landings QUESTION 4.83, POSITIONING 32.78 (+25 dB, the loudest side event), MILES AHEAD 33.93 / 34.10.
- The sub riser peaks 4–10 frames **before** the flash (3.41 vs f106 = 3.53), so the energy crests just as the picture whites out.

---

## 9 Storytelling and retention devices

- **0.00** Audience call-out as the first word and first caption ("AGENTS"), shown with a strobe; no intro.
- **0.0–3.3** Open question typed into ChatGPT = a visible curiosity gap.
- **3.8–4.8** Validation ("honestly that's a QUESTION"), with the ?-glyph gag.
- **5.4–7.4** Identification: a crowd of realtors behind her on "every single realtor".
- **7.5–10.0** Stakes: "AI is already here" as a full-screen red metaphor, colour escalating within the line.
- **10.0–14.0** Proof by demonstration: the consumer's search is typed on screen.
- **14.6–21.0** Mechanism as a 3-item list on pedestals; each item gets an icon and an SFX "reward".
- **21.1–25.8** Loss aversion: ignoring → FALLING BEHIND → WORSE (red, letters falling, i.e. kinetic type acts out the word).
- **25.97** White-flash chapter break = turn of the argument.
- **26.0–31.0** Reframe to opportunity: "upper hand" pun, most agents as pawns.
- **31.1–35.4** Payoff and positioning in gold ("MILES AHEAD"). No spoken CTA; the wrapper's "DM FOR WORK" is the CTA for the agency.
- Constant devices: a new visual idea every ≈1.8 s in the first half; one keyword per card; SFX on every event; the RAW panel always playing beside it as a live control sample.

---

## 10 Weaknesses and mistakes (so we can surpass it)

1. **Tiny panel → tiny text.** EDITED is 394 px of 720 (55 % width), so the small caption line is ≈11 px cap in a 1280-px canvas (0.9 % of screen height, ≈1.3 mm on a 6" phone) and keywords ≈24 px. Half the edit's typography is illegible in the feed.
2. **Photosensitivity:** the hook strobe has 4 full-frame luminance swings (≈60↔170) in 0.23 s, and T6/T11 repeat it. That exceeds the 3-flashes-per-second guideline and gives harsh first frames.
3. **First frame is motion-blurred** (f0–1); the reel cover/first impression is a smear.
4. **Back half loses pace:** about 10 mode switches in the first 17.8 s vs about 4 in the second; the last 4.5 s have no zoom, no graphic and no transition, right where the CTA should peak. The video ends 0.18 s after the last word with no end card and no designed loop.
5. **Caption sync is uneven:** keywords up to 17–29 f early (AGENT, WORSE start animating before the lead-in is spoken), some words late ("That's" +8 f, "AI" +10 f).
6. **Copy errors:** "its already HERE" (missing apostrophe); "this shift" on screen vs "the shift" spoken; inconsistent capitalisation ("Have no idea / How to use").
7. **Colour logic leaks:** FALLING BEHIND (negative) is gold while WORSE is red; AI is red in one scene and a gold pawn in another.
8. **One exposed jump cut** (f977) with no punch-in or SFX, after 10 others were carefully hidden.
9. **True peak +2.9 dBTP:** audio will clip or distort on platform transcode.
10. **The "RAW" is not raw:** it is the already-tightened, already-graded A-roll (same 11 jump cuts, identical colour), so the agency's cutting work (pause removal, take selection) is invisible, and 24 % of the RAW panel is hidden behind EDITED.
11. **No brand on the wrapper:** no agency name, handle, client name or result metric. "DM FOR WORK" is static and never animates or gets referenced.
12. **IP risk:** an OpenAI-logo-like knot and ChatGPT UI styling, plus obvious stock crowd and stock robot cutouts.

---

## 11 Steal list (recipes with numbers)

1. **5-frame strobe cut:** outgoing ×2 flash frames (invert, or +90 % exposure with bloom) → 1 normal → incoming ×2 flash → cut; bright "hit" SFX on the first flash frame. Use it to hide jump cuts. (Keep it to one burst per 3 s if photosensitivity matters.)
2. **Zoom-through:** outgoing push 1.0→1.26x over 12 f, ease-in with motion blur → cut → incoming starts at 1.35x and settles to 1.0x in 16 f, expo-out (remove ~36 % of the remaining excess every 2 f); a sub boom peaking on the cut.
3. **Two-tier caption card:** small white line at cap ≈3 % of frame width (typewriter, 1 char/frame) + one keyword at cap 5–7 % (up to 10–11 % for emphasis), extra-bold geometric caps, gold #e8a64e; keyword centre at 63 % of frame height; staggered ladder (left / indent / right-aligned tail).
4. **Keyword entrance:** tracking from +100 % to 0 in 6–8 f, starting ≈8 f before the spoken onset so it settles on the word; one tick or boom when it lands.
5. **Three-colour semantic system:** gold = opportunity, red #da1e34 = threat or out-group, white + 15-px orange bar wipe = argument pivot ("But…", "Which means…").
6. **Hook-as-UI:** in the first 1.2 s, shrink the speaker plate 1.0→0.35x over 14 f (ease-in-out, slight bulge) into a dark app screen and type the spoken question into its search bar at speech pace (≈22 chars/s).
7. **Identity sandwich:** roto speaker / stock crowd / giant title (cap ≈19 % width, bleeding off both edges, behind heads) / brand-colour backdrop, revealed on the exact identity word.
8. **Object behind the head:** 3D brand or topic object rises from behind the rotoscoped speaker over ≈20 f with rim light, under a slow 1.0→1.19x push over 48 f that ends in a transition.
9. **Metaphor cutaway ≤2.6 s with a colour drift:** background radial shifts neutral → red across the sentence; captions move to the top 12–21 % band when the graphic owns the centre.
10. **List → pedestals:** one pedestal per item rising in ≈12–16 f, an icon dropping on the item's spoken keyword (±3 f), boom + hit per drop, the item label printed on the pedestal instead of a caption.
11. **Dim-and-overlay:** take the speaker to ≈46 % luminance and defocus over 30 f, then layer a literal pun of the idiom ("upper hand" = a hand) without typing the idiom.
12. **Leak chapter break:** 7-f warm leak ramp (luma ~50→195) + 2 pure white frames + 1 residue frame, placed in the pause before "But…".
13. **Hide every jump cut:** put a strobe, leak, zoom-through or graphic over each A-roll cut (10 of 11 here).
14. **SFX density ≈12 per 10 s** on a quiet tonal bed ≈24 dB under the voice; pull the bed's bass for the final 3 s, then hit on the last word.
15. **Before/after wrapper:** EDITED panel in front, 55 % of canvas width, at the right; RAW 79 % of its height, behind and left; both vertically centred on y=640; bold labels; static #e6e6e6; giant footer CTA. Improve on it by making the panels bigger and showing the truly raw take.

---

## 12 RAW vs EDITED delta

**Wrapper geometry (measured at 720x1280):**

| element | box | notes |
|---|---|---|
| EDITED panel | x 285–679, y 290–987 (394x697, 0.566 ≈ 9:16) | centre (482, 638); 55 % of width; radius ≈14 px; in front |
| RAW panel | visible x 49–284, y 364–917 (236x553) | full width ≈311 px if 9:16, so ≈76 px (24 %) is hidden under EDITED; centre y 640.5; radius ≈10 px; 79 % of EDITED height |
| "RAW" label | x 126–233, y 298–331 | cap 34 px, medium weight, tracked; 33 px above the panel |
| "EDITED" label | x 383–578, y 245–281 | cap 37 px, bold, centred on the panel (480 vs 482); 9 px above |
| footer "DM" | x 169–352, y 1069–1151 | cap 83 px, black heavy sans (≈Montserrat Black or Archivo Black) |
| footer "FOR / WORK" | x 377–553, lines y 1068–1106 and 1117–1156 | bold italic, 2 lines ≈39 px; footer block centred at x 361 |

Layout: content spans y 245–1156; the panels fill ≈44 % of the canvas area and the rest is empty grey.

**Sync:** frame-locked. Grey-level MAE between ED and the warped RAW is minimal at offset 0 for all 10 test frames (3.8–4.2 vs 4.2–16 at ±1–3 f). No speed change and no retime.

**Grade: none added.** Per-channel linear fit ED = 0.975–0.998 × RAW + (−0.1…+0.6); binned luma curve is identity within ±1.5 levels; saturation 0.515 vs 0.515; ED/RAW luma ratio 0.98–1.01 at the corners (no vignette). Swatches: wall #3d1e11 → #3e1e15, skin #5a3723 → #5a3723. The warm low-key look comes from the shoot, not the edit.

**Framing:** identical base framing (ED shows 97 % of RAW height). Every scale change is an edit event: hook settle 1.35x, shrink to 0.35x, two zoom-ins (1.26x, 1.19x, plus 1.07x), and three settles from 1.34–1.36x (table in §4).

**Cuts:** the RAW panel has the **same 11 jump cuts** (f112, 224, 303, 426, 508, 549, 632, 779, 851, 932, 977), so the showcase's "RAW" is the tightened assembly. Pause removal and take selection are **not** shown as an edit contribution. The edit's contribution on cuts is **concealment**: 10 of 11 are hidden (leak f112, zoom-cut f224, zoom-through f303, invert f426, under the pedestals f508/549, zoom-through f632, white flash f779, under chess f851, strobe f932); only f977 is exposed. The edit also adds visual changes where RAW is continuous: f0–7 strobe, f34–48 shrink, f162 background swap, f350 knot, f461 portal cut, f802 dim.

**What the edit added (inventory):**
- 19 caption cards, plus 3 set titles (REALTOR, MOST AGENTS, pedestal labels).
- 2 full-screen 3D/stock scenes (8.3 s).
- 5 composited stretches (11.6 s) using rotoscoping (crowd, knot), scaling into a UI, dimming and defocusing.
- 4 flash transitions, 3 zoom-throughs, 1 portal.
- 42 SFX and a tonal music bed.
- Loudness at −14.7 LUFS.

**Screen-time delta:** the unaltered full-frame speaker (mode A) is 41.7 % of the ED runtime. For 56 % of the runtime (B + C = 19.9 s) the EDITED panel looks nothing like the RAW panel next to it. That constant side-by-side contrast is the ad.

**Why before/after sells editing:** the RAW panel is a live control sample, same words and same frame, so every difference is attributable to the editor. The viewer's eye goes back and forth (left plain, right busy), which adds dwell time. The client's own hook ("Agents keep asking me…") carries retention for the agency's ad. The static #e6e6e6 card keeps all motion inside the EDITED panel, and the 83-px "DM FOR WORK" footer is the only text outside the panels, so the CTA can't be missed. An improved version would show the truly raw take with its pauses and its time-saving, larger panels, and a brand or handle.
