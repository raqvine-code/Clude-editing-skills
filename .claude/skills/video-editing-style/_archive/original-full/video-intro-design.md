---
name: video-intro-design
description: Build kit and rules for a short, extremely dense INTRO (20–40 s) cut from one locked-off talking-head take — browser-side camera on a 2560×1440 plate (pixel-exact punch-ins), Vision person mattes for giant type behind the head, measured colour-separation for the accent palette, Win98/BIOS period UI, dither-through-black transitions, procedural SFX balanced for phone speakers, and the six-lens QA that catches what stills QA misses. Use for any intro, hook, cold open, title sequence or short high-density motion-graphics piece over a single talking-head clip. Built on the Y2K intro (experiment/claude6_intro, 2026-10-01).
---

# Intro motion design (built on the Y2K intro, 2026-10-01)

> **Note (2026-10-06):** `experiment/` paths in this skill are historical — that folder was cleared. Final videos + edit notes: `Raghu and claude/edited videos by claude/`. Reusable code: the `code/` folder inside each video folder. Reference analyses were folded into the skills and deleted.

Project: `experiment/claude6_intro/` — `build/` code, `work/` intermediates, `deliver/` outputs.
Long-form sibling: `youtube-long-video-editing`. Look rules: `motion-graphics-style`. Deepak's word wins: `my-editing-rules`.
Tags: **[USED]** done on this intro · *(Claude, not yet approved by Deepak)* = my own rule.

An intro is **not a short explainer**. 33 s carries ~90 SFX cues and ~28 graphic events, every one keyed to a
measured word onset. Everything below exists because a 20-minute-film habit broke at that density.

## 1. Pipeline [USED]

1. **Recover the script exactly.** ASR of Telugu/English is unreliable at sentence level. Run
   `faster-whisper large-v3` on **VAD-aligned chunks** (not the whole file — long segments merge and hallucinate),
   then cross-check every line against Deepak's own transcript file. The Y2K intro turned out to be assembled from
   8 lines of `refrences for claude/transcript for Y2K video.txt`; that file, not the ASR, is the truth.
2. **Measure the phrase map before designing.** 5 ms RMS envelope → speech runs, pause lengths, stress peaks
   (`work/analyze_audio.py`). This gives the real cut points and proves how much dead space actually exists.
3. **EDL = trims only.** Map output frame → source frame as a table (`work/edl.py` → `edl.js`), so the edit can be
   re-timed without re-extracting a single frame.
4. **Grade once, extract at native resolution.** One continuous ffmpeg pass, 2560×1440, `-q:v 3`, ~100 s for 1982
   frames. Vignette, grain and any region mask go in the browser, never baked.
5. **Person mattes** with macOS Vision (`work/tools/matte.swift`, `VNGeneratePersonSegmentationRequest`,
   `.accurate`) — ~1.8 s/frame, 6 parallel processes ≈ 10 min for 2000 frames.
6. **Scenes** in HTML + GSAP on one clock; render through headless Chrome at **deviceScaleFactor 4/3** so every
   capture is 2560×1440; downscale to 1920×1080 with lanczos at encode time.
7. **Stills QA → fix → full render → six-lens QA → fix → final render.** Budget two full renders. 1937 frames at
   28 % supersampled = ~3.5 min render + ~1.5 min averaging + ~5 min encode on a 6-core i7.

## 2. The camera — a punch-in can be pixel-exact [USED]

The plate is 2560×1440 and the stage is 1920×1080, so **zoom 1.3333 is a 1:1 crop**. Measured against an ffmpeg
`crop=1920:1080` of the same frame: **1.005** of its sharpness — indistinguishable.

- `k = 0.75 × zoom`. **Only hold where k is exactly 0.75 or 1.0 AND the translate is an integer.**
- Landing off the pixel grid costs more (0.885) than zooming past 1.33 does (0.870). So: *a hold snaps, a move
  does not*, and `camTrack` returns `snap:true` only when two keyframes are identical.
- Presets that are all 1:1: `PUNCH` (centred), `PUNCH_HI` (chin-up), `SPLIT_R` / `SPLIT_L` (head in one half,
  a 900 px panel in the other — a split layout costs **zero** sharpness).
- Everything between is transit: pass through, never rest.
- **`will-change: transform` does not soften the punch-in** — `Page.captureScreenshot` forces a full re-raster.

### Camera rules learned
- A `power3.inOut` leg over 2.9 s is **motionless for its first 0.7 s and last 0.4 s**. Split long pushes:
  `out3` off the cut (immediate motion) then `in2` into the end (fastest on the final frame).
- Two identical keyframes = a dead camera. If a hold must last > 1.2 s while he is still talking, make it a
  micro-drift (3–4 % of zoom over the span) instead.
- **Snap OUT on a hero word, snap IN on a negative word.** A pull-out gives the word room; a push-in reads as panic.
- Cap the punch per shot by its own softness, not by one global number: measure mean abs-Laplacian on the face
  band. On the Y2K intro shots 4 and 5 carried 35–45 % less detail than shot 3 *despite being tighter framings*.

## 3. Giant type behind the head [USED]

The signature Tharun/Somrat look, and it works — with two conditions.

- Layer order: plate → **dark band (`L_behind`)** → type → **person cut-out (`L_person`)** → scrim → scene.
  The band is what makes it readable; white on the bare wall is 1.9:1.
- The Vision mattes are **opaque greyscale PNGs**, so the CSS mask must read luminance:
  `mask-mode: luminance; -webkit-mask-source-type: luminance`. With the default alpha mode the mask is a no-op and
  the un-masked plate silently covers every layer beneath it. *(This cost an hour; symptom = graphics "disappear".)*
- **A long word loses whole glyphs.** "SHOCKING" at 268 px centred on his head lost three letters for its entire
  life. Size and stage the word so the silhouette eats **one letter at most**: measure the occluder's x range in
  the letter band first, then set `x` and `size` so only the first glyph crosses it.

## 4. The accent colour is a measurement, not a taste call [USED]

Sample the plate before choosing anything. On the Y2K footage skin (Lab hue 52°), the door (52°), the lampshade
(54°) and the warm wall (60°) all sat inside **one 9° hue band** — so amber/orange, the reflexive Y2K choice,
dissolves into his face (ΔE 33–41 from the lamp). Cyan at 215° is the maximum separation available.

| | value | the rule it creates |
|---|---|---|
| accent | `#00E5FF` | **1.03:1 on the bare wall — physically invisible unplated.** Cyan may only exist on a `#06070A` plate. That single fact is what keeps the black gradient "sparing": the accent *cannot* leave the plate. |
| chrome | `#C0C0C0` | 1.22:1 on the wall. Plated-only, no exceptions, and exactly one hero word per film. |
| alarm | `#E23A2E` | turn words only. If two reds appear in one frame they must be the *same* red. |
| amber | `#FFB000` | only inside a fully plated frame (a DOS/BIOS card, a dialog's marker). |

**Corollaries that bit:**
- A 1 px cyan rule is invisible the instant it leaves its plate. **Stop every rule where the dark backdrop stops.**
- Small cyan labels need their own chip (`rgba(6,7,10,.9)`, 7/16 px padding), not the big scrim — a bottom scrim
  of height 640 evaluates to α 0.05–0.10 at y 600, which is nothing.
- Never put a label in the mouth band. It is both a house rule and a contrast failure (skin and teeth are the
  brightest thing in frame).

## 5. Composition and hierarchy [USED]
From the reference-board law (`motion-graphics-style` → Editorial print-grain explainer), re-proved here:
- **Chroma beats size; size beats position.** A data panel with seven hues put the two *reference* bars on top of
  the hero number. Neutralising the "before" bars to white at 20–40 % fixed the whole frame in one move.
- **One object carries the beat.** The panel asked the question (a cyan "?" plus a blinking AWAITING caret), then
  answered it with the same chart, then expanded to full frame on the number. Morph, don't replace.
- **Never pre-draw the answer.** Bars created with `scaleY(0.03)` sat on screen as coloured 9 px stubs for 2.6 s
  before their cue, giving the result away and striking through the label underneath. Create hidden, reveal on cue.
- Parent a component to the thing that slides. A chart built on `c.root` while its panel animates from x −900
  tears off the panel for five frames and reads as a render bug.
- **Qualifier on screen, always** — `Source · …` at the bottom left. It is both a credibility device and what
  closes the bottom of the frame. Give `srcTag` an explicit `z-index` or it paints *under* an opaque panel.

## 6. Transitions [USED]
- **Dither-through-black** is the premium Y2K transition and the one that solves full-frame cards: 16 discrete
  Bayer steps to full black at a chosen instant, then 16 steps back. Put the black instant on the cut.
  The full-frame scene must **end exactly at that instant** — otherwise the dissolve reveals the card, not the footage.
- It also hides an EDL join: hold the card through the pause so the black instant lands on the join frame.
- **Scanline flash** must be a translucent scan *over* the picture (peak α ≤ 0.35), not opaque bars; at 0.55–1.0
  it replaces the image and reads as a glitch artifact.
- **One flash, never a train.** Five 1-frame white flashes 4 frames apart is a ~16 Hz strobe that changes 96 % of
  the frame each time — a photosensitivity risk and it makes the pinned word disappear four times. One flash, 0.12 peak.
- Period UI (Win98 dialog, BIOS card) appears in **one frame**, never eases, and never gets a drop shadow.
  Render at integer px with `image-rendering: pixelated` and `-webkit-font-smoothing: none`.

## 7. SFX — the phone-speaker rule *(the single biggest audio finding)* [USED]

`pk50` (and every loudness meter) is **band-blind**. A hit made almost entirely of 40–120 Hz measures "as loud as"
a click and then **vanishes** on a phone. Measured through a 300 Hz high-pass on the first build:

| | full-band | > 300 Hz | loss |
|---|---|---|---|
| `imp_crush` (the climax) | −25.7 | −43.8 | **20.4 dB** |
| `imp_sub_land` | −26.7 | −49.6 | **23.0 dB** |
| `dither_wipe` (a transition) | −32.7 | −32.8 | 0.2 dB |

So on the device Deepak's audience actually uses, the transitions were the accents and the accents were inaudible.

**Fix:** every sub-bearing hit gets a **150–400 Hz knock** and a **1.2–3.5 kHz click** (4 ms attack, ~25 ms decay),
then `phone_balance(x, target_loss_db)` solves for the sub's gain so the full-band level is only 5–8 dB above the
>300 Hz level. Split the bands with **zero-phase `sosfiltfilt`** — a causal lowpass plus `x − lo` is not a
complementary split and the solver silently does nothing. Verify the hierarchy in the phone band:
hit → transition → text entrance → tick.

### Other sound rules learned
- The cue's `gain` in the scene file is the **absolute target** (dB relative to voice RMS); the mix applies
  `gain − baked_level`. Changing a baked level alone therefore does nothing. Change the cue.
- **A sting only brands a moment if its first appearance IS that moment.** `ui_err` fired on every dialog *open*,
  so by the time the dialog actually errored the ear had learned the buzz meant "a window appeared".
- **No cue without a picture event.** A landing fired on a frozen match-cut card and put three sub-bearing hits
  inside 470 ms, making the montage louder than the climax.
- Sub-bearing sounds need **300 ms minimum spacing** (measured buildup: +3.5 dB at 60 ms, 0.0 at 550 ms).
- A hit paired with a 1-frame flash and a shake must be **sample-locked** (+25 ms), not the component's default
  +120 ms — 7 frames is well past the ~45 ms window where the ear fuses a transient with a flash.
- A riser must land on something. `rise_short` with nothing to release into just decays.
- **No music in an intro Deepak will score himself:** master at **−17 LUFS / −1.5 dBTP** (not −14) and ship
  `stem_voice.wav` + `stem_sfx.wav` so he can rebalance instead of asking for a re-render.
- Texture beds must be **narrowband and slotted outside 250–1000 Hz** (CRT whine at 7812.5 Hz — the 15.625 kHz
  octave dies in AAC — plus 50 Hz Indian mains, not 60). A broadband bed at a useful level fights the consonants.

## 8. Six-lens QA *(Claude's rule, not yet approved by Deepak)* [USED]

Stills QA catches layout. It does **not** catch strobes, band-blind levels, exposure steps at cuts, a vignette
that falls outside the frame, or a 16 px head jump at an EDL join. After the first full render, run six
independent reviewers over the rendered frames — **frame design · typography · motion & timing · continuity ·
colour & grade · sound against picture** — then attack every finding with a separate skeptic that defaults to
refuting it. Each reviewer must open the real 2560×1440 frames, not only a contact sheet, and report with
measurements.

Things only this pass found, on a film that already looked finished:
- a 16 Hz strobe over the match cut;
- every impact 20–26 dB down on a phone;
- one shot graded a third of a stop under for 5.3 s (the per-shot exposure match had over-corrected the one shot
  that was already matched — always verify the *graded output*, not the correction you intended);
- `radial-gradient(118% 150% …)` putting both vignette stops outside the picture — 5 % falloff instead of 30 %;
- the CRT open revealing him mid-blink for 7 frames;
- chapter ticks left out of the fade-out array, so they were at full strength on the last frame.

**Pitfall:** if you fix findings while the verifiers are still running, they will read the *fixed* frames and
refute almost everything. Judge each finding yourself against the frames; a refutation only counts if the
verifier was looking at the same build.

## 9. Measurements worth keeping
- `fps=4` contact sheets drift up to ~0.15 s off their burned-in label. Confirm any timing claim on the numbered
  frame file, never on a sheet cell.
- `-i frames/%06d.jpg` defaults to `start_number 1` — frame 0 is silently dropped. Pass `-start_number 0`.
- `-shortest` trims the video to the audio: make the mix `round(N/60 × SR) + 240` samples or you lose the last frame.
- A full-frame per-element `filter: blur()` doubles render time. Masks and transforms are free; use `clip-path`.
- `opaque: () => true` on a designed full-frame scene skips the 2560×1440 JPEG decode entirely.
- Parallelise the sub-frame averaging (`Pool(6)`): 30 min → 5 min, and it is the real bottleneck, not Chrome.
