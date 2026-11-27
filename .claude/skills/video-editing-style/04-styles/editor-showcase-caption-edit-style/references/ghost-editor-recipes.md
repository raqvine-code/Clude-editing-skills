# Ghost Editor: 18 layout "worlds" and the house-look / components rule (read 2026-11-27)

Source: `github.com/kurbaitaev/ghost-editor` (MIT; some recipes are ports of MIT recipes by Lemo-Opuscar, credits in each recipe's `CREDITS.txt`). Read from a shallow clone; **nothing was installed or run**. The tool itself is built for Apple-silicon Macs (macOS text recognition, Homebrew) and was not tried here. Study only: other people's designs are reference, not material to copy (`CLAUDE.md` Rule 1.4). Clone to read the full `SYSTEM.md` of any recipe: `git clone --depth 1 https://github.com/kurbaitaev/ghost-editor`.

## Why this file exists
The owner rejected the redo of the "story you tell yourself" short because "every frame used the same pattern". Ghost Editor states the same failure in its Clean OS recipe: *"A new reel fills each slot with something NEW; copying a previous reel's scenes is the known failure (it reads as the same edit)."* and *"Clean OS as a system (not a template)"*.

## The rule it teaches (adopted in `GUIDE.md` 10b, rules 8-10)
| Part | What it is | Changes? |
|---|---|---|
| **House look** | type families, caption treatment, accent colours, how an insert is framed, the speaker's face as shot | fixed per client / style: this is the brand |
| **Components** | the scenes, props, transitions, hook device, outro device, B-roll treatment that fill the slots | **new every video**; log them (`02-craft/shorts-editing-pro/COMPONENTS-LOG.md`) and pick ones not used in the last three videos |
| **Two worlds** | the footage world (the person) and the designed world (the idea made concrete); the cut between them is the rhythm | alternate; the designed world is 20-35 % of runtime in Clean OS |
| **Literalism** | a designed moment shows exactly what is said, and its state change lands on the key word (about ±0.05 s) | always |
| **Footage hygiene** | no real look-away on screen; no pause inside a sentence; small glances (under 0.5 s, head within 12 degrees) stay | always |

## The 18 recipes (one line each: the world, not a template to reuse)
| Recipe | World |
|---|---|
| `caption-news` | huge captions slammed on word onsets, one keyword per caption on a honey block that wipes in; a document beat on a dark desk; lists as a lit grid |
| `clean-os` | the idea becomes a state change on the viewer's phone: white system surfaces or frosted glass over blurred footage; lowercase Inter word cards |
| `data-story` | a chart draws itself on cream paper with a red-blue pencil; handwritten notes pin the words; subtitle = the figure caption |
| `explainer-vector` | a narrated story drawn live in one continuous vector world (no footage) |
| `halftone-dossier` | retro print case file: halftone dots in four flat inks, misregistered shadow headlines, rubber stamps with a page shake, a case-file HUD |
| `hologram-hud` | the thing discussed is scanned into a glowing wireframe on a projector pad; target boxes lock on; values dock as chips |
| `kinetic-doc` | black-and-white archive documentary with one red accent; one centred line (a big heavy word + small words); prints, windows, polaroids |
| `news-package` | the speaker as a TV news anchor: sting that becomes the channel bug, a lower-third on the chest, a rundown ticked off at the end, fact cards between |
| `pov-montage` | first-person clips cut into a story with an editorial motion layer on top |
| `product-page` | a tool review laid out like a product page: rounded footage card on a gradient page, two-tier headlines, one spoken word at a time in a pill |
| `result-podcast` | warm podcast edit with paper, film and handwriting; a photo per idea |
| `seoul-list` | voice-over list over fast B-roll, two type families, phone-UI stickers, an iMessage outro |
| `stan-style` | seated tool tutorial with screen recordings on top |
| `step-deck` | a tips reel as a numbered deck: every word on its onset behind the head, flat full-screen cards every 1-2 s, giant italic numerals that shrink into place |
| `swiss-grid` | International Typographic Style: a 6-column page, one typeface, one signal colour, words rising out of clip rects |
| `tactile-paper` | printed paper that turns with a page fold, stepped 8 fps motion, zoom-blur pushes, hand-drawn labels, paper foley |
| `telestrator` | TV football analysis: freeze on the finding, draw a ring or arrow around (never on) the face, tactics boards between |
| `whiteboard` | the talk drawn on a whiteboard |
Each recipe has its own `SYSTEM.md` (invariants, slots, generators) and a `catalog.json` that records every element used.

## How this skill uses it
- The owner's client (Naveen bro) keeps ONE house look (Poppins + Playfair, haldi / kumkum / cream / ink, captions on the chest). The variety comes from the components. See `GUIDE.md` 10b.
- Good fits for a calm talking-head short: `kinetic-doc` (one heavy word + small words, prints as windows), `step-deck` (word cards between face shots), `swiss-grid` (one signal colour), `tactile-paper` (paper foley), `data-story` (quote and figure cards), `clean-os` (idea as a device state change). Borrow the world's logic, never its look.
- Its library of sounds was mined: the 8 calm CC0 sounds are in `03-sound-type-assets/sound-and-music-design/assets/ghost-cc0/`; the Mixkit ones are listed by id in `assets/mixkit-restore-list.json` and fetched with `06-tools/tools/mixkit_fetch.py`.
