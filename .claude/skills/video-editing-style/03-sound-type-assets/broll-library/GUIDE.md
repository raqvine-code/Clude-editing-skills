---
name: broll-library
description: Use when editing a video, placing B-roll on a script/voiceover line, searching footage (coding, AI, college, exams, money, jobs, motivation, emotions, flags, social CTAs, icons, backgrounds, transitions), or asked "which B-roll fits this part?". Index, technical rules and selection method for the 272 clips in "brolls for claude/"; per-file entries are in catalog.md.
---

> **Scope: asset catalog. Describes the 272 clips on Raghu's Mac (see PATHS-AND-SETUP.md). The clips are NOT in this zip; grep catalog.md first, then fetch the file from the Mac.**

# B-roll library

Folder: `/Users/raghusai/Downloads/claude/brolls for claude/`. 272 visual files plus 1 audio file.
`catalog.md` (copied unchanged): one section per category, each file has Shows / Use when / Quality / Info (duration, resolution, style) / Keywords / optional warning. Search with `grep -i -B2 -A5 '<keyword>' catalog.md`. `scripts/sheet.swift` builds a 4-frame contact sheet via AVFoundation (prints duration|WxH).

## Picking B-roll for a line
1. Load `my-editing-rules` first; it overrides this file.
2. Get the meaning of the line ("stuck for months" = confusion, not "months").
3. Scan the index, then compare Use-when lines in catalog.md.
4. Give 1 main + 1 backup, Pro first, exact filename (spaces and odd names included), plus a trim if long.
5. Read the warning note: some clips need trimming (credits/promo cards), rotating, or have watermarks.
6. If nothing fits, say so and suggest what to download; do not force a weak match.
7. **Stock titles and search results can lie: look at the frames before using a download** (2026-11-26: Pexels 34565141, found for "Bhagavad Gita", is a Hindi wedding programme card). A wrong religious or cultural object is worse than no B-roll; use a public-domain museum image (Wikimedia Commons) instead.
8. On white phone screens and paper-white artwork the caption needs ink lead-ins + a deep-haldi keyword with the ink outline (and `shade: false`); cream type on white does not read.

## Professional-first rule (2026-09-29)
Pro = sharp for 1080x1920, no third-party watermark (default). Usable = soft (use framed/split/small), or needs trim/rotate/cleanup, or copyright risk; state the fix. Avoid = watermarked, burned-in foreign captions, too low-res, other creators' promo cards, duplicates; suggest a replacement. If only Usable/Avoid fit, say so.

## Technical rules
- Green-screen clips (chroma key / Ultra Key): `comment.mp4`, `dollar.mp4`, `save.mp4`, `share.mp4`, `tech boy follow.mp4`, `subscribe button .mp4`, `mobile view.mp4` (green phone screen, put footage inside).
- Black-background graphics (icons, arrows, neon, light leaks, `Money .mp4`, `cash .mp4`): Screen or Add blend.
- True transparency only in `Money Rain.mp4.mov` (ProRes 4444). `follow.mp4` has a checkerboard printed in, so key or mask it.
- Check orientation in Info; horizontal clips in a 9:16 reel need scale/crop or blurred-background fill.
- `template*` / `templates*` are empty animated backgrounds for text/explainer slides, not story B-roll.
- Branded CTA/outro assets: `tbd.mp4`, `outro.mp4`, `subscribe button .mp4`, `tech boy follow.mp4`. `abhi follow button.mp4` and `bargav follow button.mp4` belong to other creators; use only when mentioning them.
- Duplicates: `AI 1.mp4` = `aiii.mp4`; `typing.mp4` = `typing 3.mp4`.

## Category index (counts of Pro entries are large; see catalog for filenames)
Coding/laptops/tech setups; AI, tech companies and logos; Electronics (ECE), factories, engineering; Study, exams, books; College, school, students; Jobs, office, meetings, interviews; Money, salary, payments, finance (many Pro: cash, digital pay, graphs, tax, trading, Money Rain); Emotions and people (confused, stressed, sad, shocked, crowds); Motivation, success, growth, ideas; Social media, engagement and Tech Boy Deepak branding; Icons, arrows, counters, motion-graphic elements; Countries, flags, maps, Earth; Health, lifestyle, cars, food, movies, misc; Backgrounds, templates, transitions; Audio (one Epidemic Sound track, not B-roll).
Notable Avoid items: `typing.mp4`, `aiii.mp4`, `faang.jpeg`, `class.mp4`, `study 2.mp4`, `study 4.mp4`, `hook.jpg`, `upload.mp4`, health clips, `images.jpeg`, a pngtree watermarked image.

## Maintenance
Rules learned from Deepak are appended here by `skill-saver`. New/removed files: follow `skill-saver` section 4.


Full original notes (every detail, uncut): `_archive/original-full/broll-library.md` in this folder.
