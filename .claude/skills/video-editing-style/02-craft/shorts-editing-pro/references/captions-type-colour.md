# Captions, type and colour

## Caption system (default: Tharun word-pop, measured)

**Beats**
- One beat per word.
- Join short glue pairs ("in the", "he built"). Names and numbers stay alone. At most 3 words on screen.
- The in-point is the word's first frame, from the envelope onset (not raw ASR). It may be up to 1 frame late, never early by more than 0.1 s.

**Look**
- White heavy sans, sentence case, punctuation kept.
- Soft shadow: 0 5 px 12 px rgba(0,0,0,.8), plus a 34 px blur at 50 %. No box, no outline.

**Animation**
- Hard pop at final size, or a 3-4 f scale 1.15 → 1.
- Optional: the accent keyword flashes the accent colour, then settles to white over about 8 f.

**Stacks** (about one every 4-6 s, on the last phrase before a cut)
- Small lead (0.72x) over a BIG keyword:
  - 1.75x for up to 5 letters;
  - 1.45x for 6-8 letters;
  - 1.30x for 9 or more letters;
  - never wider than 900 px.
- Then a small trailer. Reserve the stack's space from its first word so nothing moves.
- Lay out by ink metrics: the gap is max(10, 0.09 × lower size), so descenders never touch.

**Position and size**
- Centre at y about 1150-1300. Choose one value per video, below the mouth and above the platform UI.
- On a tight framing, use about 85-100 px at y about 1060.

**When captions leave**
- They hide while a giant behind-head word, a full-screen title or a kinetic scene is up. No two text systems at once.

**Bright B-roll**
- Add a soft radial shade graded into the clip behind the caption zone (target contrast ≥ 3.5:1). No caption boxes.

**Language**
- Captions are exactly as spoken. Telugu lines are written in English letters (Tenglish) and synced to the Telugu audio.

## Alternatives (per style)
- **Hormozi:** ALL CAPS, Montserrat Black or Archivo 800-900, 2-3 words, the spoken word highlighted in the accent (yellow/green); emoji pop on 1-2 words.
- **Iman:** lowercase Inter/Montserrat, each word going light → bold as it is spoken, one line.

## Type system (one font per role; change the pair every video)
- **Caption:** Inter Tight 800 (Tharun token), Inter Black or Tactic Sans Bold.
- **Hero/display:**
  - Archivo Expanded 900 (Akira stand-in) for 2-6 letter words;
  - Anton or Bebas Neue (condensed) for long words and numerals;
  - Tactic Sans Extended.
- **Meaning word:** EB Garamond Italic (one per video, at most).
- Use fonts only from the `fonts-and-colours` list, checking its "already used" table first.
- Expanded type eats width: "PARTIALLY" fits only at 132 px. Use the normal width for long words.
- Slams overshoot safe zones on frame 1. Scale from the cap top, and use smaller slam factors (1.05-1.07) for wide words.

## Colour
**Accent**
- One accent per video, changed every video. Used so far:
  - rose (17), saffron (16), volt lime #C8FF2E (18);
  - Tharun lime #D6FD00, navy and neon green.
- Never violet. Red/green only for semantic data.
- The accent lives on type, rims and light, never as a coloured world behind his cut-out.

**Grade for Deepak's room**
- Face Y 135-150. The lower wall darker (about 85-105), so face-to-wall separation is about +50.
- Skin hue about 50-58 degrees, slightly teal background, contrast 1.06-1.12, saturation +5-8 %.
- Vignette 0.3-0.4, fine moving grain about 0.05.
- "Brighter" must actually fire: check the face and the frame mean (target A-roll frame mean above 70), not just the curves.

**B-roll**
- Grade each clip with ONE level map per clip (never per frame), matched to the A-roll's black level and white point.
