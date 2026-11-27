---
name: video-editing-style
description: Use when planning, editing, building or reviewing a faceless voice-over explainer reel in the "editorial motion-graphics" style - white studio cutout scenes that flip to dark glow scenes, dual-font word-by-word captions, logo pie-wedge stats, light-leak flash transitions, whoosh SFX on every cut. Covers pacing, type, motion, transitions, grade, sound and a build workflow (After Effects first, also Premiere/CapCut/Remotion).
---

# Editorial motion-graphics reel style

Learned frame-by-frame from a 29.9 s finance explainer (720x1280, 30 fps, 896 frames, 10 scenes).
Pixel values below are for **1080x1920**; frame counts are at **30 fps**.

## 1. Identity (the 6 things that make it this style)

1. **No footage.** Every scene is a designed composition: cutout subject or 3D object + caption + one graphic.
2. **Light act → dark act.** Starts on off-white "studio wall", flips to near-black at ~37% of runtime and stays dark.
3. **Dual-font captions**: bold sans statement + thin italic serif emphasis, revealed word-by-word on the voice.
4. **One accent hue per scene**, everything else monochrome.
5. **Nothing is ever still** (4 of 896 frames had zero motion): everything eases in, then keeps drifting.
6. **Every scene change has a designed transition + SFX**; plain cuts only inside a repeated template.

## 2. Script and pacing template

Voice-over drives everything. ~160 wpm, short declaratives, 0.3-0.6 s gap between sentences; cuts land in that gap, 0-2 frames before the next sentence's first word.

| % of runtime | Beat | Scene length | Look |
|---|---|---|---|
| 0-27% | 3 parallel examples ("[Name] owns [X]% of [brand]") | 80 f each, identical | Light |
| 27-37% | Payoff: all 3 subjects together, then "They know this" | 68 f + 30 f | Light |
| 37-50% | Core insight with one metaphor object | ~105 f | Dark |
| 50-61% | Consequence ("If you help... you'll make...") | ~90 f | Dark, B&W |
| 61-74% | Contrast pair: stop X / start Y | ~120 f (two halves) | Dark, red → green |
| 74-78% | Punchline | 38 f (shortest scene) | Dark, gold |
| 78-94% | CTA with product objects | ~128 f | Dark, brand hue |
| 94-100% | Endcard, 2 lines, hold ≥ 1 s | ~47 f | Dark |

Rules: average scene 3.0 s, range 1.3-4.3 s. Rule of three in the hook, with the repeated template getting no entrance animation after the first. A new word appears roughly every 0.35 s. Captions are a **condensed** version of the VO (drop "and yet", "because"); when the graphic already says it, show no caption at all (the line "you need a bigger pie" is only shown as the pie growing).

## 3. Two scene looks

**Light (hook)**
- Background `#F3F3F3` → `#EDEDED` soft gradient; faint topographic contour lines (~6% black) and tiny dot markers, slowly drifting.
- Thin inner shadow on the frame edge (~15 px feather, mid-grey at the corners) so the frame reads like a card.
- Subject: clean cutout, centred, filling the lower ~65%. Soft drop shadow on the wall (blur ~90 px, ~25%, offset down-right). Bottom of the body dissolves into blur, never a hard crop.
- Text near-black `#2A2829`, top-left, left margin ~13%, top at 8-10% of height.

**Dark (body + CTA)**
- Background `#030303`-`#171717`; texture is one of: concentric rounded-diamond hairlines (~8% white), dark marble, or HUD micro-text at the side edges (rotated 90°, ~10 px caps).
- One hero object, emissive or rim-lit, with bloom in its own colour spilling on the background.
- Text white with soft outer glow (radius 40-80 px, 40-60%); accent captions take the scene hue.
- Optional giant ghost word behind the subject (vertical caps, ~10% opacity).

**Both**: periphery lens blur (centre sharp, roughly the outer 10-15% of the frame soft), motion blur on all moving layers, subject always layered above the graphic for depth.

## 4. Typography

| Role | Face (pick one per project) | Use |
|---|---|---|
| Statement | Tight bold grotesk (Inter Tight / Neue Haas / Gilroy Bold), tracking -20 to -40 | Names, main clause |
| Emphasis | High-contrast italic serif (Playfair Display Italic / PP Editorial New Italic / Instrument Serif Italic) | Verb, stat, payoff word |
| Light variant | Geometric sans Light + SemiBold (Poppins) | Reflective lines, endcard |
| CTA label | Condensed caps (Bebas Neue / Oswald), blue→white gradient fill + glow | One line only |

- Every caption is **2 fonts, max 2 lines, 2-6 words per line**. Line 1 sans, line 2 italic serif (or the serif word inline: "Name **owns**").
- Sizes: light headline ≈ 66 px; stat sub-line ≈ 40 px in italic serif, tucked under the right end of the headline; dark captions ≈ 84-90 px; endcard ≈ 76 px. Line width 55-65% of frame, never over 70%. Leading tight (≈ 1.0-1.1).
- Sentence case or all lowercase for italic lines. No caption boxes, no strokes, no emoji, no highlight-word colour pops, no karaoke bounce.
- Proofread: the reference shipped typos on screen. Do not copy that.

## 5. Text animation

**Word reveal (default, ~90% of text):** per word, on its spoken onset (±3 f): opacity 0→100, Gaussian blur ~14→0 px, y +10→0 px, grey→final colour, over **6-8 f**, ease-out. Words never scale or bounce.
**Random character fade (once, for the pivot line):** letters fade in in random order over ~10 f.
**Exit:** whole block fades + slight blur over 8-12 f, or leaves with the transition. Line swaps in the same scene cross over ~12 f (old line dims back while the new one reveals on top).
**Glow** ramps with the reveal on dark scenes.

AE: one text layer per word with markers at VO word onsets (most accurate), or a Text Animator (Opacity 0, Blur 14, Position 0,10) with Range Selector "Based on: Words", animated Offset. Remotion/CSS: `opacity`, `filter: blur()`, `translateY`, easing `cubic-bezier(0.16,1,0.3,1)`.

## 6. Motion rules

- **Subject/object entrance:** rises from below the frame, expo ease-out, ~66 f total with ~70% of the travel in the first 20 f, then keeps creeping until the cut. The headline drifts up ~5-7% of frame height with it (parallax).
- **Template repeats** (examples 2 and 3): hard cut, subject already in place with a 1-2 f settle; only the text and graphic re-animate.
- **Re-stage instead of cutting:** to go from one subject to the group, fade the graphic and caption (12 f), scale the hero to ~85% and lower it, slide the others in from the left/right edges with motion blur and depth blur (20 f, ease-out).
- **Camera:** slow push-in on every scene (≈ 1-2% scale per second); one lateral pan (~40% of frame width, ~30 f, ease in-out) to reveal a second, bigger object.
- **Foreground debris** (bills, icons) crosses in front of the text, defocused and motion-blurred, at 2-3 depths.
- **Line art** (hand-drawn pointer strokes, dotted connectors, dotted ellipse around a caption) draws on with Trim Paths over 10-14 f, synced to the caption it belongs to.

## 7. Motion-graphic devices

- **Stat wedge:** light-grey disc (diameter ≈ 50% of frame width) behind the subject's head with the brand logo ghosted in grey. A wedge radial-wipes clockwise from 12 o'clock to exactly `stat% × 360°` (20% → 72°) over ~34 f; inside the wedge the logo shows in brand colour. Build: grey logo + colour logo matted by the wedge (Radial Wipe, or `conic-gradient`).
- **Metaphor object** on dark scenes: one literal object per idea (pie for share, traffic light for stop/start, statue for wealth, bills for money). Animate its *state* to carry the meaning: wedge fills, red lamp dims to ~40% as green brightens, bills rain.
- **State-linked captions:** caption colour and scene tint follow the object's state (red caption with red lamp, then green caption drawn in a different position when the lamp turns green).
- **CTA objects:** two 3D icons in opposite corners, slow rotation, slightly defocused.

## 8. Transitions (use in this ratio)

| Transition | Count | Recipe |
|---|---|---|
| **Light-leak flash** (signature) | 3 | 10-11 f. Seed a bloom on the hero object 2-3 f early → white core fills frame with rose `#E89898` / slate-indigo `#686888` edges and a fine vertical fluted-glass line texture → new scene ghosts through for 1-2 f → **first frame of the new scene is 1 f of horizontal scanlines**. Use at act changes; reuse the same leak asset every time. |
| Hard cut | 2 | Only between repeats of the same template. |
| Re-stage (no cut) | 1 | See section 6. |
| Object wipe | 1 | A foreground object fills the lens for 6-7 f; cut underneath it. |
| Invert flash | 1 | 1 f negative of the outgoing frame, then hard cut. Use before the punchline. |
| Zoom-through | 1 | A scene object flies into the camera over 8 f and covers the frame; reveal the next scene behind it. |

AE: stock light leak on Screen/Add across the cut + adjustment-layer exposure ramp; CC/Venetian Blinds for the fluted lines and the scanline frame; Invert on a 1-frame adjustment layer.

## 9. Colour and grade

- Light act: median luma ~80%, saturation very low (only skin tones and the brand wedge carry colour). Dark act: median luma ~3%, highlights up to ~85%, blacks never lifted.
- Accents measured: amber `#E48424` / `#FCB46C`, lamp red `#FC0C0C`, lamp green `#54E40C`, periwinkle `#846CCC` (text `#B8A8F8`), muted gold `#6C5424`, blue-grey wedge `#A8B8C8`. Caption tints are lighter versions of the lamp colour (pink-red, mint-green) with white on the bold line.
- Subjects: slightly desaturated, smooth/retouched skin, crisp contrast. Statues and money go fully B&W.
- Finish: bloom on emitters, periphery blur, no film grain, no LUT cast, no heavy vignette on dark scenes beyond the natural falloff.

## 10. Sound design

- **VO is the bed**: deep, close, heavily compressed male read. Master measured -14 LUFS integrated, -0.2 dBTP, LRA ~3 LU, near-mono.
- **No prominent music**: between sentences the mids and highs fall to the noise floor; only a faint low rumble sits underneath. If music is used, keep it a sub/pad at least 20 dB under the VO.
- **SFX on every scene change**: a short airy whoosh or click (energy 6-16 kHz, 100-200 ms) within ±3 f of the cut. Heavier whoosh for light-leak flashes and the zoom-through.
- **One sub impact**: a 20-80 Hz boom/riser about 1.3 s long, ~20 dB above the bed, under the mid-reel reveal and into the flash that follows. Use it once.
- Light ticks or swishes may accent word reveals and line draw-ons; keep them under the VO.

## 11. Build workflow

1. **Script** to the beat table in section 2. Mark the pivot line, the punchline, and one line to show without a caption.
2. **VO** first (record or TTS), compress hard, trim gaps to 0.3-0.6 s. Get word timestamps (Whisper or manual markers).
3. **Assets**: subject cutouts (remove background, upscale, retouch), brand logos as vectors in grey + colour, one metaphor object per dark scene (3D render or clean PNG), textures (contours, hairline pattern, marble), light-leak clips, whoosh/click/boom SFX.
4. **Comp** 1080x1920, 30 fps. Build the light template once and duplicate it for each example; build each dark scene around its object.
5. **Animate** in this order: subject/object entrance → graphic state → word reveals on VO markers → continuous drift on everything → foreground debris.
6. **Transitions** per section 8, then SFX on each.
7. **Finish**: glow, periphery blur, motion blur on, loudness to -14 LUFS, export H.264.

Tool notes: After Effects is the native fit (the reference is an AE project). Premiere/CapCut: prebuild cutouts and graphics, use keyframed blur+opacity per word and a light-leak overlay on Screen. Code (Remotion): `spring`/`interpolate` per word from the timestamp JSON, `conic-gradient` wedge, `mix-blend-mode: screen` leak, SVG `stroke-dashoffset` for line draw-ons.

## 12. QC checklist

- [ ] Hook starts moving by frame 4; first word on screen within 0.15 s.
- [ ] Each caption: 2 fonts, ≤ 2 lines, every word lands on its spoken onset.
- [ ] Wedge angle equals the stated percentage; logo colour only inside the wedge.
- [ ] No frame-static scene: drift on background, subject and text.
- [ ] One accent hue per scene; light → dark flip happens once.
- [ ] Every scene change has a transition from section 8 and an SFX hit.
- [ ] Light-leak flash ≤ 11 f and ends on a 1 f scanline frame.
- [ ] Punchline is the shortest scene; endcard holds ≥ 1 s after its last word.
- [ ] Spelling and grammar checked on every caption; safe margins ≥ 10% left/right, captions clear of platform UI.
- [ ] -14 LUFS, true peak ≤ -1 dBTP for delivery (reference peaked at -0.2).

## 13. Not this style

Talking-head jump cuts, boxed or karaoke captions, emoji, stock B-roll montage, beat-synced music edits, zoom-punch on faces, colourful gradients, more than one accent hue in a scene, static holds.
