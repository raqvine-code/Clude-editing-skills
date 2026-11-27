# Timing & Sound Design Guide

## Measured pacing (V)
| Profile | Shots/min | Median shot | Still frames* | Speech |
|---|---|---|---|---|
| P1 motion ads | 36-51 | 1.3 s | 47-65 % | none (music) |
| P2 Hera | 43 | 1.2 s | 29 % | 205 wpm |
| P3 podcast in card | 29-37 | 1.6-1.9 s | 81-88 % | 176-185 wpm |
| P4 results shell | shell 0 cuts | - | 92 % | 171 wpm |
| P5 explainers | 12-24 hard cuts (active-area detection) + many in-shot graphic changes | 0.7-4.3 s | 85-97 % | 150-213 wpm |
| P12 faceless explainer | 18 (9 scene changes in 29.9 s) | 3.0 s average, 1.3-4.3 s | 0.4 % (4 of 896, pack count) | about 179 wpm overall, sentence gaps 0.30-0.60 s |
| P13 two-tier talking head | 14-18 (R1 10, R4 8 visible hard cuts; R4 hides 10 of 11 jump cuts) | 3.1 s average (R1); mode switch about every 2.5 s (R4) | 2.4 % / 0.2 % (pack count) | 224 / 204 wpm |
| P14 faceless 2.5D documentary | 10-13 (R2 7, R3 9 hard cuts; most scene changes are moves) | one picture per sentence, about 2.5 s | 0.5 % / 1.2 % (pack count) | 151 / 130 wpm, sentence gaps 0.2-1.0 s |
*Frames with no visible change (frame diff <= 2/255). Low = constantly moving graphics.

## Sync rules (V)
- A key-word graphic lands 0.1-0.35 s BEFORE or exactly on the spoken word (Hera, Raj, 94a1). List items/pills may lag ~0.1 s (canvers).
- A letter-stagger word starts ~0.35 s early and completes on the word.
- Phrase-per-beat slides change on each phrase boundary from the transcript.
- Music-only ads: put entries/slams on audio onsets (f00: 50 % of events within 70 ms of an onset, 2.6x chance). Not every reference does this (fdf/4a6 at chance), so beat-lock is a style choice, not a rule.

- P12 (faceless, pack data): a short airy sound (6-16 kHz, 100-200 ms) sits within 0.2 s of all 9 scene changes; one sub boom (20-80 Hz, about 1.3 s, about 20 dB over the bed) under the biggest reveal; no audible music. The punchline cut lands about 10 f after its sentence starts (voice leads picture).
- Event-map pack (5 reels): nothing stays visually quiet for more than 1.3 s; sync offsets per event type and the tick / whoosh-boom / sub-boom grammar are in `02-craft/event-map-reel-edit-style/GUIDE.md` sections 3-4.

## Durations cheat sheet (30 fps)
Snap entry 2-4 f. Normal entry 5-8 f. Morph/branch 15 f. Card shrink / canvas pan ~40 f. Hold a statement 1-2 s. Behind-head word 1-2 s. Letter stagger 3 f/letter. Type-on 1 f/char.

## Sound (E unless stated)
- Reference loudness -16.6 to -12.4 LUFS integrated (V, platform reposts). For delivery follow the user's master rule (-14 LUFS, -1 dBTP) unless told otherwise.
- Motion ads: music-led; whoosh on smears/whips, tick/pop on sparkle and pill pops, riser into white-out, impact on keyword slam.
- Talking-head: voice first, music bed low and ducked; small UI clicks on cursor clicks and card pops; swoosh on panel slides.
- Source SFX/music from Mixkit / Freesound / Pixabay (user decision 2026-11-14).

## Editing theory stated in the references (V, transcript cab9807914a3)
"Stop cutting randomly and start cutting with the music": place cuts on beats, use the rise and fall of the song, match the energy of the track with the visuals (high BPM for high-energy sections).
