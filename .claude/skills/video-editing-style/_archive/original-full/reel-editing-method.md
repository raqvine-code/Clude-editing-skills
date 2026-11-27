---
name: reel-editing-method
description: The complete editing methodology learned from Deepak's first full motion-graphics edit (AI vs AGI vs ASI talking-head reel, 68s, 9:16). Covers philosophy, structure, pacing, typography, motion graphics, effects, B-roll, music, sound design, colour, transitions, decision rules, the HTML/GSAP render pipeline, what worked, what didn't, and a QC checklist. Load whenever editing a talking-head video into a high-engagement reel, adding motion graphics/captions/HUD elements, or when asked "edit it like the AI-AGI-ASI video".
---

# First Video Edit — Draft 1 (AI vs AGI vs ASI)

> **Note (2026-10-06):** `experiment/` paths in this skill are historical — that folder was cleared. Final videos + edit notes: `Raghu and claude/edited videos by claude/`. Reusable code: the `code/` folder inside each video folder. Reference analyses were folded into the skills and deleted.

Everything below comes from one real project: turning Deepak's plain Telugu talking-head (`/Users/raghusai/Movies/CapCut/for claude.mp4`, 68.3s, 1440x2560, 60fps, CapCut keyframes already applied) into `experiment/talking_head/deliver/AI_AGI_ASI_MG_edit_upload.mp4`.

Tags used in this file:
- **[USED]** — actually done in this edit.
- **[REC]** — a recommendation derived from the project, not yet tested on a second video.

Related skills: `my-editing-rules` (Deepak's rules always win), `motion-graphics-style` (the reference look), `broll-library`, `png-library`, `where-to-find-assets`.

Source of truth for exact timings: `edited videos by claude/1. AI vs AGI vs ASI/code/comp.js`. Beat table: `edited videos by claude/1. AI vs AGI vs ASI/EDIT_BREAKDOWN.md`.

---

## 1. Editing philosophy

**Creative direction [USED]:** one visual system that carries the whole video instead of a pile of unrelated effects. Here the system was a **danger meter**: three levels, three colours, one gauge that climbs, one countdown that runs out.

**Intended viewer experience [USED]:**
1. Second 0: a slam that stops the scroll (giant AI / AGI / ASI behind the head).
2. A visible promise ("explained in 1:00") so viewers know it's short and worth finishing.
3. Something new on screen every 2–4 s so the eye never rests.
4. A tension curve that rises to the ASI section and pays off with a question as the timer hits 0:00.
5. A frictionless CTA (comment box, follow card) in the last 5 s.

**What made it feel professional [USED]:**
- Consistent design tokens: 3 accent colours, one display font family (Montserrat 500–900), one mono font (JetBrains Mono) for HUD labels, one handwritten font (Caveat) for annotations, one glass-card style everywhere.
- Depth: text placed *behind* the speaker using a person mask, not only on top.
- UI mock-ups that look like the real apps (ChatGPT chat, Instagram comment box and follow card, macOS-style cursor).
- Every graphic has a sound; every transition has a whoosh or hit; nothing appears silently.
- Word-level sync: text lands on the exact word from a word-timestamped transcript, not "roughly there".
- No preset transitions: only blur, whip with motion blur, glitch, flash, hazard-tape wipe.

**Guiding principles [USED]:**
- Talking head is the base layer; graphics support the speaker, never hide the face while he is making a point.
- One keyword = one object/graphic. Don't stack three ideas into one card.
- Use the speaker's own words as the on-screen text (translated), not paraphrased marketing copy.
- Keep the speaker's footage untouched (no added keyframes, per Deepak's rule).
- Design for 9:16 phone viewing: big type, safe margins, nothing important in the bottom 15% (UI overlays) or top 8% (status bar).

---

## 2. Video structure

**Shape used [USED]** (68 s):

| Section | Time | Job | Intensity |
|---|---|---|---|
| Hook | 0–5.5 | Slam the three words, ask "do you know?", promise 1 minute | ★★★★★ |
| Definitions | 5.5–12.4 | Calm glass card, 3 rows build word-by-word | ★★ |
| Danger-meter intro | 12.4–14.6 | Full-screen takeover, gauge revs, shrinks into HUD | ★★★★ |
| Level 1 AI | 14.6–24.9 | ChatGPT UI story in 3 phases | ★★ → ★★★ |
| Level 2 AGI | 24.9–45 | Glitch, header, bars, paper "thinks/reasons" beat, stamp, example card | ★★★ |
| Level 3 ASI | 45–58 | Red flash, movie card, chips multiply, chart blows out | ★★★★★ |
| Blackout question | 58–63 | Lights off, spotlight, ticker, giant "?", timer hits 0 | ★★★★ (quiet but tense) |
| CTA | 63–68.3 | Light-leak reset, comment box, follow card, thank-you | ★★ |

**Hook strategy [USED]:**
- The first three spoken words are the three biggest graphics in the video (440 px / 400 px type behind the head), each with an impact SFX and a 0.2 s shake.
- Background is swapped to a dark grid studio for the hook only, so the hook looks different from the rest.
- A question caption ("Do you know the REAL DEFINITIONS?") immediately after the slam.
- The promise is made concrete and visible: a big 1:00 that flies into the corner and starts counting.

**Pacing strategy [USED]:**
- A new visual event at least every 2–4 s; micro-events (a word, a tick, a chip) every 0.25–0.8 s inside a card.
- Cards live 2–10 s. Anything over ~4 s must keep changing internally (phases, rows, counters).
- Breathers: text-only or empty-room beats after heavy cards (e.g. 26.95–28 "Now let's talk about AGI").

**Section transitions [USED]:** each level change gets a signature: AI = whoosh + card; AGI = RGB glitch + amber header; ASI = red flash + heavy glitch + alarm + red header. The viewer learns "big change" from the sound alone.

**Intensity control [USED]:** tension is built with a 2 s riser and a red vignette *before* the ASI cut (43.5–45 s), then released with a flash. The final question drops the music entirely; silence plus a drone reads as "important".

**Attention maintenance [USED]:** the countdown timer (top-right) and the danger gauge (top-left) are persistent and change state at every level, giving the viewer two reasons to keep watching.

---

## 3. Timeline and pacing rules

- **Cuts and jump cuts [USED]:** the speaker's jump cuts were found from the audio (micro-silences of 60–150 ms) and used as the boundaries for cards. Never place a card entry across a jump cut; enter just before or just after.
- **Speech-driven timing [USED]:** every element is timed to a word timestamp (faster-whisper large-v3, per-jump-cut chunks). Enter ~0.05–0.1 s *before* the word so it feels anticipatory; exit on the next jump cut or when the next card needs the space.
- **Pauses and silence [USED]:** the only deliberate silence in the mix is 58.0–63.0 s (music cut, low drone) under "imagine that day… will humans be needed?". Rule: cut music once per video, on the single most important line.
- **Beat changes [USED]:** each level change is a hard reset (flash/glitch + new header + new gauge state + new caption colour).
- **Speed changes:** none used. The footage runs 1×. [REC] Keep it that way for talking heads; speed ramps break lip sync.
- **Punch-ins / zooms [USED — not added]:** Deepak's CapCut export already contained zoom keyframes. Rule from Deepak: **do not add keyframes to his footage**. When his zoom-out exposes a black band at the top (it did at 25.47–26.97 s and 45.03–46.87 s, ~300 px tall), cover the band with a designed header strip that starts one frame *before* the band appears.
- **Camera movement:** none added. [REC] A very slow 1–2 % push-in on static cards is acceptable; leave the speaker alone.
- **Rhythm [USED]:** big → small → big. A slam (hook) is followed by a calm card (definitions), followed by a takeover (danger meter). Never two takeovers back to back.
- **Hold times [USED]:** captions 0.6–1.5 s per phrase; big keyword slams 0.4–0.6 s each; cards 2–10 s with internal changes; end cards 3–4 s.

---

## 4. Text and typography

**When text appears [USED]:**
- Every spoken sentence that carries the argument gets a caption or a card. Filler ("in simple words…") gets a small caption or nothing.
- Brand/app names get their logo, not text (ChatGPT logo, Instagram handle card).
- Numbers and lists get their own UI (rows with badges, counters, bars).

**Hierarchy [USED]:**
- Small setup line (Montserrat 600, 46 px, 92 % opacity) above one big keyword (Montserrat 800, 70–84 px). Only the keyword needs to be read.
- Giant "behind the head" words: Montserrat 900, 178–440 px, letter-spacing −0.035 em, line-height 0.9, auto-fitted to a max width of 1000 px.
- HUD labels: JetBrains Mono, 19–30 px, letter-spacing 0.1–0.24 em, grey `#8B8D93`.
- Handwritten annotations: Caveat 700, 92–112 px, red `#D7261E`, rotated −5° to −8°.

**Positioning [USED]:**
- Captions centred, top at 1250 px (bottom third) so they sit over the chest, not the face. Moved up to 1210 px when a comment/follow card needs the bottom.
- Cards: 940 px wide, 70 px side margins, top between 1030 and 1130 px, height 470–640 px.
- Behind-the-head words: top 60–90 px, centred. Measured head top per scene from the mask (e.g. 156–350 px) to make sure the word's baseline sits above or just behind the hair.
- HUD: gauge top-left at (30, 126), timer top-right at (818, 126). Nothing else in the top 300 px except headers.

**Animation style [USED]:**
- Caption words: fade + rise 26 px + scale 0.9→1 + blur 10→0, `back.out(1.8)`, 0.17 s, one word at a time on its timestamp.
- Keyword slam: scale 1.45→1 + blur 14→0, `expo.out`, 0.26 s, followed by a 0.2 s decaying shake.
- Grey→black "light up": word arrives grey (#9A9A9A / #8a8a8a), turns to black or white 0.18 s later when spoken.
- Exit: fade + rise −12 to −20 px + blur 8–14 px, `power2.in`, 0.14–0.2 s. Exits are always faster than entries.
- Typewriter: one character per tick with a block cursor; each 2nd character gets a key-click SFX.

**Emphasis techniques [USED]:** accent colour on the key word; hand-drawn ellipse and animated strike-through (from the references, available in `motion-graphics-style`); outlined text (`-webkit-text-stroke`) for the second word of a pair (DANGER / LEVEL); a stamp box rotated −5° with a shake for a verdict ("THAT'S AGI").

**Safe areas [USED]:** keep text within x 60–1020 px and y 120–1700 px. The follow card sits at y 1180–1510 so Instagram's own UI doesn't cover it.

**Avoiding excessive text [USED]:** max one caption line + one card at a time. When a full card is up, the caption is dropped (the card *is* the text). Never more than ~6 words in a caption.

---

## 5. Motion graphics

**Inventory [USED]:**

| Graphic | Where | Why |
|---|---|---|
| Behind-the-head slam words (AI/AGI/ASI) | 0–1.6 s | Hook; shows the three subjects as objects, not captions |
| Countdown timer widget | 2.9–63 s | Promise + retention |
| Danger gauge (SVG arc, needle) | 12.5–63 s | The video's spine; state = current level |
| Full-screen "DANGER LEVEL" takeover + hazard-tape wipe | 12.4–14.6 s | Introduces the gauge with weight |
| Glass explainer cards (definitions, ChatGPT, knowledge bars, example, intelligence) | throughout | Structured info without hiding the speaker |
| ChatGPT UI (chips flying into a core, loading bar, typed prompt, streamed answer, capability rows) | 15.4–24.6 s | Turns "pre-trained data / ask anything / writes code" into a story |
| Level header strips | 25.5 s, 45 s | Section change + hides CapCut's black band |
| Paper scene with giant grey→black words + "like us!" annotation | 30.8–36 s | Reference-style editorial beat for the "human" idea |
| Stamp "THAT'S AGI" | 36.3 s | Verdict punctuation |
| Film-strip movie card (Robo 2.0) with laser-scan reveal | 47.8–51.2 s | Visualises the movie reference |
| Multiplying AI chips behind the speaker + "AI × n" counter | 51.4–54 s | "One AI builds another" made literal |
| Intelligence bar that overshoots the frame | 54.9–55.7 s | Scale of ASI vs human |
| Blackout + spotlight + ticker of solved problems | 58–61 s | Quiet, tense "imagine" beat |
| Giant red outlined "?" | 61.3–63 s | Final question |
| Light-leak flash | 63 s | Mood reset into CTA |
| Instagram comment composer (typed) and follow card with cursor click | 63.2–68 s | CTA as a real UI |

**Animation principles [USED]:**
- Enter fast with overshoot (`back.out(1.6–2.4)` or `expo.out`), exit faster with `power2.in`/`power3.in`.
- Blur is part of every entrance (16 px → 0) so elements "focus in" rather than pop.
- Objects arrive from an edge or from scale 0.2–0.5, never from nowhere.
- Persistent widgets change state with a small overshoot on the needle (`back.out(2.2)`), plus an elastic settle for the ASI hit.
- Idle motion on anything that stays >3 s: gauge needle jitter in the ASI section, timer flashes in the last 10 s, corner stars slowly rotate, chips pop in waves.

**Timing/easing/scale/position/rotation/opacity [USED]:**
- Card entrance: y 90→0, scale 0.97→1, blur 16→0, opacity 0→1, 0.32–0.36 s.
- Pop: scale 0.4–0.7→1, `back.out(2.2)`, 0.34 s.
- Slam: scale 1.3–1.8→1, 0.22–0.26 s, then shake amplitude 8–14 px decaying over 0.18–0.3 s.
- Stamp: rotation −14°→−5° while scaling 1.8→1.
- Counter/bar fills: `power1.inOut` or `power2.out`, 0.7–1.0 s; the ASI bar uses `power4.in` to "explode".
- Timer flight: scale 1→0.22 while translating to the corner, `power3.in`, 0.34 s, then the HUD widget pops in.

**Interaction with footage [USED]:** five layers, bottom to top: `base` footage → `bgrep` (replacement backgrounds: dark grid, paper, red grid, black) → `behind` (giant words, chips, question marks) → `person` (the same footage clipped by a per-frame person mask) → `front` (cards, captions) → `hud` (gauge, timer, headers) → `fx` (vignette, red pulse, flash, grain, glitch bars). Anything in `behind` shows *around* the speaker; anything in `front` sits on him. Cards use `backdrop-filter: blur(26px)` so the footage is visible but soft behind them.

---

## 6. Effects

| Effect | When to use | When NOT to use | Purpose | Strength used |
|---|---|---|---|---|
| **Blur in/out** [USED] | Every card, caption and word entrance/exit | Never leave an element half-blurred on hold | Focus-pull feel, hides pop-in | 8–16 px → 0 over 0.15–0.35 s |
| **Backdrop blur (glass)** [USED] | Info cards over the speaker | Full-screen takeovers (use solid bg) | Readability without hiding the footage | 26 px, card bg `rgba(12,13,16,.78)` |
| **Glow** [USED] | Accent-colour badges, gauge, timer digits, the ASI bar | On body text (muddies it) | Makes the accent colour feel lit | `0 0 40–60px <colour>40–66` |
| **Shake** [USED] | After a slam, stamp or impact | On captions or anything with small text; never >0.3 s | Sells weight | 8–14 px amplitude decaying over 0.18–0.3 s, seeded random |
| **Motion blur (SVG feGaussianBlur X)** [USED] | Whip-in/out of full cards | On text alone (it smears) | Fast card swaps that still read as motion | stdDeviation 60–70 → 0 over 0.18–0.24 s |
| **RGB split glitch + scan bars** [USED] | Level changes, one hard cut into ASI, exit of the movie card | More than ~3 times per minute; on calm sections | Signals "system change" | 0.14–0.22 s, dx 8–34 px, skew ±3°, amp 0.8–1.6 |
| **Flash** [USED] | Section resets, impacts | Back-to-back flashes | Hard reset of the eye | White 0.18–0.5 opacity over 0.22–0.32 s; red flash for the ASI hit |
| **Hazard-tape wipe** [USED] | Once, into the danger-meter takeover | Anywhere else in the same video (it's a signature) | Themed transition | 0.17 s in, 0.2 s out |
| **Light-leak** [USED] | Once, out of the dark question into the CTA | Mid-argument | Warm mood reset | Screen-blend radial gradients, 0.22 s in / 0.45 s out |
| **Red pulse vignette** [USED] | ASI section only | On the low/medium levels | Continuous tension | opacity 0.2 ± 0.13 at 0.9 Hz |
| **Vignette + film grain** [USED] | Always on | — | Unifies footage and graphics | Grain 0.075 opacity overlay, moves every frame; vignette 0.38 at edges |
| **Person mask compositing** [USED] | Hook, paper beat, chips beat, blackout | When the mask edge is visibly wrong (hands crossing the face) | Depth: text behind the head | MediaPipe selfie segmentation, temporal smoothing 0.65/0.35, 1.2 px feather |
| **Speed effects** | not used | — | — | — |
| **Colour effects on footage** [USED] | Global only | Per-scene grades that shift skin tone | Pop | contrast 1.06, saturate 1.07, brightness 1.02 |

Rules:
- One signature transition per section change; don't reuse the hazard tape or the light-leak twice.
- Every flash or glitch must be paired with a sound.
- Shake the *graphic*, not the whole frame, unless it's the hook.
- Never blur the speaker's face for more than the length of a transition.

---

## 7. B-roll

**What was used [USED]:** this edit is motion-graphics-led, so classic B-roll clips were *not* cut in. Assets from the local kit that were used as graphic elements:
- `png for claude/chatgpt.jpg` → converted to a white transparent logo (ChatGPT card, avatar).
- `png for claude/robo.jpg` → greyscale, multiplied on paper (Robo 2.0 card, mirrored for the second robot).
- `png for claude/tech boy deepak .jpeg` → face crop for the comment/follow avatars.

**Rules derived [REC]:**
- On a talking head with a strong graphics system, B-roll is a *fallback* for beats that have no good graphic (e.g. a real location, a real person, a product). Check `broll-library` first, professional-first rule applies.
- If B-roll is used, hold it 1.5–3 s, enter/exit with the same blur or whip language as the cards, and keep the HUD on top so the system stays continuous.
- Desaturate or tint B-roll toward the level colour so it doesn't break the palette.
- Avoid repetition: never reuse a clip or a PNG in two sections; the second appearance reads as laziness.
- B-roll must match the spoken noun literally (a robot when he says robot), the same rule as PNG pop-ups.

---

## 8. Music / BGM

**Selection [USED]:** `bgm for claude/Tech beat.mp3` (~118 BPM, flat energy, −8 dB constant). Chosen because it has no swells that fight the voice and no drops that would need beat-matching. Candidates rejected: `Smooth 1` (energy jumps of 10+ dB every 16 s), `Interstellar` (60 s silent intro), `Loop 5` (a drop at 1:52 that doesn't line up with anything).

**Criteria [REC]:**
- Constant energy or very slow swells for explainer talking heads.
- Tempo 100–125 BPM feels "tech"; slower reads as emotional.
- No vocals, no melodic hook loud enough to compete with speech.

**Enter/exit [USED]:**
- Music starts at 0.02 s (under the first impact) and ends with a fade in the last 0.6 s.
- Dip of −5 dB from 44.6 s through the ASI hit so the riser and impact are the loudest thing.
- **Full cut at 58.0 s** ("imagine that day…"), replaced by a low synth drone, back at 63.35 s under the light-leak. Rule: cut music once, on the most important line, and bring it back on the reset.

**Volume strategy [USED]:**
- Voice bus 0 dB, music bus −15 dB (measured: voice −15 LUFS, music −33 LUFS integrated ≈ 18 LU under the voice).
- Sidechain-style ducking: up to −5 dB while the voice is above −40 dB RMS, attack fast (k 0.5), release slow (k 0.06) on 10 ms frames.
- Master: peak-normalised to −1 dB, +1 dB, limiter at 0.84 → final −13.8 LUFS integrated, −1.3 dBFS peak (social-platform target ≈ −14 LUFS).

**Beat sync:** not used on this edit (graphics follow speech, not the music). [REC] Only beat-sync when the video has no VO or the music is the point.

**When music should NOT be used [USED/REC]:** under the single most important question; under a heartbeat/drone moment; when the speaker goes very quiet. Silence with a drone reads as "important".

---

## 9. Sound design

**Kit [USED]:** 29 procedurally generated placeholder sounds (`build/sfx_synth.py`, no licensing risk): whoosh (fast/med/slow/low), swipe, pop (normal/high/low), click, tick, 4 keyboard keys, impact (hard/soft), riser (2 s / 1 s), reverse swell, glitch (long/short), ding, notify, alarm, buzz, thump (heartbeat), shutter, scan, sparkle. **These must be swapped for Epidemic Sound SFX** using `deliver/sfx_cue_sheet.csv` (147 cues with time, name, gain, search term). `EPIDEMIC_API_KEY` was not set on this Mac during the edit.

**Cue rules [USED]:**
- Whoosh on every card whip/blur entrance (−4 to −10 dB); the faster the motion, the shorter the whoosh.
- Pop on every chip, badge, row or icon that appears (−5 to −13 dB). High pop for small things, low pop for large things.
- Impact on the three hook words (−1 dB, soft −3 dB for the middle one), the ASI hit (0 dB), the intelligence bar overshoot (−3 dB).
- Tick/click for UI state changes: timer docking, checkmarks, cursor click (−2 to −12 dB).
- Keyboard keys on every second character of typed text (−14 to −18 dB).
- Riser 1.5 s before a big change (43.55 s → ASI hit at 45.09 s; short riser before the bar explosion).
- Glitch under every RGB-split (−6 to −12 dB); alarm under warning icons (−13 to −16 dB).
- Scan/data sweep under bars filling and the laser reveal; ding at 100 %.
- Thump (heartbeat) ×3 under the final question, spaced to the caption words.
- Buzz when the timer hits 0:00. Sparkle when Follow turns to Following.

**Timing [USED]:** SFX starts at the graphic's first frame, not the peak of its motion; impacts may lead the visual by ~1 frame. Density: one sound every 0.4–0.8 s on average, never two whooshes within 0.25 s.

**Layering [USED]:** an impact can stack with a glitch and a flash; a whoosh never stacks with another whoosh; pops stack freely if they are ≥0.08 s apart.

**Volume hierarchy [USED]:** voice > impacts/hits > whooshes > pops/clicks > typing/ticks > drone/ambience > music. SFX bus −5 dB overall.

**Ambient [USED]:** a low synth drone (55/82/110 Hz) only during the blackout beat, 0.6 s fade in, 0.15 s out.

---

## 10. Colour / visual style

- **Palette [USED]:** ink `#0B0C0E`, charcoal `#141518`, paper `#E9E7E2`, off-white text `#F4F4F1`, grey `#8B8D93`; accents lime `#C6FF33` (AI/low), amber `#FFB020` (AGI/medium), red `#FF3B30` (ASI/extreme), Instagram blue `#0095F6` for the follow button, handwriting red `#D7261E`.
- **Footage treatment [USED]:** one global filter on the speaker (`contrast 1.06, saturate 1.07, brightness 1.02`). Skin tone was left natural; no per-scene grade. Vignette (radial, 0.38 at the edges) and moving film grain (0.075, overlay) on top of everything.
- **Contrast [USED]:** dark cards on the bright room, bright paper scene as the contrast beat, black blackout with a warm spotlight. Alternating light/dark scenes keeps the timeline from looking flat.
- **Highlights/shadows [USED]:** glass cards get an inner top highlight (`inset 0 1px 0 rgba(255,255,255,.08)`) and a 40–80 px drop shadow so they float. Text on footage always has a text shadow (`0 6px 26px rgba(0,0,0,.55)`).
- **Consistency [USED]:** level colour appears in the gauge, the header strip, the badge, the caption highlight and the card accent at the same time. Never mix two accent colours in one card unless comparing levels.
- **Mono B&W beats [USED]:** the paper and movie cards desaturate their imagery (greyscale robots, black stars, red accent only) to match the reference reels.

---

## 11. Transitions

| Transition | Used at | Rule |
|---|---|---|
| Blur out → blur in (default) [USED] | almost every card swap | Default; 0.15–0.35 s |
| Whip with horizontal motion blur [USED] | movie card in (from right) and out (to left) | For full-frame cards; direction consistent within a sequence |
| RGB glitch + scan bars [USED] | AI→AGI, AGI→ASI, movie card exit | Level changes only; ≤3 per minute |
| Flash (white/red) [USED] | after hook, into paper beat, ASI hit, chips exit, timer end | Pair with a hit; never two within 1 s |
| Hazard-tape wipe [USED] | into the danger meter | Once per video |
| Light-leak [USED] | out of the blackout | Once per video, only for a mood reset |
| Hard cut | between the speaker's own jump cuts | Preferred when the audio already cuts; don't add a transition on top |
| Fly-to-corner (element becomes a widget) [USED] | 1:00 → timer HUD; gauge → HUD | Use when a big element must persist |

Rules against unnecessary transitions: if two cards are the same style, just blur-swap; if the speaker keeps talking through a jump cut, do nothing; no zoom transitions, no spins, no preset "slide" wipes.

---

## 12. Creative decision rules

Recurring situations from this edit, written as IF → THEN rules.

- **IF the video has 2–5 named things (levels, steps, tools)** → give each a colour, a badge and a persistent widget state; make the widget the video's spine.
- **IF the speaker promises a duration ("in 1 minute")** → put a real countdown on screen and make it end on the payoff line.
- **IF the first sentence names the subject(s)** → slam them as giant words behind the head with impacts; no caption in the first 1.5 s.
- **IF he names an app/tool** → build a mock-up of that app's UI and let the explanation play out inside it, phase by phase.
- **IF he lists capabilities** → rows with icon + label + checkmark, one row per spoken item, pop + tick each.
- **IF he compares two things** → two columns or two bars; animate the difference last (the "=" or the overshoot).
- **IF he references a movie/scene** → a titled card (film-strip frame) with the object and one caption line; keep it under 4 s.
- **IF he says "like humans / like us"** → switch to the paper/editorial look and use handwriting for the aside.
- **IF the argument peaks** → riser 1.5 s before, flash + hit + glitch on the word, pulsing vignette after.
- **IF he asks the closing question** → cut the music, black background, spotlight, drone, heartbeat thumps, the biggest symbol behind him.
- **IF CapCut's keyframes leave a black band** → cover it with a header strip that starts 1 frame before the band and ends on the last band frame.
- **IF a card would cover his face** → move it to y ≥ 1030 px or split top/bottom; never over the eyes while he's talking.
- **IF the same layout appears twice** → change the background (dark grid / paper / red / black) or the card style before repeating.
- **IF a caption has more than 6 words** → split it into setup line + keyword, or drop the setup.
- **IF an element stays longer than 3 s** → give it idle motion (jitter, blink, slow rotate, counter).
- **IF a graphic appears silently** → add a pop/whoosh; if it appears with a sound that already played <0.25 s ago, drop the sound, not the graphic.
- **IF the transcript is in Telugu/Hinglish** → transcribe per jump-cut chunk with large-v3 and a domain prompt, then caption in English keywords; keep proper nouns as spoken (ChatGPT, Robo 2.0).

---

## 13. Tools and workflow

**Stack [USED]** (no Remotion; the composition is plain HTML + GSAP rendered by headless Chrome):
- Transcription: `faster-whisper` large-v3 (int8, CPU), word timestamps, `clip_timestamps` from audio micro-silences (`silencedetect n=-38dB d=0.06`), `condition_on_previous_text=False`, domain `initial_prompt`. The small model and the un-chunked large run both hallucinated ("AI, AI, AI…"); chunking fixed it.
- Person masks: `mediapipe` selfie segmentation (model 0) at 540×960, temporal blend 0.65/0.35 within a shot, reset on scene cuts, S-curve contrast, 1.2 px Gaussian feather → RGBA PNG per frame used as a CSS `mask-image`.
- Composition: `build/index.html` (styles, layers, SVG filters) + `build/comp.js` (one paused GSAP timeline, `window.__seek(t)` sets the base frame, the mask, the timeline position and per-frame state; `window.__sfx` collects cues).
- Renderer: `build/render.js` (puppeteer-core → local Chrome, one browser per worker, `Page.captureScreenshot` JPEG q94, `--times a,b,c` for key frames, `--scale 0.5` for previews via a clip scale, `--sfxout` to export cues).
- Audio: `build/sfx_synth.py` (procedural kit), `build/mix.py` (voice + cues + ducked BGM + drone → stems + premaster), ffmpeg `alimiter` for the master.
- Encode: ffmpeg `libx264 -preset slow -crf 17` master (bt709 tags, full→tv range), then a `-crf 20 -maxrate 22M` upload copy. Audio AAC 320 k / 48 kHz.
- ffmpeg binary came from the `imageio-ffmpeg` pip wheel because Homebrew ffmpeg wasn't installed; all tooling lives in a venv in the session scratchpad.

**Reusable code patterns [USED]** (in `comp.js`):
- `blurIn / blurOut / pop / slam / shake / flash / glitch / whipIn / whipOut / typeText / caption / card / header` helpers: every animation in the video is one of these with parameters.
- `textAt(el, t, text)` + `applyTexts(t)` for deterministic text swaps on seek (GSAP `set textContent` was not seek-safe).
- `fit(el, maxWidth)` measures with canvas after fonts load and shrinks giant words to fit.
- `rng(seed)` for repeatable shake/glitch randomness so re-renders match.
- Layer order and the `PERSON` time ranges decide when the mask is applied.

**Asset organisation [USED]:**
```
experiment/talking_head/
  audio16k.wav, transcript_large.json, frames/        # analysis
  build/ index.html comp.js render.js mix.py sfx_synth.py sfx/ assets/ node_modules/
  deliver/ AI_AGI_ASI_MG_edit.mp4 (master) AI_AGI_ASI_MG_edit_upload.mp4 EDIT_BREAKDOWN.md sfx_cue_sheet.csv stems/
scratchpad/ base_frames/ (1080x1920 jpg) masks/ (png) full/ (rendered) audio/
```
Naming: `ref0N_<topic>` for reference videos, `stem_<bus>.wav`, `sfx/<name>.wav`, frames `%05d`.

**Preview workflow [USED]:** render 15–30 hand-picked timestamps at half scale → contact sheet (`sheet.py`) → fix → repeat. Then full render (4 workers ≈ 18 fps at 1080×1920) → QA sheet from the *encoded* MP4 at 2 fps → pixel checks for known risks (black bands).

**Problems met and fixes [USED]:**
- Whisper looped on "AI, AI, AI" → chunk by jump cuts, disable context carry-over.
- Half-scale previews rendered only the top-left → use `clip.scale`, not `deviceScaleFactor`.
- Four tabs in one Chrome starved each other → one browser per worker.
- Instagram blue vanished on the Follow button → the `ig` colour was missing from the token object; always read the token map before using a key.
- Header started one frame after the black band → measure band frames from the source and start the cover ≥1 frame early.
- ffmpeg `drawtext` has no fonts on this Mac → draw labels with PIL instead.
- Reverb tail length mismatch in the SFX synth → pad the wet signal to the dry length.

---

## 14. What worked

- **One spine (gauge + timer)** — every section had a reason to exist inside a system; the video reads as designed, not decorated.
- **Behind-the-head text** — the single biggest "pro" signal for the cost of one segmentation pass. The hook and the "?" ending depend on it.
- **Word-timed captions from the transcript** — sync is exact, so even simple captions feel expensive.
- **App mock-ups (ChatGPT, Instagram)** — familiar UI explains faster than abstract icons and makes the CTA feel native.
- **Section signatures (glitch/flash/header + colour)** — viewers can feel the structure with eyes half-closed.
- **Music cut on the closing question** — silence + drone gave the ending weight without any extra graphics.
- **Covering CapCut's black bands with header strips** — turned a defect into a designed moment; Deepak's keyframes stayed untouched.
- **Previewing by hand-picked timestamps** — 15–30 frames caught every layout bug before a 4-minute full render.
- **Rendering the QA sheet from the final MP4**, not the frame folder — caught the one-frame band gap the frame preview missed.

## 15. What did not work / was rejected

- **First hook layout** placed the words over the face; moved above the hairline after measuring head tops from the masks.
- **"HUMANS?" as one outlined word** behind the head was unreadable behind hair → replaced with two large "?" glyphs offset left/right.
- **"like us!" annotation** first sat on the cheek → moved to the upper-right gap beside the head, scaled 0.72.
- **Robo 2.0 card** first put the title at the top edge with robots in the middle → looked like a poster, not a scene; re-stacked title at y 410–460 with robots at y 760 and caption at y 1330.
- **AI×n counter** collided with the caption → moved below the caption (y 1452).
- **Danger-level label "DANGER LEVEL"** wrapped in the HUD → shortened to "DANGER".
- **Whisper small / un-chunked large** → hallucinated loops; only chunked large-v3 with a domain prompt was usable. Budget ~15 min CPU for 68 s.
- **BGM at −22 dB** was inaudible on a phone; −15 dB bus (≈18 LU under voice) is the floor.
- **Procedural SFX** are acceptable for timing but sound thin next to licensed ones → keep the cue sheet and swap to Epidemic before publishing.
- **Not tried yet (open):** desaturating the speaker to match the B&W references (asked Deepak, no answer); real B-roll cut-ins; beat-synced cuts.

## 16. Reusable checklist

**Story** ☐ One-sentence spine ("the danger meter") ☐ 6–8 sections with an intensity curve ☐ One peak, one quiet beat, one CTA.
**Hook (0–2 s)** ☐ Biggest graphic of the video ☐ Impact SFX ☐ No caption clutter ☐ Promise made visible (timer/number).
**Pacing** ☐ New visual every ≤4 s ☐ Micro-event every ≤0.8 s inside cards ☐ Cards enter just before the word ☐ Breather after every takeover.
**Text** ☐ Setup line + one keyword ☐ ≤6 words ☐ Word-timed ☐ Grey→bright on the spoken word ☐ Never over the eyes ☐ Safe area x 60–1020, y 120–1700.
**Motion graphics** ☐ One design token set ☐ Blur on every entrance ☐ Overshoot in, faster out ☐ Idle motion on anything >3 s ☐ Behind-the-head layer used at least twice.
**B-roll / PNG** ☐ Pro assets only ☐ Literal noun match ☐ No asset twice ☐ Tinted to the palette.
**Effects** ☐ One signature transition per section change ☐ ≤3 glitches/min ☐ Every flash has a hit ☐ Grain + vignette on.
**Music** ☐ Flat-energy track ☐ ≈18 LU under voice with −5 dB ducking ☐ One full cut on the key line ☐ Fade in the last 0.6 s.
**Sound design** ☐ Every graphic has a sound ☐ Riser before the peak ☐ No two whooshes within 0.25 s ☐ Cue sheet exported for Epidemic swap.
**Colour** ☐ Accent colour = section state everywhere ☐ Skin tone untouched ☐ Light/dark scenes alternate.
**Transitions** ☐ Blur by default ☐ Hard cut on the speaker's own jump cuts ☐ Hazard/light-leak once each.
**Final QC** ☐ Key-frame sheet reviewed ☐ QA sheet from the encoded MP4 ☐ Black bands covered from the first frame ☐ Loudness −14 LUFS / peak ≤ −1 dB ☐ Master + upload MP4 + stems + breakdown delivered ☐ Playbook updated with any new Deepak rule.

## 17. Applying this to a new video

1. **Analyse first:** ffprobe the source, extract 1 fps contact sheets, find jump cuts from audio micro-silences, transcribe per chunk with word timestamps, measure head position per shot from masks, and locate any black bands from existing keyframes.
2. **Find the spine:** what single visual system can hold the whole script? (a meter, a checklist, a map, a scoreboard, a timeline, a phone screen). If none fits, use the reference two-size type system from `motion-graphics-style` as the default spine.
3. **Map beats to graphics** using the IF→THEN rules in §12, one graphic per beat, then assign a colour token per section.
4. **Build with the helpers** in `comp.js` (copy the file, replace the beats; keep layers, `__seek`, `textAt`, `fit`, `rng`). Reuse the gauge/timer/card/header components only if they fit the new spine; otherwise build new ones with the same tokens and easing.
5. **Preview by timestamps → fix → full render → QA from the MP4.**
6. **Mix**: voice 0 dB, SFX −5 dB bus, BGM −15 dB bus with ducking, master to −14 LUFS. Export stems and the SFX cue sheet.
7. **Deliver** master + upload MP4 + breakdown, then save any new Deepak feedback via `skill-saver`.

Do **not** copy this video's timings, colours or the danger-meter idea verbatim onto a different topic. Copy the method: analyse → spine → beat map → tokens → helpers → preview loop → mix → QC.
