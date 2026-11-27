---
name: event-map-reel-edit-style
description: Use when planning, editing, captioning, sound-designing or reviewing ANY 9:16 short - the event-map method (something new every 1.3 s, every visual caused by a word, every change has a sound) plus two measured styles - P13 two-tier kinetic talking head (small line + one big keyword, hidden jump cuts, speaker inside graphics, pedestal lists) and P14 faceless 2.5D documentary story (stills as dioramas, camera never stops, text only when the word is the picture) - and the RAW vs EDITED showcase wrapper. Holds the transition-by-meaning table, sync offsets, SFX grammar and a QC checklist.
---

# Event-map reel edit style (profiles P13 + P14, method for every short)

Learned 2026-11-22 from the "zip 2" analysis pack (5 reels, no video inside). This folder is the home; `pro-video-editing/profiles/P13-*.md` and `P14-*.md` only point here.

Labels: **(M)** measured in the pack data · **(O)** seen by Claude on the pack's sheets · **(C)** checked by Claude against the pack's transcripts / scorecards · **(S)** suggested for our edits, not rendered yet. Frames at 30 fps. W / H = frame width / height.

| Ref | Reel | Length | Speech | Profile |
|---|---|---|---|---|
| R0 | "Elon owns 20% of Tesla" finance explainer | 29.9 s | 163 wpm | = P12, already in `faceless-explainer-reel-edit-style` (same reel as zip 1) |
| R1 | "Remember your script" 3 tips, dark studio | 34.0 s | 224 wpm (C) | **P13** |
| R4 | Realtor / AI reel inside a RAW vs EDITED card | 35.6 s | 204 wpm (C) | **P13** + wrapper (P4) |
| R2 | Semmelweis hand-washing story | 40.9 s | 151 wpm (C) | **P14** |
| R3 | Russian scientist plague mystery | 42.6 s | 130 wpm (C) | **P14** |

## When to choose this style
| The video is... | Use |
|---|---|
| ANY short, any style | Sections 1-4 and 9 (three laws, event map, sync table, QC) on top of the chosen style |
| Talking-head tips / opinion / client A-roll that should look "heavily edited" | **P13** (section 5) |
| Story, history, news, mystery told by voice-over with no camera footage | **P14** (section 6) |
| Facts / money explainer with no footage | P12 `faceless-explainer-reel-edit-style`, not this |
| Portfolio post selling editing | Wrapper (section 7) + `pro-video-editing` P4 |
| Energetic word-pop talking head | `tharun-speaks-edit-style` stays the default; borrow devices from section 8 |

Read with `shorts-editing-pro` (entry point, safe zones, shortkit), `mistakes-to-avoid`, `fonts-and-colours`. Full recipes: `references/format-b-talking-head.md`, `references/format-c-faceless-documentary.md`, `references/transitions.md`, `references/devices.md`. Per-reel beat sheets: `references/reels/`. Looks: `references/pack/analysis/R*/contact_sheets/overview_1fps.jpg`; frame-numbered animation sheets in `.../evidence_sheets/`.

## 1. Three laws (true in all five reels) (M)
1. **Something new on screen at least every 1.3 s.** Longest quiet stretch 0.13-1.30 s; frozen frames 0.2-2.4 %.
2. **Every visual event is caused by a word.** Scene changes on sentence onsets, emphasis on the keyword, mode changes in breaths. The voice is the clock, not the music (R1: only 3 of 10 cuts on its beat grid).
3. **Every change has a sound** from a small vocabulary where each sound has one meaning (section 4).

## 2. Event map (goes into PLAN.md as the shot table)
One row per event: `t | VO words | picture / transition | device | camera | text | SFX`. An event = transition, device changing state, text appearing, or a camera accent.
- Word budget = seconds x wpm / 60: 35 s is about 75-88 words faceless, 120-130 talking head.
- Voice first, then word timestamps, then the map. Check: no gap over 1.3 s; in the hook one event every 0.6-1.0 s.
- Build order: camera moves, transitions, devices, text, SFX, mix (text and SFX last: they snap to final word timing).
- Story spine: hook claim (ends 2.1-3.4 s) → reframe → proof in threes → **the turn at 60-77 % of runtime** ("But...", gets the biggest device of the second half; C: 62 / 63 / 73 / 77 %) → one-line payoff shown big → CTA no more than 12 % of runtime, still moving.
- Second half keeps at least 70 % of the first half's event rate (R4 dropped from about 10 mode switches to 4 and its last 4.5 s had nothing new).

## 3. Sync table (word → event) (M)
| Event | Timing against the word onset |
|---|---|
| Caption / small words | 0 to +2 f |
| Big keyword | start 6-8 f early and settle ON the word, or start on the word and finish in 7-10 f |
| Text that is the picture (name, date, number) | 0 to +4 f; typing starts about 10 f early so it ends on the word |
| Scene change | within -0.22 / +0.25 s of a sentence or clause onset; long moves peak on that sentence's key word |
| Mode change (speaker ↔ graphic) | in the breath, +50 to +300 ms after the phrase; return on the next phrase's first word |
| Emphasis hit (punch, icon drop, circle, boom) | on the keyword ±3 f |
| SFX | within ±3 f of its picture event; ticks 1-2 f before a word swap |
| VO pause of 0.5 s or more | must carry a move + a sound |

Hook (first 3.5 s): voice on frame 0, motion by frame 5, readable text by 1 s, 3-5 state changes each tied to a word of the first sentence, 70 % of the hook move in its first 0.7 s, exit on the biggest contrast change of the first 10 s (luma flip, beat drop, shrink into a UI).

## 4. Sound grammar (M, measured not heard)
| Sound | Spec | Means |
|---|---|---|
| Tick / click | 30-130 ms, 7-11 kHz | small event: word swap, type-on, material change |
| Whoosh → boom | 0.46-0.8 s, wide stereo, falling about 7 kHz → 500 Hz | change of place or world; peak on the cut |
| Sub boom | mono 20-80 Hz, 0.5-1 s | a meaning word (died, dropped) or an object landing |
| Bright hit + riser | hit on the first flash frame, riser peaks 4-10 f before | flash transitions |

Density 5-10 distinct SFX per 10 s. Music at least 12 dB under the voice (R1's bed was only 3 dB under: do not copy). Let the floor fall toward the moral; CTA cut on the quietest moment. Master -14 LUFS, true peak -1 dBTP or lower (all five references peaked hotter: do not copy).

## 5. P13 Two-tier kinetic talking head (R1, R4)
- **Job list:** R4's RAW panel is frame-locked to the EDITED one with the same grade and the same 11 jump cuts (M), so "edited" = captions + reframes + composites + cutaways + cut-hiding transitions + about 34 SFX.
- **Three modes**, switched about every 2.5 s, always in a breath: speaker full frame + captions (42 %), speaker composited into graphics (33 %), full-screen graphic or metaphor cutaway (23 %) (M, R4).
- **Two-tier caption:** a small sentence-case line carries the sentence, ONE big keyword per group is the reward; 3-9 words per group, about 1.3 s, clears in 1 f. Sits on the chest (0.56-0.74 H), never on the face, in front of hands. R1: one heavy sans, keyword 2.3x the small words, tight tracking, lines overlap. R4: small line types on at about 1 char / f; keyword in caps tracks in from wide letter-spacing over 6-8 f starting about 8 f early.
  - (O, Claude, sheet f736-756) R4's strongest threat word ("WORSE") does not track in: its letters arrive one at a time, about 4 f apart, each rising into place (about 16 f in all). Use this letter stagger once, on the worst-news word.
- **Colour = role:** gold `#E8A64E` topic / opportunity, red `#DA1E34` threat, white + orange bar wipe = argument pivot ("But the crazy thing is"). One accent underline in R1 (cyan `#2EC0D7` brush, drawn in 5-6 f).
- **Camera:** hook push-in x1.6 from f5 to f55 then hold; list zoom-bumps +7 to +15 % in 6-8 f, 1-4 f before each label; breathing pull-outs -2.5 to -3.2 %/s on tight shots; a new framing (at least 15 % different) after every hidden cut.
- **Hide the jump cut:** push-through (out 1.0 → 1.26x in 12 f, cut, in 1.35 → 1.0x in 16 f, sub boom on the cut), a graphic laid over the cut, or a 5-frame strobe (photosensitivity risk: at most one burst).
- **Devices** (`references/devices.md`): hook shrinks into a search-bar UI that types the spoken question; identity sandwich (speaker / crowd / giant title / brand backdrop); 3D topic object rising behind the head; metaphor cutaway of 2.6 s or less with captions moved to the top band; list as pedestals (icon drops on its keyword ±4 f, label printed on the pedestal); live video card on a white canvas; dim-and-overlay for idioms; mascot pun on the payoff adjective.
- **Luma flip:** R1 cuts from the dark set (luma 12) to a pure white canvas on the hook's last word and again at the turn (26 s) (M + O).

## 6. P14 Faceless 2.5D documentary (R2, R3)
- Slow serious voice (130-151 wpm, sentence gaps 0.2-1.0 s) over stills built as layered dioramas: blurred foreground edge → cut-out subject → props → blurred plate with 1.3-2.5x overscan. **The camera never stops** (frozen frames 0.5-1.2 %, frame change 3x a talking head).
- House move on every still: start 1.3-2.5x and tilted 15-30°, ease out to level over 1.3-2.5 s. Fly-back entrance (3x → 1x in 12 f + sub boom) at most twice per reel.
- Scene changes are moves, not cuts (R2: 2 true content cuts in 41 s): window zoom-through, light iris, object iris born where the next idea comes from, spin-portal, blur-rotation, macro-texture bridge, vertical whip, card push-up, live-to-print pull-back, keyhole hold. Recipes: `references/transitions.md`. Pick by what changes (place, time, cause → effect, live → evidence).
- **Text as object, no captions:** text appears only when the word IS the picture, printed on a surface in the scene. Three voices: verdict = heavy extruded 3D caps with one red word; data = typewriter or condensed caps (date card typed at about 1.9 f / char with a trailing red underline); archive / moral = bold italic serif, one word at a time.
- Devices: red name pill on the chest; highlighter (18-20 f per line) → hand-drawn red circle around the number → x1.35 punch; graph pair (red rising line with a camera chasing the pen, later a green falling line that floods on "dropped"); twist word stack in a black void; single-word moral under a spotlight after a hard luma flip (31 → 203).
- Colour script: luma flips of more than 80 levels at act boundaries; saturated emotional scenes alternate with near-mono evidence scenes; red = danger, green = life, B&W = death / past / doubt; a static halftone screen over every plate as glue.
- Sound: no music; sub drones as score; the section 4 grammar.
- Always add one line of verdict caps in the hook so sound-off viewers get the premise (R2 showed no text for 4.5 s).

## 7. RAW vs EDITED wrapper (R4 layout) (M)
At 1080x1920: static `#E6E6E6` card; EDITED panel 9:16 at 55 % of the width, right and in front, radius about 21 px; RAW panel 79 % of its height, behind and left, about 24 % hidden; bold "RAW" / "EDITED" labels above; footer "DM FOR WORK". Nothing moves outside the panels. Beat it (S): larger panels so captions stay readable, show the truly raw take, add the handle.

## 8. Borrow in our talking-head shorts (S)
- Fill the PLAN.md shot table as an event map and run the 1.3 s gap check before building.
- One keyword per caption group, coloured by role (opportunity / threat / pivot), never by decoration.
- The turn ("But...") is planned first and gets the biggest device of the second half plus a light-leak or luma flip in the pause before it.
- A list becomes pedestals or zoom-bumps, not bullet cards; a number in a source gets highlighter → circle → punch; a named thing gets an object behind the head.
- Every jump cut is hidden under a move, a graphic or a new framing of at least 15 %.
- Every VO pause of 0.5 s or more carries a move and a sound.

## 9. QC before delivery (adds to `shorts-editing-pro/references/export-qc.md`)
- [ ] Scorecard run: `python3 02-craft/event-map-reel-edit-style/tools/score_reel.py <render> --words <N>`; every LOOK line gets a fix or a written reason.
- [ ] Every overlay spell-checked against the spoken words (all five references shipped a typo: "scipt", "DRAMATICALY", "its already").
- [ ] Longest quiet stretch 1.3 s or less; hook readable with sound off by 1 s; no dead first frames.
- [ ] Each transition within -0.22 / +0.25 s of a sentence onset; each emphasis within ±3 f of its word; each scene change has a sound.
- [ ] Turn at 60-77 % carries a major device; second half at least 70 % of the first half's event rate; CTA 12 % or less.
- [ ] One signature transition used 3 times at most; fly-back 2 at most; no more than 3 flashes per second.
- [ ] -14 LUFS ±1, true peak -1 dBTP or lower.
- [ ] No news-brand logos on generated headlines, no AI image passed as an archive photo, no borrowed trademarks (R3 and R4 did this; also `mistakes-to-avoid` I).

## 10. House rules win
**Captions:** `my-editing-rules` section 9 says keyword captions only, never a running transcript (English or Telugu). P13's small sentence line is a running subtitle, so in our edits the small tier is a 1-3 word lead-in to the keyword (as in the Tharun stacks), not the whole sentence, unless the user asks for full captions. Fonts for these styles: `fonts-and-colours/assets/fonts/`.

Not copied from the references: captions on the chest still stay inside the `shorts-editing-pro` safe zone and size limits (R1's 2.3x keyword is above our 1.75x cap; R1 white on a light shirt was 2.35:1, add a shadow); R1's chapter cards only repeat the spoken word, so give a card a number or picture or skip it (`mistakes-to-avoid` J on flat cards); keyword fades from 35 % opacity (use scale or tracking); 15 fps sections; strobe bursts; hot true peaks. Study only: never reuse the references' footage, art or scripts.

## 11. Tools
- `python3 tools/score_reel.py VIDEO [--words N] [--crop W:H:X:Y] [--json out.json]`: the scorecard, working on this Mac since 2026-11-22. It wraps the pack's `reel_metrics.py` (unchanged): supplies ffmpeg (imageio binary) and an ffprobe stand-in, scores a temporary 30 fps copy when the render is 60 fps (the thresholds assume 30 fps), and takes the word count from our own transcript (`--words`) for wpm. About 20 s for a 33 s short. `--transcribe` still needs `faster-whisper` (not installed; not needed with `--words`).
- `bash tools/frame_sheets.sh VIDEO OUT.jpg START_S END_S FPS COLS ROWS TILE_W`: frame-numbered sheets (label = frame at 30 fps numbering); falls back to the imageio ffmpeg. Use 30 fps across a transition, 10-15 fps across a text animation.
- Reading the scorecard: "SFX events per 10 s" is measured only when the mix is wide (side / mid 0.2 or more). "SFX on cut" counts an airy 6-16 kHz onset within 0.10 s of each detected hard cut; a hi-hat bed inflates it, so confirm by ear.
- First baseline, 17. Embarrassment Short (60 fps, scored on the 30 fps copy): PASS frozen frames 0.2 %, longest quiet stretch 0.60 s, -14.1 LUFS, -1.3 dBTP. LOOK quiet-frame share 12.6 % (refs 9 % or less) and an airy sound on 11 % of 19 detected cuts (refs 57-86 %). Mix near-mono (side / mid 0.14), so SFX density was not measurable. (S) next short: an airy sound on every visible cut and SFX spread in stereo, checked by ear.
- Reference ranges: `references/pack/CROSS-REEL.md`.
- First render in this style, 22. Grayscale Tip (2026-11-22, P13, Telugu, 58.35 s): all lines PASS (static 0 %, quiet stretch 0.83 s, quiet frames 8.7 %, -14.4 LUFS, -1.3 dBTP, 190 wpm, airy sound on 85 % of 26 detected cuts). Lessons: the cut line needs a SHARP airy sound (slow whooshes scored 58 % on the first run); a voice + SFX master with no music bed stays near-mono (side / mid 0.10), so the SFX density line is not measured; the tool detects cutaway edges, not his jump cuts. Kit pieces and the builder checks are in `shorts-editing-pro/LEARNING-LOG.md` (entry 22) and `edited videos by claude/22. Grayscale Tip/code/`.
