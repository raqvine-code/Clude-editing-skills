# CLAUDE.md: master rules for every edit

Regrouped from the original CLAUDE.md (kept word for word in `_archive/CLAUDE-original.md`). `README.md` is the router that says which file to read for which job.

## The order of every edit
1. **Know the client.** Load `05-clients/<client>/` (see `05-clients/README.md`). A client's taste never carries to another client. The owner's latest word beats every file here.
2. **Read** the Core 5 from `README.md`, plus the one style skill and the router rows for the job. Say in one line which skills and which ONE style you are using.
3. **Analyse, then plan, then edit** (Rule 2 below).
4. **Pass the gate** (Rule 0): `PRE-EDIT.md` filled, draft EDL READY, then a 6-10 s full-quality sample of the hook, then the full render.
5. **QC**: gate again, phone-size contact sheet, `05-clients/tech-boy-deepak/mistakes-to-avoid/GUIDE.md` sections H and K, `02-craft/beginner-to-pro-edit-tips/GUIDE.md`.
6. **Deliver and log**: finished video to `edited videos by claude/N. <Short Name>/` (a Mac folder, see `PATHS-AND-SETUP.md`), append to `02-craft/shorts-editing-pro/LEARNING-LOG.md`, save every lesson with `06-tools/skill-saver/GUIDE.md`, then rebuild the index: `python3 06-tools/tools/build_index.py`.

## Two reading modes (changed in the 26 Nov 2026 reorganization; the owner can overrule)
- **Fast mode**: own-channel drafts, quick tests, captions-only or sound-only jobs. Read the Core 5, the style skill, and the router rows for the job.
- **Full mode**: any client delivery, any redo after a rejection, or when the owner says "use all skills". Read everything in `01-process/before-edit/1-READ-THESE-SKILLS.md` and tick each row in `PRE-EDIT.md` with the one thing taken from it. This keeps the owner's standing instruction of 2026-11-17 ("every video the user attaches gets edited with ALL trained skills") and 2026-11-26 ("use all skills you learned, especially yesterday's").

## Rule 0: the gate comes first (2026-11-26)
Why it exists: the client was not impressed by video 25. It was text on a talking head: 11 % designed motion graphics, nothing designed for the first 17.8 s, no highlight and no match cut. Post-mortem: `08-learning-log/VIDEO-25-POSTMORTEM.md`.
1. Follow `01-process/before-edit/README.md`: reading list, client bar, pro move menu, then copy `01-process/before-edit/3-PRE-EDIT-SHEET.md` to `<project>/PRE-EDIT.md` and fill it (skills read, speech to visual map, motion-graphics plan, HL + MC, asset search log).
2. Meet the floor in `01-process/before-edit/2-PRO-MOVE-MENU.md` for every short:
   - a designed motion graphic every 8 s (3+ kinds, at least 25 % of the runtime, no stretch over 9 s without one)
   - HL + MC wherever the script quotes, names a source or repeats a key word
   - literal B-roll per noun (local catalog first)
   - a sound on every insert
   - a move and a sound on every pause of 0.5 s or more
   - **Text on footage is not motion graphics.**
3. Run `python3 01-process/before-edit/tools/pre_edit_gate.py <project>/edl.json` on the DRAFT EDL. No full render until it says READY; run it again before delivery. A FAIL is fixed by adding the missing work, never by editing the gate.

## Rule 1: pick the skill without being asked (2026-11-22)
1. For any edit request, check which skills fit and follow them exactly. Several fit: combine them.
2. If a request goes against a skill, or two fitting skills give opposite rules, **say what clashes BEFORE continuing and let the owner choose.** This is the one stop that is wanted; otherwise edits run without approval stops.
3. If the footage is already rough-cut or polished, keep the owner's cut and add only the missing layer (colour, captions, graphics, sound) unless a re-cut is asked for (`02-craft/my-editing-rules/GUIDE.md`, "keep his cut").
4. Reference videos are other creators' finished edits: study only, never re-edit or reuse their footage, faces or branding.

## Rule 2: analyse, then plan, THEN edit (2026-11-15, reinforced 2026-11-17)
Never start editing before the analysis and the plan exist. Never pick effects at random.
1. **Analyse** the footage: `python3 04-styles/pro-video-editing/tools/analyze_raw.py <video> <project_dir>` (facts, loudness, silences, speech rate, word transcript, 0.5 s contact sheets, candidate cuts). Watch the sheets and read the whole transcript.
2. **Plan**: fill `01-process/mastery/05-PLAN-TEMPLATE.md` into `<project_dir>/PLAN.md`: goal, story, style and the reason for it, skills used, shot-by-shot table, graphics list, sound plan, three weakest moments and their fixes, QC targets. The shot table carries the motion-graphics plan from `PRE-EDIT.md`.
3. **Creativity**: every plan includes 2-3 original ideas marked "Claude's idea", built on the chosen style, not copied from a reference, and still obeying `mistakes-to-avoid`.
4. Show the plan summary in one short message and carry on without waiting; update `PLAN.md` if the edit changes.

## Rule 3: decide like a pro editor; take the time to make it right (2026-11-25)
1. Every creative choice comes from THIS video's content: topic, words, speaker, light, pace. Write the reason in `PLAN.md` and build. No approval stops, except a Rule 1 clash.
2. **Quality before speed.** Render samples, check stills and contact sheets, fix, re-check, then deliver.
3. **When the video needs something the skills do not cover** (a style, a technique, an asset, a tool feature): research it first (web, or Instagram / YouTube through `06-tools/_video-analysis-tools/browser_reference_capture.js`), build it, then save it with `skill-saver` and a CHANGELOG entry.
4. One edit per fresh session; no subagent fan-out unless needed; finish and deliver video N before starting video N+1.

## Where the rules for one client live
`05-clients/<client>/`: fonts, palette, caption look, music and grade rules, dislikes, references, delivery copy. If a client has no folder, copy `05-clients/_TEMPLATE.md`, ask the owner the questions in it once, up front, and then run to the end.

## Fast access
- `SKILL.md`: the entry point when this folder is loaded as the Claude skill `video-editing-style`.
- `INDEX.md`: all 37 skills, path, scope, use-when.
- `PATHS-AND-SETUP.md`: Mac folders, tool paths, what is not in this zip, and what works in a cloud session.
- `06-tools/MAC-TOOLCHAIN.md`: what is installed on the Mac (ffmpeg, render venv, Telugu shaping, Homebrew on Intel).
- `08-learning-log/CHANGELOG.md`: everything learned, by date.
- `REORG-NOTES.md`: what moved, what was left out, what was changed.
