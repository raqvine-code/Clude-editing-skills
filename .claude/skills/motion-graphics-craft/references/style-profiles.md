# Style profiles (M1 to M7)

Seven kinds of piece, found by grouping the 33 picks. Pick one before writing a brief; the profile decides length, pacing, how much text, and how detailed the prompt should be.

**Evidence labels.** `[prompt]` = stated in the creator's own prompt. `[seen]` = what I saw in sampled frames (8 per video for triage, 18 plus a 6-frame burst for the close-up sheets); I did not watch playback or hear audio. `[measured]` = computed from the video files: `median diff` is the median frame-to-frame change (0-255 grey scale, sampled at 12 fps), `static` is the share of sampled steps with almost no change, `spikes/10s` counts sudden whole-frame jumps (hard cuts, flashes, flips) per 10 seconds. Entry numbers refer to `data/entries-all-242.csv`; frames are in `visual-reference/detail/`. The exact prompts are in `picks.md`.

Collection-wide for comparison (all 242 entries): median length 20 s, 57 % at 60 fps, median diff 2.04, static 7 %, 6.9 spikes/10s. The 33 picks: median length 29 s, 67 % at 60 fps, median diff 3.12, static 3 %, 5.0 spikes/10s, every one with an audio track.

## Which profile?

| If the goal is | Use | Prompt style that worked |
|---|---|---|
| A story, mood or "wow" with no client brief | M1 | Open brief, 50-105 characters |
| One surprising idea that pays off | M2 | Open brief, or one topic constraint |
| Variety held together by a rule | M3 | One sentence that states the rule |
| A designer-reel or portfolio piece | M4 | The showreel one-liner plus one decisive constraint |
| A strong, recognisable look | M5 | Name the medium in 1-3 words, or a detailed art-direction brief |
| A polished, loopable UI piece | M6 | Structured template (see `prompt-patterns.md`) |
| A launch or promo film | M7 | Showreel + product (cheap) or structured template with real assets (premium) |

---

## M1 Narrative short / cinematic world
Entries 109, 68, 186, 173, 32, 154, 59 (alternates examined: 7, 24, 97, 100, 111).

- **What it is.** A wordless or lightly captioned film where lighting, camera and a small story carry the piece. The lowest cut rate in the study.
- **[measured]** median length 46 s, 2 of 7 at 60 fps (the rest are 24 or 30), median diff 2.01, static 0.7 %, **0.4 spikes/10s** (versus 6.9 overall). Long takes; cinematic pieces did not need 60 fps.
- **[seen]**
  - 109 *Lighthouse keeper*: letterboxed 1920x816, dark silhouettes lit by one lamp or window at a time, title card "THE KEEPER", fog and light beams, a tiny mark as the end card.
  - 68 *The Last Light* (240 s, 24 fps, 720p): a small robot in a lighthouse, a boat in a storm, lightning; dialogue as lower-third captions; the colour script runs sunset, storm blue, warm interior.
  - 186 *Beacon* (295 s): 3D cartoon characters against a purple void with red and yellow key light, speaker-named subtitles, an end title card.
  - 173 *Black hole* (300 s, 60 fps): a lensed accretion disc, almost no cuts (0.23 spikes/10s), Chinese captions under the frame, numeric readouts at the right, a title "视界" at both ends.
  - 32 *Pelican on a bicycle*: real-time 3D shot like live action: wide on the pier, close on the drivetrain, close on the beak, wings spread, flares and shallow depth of field, a bilingual title at the end.
  - 154 *Porco Rosso*: 14 s, one continuous aerial take with a rolling camera, painterly purple clouds and orange sea light, small italic caption ("just breathe.") plus manoeuvre names as lower thirds.
  - 59 *Tengwang Pavilion*: 30 s, one unbroken scene from sunset to moonlit night, vertical lines of classical Chinese verse appearing in sync; stack stated as WebGL2 + Canvas 2D + Web Audio.
- **[prompt]** The best ones gave the model the story: "Make a 45-second silent short film with no dialogue, where sound tells half the story. Invent the story." (109), "make a 4-minute animated short that blows my mind." (68). Pelican (32) is a long brief that grants unlimited time ("you can spend a whole day drawing it").
- **Build notes.** Three.js (186, 154), WebGL2 (59). Long films need chunked or resumable rendering.
- **Risks.** Render time at 4-5 minutes; story clarity (68 and 186 need their captions to be followed); 720p on the longest piece.

## M2 One-idea concept piece / data poem / 3D explainer
Entries 28, 156, 82, 142, 95, 195 (alternates: 36, 116, 144, 24).

- **What it is.** One idea, one visual system, a payoff in the last beat. Text is short; numbers and counters drive the motion.
- **[measured]** median 25 s, 5 of 6 at 60 fps, median diff 2.46, static 4.8 %, 2.3 spikes/10s.
- **[seen]**
  - 28 *Photon*: sequence of a counter in the Sun's core, "ABSORBED. AGAIN", "170,000 YEARS.", a flight HUD with a running clock while giant words (LIGHT, BRAKES, DETOURS, MILLION, EARTH) sit behind a starfield, a macro of a human eye, the closing line "YOU BLINKED." The on-screen figures were not fact-checked by me.
  - 156 *One second*: particle-built title, then counters (light around the Earth, the Earth's travel, lightning strikes, mass the Sun converts), a heartbeat line, "All of that.", and the title again.
  - 82 *Full Stop*: cream page, numbered figure captions ("FIG. 1 a point" ... "a full stop"), a point becomes a line, circle, sphere, lens, ball, flock and world; a glossy black sphere with a real cast shadow; ends on typed text with a blinking cursor. Prompt: "...with the sole purpose of flexing Opus 5.5 capabilities."
  - 142 *Mathematics*: unit circle to sine wave to epicycles tracing π, Lissajous, surface plot, Julia set, phyllotaxis dots, then Euler's identity and the name; thin line art on near-black with cyan, magenta and orange.
  - 95 *Drone Emprit*: one particle system keeps re-forming (map-like shape, network clusters, spike chart, logotype) with one caption line per beat and a running counter.
  - 195 *AI data centre*: 98 s white-studio 3D exploded views (power, hall, rack, chip), a title and one caption per section, a visible playback bar; soundtrack nearly silent.
- **[prompt]** Open or lightly constrained: "make a 20-second video about anything, your call; make it crazy." (28), "related to mathematics" (142), "show me what goes on inside an AI data centre." (195).
- **Risks.** Facts on screen need checking before publishing; the concept has to be visible without sound.

## M3 Format-play and chaptered pieces
Entries 63, 130, 41, 187 (alternates: 61, 116).

- **What it is.** The structure is the idea: many styles, one rule, one anchor device so it still reads as one film.
- **[measured]** median 56 s, 1 of 4 at 60 fps, median diff 4.08, static 2.7 %, **12.5 spikes/10s**. Fast cutting because every segment is a new world.
- **[seen]**
  - 63 *Recursion in genres*: the same lesson as a corporate explainer, terminal session, 8-bit game, nature documentary, noir, kids' TV, infomercial, trailer and a plain web page; a row of genre chips sits at the top throughout; the film refers to itself ("Base case... return").
  - 130 *Cycle of life*: age counter at left and heart rate at right (falls from 120 to 62), a different art style per life stage (flat pastel child, synthwave teen, grey city with a clock face for the 9-5, warm family, dusk elders), flatline, and a cut back to the start so it loops.
  - 41 *Indian civilisation*: each chapter has its own full-bleed palette and type (navy, cream, yellow, pink, orange-red), mixes scripts, carries a year in the footer, and closes on a timeline of icons.
  - 187 *Talking-head edit*: real footage cut out and placed in eight "idea" worlds (kawaii, manga, rubber-hose, holographic card, 8-bit, clickbait...), each with its own caption face and a label bottom right; ends on a "WHICH ONE? YOU TELL ME." grid. Stack: OpenEdit.
- **[prompt]** "...every explanation about recursion has a radically different video style, make this self-referential & clever & fast moving." (63). 130 spells the whole arc and asks it to "cut ready to loop".
- **Risks.** Whiplash. Keep one thing constant (chips, counter, label, footer) across segments.

## M4 Type-and-shape showreel
Entries 69, 161, 197, 131 (alternates: 124, 152, 190, 192, 201, 241, 107).

- **What it is.** A designer's reel in a strict system of type and primitive shapes. The most common kind in the collection and the easiest to make generic.
- **[measured]** median 23 s, **4 of 4 at 60 fps**, median diff 4.0, static 11 %, **20 spikes/10s**.
- **[seen]**
  - 69: cream and one ultramarine blue only; counting grids of squares, an isometric block wave, halftone ripples, a figure clearing hurdles; ends on a very large blue serif "Claude." with a square full stop.
  - 161: concept-led ("poster breaking out of its own frame"): a thin frame line with caption chips, a black circle becomes letters that overflow the frame, primary red, yellow and blue, a tilted 3D poster, ends on a name card.
  - 197: black with a single orange dot, a glitch "CODE", a ripple across a cube grid, then a switch to lime green with chrome 3D knots and lines such as "TYPE IN MOTION", "HIT THE BEAT" with a waveform, "BOLD."
  - 131: widest technique range of the four: sliced-block type, a chrome sphere and primary cubes, a fluid-simulation swirl behind outlined "FLUID", a particle vortex, streaked "MOTION", "SHOWREEL '26". Highest frame-to-frame energy of the picks.
  - Seen across many entries in this family (124, 152, 190, 192, 201, 241): small corner furniture (labels, timecodes, tick marks). Two creators asked to avoid it (see `prompt-patterns.md`).
- **[prompt]** 28 entries use the same one-line prompt (identical apart from capitalisation and a final full stop); 41 open with it; 85 mention "showreel". 131 shows the long version: an explicit list of techniques plus "meticulously art-directed rather than a random collection of effects".
- **Risks.** Sameness. What lifted 69, 161, 197 and 131 above their siblings was one system rule (two colours; one concept; one material; the widest technique list) held to the end.

## M5 Look-driven piece
Entries 151, 177, 125, 191 (alternates: 178, 47, 77).

- **What it is.** Pick one medium and let it dictate everything.
- **[measured]** median 25 s, 3 of 4 at 60 fps, median diff 7.4 (highest), static 0.4 %, 4.3 spikes/10s.
- **[seen]**
  - 151 *Phosphene*: an eye, then a kaleidoscopic tunnel in pink, cyan and violet, iridescent metaballs, a white-out, the eye again; shader work, almost no stillness.
  - 177 *Risograph*: pink, blue and yellow inks on cream with grain, hatching, misregistration, Korean type, a recurring blimp mark. 178 is the same studio script in an oscilloscope (phosphor line) look, so 177 and 178 show one script in two media.
  - 125 *Engraving*: white page, engraved figures (anatomy, horse, bust) morphing, a serif word set, a coral asterisk mark, vertical 1080x1920.
  - 191 *Lyrics*: a sun and eclipse as the hero, lyric words changing weight and face, a countdown readout at the bottom. Needs your own music.
- **[prompt]** Short and medium-first: "make about my studio with Risograph style" (41 characters, 177). 125 is a detailed brief (research the brand first, reference video attached, "no beige 'artsy' look", "every morph has to be perfect").
- **Risks.** The look has to be built, not filtered; check halftone, grain and misregistration at full size.

## M6 One-take UI motion
Entries 226, 183, 230 (the same template family also produced 60, 225, 229).

- **What it is.** One object or camera runs through a series of interface states without cutting; loops back to its first frame.
- **[measured]** median 14 s, 3 of 3 at 60 fps, median diff 5.4, static 5 %, 2.1 spikes/10s.
- **[prompt]** All three are 2,700-3,700 character structured prompts: a one-shape morph through a button, loader, player, slider, toggle, tabs, chart and command palette (226); a white ball that travels toggle, slider, notifications, reply field and keyboard (183); an orange dot that links a toggle, a word, a spring graph, a shape, orbiting type and a halftone field (230). Fonts: Geist for UI. Stack listed on the site: HTML (226 lists HTML + Playwright). Entries 60 (a different creator) and 226 share the identical prompt, so these structured prompts work as shared templates.
- **[seen]** Dark or off-white canvas, one accent, real cursor, camera zooms so each state fills the frame, small spring overshoot.
- **Risks.** Every handoff must be physically explained (no teleporting); match first and last frame, cursor included, or the loop stutters (all three prompts say this).

## M7 Product / brand launch film
Entries 225, 227, 139, 202, 200 (alternates: 229, 182, 233, 8, 72, 58).

- **What it is.** Short claims in large type, UI shown in context, one accent, a logo end card.
- **[measured]** median 20 s, 4 of 5 at 60 fps, median diff 2.7, static 5.6 %, 13.9 spikes/10s.
- **Two routes.** The cheap route is the showreel one-liner plus the product (139: "...like it's your showreel for a flowdrive"; 202: showreel plus "a launch saas video for https://dub.co"; 200: "Create a 30sec pitch video for @chaindotwtf"). The premium route is a structured prompt with real assets: 225 (a photo-print app, 54 beats at 120 BPM, one continuous take, real photos and wall footage) and 227 (a UGC ad tool, real vertical clips in a 3D carousel, one idea per shot).
- **[seen]** 139: orange system with halftone dots, a globe, an infinity loop; 202: a typed URL, a counter globe, dashboards, a ring of partner avatars; 200: 3D props (a big red button, slot reels, dice, a coin) cut against a light-trail vortex and glitch type; 225: Apple-keynote feel, hands holding the framed print as the payoff.
- **Risks.** Real assets are required for the premium route (photos, clips, a licensed track); the cheap route inherits the showreel look unless you add constraints.
