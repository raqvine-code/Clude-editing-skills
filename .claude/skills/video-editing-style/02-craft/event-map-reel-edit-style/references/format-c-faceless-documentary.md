# Format C — Faceless 2.5D documentary story (history, news, mystery)

Sources: R2 (Semmelweis, 40.9 s, 150 wpm, 16 visual beats, 2 true content cuts) and R3 (Russian scientist mystery,
42.6 s, 128–130 wpm, 18 scene changes, ≈10 hard cuts, nearly all hidden inside moves). Full evidence: `reels/R2-faceless-documentary.md`,
`reels/R3-faceless-news-mystery.md`. Frames at 30 fps; W/H = frame width/height.

## 1. Identity

A slow, serious narration (128–150 wpm, sentence gaps 0.2–1.0 s) over generated stills built into 2.5D dioramas and
filmed by a virtual camera that never stops (frozen frames 0.5 % and 1.2 %; median frame-to-frame change 5.8,
three times a talking head's). Scene changes are spatial moves, not cuts. Text is withheld except when the word
is the picture. Sound is SFX and sub drones, no melody. Colour carries the meaning.

Why it works: stills can't hold attention on their own, so the camera supplies the life; continuous moves carry
the viewer through time and place without the "new clip" moment where people swipe; withholding text makes the
few words that appear land like evidence.

## 2. Story structure

R2: problem (0–3 s) → hope (3–7) → person (7–10) → evidence (10–15) → cause (15–20) → fix (20–23) → result
(23–25) → rejection (25–27) → vindication (27–31) → moral (32–35) → CTA (35.5–41): 10 story beats in 35.5 s, ≈3.5 s
each (carried by 16 visual beats).
R3: literal triple (scientist → died → mysteriously, an event every 0.6 s) → stakes widen (one death → plague
crowd at 3 s) → specificity stack (date, age, job, name, place, 6.5–11 s) → annotated evidence → acceleration
(6 cut events in 10.3 s, 17.2–27.5 s) → twist reset at 63–65 % (black void, words only) → denial → open question
(34.1 s) → CTA that converts the open loop ("Some editors rewatch this. Others open the project file…").

Devices that hold people:
- **Paradox cold open** with the trusted figure as villain ("Doctors were unknowingly killing their own patients").
- **An open loop of 15–20 s** ("until one man discovered a simple habit" paid off at 20.5 s; the answer words are
  withheld until 19 s). Show the mechanism a beat before the voice says it so the viewer solves it first.
- **Specificity stack**: name, date, number, place within ≈2 s reads as credibility.
- **Pattern break at the point**: R2 cuts from its darkest, most saturated frame (luma 31) to its whitest (203)
  and changes every device at once (single words, ticks, spotlight) for the moral.
- **Callback**: the opening phrase returns as the moral, quieter ("save lives": loud 3D caps at 6 s, small serif
  at 35 s).
- An unresolved ending (R3) drives comments and rewatches but frustrates; resolve the main loop and only leave a
  second question open if part 2 exists.

## 3. Building a scene (2.5D diorama)

Layers: foreground prop or frame edge (blurred) → cut-out subject → mid props → background plate (blurred,
1.3–2.5× overscan). Light and shadow must agree across layers; props on desks get a soft contact shadow and a
paper/wood texture.

House camera moves:
- **Rotate-and-pull-back on every still** (R2): start 1.3–2.5× and 15–30° tilted, ease out to level at −16 to
  −23 %/s over 1.3–2.5 s; some scenes drift ≈10° past level instead of stopping. Hook version: 2.5× and −28.5° in
  39 f, peak −9.5 %/f at f12. It hides the weak edges of generated plates and makes stills feel filmed.
- **Fly-back entrance** (R3): subject from ≈3× scale, per-frame 0.83, 0.88, 0.91, 0.93, 0.95, 0.96, 0.97 over ≈12 f,
  directional blur on frames 1–4, sub boom on frame 1, then −1 %/f drift. Max twice per reel (R3 used it 5 times).
- **Graph chase** (R2): the camera pans ≈290 px/s at 720 W and rotates ≈−11° to keep the pen tip at 45–60 % W.
- **Punch on negation** (R3): same plate ×1.41, −16° roll, crushed B&W, on the word "no" ±2 f with a boom.

Fill every pause: all 8 of R3's VO pauses ≥ 0.5 s carry a move or device plus an SFX. Big scene changes sit in
pauses; punches land on keywords (±3 f).

## 4. Transitions (recipes in `transitions.md`)

R2 used 15 transitions, 5 of them circles (a family, so it feels designed rather than repetitive); 14 of 15
start within −0.22 to +0.25 s of a sentence or clause onset (median +3 f); the hook move locks to "killing".
Library: window zoom-through (44 f), light iris out of a lamp (12 f), spin-portal (16 f + ≈25 f unwind), object
iris born at the cause (14–15 f), blur-rotation cut (5 + 6 f), floor wipe (4 + 3 + 11 f), vertical whip (15 f),
microscope-eyepiece wipe (21 f), card push-up (8–14 f), rotation-matched cut (≈20 f unroll), macro-texture bridge
(8 f hold + 12 f), live-to-print pull-back (23 f), mouth iris (12 f), keyhole hold and push-through.

## 5. Text as object

Rule: no captions; text appears only when the word *is* the picture, and it sits on a surface in the scene.
Three voices, chosen by the surface:

| Voice | Look | Used for | Numbers |
|---|---|---|---|
| Verdict | ultra-black extruded 3D caps, one red word per block when it holds a danger or turn word | the claim, the rejection, the CTA | cap ≈7.8 % W (R2); CTA lines 63–65 % W (R3) |
| Data | typewriter or condensed caps on slate/dark | dates, numbers, chart labels | ≈1–1.9 f per character; red underline trailing ≈8 f; R3 date ≈45 % W, start typing 10 f before the spoken date |
| Archive / moral | bold italic serif (≈Playfair, guess), soft shadow | abstract lines, the moral | one word at a time; R3's abstract words pop 1.42 → 1.0 in 6 f; R2's moral words scale/blur in over ≈4 f and hard-swap 0–4 f after each onset, with a 7–11 kHz tick 1–2 f before |

Other text devices: red name pill on the subject's chest (`#E61C1F`, 46 % W × 5 % H, expands in 8 f, later appears
"printed" in the newspaper); diegetic headlines annotated highlighter → circle → punch (see `devices.md`); a
vertical word stack in a black void for the twist ("But / there / was / a twist", camera rising ≈500 px/s at
1080 W).

Sync: when the word is the shot, 0 to +4 f after it is spoken (R2 mean +1.5 f). Recap phrases on a fixed 5–8 f per
word drifted up to 22 f behind the voice in R2 — time each word instead.

Sound-off: R2 showed no text for 4.5 s and only ≈37 % of its runtime had text; R3 ≈15 % of its VO. Add one
on-screen line in the hook (the claim in verdict caps) so sound-off viewers get the premise.

## 6. Colour script

- Luma flips > 80 levels at act boundaries (R2: 3, 8, 10, 23, 32 s).
- Saturated emotional scenes (0.6–0.75) alternate with near-mono evidence scenes (0.02–0.1).
- Red = danger, death or the turn word; green = life and improvement (R2's falling death-rate line is green and
  mirrors the earlier rising red line). B&W = death, the past, doubt (R3). R3 threads red from the first underline
  to the final red room.
- Glue: a static 45° halftone screen, ≈0.6 % W period, 2–3 % amplitude, over every shot (R2).

## 7. Sound

No music in either reel: low drones (20–80 Hz, −12 to −17 dB) act as the score.
- High click/tick (30–130 ms, 7–11 kHz): a change of material (to the date card, the blueprint, the CTA) or a word.
- Falling whoosh-boom (0.46–0.8 s, wide stereo, ≈7 kHz → ≈500 Hz; R3's texture bridge 2.4 kHz → 409 Hz): a change
  of location or world.
- Pure sub boom (mono 20–70 Hz, −15 to −23 dBFS): a meaning word (died, killed, dropped) or an object landing; R2's
  "dropped" gets a 1 s sub drop at ≈−15 dBFS.
- ≈5.4 (R2) and ≈6.6 (R3) distinct stereo SFX per 10 s (scorecard detector), plus mono sub hits; long booms at a
  median spacing of ≈4.6 s (R2) and ≈6.6 s (R3), mostly on seamless scene changes rather than hard cuts.
- R2's floor falls from −25.5 to −37.9 dBFS toward the moral; the CTA cut sits on the quietest moment.
- Both clipped (+1.3 and +3.4 dBTP; R3's 19 clipped samples all on transition SFX): limit the SFX bus, master to
  ≤ −1 dBTP.

## 8. CTA in the reel's language

R2: "The editors making work like this started with a project file from…" over the same extruded caps, then a
laptop on a desk with a search bar typing the URL. R3: 3D extruded "SOME EDITORS REWATCH THIS" on grid paper, then
a retro computer with a hanging project-file tag and a URL bar, entered by pushing through the keyhole. Both keep
the visual language so the ad doesn't feel like a channel change, but both ran ≈13 % of runtime and R2's was the
stillest part of the reel. Keep the house move alive, ≤ 12 % of runtime, URL typed on the spoken word (R2's
typed 0.5 s late), and end on a frame that loops to the first (e.g. a red circle matching an opening red cross).

## 9. Mistakes to beat

- Typos and garbled generated text ("DRAMATICALY"; "Dies" mid-headline; nonsense body copy).
- Fabricated evidence: news-brand logos on generated headlines, a named victim presented as real, AI images
  passed off as archive photos. Use your own masthead, label illustrations, keep real names to real facts.
- Data that contradicts the story (R2's death curve keeps rising past the year it should fall; no numbers).
- Plate artefacts revealed by camera moves (R2 showed mirrored tiling while panning ≈f165–235).
- Pacing sags (R2's sink: 2 s with nothing new; the newspaper hold); 15 fps sections next to 30 fps moves (R3).
- Small, low-contrast text (R3 date ≈3.7 % H with a dark red underline on near-black; R2 red on sky 1.3:1).
