---
name: skill-saver
description: Use whenever Deepak gives an editing preference, correction or rule ("remember this", "always/never X"), approves an editing insight, adds new B-rolls/PNGs to the asset folders, sends reference videos, or asks to create/adjust a skill. Defines where each insight is stored, how skills are created, how assets are catalogued and the reference-video analysis procedure.
---

> **Scope: mixed. The skill map inside was written for the old flat layout. Skills now live in numbered layers: put a new skill in the matching layer folder, then run `python3 06-tools/tools/build_index.py` to refresh INDEX.md and check the structure.**

# Skill saver: growing Deepak's editing brain

Skills live in `<layer>/<name>/GUIDE.md` (layer per `INDEX.md`); the original set is in `/Users/raghusai/Downloads/claude/Raghu and claude/skills/` (untouched). Asset folders stay in `/Users/raghusai/Downloads/claude/`. Note (2026-10-06): the `experiment/` folder was cleared; finals + edit notes go to `Raghu and claude/edited videos by claude/`, reusable code in each video's `code/` folder.

## Skill map
broll-library (B-roll catalog) · png-library (pop-up catalog) · my-editing-rules (rules, style, approved insights) · where-to-find-assets (website list) · motion-graphics-style (look learned from 82 reference reels) · reel-editing-method · app-product-animation (SaaS/product MG grammar, easing ladder) · motivational-video-editing · client-video-editing-process · text-highlight-match-cut · youtube-long-video-editing (16:9 build kit) · sound-and-music-design · video-intro-design · thumbnail-strategy · fonts-and-colours · mistakes-to-avoid (rejected frames as hard rules) · skill-saver (this file).
Added 2026-11-15 to 2026-11-22 (map caught up 2026-11-25): shorts-editing-pro (entry point for every 9:16 short, shortkit.py, LEARNING-LOG.md) · pro-video-editing (reference library, profiles P1-P20, analyze_raw.py, refscan.py) · edit-kit-playbook (always-read Edit-Kit layer) · event-map-reel-edit-style (P13 + P14, event-map method for every short) · faceless-explainer-reel-edit-style (P12) · tharun-speaks-edit-style (9:16) · tharun-speaks-longform-edit-style · aasil-khan-longform-edit-style · top-editor-styles (MrBeast / Hormozi / Johnny Harris / Iman Gadzhi / calm). Full list by category: `INDEX.md`; history: `08-learning-log/CHANGELOG.md`; structure check: `python3 "06-tools/tools/build_index.py"`.
Added 2026-11-25 (late): text-animation-moves (word stacks, type-on, blur / rise / grain / pop / cut arrivals, a sound per move; shortkit `stacks`).
Added 2026-11-27: editor-showcase-caption-edit-style (P17-P20: type cards + inversion, brand-colour caps + pills, under-chin kinetic, script + sans; four measured editor-showcase reels; `tools/caption_moves.py` renders write-on, pills, converge, type cards and tiles as shortkit `layers`).
Added 2026-11-25 (later): pro-font-and-subtitle-guide (fonts by video type and role, subtitle specs, safe zones, Telugu, licences) · video-styles-atlas (every video form and its style). Both always-read.
Added 2026-11-25: mustard-red-caption-style (client's mustard + red aesthetic subtitles, 11 measured references, M1-M4 looks; M4 Haldi-Kumkum default) · aesthetic-pro-reel-edit-style (P16: the same client's fully advanced pro edit, 11 measured Instagram reels).
Added 2026-11-22: ultimate-editors-shortform-style (P15 look, master prompt + reel) · ue-sound-design (Joseph's three-family sound passes) · beginner-to-pro-edit-tips (smaller, fewer effects, dull colours) · watch (learn a style from a video; a new style it learns is saved as `04-styles/<slug>-edit-style/`) · ae-builder (After Effects rebuild scripts).

## 1. Capture insights automatically
Every video Deepak sends triggers the routine in `my-editing-rules` ("Automatic routine"): reference video -> analyse every frame -> save to skill -> trash scratch; edit video -> deliver to `edited videos by claude/` with notes, WHAT_I_LEARNED.md and code -> update skills + README -> trash scratch. He will not say "save this". (2026-10-06)

Save in the same turn when Deepak: states a preference/rule ("I like", "always", "never", "cuts should be"); corrects an edit (save correction and reason); approves a non-obvious suggestion; says remember/save/note this; or when an asset fits or fails a topic in a way the catalog missed.
Do not save: one-off details of one video, things already in a skill, unconfirmed guesses.
After saving, tell him in one line what and where, e.g. `Saved to my-editing-rules -> "Hook: first B-roll must land within 1s".`

## 2. Where an insight goes
1. A specific B-roll -> its entry in `broll-library/catalog.md`.
2. A specific PNG -> its entry in `png-library/catalog.md`.
3. General B-roll/PNG placement rules (timing, frequency, blending) -> "Rules" section of that library's GUIDE.md.
4. Style, pacing, captions, music, hooks, transitions, workflow -> `my-editing-rules/GUIDE.md` under the matching heading.
5. A new repeatable workflow -> a new skill (section 3).
Prefer updating over duplicating; if a new rule contradicts an old one, replace it (latest word wins) and date it. Format: **rule** - why - (YYYY-MM-DD).

## 3. Creating a skill
Folder `<layer>/<kebab-name>/` (layer per `INDEX.md`) with required `GUIDE.md`, optional `catalog.md` for long data and `scripts/`. Frontmatter: `name` and a `description` stating what it does AND when to use it (specific trigger words; this line decides loading). Keep GUIDE.md short, long lists in catalog.md, then add the skill to the map above.

## 4. New assets
1. List uncatalogued files: `bash "06-tools/skill-saver/scripts/find_uncatalogued.sh"`.
2. Videos: compile `swiftc -O "03-sound-type-assets/broll-library/scripts/sheet.swift" -o /tmp/sheet`, run `/tmp/sheet "<file>.mp4" /tmp/<name>.jpg` for a 4-frame sheet. Images: `sips -s format jpeg -Z 600 "<file>" --out /tmp/<name>.jpg`, then view.
3. Look at every frame; never describe from filenames (hash names are meaningless).
4. Add the entry in the same format with a Quality line:
   - Pro: no watermarks/captions; video short side >= 720, or vertical with height >= 1000, or black/green-screen element with short side >= 400; image short side >= 600.
   - Usable: softer, needs trim/rotate/cleanup/checkerboard removal, or copyright risk; state the fix.
   - Avoid: stock/app watermark, foreign burned-in captions, other creators' promo cards, tiny, duplicates.
   Pro first within the category, and add the filename to the category index line.
5. Delete or fix entries for removed/renamed files.

## 5. Asset folders (under /Users/raghusai/Downloads/claude/)
`brolls for claude/` · `png for claude/` · `fonts for claude/` (list in fonts-and-colours) · `bgm for claude/` (not catalogued).

## 6. Reference videos (82 processed so far; latest ref82 documentary explainer, 2026-10-16)
Scratch lives in `pending videos/`; learnings go into skills, then reference copies/frames/notes are trashed (the skill is the only record, so write everything needed). (2026-10-06)

Procedure:
1. Copy/rename to `refNN_<topic>.mp4`, naming by what you see (Klickpin names describe the pin, not the video).
2. Probe length, size, fps with ffmpeg (the scripts find it via `FFMPEG` env, PATH, Homebrew, or `imageio-ffmpeg`, which is installed).
3. Scene cuts: `-vf "select='gt(scene,0.2)',showinfo"`; zero cuts = continuous morphing scene (a technique).
4. Frame sheets: `fps=4,scale=200:-1,tile=8x2` (each sheet = 4 s); read every sheet.
5. 2-3 full-res detail frames at typography moments, scaled to the same height (`scale=360:640`).
6. Numbers: luma/saturation (`signalstats`), audio onsets (20 ms RMS spikes), mean loudness, `silencedetect`; report, do not guess "dense".
7. Write an analysis file: file table, beat table per video (time/text/visual/motion), grade + audio notes, what is new.
8. Fold only genuinely new patterns into `motion-graphics-style`, tagged `*(refNN)*`; merge repeats.
9. Report to Deepak in one short message: what each video is, new patterns, where saved.

Tooling gotchas: measure easing with `06-tools/_video-analysis-tools/track.py` (60 fps; noisy when shapes blur/change colour, label as "by eye"); `gsheet.py` makes time-labelled sheets for 16:9, 1:1, 9:16 (FF env var, `python -I`). No `drawtext` fonts; draw labels with PIL. `pip install` needs a venv; scratch goes in the session scratchpad, not /tmp. All `06-tools/_video-analysis-tools` scripts now resolve ffmpeg automatically. Helpers: `motion_curve.py`, `band_onsets.py`, `spectrogram_log.py`. Split-screen references: find panel bounds from a saturated pixel column, crop each panel, sheet per panel.
YouTube downloads: pip `yt-dlp` on Python 3.9 fails ("page needs to be reloaded"); use the official `yt-dlp_macos` binary, verify against `SHA2-256SUMS`, run with `--js-runtimes node`, and tell Deepak it is a download.

Quality rule: separate what is seen (timings, colours, text) from what is inferred (fonts, easing, sound type); say "looks like Montserrat" or "probably a whoosh".


Full original notes (every detail, uncut): `_archive/original-full/skill-saver.md` in this folder.
