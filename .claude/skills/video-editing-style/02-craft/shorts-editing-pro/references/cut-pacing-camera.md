# Cutting, pacing, camera, transitions

## Cut to the voice (raw take)

1. **Find speech runs.** Use `silencedetect n=-38dB d=0.06` or the analyze_raw `speech_runs`. ASR word times are often a word early on Deepak's voice. Confirm cut points on the 10 ms RMS envelope, not ASR.
2. **Choose keeps.** Keep the best take of each line; the last clean take usually wins. Drop:
   - stumbles and false starts;
   - "uh/um", "like", "now like";
   - repeated lines.
3. **Gaps.**
   - Trim pauses to ≤ 0.3 s.
   - Keep 0.10-0.15 s breaths at commas; cutting every gap to zero sounds rushed (ONL).
   - Cut points sit in room tone, about 1 frame (17-40 ms) before the next word's onset.
   - Use 8-10 ms audio crossfades.
4. **Splices from another take:** match the level (a splice was 8 dB quieter in 18; it got +4 dB) and check with sample-level NCC.
5. **Never** speed-ramp, time-stretch or re-pitch the voice.

## Rhythm (measured)
- **ref61 (smooth short):**
  - cuts every about 1.1 s (0.25-2.4 s), each on a word boundary (median 0.02 s before the next word);
  - 3.9 words/s;
  - one complete thought.
- **Tharun A:**
  - a cut about every 2.0 s (0.56-8.5 s), and a caption change every 0.25 s;
  - full-screen graphic scenes take about a third of the runtime, at 1.1-3.4 s each.
- **Web (ONL):** a visual change every 2-5 s, with the interval varied.
- **Rule:** nothing static for more than 2.5 s. Long shots stay alive with a push, caption stacks or a card swap.

## Camera on his footage (shorts allow keyframes)

**Jump-cut size change:**
- Alternate about 1.00-1.12 with 1.22-1.40 scale.
- Anchor on the eyes: keep the eye line at screen y about 640-720 of 1920.
- Head top stays at y 84 px or lower.

**Moves:**
- **Hook push:** 1.00 → 1.16 over about 40 frames at 60 fps, ease-out, then hold with drift.
- **Slow push:** 1-3 %/s on holds over 1.2 s. Split long moves (out3 off the cut, in2 into the end) so no part is motionless.
- **Zoom punch:** 4-6 frames, expo-out, +12-20 %, on the hero word's first frame. An optional 2-frame scale overshoot is the only "shake" allowed.

**Source quirks:**
- Source 1440x2560 means a 1.333x oversample, so zooms to about 1.33 stay sharp.
- A 1080p source above 1.25 starts to soften: add light sharpening.
- Deepak's 60 fps files are 24p with 2:3 pulldown. Matte or motion comparisons must use distinct pictures.

## Transitions (ranked, use sparingly)
| Transition | Frames | Use |
|---|---|---|
| Hard cut | 0 | default, about 85 % of cuts |
| Negative flash | 2 (invert + desat), then 1 black | 1-3 section turns |
| White flash | 1-2 | in or out of a B-roll burst, pair with a hit |
| Blur-zoom | 3-5 | into a hero B-roll shot or a tight punch |
| Whip (horizontal motion blur) | 4-6 | between B-roll in a montage, same direction each time |
| Freeze + B&W | hold 0.3-0.6 s | open-loop or "pause" beat |
| Speed ramp | B-roll only | 1.0 → 0.35-0.4x → 1.3x on action clips; freeze on a whole source frame |

**Never use:**
- dissolves between talking cuts, or preset slides and spins;
- glitch more than 3 times a minute;
- flash trains (more than 1 flash per beat; strobe risk).
