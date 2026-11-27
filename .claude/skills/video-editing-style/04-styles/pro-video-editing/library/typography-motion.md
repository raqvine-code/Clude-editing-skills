# Typography & Motion Library

Each technique: What / Why / How (implementation) / When / Evidence. Frame counts at 30 fps (x2 at 60 fps). Easing names = After Effects / CSS equivalents.

## T1 Three-tier statement stack
- What: small light lead line + coloured script/serif accent word + giant heavy keyword with a coloured full stop.
- Why: reads in one glance; hierarchy tells the eye which word matters.
- How: lead at 25-30 % of keyword cap height, weight 300-400; accent script 40-60 % of keyword height, accent colour + glow (Gaussian glow 10-20 px, 60 %); keyword weight 800-900, tracking -3 to -5 %, period in accent colour. Stack left-aligned or centred above head.
- When: one statement per 1.5-2.5 s beat.
- Evidence: f00ae5949170 f11-f34 (V), 4a6cb105b501 6.5-7.5 s (S), screenshot 9.

## T2 Keyword slam with motion blur
- What: big word enters from the side and lands hard.
- How: position X from -40 % frame width to final in 4 f, ease-out (cubic-bezier(0.16,1,0.3,1)), motion blur on (shutter 180-360), scale 105->100 %. Optional 1-frame overshoot.
- Evidence: f00ae5949170 f26-f30 (V).

## T3 Type-on lead line
- 1 frame per character (fast) or word-by-word on speech. Cursor not shown.
- Evidence: f00 f11-f17, 4a6 f68-f78, cab9 bullets (V).

## T4 Letter-stagger display word
- Each letter appears in ~3 f, left to right, with tiny scale pop (90->100) and no blur; finishes ON the spoken word (start ~0.35 s early).
- Evidence: Hera f10-f23 (V).

## T5 Accent script write-on with glow decay
- Script word reveals with left->right mask over ~8 f, starts accent-coloured with strong glow, glow falls to 0 over the next 8-12 f.
- Evidence: f00 f27-f34 (V).

## T6 Serif-italic display caption (podcast)
- Lead words small sans (fade 3 f) + 1 emotional word in serif italic (Playfair Display Italic / Didot Italic), fade+scale 95->100 over 5 f; lands 0.2-0.4 s before the spoken keyword.
- Evidence: 91170c08735e f19-f24 (V).

## T7 Caps phrase with highlight box
- Heavy caps phrase on B-roll; coloured rectangle grows behind it left->right in 3 f; phrase revealed by a white bar wipe (T-wipe, see transitions X7).
- Evidence: 91170 f91-f98 (V).

## T8 Behind-subject giant word
- What: 1-2 words, full frame width, white or brand colour, placed between background and person.
- How: rotoscope/person matte (AE Roto Brush, Runway/CapCut "remove background", or Mediapipe/rembg per frame), text layer between plate and matte. On in 1-2 f; optional scale punch-in of the whole shot 1.0->1.1 with motion blur over ~10 f right after.
- When: on the single strongest word of a sentence; hold 1-2 s.
- Evidence: 94a17cc80891 f633-f651 (V), 7a74 SMARTER (S), Hera Clients (S).

## T9 Neon pill caption list
- Rounded pill, red outline with outer glow, white sans text; pops scale 80->100 in 3 f; items stack downward as each is spoken (lag ~0.1 s).
- Evidence: 9783b41eed0a f190-f192 (V).

## T10 Underline-progress lower third
- Small white sentence near lower third; red bar under it grows with each word (bar width = spoken fraction).
- Evidence: 94a17cc80891 f15-f87 (V).

## T11 Side panel bullet build
- Coloured panel slides in from edge in ~8 f (ease-out), header first, then bullets type word by word as each point is spoken; panel stays while the speaker talks.
- Evidence: cab9807914a3 f134-f160 (V).

## T12 Feathered mask title reveal
- Text revealed left->right by a feathered mask with per-letter blur 20->0 over ~1 s; supporting lines/dashes extend with it.
- Evidence: cab9 f0-f30 (V).

## T13 Pixel / bitmap word with corner brackets
- Mono bitmap font, one word at a time; four small square dots at the corners; corner bracket marks fly in from outside over 5 f.
- Evidence: fdf671691d67 (V).

## T14 Number counter
- Large numeral rolls up to the target value (₹993651 -> ₹1000000) then holds; currency symbol fixed.
- Evidence: 1ef4cbf46f08 20.5-22 s (S). Duration estimate 0.5-1 s (E).

## T15 Blur-in two-font word reveal
- Caption = bold sans line + thin italic serif line (or the serif word inline), at most 2 lines, 2-6 words per line. Each word: opacity 0 -> 100, blur about 14 -> 0 px, y +10 -> 0 px, grey -> final colour, 6-8 f ease-out. No scale, no bounce. Glow ramps with the reveal on dark scenes.
- Hook words follow the voice (uneven gaps); in dark scenes words step at an even 4 f. After a flash the first word shows 6-10 f late and the line catches up within 3-4 words.
- Evidence: P12 pack f4-f50, f343-f379, f456-f486 (V). Blur and y values (E).

## T16 Random character fade
- Letters of one short line fade in in random order over about 12 f. Use once, for the pivot line.
- Evidence: P12 pack f312-f323 (V).

## Motion graphics elements
- M1 Glass frame/card: rounded rect, frosted fill (bg blur 20-40 px + 10-20 % white), 1-2 px light rim, soft top highlight; scale-in 8 f expo-out (f00 V).
- M2 Sparkles (+, x): scale 0->120->100 % in 4 f with 10-20 deg rotation; idle drift (f00 V).
- M3 Comet streak: tapered white stroke, trim-path start/end offset 4-6 f, 15-20 f travel; can carry across a cut (4a6 V).
- M4 Hand-drawn circle: rough ellipse stroke, write-on 10 f, then fade (f00 V).
- M5 Icon tile morph: rotate + colour lerp 12 f (4a6 V).
- M6 Halftone dot ring burst: radial halftone ring expanding 5-13 f, fading (Hera V).
- M7 Pixel squares: 8-bit squares that flicker/step on 2-frame holds (fdf, Hera V).
- M8 Glass UI carousel: cards slide horizontally between < > chevrons, cursor clicks (7a74 V).
- M9 Node graph: card bump, branch pills slide out, connector lines draw ~15 f (7a74 V).
- M10 Photo card pop: rounded photo with coloured frame + pill tag, scale pop with overshoot, cards fan with 2-3 f stagger (Hera S).
- M11 Eye-bar: solid red rectangle over eyes on B-roll (P3 S).
- M12 Glowing icon: white line icon with outer glow fades in under a card (94a1 V).
- M13 Stat wedge: light-grey disc (about 50 % of frame width) behind the head with the logo ghosted in grey; a wedge wipes clockwise from 12 o'clock to stat % x 3.6 deg in about 34 f; the logo shows in brand colour only inside the wedge (P12 pack f24-f58 V).
- M14 Metaphor object with a state: one literal object per idea; its change carries the meaning (pie fills, red lamp dims to about 40 % as green brightens, bills rain). Caption colour and scene tint follow the state; the second caption appears in a different place (P12 pack f347-f443, f597-f633 V).
- M15 Line-art draw-on: hand-drawn pointer strokes, dotted connector, dotted ellipse around a caption; trim-path draw 10-24 f, timed with the caption it belongs to (P12 pack f316-f330, f561-f581, f609-f633 V).
- M16 Ghost word: giant vertical caps behind the subject at about 10 % opacity, as a texture rather than a caption (P12 pack f456+ V).
- M17 Rise entrance with creep: subject rises from below the frame, about 70 % of the travel in the first 20 f, about 66 f in total, then keeps creeping to the cut; the headline drifts up 5-7 % of frame height with it. Repeats of the same template skip the entrance (P12 pack f10-f79, f80 V).
- Event-map pack devices (P13 / P14, zip 2): two-tier caption group, letter-stagger threat word, text-as-object voices (3D verdict caps, typed date card, one-word serif moral), name pill, highlighter → circle → punch, pedestal list, identity sandwich, object behind the head, dim-and-overlay idiom, graph pair with pen chase, twist word stack, halftone glue screen: recipes in `02-craft/event-map-reel-edit-style/references/devices.md`.
