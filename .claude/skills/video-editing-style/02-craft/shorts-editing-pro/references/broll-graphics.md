# B-roll, PNGs, motion graphics

## B-roll

**Coverage and timing**
- 25-50 % of runtime, in bursts of 0.6-2.5 s.
- Enter on the noun's word frame or up to 0.3 s before.
- Show his face for emotional lines; use B-roll for concrete nouns and actions.

**Matching**
- Match the line literally or metaphorically, with motion that carries the verb: dive = "all in", run = "move", crowd = "excitement".
- Never reuse a clip in one short.

**Sources**, in order:
1. `broll-library/catalog.md` (Pro-tagged only).
2. Pexels or Mixkit or Coverr at 1440p+, free licence. Log URL, licence and size in `assets/_urls.tsv` and CREDITS.
- The Pexels API needs a key. Use direct video file URLs from a page fetch, or Mixkit's direct MP4s.

**Prep**
- Center-crop to 9:16, then scale to 1080x1920 (or 1.04-1.08 for a push).
- Trim to the most active part; one level map per clip.
- Optional speed ramp. Freeze only on a whole source frame (time × fps is an integer).

**Montage**
- 3-4 clips of 0.5-0.9 s with whips in the same direction, on a list of verbs or adjectives.

## PNGs, icons, proof
- `png-library/catalog.md` first. Logos only when named.
- Any real document, tweet or number must be the real capture with a source line (`text-highlight-match-cut`). Never fabricate.
- Pop in: scale 0.5 → 1, back.out(2), 0.3 s, with a soft pop SFX. Place it in the empty space beside the head, never over the eyes.

## Motion graphics that read as pro
- **Behind-the-head giant word** (needs a person matte; check hair edges):
  - Condensed or expanded caps, 1-3 times per short.
  - Top third of the frame, with the head overlapping the middle letters by at most 20 % of cap height.
- **Kinetic word fill / liquid / counting number** for the single hero idea:
  - Numbers count up over 20-30 f, ease-out.
- **Freeze-frame + B&W + label:** for a pause or "see what happens" beat.
- **Light-rise on a turning point:** +0.2 stop and a warm pool on the subject, kept for the rest of the video (18).
- **No:**
  - flat black cards with thin line art;
  - clip-art;
  - arrows across footage;
  - progress rails on footage;
  - tilted cards;
  - mock-ups of his own face in a phone.
- **Every MG element:**
  - blur-in 8-16 px → 0;
  - enters fast with overshoot, exits faster;
  - idle motion if it stays over 3 s;
  - has a sound.
