---
name: video-editing-style
description: The owner's complete video-editing rulebook as one skill - a process gate, craft methods, 20 measured style profiles (P1-P20), client rule folders, sound and type guides, and render tools (shortkit EDL renderer, pre-edit gate, caption-move renderer). Use it whenever the user wants to plan, edit, caption, sound-design, review or redo a reel, Short, TikTok, podcast clip or long-form YouTube video; asks for a premium, aesthetic, advanced or pro edit, kinetic captions, typography, text animation, motion graphics, transitions, B-roll or a hook; sends raw talking-head footage or a client video; or sends reference videos to analyse and save as a new style. Read this file first - it gives the order of every edit (client, Core 5 plus ONE style, analyse, plan, gate, hook sample, render, QC, deliver and log), the floors every short must meet, and a router into the layer folders. Never start an edit from memory without it.
---

# Video editing style: the editing brain

This folder is the owner's whole editing rulebook: 37 skills in eight layers, written from 25 delivered edits, 100+ reference videos and reels, and client feedback. This file is the entry point. Every skill inside is a `GUIDE.md`; all paths below are relative to this folder (`<ROOT>`).

**Two rejections shaped it.** Video 25 and a cloud-session short were both turned down for the same reason: **text on a talking head**. Captions, stock clips and titles are not an edit. Designed motion graphics, literal pictures for the words, sound on every change and the client's own rules are.

## 1. The order of every edit (never skip a step)
| # | Step | Do | Done when |
|---|---|---|---|
| 1 | **Client** | open `05-clients/<client>/` (`05-clients/README.md` says how). Client rules beat the style; the owner's latest word beats both. No folder: copy `05-clients/_TEMPLATE.md`, ask its questions once | fonts, palette, music and grade rules, dislikes are written in the plan |
| 2 | **Read** | `CLAUDE.md` (master rules, one page), the Core 5 (section 2), ONE style (section 5), the router rows in `README.md`. Client delivery or a redo after a rejection = Full mode: every row of `01-process/before-edit/1-READ-THESE-SKILLS.md` | one line says which skills and which ONE style |
| 3 | **Analyse** | `python3 04-styles/pro-video-editing/tools/analyze_raw.py <video> <project>`; watch the sheets, read the whole transcript | facts, word timings, pauses, contact sheets exist |
| 4 | **Plan** | `01-process/mastery/05-PLAN-TEMPLATE.md` -> `<project>/PLAN.md`; `01-process/before-edit/3-PRE-EDIT-SHEET.md` -> `<project>/PRE-EDIT.md` (speech-to-visual map, motion-graphics plan with times, HL + MC, asset search log, 2-3 ideas marked "Claude's idea") | every spoken line has a visual that matches its exact words |
| 5 | **Gate** | `python3 01-process/before-edit/tools/pre_edit_gate.py <project>/edl.json` on the DRAFT EDL | `RESULT: READY`. A FAIL is fixed by adding work, never by editing the gate |
| 6 | **Hook sample** | stills, then a 6-10 s full-quality render of the hook | it looks designed in the first second |
| 7 | **Render** | `02-craft/shorts-editing-pro/tools/shortkit.py` (`video`, `audio`, `mux`) | full video |
| 8 | **QC** | gate again; phone-size contact sheet; `05-clients/tech-boy-deepak/mistakes-to-avoid/GUIDE.md` sections H and K; `02-craft/beginner-to-pro-edit-tips/GUIDE.md`; the style's own QC list | READY + no mistake left |
| 9 | **Deliver and log** | send the video; append `02-craft/shorts-editing-pro/LEARNING-LOG.md`; save every lesson with `06-tools/skill-saver/GUIDE.md`; `python3 06-tools/tools/build_index.py` | logged, index rebuilt |

If a request clashes with a skill, or two skills clash: **say what clashes before continuing and let the owner choose.** That is the only wanted stop. Otherwise run to the end.

## 2. Core 5 (read for every edit)
| File | Gives |
|---|---|
| `01-process/before-edit/2-PRO-MOVE-MENU.md` | the floors and the full menu of moves |
| `02-craft/event-map-reel-edit-style/GUIDE.md` | the event map: something new every 1.3 s, every visual caused by a word |
| `02-craft/edit-kit-playbook/GUIDE.md` | section 4, the speech-to-visual map |
| `02-craft/beginner-to-pro-edit-tips/GUIDE.md` | 25 % smaller, effects only on the attention element, dull colours |
| `04-styles/video-styles-atlas/GUIDE.md` | the ONE style for this form of video |

## 3. The bar (floors for a 45-60 s short; the gate checks them)
- **Designed motion graphics:** one every 8 s, 3+ different kinds, at least 25 % of the runtime, no stretch over 9 s without one, one in the first 3 s. **Text on footage never counts.**
- **Text highlight (HL) + match cut (MC):** one of each wherever the script quotes, names a source or repeats a key word, or a written reason to skip.
- **Literal B-roll:** one per concrete noun, at least one per 7 s, at most 50 % of the runtime; frames checked (stock titles lie).
- **Sound:** a sound on every insert and every motion-graphic element; three families (whoosh, texture, riser + hit); master -14 LUFS, true peak -1.5 dBTP.
- **Pauses:** every pause of 0.5 s or more carries a move AND a sound.
- **Type:** two font families at most; one hero word per card; 1-3 accent texts above the head per short, everything else on the chest.
- **Three laws** (`02-craft/event-map-reel-edit-style`): something new at least every 1.3 s; every visual is caused by a spoken word; every change has a sound.

## 4. One premium workflow: the layers of a talking-head short
Build in this order. Each layer names where its numbers live.
| Layer | What a pro does | Numbers | Read |
|---|---|---|---|
| 1 Cut and camera | keep the speaker's best takes; a new framing on every cut; punch in on negative words, out on hero words; eye line at one height all video | framing change every 2-2.5 s; change of 15 % or more on a cut; micro-drift 3-4 % on holds; zoom cap 1.80 | `02-craft/shorts-editing-pro`, `02-craft/reel-editing-method` |
| 2 Captions | on the chest under the chin, inside one focal zone; two voices: tiny lead-in + ONE hero word sized to the frame | block centre = chin + 17 % of the height (58-65 % in the usual framing); hero word 72-80 % of the width; lines inside x 120-960, bottom above y 1470 | `04-styles/editor-showcase-caption-edit-style`, `03-sound-type-assets/pro-font-and-subtitle-guide` |
| 3 Literal B-roll | one picture per noun, entered with a move, caption on top | 0.8-2.0 s each; whip / blur-zoom entry | `03-sound-type-assets/broll-library`, `where-to-find-assets` |
| 4 Designed motion graphics | list device, contrast-pair object, quote card with HL, match cut, stat number, on-screen UI, split, full scene, object behind the head, speaker in a card, object type card, number tiles | the floors in section 3 | `01-process/before-edit/2-PRO-MOVE-MENU.md`, `02-craft/motion-graphics-style`, `02-craft/text-highlight-match-cut` |
| 5 Plates and returns | take the speaker away for a card or B-roll, bring him back with a focus pull; the card carries one object | card held 0.3-2.5 s; closes in round the speaker in 4-9 frames; return sharpens in 5-10 frames | `04-styles/editor-showcase-caption-edit-style` sections 4-6 |
| 6 Text moves | the move is chosen by the word's meaning: blur-in, rise, type-on, write-on, pill, converge, colour inversion; an empty beat between caption groups | at most two kinds per stack; one type-on per stack; 0.3-0.8 s empty between groups | `02-craft/text-animation-moves` |
| 7 Sound | whooshes on movement, textures on things that change, riser + hit into the turn and payoff; music only if the client allows it | 7-10 events per 10 s in the showcase references; nothing within 6 dB of the voice | `03-sound-type-assets/ue-sound-design`, `sound-and-music-design` |
| 8 Hook and loop | something designed or literal within 1 s, not only a title; the last frame returns to the frame-0 look | hook device by 1.0 s | `02-craft/video-intro-design` |
| 9 Colour | only if the client allows a grade; dull, not saturated; one accent hue taken from the footage or brand | - | `03-sound-type-assets/fonts-and-colours`, the client folder |

## 5. Pick ONE style (reason written in `PLAN.md`)
| The video is | Style | File |
|---|---|---|
| Naveen bro short, or any "aesthetic / premium Instagram-editor" talking head | P16 aesthetic pro reel + the client's caption look | `04-styles/aesthetic-pro-reel-edit-style/GUIDE.md`, `05-clients/naveen-bro/CLIENT-BAR.md` |
| Caption-led talking head like the editor showcases ("Raw vs My Edit") | P17 type cards + inversion, P18 brand-colour caps + pills, P19 under-chin kinetic (safest base), P20 script + sans | `04-styles/editor-showcase-caption-edit-style/GUIDE.md` |
| Heavy-edit talking head with two-tier kinetic captions; faceless 2.5D documentary story | P13, P14 (the event-map method) | `02-craft/event-map-reel-edit-style/GUIDE.md`, full numbers in its `references/event-map-method-full.md` |
| Calm premium talking head, "Remotion short" | P15 | `04-styles/ultimate-editors-shortform-style/GUIDE.md` |
| Energetic list video, word-pop captions | Tharun Speaks | `04-styles/tharun-speaks-edit-style/GUIDE.md` |
| Faceless voice-over explainer | P12 | `04-styles/faceless-explainer-reel-edit-style/GUIDE.md` |
| Ad, podcast clip, noir, studio brand, UI educator | P1-P11 | `04-styles/README.md`, `04-styles/pro-video-editing/GUIDE.md` |
| A creator's look (MrBeast, Hormozi, Johnny Harris, Iman Gadzhi) | - | `04-styles/top-editor-styles/GUIDE.md` |
| 16:9 long-form | - | `02-craft/youtube-long-video-editing/GUIDE.md` and the two long-form styles in `04-styles/` |
| Anything else | - | `04-styles/video-styles-atlas/GUIDE.md`, then the router in `README.md` |

## 6. Tools
| Job | Command (from `<ROOT>`) |
|---|---|
| Analyse raw footage | `python3 04-styles/pro-video-editing/tools/analyze_raw.py <video> <project>` |
| Gate | `python3 01-process/before-edit/tools/pre_edit_gate.py <project>/edl.json [--facts <project>/analysis/facts.json]` |
| Render from an EDL | `python3 02-craft/shorts-editing-pro/tools/shortkit.py stills|video|audio|mux <project>/edl.json` (keys in the file's header) |
| Caption and card moves as layers | `python3 04-styles/editor-showcase-caption-edit-style/tools/caption_moves.py <spec.json> <project>/assets/moves --sheet` |
| Score a render against the reference ranges | `python3 02-craft/event-map-reel-edit-style/tools/reel_metrics.py <video>` |
| Frame sheets of any video; panel sheets of a showcase reel | `02-craft/event-map-reel-edit-style/tools/frame_sheets.sh`; `04-styles/editor-showcase-caption-edit-style/tools/panel_sheets.py` |
| Rebuild the index, check structure | `python3 06-tools/tools/build_index.py` |

## 6b. Sound: three skills installed next to this one (2026-11-27, owner's request)
`../real-sfx/` (places real recordings on cue frames, keeps voice, reports), `../real-sound/` (whole soundtracks: sourcing with licence checks, mixing, mastering, credits) and `../earshot/` (makes and LISTENS: `realness`, `rank`, `critique`, `timeline`). All three are third-party, MIT (Real SFX's bundled UI pack is CC0). Use them for the sound pass of any edit; this skill's rules win where they differ:
- **The bank first:** `03-sound-type-assets/sound-and-music-design/assets/openverse-real/` (75 real recordings with credits), then `references/sfx-sources-and-ears.md` for more. Real SFX's own rule agrees: sound is never synthesised (its `uisfx` pack, itself synthesised, only for interface ticks).
- **Client bar beats them:** no BGM, no grade, the owner's fonts. `real-sound` can edit music to picture, but only when the client allows music.
- **Sound variety gate** (no file over 3 uses, 60 % distinct, at most 20 % synthesised) applies to any sound they place.
- **No parallel agents:** `real-sound` offers a multi-agent critique; do not run it unless the owner asks (usage limits, `CLAUDE.md` Rule 3.4).
- **Never upload audio** (their optional Gemini listener) without the owner's explicit yes.
- **Install earshot first** in a cloud session (`sfx-sources-and-ears.md` section 2); the other two need Python and ffmpeg only.
- Validator notes: Real SFX's description has an unquoted colon and earshot's is 1,327 characters (limit 1,024 in the skill-creator validator); the harness loads both, so they are left as published.

## 7. Learning a new style from reference videos
1. Follow `06-tools/watch/GUIDE.md`: frames at the source rate, word transcript, cuts, audio events; measure, do not guess. Label every number (measured, observed, estimate).
2. Find the technique, not the look: why the move is on that word, what the eye does, what the sound does.
3. Save with `06-tools/skill-saver/GUIDE.md`: a new `04-styles/<slug>-edit-style/` folder with its own `GUIDE.md` (frontmatter `name` = folder name), the next profile number (**P21**) in `04-styles/README.md`, an entry in `08-learning-log/CHANGELOG.md` with the owner's words, then rebuild the index.
4. Reference videos are other creators' finished work: study only; never reuse their footage, faces or branding.
5. Keep exactly one `SKILL.md` (this file). New skill files are named `GUIDE.md`.

## 8. In a cloud session
`PATHS-AND-SETUP.md`, section "Cloud session", has the checked list. The short version:
- The gate, shortkit and `caption_moves.py` run. Style font keys in the EDL need absolute paths.
- No person matte: nothing behind the head, no paper scenes. Use front layers, type cards and the speaker window.
- The owner's B-roll, PNG, music and font folders are on the Mac. Ask for the clips the plan names; do not fill the gap with random stock.
- Work in sequence, one edit per session, no parallel agents.

## 9. Map of this folder
| Folder | Holds |
|---|---|
| `01-process/` | the gate, reading list, move menu, PRE-EDIT sheet, plan template |
| `02-craft/` | how to build: shorts kit, event map, motion graphics, text moves, HL + MC, hooks, long-form |
| `03-sound-type-assets/` | sound design, fonts and subtitles, placement research, B-roll and PNG catalogs, thumbnails |
| `04-styles/` | the style library, profiles P1-P20 |
| `05-clients/` | one folder per client: rules that never carry to another client |
| `06-tools/` | watch-and-learn, After Effects builder, skill-saver, index builder |
| `07-edit-kit-reference/` | 41 open-source kit skills, reached through `02-craft/edit-kit-playbook` |
| `08-learning-log/` | `CHANGELOG.md` (everything learned, by date), the video 25 post-mortem |
| `INDEX.md`, `README.md`, `CLAUDE.md`, `PATHS-AND-SETUP.md` | all skills listed; the job router; the master rules; paths and setup |

Earlier learnings kept whole: the five-reel event-map method (`02-craft/event-map-reel-edit-style/references/event-map-method-full.md`, with its format, transition, device and per-reel notes beside it) and the client font-board study (`05-clients/naveen-bro/mustard-red-caption-style/references/typography-pairings-measured.md`).

## 10. Known limits
- P12-P15 and P17-P20 were learned from analysis without a client-approved render. Treat their numbers as a starting point and check stills.
- Sound in the reference analyses is measured from the signal, not listened to. Font names of references are visual guesses.
- No client has approved an edit built to the gate from a cloud session yet. The rejected short of 2026-11-26 is still to be rebuilt.
