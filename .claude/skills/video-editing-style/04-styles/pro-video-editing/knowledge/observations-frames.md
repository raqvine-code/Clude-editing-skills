# Frame-by-frame findings (pass 2, native fps strips via tools/vstrip.py)

Frame numbers at the source fps (30 unless stated). Each entry: What / When (frames) / How (reconstruction, label E) .

## f00ae5949170 "Let's make it pay" (P1)
1. **Blur-in open** f0-f2: subject heavily motion/defocus blurred, sharp by f3 (3 frames). How (E): Gaussian/camera blur 40->0 px, ease-out, or Transform scale 110->100 with motion blur.
2. **Glass frame scale-in** f2-f9 (8 f): rounded glass rectangle behind subject grows to size, soft top highlight bar. How (E): shape layer, scale 85->100 %, opacity 0->100, ease-out (expo), Fast Box Blur on a duplicate for frosted look.
3. **Sparkle pops** f4-f8: yellow "+" and "x" glyphs scale 0->120->100 with slight rotation (overshoot), one stays drifting.
4. **Comet light streak** f6-f25: thin white tapered stroke sweeps around the frame top (trim-path head and tail offset ~6 f).
5. **Loading squares** f8-f17: 4-5 lime squares light up one by one (~2 f apart).
6. **Lead line type-on** "You're not" f11-f17 (~1 f per character).
7. **Keyword slam** "price." f26-f30 (4 f): enters from left with strong horizontal motion blur and slight scale, lands hard; lime full stop.
8. **Accent script** "competing" f27-f34: script/italic word writes in with lime glow, glow decays to white over ~8 f.
9. **Word swap** f89-f97: glass frame scales up and fades (f89-f93), old words smear horizontally (directional blur), "value." appears f95-f97; lime hand-drawn circle strokes on around the text f95-f104 (10 f) then fades.
10. **Exit + whip transition** f123-f138: upper lines leave to the right one by one with lime motion trails (stagger ~3 f), frame scales up with blur f137, cut f138 to black slide where "show" enters from left with heavy motion blur, sharp by f141 (3-4 f); two arc brackets rotate in.
11. Music: 50 % of visual events within 70 ms of an audio onset vs 19 % chance -> **cut/animation on beat (V)**. Implied pulse 104 BPM.

## 4a6cb105b501 (P1)
1. **Streak carries across cut** f56-f62: white streak travels across subject shot, frame zoom-blurs (f60-f62), cut to dark arrow tile with the same streak continuing = motion-matched transition (V).
2. **Icon morph** f62-f78: arrow rotates 45 deg down while colour lerps white->red (~12 f); text "Your profits aren't" types on letter by letter; red line chart glows behind.
3. **White-out exit** f182-f184: scene blurs and over-exposes to white in 2-3 f.
4. **Rack-focus entry** f184-f192: next shot starts ~12 px blurred, sharp in ~8 f; text ("more") fades in after focus settles (f193), then "operational / costs" (small light line + giant heavy word).
5. Desaturated grainy flash frame at 5.0 s before the colour scene returns (S).

## fdf671691d67 (P1 pixel variant)
1. **Pixel block glitch** f63-f72: a white square jumps position in 2-frame steps (no easing, stepped), grows to cover the face (f67-f68), then RGB/pixel horizontal displacement on text and subject (f69-f72), cut to black with tiny squares (f73).
2. **Logo slow push-out** f159-f166 on white card ("Let Claude" + asterisk): scale ~100->92 %.
3. **Blur-in subject** f167-f170 (3 f) then "Handle" enters with RGB echo/smear flicker f170-f176 (~6 f); "the" "rest" type in; corner brackets fly from outside to corners f176-f181 (5 f).
4. Bitmap/mono pixel display font with square corner dots framing each word (S).

## 32ec48946f60 Hera (P2)
1. **Glitch intro** f0-f2: dark, blurred, RGB-split frames, cut to bright studio f3.
2. **Word-by-word lead** "My name is" f4-f10, words placed with small jitter; 8-bit pink/red pixel squares flicker around.
3. **Letter-stagger display word** "Hera" f10-f23: H, e, r, a appear one by one (~3 f each) in giant red heavy italic; completes on the spoken word (speech "Hera" at 0.70 s, word complete at 0.77 s) (V).
4. **Red energy streaks** f36-f42 shoot up from the floor across the subject; **halftone dot ring** expands from centre f42-f47 revealing a red-framed photo card; next display word ("CEO") starts letter by letter.
5. **Laser sweep + halftone transition** f145-f160: red laser line sweeps, cut to new scene with blur, red halftone ring expands outward ~13 f and dissipates; pixel blocks.
6. Text sits behind the subject on some words ("Clients", "CEO" region) = person matte (S).

## 91170c08735e Raj (P3 inside P4 shell)
1. Outer showcase shell is static (no camera move) for the whole 16 s (V, still-frames 81 %).
2. **Caption build** f19-f24: small sans lead ("if you want") + serif italic display ("To achieve") fade/scale in ~5 f, soft; display word appears ~0.2-0.4 s before it is spoken.
3. **Wipe-bar reveal** f91-f93 and f102-f104: a white full-height bar wipes across the card (3 f) and reveals the next caps phrase ("YOU NEED", "TO BE"); then a green highlight box grows behind the word left->right (f96-f98).

## 9783b41eed0a canvers 70x (P4)
1. Single continuous composition, no cuts in the shell (V). Inside the AFTER card the talking head is cut normally.
2. **Neon pill captions** f190-f192: red glowing outline pill with white text pops in (scale ~80->100, 3 f), list items stack downward one per spoken item; spoken "oil" at 6.22 s, pill visible 6.33 s (lag ~0.1 s) (V).

## 1ef4cbf46f08 somrat (P5)
1. **Frame shrink-to-card** (S 1.0-1.5 s): full 16:9 shot scales down into a rounded card over red radial gradient while outline+fill text "Video Editing" sits across it.
2. **Canvas pan** f84-f124 @15 fps sample: card slides out left at roughly constant speed (~1.3 s) while a dashed timeline line with arrow ticks scrolls in from the right to "ZERO" = one long horizontal canvas with a camera pan (V).
3. Fanned, rotated photo cards with labels ("zero skills", "no connections") (S); number counter ₹993651 -> ₹1000000 (S); phrase-per-beat text slides on red ("no rich parents" / "no cheat codes" / "no special treatment") (S).

## 94a17cc80891 100 AI Agents (P5, 59.94 fps)
1. **Card shrink open** f9-f87 (~1.3 s): full frame becomes a rounded card with white/red stroke and keeps shrinking smoothly (ease-in-out); red glow swoosh revealed in the corner; caption types word by word under it with a **red underline progress bar** that grows with the sentence (V).
2. **Behind-head giant word** "ACHIEVABLE" f633-f637: appears in ~2 frames (fast fade), behind the head (matte); spoken at 10.92 s, text full at 10.63 s (leads ~0.3 s) (V). Followed by a scale punch-in with motion blur f641-f651 (~1.1x).
3. **Hexagon mosaic transition** f1855-f1885 (~0.4-0.5 s): hex cells reveal the next location from the right, cells semi-transparent during the change (V).

## 7a74184fe0d2 AI Workflow (P5 glass-UI)
1. **Whip left** f120-f124 (4 f): title + collage slide left with heavy motion blur into red-gradient UI world.
2. **Bar-to-card morph** f126-f140 (~0.5 s): a thin red bar grows into a card; chevrons "< >" then appear and the card behaves as a carousel (V).
3. **Node branch growth** f831-f867 @15 fps sample: card scales up slightly, bumps down ("settle"), branch pills slide out from behind it and connector lines draw (~0.5 s) (V).

## cab9807914a3 Intermediate (P5)
1. **Title reveal** f0-f30 @15 fps sample: "Intermediate" revealed left->right with feathered mask + per-letter blur over ~1 s; dashed line extends; exit with horizontal streak/whip at f44 (V).
2. **Side panel slide** f134-f142 (~0.27 s): red panel slides in from the right edge; header then bullets type in word by word, one bullet per spoken point (V).

## Cross-reference measurements
- Key-word graphic timing vs speech (V, 4 checks): lands 0.1-0.35 s before or at the spoken word; neon list pills lag by ~0.1 s.
- Speech rate 150-213 wpm (transcripts).
- Music-only motion ads: on-beat events only clearly in f00ae5949170; fdf/4a6 show no beat lock above chance (V, onset analysis).
- Integrated loudness of reposts -16.6 to -12.4 LUFS (V; platform-processed audio, use only as a range).
- Share of frames with no visible change (framediff <= 2): 29-97 %; podcast/showcase shells 81-92 %, motion ads 47-65 %, Hera 29 % (V).

## 2026-11-17 batch (dd0713672607, 48a38ca593e4, 8f956030b898, 0e5c76cf941e)
Evidence sits in the profile files P6-P9 (1 fps sheets + 11 close-ups at 240 px; no frame-numbered strips yet). Shared findings across all four (S, >= 3 refs):
- Every one is a BEFORE/AFTER showcase post: still shell, motion only inside the AFTER card, raw card greyscale or plain.
- Every one puts one giant word BEHIND the subject (condensed sans P6, red condensed P7, gold serif P8, lime serif italic P9).
- One accent hue per video + white (violet, red, orange, lime); B&W used as a contrast tool (P7 punch, P8 B-roll, P6 before).
- Masters at -14.1 to -14.6 LUFS (V, all four).
- Graphics pop on the exact spoken word; a recurring motif (ribbon, ??? icons, brand dot) ties the edit together.
