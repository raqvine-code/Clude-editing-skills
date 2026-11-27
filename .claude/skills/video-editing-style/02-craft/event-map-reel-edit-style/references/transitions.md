# Transition library (measured recipes)

Frames at 30 fps; px at 720 W unless marked. "Out" = outgoing shot, "in" = incoming shot. Every transition gets an
SFX (section 10 of GUIDE.md). Choose by what changes (GUIDE.md section 9), then build from the recipe.

## Hide-the-cut (same scene, same speaker)

**Zoom-through cut** (R4) — out: push 1.0 → 1.26× over 12 f, ease-in (accelerating) with motion blur; hard cut; in:
start at 1.34–1.36× and settle to 1.0 in 16 f, expo-out (≈36 % of the remaining excess removed every 2 f). Sub boom
peaking on the cut. Hides a jump cut by making the cut part of a move.

**5-frame strobe** (R4) — 2 flash frames on the out shot (inverted, or +90 % exposure with bloom), 1 normal frame,
2 flash frames, cut (0.17 s). Bright hit SFX on the first flash frame, riser peaking 4–10 f before. R4's 7-frame hook
version (f0–7) lifts mean luma ≈60 → 170 and swings brightness 4 times in 0.23 s: a photosensitivity risk. Use one
burst at most, or ≤ 3 flashes per second.

**Graphic over the cut** (R4) — let a pedestal rise, a chess scene or a full-screen cutaway cover the A-roll cut;
return at a new framing (≥ 15 % scale change).

## Speaker ↔ graphics

**Luma-flip hard cut** (R1) — from the dark set (median luma ≈12) straight to a pure `#FFFFFF` canvas on the last
syllable of the hook; no flash needed, the jump is the flash. Pair with a beat drop (full beat back 27 ms after the
cut).

**Live video card** (R1) — the speaker keeps playing inside a rounded card (r ≈ 3 % W, soft shadow) that settles
from 0.61 W to 0.52 W in 3 f, ease-out, while a dark crescent ribbon grows behind it in 6 f as a leading line.

**Canvas push** (R1) — move between metaphors on the white canvas with a ≈1 W push-left in ≈7 f, decelerating
(≈35 → 25 px/f at 720 W), stereo whoosh.

**Shrink into a UI** (R4 hook) — whole plate 1.0 → 0.35× over 14 f, ease-in-out with a slight bulge, landing inside
an app screen.

**Re-stage instead of cutting** (R0) — fade graphic and caption (12 f), scale the hero to ≈85 % and lower it, slide
the others in from the edges with motion and depth blur (20 f, ease-out).

## Chapter / section breaks

**Chapter card** (R1) — one dark `#020308` clip with slow 3D ribbons, restarted from frame 0 each time; small label +
big word centred at 0.45–0.50 H; text in 1–5 f; 0.7–1.8 s (R1: 53, 21, 29 f). Cut in 50–300 ms after the phrase
ends; cut back on the next phrase's first word at a new framing (≥ 15 % different). Give it information (a number,
a picture), not just a word the voice already said.

**Card push-up** (R3) — the next scene is a full-width rounded-corner card (radius ≈3 % W) sliding up, expo-out over
9, 8 and 14 f, first frame ≈10 % H visible; sub boom pre-lapping by ≈3 f; the card's content runs its own entrance.

**Light-leak, short** (R4) — 7 f warm leak ramp (luma ≈49 → 195), 2 pure white frames, 1 residue frame, inside the
pause before "But…".

**Light-leak flash, signature** (R0) — 10–11 f: bloom seeded on the hero object 2–3 f early → white core fills the
frame with rose `#E89898` / slate-indigo `#686888` edges and fine vertical fluted-glass lines → new scene ghosts
through for 1–2 f → its first frame is 1 f of horizontal scanlines. Use at act changes, same asset every time, ≤ 3.

## New place or time (faceless)

**Window zoom-through** (R2 hook) — composite the next shot inside a window or screen of the current plate; scale
8.5× over 44 f, peak +15 %/f on frame 4 of the move decaying to +0.5 %/f; radial blur for 6–8 f; whoosh starting
3 f before + 1.2 s sub. Lock it to the shock word.

**Light iris** (R2) — the next scene grows as a disc out of a light source in the current plate (a ceiling lamp):
white bloom rim, radius ×1.6 every 2 f, 12 f total; the outgoing plate fades toward white. Use on the hope turn
("until…").

**Spin-portal** (R2) — a 1 px dot in empty space grows to full frame in 16 f; out spins −25° with ease-in (−0.5 →
−8° per step); in starts ≈27° tilted and unwinds in ≈25 f. A soft drop shadow on the circle makes it read as a hole.

**Blur-rotation cut** (R2) — out: 5 f to full defocus with −4 %/f pull-out and +2.5°/f spin; hard cut; in: starts
blurred, continues the same spin direction at +0.9 → 0.3°/f, sharp by 6 f. For era or material jumps.

**Rotation-matched cut** (R3) — roll the out shot +20° with ease-in; cut to the next plate already rolled the same
way; un-roll with expo decay (1.9°/f → 0.4°/f over ≈20 f); click SFX on the cut.

**Macro-texture bridge** (R3) — hard cut to an extreme close-up of the next set's surface (red wood) for ≈8 f, then
pull back with a −40°/s counter-roll while the hero prop slides in over 12 f; descending whoosh-boom (2.4 kHz →
≈400 Hz) covers the cut.

**Vertical whip** (R2) — two tabletops on one tall canvas; tilt 15 f at ≈1240 px/s with vertical motion blur, the
next prop rotating in, mono sub at mid-whip. Good for "years later".

**Floor / pedestal wipe** (R2) — the incoming scene's dark foreground plane covers the frame from the bottom in 4 f,
holds black 3 f, drops away in ≈11 f; boom peaking on the black hold.

**Eyepiece wipe** (R2) — a microscope-eyepiece circle wipe over 21 f that finishes centred exactly on the spoken
word ("bacteria").

## Meaning-driven

**Object iris from the meaningful point** (R2) — birth the transition dot where the next idea comes from (between
the washing palms → the result chart; the glowing end of the green line → the twist). 14–15 f, exponential
(×1.35/f). Black dot for a dark incoming scene; glowing pinpoint with bloom (≈37 % of the frame white at peak) for a
bright one. Tick on the birth frame, boom on the fill.

**Shape insert on the verb** (R3) — a prop layer (coffin) between subject and plate rises from the bottom in 8 f and
lands on the verb ("died"); a new background texture irises open from the centre behind it in 5 f; B&W + bloom on
the next word.

**Live-to-print pull-back** (R3) — zoom out ×0.45 over 23 f to reveal the live shot is a photo in a newspaper frame;
desaturate in 7 f mid-move; blur-zoom ×0.78 over 6 f to reveal the hands holding the paper. Turns a person into
evidence.

**Mouth iris** (R3) — a red glow starts at the speaker's mouth 3 f before the question; a circle grows over 12 f
with light rays; saturation 24 → 154 in 7 f; the inner plate zooms 0.915 → 0.985 per frame.

**Keyhole hold** (R3) — whip-zoom on the key verb (6 f, boom); the same plate ×0.90 behind a rim-lit keyhole matte;
hold 1 s in silence; ease-in push (1.008 → 1.064 per frame) through the hole into the next section, click SFX.

**Invert flash** (R0) — 1 frame negative of the outgoing frame, then hard cut. Before the punchline.

**Object wipe** (R0) — a foreground object (a falling bill) fills the lens for 6–7 f; cut underneath it.

**Zoom-into-object** (R0) — a scene object flies into the camera over 8 f and covers the frame; reveal the next
scene behind it.
