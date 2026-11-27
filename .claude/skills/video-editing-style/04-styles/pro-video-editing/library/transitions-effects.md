# Transitions & Effects Library

Durations at 30 fps. "V" = verified frame by frame (see knowledge/observations-frames.md).

| ID | Transition | Frames | How to build | Evidence |
|---|---|---|---|---|
| X1 | Blur-in / rack focus | 3 f (snap) or ~8 f (rack) | Gaussian blur 40->0 px (snap) or 12->0 px (rack), ease-out; text waits until focus settles | f00 f0-f2, fdf f167-f170, 4a6 f184-f192 (V) |
| X2 | Whip / smear | out 1-2 f + in 3-4 f | outgoing: scale up + directional blur; cut; incoming slides from opposite side with motion blur (shutter 360) | f00 f137-f141, 7a74 f120-f124 (V) |
| X3 | Streak carry | 6 f around the cut | light streak crosses the cut point; zoom blur on outgoing 2-3 f | 4a6 f56-f62 (V) |
| X4 | White-out | 2-3 f | exposure up + blur to white, cut to next | 4a6 f182-f184 (V) |
| X5 | Pixel block glitch | ~10 f | white square stepping (2 f holds), grows over subject, RGB/pixel displacement 3-4 f, cut to black | fdf f63-f73 (V) |
| X6 | Glitch intro | 3 f | dark, blurred, RGB-split frames before the first clean frame | Hera f0-f2 (V) |
| X7 | Bar wipe reveal | 3 f | full-height white bar sweeps across, new phrase behind it | Raj f91-f93 (V) |
| X8 | Energy streak + halftone ring | 6 + 5-13 f | red streaks up the frame, radial halftone ring expands from centre revealing next element | Hera f36-f47, f145-f160 (V) |
| X9 | Frame shrink-to-card | ~1.3 s | whole shot scales into rounded card (radius ~4 % width) with stroke + glow, ease-in-out | 94a1 f9-f87, 1ef4 (V/S) |
| X10 | Canvas pan | ~1.3 s | elements laid on one long canvas; camera moves sideways at near-constant speed | 1ef4 f84-f124 (V) |
| X11 | Shape morph | ~15 f | bar grows into card, which becomes the next scene | 7a74 f126-f140 (V) |
| X12 | Hexagon mosaic | ~12-15 f | hex grid matte reveals next shot from one side, cells semi-transparent mid-change | 94a1 f1855-f1885 (V) |
| X13 | Punch-in with motion blur | ~10 f | scale 1.0->1.1, motion blur; often right after a behind-head word | 94a1 f641-f651 (V) |
| X14 | Hard cut | 0 | the default inside talking-head sections and inside showcase cards | all (V) |
| X15 | Light-leak flash with scanline landing | 10-12 f | seed a bloom + thin horizontal streak on the hero object 1-2 f early; white core fills the frame with rose `#E89898` / slate-indigo `#686888` soft edges and a fine vertical line texture on the leading edge; new scene ghosts through; LAST frame = new scene under horizontal scanlines for 1 f. Act changes only, same leak each time, 3 at most | P12 pack f331-f340, f444-f455, f704-f714 (V) |
| X16 | Object wipe | 6-7 f | a foreground object already in the scene (falling bill) grows until it fills the lens, out of focus; cut underneath it | P12 pack f541-f547 (V) |
| X17 | One-frame invert | 1 f | negative of the outgoing frame for exactly 1 f, then hard cut; right before the punchline | P12 pack f665 (V) |
| X18 | Zoom-through | 8-10 f | an object in the scene flies into the camera, covers the frame for about 5 f, next scene is behind it | P12 pack f838-f848 (V) |
| X19 | Re-stage (no cut) | 30-35 f | fade text + graphic 12 f, scale the hero to about 85 % and lower it, slide the other subjects in from the frame edges in 14-20 f with motion blur | P12 pack f234-f266 (V) |
| EM | Event-map pack transitions, chosen by what changes: push-through cut, 5-frame strobe, luma-flip hard cut, live video card, canvas push, shrink into a UI, chapter card, card push-up, short light-leak, window zoom-through, light iris, object iris, spin-portal, blur-rotation cut, rotation-matched cut, macro-texture bridge, vertical whip, floor wipe, eyepiece wipe, live-to-print pull-back, mouth iris, keyhole hold | 5-44 f | every frame count in `02-craft/event-map-reel-edit-style/references/transitions.md`; the picker table is section 9 of `references/pack/pack-skill-as-received.md` | zip 2 pack R1-R4 (measured in the pack) |

## Effects
- Grade: P1 high-contrast spotlight, crushed blacks; P5 warm practicals, teal-free; P3 B-roll teal/orange film look; B&W background with colour subject (7a74 S).
- Texture: grain, halftone, photocopy (P3, S3), frosted glass.
- Glow: on accent words, neon pills, icons, card rims.
- Matte: person cut-out for behind-subject type (P1, P2, P5).
- Avoid (never seen in the 12 references): cross-dissolves, spin/3D cube transitions, lens-flare packs, film-burn packs.
