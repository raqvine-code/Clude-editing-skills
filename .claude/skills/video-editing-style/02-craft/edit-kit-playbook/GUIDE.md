---
name: edit-kit-playbook
description: Use on every edit (short or long) as the second layer after my-editing-rules - the distilled Edit-Kit (40 open-source HyperFrames video skills, vendored in 07-edit-kit-reference) - routing, beat grammar, speech-to-visual map, theme and typography rules, caption model (drop/rail/embed), motion seam law, sound cue sync, QA gate, and the reusable MotionKit/CreatorFX helpers.
---

# Edit-Kit playbook (learned 2026-11-17)

Source: `Downloads/Edit-Kit.zip` (core kit by Sahil Sharma, MIT; extras by other open-source authors, licences in
`07-edit-kit-reference/licenses/`). Full copy, unmodified: `07-edit-kit-reference/<layer>/<name>/GUIDE.md`. Not installed globally and
its installers were not run; read a sub-skill only when this page points to it.

**Rank of rules:** the user's rules (`my-editing-rules`, `mistakes-to-avoid`, the chosen style skill,
`shorts-editing-pro` LEARNING-LOG) > this playbook > kit presets. Known conflicts, user wins:
- Kit says smooth zooms, no hard punch-in cuts. Tharun / Hormozi / Bold Impact looks use punch-ins on purpose: keep them there.
- Kit says code-made audio only. The user approved Mixkit / Freesound / Pixabay / Pexels downloads: keep using them.
- Kit fixed mix (SFX -17 dBFS peak, music 24 dB under voice) is the simple fallback; `sound-and-music-design` tiers win.

## 1. Router: which kit skill for which job
| Job | Kit skill (`07-edit-kit-reference/skills/...`) |
|---|---|
| Front door, style choice, pipeline | `edit`, `director` (11 styles) |
| 9:16 talking head | `reels` + `reels/references/presets.md` |
| 16:9 talking head / creator explainer | `youtube` + `youtube/references/presets.md` |
| Effects runtime (GSAP helpers), scaffold, finalize | `fx` (`assets/motionkit.js`, `creatorfx.js`, `references/effects.md`, `examples/*.html`) |
| Colours + fonts from footage or brand | `theme` (`scripts/analyze.py`) |
| SFX on impact frames, music bed, TTS | `sound` |
| Delivery gate | `qa` |
| Captions on an existing talking head (35 identities, 10 DNA looks, behind-subject words) | `embedded-captions`, `captions-overlay` |
| Overlay cards on interview / podcast (lower thirds, quotes, data, PiP) | `talking-head-recut` |
| Seams, camera, transitions | `motion-doctrine` (read first), `cut-the-curve`, `seam-craft`, `video-shotcraft` (shot recipe cards), `camera-arc` (2.5D orbit from depth) |
| SaaS / product / launch, no footage | `saas`, `product-launch-video`, `pr-to-video`, `oversized-cursor`, `figma` |
| Explainer from text / topic | `faceless-explainer`, `vox-director`, `slideshow`, `whiteboard` |
| Music-driven video, lyric / beat montage | `music-to-video` (26 templates + motion primitives) |
| Copy a reference look | `video-clone` -> `anime-cel`, `pixel-art`, `paper-cutout`, `crayon-storybook`, `painted-animation`, `blender-product-film` |
| 3D, particles, shaders | `threejs-animation`, `particle-system`, `shader-glsl` |
| Tools | `ffmpeg` (432-line recipe book), `general-video`, `remotion-to-hyperframes`, `frontend-design` |

## 2. Pipeline (maps onto ours)
Kit: intake -> raw cut -> words -> frame map -> theme -> storyboard -> build -> check + snapshots -> sound -> finalize -> QA.
Ours: `analyze_raw.py` (words, silences, sheets) -> PLAN.md (= storyboard: time | words | on screen | motion | SFX,
palette + fonts on top) -> `shortkit.py` or the tes2 browser kit -> stills check -> render -> mix -> QC.
- **Raw cut:** the LAST full take of each line wins; drop false starts and repeated words; close pauses inside a line;
  keep real ad-libs. Check the script first: a repeated opening can be deliberate. Edit the whole clip, never stop silently.
- **Frame map** before placing anything: frames at 3-4 moments with a 10 % grid, face box at the TIGHTEST zoom, empty space per shot.
- **Snapshot 0.3 s after each entrance**, not mid-animation, and look at every one.

## 3. Beat grammar
**9:16:** strongest line first; a giant word (behind the subject if the wall allows) or claim on screen by 1.5 s; captions
from word one; change something every 1.5-3 s; end on a payoff word + hold or CTA, never mid-word.
Safe zone x 150-930, y 210-1530 (overshoot included). Graphics band below the chin, captions under it; a short hook
word may sit above the head. Hide captions while a giant word is up.
**16:9:** text lives on the empty wall (left x 96-640 when the speaker sits right), soft dark left scrim on bright walls;
a designed beat every 1-3 sentences, speaker-only stretches between; smooth zooms 4-6 per minute on impact lines only
(0.5-0.9 s ease in, hold, ease out); pattern break every 30-60 s (PiP showcase, light studio box, full-frame graphic);
keep the last 20 s of long videos clear for end screens. Safe zone x 96-1824, y 54-1026.

## 4. Speech -> visual map (visual must match the exact words)
| They say | Show |
|---|---|
| a list | checklist chips, each landing on its word, tick draw-on |
| "not X", wrong way, what others do | red X chip or strike-through, then slam the right word |
| a number / stat | rolling counter or big condensed number (never invent one; flag illustrative UI numbers) |
| "the right people / buyers" | target ring + avatars |
| "everyone says it" | 3 REAL posts (X/Threads cards) the user picked |
| the product / course / kit | a recurring hero object (folder that opens, labelled papers) reused every time it is named |
| "you can make this too" | PiP: speaker shrinks to a corner with accent ring, examples fan in on a dot stage |
| "just type it" | glass prompt bar types, send pulses |
| client feedback / DM | WhatsApp-style chat with typing dots |
| "start to end", steps | glass progress bar with knob, progress steps |
| "it's 3 AM" | macOS menu-bar clock, only over a night shot or a screen |
| "the render failed" | the real export window and error dialog |
| nothing real fits | stay on the speaker with ONE key word |
Real UI recreations and the user's own screenshots beat invented mock cards. Seek-safe UI: render each UI state from
timeline time, never by appending DOM during playback.

## 5. Theme and typography
- Brand priority: client brand kit > colours the user gives > designed from the footage. One video = one brand.
  Client kits: `07-edit-kit-reference/brands/_template/brand.json`; save one per client and reuse.
- **Opposite-light accent** for creators in a lit room: red/magenta room -> ice cyan #3EE0FF on graphite #0B0D12,
  text #F5F2EA; blue/teal room -> amber #FFB547; green room -> magenta #FF5FA2. Gold only when the words say gold.
- Accent: the hue farthest from the frame's dominant colours; >= 3:1 contrast for big text. Red only for negatives.
- Font pairs (serif lead + bold sans key): luxury Playfair Display Italic + Inter Tight; editorial DM Serif Display +
  Inter Tight; clean Instrument Serif + Poppins; bold Playfair 900 + Montserrat 900 Italic / Anton; tech Instrument
  Serif + Inter Tight + JetBrains Mono numbers. Free Google fonts only.
- **Human typography:** big words -0.015em tracking with .08em word-spacing (words never merge); sentence-case sans
  labels; NO wide-tracked uppercase mono kickers (reads "AI-made"); even gaps between lead, key word, icons, cards;
  no em/en dashes on screen.

## 6. Caption model (embedded-captions)
Every phrase is **drop** (filler, stutter: not shown), **rail** (default readable caption in front, a punch word may get
an inline accent) or **embed** (the earned peak: one big word behind the subject). Rules:
- Embed is scarce: <= 1 per beat, never two co-visible, >= 0.6 s air between hero windows, one apex per clip.
- Each caption >= 0.5 s on screen (>= 0.4 s per word); timings within 80 ms of the transcript; a group's window must
  start at or before its first word (late mounts shipped 800 ms lag bugs).
- No two groups overlap in both time and screen region. Face >= 30 % uncovered in every 0.3 s window.
- Screen/cream blends wash out on walls > 180 luma: use ink (multiply, "printed on the wall") there.
- Animate transform only: never letter-spacing or blur on inline-block words (reflow line jumps).
- Footage stays ungraded in caption-only jobs; texture lives inside the caption element, not over the frame.
- 18 principles (`embedded-captions/references/aesthetic-principles.md`): subject wins; occlude, don't hover; contrast by
  hierarchy (blend -> stroke+shadow -> narrow gradient bar -> local dim; white pill last); kill the constant lower third;
  one family, two weights; tracking tightens as size grows; body cap height 3.5-5 % of frame height; one hue +
  neutrals; stagger is the main expressive axis; emphasis escalates within a phrase; break rhythm once per 30 s;
  caption what adds, cut what restates; segment on breath, not duration; letterbox is caption space.
- DNA looks: cream (warm dark), ink (bright), editorial (Bodoni lowercase italic), keynote (white Inter 800 centre),
  documentary (burn-in, no hero), loud (Anton slam + ripple), neon (sign ignition), glitch (RGB split snap),
  chrome (liquid metal + one sheen), velocity (streak + skew along motion vector).

## 7. Motion law (motion-doctrine, cut-the-curve)
- **Vector law across a cut:** same axis; same direction (on Z, the sign of scale change); entry speed = exit speed via
  mirrored eases (exit power4.in, entry power4.out, same distance and duration); the cut lands mid-motion on both sides.
- Exit opacity finishes at 25-30 % of its travel (fade ~0.18-0.3 s). Stage background opaque (white-flash guard at seams).
- Seams: zoom-through, inverse zoom-through, cut-the-curve (default), waterfall cut (word by word), rack-focus blur-cut.
- In-scene: waterfall entry (next element starts within +-2 frames of the previous; heavy elements travel further and
  longer), nudge curve (slow-fast-slow group slide).
- No idle wobble: the frame keeps gaining information (staged reveals, camera with intent, UI that progresses,
  cursor-led action whose click ignites the next beat). Stillness right before the climax.

## 8. Sound (kit fallback; `sound-and-music-design` wins)
- Cue time = the IMPACT frame (pop peaks, card lands, cursor presses, wipe crosses centre), not animation start;
  whooshes/risers start early and peak on the frame. Within 1 frame (33 ms) or it fails QA.
- Cue types: pop (word/card/chip/counter start), click (ticks, cursor, checklist), whoosh (punch-in, zoom-through, scene
  change), swipe (strike, wipe, line draw), hit (hero word, punchline, flash, logo), shimmer (sparkle, sheen).
- Density: vertical = every pop and cut; horizontal = transitions and key reveals only; SaaS = every UI move + music.
  Max one SFX per 0.25 s, 3 variants per type.
- Voice -14 LUFS / -1.5 dBTP always loudest; voice-only edits just loudnorm. Premiere finishers get stems + cues.json.

## 9. QA additions (kit `qa`)
Keyframe every <= 1 s with closed GOP so it scrubs in Premiere (`fx/scripts/finalize.py` or `-g 30 -keyint_min 30
-sc_threshold 0`); last frame is a deliberate end; no two beats look alike; on-screen language as asked (English key
words on Hinglish/Telugu speech unless told otherwise); no leftover watermarks; the whole requested range edited;
raw cut kept only the last takes; no hard punch-ins unless the style wants them.

## 10. Reusable code
- `fx/assets/motionkit.js` (`MK = MotionKit(tl)`, one paused GSAP timeline): captions, lead, popIn, slam, blurRise, out,
  strike, zoom, camera, cardIn/Out, chipIn, counter, type + blink, click, tiltIn, zoomThrough, draw, grain, flash, drift.
  CSS: .mk-cam .mk-scrim .mk-vig .mk-grain .mk-glass .mk-dark .mk-card .mk-chip .mk-tick .mk-x. Drops into the tes2
  browser kit (also GSAP); lint: never CSS-transform an element GSAP transforms (use fromTo), no letterSpacing tweens.
- `fx/assets/creatorfx.js` (`CF`): decode (scramble reveal), shimmer + .cf-gold/.cf-silver, folder/openFolder, pipIn/Out,
  camBox/camFull, lightStage (blobs + dot grid), post, chat, progress, rise/fall.
- Scripts: `fx/scripts/words.py --refine`, `finalize.py --target social|youtube|youtube4k|master`, `new_project.py`,
  `theme/scripts/analyze.py --style <id>`, `sound/scripts/sfx_music.py`, `mix.py`, `tts.mjs` (Kokoro, free),
  `youtube/scripts/remove_logo.py`. Run scripts by path with `python3 -I`; HyperFrames via `npx hyperframes` (Node 22+).
- Footage fixes: <= 720p source -> `scale=...:flags=lanczos,unsharp=5:5:0.6`; corner watermark -> base zoom 1.12-1.14;
  background logo -> patch from above; screen recordings cropped to content, moving segments only; clip ending
  mid-sentence -> end after the last full phrase with a 0.25 s audio fade.

## 11. Styles the kit names (pick ONE, see presets files)
9:16: Real Estate (Agent Story / Luxury Walkthrough / Project Launch Ad), Construction (Progress / Contractor Talk /
Renovation Before-After), Bold Impact, Ali Abdaal Clean, Faceless Kinetic, Podcast Clip, Finance.
16:9: Creator Explainer, Creator Light Studio, Clean Talking Head, Gadzhi Cinematic, Vox Explainer, Documentary Collage.
Measured examples of four of these looks from the user's references: `pro-video-editing` P6-P9.
