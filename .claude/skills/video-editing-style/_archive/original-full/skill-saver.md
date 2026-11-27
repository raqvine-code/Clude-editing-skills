---
name: skill-saver
description: Creates, updates and maintains the video-editing skills in .agents/skills. Use whenever Deepak gives an editing preference, correction, rule, or says something like "remember this", "save this", "that's a good insight", "always/never do X"; whenever Claude produces an editing insight Deepak approves; whenever new B-rolls or PNGs are added to the asset folders; or when asked to create/adjust a skill.
---

# Skill Builder — growing Deepak's editing brain

> **Note (2026-10-06):** `experiment/` paths in this skill are historical — that folder was cleared. Final videos + edit notes: `Raghu and claude/edited videos by claude/`. Reusable code: the `code/` folder inside each video folder. Reference analyses were folded into the skills and deleted.

All skills live in `.agents/skills/<skill-name>/SKILL.md` (project root: `/Users/raghusai/Downloads/claude`).
`.claude/skills` is a symlink to `.agents/skills`, so Claude Code auto-loads every skill saved here.

Current skills:

| Skill | Holds |
|---|---|
| `broll-library` | Every B-roll in `brolls for claude/` with a description + when to use it |
| `png-library` | Every pop-up image in `png for claude/` with a description + when to use it |
| `my-editing-rules` | Deepak's editing rules, style preferences and approved insights |
| `where-to-find-assets` | Deepak's fixed website list + decision tree for ideas, footage, SFX, music, fonts, vectors |
| `motion-graphics-style` | Learned motion-graphics look (type, grade, SFX, transitions) from reference reels and videos in `experiment/` (81 so far; latest: refs 80–81, Tharun Speaks + Somrat Dutta for the SaaS news look, 2026-10-15) |
| `reel-editing-method` | Full methodology from the first motion-graphics edit (AI vs AGI vs ASI): structure, pacing, type, MG, effects, sound, pipeline, checklist |
| `app-product-animation` | SaaS / product motion-graphics grammar (morph-not-cut, blur, glow-bloom impacts, cursor, type-on) + SFX recipe, from refs 09–11, 62–63 and 69 (a 14.5 s problem→product→result→CTA Short with a frame-timed beat table) + §6d, the smooth-animation study of refs 70–74 (measured easing/duration ladder, object-chain and one-camera patterns) |
| `motivational-video-editing` | motivation / life-lesson talking-head method from refs 75–77: story shape, visual spine, hero words, recap + one-action CTA, conflicts with his rules |
| `client-video-editing-process` | End-to-end pro pipeline for a client talking-head reel: analysis, selective correction, live reference research + concept panel, build kit, SFX/music/mastering, QA workflow (draft 2, Mr. Unbox iPhone 18 Pro); draft 3 (§10): SaaS-style IKKO MindOne product review with tracked UI objects, B-roll edit list, highlight + match cut |
| `text-highlight-match-cut` | The two must-use effects: brush-stroke text highlight (ref12) + keyword-anchored match cut (ref13), CapCut recipes, variants per genre, QC |
| `youtube-long-video-editing` | 16:9 long-form build kit: segment join/EDL, graded base-frame extraction + byte verification, HTML/GSAP scene engine, per-scene layout QA, mix, encode, final QA (Indian IT / Y2K / AI video) |
| `sound-and-music-design` | Audio-only redesign of a finished edit: designed SFX palette per visual world, music scored to picture (tempo/key/downbeat anchors), voice-relative levelling, phone-first loudness, numbers-based QA (Indian IT / Y2K / AI video, 2026-10-01) |
| `video-intro-design` | Short high-density intros (20–40 s) over one talking-head take: browser camera on a 2560×1440 plate, Vision person mattes, measured accent palette, period UI, dither transitions, phone-first SFX, six-lens QA (Y2K intro, 2026-10-01) |
| `thumbnail-strategy` | Click-strategy for YouTube thumbnails: 0.5 s glanceability, 1–2 focal points on the eye path, face emotion + gaze, separation, light/dark-mode colour, thumbnail+title 1+1=3, six formulas, honest payoff in 30 s, mobile feed test script (ref61 HimanshuG, 2026-10-06) |
| `fonts-and-colours` | Deepak's font list (Tactic Sans files in `fonts for claude/` + 10 fonts from his reels), one body + one heading font per video, change fonts every video, disliked palettes |
| `mistakes-to-avoid` | Deepak's rejected frames (Day 03, 2026-10-07) as hard rules + the fix for each; load before every edit and in final QA |
| `gadget-review-editing` | Pro tech-review / buying-guide system learned from Mr Techpedia's phone-sale video (ref66, 2026-10-07): per-phone recipe (store card → spec beats → cons), 12 layouts (circle PiP, screen cards, checklists, chip stacks, blueprint callouts, vs, frosted cons), tier chapter cards, brand-colour grid worlds, flashes, 3 s rhythm numbers, QA; applied on 11. Sale Phones Buying Guide (data-driven per-phone grammar, truthful price labels, research agents, render cut-outs, Telugu-word sync audit) |
| `skill-saver` | This file — how to create and maintain skills |

## 1. Capture insights automatically (do not wait to be asked)

**Every video Deepak sends triggers the automatic routine in `my-editing-rules` → "Automatic routine"** (reference video → analyse every frame → save to skill → trash scratch; edit video → deliver into `edited videos by claude/` with notes + WHAT_I_LEARNED.md + code → update skills + README → trash scratch). He will not say "save this". `(2026-10-06)`

Save to a skill **in the same turn** when any of these happen:

- Deepak states a preference or rule: "I like...", "always...", "never...", "don't use...", "cuts should be...".
- Deepak corrects an edit ("not this B-roll, use that one", "too many PNGs"). Save the correction *and* the reason.
- Deepak approves something non-obvious Claude suggested ("great idea", "perfect", "keep doing this").
- Deepak says "remember", "save this", "make this a skill", "note this down".
- A B-roll/PNG turns out to fit (or not fit) a topic in a way the catalog didn't capture.

Do **not** save: one-off details of a single video, things already in a skill, guesses Deepak hasn't confirmed.

After saving, tell Deepak in one line what was stored and where, e.g.
`Saved to my-editing-rules → "Hook: first B-roll must land within 1s".`

## 2. Where does the insight go?

1. About a specific B-roll (better use, wrong description, avoid it) → edit its entry in `broll-library/catalog.md`.
2. About a specific PNG → edit its entry in `png-library/catalog.md`.
3. General B-roll or PNG *placement* rules (timing, frequency, blending) → the "Rules" section of that library's `SKILL.md`.
4. Style, pacing, captions, music, hooks, transitions, workflow → `my-editing-rules/SKILL.md` under the matching heading.
5. A new repeatable workflow that doesn't fit anywhere (e.g. "thumbnail making", "caption style", "BGM library") → create a new skill (section 3).

Prefer updating an existing entry over adding a duplicate. If a new rule contradicts an old one, replace the old one (Deepak's latest word wins) and note the date.

Write each rule as: **the rule** — *why* (Deepak's reason, if given) — `(YYYY-MM-DD)`.

## 3. Creating a new skill

```
.agents/skills/<kebab-case-name>/
├── SKILL.md          # required
├── catalog.md        # optional: long reference data
└── scripts/          # optional: helper scripts
```

`SKILL.md` must start with frontmatter:

```markdown
---
name: <kebab-case-name>
description: <what it does AND when to use it — specific trigger words, because this line decides when the skill is loaded>
---
```

Keep `SKILL.md` short (instructions + rules). Put long lists in `catalog.md` and link to it.
Then add the skill to the table at the top of this file.

## 4. When new assets are added

1. Find what's new:
   ```bash
   bash .agents/skills/skill-saver/scripts/find_uncatalogued.sh
   ```
2. For each new video, build a 4-frame contact sheet and look at it (there is no ffmpeg on this Mac; this uses AVFoundation):
   ```bash
   swiftc -O .agents/skills/broll-library/scripts/sheet.swift -o /tmp/sheet   # once
   /tmp/sheet "brolls for claude/<file>.mp4" /tmp/<name>.jpg                # prints duration|WxH
   ```
   For new images: `sips -s format jpeg -Z 600 "<file>" --out /tmp/<name>.jpg`, then Read the jpg.
3. Look at every frame — never describe from the filename alone (names like `template 4` or hashes are meaningless).
4. Add the entry to the right category in the catalog using the same format as the existing entries, including a **Quality** line:
   - ⭐ Pro: no third-party watermarks or captions, and sharp enough for 1080×1920. Video: short side ≥720, or vertical with height ≥1000, or a black/green-screen graphic element with short side ≥400. Image: short side ≥600.
   - ✅ Usable: softer resolution, or needs a trim/rotate/cleanup, fake-checkerboard removal, or has copyright risk. Say the fix.
   - ⛔ Avoid: visible stock/app watermarks, foreign burned-in captions, other creators' promo cards, tiny files, duplicates.
   Put ⭐ entries first within the category, and add the filename to the matching ⭐/✅/⛔ line in that skill's "Category index".
5. Removed/renamed files: delete or fix their catalog entries.

## 5. Asset folders

- B-rolls: `/Users/raghusai/Downloads/claude/brolls for claude/`
- PNGs: `/Users/raghusai/Downloads/claude/png for claude/` (`Png's/` holds the same file names — treat it as a duplicate)
- Fonts: `/Users/raghusai/Downloads/claude/fonts for claude/` — font files Deepak gives; list them in `fonts-and-colours`
- Background music: `/Users/raghusai/Downloads/claude/bgm for claude/` — not catalogued yet

## 6. When Deepak sends reference videos

Deepak keeps sending motion-graphics reels (Pinterest/Klickpin downloads) to raise the quality bar. Analyse every one the same way, then fold the patterns into `motion-graphics-style`. Eighty-two references have been processed so far (ref82 = Think School's documentary explainer youtu.be/e1cwjeP5Ofs, 2026-10-16, for the ep 02 v2 real-evidence pass, saved into `motion-graphics-style` + `my-editing-rules` + `where-to-find-assets` + `mistakes-to-avoid` I; refs 80–81 = Tharun Speaks "14 Brutally Honest Truths" + Somrat Dutta "ZERO to ₹5L/Month", 2026-10-15, for the AI Tech News ep 02 SaaS look, saved into `motion-graphics-style` + `app-product-animation` §9; refs 78–79 = Somrat Dutta + Tharun Speaks long-form, video 13 v2; refs 75–77 = three YouTube motivation talks, 2026-10-13, saved into the new skill `motivational-video-editing` + `motion-graphics-style` + `fonts-and-colours` + `my-editing-rules`; refs 70–74 = five UI/UX promo clips from `UI:UX reference/`, 2026-10-09, studied for smooth animation: an After Effects glass-folder tutorial, a video-editor promo, a one-camera 3D phone promo, an Apple-Wallet concept loop and a website promo with a circle wipe; saved into `app-product-animation` §6d, with easing measured by `_video-analysis-tools/track.py`; their Klickpin file names named Pinterest pins that had nothing to do with the videos; ref69 = a 14.5 s "wireframe vs final" SaaS Short, 2026-10-09, saved into `app-product-animation` §6c + `fonts-and-colours` + `my-editing-rules`; refs 67–68 = the "new reference" folder, 38 stills + 6 screen recordings of two YouTube videos, 2026-10-09, saved into `motion-graphics-style` + `fonts-and-colours` + `mistakes-to-avoid` G; ref66 = Mr Techpedia's phone buying guide, 2026-10-07, saved as its own skill `gadget-review-editing`; refs 64–65 the font Shorts; (latest: refs 57–58, two YouTube concept explainers by Aishwarya Srinivasan downloaded with yt-dlp, analysed frame by frame plus Demucs-separated SFX timing in `10_references_57-58_aishwarya_rag_vectordb_analysis.md`; refs 50–56, the AI Tech News ep. 1 folder — official launch films, creators' comparison clips, posts and two incident reports, analysed for **pacing** in `09_references_50-56_ai_news_ep01_pacing.md`; refs 41–49 the red-glass motion-educator stills, `08_…`; refs 14–40 the editorial board, `07_…`) (`experiment/01_…`, `02_…`, `03_…` analysis files).

**Scratch goes in `pending videos/`, learnings go in skills.** Reference copies, frame sheets and analysis notes are temporary working files in `/Users/raghusai/Downloads/claude/pending videos/` (project work in `pending videos/<project>/build|work|deliver`). Once the patterns are folded into a skill, the reference videos/frames are trashed — the skill is the only permanent record, so write everything needed into it (no pointers to analysis files that will be deleted). Finished videos go to `Raghu and claude/edited videos by claude/`; see my-editing-rules → "Keep the workspace clean". `(2026-10-06, replaces the earlier keep-everything-in-experiment rule)`

**Procedure (all commands run from `experiment/`):**
1. **Copy and rename** to `experiment/refNN_<topic>.mp4`. The Klickpin file names describe the *pin*, not the video (a "puppy training" pin was a trading explainer), so name by what you see.
2. **Probe:** length, size, fps. Use the ffmpeg from the `imageio-ffmpeg` pip wheel (`pip install imageio-ffmpeg` in a venv) because Homebrew ffmpeg is not installed. Reference videos are 640–720 px wide; that is fine for analysis.
3. **Scene cuts:** `-vf "select='gt(scene,0.2)',showinfo" -f null -` and read the `pts_time` values. Zero cuts means a continuous morphing scene (note it, that is a technique).
4. **Frame sheets:** `-vf "fps=4,scale=200:-1,tile=8x2" frames_refNN_<topic>/sheet_%02d.jpg`. Each sheet = 4 s (16 tiles at 4 fps, left→right, top→bottom). Read **every** sheet; never describe a video from its file name or from a few frames.
5. **Detail frames:** 2–3 full-res frames at typography-heavy moments, scaled to the *same* height (`scale=360:640`, or `hstack` fails on a 1-px height mismatch).
6. **Numbers:** luma and saturation (`fps=2,signalstats`, average `YAVG`/`SATAVG`), audio onsets (spike detection on 20 ms RMS), mean loudness, and `silencedetect` for pauses. Report them; do not guess "dense" or "sparse" without them.
7. **Write** `experiment/NN_references_<a>-<b>_analysis.md`: file table, one beat table per video (time / text / visual / motion), grade + audio notes, and a "what is new vs earlier references" list.
8. **Fold into `motion-graphics-style`:** add only genuinely new patterns, tag them `*(refNN)*`, and update the skill's description ("learned from N reels") and source list. Merge a repeat of an existing pattern into the existing bullet instead of duplicating it.
9. **Report to Deepak in one short message:** what each video really is, the new patterns, and where they were saved.

**Tooling gotchas (this Mac):** for any reference whose point is *motion quality*, measure the easing instead of guessing it: `_video-analysis-tools/track.py` follows one shape at 60 fps (width, centre, area, brightness) and prints duration, t10/t50/t90 against easing templates and overshoot; `gsheet.py` makes time-labelled contact sheets for 16:9, 1:1 and 9:16 (both take the ffmpeg path in the `FF` env var; run with `python -I`). Tracking is noisy when a shape blurs or changes colour mid-move, so label those readings "by eye". No `drawtext` fonts, so draw time labels with PIL; `pip install` needs a venv (system Python is 3.9); frame sheets and other scratch files go in the session scratchpad, not `/tmp`.
- **YouTube downloads (ref69, 2026-10-09):** the pip `yt-dlp` on Python 3.9 fails with *"The page needs to be reloaded"*. Download the official standalone `yt-dlp_macos` binary from the yt-dlp GitHub releases, verify it against the release's `SHA2-256SUMS`, and run it with `--js-runtimes node`. Say so to Deepak, since it is a download.
- **ffmpeg:** `pip install imageio-ffmpeg` inside the venv; the binary is in `site-packages/imageio_ffmpeg/binaries/` (export it as `FF`). The older scripts in `_video-analysis-tools/` hardcode a deleted path, so pass `FF` instead.
- **Generic helpers saved in `_video-analysis-tools/` (ref69):** `motion_curve.py` (60 fps frame-difference, luma and saturation per second, finds hard cuts), `band_onsets.py` (loudness, energy per band, per-band onset times, 1 s RMS profile) and `spectrogram_log.py` (log-frequency spectrogram PNG plus tempo guess). All take the ffmpeg path or a mono WAV as arguments, run with `python -I`.
- **Split-screen references (panels stacked in one frame):** find the panel bounds from a saturated pixel column first, then crop each panel and build the frame sheets per panel (a whole-frame sheet wastes 60 % of the tile on white page).

**Quality rule:** analysis must distinguish what is *seen* (timings, colours, text) from what is *inferred* (fonts, easing, sound type). Say "looks like Montserrat" or "probably a whoosh", never state an inferred fact as certain.
