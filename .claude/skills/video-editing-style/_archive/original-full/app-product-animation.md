---
name: app-product-animation
description: How to make SaaS / product motion-graphics videos (pure motion graphics, no talking head: app UI, cards, cursor, type-on, logo bookends) the way the high-demand reference reels do it — the motion grammar (morph-not-cut, motion-blur streaks, spring settle, glow-bloom impacts, cursor as actor, 3D tilt, move-hold-move rhythm), the typography rules (letter type-on with tracking collapse and colour flip), the grade (one brand colour on black or lavender-white), and the SFX recipe (which sound on which event, level, lead/lag). Learned frame by frame from refs 09-11 (Google Drive, ChatGPT, Spotify spec reels), refs 62-63 (showreel, SFX-pack promo) and ref 69 (a 14.5 s 9:16 "wireframe vs final" SaaS Short: problem text → globe → liquid star-wipe logo → payment UI → neon "Total Money" counter → glass CTA pill, with the measured beat table, palette and music-led audio), plus refs 70-74 (five UI/UX promo clips studied for SMOOTH ANIMATION: measured easing curves and durations — ease-out with a long tail, 0.15-0.22 s snaps, one 20 % overshoot on a small→big morph, ease-in-out only on fades — plus the object-chain, conveyor, circle-wipe and one-continuous-camera patterns, and a tutorial's CC Light Sweep glass-folder settings). Load for any "SaaS video", "product demo animation", "app UI motion graphics", "explainer of a feature", "logo + UI reveal", or when Deepak says a client wants a SaaS-style motion graphic.
---

# SaaS motion graphics (learned from refs 09–11, 2026-09-30; refs 62–63, 2026-10-06; ref 69, 2026-10-09; refs 70–74, 2026-10-09)

> **Note (2026-10-06):** `experiment/` paths in this skill are historical — that folder was cleared. Final videos + edit notes: `Raghu and claude/edited videos by claude/`. Reusable code: the `code/` folder inside each video folder. Reference analyses were folded into the skills and deleted.

Sources: `experiment/05_references_9-11_saas_analysis.md`, `experiment/11_references_62-63_saas_showreel_sfxpromo_analysis.md` (showreel + SFX-pack promo, every frame at 10 fps) (frame-level beat tables, measured grade) and `experiment/audio_ref09.md`, `audio_ref10.md`, `audio_ref11.md` (measured SFX inventory, sync offsets, bed handling). Deepak: **"these are high-demand videos; SFX creates the impact; learn seriously, no mistakes."** Related: `motion-graphics-style` (talking-head reels), `client-video-editing-process` (build kit: HTML/GSAP + puppeteer render + mix2.py), `my-editing-rules` (Deepak's rules; SFX/BGM from Epidemic Sound).

## 1. Structure (all three references)
Logo enters → product name types in beside it → feature story told with the UI itself (3–6 morphing states) → tagline (1–2 short lines) → logo + name again. 9–16 s. **Zero hard cuts**: the only "cuts" are a theme switch (light ↔ dark), a white-out from the bottom, or a fade-through-black. One element, one colour, one action at a time; nothing else on screen except a tiny footer credit.

## 2. Motion grammar (frame-accurate rules)
1. **Morph, never cut.** pill → card → dialog → toast → pill → check-mark; horizon arc → input bar → send button → photo tile → full frame; text → avatar circle; list → filter pills. A morph takes **6–12 frames (0.2–0.4 s)** and often adds a few degrees of 3D tilt while the shape changes.
2. **Motion blur on every fast move.** Anything that travels more than ~10 % of the frame arrives as a directional streak (logo strokes flying in, a file icon shooting up, a headline whipping in from the left, list rows rising). Nothing pops in sharp.
3. **Spring settle once.** A dropped logo overshoots once and settles (Spotify drop: stretch → overshoot low → back → settle in 10 frames). UI elements ease out with no bounce; a clicked pill **tilts −8° like a physical press** and settles.
4. **Glow bloom = the impact.** On landing, a brand-colour radial glow expands behind the element (Drive colour wash 0.3 s, blue click ripple rings that wash the whole frame, green success bloom). Impact is light, not camera shake.
5. **The cursor is the actor.** White hand cursor with a blurred trail: hover highlight jumps row to row, press tilt, click ripple, drag-and-drop. Hover states are visible (lighter row, blue button fill) before the click.
6. **Staggers.** Menu rows appear top-to-bottom 4–5 frames apart; list rows 3 frames apart; filter pills 4 frames each; check marks 4 frames apart; tagline words ≈ 0.4 s apart.
7. **Move–hold–move.** After every landing hold **0.5–1.3 s** before the next event. The rhythm is a beat, not continuous busyness.
8. **One camera move at most** (ChatGPT: a 0.7 s push-in ≈ 1.6× toward the button before the click). Otherwise the camera is locked; the objects move.
9. **Bookends**: the outro repeats the intro's logo + type-on.

## 3. Typography
- Use the product's own UI face (Google Sans / Inter-like grotesk, medium), sentence case, tight tracking. Hero words ≈ 8–10 % of frame height, taglines ≈ 5 %, UI text 2–3 %, footer 1.5 %.
- **Letter type-on with tracking collapse and colour flip**: each new letter arrives in the accent colour (or lighter grey) with wide tracking that collapses as it turns white/black; 15–25 chars/s; product name ≈ 2–3 frames per letter. Taglines build **word by word** (grey → final colour).
- **Word swap in place** ("Sound" blurs out, "Immersion" types in). Headline can **whip in** with horizontal blur. Exits fade upward or blur-wipe.
- Placement: logo/tagline centred; the feature beat can be a left-aligned hero block (H1 + 3-line paragraph + pill button); UI text lives inside the UI element. Never overlap two elements.

## 4. Grade and colour (measured)
- Dark stage: luma 6–20, blacks 0–10, a radial brand-colour bloom (blue for ChatGPT sat 30–52 %, green for Spotify sat 72–97 %). Light stage (Drive): lavender-white, luma 240, sat 7 % — not pure white.
- **One brand colour + black/white.** Glows, highlights, ripples, progress bars and the accent letters all use that one colour (plus green for "success" states).
- Backgrounds are radial gradients (lit centre, dark edges). No grain, no textures, no particles.

## 5. SFX recipe (measured — `audio_ref09.md`, `audio_ref10.md`, `audio_ref11.md`; SFX carries the impact)
None of the three has a voice-over. **83–100 % of visual events have a sound within 120 ms.** The shared grammar of every screen change: a **300–900 ms riser or reverse swell** that starts within ±100 ms of the motion start and **ends on the landing frame**, a **low landing hit (43–65 Hz sub-drop) within ±80 ms** of landing, then a **settle tick 30–100 ms later, 10–20 dB quieter**. The kit is one dry "glassy UI" family (8–14 kHz shimmers and dings, sub-drops, one tonal chime, 5–20 ms clicks); samples are reused (the same pop ×3, the same chime ×6) and only one sound per reel gets a reverb tail.

Levels are 5 ms RMS peaks for a −14 to −16 LUFS master; lead = sound onset vs the first frame of the visual (negative = before).
| Visual event | Sound (layers) | Level dBFS | Timing |
|---|---|---|---|
| logo / hero pops in | HF tick or reverse swell + 43 Hz sub boom + settle click | tick −7, boom −5…−7, click −12 | tick −130 ms, boom −130…−270 ms before the glow bloom, click +20…+60 ms |
| card / panel slides or morphs in | riser 300–520 ms + landing impact + 2–4 settle ticks | riser −18 → −12, impact −6, ticks −14…−20 | riser starts ±100 ms of the motion start, impact on landing ±40 ms, ticks +50…+200 ms |
| light ↔ dark / screen transition | bright falling whoosh 8–11 kHz (150–300 ms) + shimmer + tick | whoosh −13…−17, tick −17 | +40 ms after the cut; give one transition per reel a 1 s reverb tail |
| cursor click | 2–4 soft clicks during travel, click on press | −12…−15 (travel −27) | on the frame ±15 ms |
| hover highlight | tiny tick | −30…−33 | +60…+180 ms after the highlight |
| word / chip pops in | one pop (1.29 kHz, 47 ms) **or** one chime (237 Hz) **or** one bell (1.79 kHz) — pick one and reuse it | pop −13 / chime −4 | 30–60 ms before the word |
| title / headline | 12–14 kHz glass ding + short whoosh + tick | ding −16, tick −16 | +50 ms |
| type-on (letters) | **one** noise riser 600–900 ms with one HF tick per letter inside it — never a click per key | riser −8…−6 | riser from the first letter to the last |
| typing in a field | loud sub thud on the first key, click + thud on keys 2–3, then silence | −5 / −12 | on the keystroke |
| progress bar | 12–16 tonal ticks 50 ms apart rising 2 → 12 kHz, then a completion sound | ladder −11, completion −19 | completion +100…+250 ms after the last tick |
| success / check | sub boom + 330 ms riser + falling HF whoosh with a 1 s tail | boom −24, riser −16, whoosh −16 | boom −140 ms, whoosh +200 ms after the tilt peak |
| outro tagline | drop the SFX layer 15–20 dB, clicks −24…−35, then air only | | click on the word |

**Bed — pick one and commit:** (a) **no bed**: SFX over true digital silence, each tail is the bed (Drive, 44 % silence); (b) **music-led**: one continuous track (ChatGPT 88.4 BPM), the first UI action is the drop, UI beats sit on the kick grid (cuts ≤ +100 ms after a kick), swells end on downbeats, SFX only as filter sweeps inside the music, ~8 dB sidechain pump, no UI clicks; (c) **intro swell then air**: 2 s pad swell, dry SFX over a −46 dBFS air floor, a 20 dB breakdown for the tagline/logo (Spotify). Density: 4.6–6.7 sound objects/s when SFX carry the reel, ~0.8 genuine SFX/s when music carries it; the busiest seconds are the quiet builds. Stereo: risers/impacts wide, clicks mono, pan one accent toward its element (±5 dB). Master −14 to −16 LUFS, peaks −1 dBTP (ref09's +1.7 dBTP is clipped — don't copy).
**With a voice-over** (product reviews): use recipe (b) or a quiet (c), keep hits 8–13 dB over the bed but under the voice, and keep ticks at −25…−35 so they never mask a word.

## 6. How to build one with our kit
Use `edited videos by claude/2. Mr Unbox iPhone 18 Pro/code/` (HTML + GSAP, puppeteer render with `--sub 4` motion blur, `mix2.py` for SFX/bed). Build the UI as real DOM/SVG (cards, pills, inputs), morph with GSAP (`width/height/borderRadius` tweens + `rotationY`), type-on with a per-letter span stagger (tracking from 0.3 em → 0, colour accent → white), glow bloom = a radial-gradient div scaled up behind the element, streaks = the supersampled render (or a directional `filter: blur()` for 3–4 frames). Cursor = an SVG hand with a 3-frame blurred trail. Keep a cue for every event (`sfx()`), and render the whole thing as one timeline with no cuts.

## 6b. Two more formats *(refs 62–63, 2026-10-06 — Deepak: "high demand in the market, I want this type")*
**Motion-designer showreel (ref 62, 15 s, 16:9, dark, 0 cuts, music-led at ~120 BPM):**
- Numbered **chapters, one technique each, 1.2–2.2 s**: countdown → kinetic type → dot/pill grid → particle sphere that assembles a word → iridescent 3D blobs over a giant word → dashboard demo → orbit-path wordmark → outro. Joined by morphs; the only hard cuts are a **6-word slam run at 3 frames per word** on the beat, every word a different texture (stripes, rings, halftone, serif).
- **Persistent HUD frame**: mono-caps corner captions (project / chapter name + number / 1920×1080 60 FPS / timecode) with thin rules. This alone makes a loop read as a designed reel.
- **4-colour kit, one per chapter** (orange, lime, violet, cream on black); the dashboard is the only scene with three accents at once. Display = extended heavy grotesk; countdown digits and "with intent." / "precise." in a **serif italic**; "Form." in script.
- **Letter → object morphs**: an O becomes a disc, the disc a grid, dots become squares/diamonds/pills, pills scatter into particles, particles become type. Wordmark **type-on with glyph scramble** over a ruler rule that then becomes the frame colour.
- **Dashboard moment in 2.2 s**: four cards in four colours pop in staggered (~0.15 s), counter 0 → +248 %, ring 0 → 99 %, toggle flips, line chart rises, then the cursor **drags the cards off**.
- Audio: every scene change and slam on the 0.5 s kick, 72 % of energy below 150 Hz, no UI ticks; −14 LUFS.
**SFX-pack / product promo (ref 63, 15 s, 9:16, white, 0 cuts, SFX-led, no music):**
- **Word-ladder script**: the sentence arrives one word or pair at a time, each word blue (accent) then black, tracking collapses as it lands; readable with sound off. Every noun gets a lookalike UI object: clock icon riding a drawn arc, Google search bar with **letter-by-letter typing and a hand cursor**, a Drive-style file list (name + MB) with the hover highlight walking down the rows, **drag-and-drop** of a file onto a phone card, a **pixel-bloom "processing" wash**, a Google app card.
- Exits: a word or set **scales to a point** (with dashed vertical guides) or the whole UI pushes out to a corner; the reel ends on a black wipe from a corner.
- One Apple-style grotesk, sentence case, one blue; brand wordmarks are the only multicolour elements. Phone-shaped cards ≈ 36 % width with soft shadows.
- Audio: 2.6 soft pops/s on UI events, nothing above 4 kHz, 9 % silence, thud on the search button and the drop; −14 LUFS. Proof that a **muffled low pop kit** works as well as the glassy one.
**Use for Deepak:** the showreel grammar for a channel/brand trailer or a "what I can build" reel; the promo grammar for any tool/pack/course sell (his AI-tools and SFX topics), reusing the word-ladder + lookalike-UI storytelling with one accent colour.

## 6c. "Professional SaaS motion" Short: problem → product → result → CTA *(ref 69, 2026-10-09)*
Deepak: *"this reference is professional SAAS motion; understand the pacing, visuals, SFX, texts, fonts, colour themes, analyse every frame, speed, motion graphics."* Source: a 14.54 s, 1080×1920, 60 fps YouTube Short. Every frame read at 10 fps, the six transitions at 30–60 fps, plus loudness, band onsets, luma/saturation and palette numbers. SEEN = measured on frames; INFERRED = fonts and sound types (stems were not separated).

**Format (SEEN):** a white page, two rounded 880×482 panels stacked in the middle with a big soft shadow, a lowercase heavy-black grotesk label above each (`wireframe`, `final`). The top panel plays the same animation stripped to a After-Effects-style view: light-grey `#F7F7F7`, green grid, dotted anchor points, red/blue keyframe handles, centre guide line. Both play in lockstep. This is a **"how it is built" showcase format** (portfolio, client proof, "how I animate" Shorts); the scene inside is an ordinary 16:9 SaaS animation, so build the scene once and render a stripped wireframe pass beside it.

**Beat table (SEEN: 6 scenes of 2.7 / 2.4 / 3.8 / 1.4 / 2.5 / 1.7 s, two hard cuts, one visual event every 0.5–1.4 s; "low onset" = 40–300 Hz band onset in the audio):**
| t (s) | What happens | Motion | Audio |
|---|---|---|---|
| 0.0–0.4 | "So" on a near-white card | deblur + fade in 0.4 s | none |
| 0.6–1.4 | sentence builds "You want / a / clean motion / ad" | one word or pair at a time, each deblurs in ≈ 0.2 s, the whole line scales down to stay centred in the card | low onsets 0.62, 1.14, 1.51 |
| 1.8–2.6 | "For your **product**" (second word heavier) holds 0.6 s | fades and shrinks out 2.5–2.7 | |
| **2.70** | **hard cut: one pure-white frame**, then a globe | | low onset 2.83 (+130 ms late) |
| 2.75–3.6 | "But" deblurs 2.75, small stacked "can't find / right person" 3.2–3.6 left of a slowly drifting globe | blur-in per line | 2.83, 3.0, 3.15, 3.35, 3.6 |
| 3.6–4.4 | four avatar pins pop on Europe ≈ 0.15 s apart, then hold to 5.0 | pop | 3.6, 3.82, 4.18 |
| 5.07–5.50 | two navy liquid lobes sweep in from top-right and bottom-left and **meet as a 4-point white star** | 13 frames | low 5.39 (−60 ms before the star completes) |
| 5.5–5.8 | star holds, shrinks and spins ≈ 90° | 0.25 s | |
| 5.8–6.3 | "Yonomi" wordmark deblurs in; the star slides onto the Y and settles as the logo mark to its left | | low 6.22 (0 ms) |
| 6.3–8.8 | logo lockup holds 2.5 s: star mark idles in 3D (× ↔ ✦ silhouette about every 0.4 s), a bright horizon arc glows along the bottom | the quietest stretch | music only |
| 8.83–9.0 | a light band wipes down from the top; bg → white | 0.17 s | low 8.86 (0 ms) |
| 9.0–9.4 | a full-width saturated-blue band with a spinner arc; "Sell" + "USD 209.99$" slide in above, "Mastercard ....1234" row joins; the band shrinks into a button | morph | |
| 9.6–9.8 | spinner closes to a ring → **green glow check** → white check | 0.15 s | |
| 9.8–10.25 | hold on the check 0.45 s | | |
| 10.25–10.33 | **power-down**: the white card dims to near-black in 5 frames with one white streak | 0.08 s | hi/air onsets 10.42 and 10.56 (−24 dBFS, the loudest highs in the Short) |
| 10.35–10.48 | "306.53 $" **types on in 8 frames at 60 fps** (3 → 30 → 306 → 306.5 → 306.53 → $); "Total Money" fades in above it | 0.13 s | |
| 10.4–12.7 | dark scene: a neon comet (blue, green, white, purple, red, yellow) crosses every 0.2–0.35 s; **a digit glows in the comet's colour as it passes**; big white blooms at 10.9 and 11.5 | curved arcs, 0.3–0.5 s each | sub onsets 10.97, 11.25 (−12.9 dBFS), 11.56 (+60–70 ms) |
| 12.6–12.7 | the whole frame smears horizontally for 1–2 frames with a yellow comet at the right edge | blur-out | low 12.71 (−90 ms) |
| **12.80** | **hard cut** to the blue gradient; a white comet loops in from the left (0.3 s) and becomes the outline of a glass pill | | sub −36 dBFS at 12.98 |
| 13.1–13.4 | pill narrows and blurs, "send me your message" appears at 13.2, its arrow grows › → ▶ by 13.4 | 0.2 s | hi/air 13.26 (+24 dB flux), low 13.27 (+70 ms) |
| 13.4–14.54 | CTA holds 1.15 s, only a faint sheen on the pill | | music falls ≈ 10 dB under it (1 s RMS −12.7 → −17.2 → −22.4) |

**New patterns (not in §1–6b):**
1. **Text before product.** The first 2.7 s is only a pain sentence; the product shows at 5.5 s. The arc is pain → "can't find the right X" → brand reveal → one feature beat → the result as a number → CTA.
2. **Word-append sentence with auto-fit**: one word at a time, each deblurring in, the line shrinking to stay centred; weight contrast on the key word ("**product**").
3. **Shape = transition = logo.** Two liquid lobes meet to make the 4-point star, which shrinks, spins and becomes the logo mark: the wipe, the brand reveal and the icon are one object.
4. **Idle on the hold.** The 2.5 s logo hold is never static: the mark spins in 3D and a bottom horizon arc glows.
5. **Band → button → spinner → check.** A full-width brand-blue band wipes in, shrinks to the button, the spinner becomes a green-glow check (success = green, the only second hue in the UI).
6. **Power-down cut.** 5-frame dim to near-black with a streak; the number types on during the dim.
7. **Result number types on in 0.13 s**, then a label fades in. **Comets glow the digit they cross** in their own colour.
8. **Blur-out then hard cut** (2 frames of horizontal smear), and the next scene's first move is a comet that draws the CTA pill outline.
9. **Glass CTA pill**: ≈ 25 % white fill, thin white rim, lowercase label, arrow that grows in. Held 1.15 s, the quietest frame of the Short.
10. **Theme rhythm** (luma 231 → 178 → 203 → 143–151 → 182; saturation 0.01 → 0.30 → 0.17 → 0.38 → 0.28): white card → sky-blue globe → navy hero gradient (logo) → white UI → near-black result → the **same navy gradient again** for the CTA (bookend).
11. **Hard cuts are allowed when hidden**: one white frame (2.70) or a 1–2 frame blur-out (12.7). Both fall at a change of theme, never mid-scene. (§1 "zero cuts" still holds for single-scene reels.)

**Palette (measured on the final panel):** story card `#F7F7F7` (neutral, not tinted) with thin indigo-slate text ≈ `#6574B7`; globe scene sky `#A9D6F6 → #E8F8FE` with globe `#5492DC`; **hero gradient** diagonal, top-left navy `#0B1794`, mid `#2A4DB0 / #4B7BCE`, bottom-right sky `#8DC5EE` (highlights `#B8D9F7`); **action blue** `#0001E9` (≈ pure `#0000E8`, saturation ≈ 100 %) with white text on `#F7F7F7`; result scene `#010118` with a `#020241` glow low-right and white `#F5F6FA` type; comet colours blue / green / white / purple / red / yellow, each with a white core and a coloured glow; success green only on the check. One hue family (blue) for the brand; the dark scene is the only place with six hues.
**Type (INFERRED):** story text and wordmark in a light humanist sans (Segoe UI / Open Sans-like), sentence case, centred; UI text and numbers ("Sell", "USD 209.99$", "Total Money 306.53 $") in a bold neo-grotesk (Inter / SF Pro-like); CTA lowercase medium weight. Sizes in the 880 px panel: story and UI text 4–6 % of panel height, hero number ≈ 9 %. At a 1920×1080 stage that is ≥ 40 px, well above Deepak's 24 px floor (`mistakes-to-avoid` C7).
**Audio (measured; music-led, recipe (b) of §5):** integrated −11.4 LUFS (louder than our −14…−16), loudness range 1.8 LU (flat, compressed), true peak **+0.7 dBTP: clipped, don't copy**. 81 % of the energy is below 500 Hz (30 % below 150 Hz), 3.5 % at 2–6 kHz, **0.6 % above 6 kHz**: there are no glassy UI ticks, no clicks, no riser layer. Almost no digital silence (0.4 % of frames under −50 dBFS). The spectrogram shows one continuous pitched, gliding lead (150–800 Hz contours repeating about every 0.5 s) over a sub bed, which looks like a trending music track with a vocal-like lead rather than designed SFX (INFERRED). Low-band tempo autocorrelation peaks at ≈ 72 BPM (0.83 s), but the visuals are not on a bar grid: they sit on low-band onsets within ±100 ms (see the table), except the first hard cut, which is 130 ms ahead of its hit. Lesson: with a loud music-led bed, the picture moves on the track's hits and the track itself ducks ≈ 10 dB for the CTA; no per-event SFX are needed.
**How to use it for Deepak:** a client SaaS / AI-tool Short or a "how I animate this" showcase. Keep the arc and the pacing (scene lengths 1.4–3.8 s, brand hold ≈ 2.5 s, result number held ≈ 2.5 s, CTA ≈ 1.2 s), use **one** hero gradient for the opening logo and the CTA, one neon moment only on the result scene, and pick a new accent hue per video (`fonts-and-colours`). Pure-motion piece, so none of the footage rules apply; if any of it is laid over his footage, the one-element-at-a-time rule (`mistakes-to-avoid` B2) wins.

## 6d. Smooth-animation study: five UI/UX promo clips *(refs 70–74, 2026-10-09)*
Deepak: *"5 UI/UX motion references, understand the visuals, motion, sound effects, mostly focus on smooth animations."* The Klickpin file names (makeup, boho decor, wedding colours, debate ideas, air-fryer recipes) are Pinterest pin titles and have nothing to do with the videos. Every clip was read at 2 and 10 fps (60 fps source, so 10 fps sheets of each move), and seven moves were tracked frame by frame at 60 fps to classify the easing from numbers. SEEN = measured or read on frames; INFERRED = sound types and why the audio is the way it is.

| Ref | What it really is (SEEN) | Format | Cuts |
|---|---|---|---|
| 70 | After Effects tutorial, "Spotify Glass Folder Effect": 0–6 s finished piece (green glass folder, album cards fan out, glass cursor arrow, title), 6 s "using After Effects", 9–85 s screen recording of the build, 85–88 s the finished loop again | 9:16, 88 s, 30 fps | 15 (screen-recording jumps) |
| 71 | Freelance video-editor promo for "Yonomi": purple text scene → white kinetic text → black phone UI → navy card conveyor → white question → dark orbit logo | 16:9, 16.8 s, 60 fps | 4, at 4.02 / 9.25 / 13.78 / 15.02, each on a theme change |
| 72 | App promo: avatar bubbles → halo ring → phone with a notification pill tumbling in 3D → ring of phones → white bloom → gear logo on black | 16:9, 15.1 s, 60 fps | **0** (one continuous 3D camera) |
| 73 | Apple-Wallet concept: Wallet icon → Face ID scan → pass stack rises ($120,000 bar, black card) → tilted world-map card with a Germany → Vietnam route; the 5 s sequence plays twice | 1:1, 10.35 s, 60 fps | 0 (loop restart at 5.15) |
| 74 | Website promo for "Teamsonic.org": cursor → dock rises → Chrome icon → circle wipe → blue world with loader ring → "Team" pill → laptop with scrolling pages → yellow wipe with green zigzag line → logo on black | 16:9, 17.2 s, 60 fps | 1 (16.37, to the logo) |

**Measured easing (60 fps; t50 / t90 = share of the move's time at which 50 % / 90 % of the distance is done; linear is .50 / .90):**
| Move | Duration | Curve | Numbers |
|---|---|---|---|
| 74 dock rises from the bottom edge (centre y 0.92 → 0.50 of frame height) | 0.50 s (30 frames) | very strong ease-out (≈ out-quart) | t50 **.17**, t90 .83: half the travel in the first 0.09 s, then a 0.4 s glide |
| 74 green circle wipe (green area 0 → 91 % of frame) | 0.22 s (13 frames) | ease-out (≈ out-quad), 2.6 % overshoot | t50 .31, t90 .77 |
| 71 card slides in from the right (right edge 0.99 → 0.78) | 0.57 s (34 frames) | ease-out with a long soft tail | t50 .32, t90 **.82** |
| 71 pill → card morph (height 0.21 → 0.66) | rises in 0.15 s (9 frames) to 0.75, settles by ≈ 0.3 s | under-damped spring | **21 % overshoot, once** |
| 72 full-frame white → black fade | 0.55 s (33 frames) | ease-in-out, late-weighted | t10 .18, t50 .61, t90 .88 |
| 72 halo ring grows behind the phone (width 0.19 → past the frame edge) | 0.20 s | nearly linear, ends off-frame | steps of 0.10–0.17 per frame |
**Read as rules:** (1) **no move is linear**: every entrance is an ease-out whose last 10 % takes 17–23 % of the time (a long soft tail), only full-frame fades are ease-in-out; (2) **overshoot only on a small → big morph** (≈ 20 %, once, back in 0.3 s), slides and wipes stay under 3 %; (3) a **duration ladder**: 0.15–0.22 s for snaps (morph, wipe, halo), 0.5–0.6 s for travel (rise, slide, fade through black), 1–1.2 s hold before the next beat (ref 71's "Idea" card holds 1.1 s); (4) the quick moves are the ones with blur and bloom, the long moves are clean.

**Smooth-animation patterns (SEEN on the 10 fps sheets):**
1. **One object carries the story (morph chain).** 71: dot → ring with arrow → pill "Video Editor" → tall white card (overshoots) → star grows inside → cursor presses "Hire" → card tilts in 3D, 0–4 s with no cut. 73: Wallet icon → Face ID brackets → card stack → map card. 74: Chrome icon → circle wipe → loader ring → "Team" pill → "Teamsonic.org" pill → laptop. Plan the object chain first, then the scenes.
2. **Conveyor, never an empty frame (71, 9.8–13.4 s).** Each card enters from the right in the same move that pushes the previous one out to the left; cards hold ≈ 1 s, then the next move starts. The contents (an "Idea" badge, a comet shrinking into a star, an 82 % → 100 % counter) build while the card is held.
3. **Type is part of the motion.** Letters blur in one by one ("can you really", 0–0.5 s), then the whole line scales down and collapses to a dot that becomes the button (0.5–0.7 s); the next phrase pushes the previous one off-frame with a horizontal smear ("Well Yeah" → "You just did", 71, 4–6 s); a pill reveals its label left to right.
4. **Depth cues instead of effects:** 3D tilt on cards and phones, the far edge of a tilted map card defocused (73), a rim-light glow on the phone edge (72), a soft shadow that grows when an object lifts, stacked cards in three offset colours (73).
5. **Circle wipe from the thing you clicked (74):** the green circle grows out of the Chrome icon in 0.22 s, concentric rings pulse behind the logo, and the logo then zooms past the frame edge into the next colour. A **halo ring** behind a new object (72) does the same job as the glow bloom of §2.4.
6. **One continuous camera can replace cuts (72):** the phone tumbles, the camera pulls back to a turntable ring of phones, and a white bloom hides the scene change at 12 s; 0 cuts in 15 s. **Hard cuts only at a theme change (71):** all four land on a luma jump (≈ 90 → 222 at 4.02, 175 → 103 at 9.25) and the new scene opens with a motion in its first 0.2 s.
7. **Loop by design (73):** the sequence repeats with different data (a different route) so the clip is watchable on loop; 70 ends on the opening frame.
8. **Guide lines as accent (74):** green and yellow line segments draw along the laptop frame and then a green zigzag crosses the yellow wipe, so the colour change reads as drawn, not cut.
9. **Cursor reacts to the click (71, 74):** the card tilts, the icon pops, the ring ripples within 3 frames of the press.
10. **Colour per scene, one accent each:** 71 purple → white/black text → navy, 74 white → green → blue → yellow → black, 73 white with grey glass and one blue; the scenes are separated by theme, so cuts are free.

**Tutorial (ref 70) — what the screen recording shows (SEEN):** the glass folder is two layers (Front, Back) with **CC Light Sweep** (centre 256, 128; direction −30°; shape Smooth; width 284; sweep intensity 10; edge intensity 47; edge thickness 3.9; light colour green; light reception Cutout), moved by null layers (Front null, Back null, "all control") with 3D rotation, and the album cards are parented inside so they fan out when the folder opens. In CapCut there is no equivalent, so the transferable idea is the structure: a glass body, a moving light edge, a controller object, and cards that emerge from it. Not tested.

**Audio (measured; INFERRED sound types):**
| Ref | Loudness | Spectrum | Character |
|---|---|---|---|
| 71 | −13.7 LUFS, LRA 1.5, peak −0.8 dBFS | 31 % < 150 Hz, 50 % 150–500, 14 % 0.5–2 k, 4 % 2–6 k, 0.4 % > 6 k | music-led and flat (1 s RMS −14…−17 dBFS), only 1 % silent; the second before the white cut at 4.0 s drops to −33 dBFS and the beat returns on the cut |
| 72 | −24.0 LUFS, LRA 5.7, peak −7.1 | 40 % < 150 Hz, 44 % 150–500, 16 % mid, 0.7 % 2–6 k, nothing above | quiet low thumps and swells, 23 % of frames silent, 1 s RMS −24…−48; the gear-logo hold is ≈ 2 s of near-silence (−43, −60 dBFS) |
| 73 | −28.8 LUFS, LRA 1.1, peak −19 | 67 % < 150 Hz | one flat low bed (every second −29…−30 dBFS), no discrete hits; the motion is silent-smooth |
| 74 | essentially silent: 99.8 % of frames under −50 dBFS | one HF tick near 1.1 s (79 % of its energy above 6 kHz) | the picture carries all the rhythm; the audio was probably stripped from the repost |
| 70 | −20.6 LUFS | 60 % < 150 Hz, 19 % mid, 7 % above 2 k | low-band hits every 0.17–0.2 s during the finished piece, sparse in the tutorial |
**No SFX kit to copy from these five** (levels range −13.7 to −30 LUFS, 74 is silent): §5 stays the recipe. What they confirm: keep the low end heavy and the top clean, duck the bed for ≈ 1 s into a hard cut and re-enter on the cut (71), and end on ≈ 2 s of near-silence under the logo (72).

**How to use it for Deepak:** any UI / product / app promo or a "how it works" feature beat. Define the **object chain** and the easing set up front (ease-out with a long tail for moves, ≈ 0.2 s snaps, one 20 % overshoot on the biggest morph, ease-in-out only on fades), keep one accent per scene, hide any hard cut on a theme change. Fonts: from his list only (`fonts-and-colours`). On his **talking-head footage** the footage rules win: one graphic at a time (`mistakes-to-avoid` B2), no tilted cards (D10) and no phone mock-up with his footage (D8); 3D tilts, turntables and full-frame colour scenes belong to full-screen promo/product scenes only.

## 7. Checklist
☐ no linear moves: enters ease-out with a long tail, only fades ease-in-out, overshoot ≤ 3 % except one 20 % on a small → big morph (§6d) ☐ 0 hard cuts (ref 69 allows 2, each hidden by a white frame or a 1–2 frame blur-out at a theme change) ☐ every move has blur ☐ one overshoot max ☐ bloom on every landing ☐ hover before click ☐ holds 0.5–1.3 s ☐ type-on with tracking collapse ☐ one brand colour ☐ logo bookends ☐ riser → landing hit → settle tick on every screen change ☐ one pop/chime sample reused, ticks quiet (−25…−35), hits loud (−5…−7) ☐ one bed strategy (none / music-led on the kick grid / swell then air) ☐ master −14…−16 LUFS, −1 dBTP

## 8. On a talking-head product review (IKKO MindOne, 2026-09-30)
The grammar transfers when every UI object explains one spoken fact and sits on or beside the real product:
- **Tracked selection boxes** (Figma-style: 2.5–3 px accent stroke, white corner handles, mono tag) turn a size claim into a visual comparison (phone box vs dashed palm box).
- **Dimension line corner to corner on the screen** for a display size; **spec pills** on each number word.
- **AF viewfinder brackets** for "this camera"; **segmented toggle** for a two-state feature (Back → Front), which then morphs into the benefit pill.
- **Heads-up notification** from the top edge for connectivity or system features, growing extra rows instead of adding new cards.
- **Comment box → follow chip** with the cursor as actor for the CTA.
- Use the **product's own screen colour** as the one accent; keep his face clean on the opinion lines ("but the coolest part", "I honestly didn't expect").
- Levels with a voice: bed 16–25 dB under speech RMS by section, UI cue gains −20 to −10 dBFS, one success sound with a tail.
Full build notes: `client-video-editing-process` §10.

## 9. Premium SaaS news show on a talking head *(AI Tech News ep 02, 2026-10-15; refs 80–81)*
- **World:** midnight navy gradient (#071233 → #040918) with an electric-blue top bloom and a floor glow (Somrat's Google-AI segment); a faint 80 px grid only on chapter cards; glass cards (navy fill, 1 px light rim, inner top highlight, big soft shadow); white "ice" cards for documents and evidence; one accent #2F6BFF / #5A8BFF; red and green only inside data; yellow only as the article marker.
- **Type:** Outfit 600–700 for titles and numbers + Inter 500–600 for UI and chips; letter type-on with tracking collapse for names; word-by-word blur-in for lines; the accent word in light blue.
- **Devices that carried 16 minutes:**
  - a search pill typing "Artificial Intelligence", then "Artificial" selected and replaced by "Super" (the hook);
  - a document card with a hand-drawn signature and a "Signed" chip;
  - 12 agency tiles flipping AI → SI in a diagonal wave;
  - a glass profile grid ticking ✓ in a wave;
  - a pill → card morph (the one ≈ 25 % overshoot);
  - a countdown ring; a node trace (sources → model → MATCH → Fired);
  - a toggle switching live internet off;
  - a code window where the bug row turns red, then the patched row green;
  - bar boards: the vendor chart first, then the independent index with rank badges;
  - race lanes, a poll card with a cursor, a satellite globe (pins only, no country map);
  - the keyed subscribe card; the chapter key row (Tharun's counter, active key lights blue with a bloom).
- **Rule learned:** a full-screen scene needs a visible change at least every ≈ 5 s while he talks (a counter, a chip, a highlight). Slow drifts and small colour changes do not read as change, and `freezedetect` flags them.

## 10. Rebuilding a 3D product explainer without Blender *(video 15 Mini LED Backlight, 2026-10-16)*
- **Brief:** copy a reference 3D explainer shot for shot, with no text (Mini-LED backlight: macro LED dolly → dot field pulling back into a backlight panel → the LCD layer slides out in front → airplane backlight with a blue edge glow, the LCD slides in, orbit → slice glitch → push-in on an angled LED wall).
- **Kit:** `edited videos by claude/15. Mini LED Backlight/code/render.py`. It uses numpy + PIL + scipy only (no OpenCV or Blender on this Mac). The pieces:
  - a pinhole `Cam`;
  - `homog`/`warp` (PIL `PERSPECTIVE`, with the texture pre-shrunk to its on-screen size so LED grids don't alias);
  - `draw_panel` (front face, side and top edge for thickness, a mirrored floor reflection that fades out, an optional blurred edge glow);
  - `draw_leds` (dome sprites resized per LED and squashed by the view angle);
  - bloom, a soft highlight knee, vignette and grain.
  Each 1080×1920 frame takes about 1–2.5 s, spread over 12 worker processes.
- **Shapes:** the Zapf Dingbats ✈ glyph (rotated 28°) and the Apple emoji 🐬 alpha give clean silhouettes. `distance_transform_edt` on the mask turns a silhouette into a lit 1–2-LED outline.
- **Moves that sell it:** one continuous camera from a grazing dot field to a frontal view to the reveal (no cut); all LEDs on, then dimming to just the outline (local dimming); the LCD sliding out along the panel normal; an exploded 3/4 view; the LED-wall camera set off the wall's normal (about 35°) so the far side recedes.
- **Gotcha:** the imageio ffmpeg is an Intel build running under Rosetta, so libx264 caps the pipe at about 1 fps. Encode with `h264_videotoolbox -b:v 45M` instead.

