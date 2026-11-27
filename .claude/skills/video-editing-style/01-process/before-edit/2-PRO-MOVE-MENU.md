# 2. Pro move menu: everything the skills can do, and the floor for every short

The floor is the minimum for a 45-60 s talking-head short. `tools/pre_edit_gate.py` checks families 1-2 and 6-7 from the EDL. Captions and text moves are their own layer: **text on footage never counts as motion graphics** (`mistakes-to-avoid` 16).

## Floor (45-60 s short)
| Family | Floor | Gate |
|---|---|---|
| Designed motion graphics | **1 every 8 s** (6-7 per short), **at least 3 different kinds**, **>= 25 % of runtime**, **no stretch over 9 s without one**, one in the first 3 s or on the first B-roll line | yes |
| Text highlight (HL) + match cut (MC) | 1 of each wherever the script quotes, names a source or repeats a key word; else a written skip reason | yes |
| Footage B-roll | 1 per concrete noun, 1 per 7 s at least, <= 50 % of runtime; local catalog searched first | yes |
| Text moves | hook title (pairing), 2-4 word stacks, 1-2 pairing moments, captions with brush / dot / strike | info |
| Transitions | a move on every jump cut; light-leak or luma flip on act turns (<= 3) | events |
| Camera | new framing >= 15 % on every cut; snap out on hero words, in on negative words | builder check |
| Sound | a sound on every insert and every MG element; three families (whoosh / texture / riser + hit) | yes |
| Pauses | every pause of 0.5 s or more carries a move AND a sound | yes |

## 1. Designed motion graphics (built visuals with depth, not text)
How to build them: render a scene clip with a `tools/scenes.py` in the project (PIL + OpenCV frames -> `assets/scenes/<key>.mp4`), then place it as a B-roll slot whose key starts with `mg_` / `hl_` / `mc_`. Or render RGBA frames and place them as a `layers` entry (`behind: true` puts objects between the wall and the speaker). Examples on this Mac: **`edits/roughcut3/tools/mg.py` (video 25 v2, the reference build: MC window behind the head, checklist card with a video window + strike-out, exam sheet with a stamp, status card with a filling / draining bar, real-page HL with marker + underline, share card with a cursor tap, loop window; one `Canvas` class for scene clips and RGBA layers)**, `edits/ammailu/tools/scenes.py` (split price board, hanging tags layer, receipt), `edits/telugu1/tools/scenes.py`, `edits/roughcut3/tools/scenes.py` (artwork plate). List the beats a scene animates inside itself (a row ticks, a bar fills, a cursor taps) in `edl["meta"]["mg_events"]` so the gate counts them; each one needs its own sound. Every scene follows `beginner-to-pro-edit-tips` (25 % smaller, one effect, dull colours), has depth (soft shadow, 2+ layers, slow drift), and moves on the spoken word.

| Kind | Use when the words... | Source skill | Kit |
|---|---|---|---|
| **List device**: checklist card filling item by item / pedestals / 1-2-3 step pill | list 3+ things ("guarantee, secure job, what people say, blueprint") | `event-map-reel-edit-style` 8, `ultimate-editors-shortform-style` 5 | scene clip, or `layers` + `dims` |
| **Contrast-pair object** (one object changes state) | set two ideas against each other (action / outcome, control / uncertainty, myth / fact) | `faceless-explainer-reel-edit-style` 12B | scene clip |
| **Quote / verse / page card with HL** (brush wipe under the spoken words) | quote a book, scripture, article, a person | `text-highlight-match-cut` | `hl_` scene clip |
| **Match cut (MC)** (one pinned word, 5-7 sources flash-cut behind every 3-4 frames) | repeat a key word or claim ("uncertainty", "control") | `text-highlight-match-cut` | `mc_` scene clip |
| **Stat wedge / live number / odometer** | say a percentage or number | `faceless-explainer-reel-edit-style`, `client-video-editing-process` | scene clip, `giants` number beat |
| **On-screen UI** (small card / pill over a darkened, blurred lower band) | name a tool, a step, a choice, a message | `ultimate-editors-shortform-style` 5, `app-product-animation` | `layers` (front) + `dims` |
| **Split screen** (animation top 58 %, speaker bottom 42 %) | explain a process while he keeps talking | `ultimate-editors-shortform-style` 3 | scene clip with a speaker window, or `layers` |
| **Full-screen off-white scene** (object-centric) | a concept needs the whole frame (a flow, a timeline, a map) | `ultimate-editors-shortform-style` 4, `motion-graphics-style` 17 | scene clip |
| **Object behind the head** | name a thing (a book, a degree, a phone) | `event-map-reel-edit-style` 8, `motion-graphics-style` 14 | `layers` `behind: true` |
| **Paper scene + topic giant** | the thesis line, the key question (budget 2) | `aesthetic-pro-reel-edit-style` 3 | `paper` + `giants` |
| **Artwork plate** | a named scripture, book or artwork | `aesthetic-pro-reel-edit-style` 3 | scene clip |
| **Face HUD / face ring** (light MG) | "check this" / a line pointed at "you" | `aesthetic-pro-reel-edit-style` 3 | `brackets` |
| **Mirror split** | self-talk, two sides of one person | shortkit | `mirror` |
| **B&W stretch** | the loss / waste / "never in our hands" beat | `aesthetic-pro-reel-edit-style` 3 | `desat` or B-roll `bw` |
| **Dim-and-overlay** | any front UI card that needs the speaker pushed back | shortkit | `dims` |
| **Speaker in a card / video into a phone** (the plate closes in round the live speaker in 4-9 frames; hero word across the card's lower edge) | name a platform, a screen, "my video", "the algorithm"; or the thesis line | `editor-showcase-caption-edit-style` 4 (11-12) | `caption_moves.py` `typecard` + `window` as a front `layers` entry |
| **Object type card** (full-frame accent plate + hero word + ONE object: icon system, tiles, phone) with a colour-inversion cut on the stressed word | a one-word claim ("wins", "chasing") that deserves the whole frame; counts as MG only with an object | `editor-showcase-caption-edit-style` 4 (9-10), 6 | `caption_moves.py` `typecard` (`invert`) |
| **Number tiles** (1-2-3 diamonds pop; the named one rolls to its word, the rest fade) | "one of these three things", "number one..." | `editor-showcase-caption-edit-style` 4 (16) | `caption_moves.py` `tiles` |

**Gate note (2026-11-27):** a `layers` entry keyed `txt_...` is a text move and a `dims` entry with `amt` >= 0.99 is a focus pull; the gate counts neither as designed MG.

## 2. Footage B-roll
- One literal clip per concrete noun and action (`edit-kit-playbook` 4: the visual matches the exact words).
- Search order: `broll-library/catalog.md` (grep every noun) -> Pexels portrait -> Pixabay -> Wikimedia Commons (public-domain art). Log each search in `PRE-EDIT.md`.
- Watch the frames of every download (stock titles lie: Pexels 34565141 "Gita" was a wedding card).
- Entries: `whip` / `whipL` / `blurzoom` / `cut`, a push `z` on every slot, `shade` for caption contrast (off on white backgrounds, ink lead-ins there).
- PNG pop-ups (`png-library`, Pro only) for a named object when no clip fits.

## 3. Text moves (the caption layer: needed, but not motion graphics)
| Move | Skill | Kit |
|---|---|---|
| Running captions, client look (ghost, blur reveal, brush, dot, strike, bar) | `mustard-red-caption-style` | `captions` + `style` |
| Word stack on the chest, type-on hero word, rise / blur / pop / grain / cut | `text-animation-moves` | `stacks` |
| Pairing moment (two-font title above the head) | `mustard-red-caption-style` 2c | `giants` / `stacks` |
| Giant behind the head, number beat, swap, strike | `tharun-speaks-edit-style`, P16 | `giants` |
| Letter tracking / stagger on the worst word | `event-map-reel-edit-style` P13 | caption `fx` |
| Write-on script through a blur, pill captions, converge from the edges, ghost-to-solid, the deliberate scatter, the quiet boxed ending | `editor-showcase-caption-edit-style` 4 | `caption_moves.py` (`writeon`, `pill`, `converge`) as front `layers`; `stacks` |

## 4. Transitions and flashes
`whip`, `whipL`, `blurzoom` and push-through (camera scale through the cut). **Focus-pull return** (2026-11-27, `editor-showcase-caption-edit-style` 4 (8)): after any card or B-roll the speaker arrives blurred and sharpens in 5-10 frames: `dims` `{"t0": cut-0.3, "t1": cut+0.3, "amt": 1.0, "blur": 16, "fade": 0.3}`. `flashes` `neg` (luma flip) on the turn, `white` as a one-off accent (never trains). Light-leak flash on act turns (P12: one asset, 3 max; build it as a scene clip). Dip-to-black only at chapter turns (long-form).

## 5. Camera (shortkit `camera`)
Wide / tight alternation with >= 15 % change on every cut. Snap out on a hero word, in on a negative word. Slow `in2` push on a build-up. A 3-4 % micro-drift on any hold over 1.2 s. Push-through on the hook exit and the payoff. Zoom cap 1.80 (2.0 on a 4K source). Last frame matches frame 0 (loop).

## 6. Sound (`ue-sound-design` passes, then `sound-and-music-design` levels)
1. **Whooshes:** every movement (B-roll entries, slides, push-throughs), panned with the motion.
2. **Textures:** every thing that changes without sliding: type-on slices, ticks on checklist items, paper, UI pops, the brush swipe, dots.
3. **Risers + hits:** into the turn, the reveal, the payoff, the loop.
- An airy flick on every hard cut.
- Music per the brief (none on video 25).
- Master -14 LUFS / -1.5 dBTP.
- Check the collision table: nothing within 6 dB of the voice.

## 7. Hook and loop
- The hook shows something designed or literal within 1 s: an MG scene, a B-roll or a paper scene, not only a title (`video-intro-design`).
- The loop line returns to the frame-0 look.
