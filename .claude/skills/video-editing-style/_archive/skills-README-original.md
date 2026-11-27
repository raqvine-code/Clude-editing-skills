# Skills set: Tech Boy Deepak video editing

Everything Claude has learned about editing, one folder per skill: 36 skills plus 2 shared folders (`_edit-kit`, `_video-analysis-tools`). Each skill's `SKILL.md` starts with a description of when to use it. CLAUDE.md Rule 1 says which to read for each edit.
- What was learned and when: `CHANGELOG.md`.
- What is installed on this Mac (ffmpeg path, render venv, Telugu shaping, Homebrew on Intel, downloads): `MAC-TOOLCHAIN.md`. Read it before installing anything.
- Every section with its line number: `../VIDEO EDITING MASTERY/QUICK-INDEX.md`. Rebuild it after any skill change with `python3 "VIDEO EDITING MASTERY/tools/build_index.py"`.

**Order for every edit:**
0. Run the `../before edit/` gate (CLAUDE.md Rule 0, 2026-11-26): fill `PRE-EDIT.md`, meet the motion-graphics floor, and get `pre_edit_gate.py` to READY before the full render.
1. Read the always-read layer (section 1).
2. Pick the ONE style from `video-styles-atlas` and the type table (sections 2-4).
3. Analyse the footage and write PLAN.md (CLAUDE.md Rule 2).
4. Build the edit.
5. Run QC.
6. Deliver to `edited videos by claude/`.
7. Log the edit and any feedback (section 7).

## 1. Always read first (every edit)
| Skill | Why |
|---|---|
| `my-editing-rules` | Master playbook: briefs per video type, pacing, SFX / BGM, transitions, dislikes, "keep his cut", delivery routine |
| `mistakes-to-avoid` | Rejected moves and their fixes; use before styling and in final QA |
| `fonts-and-colours` | Approved fonts and palettes, plus the central font library (`assets/fonts/`: 79 font files, licences inside) |
| `pro-font-and-subtitle-guide` | Which free font fits each video type and role (₹ and Telugu support marked). Section 2b has six two-font pairing recipes. Also: Netflix / BBC subtitle numbers, caption sizes, safe zones, **where text goes in a vertical short** (researched 2026-11-25: section 5 + `references/vertical-text-placement-research.md`), Telugu rules, licences, font QC |
| `video-styles-atlas` | Every video form (shorts, podcast, faceless, long-form, documentary, vlog, wedding / brand film, tutorial, UGC ad, fan edit). For each: rhythm, captions, grade, moves, sound, length and the deep skill to read |
| `edit-kit-playbook` | Edit-Kit layer: router to the 40 kit skills, beat grammar, speech-to-visual map, caption model, motion seam law, cue sync, QA |
| `beginner-to-pro-edit-tips` | Three rules for every animation: 25 % smaller, effects only on the attention element, dull colours. Also a final QC check |

## 2. Short-form 9:16 (reels, Shorts)
| Making... | Use |
|---|---|
| **Any 9:16 short (start here)** | `shorts-editing-pro`: playbook, `tools/shortkit.py` renderer (new keys from 2026-11-25 are in its Files section) and `LEARNING-LOG.md` (append after every edit) |
| Method for EVERY short: event map, something new every 1.3 s, word-to-event sync table, sound grammar, QC. Also P13 two-tier kinetic talking head and P14 faceless 2.5D documentary | `event-map-reel-edit-style` (= P13, P14) |
| Talking-head reel, step-by-step method | `reel-editing-method` |
| Tharun Speaks 9:16 look (measured): word-pop captions, behind-subject headlines, punch-ins, lime labels | `tharun-speaks-edit-style` |
| Faceless voice-over explainer, no camera footage: white cutout scenes, then dark object scenes, blur-in two-font captions, stat wedge, light-leak flash. Its scenes also work as inserts | `faceless-explainer-reel-edit-style` (= P12) |
| Calm premium talking head: small sans + blue italic-serif keyword, overlay / split / off-white scenes, 1-2-3 step pill ("Remotion short", "Joseph style") | `ultimate-editors-shortform-style` (= P15) |
| **Naveen bro client: subtitles.** Aesthetic mustard yellow + red captions. M4 Haldi-Kumkum is the default; also M1 podcast serif, M2 golden caps, M3 film subtitle. Red only on negative words. Section 2c adds the client's font-pairing brief (round 4): six two-font pairing moments set above the head. Captions layer only | `mustard-red-caption-style` |
| **Naveen bro client: full edit.** "Fully advanced pro, aesthetic font subtitles like the Instagram channels": dark warm grade, blur reveal, cut every 2-2.5 s, literal B-roll per noun, one insert every 6-8 s (paper scene, face HUD, ring, number giant) | `aesthetic-pro-reel-edit-style` (= P16) + `mustard-red-caption-style` |
| Words that arrive with a designed move: a word stack building word by word on the chest under the chin (above the head only as a 1-3 per short accent), a letter-by-letter type-on hero word, blur / rise / grain / pop / cut arrivals, big meaning words with small link words, and the sound for each move (shortkit `stacks`) | `text-animation-moves` |

## 3. Long-form 16:9 (YouTube)
| Making... | Use |
|---|---|
| **Any long YouTube explainer (start here)** | `youtube-long-video-editing` (16:9 build kit) |
| Tharun Speaks long-form look | `tharun-speaks-longform-edit-style` |
| Numbers / roadmap / framework explainer: white + navy UI scenes, recap chart, staircase, flash cuts | `aasil-khan-longform-edit-style` |
| Motion-graphics look learned from 82 reference reels | `motion-graphics-style` |
| MrBeast / Hormozi / Johnny Harris / Iman Gadzhi / calm educational (also as 9:16) | `top-editor-styles` |

## 4. Any form: style library and special jobs
| Need | Use |
|---|---|
| Premium styles from the reference library, profiles P1-P16 (map below), `analyze_raw.py`, `refscan.py`, QC | `pro-video-editing` |
| Motivational / motivation + AI | `motivational-video-editing` |
| Client edit ("make this boring video high-engagement"): end-to-end pipeline, camera keyframes, price / number reveals, map beats, the Mr. Unbox build kit | `client-video-editing-process` |
| SaaS / app product video, no talking head | `app-product-animation` |
| 20-40 s intro, hook, cold open | `video-intro-design` |
| A video quoting sources, numbers, names (highlight match cut) | `text-highlight-match-cut` |
| Vlog, wedding / brand film, tutorial, UGC ad, meme / fan edit | `video-styles-atlas` sections 2-6 |

### Profile map (`pro-video-editing/profiles/`; next new style = P17)
| P | Style | Form | Lives in |
|---|---|---|---|
| P1 | glass spotlight motion ad | 9:16 ad, music-led | profiles |
| P2 | editorial red studio | 9:16 value reel | profiles |
| P3 | podcast magazine | podcast clip | profiles |
| P4 | results / before-after showcase shell | 9:16 showcase | profiles |
| P5 | red-gradient explainer | 16:9 long-form | profiles |
| P6 | violet condensed tips | "3 tips" educator | profiles |
| P7 | noir red kinetic | dark-room opinion | profiles |
| P8 | real-estate orange explainer ("X vs Y") | explainer | profiles (= Edit-Kit Agent Story) |
| P9 | lime studio personal brand | white-studio brand | profiles |
| P10 | amber UI educator | seated educator, dark studio | profiles |
| P11 | podcast scene inserts | podcast / interview clip | profiles |
| P12 | editorial cutout explainer | faceless voice-over | `faceless-explainer-reel-edit-style` |
| P13 | two-tier kinetic talking head | heavy-edit talking head | `event-map-reel-edit-style` |
| P14 | faceless 2.5D documentary | voice-over story / history / news | `event-map-reel-edit-style` |
| P15 | Ultimate Editors sans + script | calm premium talking head | `ultimate-editors-shortform-style` |
| P16 | aesthetic pro reel (Haldi-Kumkum) | Instagram-editor talking head | `aesthetic-pro-reel-edit-style` |
| - | screenshot-only looks (no measured video) | - | `profiles/screenshot-only-styles.md` |

## 5. Sound, assets, thumbnails
| Need | Use |
|---|---|
| SFX / BGM redesign, voice chain, mastering | `sound-and-music-design` |
| Ultimate Editors (Joseph) sound passes: whooshes, textures, risers + hits, four fixed passes, fixed levels (clashes with the older rules in its last section) | `ue-sound-design` |
| B-roll for a script line (272 local clips) | `broll-library` (+ `catalog.md`) |
| Pop-up PNGs, logos, stickers (78) | `png-library` (+ `catalog.md`) |
| An asset not available locally (stock sites, licences) | `where-to-find-assets` |
| YouTube thumbnail | `thumbnail-strategy` |

## 6. Learning and tools
| Need | Use |
|---|---|
| Save a new rule, correction or approved insight; catalogue new assets; create a skill | `skill-saver` |
| Learn a style from a video FILE: frame pairs, words, sound hits; saves `skills/<slug>-edit-style/` | `watch` (`scripts/watch_mac.py`) |
| Study an Instagram / YouTube LINK without downloading it: frame grids, cut count, likes / caption | `_video-analysis-tools/browser_reference_capture.js` (steps in that README) |
| Reference-video forensics: easing tracker, contact sheets, spectrograms, SFX onsets | `_video-analysis-tools/` (10 Python scripts; 4 hardcode an old ffmpeg path, fix before running) |
| After Effects project rebuilt from an animation (code, MP4, storyboard, HTML), its errors, easing mismatch | `ae-builder` |
| The full Edit-Kit (40 skills, MIT / Apache, licences inside, unmodified) | `_edit-kit/` (entry point `edit-kit-playbook`) |

## 7. Folder rules (keep the set tidy)
- **One skill = one folder** with a `SKILL.md`. Its frontmatter `name` equals the folder name, and `description` says when to use it. A newly learned style gets its own `<slug>-edit-style/` folder, never only a file inside another skill.
- Inside a skill:
  - `references/` holds measured notes, reference tables and frame sheets.
  - `tools/` (newer) or `scripts/` (older, kept as received) holds runnable code.
  - `assets/` holds fonts and images.
  - `original-full.md` is the long original from `Downloads/claude/Raghu and claude/skills/`, before it was distilled.
  - `LEARNING-REPORT.md` explains how a style was learned from a pack.
  - `LEARNING-LOG.md` (only in `shorts-editing-pro`) holds every short and every piece of feedback.
- Folders starting with `_` are shared kits or tools, not skills.
- Received skills (`.skill`, `.zip`, `.md`) are stored unchanged; this Mac's notes go in an "On this Mac" section at their end.
- After any change:
  1. Add the skill's row here.
  2. Add an entry to `CHANGELOG.md`.
  3. Add a line to CLAUDE.md Rule 1 if it is a new style.
  4. Add a line to the `skill-saver` map.
  5. Add a line to `VIDEO EDITING MASTERY/README.md`.
  6. Rebuild QUICK-INDEX.
  7. Run the structure check: `python3 "VIDEO EDITING MASTERY/tools/lint_skills.py"` (SKILL.md, name = folder, description, README row, skill-saver map, no dangling skill names).
- When two skills disagree, the clash is written in the newer skill ("Clashes" section) and said to the user before the edit (CLAUDE.md Rule 3).

## 8. Known gaps (2026-11-25)
- **Telugu script:** fixed on 2026-11-25 (Homebrew `fribidi` turned on Pillow's raqm). Check it with `pro-font-and-subtitle-guide/tools/telugu_check.py`. Not used for the Naveen bro client: user, 2026-11-25, "dont use telugu font" (Tenglish in Latin fonts).
- **PDFs:** no PDF reader on this Mac (no pypdf, no poppler), so a research paper's full text can't be read; use its abstract or an HTML copy (`MAC-TOOLCHAIN.md`).
- **Links:** `yt-dlp` is not installed, so a link cannot be downloaded. Study it with the browser capture instead (it measures picture only, not sound).
- **P15:** the linked brief has not been received.
- **P16 / M4 samples:** not yet seen by the client, and not watched on a phone.
- **₹ glyph:** 7 fonts have none (listed in `pro-font-and-subtitle-guide` section 3).
- **Mixkit:** video is 720p and personal-use only since 2026-11. Pexels comes first.
- **Text moves not built yet:** liquid / ink matte word transition, invert-background one-word scenes, mask-wipe reveal (`text-animation-moves` section 8). Word stacks, type-on and the other arrivals are built (shortkit `stacks`).
