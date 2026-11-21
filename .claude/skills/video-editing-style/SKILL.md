---
name: video-editing-style
description: Professional short-form vertical (9:16) editing methodology, reverse-engineered frame by frame from five high-retention reels - an editorial motion-graphics explainer, two talking-head reels with kinetic captions, two faceless 2.5D documentary stories and a raw-vs-edited agency showcase. Use it whenever the user wants to plan, script, edit, caption, sound-design, review or critique a reel, TikTok, YouTube Short or other vertical video, asks for an edit in this style or like these reels, wants a beat sheet, shot list, caption system, transition plan or an After Effects, Premiere, CapCut or Remotion build sheet, or wants to analyse a reference video's editing. Gives measured numbers (frame counts, ease curves, sync offsets, SFX grammar, loudness), a word-to-event mapping workflow, a transition and device library, fixes for the references' mistakes and a scorecard script that checks a render against the reference ranges.
---

# Short-form editing methodology (5 reference reels)

Everything here was measured frame by frame (30 fps) on five reels; ≈ marks an estimate, font names are visual
guesses. Frame counts assume 30 fps: convert with seconds = frames / 30. Sizes are % of frame width (W) or height (H).
"wpm" = spoken words ÷ total runtime, pauses included (the scorecard's count), so it converts straight into a word budget.

| Ref | Reel | Format | Length | Voice | Deep notes |
|---|---|---|---|---|---|
| R0 | "Elon owns 20% of Tesla" finance explainer | A editorial motion graphics | 29.9 s | 163 wpm | `references/format-a-editorial-motion-graphics.md` |
| R1 | "Remember your script" 3 tips | B talking head, kinetic captions | 34.0 s | 224 wpm | `references/reels/R1-talking-head-tips.md` |
| R2 | Semmelweis hand-washing story | C faceless 2.5D documentary | 40.9 s | 150 wpm | `references/reels/R2-faceless-documentary.md` |
| R3 | Russian scientist plague mystery | C faceless 2.5D news mystery | 42.6 s | 128 wpm | `references/reels/R3-faceless-news-mystery.md` |
| R4 | Realtor/AI reel in RAW vs EDITED wrapper | B talking head + heavy graphics, D showcase | 35.6 s | 204 wpm | `references/reels/R4-talking-head-showcase.md` |

Read this file first. Then open only the reference you need: the format file for the chosen format
(`format-a…`, `format-b-talking-head.md`, `format-c-faceless-documentary.md`), `transitions.md` for a transition
recipe, `devices.md` for a graphic or text device, a reel note when you want the full beat sheet or evidence.

## 1. The method in one paragraph

Every reel that held attention did the same three things, whatever it looked like. **Something new happens on
screen at least every 1.3 s** (longest visually quiet stretch measured: 0.13–1.30 s; frozen frames 0.2–2.4 %).
**Every visual event is caused by a word**: scene changes start on sentence onsets, emphasis lands on the keyword,
mode changes sit in breaths. **Every change has a sound** from a small, meaning-coded vocabulary. The look varies by
format; these three laws do not. The workflow below turns a voice-over into an *event map* that satisfies them,
then builds it.

## 2. Pick the format

| | A Editorial motion graphics | B Talking head, kinetic | C Faceless 2.5D documentary | D Before/after wrapper |
|---|---|---|---|---|
| Use for | Explainers, money/business ideas, product promos | Tips, opinions, creator or client A-roll | Stories, history, news, mysteries | Selling editing services, case studies |
| Picture | Cutouts + 3D objects + type, no footage | Speaker, cut-outs over graphics, full-screen cutaways | Generated or stock stills built into layered dioramas, virtual camera | B or C inside a static card layout |
| Voice | ≈165 wpm, deep, compressed | 200–225 wpm, natural | 128–150 wpm, slow, sentence gaps 0.2–1.0 s | inherits |
| Cut style | Designed transition on every scene change | Hard cuts hidden under moves; 11 shots / 34 s | The camera moves *through* scene changes: R2 has 2 true content cuts in 41 s; R3's ≈10 hard cuts sit inside rolls, pull-backs and texture bridges | inherits |
| Camera | Slow push 1–2 %/s, rise-in entrances | Push-in hook, zoom bumps, breathing pull-outs | Rotate-and-pull-back on every plate, fly-back entrances | static wrapper |
| Text | Every line, dual-font word reveal | Every phrase, two-tier captions | Only when the word *is* the picture | labels + footer CTA |
| Sound | VO + whoosh per cut + one sub boom | VO + music bed + sparse SFX | VO + SFX grammar, no melody, sub drones | inherits |
| Median frame-to-frame change (scorecard) | 2.2 | 1.8 (R1), 3.1 (R4 panel) | 5.8 | — |

The median frame difference tells you the energy budget: talking heads are calm between events and rely on
captions and reframes; faceless stills must move all the time or they read as a slideshow.

## 3. Workflow (the event map)

1. **Script** to the story spine in section 4. Word budget = seconds × wpm ÷ 60, CTA included: a 35 s reel is
   ≈75–88 words faceless (128–150 wpm), ≈95 words format A (165 wpm), ≈120–130 words talking head (204–224 wpm).
   Read it aloud; cut until it fits.
2. **Voice first.** Record or synthesise, then edit the pauses. Talking head: keep 0.2–0.3 s breaths only where a
   mode change will go. Faceless: keep 0.4–1.0 s gaps between sentences; they are where scene changes and sounds live.
3. **Word timestamps.** Run Whisper (or mark by hand). Every later rule is an offset from a word onset. Planning
   before the VO exists, estimate onsets at 60 ÷ wpm seconds per word plus the gaps, then re-snap every event to
   the real onsets once the voice is recorded.
4. **Event map.** A table with one row per event: `t | VO words | picture/transition | device | camera | text | SFX`.
   An event is anything new on screen: a transition, a device changing state, text appearing, a camera accent
   (punch, bump, entrance). Fill it with the rules in sections 5–10, then check the cadence: no gap over 1.3 s
   without an entry; in the hook aim for one every 0.6–1.0 s (R3: every 0.6 s).
5. **Assets** per row: cut-outs, plates (generated images need 1.3–2.5× overscan for the camera moves), props,
   logos as vectors, textures, SFX.
6. **Build** in this order: base camera moves → transitions → devices → text → SFX → mix. Text and SFX go last
   because they snap to the final word timing.
7. **Finish**: grade, a glue texture, loudness (section 10).
8. **Score**: `python3 scripts/reel_metrics.py render.mp4 --transcribe` and the checklist in section 12; inspect
   every transition with `scripts/frame_sheets.sh` at 30 fps.

Example event-map rows (R3, 0–1.7 s; the VO starts on frame 0):

| t | VO | picture / transition | device | camera | text | SFX |
|---|---|---|---|---|---|---|
| 0.20 | "A Russian scientist" | lab plate, subject cut-out | fly-back entrance | 3× → 1× in 12 f, then −1 %/f | none | sub boom (0.19 s) |
| 1.16 | "died" | coffin rises behind subject (8 f, lands on the word) | shape insert | drift | none | sub boom (0.99 + 1.16 s) |
| 1.43 | "mysteriously" (1.56) | grave texture irises open (f43–48), B&W + bloom at f50 | colour = death | drift | none | carried by the boom tail |

## 4. Story spine and pacing

All five scripts share one spine:

1. **Hook claim or question** in the first sentence (ends at 2.1–3.4 s in R0, R1, R4; the faceless reels ran one long
   sentence to 6.0–6.8 s, which only works because the picture changes on every key word).
2. **Reframe or stakes** ("you don't actually need…", "AI isn't coming, it's already here", "until one man…").
3. **Proof in threes**: three examples (R0), three numbered tips (R1), problem → discovery → result (R2).
4. **The turn** at **60–75 % of the runtime in seconds** in every reel: R2 "but doctors rejected" 62 %, R3 "But there
   was a twist" 63–65 %, R0 "Stop… / Start…" 61–74 %, R4 "But the crazy thing is" 73 %, R1 "And that way" 76 %.
   Spend the biggest device of the second half here.
5. **Payoff / moral** in one short line, shown big (R0 "That's how real wealth is made", R2 single serif words).
6. **CTA**. The references spent 13–22 % of runtime on it, often static: that is where they lost people. Keep it
   ≤ 12 %, keep the house camera move alive, and end on a frame that loops into the first. A follow CTA needs no
   URL: put the handle on a surface in the reel's own style (verdict caps, a card push-up) and keep moving.

Pacing numbers: a new caption word every ≈0.35 s (R0), talking-head shots average 3.1 s (R1), mode switches
every ≈2.5 s (R4), faceless beats ≈2.5 s with one picture per sentence (R2: 16 beats in 41 s). Keep the second
half as dense as the first: R4 made ≈10 mode switches in its first half and ≈4 in its second, and its last 4.5 s
had nothing new.

## 5. The hook (first 3.5 s)

Measured: R1 push-in starts f5, first caption f1, three underline "rewards" by 3.3 s, then a beat drop and a
luma flip (12 → 255) on the first cut at 3.33 s. R2 moves through four spaces in 3.5 s without a cut. R3 lands
five events in 3 s, each on a VO word. R4 shows four visual states in 3.7 s and types the spoken question into a
search bar. R0 shows the first word at f4 and the subject rising into frame from ≈f10.

Rules:
- Voice on frame 0; first motion by frame 5; first readable text by 1 s, in every format: a faceless reel that
  otherwise shows no captions still puts its claim in verdict caps in the hook (R2 had no text for 4.5 s, so
  sound-off viewers got nothing; R3 opened on 6 dead frames; R4 on a motion-blurred frame — avoid all three).
- 3–5 visual state changes in the first 3.5 s, each tied to a word of the first sentence.
- Front-load the motion: 70 % of the hook move in its first 0.7 s (R1 ×1.6 push-in, 70 % done by f20), then hold.
- Exit the hook with the biggest contrast change of the first 10 s, on the first sentence's last word: luma flip,
  beat drop, world change or a shrink into a UI.

## 6. Sync rules (word → event)

| Event | Timing against the word onset | Evidence |
|---|---|---|
| Caption / function words appear | 0 to +2 f | R1 median +0.8 f over 53 words, 70 % within ±3 f; R4 median −1 f |
| Keyword (big caption word) | either starts 6–8 f early and settles *on* the word, or starts on the word and fills over 7–10 f | R4 tracking-in −8 f; R1 opacity fill 7–10 f |
| Text that *is* the picture (name, date, number, verdict) | 0 to +4 f; typing may start ≈10 f early so it completes on the word | R2 mean +1.5 f; R3 date typed 10 f early |
| Scene change / transition start | −0.22 to +0.25 s around a sentence or clause onset; long moves (up to 44 f) run on over the next words and are timed so their peak or fill lands on that sentence's key word | R2 14 of 15 transitions, median +3 f; eyepiece wipe completes on "bacteria" |
| Mode change (speaker ↔ graphic, chapter card) | in the breath: +50 to +300 ms after the phrase ends; return on the next phrase's first word | R1, all mode changes |
| Emphasis hit (punch-in, icon drop, circle, boom) | on the keyword ±3 f | R3 punches, R4 pedestal icons within 4 f, R1 list bumps 0–4 f early |
| SFX | within ±3 f of its picture event; ticks 1–2 f before a word swap; booms pre-lap a card by ≈3 f | R2, R3 |
| VO pause ≥ 0.5 s | must carry a move + SFX | R3: 8 of 8 pauses |

Do not cut to a music grid unless the music leads the piece: R1 had a 133 bpm hat grid and only 3 of 10 cuts and
7 of 23 keyword pops landed on it (chance level). The voice is the clock.

## 7. Text systems

Pick one per reel; full specs in the format files and `devices.md`.

- **Two-tier captions (format B).** Small function line + one big keyword per group, 3–9 words per group (median
  5–6), groups last ≈1.3 s and clear in 1 frame. R1: small ≈2.3 % H, keyword ≈5.4 % H (2.3×), heavy geometric
  sans, centred, block in 0.56–0.74 H on the torso, never on the face, always in front of hands. R4: small line
  ≈3 % W typed at 1 char/f, keyword cap 5–7 % W (10–11 % for emphasis), centre at 0.63 H, staggered 3-line ladder.
- **Colour = role, not decoration.** R4: gold `#E8A64E` = topic/opportunity, red `#DA1E34` = threat or the
  out-group, white + 15 px orange bar = argument pivot ("But…", "Which means…"). R2: red only for danger and the
  turn word, green for life and improvement. A verdict block gets one red word only if it contains one of
  those; otherwise it stays white or black. R1: one cyan `#2EC0D7` brush underline as the accent.
- **Text as object (format C).** No captions; text appears only when the word is the shot (name, date, number,
  headline, verdict, moral) and is printed on a surface in the world. Font follows the surface: verdict =
  ultra-black extruded caps with one red word (cap ≈7.8 % W in R2); data = typewriter (≈1 char/f, underline trailing
  ≈8 f); archive/moral = bold italic serif, one word at a time. R3 showed text for ≈15 % of its spoken words; R2 had text on screen for ≈37 % of its runtime.
- **Dual-font word reveal (format A).** Bold grotesk + italic serif, words blur in over 6–8 f. See format A.

Legibility floor (the references broke all of these):
- Smallest text ≥ 2.5 % H on the final 9:16 frame (R4's small line was ≈0.9 % H inside its wrapper: unreadable).
- Contrast ≥ 4.5:1, or a 2–3 px dark stroke / 30 % shadow (R1 white on a light shirt 2.35:1; R2 red on sky 1.3:1).
- Reading order left → right, top → bottom (R1 stacked "practice / it in your saying / own words").
- Animate keywords with scale or tracking, not a fade from 35 % (R1 keywords were near-invisible for 3–4 frames).
- Spell-check every overlay against the script: **all five references shipped a typo** ("Billionairs",
  "scipt", "DRAMATICALY", "its already", a mid-headline "Dies").

## 8. Camera and motion

House curve for every move: **front-loaded ease-out, ≈70 % of the travel in the first 30 % of the duration**,
then keep drifting until the next event (R0 rise-in, R1 push-in, R3 fly-back, R4 settle all match). Motion blur on.

| Move | Numbers | Use |
|---|---|---|
| Hook push-in | ×1.57–1.65 from f5 to f55, peak 3.2 %/f at f13, then hold | B hook |
| List zoom-bump | +7 to +15 % in 6–8 f, starting 0–4 f before the item's label; hold still between | B lists |
| Breathing pull-out | −2.5 to −3.2 %/s for 3.7–6.2 s, easing to a stop | B tight delivery shots |
| Zoom-through cut | out 1.0 → 1.26× in 12 f ease-in, cut, in 1.35 → 1.0× in 16 f (36 % of the remainder every 2 f) | B hide a jump cut |
| Rotate-and-pull-back | start 1.3–2.5× and 15–30° tilt, ease out at −16 to −23 %/s over 1.3–2.5 s | C every plate |
| Fly-back entrance | subject 3× → 1× in ≈12 f (0.83, 0.88, 0.91, 0.93, 0.95, 0.96, 0.97 per frame), sub boom on f1, then −1 %/f | C; the entrance itself ≤ 2 per reel (R3 used 5: predictable); constant drift is separate and never stops |
| Denial punch | same plate ×1.41, −16° roll, crushed B&W, settles in 9 f | negation words |
| Dim-and-overlay | speaker to ≈46 % brightness + defocus over 30 f, overlay a literal object | B idioms |
| Rise-in | from below frame, 66 f, 70 % of travel in 20 f, keeps creeping | A subjects |

Never mix frame rates: R3's 15 fps archive sections read as stutter beside 30 fps moves.

Defaults when no recipe fits (all within the measured ranges): text or object pop-in 4–8 f ease-out, exit 6–12 f
fade + blur; line or circle draw-on 8–14 f; colour or B&W switch 7 f; prop rising into frame 8 f landing on its
word; emphasis punch on a non-negation keyword +7 to +35 % in 1–6 f with a sub boom; hard cut = an airy whoosh or a
beat drop on the cut frame.

## 9. Transitions: choose by meaning

Each transition says something; pick it from what changes. Recipes with every frame count are in `transitions.md`.

| What changes | Transition | Frames | Ref |
|---|---|---|---|
| Nothing (same speaker, same thought) | hide the jump cut: zoom-through, strobe, or a graphic laid over it | 12+16 / 5 | R4 hid 10 of 11 cuts |
| Speaker ↔ graphics (same idea) | luma-flip hard cut in the breath (dark 12 → white 255) | 0 | R1 |
| Speaker ↔ graphics (metaphor) | live video card: speaker keeps playing in a rounded card | 3 + push 7 | R1 |
| New chapter / list item | chapter card (0.7–1.8 s), card push-up, or a light-leak in the pause before "But" | 21–53 / 8–14 / 7+2+1 | R1, R3, R4 |
| Act change, light ↔ dark | light-leak flash ending on 1 f of scanlines | 10–11 | R0 |
| New place or time (faceless) | window zoom-through, light iris, spin-portal, blur-rotation, rotation-matched cut, macro-texture bridge, vertical whip, floor wipe | 11–44 | R2, R3 |
| Cause → effect | object iris born at the cause (between the washing hands → result chart) | 14–15 | R2 |
| Live → evidence | live-to-print pull-back: zoom out ×0.45 to reveal the shot is a photo in a newspaper | 23 | R3 |
| Into the punchline | 1-frame invert flash, then hard cut | 1 | R0 |
| Open question / ending | keyhole hold 1 s in silence, then push through | 30 + push | R3 |

Limits: one signature transition, used ≤ 3 times (R0 used its light-leak 3 times); vary the rest. Flashes: no more
than 3 per second (R4's 7-frame hook strobe swings brightness 4 times in 0.23 s, a photosensitivity risk).

## 10. Sound design

One vocabulary, three meanings (R2 and R3 measured it; R4 matches):

| Sound | Spec | Means |
|---|---|---|
| Tick / click | 30–130 ms, 7–11 kHz | small event: a word swap (1–2 f before), a material change, a UI type-on |
| Whoosh → boom | 0.46–0.8 s, wide stereo, pitch falling ≈7 kHz → ≈500 Hz, +26–33 dB over the floor | change of world or location; peak on the cut or the iris fill |
| Sub boom | mono 20–80 Hz, ≈0.5–1 s, −15 to −23 dBFS | a meaning word (died, killed, dropped) or an object landing |
| Bright hit / riser | hit on the first flash frame; riser peaking 4–10 f before it | flash and strobe transitions |

- Density: ≈5–10 distinct stereo SFX per 10 s (scorecard detector on the stereo side channel: R2 5.4, R3 6.6,
  R4 9.5), plus mono sub hits that this count misses. R1's SFX were sparse and loosely placed (only 7 matches
  between its 20 visual events and its stereo transients), so its cuts went unmarked.
- Music: the faceless reels had none (drones and ambience only); R4 had a beatless tonal bed ≈24 dB under the
  voice and pulled its bass out from 31 to 34.5 s, just before the final hits; R1's beat bed sat only ≈3 dB below
  the full mix, never ducked.
  Rule: voice first; any bed ≥ 12 dB under the voice band; use the music's structure once (R1 removed the kick
  through the hook question and dropped the full beat on the first cut).
- Let the floor fall toward the moral (R2: −25.5 → −37.9 dBFS) and put the CTA cut on the quietest moment.
- Master to −14 LUFS integrated (references −14.1 to −15.2) and **true peak ≤ −1 dBTP**: all five references
  exceeded it (−0.2, −0.8, +1.3, +2.9, +3.4 dBTP) and R3's clipped samples all sat on transition SFX. Limit the
  SFX bus, then the master.

## 11. Colour and finishing

- **Luma = chapter.** Flip average brightness by more than 80 levels at act boundaries (R2 at 3, 8, 10, 23 and
  32 s; R0 white → black at 37 %; R1 black → white on the hook exit). The eye reads it as "new section".
- **Colour = meaning, one accent per scene.** Alternate saturated emotional scenes (saturation 0.6–0.75) with
  near-mono evidence scenes (0.02–0.1). B&W = death, the past, doubt (R3); red = danger, green = life (R2).
- **Glue texture** over mixed or generated imagery: a static 45° halftone screen, ≈0.6 % W period, 2–3 %
  amplitude (R2), so every plate reads as one printed piece.
- **Talking-head grade (R1):** background crushed to ≈`#040004`, hot orange hair rim (`#DC8438`), steel-blue fill
  (`#465C70`), skin ≈`#9C7668`, warm out-of-focus practicals (`#FDEE96`) in the top third. R4's grade came from the
  shoot, not the edit: light the set and the edit only has to protect it.

## 12. Surpass the references (QC checklist)

Run `python3 scripts/reel_metrics.py render.mp4 --transcribe` (add `--crop W:H:X:Y` for a panel). Its targets are
the reference ranges; every LOOK line needs a reason. Then check:

- [ ] Every overlay spell-checked against the script and the spoken words (5 of 5 references failed).
- [ ] True peak ≤ −1 dBTP, −14 LUFS ±1 (5 of 5 failed).
- [ ] Hook readable with sound off by 1 s; no dead or blurred first frames.
- [ ] Longest visually quiet stretch ≤ 1.3 s; no frozen frames beyond 2.5 %.
- [ ] Every transition starts within −0.22/+0.25 s of a sentence onset; every emphasis within ±3 f of its word.
- [ ] Every scene change has an SFX; every VO pause ≥ 0.5 s has a move.
- [ ] Smallest text ≥ 2.5 % H, contrast ≥ 4.5:1, reading order correct.
- [ ] Signature transition ≤ 3 uses; fly-back ≤ 2; no flash burst above 3 per second.
- [ ] Second half has ≥ 70 % of the first half's event rate; the turn (60–75 %) carries a major device.
- [ ] CTA ≤ 12 % of runtime, still moving; last frame loops into the first (none of the five looped).
- [ ] No fabricated evidence or borrowed trademarks: R3 put NBC branding on generated headlines and R4 used an
      OpenAI-style logo. Label illustrative imagery and use your own marks.
- [ ] Data graphics match the claim (R2's death curve kept rising past the year it should drop; its chart had no
      numbers).
- [ ] Generated plates checked for artefacts during camera moves (R2 showed mirrored tiling while panning).

## 13. Reverse-engineering a new reference

1. `scripts/frame_sheets.sh ref.mp4 overview.jpg 0 60 1 9 5 200` for the map; then 30 fps sheets across every
   transition and 10–15 fps across every text animation.
2. `python3 scripts/reel_metrics.py ref.mp4 --transcribe --json ref.json` for cuts, quiet stretches, loudness,
   wpm and SFX-on-cut. A hi-hat bed inflates SFX-on-cut (R1 read 80 % for that reason): confirm by ear or by
   checking the stereo side channel.
3. Fill a beat sheet (t, frames, VO, visual, text, transition, audio), then answer for each technique: what
   word caused it, how many frames, what sound, and why the viewer keeps watching.
4. Write the steal list as numbered recipes with numbers, and list the reference's mistakes so the copy beats it.
