# P2 Editorial Red Studio (Hera recreation, nikhilmotion.vlc)

Refs: 32ec48946f60 (V), screenshots 24-26, 28-30. Use for: personal-brand intros, agency hiring/sales reels, founder "who I am" reels on a light background.

## Look
- Light grey/white seamless studio, subject seated wide and centred (lots of headroom for type).
- Colour: crimson/red family only (#B0001E to #E0102A, light pink pixels) on white; AI-generated or stock "fantasy" inserts (astronaut in clouds) with red UI accents.
- Giant **heavy italic display words** in red gradient (Hera, CEO, Marketing Agency, Clients), sometimes behind the subject (matte), with small italic sans lead words ("My name is", "Who can edit our").
- Photo cards with red rounded frames and red pill tags ("of", "personal", "kylie"); stacks of social-post cards fanning in; phone frame card with type-on text.
- 8-bit pixel squares, red light/energy streaks, halftone dot rings.

## Motion recipe (30 fps) (V unless E)
- Intro glitch 3 f (dark, RGB split) -> bright studio.
- Lead words appear word by word with small position jitter, 1-2 f each.
- Display word letter-stagger ~3 f per letter; finish on the spoken word.
- Transition A: red energy streaks up across subject (6 f) -> halftone ring expands from centre (5-13 f) revealing next element.
- Transition B: red laser sweep 2 f -> cut to blurred next scene -> halftone ring outward ~13 f.
- Cards: pop with scale overshoot and slight rotation; stacks fan with 2-3 f stagger (S).

## Rules
- Every spoken noun that is a name, title or brand gets the giant word; connective words stay small.
- Keep the red family; no second accent.
- Speech here 205 wpm: text must be legible in 0.5-0.8 s, so max 2 big words at once.
