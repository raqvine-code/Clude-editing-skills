# 04-styles: the style library (pick ONE per video)

Rule: every video gets ONE style, chosen from THIS video's content (topic, speaker, light, pace), with the reason written in `PLAN.md`. Borrow single devices from other styles only when the plan says so. Start with `video-styles-atlas/GUIDE.md`: one table of every video form and the style that fits it.

## Skills in this layer
| Skill | What it is | Evidence |
|---|---|---|
| `video-styles-atlas/` | every video form (short, podcast, faceless, long-form, documentary, vlog, brand film, tutorial, UGC ad, fan edit) and its rhythm, captions, grade, moves, sound, length | researched 2026-11-25 |
| `pro-video-editing/` | profiles P1-P20, `analyze_raw.py`, `refscan.py`, QC; the reference library index | measured |
| `tharun-speaks-edit-style/` | 9:16 word-pop captions, behind-subject headlines, punch-ins | measured, 2 reels |
| `tharun-speaks-longform-edit-style/` | 16:9 / 2:1 numbered-list long-form | measured, 2 videos |
| `aasil-khan-longform-edit-style/` | numbers, roadmap and framework explainers | measured, 1 video |
| `faceless-explainer-reel-edit-style/` | faceless voice-over reel (= P12) | analysis pack, not test-rendered |
| `ultimate-editors-shortform-style/` | calm premium talking head, sans plus script (= P15) | 1 reel, brief never received |
| `aesthetic-pro-reel-edit-style/` | Instagram-editor aesthetic talking head (= P16); built for Naveen bro | 11 reels |
| `editor-showcase-caption-edit-style/` | caption-led editor-showcase looks (= P17-P20): type cards with inversion, brand-colour caps + pills, under-chin kinetic, script + sans; `tools/caption_moves.py` | measured, 4 reels |
| `top-editor-styles/` | MrBeast, Hormozi, Johnny Harris, Iman Gadzhi, calm educational | general knowledge, least precise |

## Profile map P1-P20 (next new style = P21)
| P | Style | Form | Lives in |
|---|---|---|---|
| P1 | glass spotlight motion ad | 9:16 ad, music-led | `04-styles/pro-video-editing/profiles/P1-glass-spotlight-motion-ad.md` |
| P2 | editorial red studio | 9:16 value reel | `04-styles/pro-video-editing/profiles/P2-editorial-red-studio.md` |
| P3 | podcast magazine | podcast clip | `04-styles/pro-video-editing/profiles/P3-podcast-magazine.md` |
| P4 | results / before-after showcase shell | 9:16 showcase | `04-styles/pro-video-editing/profiles/P4-results-showcase-shell.md` |
| P5 | red-gradient explainer | 16:9 long-form | `04-styles/pro-video-editing/profiles/P5-red-gradient-explainer.md` |
| P6 | violet condensed tips | "3 tips" educator | `04-styles/pro-video-editing/profiles/P6-violet-condensed-tips.md` |
| P7 | noir red kinetic | dark-room opinion | `04-styles/pro-video-editing/profiles/P7-noir-red-kinetic.md` |
| P8 | real-estate orange explainer ("X vs Y") | explainer | `04-styles/pro-video-editing/profiles/P8-real-estate-orange-explainer.md` |
| P9 | lime studio personal brand | white-studio brand | `04-styles/pro-video-editing/profiles/P9-lime-studio-personal-brand.md` |
| P10 | amber UI educator | seated educator, dark studio | `04-styles/pro-video-editing/profiles/P10-amber-ui-educator-tips.md` |
| P11 | podcast scene inserts | podcast / interview clip | `04-styles/pro-video-editing/profiles/P11-podcast-scene-inserts.md` |
| P12 | editorial cutout explainer | faceless voice-over | `04-styles/faceless-explainer-reel-edit-style/GUIDE.md` |
| P13 | two-tier kinetic talking head | heavy-edit talking head | `02-craft/event-map-reel-edit-style/GUIDE.md` |
| P14 | faceless 2.5D documentary | voice-over story / history / news | `02-craft/event-map-reel-edit-style/GUIDE.md` |
| P15 | Ultimate Editors sans + script | calm premium talking head | `04-styles/ultimate-editors-shortform-style/GUIDE.md` |
| P16 | aesthetic pro reel (Haldi-Kumkum) | Instagram-editor talking head | `04-styles/aesthetic-pro-reel-edit-style/GUIDE.md` |
| P17 | type cards + colour inversion | punchy opinion short, 10-20 s | `04-styles/editor-showcase-caption-edit-style/GUIDE.md` |
| P18 | brand-colour condensed caps + pills | brand talking head, 10-30 s | `04-styles/editor-showcase-caption-edit-style/GUIDE.md` |
| P19 | under-chin kinetic captions, one focal zone | any teaching talking head | `04-styles/editor-showcase-caption-edit-style/GUIDE.md` |
| P20 | script word + small sans on the chest | calm premium talking head | `04-styles/editor-showcase-caption-edit-style/GUIDE.md` |
| - | screenshot-only looks (no measured video) | - | `04-styles/pro-video-editing/profiles/screenshot-only-styles.md` |

## Adding a style
A newly learned style gets its own `04-styles/<slug>-edit-style/` folder with a `GUIDE.md` (frontmatter `name` = folder name, `description` = when to use it), never only a file inside another skill. `06-tools/watch/GUIDE.md` builds one from a video. Then run `python3 06-tools/tools/build_index.py`, add the P-number row above, and add a line to `08-learning-log/CHANGELOG.md`.

## Evidence labels used inside the styles
V (verified frame by frame or from signal), S (contact sheet only, +/- 0.25 s), SC (screenshot only), E (estimate). Treat E and SC numbers as ideas.
