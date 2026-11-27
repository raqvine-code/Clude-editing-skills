# REORG-NOTES: what changed on 2026-11-26

Source: `CLAUDE-editing-skills-2026-11-26.zip` (folder "CLAUDE 2.0": 3,134 files, 303 MB, everything mixed in `skills/`, `before edit/` and `VIDEO EDITING MASTERY/`).
Result: this brain (about 955 files, 26 MB): 36 skills in 5 layers, plus process, kit reference, learning log and archive.

## Where things moved
| Old place | New place |
|---|---|
| `CLAUDE.md` (5 rules) | regrouped into `CLAUDE.md`; original word for word in `_archive/CLAUDE-original.md` |
| `skills/README.md` (category map, P1-P16) | `INDEX.md` (generated) and `04-styles/README.md`; original in `_archive/skills-README-original.md` |
| `before edit/` | `01-process/before-edit/` (client bar moved to `05-clients/naveen-bro/CLIENT-BAR.md`, post-mortem to `08-learning-log/VIDEO-25-POSTMORTEM.md`) |
| `VIDEO EDITING MASTERY/` | `01-process/mastery/`; its `QUICK-INDEX.md` and `tools/` (they only worked for the old layout) to `_archive/` |
| craft skills (14) | `02-craft/` |
| sound, type, asset skills (8) | `03-sound-type-assets/` |
| style skills (9) | `04-styles/` |
| `mistakes-to-avoid`, `mustard-red-caption-style` | `05-clients/tech-boy-deepak/`, `05-clients/naveen-bro/` |
| `watch`, `ae-builder`, `skill-saver`, `_video-analysis-tools`, `MAC-TOOLCHAIN.md` | `06-tools/` |
| `_edit-kit/` | `07-edit-kit-reference/` (text only) |
| `skills/CHANGELOG.md` | `08-learning-log/CHANGELOG.md` |
| each skill's `original-full.md` | `_archive/original-full/<skill>.md` |

## Left out (all heavy, all regenerable or on the Mac)
| Left out | Files | Size |
|---|---|---|
| reference-library analysis scratch (`knowledge/cache`) | 259 | 91.5 MB |
| Edit-Kit code, media, assets (text kept) | 1,679 | 119.1 MB |
| analysis-pack contact sheets (event-map 160, faceless 22) | 182 | 45.3 MB |
| fonts (6 of 82 kept) | 76 | 27.9 MB |
| one mp4 | 1 | 0.2 MB |

## Edited
- A `Scope:` line was added under the frontmatter of 14 skills: `my-editing-rules`, `mistakes-to-avoid`, `fonts-and-colours`, `thumbnail-strategy`, `mustard-red-caption-style`, `aesthetic-pro-reel-edit-style`, `tharun-speaks-edit-style`, `tharun-speaks-longform-edit-style`, `aasil-khan-longform-edit-style`, `top-editor-styles`, `broll-library`, `png-library`, `skill-saver`, `watch`. It says which parts are general and which belong to one client or creator.
- Old paths in 62 text files were rewritten to the new layout (`skills/<name>` became its layer path, `before edit/` became `01-process/before-edit/`, absolute Mac paths to the old root became `<ROOT>/`). The Edit-Kit and `_archive/` were not rewritten.
- Code: two lines in `shortkit.py` now find the font folder relative to the file (env `EDIT_FONTS` overrides); the docstring of `pre_edit_gate.py` points to the new paths. Both compile. No other code changed.
- Stale statements fixed in `01-process/mastery/README.md` and `01-SKILLS-A-TO-Z.md` (they said 23 skills and described the old layout).
- New files: `README.md`, `CLAUDE.md` (regrouped), `INDEX.md`, `PATHS-AND-SETUP.md`, this file, a README in each layer, `05-clients/` profiles and template, `06-tools/tools/build_index.py`.

## Not changed
- The wording of every rule inside the skills, the gate files and the learning logs.
- History: `08-learning-log/CHANGELOG.md`, `LEARNING-LOG.md` and `_archive/` still mention `skills/`, `before edit/` and `CLAUDE 2.0/` because those are what the folders were called when each entry was written.
- The Edit-Kit text (vendored unmodified, licences kept).

## Decisions to review (the owner can overrule any of them)
1. **Two reading modes** (Fast and Full) in `CLAUDE.md`. The original said to read every always-read skill on every edit, which is slow. Full mode keeps that for client deliveries and redos, so the 2026-11-17 and 2026-11-26 instructions still hold.
2. **Client taste separated from craft.** `mistakes-to-avoid` sits under Tech Boy Deepak; sections H and K are marked as applying to every client.
3. **`aesthetic-pro-reel-edit-style` is kept in `04-styles/`** (its layer stack is general) with a banner saying its client rules belong to Naveen bro.
4. **RAQVINE and Move with Raghu profiles are stubs.** Only brand and format facts are filled; nothing was invented.

## Known leftovers
- P12-P15 were never test-rendered; P15's brief never arrived; P16 and M4 had not been seen by the client.
- The Edit-Kit playbook says 40 kit skills; the folder holds 41 `GUIDE.md` files.
- The B-roll and PNG catalogs describe files that live only on the Mac.
- `skill-saver` text and `my-editing-rules` section 2 still describe the old delivery routine in Mac folder terms (correct for the Mac).

## 2026-11-27: installed as one Claude skill
- This folder is now the skill `video-editing-style` (`SKILL.md` at the root is the entry point, written new).
- All 77 nested skill files were renamed `SKILL.md` -> `GUIDE.md`, because a skill folder may hold only one `SKILL.md`. 159 mentions in 44 text files outside `07-edit-kit-reference/` and `_archive/` were changed to match; the text inside those two folders was left as it was.
- Added: `04-styles/editor-showcase-caption-edit-style/` (P17-P20, `caption_moves.py`, two open-licence fonts), profile pointers P17-P20, `02-craft/event-map-reel-edit-style/references/event-map-method-full.md` (the earlier skill, whole), `05-clients/naveen-bro/mustard-red-caption-style/references/typography-pairings-measured.md` (the earlier font-board study), a cloud-session section in `PATHS-AND-SETUP.md`.
- Nothing from the zip was removed: 956 files in, 956 present (901 byte-identical, 55 text files edited as listed here and in `08-learning-log/CHANGELOG.md`).
