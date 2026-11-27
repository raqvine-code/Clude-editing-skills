# Mastery overview (01-process/mastery)

Everything Claude has learned about video editing in this account, in one place.

| File | What's inside |
|---|---|
| `01-SKILLS-A-TO-Z.md` | All 23 skill folders: what each teaches, short/long form, evidence level, tools installed, known gaps |
| `02-SHORT-FORM-STYLES.md` | 11 short-form (9:16) styles + screenshot-only looks + platform rules |
| `03-LONG-FORM-STYLES.md` | 10 long-form (16:9) styles + shared rules |
| `04-PRO-EDITOR-MASTER-PLAN.md` | The step-by-step plan used for every edit, senior-editor habits, next steps |
| `05-PLAN-TEMPLATE.md` | Analysis + edit plan filled for EVERY video before editing (A footage facts ... J QC), incl. Claude's own creative ideas |
| `INDEX.md` (root) | Fast access: every skill, its layer and its one-line use-when. Rebuild: `python3 06-tools/tools/build_index.py` |
| raw-footage analysis | `04-styles/pro-video-editing/tools/analyze_raw.py <video> <project_dir>` (the old index and lint scripts are in `_archive/old-layout-tools/`; the new one is `06-tools/tools/build_index.py`) |
| skills | They live in the numbered layers 02-06; `INDEX.md` is the map |

Reference library for new styles: `/Users/raghusai/Desktop/training claude/` (add videos/screenshots any time; run `04-styles/pro-video-editing/tools/refscan.py` to learn only the new files).

## 2026-11-17 update
- `02-craft/edit-kit-playbook`: the Edit-Kit (40 open-source HyperFrames skills, vendored in `07-edit-kit-reference/`) distilled into one always-read layer: router, beat grammar, speech-to-visual map, caption model, motion seam law, cue sync, QA, MotionKit/CreatorFX helpers.
- `04-styles/pro-video-editing` profiles P6-P9 from 4 new references (violet condensed tips, noir red kinetic, real-estate orange explainer, lime studio personal brand) and P4 shell layouts C-F.
- `04-styles/faceless-explainer-reel-edit-style` (= profile P12 editorial cutout explainer; 2026-11-21, from the "zip 1" analysis pack): faceless voice-over reel, light act then dark act, with 5 new transitions (X15-X19), 2 type techniques (T15-T16) and 5 motion elements (M13-M17).
- `02-craft/event-map-reel-edit-style` (= profiles P13 two-tier kinetic talking head + P14 faceless 2.5D documentary; 2026-11-22, from the "zip 2" analysis pack of 5 reels): the event-map method used on every short (something new every 1.3 s, every visual caused by a word, every change has a sound), about 20 transition recipes chosen by meaning and a device library.
- Five skills received 2026-11-22: `04-styles/ultimate-editors-shortform-style` (= profile P15; master prompt + one measured reel, brief not received), `03-sound-type-assets/ue-sound-design` (three sound families, four passes, fixed levels), `02-craft/beginner-to-pro-edit-tips` (25 % smaller, fewer effects, dull colours; read on every edit), `06-tools/watch` (learn a style from any video file), `06-tools/ae-builder` (After Effects rebuild scripts).
- Learned 2026-11-25 from 11 measured YouTube / Instagram references: `05-clients/naveen-bro/mustard-red-caption-style` (the client's "aesthetic mustard + red" subtitles: M4 Haldi-Kumkum default (Claude's own), M1 podcast serif, M2 golden caps, M3 film subtitle; fixed palette, red only on negative words).
- Learned 2026-11-25 from 11 measured Instagram reels: `04-styles/aesthetic-pro-reel-edit-style` (= P16, the same client's "fully advanced pro edit": dark warm grade, blur-reveal captions, cut every 2-2.5 s, literal B-roll per noun, one insert every 6-8 s: paper cut-out scene, face HUD, ring, number giants).
- Standing rule: every video the user attaches is edited with all trained skills.
- Researched 2026-11-25 (user: best fonts for every video type, aesthetic subtitles, every editing style): `03-sound-type-assets/pro-font-and-subtitle-guide` (always read: fonts by video type and role, 70 free font files, Netflix / BBC subtitle numbers, safe zones, Telugu) and `04-styles/video-styles-atlas` (always read: every video form with its rhythm, captions, grade, moves, sound; new sections for vlog, wedding / brand film, tutorial, UGC ad, fan edit).
- Stored and restructured 2026-11-25: `INDEX.md` is now grouped by category (always read, short-form, long-form, any form + the P1-P16 profile map, sound / assets / thumbnails, learning and tools, folder rules, known gaps); `08-learning-log/CHANGELOG.md` records everything learned by date; the browser reference-capture tool is in `06-tools/_video-analysis-tools/`.
- Client font brief, round 4 (2026-11-25):
  - `05-clients/naveen-bro/mustard-red-caption-style` section 2c: six two-font pairing moments above the head, from the client's carousel and reel (as reference, not copied).
  - `03-sound-type-assets/pro-font-and-subtitle-guide` section 2b: the same pairing recipes for any video.
  - The font library is now 76 files.
- 2026-11-25 (night):
  - Telugu script renders (Homebrew fribidi turned on Pillow's raqm; check with `03-sound-type-assets/pro-font-and-subtitle-guide/tools/telugu_check.py`).
  - This Mac's tools are written up in `06-tools/MAC-TOOLCHAIN.md`.
