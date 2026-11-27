---
name: video-intro-design
description: Use for any short, very dense intro, hook, cold open or title sequence (20-40 s) cut from one locked-off talking-head take. Build kit and rules - browser-side camera on a 2560x1440 plate (pixel-exact punch-ins), Vision person mattes for giant type behind the head, measured accent colour, period UI (Win98/BIOS), dither-through-black transitions, phone-speaker-safe procedural SFX, and six-lens QA. Built on the Y2K intro.
---

# Intro motion design (Y2K intro, 2026-10-01)

An intro is not a short explainer: 33 s carries about 90 SFX cues and about 28 graphic events, each keyed to a measured word onset. Long-form habits break at this density. Siblings: `youtube-long-video-editing`, `motion-graphics-style`; Deepak's word wins (`my-editing-rules`). Old `experiment/` paths are historical; reusable code lives in each video's `code/` folder. Tags: [USED] = done on this intro; (Claude) = my rule, not yet approved.

## 1. Pipeline
1. **Recover the script exactly.** Run `faster-whisper large-v3` on VAD-aligned chunks (not the whole file; long segments merge and hallucinate), then cross-check against Deepak's own transcript file. That file, not the ASR, is truth (Telugu/English ASR is unreliable per sentence).
2. **Measure the phrase map first**: 5 ms RMS envelope, speech runs, pause lengths, stress peaks. Gives the real cut points.
3. **EDL = trims only**: a table output frame to source frame, so re-timing never re-extracts frames.
4. **Grade once, extract at native 2560x1440**, one ffmpeg pass, `-q:v 3` (about 100 s for 1982 frames). Vignette, grain and masks go in the browser, never baked.
5. **Person mattes**: macOS Vision `VNGeneratePersonSegmentationRequest`, `.accurate`; about 1.8 s/frame, 6 parallel processes about 10 min for 2000 frames.
6. **Scenes** in HTML + GSAP on one clock, rendered in headless Chrome at **deviceScaleFactor 4/3** (captures are 2560x1440), downscaled to 1920x1080 with lanczos at encode.
7. Stills QA, fix, full render, six-lens QA, fix, final render. Budget two full renders (1937 frames at 28 % supersampling: about 3.5 min render + 1.5 min averaging + 5 min encode on a 6-core i7).

## 2. Camera: punch-ins can be pixel-exact [USED]
Plate 2560x1440, stage 1920x1080, so **zoom 1.3333 is a 1:1 crop** (1.005 of ffmpeg-crop sharpness).
- `k = 0.75 x zoom`. **Hold only where k is exactly 0.75 or 1.0 and the translate is an integer.** Off-grid landing costs more (0.885) than zooming past 1.33 (0.870): a hold snaps, a move does not. `camTrack` returns `snap:true` only when two keyframes are identical.
- 1:1 presets: `PUNCH` (centred), `PUNCH_HI` (chin-up), `SPLIT_R` / `SPLIT_L` (head in one half, 900 px panel in the other; zero sharpness cost). Everything between is transit, never rest.
- `will-change: transform` does not soften the punch-in (captureScreenshot forces a full re-raster).
- A `power3.inOut` leg over 2.9 s is motionless for its first 0.7 s and last 0.4 s. Split long pushes: `out3` off the cut, then `in2` into the end.
- Two identical keyframes = dead camera. A hold > 1.2 s while he talks must be a micro-drift (3-4 % of zoom).
- **Snap OUT on a hero word, snap IN on a negative word** (pull-out gives room; push-in reads as panic).
- Cap the punch per shot by its own softness (mean abs-Laplacian on the face band), not one global number. Shots 4-5 had 35-45 % less detail than shot 3 despite tighter framing.

## 3. Giant type behind the head [USED]
- Layer order: plate, **dark band (`L_behind`)**, type, **person cut-out (`L_person`)**, scrim, scene. Without the band white on the bare wall is 1.9:1.
- Vision mattes are opaque greyscale PNGs: use `mask-mode: luminance; -webkit-mask-source-type: luminance`. Default alpha mode is a no-op and the unmasked plate silently covers everything below (symptom: graphics "disappear").
- A long word loses glyphs ("SHOCKING" at 268 px lost three letters). Measure the occluder's x range in the letter band, then set `x` and `size` so the silhouette eats **at most one letter** (the first).

## 4. Accent colour is measured [USED]
Sample the plate first. On the Y2K footage skin (Lab hue 52 deg), door (52), lampshade (54), wall (60) sit in one 9 deg band, so amber/orange dissolves into his face (dE 33-41). Cyan at 215 deg is the maximum separation.
| colour | value | rule |
|---|---|---|
| accent | `#00E5FF` | 1.03:1 on the bare wall, invisible unplated; exists only on a `#06070A` plate, so it cannot leave the plate |
| chrome | `#C0C0C0` | 1.22:1; plated only; exactly one hero word per film |
| alarm | `#E23A2E` | turn words only; two reds in one frame must be the same red |
| amber | `#FFB000` | only inside a fully plated frame (DOS/BIOS card, dialog marker) |
- Stop every 1 px cyan rule where the dark backdrop stops.
- Small cyan labels need their own chip `rgba(6,7,10,.9)`, 7/16 px padding (a 640 px bottom scrim is alpha 0.05-0.10 at y 600).
- Never put a label in the mouth band.

## 5. Composition and hierarchy [USED]
- **Chroma beats size; size beats position.** Seven hues put reference bars over the hero number; neutralising "before" bars to white at 20-40 % fixed it.
- **One object carries the beat**: panel asks (cyan "?" + blinking AWAITING caret), answers with the same chart, expands to full frame on the number. Morph, don't replace.
- **Never pre-draw the answer**: bars created at `scaleY(0.03)` showed 9 px stubs for 2.6 s. Create hidden, reveal on cue.
- Parent a component to the thing that slides (a chart on `c.root` tore off its panel for 5 frames).
- **Qualifier always on screen**: `Source · …` bottom-left; give `srcTag` explicit `z-index` or it paints under an opaque panel.

## 6. Transitions [USED]
- **Dither-through-black**: 16 Bayer steps to full black at a chosen instant, 16 back; black instant on the cut. A full-frame scene must end exactly at that instant. It also hides an EDL join (hold the card through the pause).
- Scanline flash: translucent scan over the picture, **peak alpha <= 0.35**; 0.55-1.0 reads as a glitch artifact.
- **One flash, never a train**: five 1-frame flashes 4 frames apart is a 16 Hz strobe (photosensitivity risk). One flash, 0.12 peak.
- Period UI (Win98 dialog, BIOS card) appears in **one frame**, never eases, no drop shadow; integer px, `image-rendering: pixelated`, `-webkit-font-smoothing: none`.

## 7. SFX: phone-speaker rule [USED]
Loudness meters (pk50) are band-blind: a 40-120 Hz hit vanishes on a phone. Through a 300 Hz high-pass: `imp_crush` -25.7 to -43.8 dB (20.4 loss), `imp_sub_land` -26.7 to -49.6 (23.0), `dither_wipe` 0.2 loss.
**Fix:** give every sub-bearing hit a **150-400 Hz knock** and a **1.2-3.5 kHz click** (4 ms attack, about 25 ms decay); `phone_balance(x, target_loss_db)` sets the sub gain so full-band is only **5-8 dB above** the >300 Hz level. Split bands with zero-phase `sosfiltfilt` (causal lowpass + `x - lo` is not complementary and the solver silently does nothing). Verify phone-band hierarchy: hit > transition > text entrance > tick.

Other rules:
- Cue `gain` in the scene file is the absolute target (dB vs voice RMS); the mix applies `gain - baked_level`. Change the cue, not the baked level.
- A sting only brands a moment if its first appearance IS that moment (`ui_err` on every dialog open taught the ear "buzz = window").
- No cue without a picture event (a landing on a frozen match-cut card put three sub hits in 470 ms).
- Sub-bearing sounds need **>= 300 ms spacing** (+3.5 dB buildup at 60 ms, 0 at 550 ms).
- A hit paired with a 1-frame flash and shake must be sample-locked (+25 ms), not +120 ms (ear fuses within about 45 ms).
- A riser must land on something.
- If Deepak will score it: **no music, master -17 LUFS / -1.5 dBTP** (not -14), ship `stem_voice.wav` + `stem_sfx.wav`.
- Texture beds narrowband and outside 250-1000 Hz: CRT whine at 7812.5 Hz (15.625 kHz dies in AAC) + 50 Hz Indian mains (not 60). Broadband beds fight consonants.

## 8. Six-lens QA (Claude's rule) [USED]
After the first full render run six independent reviewers on the real 2560x1440 frames (not just contact sheets), reporting measurements: **frame design, typography, motion and timing, continuity, colour and grade, sound against picture**. Attack each finding with a skeptic that defaults to refuting it. Found on a "finished" film: a 16 Hz strobe over the match cut; impacts 20-26 dB down on phone; one shot a third of a stop under for 5.3 s (verify graded output, not intended correction); `radial-gradient(118% 150% …)` putting both vignette stops outside the picture (5 % vs 30 % falloff); CRT open catching him mid-blink for 7 frames; chapter ticks missing from the fade-out array.
Pitfall: fixing while verifiers run makes them read fixed frames and refute everything. Judge findings yourself; a refutation counts only if the verifier saw the same build.

## 9. Measurements worth keeping
- `fps=4` contact sheets drift up to 0.15 s from their label; confirm timing on numbered frames.
- `-i frames/%06d.jpg` drops frame 0; pass `-start_number 0`.
- `-shortest` trims video to audio: make the mix `round(N/60 x SR) + 240` samples.
- Per-element full-frame `filter: blur()` doubles render time; masks/transforms are free, use `clip-path`.
- `opaque: () => true` on a designed full-frame scene skips the 2560x1440 JPEG decode.
- Parallelise sub-frame averaging (`Pool(6)`): 30 min to 5 min; it is the real bottleneck, not Chrome.


Full original notes (every detail, uncut): `_archive/original-full/video-intro-design.md` in this folder.
