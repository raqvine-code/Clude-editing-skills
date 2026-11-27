# Techniques, devices and the build pipeline

Labels: `[prompt]` = stated by the creator in their prompt (I have not rebuilt or run these pipelines, so treat them as the authors' claims, though several are specific enough to implement directly). `[seen]` = visible in sampled frames. `[measured]` = computed from the files. Numbers in brackets such as `[225]` are entry numbers from `data/entries-all-242.csv`; the full prompts are in `picks.md` (entries 225-230, 183 and 182 are the richest).

## 1. Build architecture (the part that makes the polish possible)

All of this comes from the structured prompts [225, 226, 227, 229, 230, 183, 182, 228], which agree with each other.

1. **Every frame is a pure function of time.** One HTML (or WebGL2) page exposes `seek(t)`; every style is computed from `t`. No CSS transitions or animations, no timers, no state carried between frames. This is what lets you render any frame alone, scrub, probe and re-render.
2. **Springs in closed form.** Use the analytic step response of a spring, not a simulation. A value that changes target many times is the sum of one spring per change, so it stays a pure function of time [225, 226].
3. **One camera.** Put the whole layout in one world under one transform keyed by `[time, zoom, x, y]`, zoom interpolated in log space, eased segments. Each close-up is a move through that world [183, 229]. Rules from the prompts: one eased move per scene, never zoom in and straight back out [229]; drift a little through every scene (push 1.0 to 1.04) and start the next scene at the zoom where the last ended [182].
4. **Render with Playwright, blend subframes for motion blur.** Screenshot each frame several times at tiny time offsets and average them with `ffmpeg tmix`, at 60 fps. Subframes used: 3 at t-1/240, t, t+1/240 [227]; 4 [225, 226]; 8 [229, 182]; 16 across 0.7 of a frame for a 3D fly-over [228]. Gotcha [229]: 4 subframes left ghost copies on fast moves, so use 8 and slow the move down.
5. **Footage inside a deterministic page.** Either extract clips to 30 fps JPEG sequences and swap the image source per frame, awaiting decode [227], or re-encode all-intra (`ffmpeg -g 1`), load as a blob URL and await `seeked` before drawing [225]. A plain `python http.server` cannot range-seek video [225].
6. **Audio is analysed, not guessed.** Analyse the track with numpy: tempo, beat grid, energy per bar, the drop; calibrate the grid to the real kick hits [227]. Start the music on a downbeat and put the key visual (a zoom, a reveal) on the drop [225, 182]. Every cut on a downbeat, every UI hit on a beat [227].
7. **Sound effects.** Downloaded recordings (e.g. Mixkit), not synthesized [225, 229]; place each by its **measured peak**, not the file start [225, 226, 227, 229]; keep effects quiet under the music; `loudnorm` to -14 LUFS [225, 227, 229]; only use music and effects whose licence allows commercial use [227].
8. **Human gates before the full render.** Show the beat map and four stills first (every structured prompt ends with a `<start>` section asking for this) [225, 183, 230]; render one frame per beat and fix anything off-grid or cramped [226]; probe 20+ frames [227]; make a contact sheet and scan frame differences for single-frame pops [182, 229]; for a flight, check speed with optical flow [228]. The pack's `scripts/qc_render.py` and `scripts/contact_sheet.py` do the last two.
9. **Web page as source material.** For a 3D fly-over of a landing page [228]: screenshot the page in headless Chromium at device scale 2 after scrolling to the bottom once so lazy content loads; mark pieces that lift with `data-layer`; save each piece as a transparent PNG with its page position in JSON; draw them as quads in WebGL2 with mipmaps and 16x anisotropic filtering (else far text shimmers).

## 2. Scene linking: morph, don't cut

- **Shape floods the frame and contracts into the next scene** [225, 229 prompts]. The flood must overscale past all four corners and take about 0.3-0.35 s, or it reads as a flash or changes half the screen in one frame [225, 229, 230]. Give every layer a z-index so cards do not float above the flood [229].
- **Shared-element handoff** [229]: the flood carries a copy of the bubble's words; the button carries its label into the page. Text that swaps inside a morphing container needs its own enter and exit timing and often its own mask [225, 226, 230].
- **Iris wipe** [225 prompt, 72 seen]: six blades around a hexagonal aperture; each blade is defined by two vertices, both edge extensions and the SHORT arc between them [225].
- **Goo** [225]: blur plus alpha threshold, then composite the source on top so inner detail stays sharp.
- **Mask-line text rises** and **icons pop from zero on a spring** [225, 229], **bars draw across**, **pages push**.
- **Zoom-through / match cut** [seen 7, 14]: the camera dives into an object (the centre of a sunflower in 7) and the next scene continues from inside it; 14 whips between orbits. [227] says to measure element positions at runtime for match cuts.
- **Slice and glitch** [seen 8, 107, 131]: type or frame cut into horizontal strips that slide, sometimes with colour fringing.
- **Dissolve into particles** [seen 14, 38, 95]: a shape or word breaks into dots that re-form as the next object.
- **Beat-grid hard cuts** [182, 227]: cuts on downbeats; image changes on 16th notes with a click each.
- **Style flip per chapter** [seen 41, 63, 130, 187]: a whole new palette and type system, anchored by one constant device (genre chips [63], age and heart-rate counters [130], year footer [41], idea label [187]).
- **One continuous take** [seen 154, 59, 32, 173]: lighting and camera carry change; cut rate near zero [measured: 0.4 spikes/10s for M1].

## 3. Type

- Pair a clean grotesk with a serif italic: Geist 500 with Instrument Serif italic for a two-part closing line [228]; Geist for UI with a serif for the product name on the end card [229]; Archivo (width 125, weight 800) for a wordmark [225]. Seen: serif italic words inside grotesk statements [seen 192, 201, 69].
- **Letters as objects**: a wordmark squeezes into its own full stop like an accordion, every letter moving by the same factor with its width following [225]; "Reduce Motion" bends into "Motion" letter by letter, the orange dot staying on the "i" until it jumps [230]; glass letters pop in one at a time and melt into a droplet [225].
- **Orbit and tunnel**: a ring of words orbiting a dot that opens into a field of dots [230]; rings of keywords with a whip-blur zoom [seen 14, 107, 152].
- **Extruded 3D type** [seen 190, 197]; **sliced-block type** [seen 131]; **outlined word behind a simulation** [seen 131 "FLUID"].
- **Captions typed word by word at the time they are spoken** [182]. Do not show full stops in on-screen text [227, 182]. Highlight boxes behind words look like a Windows text selection [182].
- Keep text readable during camera moves: no `will-change` on anything the camera scales, or the text renders blurry [226]; leave space for notifications to stay legible [183].

## 4. Camera and depth

- Per-pixel depth of field [228]: blur radius = 75 x (focus - depth) / depth in front of the focus, 6 x (depth - focus) / depth behind, capped at 120 px, 40 taps on a golden-angle disc, each tap from a matching mip level; keep focus on whatever crosses the centre. Razor-thin focus in front, almost none behind, so near objects melt.
- A speed curve rather than position keys for a glide [228]: define speed as a share of cruise and integrate; check with optical flow that speed never dips and the zoom never turns into a zoom-in.
- Screen-studio style zoom to make each moment fill the frame, with the cursor scaling with it [225].
- Real-time 3D that reads like live action [seen 32]: flares, shallow depth of field, a wide-close-closer shot rhythm.
- Aspect choices that carried a mood [measured]: 109 uses 1920x816 letterbox; squares (1440x1440) for UI loops [226, 225, 182]; vertical 1080x1920 for engraving, Scrabble and anime pieces [seen 125, 24, 148].

## 5. Motion feel

- Springs everywhere with a tiny overshoot at most [226, 183, 230]; "bouncy easing" appears in the ban lists of 226, 227 and 229.
- **Stretch with two springs**: a tab indicator's two edges, or a toggle knob, ride different springs so the leading edge stretches ahead [226].
- **Squash on impact** for a ball landing [183]; drags are direct manipulation (value computed from the cursor while held, springs back on release) [226].
- **A real cursor** drives interface changes, with real clicks, drags and long-presses [225, 226, 230].
- **Something happens on every beat** [225, 226, 230]; no hold longer than 1 s [225, 229]; no dead time [226, 230]; eased fades of at least 0.3 s because a 0.05 s fade reads as a pop-in [182].
- [measured] The picks are busier and less static than the collection: median frame diff 3.1 vs 2.0, static share 3 % vs 7 %. The exceptions are on purpose (M1, M2 quiet beats).

## 6. Look systems

- **One accent colour** across every scene [230, 226, 227]; neutrals chosen on purpose (warm off-white canvas, near-black).
- Named values from the prompts: canvas #f5f5f2, UI black #0e0e10, lime #cdf24f, orange #ff6a2a, blue #2f6bff [229]; floor #f9fbfb centre and #f2f3f6 corners [228].
- **Iridescent input glow** [229]: a blurred conic gradient rotating through pink, orange, lime, cyan and violet around the input.
- **Liquid glass** [225, 182]: each glass element holds its own clone of the scene behind it, filtered with an SVG `feImage` displacement map (a rounded-rect distance field) through three `feDisplacementMap`s at slightly different scales for chromatic edges, plus rim light [225]; or: blur the capture behind the shape about 14 px, add a lightly blurred copy magnified about 1.06x in a 12 px edge band, then milk, sheen, rim and shadow [182]. `backdrop-filter: url()` misreads displacement maps in Chromium, so clone the scene [225]. Glass disappears on plain white, so add a slow pastel aura behind it [182].
- **Medium emulation** [seen 177, 178, 125, 230, 139]: risograph inks with misregistration and grain, phosphor oscilloscope line, engraving, halftone dots that respond to a moving point.
- **Per-chapter palette and type** [seen 41].
- Corner furniture (labels, timecodes, tick marks) is visible in many showreel entries [seen 124, 152, 190, 192, 201, 241]; two creators told the model to avoid it as "typical ai made giveaways" [4, 199].

## 7. Sound [measured and prompt; I could not listen]

- All 33 picks carry an audio track (210 of 242 entries overall). Mean level (ffmpeg `volumedetect`, which is not loudness) of 32 of the 33 sits between about -23 and -10 dB; entry 195 is near silent (about -41 dB).
- Prompts that describe audio: "Use the Oppenheimer theme music as inspiration, but compose it yourself" [14]; "sound tells half the story" [109]; "music and sound effects" [41]; "create the music too and make sure the video is synced with it" [38].
- For a voice-over piece, check the voice-to-music ratio for every phrase [182]; tone tags such as [warmly] can sound whispered and [excited] can sound fake [182].

## 8. Loops and endings

- **Last frame = first frame**, including cursor position and speed, or the loop stutters [226, 183, 230]; 130 asks for "cutting ready to loop to the beginning". `qc_render.py` reports the first-versus-last difference.
- End cards: logo or wordmark plus URL or call to action [seen 139, 202, 200, 225]; a typed final sentence with a blinking cursor [seen 82]; a name card for a showreel [seen 161, 192].
- Watch for blank or black tails [seen 99 ends on black frames].

## 9. Gotchas collected from the prompts

- Never put `opacity` or `filter` on a `preserve-3d` element (it flattens and both faces show); fade its wrapper [227].
- A child with `visibility: visible` shows through a hidden parent; use `inherit` [225].
- Declare every variable before the first `seek()` call [229].
- Keep a typed request on fixed lines so the camera never has to chase a wrapping cursor [229].
- Phones or cards that fade with transparency show whatever is behind them: fade into the haze colour first, cut to transparent at the very end [228].
- Lock the page layout before timing anything: a changed section height shifts everything after it [228].
- A highlight box behind a word looks like a Windows text selection; a camera reset to 1.0 during a handoff makes the zoom snap [182].
- Never let the ball (or any hero object) teleport between components: show the path of every handoff [183]. The graph and the dot must follow the same motion function or the spring feels fake [230].
- Give outgoing and incoming text separate timing so letters do not overlap [230].
- Use only licensed music and effects [227]. If code cannot run in the session, say so up front: a live preview is possible, the MP4 needs a machine that can run the renderer [228].

## 10. Effects the authors themselves banned

Across the structured prompts the ban lists repeat: crossfades, blur-ins, brightness "developing", 3D flips, glows, neon glows, particle bursts, shockwave rings, RGB split, camera shake, lens flares, grid floors, flashing backgrounds, bouncy easing, stock footage, gradients (on UI chrome), mismatched icon strokes, dead time, holds over one second, random transitions, "anything that looks like a template". Some pieces in the picks use particles, flares or glitch on purpose (14, 32, 200, 197); the point is that these are decisions, not defaults.
