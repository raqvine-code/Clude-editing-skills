# Format B — Talking head with kinetic captions and graphics (and Format D wrapper)

Sources: R1 (tips reel, 34.0 s, 224 wpm, 11 shots) and R4 (realtor/AI reel inside a RAW vs EDITED showcase,
35.6 s, 204 wpm). Full evidence: `reels/R1-talking-head-tips.md`, `reels/R4-talking-head-showcase.md`.
Frames at 30 fps; W/H = frame width/height (for R4, the EDITED panel).

## 1. What the edit is for

The speaker carries the trust; the edit carries the pace. R4's RAW panel turned out to be frame-locked to the
EDITED one, with the same grade and the same 11 jump cuts, so everything the viewer perceives as "edited" was
added on top: captions, reframes, composites, cutaways, transitions that hide the cuts, and ≈34 distinct sound effects.
That is the job list for this format.

## 2. Three modes and their rhythm

| Mode | R4 share | R1 share | Use when |
|---|---|---|---|
| Speaker full frame + captions | 41.7 % (14.8 s) | 72 % | the speaker is the proof: opinions, delivery, warmth |
| Speaker composited into graphics | 32.7 % (11.6 s) | — | the line names a thing: brand, crowd, place, tool |
| Full-screen graphic / metaphor cutaway | 23.2 % (8.3 s) | 18 % white canvas + 10 % chapter cards | an idea needs a picture: lists, metaphors, data |

R4 ran 14 mode stretches (13 switches, average stretch 2.5 s). Keep the switch rate in the second half within 70 % of the
first half's (R4 fell from ≈10 to ≈4 and its last 4.5 s had nothing new). Put every switch in a breath:
+50–300 ms after the phrase ends, returning on the next phrase's first word (R1).

## 3. Captions (two-tier)

Why it works: the small line carries the sentence for sound-off viewers; the big word is what the eye lands on
and remembers. One keyword per group gives a rhythm of "reward" beats every ≈1.3 s.

| Spec | R1 | R4 |
|---|---|---|
| Font | one heavy geometric sans (≈Montserrat/Gilroy ExtraBold, guess) | extra-bold geometric caps for keywords |
| Small line | ≈2.3 % H, white, full on in 1–2 f | cap ≈3 % W, white, typed at ≈1 char/f |
| Keyword | ≈5.4 % H (2.3× the small words), ramps 35 % → 100 % opacity over 7–10 f | cap 5–7 % W (10–11 % for emphasis), tracks in from +100 % letter-spacing over 6–8 f, starting ≈8 f before the word |
| Position | centred at 0.50 W, block 0.56–0.74 H (torso), never on the face | keyword centre 0.63 H ±2.5 %, staggered 3-line ladder (left / indent / right tail); moves to 0.12–0.21 H when a graphic owns the centre |
| Group | 3–9 words (median 6), ≈1.33 s, lines overlap ≈5 px, clears in 1 f | median 5 words; 19 cards carry 96 of 121 words |
| Sync | first frame median +0.8 f after the word (IQR −2 to +2.6) | small words median −1 f |
| Accent | cyan `#2EC0D7` brush underline under the last hook keyword, drawn in 5–6 f, 3 f after the pop | colour codes (below) + 15 px orange bar wiped under pivot lines |
| Depth | always in front of hands | in front; behind the speaker only for set titles |

Colour code (R4): gold `#E8A64E` (highlight `#F4C976`) = topic or the viewer's opportunity; red `#DA1E34` /
`#E5001A` = threat or out-group (AI, HERE, WORSE, MOST AGENTS); white + orange bar = argument pivot. Keep it
consistent (R4 broke it once: FALLING BEHIND in gold, WORSE in red).

Fix the references' caption faults: start keywords at ≥ 60 % opacity or use tracking/scale instead of a 35 %
fade; keep reading order intact in stacks; 2–3 px dark stroke or 30 % shadow on light clothing (R1 was 2.35:1);
the caption text must match the spoken words (R4 showed "this shift" for "the shift").

## 4. Camera on the speaker

- **Hook push-in** (R1): open on the widest framing; eased digital push ×1.57–1.65 from f5 to f55, peak 3.2 %/f at
  f13–14, 70 % done by f20; then hold still.
- **List zoom-bumps** (R1): +13, +15, +7, +12 % in 6–8 f, each starting 1–4 f before its label; ≈×1.6 total over
  2.8 s; hold still between bumps.
- **Breathing pull-outs** (R1): −3.1 %/s over 3.7 s, −2.5 %/s over 5.2 s, −3.2 %/s over 6.2 s on tight shots,
  easing to a stop. Warm practicals at the frame edge slide in and out as free motion.
- **New framing after every hidden cut**: ≥ 15 % scale difference (R1 chapter-card returns).
- **Zoom-through** (R4): out 1.0 → 1.26× over 12 f accelerating with motion blur; cut; in from 1.34–1.36× settling
  to 1.0 in 16 f (36 % of the remainder every 2 f); sub boom on the cut.
- **Dim-and-overlay** (R4): speaker to ≈46 % brightness and defocused over 30 f; a literal pun of the idiom on top
  ("upper hand" = a hand) without typing the idiom.

## 5. Composites and cutaways (R4 devices; recipes in `devices.md`)

- **Hook as an app screen**: whole plate shrinks 1.0 → 0.35× over 14 f (f34–48) into a dark chat-search UI; the
  spoken question types into the search bar at speech pace (≈22 chars/s).
- **Identity sandwich**: rotoscoped speaker / stock crowd / giant title (cap ≈19 % W, bleeding off both edges,
  behind heads) / brand-colour backdrop, revealed on the identity word.
- **Object behind the head**: a 3D topic object rises from behind the speaker over ≈20 f with rim light, under a
  1.0 → 1.19× push over 48 f that ends in a transition.
- **Metaphor cutaway ≤ 2.6 s** with a background colour drift (neutral → red across the sentence).
- **List → pedestals**: a pedestal per item rises in 12–16 f; the item's icon drops on its keyword (±4 f) with a
  boom + hit; the label is printed on the pedestal instead of a caption.
- **Live video card** (R1): the speaker keeps talking inside a rounded card (r ≈ 3 % W) that settles from 0.61 W to
  0.52 W in 3 f, with a dark crescent ribbon growing behind it in 6 f; push left ≈1 W in 7 f to the next metaphor.
- **Mascot pun** (R1): on the payoff adjective ("robotic"), a 3D character flies up from below with rotation over
  ≈12 f with a pop SFX.

## 6. Transitions in this format

- Hide jump cuts (R4 hid 10 of 11): zoom-through, 5-frame strobe (2 flash, 1 normal, 2 flash, cut; inverted or
  +90 % exposure; the 7-frame hook version lifts mean luma ≈60 → 170), or a graphic laid over the cut.
- Luma-flip hard cut from the dark set to a pure `#FFFFFF` canvas on the hook's last syllable (R1, luma 12 → 255,
  with the beat drop).
- Chapter cards (R1): one dark `#020308` clip with slow 3D ribbons, restarted from frame 0 each time, small label +
  big word at ≈0.45–0.50 H; 53, 21 and 29 f. They added no information (the voice said "First/Second"); give them
  a number or a picture next time.
- Light-leak chapter break (R4): 7 f warm ramp (luma 49 → 195), 2 white frames, 1 residue frame, in the 0.22 s
  pause before "But the crazy thing is…".

## 7. Sound in this format

- R4: ≈34 distinct stereo SFX (9.5 per 10 s), an event within ±0.1 s on 11 of 12 transitions; low riser peaking 4–10 f before a
  flash; beatless tonal bed ≈24 dB under the voice; bass removed 31–34.5 s before the final hits.
- R1: beat bed (≈133 bpm hats) only ≈3 dB under the voice — duck it ≥ 12 dB; kick removed 1.0–3.3 s and the full
  beat dropped 27 ms after the first cut; SFX sparse and loosely placed (only 7 matches between 20 visual events and its stereo
  transients) — mark every cut.
- Both: −14.1 / −14.7 LUFS; true peak −0.8 / +2.9 dBTP — master to ≤ −1 dBTP.

## 8. Grade (R1 lighting recipe; R4 shows the edit added none)

Background crushed to ≈`#040004`; orange hair rim `#DC8438` one side, steel-blue fill `#465C70` the other; skin
≈`#9C7668`; warm bulb practicals `#FDEE96` out of focus in the top third; white canvas scenes pure `#FFFFFF`.

## 9. Format D — the before/after showcase wrapper (R4)

Layout at 720×1280 (scale ×1.5 for 1080×1920): static `#E6E6E6` card; EDITED panel 394×697 (9:16) at x 285, y 290,
55 % of the width, radius ≈14 px, in front and right; RAW panel 79 % of EDITED's height, behind and left with ≈24 %
hidden; both centred on y = 640; labels "RAW" 34 px and "EDITED" 37 px bold above each panel; footer "DM FOR WORK"
with an 83 px heavy "DM" and a two-line bold italic "FOR / WORK"; nothing else moves outside the panels.

Why it sells: the RAW panel is a live control sample (same words, same frame), so every difference is credited to
the editor; the eye ping-pongs between plain and busy, adding dwell time; the client's own hook carries the
retention. Beat R4 by: showing the truly raw take (pauses, bad takes) and its runtime, making the panels larger so
captions stay legible (R4's small line was ≈11 px tall), and adding a name or handle.
