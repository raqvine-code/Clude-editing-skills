# P1 Glass Spotlight Motion Ad (aslaniedits family)

Refs: f00ae5949170 (V), 4a6cb105b501 (V), fdf671691d67 (V, pixel variant); screenshots 5, 6, 8-11, 15. Use for: 6-10 s brand/agency promos, motion-design ads, product value statements, music-only or short VO.

## Look
- Subject = clean cut-out person in a studio: spotlight on black floor (f00), navy seamless (4a6), crimson room (fdf), white seamless (screenshots 8-9). Subject is mostly still; motion lives in graphics.
- Behind the subject: a tall **rounded glass phone/card shape** (frosted, soft top highlight bar, thin rim). It frames the type.
- One accent colour per video: lime #C8F03C-ish (f00, screenshots), red (4a6 profits scene), orange (Claude scene). Everything else white/grey on dark, or dark on white.
- Decorations: yellow/lime "+" and "x" sparkles, comet light streaks, 8-bit pixel squares, 4-5 square "loading" bar, corner bracket marks, hand-drawn circle around a keyword, thought-bubble dots.
- Full-screen 3D object scenes between subject shots: glass icon tile with arrow, moss sphere in glass ring, task-card swarm (E: stock 3D renders / AE + Element 3D).

## Type (3-tier stack) (V)
1. Lead line: light/regular geometric sans, small (about 25-30 % of keyword cap height). "You're not", "More customers mean".
2. Accent word: script or serif italic, in the accent colour with glow (decays to white or stays coloured). "competing", "tasks".
3. Keyword: heavy/black sans, tight tracking, huge, ending in an accent-coloured full stop. "price." "value." "pay." "costs".
Free matches (E): lead = Inter Light / SF Pro; accent = Playfair Display Italic or a script like "Allura"; keyword = Inter Black / "Tactic Sans Extended Black" (already installed) . Pixel variant: "Silkscreen" / "VT323" / "Departure Mono".

## Motion recipe (frame counts at 30 fps)
- Open: subject blur-in 3 f; glass frame scale-in 8 f (expo out); sparkles overshoot pop 4 f; streak sweep 15-20 f.
- Text: lead types 1 f/char; keyword slams from side with motion blur 4 f; accent script writes 8 f with glow.
- Swap keyword (price -> value): old words smear out (directional blur) 3-5 f, new word in 2-3 f, circle stroke draws 10 f.
- Exit: staggered smear-off right (3 f stagger) -> scale-up blur 1-2 f -> cut -> next element whips in from left 3-4 f.
- Pixel variant: stepped (hold-frame) movement of white squares, 2 f per step; RGB displacement 3-4 f; corner brackets 5 f.
- Total build for one statement ~1.2 s, hold ~1-2 s, change every 1.5-2.5 s (shot median 1.3 s, 36-51 cuts/min).

## Sound
Music-only. Animations hit music onsets (V on f00: 50 % of events within 70 ms of an onset). Use whoosh on smears, soft tick on sparkle pops (E).

## Rules
- One statement per beat; never more than 6 words on screen.
- Keep the face clear; type sits above head or in the glass frame.
- Contrast flip between scenes (navy -> black -> green -> navy) is part of the pacing.
