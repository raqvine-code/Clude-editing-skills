# CLAUDE 2.0 - video editing workspace

## Rule 0: the `before edit/` gate comes first (user instruction, 2026-11-26)
User's words: "this edit not impressed by client. I told you use all skills what you learned still now, especially yesterday's learned things. From next time onwards use perfect skills: B-rolls, motion graphics and other things like a pro editor."
1. Before ANY edit, open `before edit/README.md` and follow its order: read `1-READ-THESE-SKILLS.md` (ALL skills, newest lessons first, the craft skills too), check the client bar, then copy `3-PRE-EDIT-SHEET.md` into `<project>/PRE-EDIT.md` and fill it: skills read, speech -> visual map, motion-graphics plan, HL + MC, asset search log.
2. Meet the floor in `2-PRO-MOVE-MENU.md` for every short: designed motion graphics every 8 s (3+ kinds, >= 25 % of runtime, no 9 s stretch without one), HL + MC, literal B-roll per noun (local catalog first), a sound on every insert. **Text on footage is not motion graphics** (`mistakes-to-avoid` 16).
3. Run `python3 "before edit/tools/pre_edit_gate.py" <project>/edl.json` on the DRAFT EDL. No full render until it says READY; run it again before delivery.

## Rule 1: skills before every edit (user instruction, 2026-11-15)
Before ANY short-form or long-form video edit (planning, cutting, captions, graphics, sound, review):
1. Read `skills/README.md`, then always `skills/my-editing-rules`, `skills/mistakes-to-avoid`, `skills/fonts-and-colours`, `skills/edit-kit-playbook` (Edit-Kit layer, learned 2026-11-17), `skills/beginner-to-pro-edit-tips` (three rules for every animation: 25 % smaller, fewer effects, dull colours; learned 2026-11-22), `skills/pro-font-and-subtitle-guide` (fonts by video type and role, subtitle numbers, safe zones, Telugu, licences) and `skills/video-styles-atlas` (every video form and its style, to pick the ONE style); both researched 2026-11-25.
2. Read the skill(s) for the video type:
   - 9:16 short / reel: **`shorts-editing-pro` first** (its SKILL.md + LEARNING-LOG.md; build with `tools/shortkit.py`; append to LEARNING-LOG.md after every edit and every piece of feedback), then `reel-editing-method`, `tharun-speaks-edit-style`, `pro-video-editing` (profiles P1-P14), `my-editing-rules` section 6.
   - 9:16 faceless voice-over / motion-graphics reel (no camera footage), or a stat wedge / contrast-pair object / light-leak flash insert in any short: `faceless-explainer-reel-edit-style` (= P12), after `shorts-editing-pro`.
   - EVERY 9:16 short (method layer: event map in PLAN.md, something new every 1.3 s, word-to-event sync table, sound grammar, QC list), and the style itself for a two-tier kinetic talking head (P13) or a faceless 2.5D documentary story / history / news reel (P14): `event-map-reel-edit-style`, after `shorts-editing-pro`.
   - 16:9 long-form: `youtube-long-video-editing`, `motion-graphics-style`, `tharun-speaks-longform-edit-style`, `aasil-khan-longform-edit-style` (numbers / roadmap / framework explainers), `pro-video-editing` P5.
   - Creator styles (MrBeast / Hormozi / Johnny Harris / Iman Gadzhi / calm): `top-editor-styles`.
   - Intro/hook: `video-intro-design`. Facts/sources: `text-highlight-match-cut`. SaaS/product: `app-product-animation`. Client: `client-video-editing-process`. Motivation: `motivational-video-editing`.
   - 9:16 calm premium talking-head tips / list short in the Ultimate Editors look (sans + blue italic-serif keyword captions, overlay / split / full-screen off-white scenes, 1-2-3 step pill), or any "Remotion short" / "Joseph style" request: `ultimate-editors-shortform-style` (= P15; its linked brief is not received yet), after `shorts-editing-pro`.
   - Subtitles for the client who asked for "aesthetic, mustard yellow + red" captions (the Naveen bro shorts, from 2026-11-25), or any mustard / yellow-and-red / podcast-serif / golden-caps / film-subtitle caption request: `mustard-red-caption-style` (captions layer only; M4 Haldi-Kumkum is the default until the client picks a look; section 2c holds the client's font-pairing brief, used for two-font title moments above the head), after `shorts-editing-pro`.
   - The same client's full edit ("fully advanced pro edits, aesthetic font subtitles like Instagram channels", 2026-11-25), or any aesthetic / premium / advanced Instagram-editor talking-head request: `aesthetic-pro-reel-edit-style` (= P16; layer stack, insert menu, event grid), with `mustard-red-caption-style` for the captions, after `shorts-editing-pro` and `event-map-reel-edit-style`.
   - Words that arrive with a designed move in any video (word stack on the chest under the chin, letter-by-letter type-on, blur / rise / grain / pop / cut, big meaning + small link words) and the sound for each move: `text-animation-moves` (shortkit `stacks`), with the style skill of the video.
   - Learning a style from a video the user sends or links ("watch", "learn this video", "copy this style"): `watch` (run `skills/watch/scripts/watch_mac.py`; the new style is saved as `skills/<slug>-edit-style/`).
   - After Effects project wanted from an animation (code, MP4, storyboard, HTML), an error from such a build script, or easing that does not match: `ae-builder`.
   - Sound: `sound-and-music-design` + `ue-sound-design` (Ultimate Editors three-family passes; clashes between the two are listed at the end of `ue-sound-design`). Assets: `broll-library`, `png-library`, `where-to-find-assets`. Thumbnail: `thumbnail-strategy`.
3. Tell the user in one line which skills and which ONE style are being used, then follow `VIDEO EDITING MASTERY/04-PRO-EDITOR-MASTER-PLAN.md`.
4. If the user's video is already rough-cut or polished: keep their cut (`my-editing-rules` "keep his cut"), only add the missing layer (colour, captions, graphics, sound) unless they ask for a re-cut.
5. Every video the user attaches gets edited with ALL trained skills (user instruction, 2026-11-17); until new training arrives, the current skills are the standard.
6. Reference videos in `/Users/raghusai/Desktop/training claude/` are other creators' finished edits: study only, never re-edit or reuse their footage.
7. After feedback, save the lesson with `skills/skill-saver`.

## Rule 2: analyse, then plan, THEN edit (user instruction, 2026-11-15; reinforced 2026-11-17)
Never start editing a video before its analysis and plan exist. Never pick skills or effects at random: analyse the footage (topic, tone, speaker, room light, framing, pace), then choose from ALL learned skills the ONE style and the specific moves that fit THIS video best, write the reason for each choice in PLAN.md, then edit exactly to the plan like a pro editor.
1. **Analyse** the footage: `python3 skills/pro-video-editing/tools/analyze_raw.py <video> <project_dir>` (facts, loudness, silences, speech rate, word transcript, 0.5 s contact sheets, candidate cuts). Watch the sheets and read the whole transcript.
2. **Plan**: fill `VIDEO EDITING MASTERY/05-PLAN-TEMPLATE.md` into `<project_dir>/PLAN.md`: goal, story, style + reason, skills used, shot-by-shot table, graphics list, sound plan, creative ideas, three weakest moments + fixes, QC targets. The shot table carries the motion-graphics plan from `PRE-EDIT.md` (Rule 0).
3. **Creativity**: every plan includes 2-3 original ideas of Claude's own (marked "Claude's idea"), built on the chosen style but not copied from any reference; they must still obey `mistakes-to-avoid`.
4. Show the plan summary to the user in one short message and carry on without waiting (Rule 4), then edit exactly to the plan; update `PLAN.md` if the edit changes.

## Rule 3: pick the skill without being asked; say so when a request goes against one (user instruction, 2026-11-22)
1. For any edit request (reels, YouTube videos, captions, cuts, transitions, thumbnails, sound, After Effects), first check which skills in `skills/` fit and follow them exactly. Do not wait for the user to name the skill.
2. If more than one skill fits, combine them.
3. If the request goes against a skill, or two fitting skills give opposite rules, tell the user what clashes BEFORE continuing and let them choose. This one stop is wanted even though edits otherwise run without approval stops.

## Rule 4: decide like a pro editor on every edit; take the time to make it right (user instruction, 2026-11-25)
User's words: "based on video content you have some knowledge now, do work by own decisions like pro editor, for every edit. If you need some time to edit perfectly, take it, and gain knowledge to edit well."
1. Every creative choice comes from THIS video's content: topic, words, speaker, light, pace. That covers style, cut, captions, fonts / pairings, inserts, B-roll, sound and grade. Decide, write the reason in PLAN.md, and build. No approval stops, except a Rule 3 clash.
2. **Quality before speed.** Render samples, check stills and contact sheets, fix, then re-check before delivering.
3. **When the video needs something the skills don't cover** (a style, a technique, an asset, a tool feature), research it first (web, Instagram / YouTube via `_video-analysis-tools/browser_reference_capture.js`). Build it, then save it to the skills (`skill-saver`, `CHANGELOG.md`).
4. **For the Naveen bro client's shorts, the standard is the client's level:**
   - `aesthetic-pro-reel-edit-style` (P16);
   - `mustard-red-caption-style` M4 captions, in ONE font pairing from the client's carousel (default Poppins + Playfair Display ExtraBold Italic; never Bricolage + Fraunces, never many font types; user feedback, 2026-11-26);
   - 1-2 pairing moments (section 2c);
   - subtitles on the chest under the chin (block centre 58-65 % of the height, y about 1110-1250), with text above the head only as 1-3 accents per short (hook title, number, label), as researched in `skills/pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`; no Telugu-script font (user feedback, 2026-11-25);
   - the event-map method;
   - a sound on every insert;
   - the motion-graphics floor and the gate (Rule 0, `before edit/4-CLIENT-BAR-NAVEEN-BRO.md`); video 25 was rejected as text on a talking head (11 % designed motion graphics).
5. Still lean on credits (one edit per fresh session, no subagent fan-out unless needed). Still check on a phone-size sheet before delivery.

## Folder map (user instruction, 2026-11-21: one folder for edited videos, one for skills)
- `edited videos by claude/`: every finished video, one numbered folder each (`N. <Short Name>/` = final video + `code/` + `notes/`), plus `brain/` (all notes) and `README.md` (index). Deliver every finished edit here and add its README row.
- `skills/`: every skill learned. A newly learned style gets its own named folder here, never only a file inside another skill.
- `before edit/`: the gate before every edit (Rule 0): reading list, pro move menu, PRE-EDIT sheet, client bar, post-mortems, `tools/pre_edit_gate.py`.
- `edits/`: working projects and big masters only. `VIDEO EDITING MASTERY/`: overview and quick index of the skills.
- `Downloads/claude/Raghu and claude/` holds the old copies of both; nothing new goes there.

## Fast access
- `skills/MAC-TOOLCHAIN.md`: what is installed on this Mac (ffmpeg path, render venv, Telugu shaping, Homebrew on Intel, downloads). Read it before installing anything.
- `skills/CHANGELOG.md`: everything learned, by date.
- `VIDEO EDITING MASTERY/QUICK-INDEX.md`: every skill, its sections and line numbers (jump straight to the part needed). Rebuild after any skill change: `python3 "VIDEO EDITING MASTERY/tools/build_index.py"`.
- Overview of everything learned: `VIDEO EDITING MASTERY/README.md`.
