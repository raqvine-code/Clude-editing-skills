---
name: png-library
description: Use when adding pop-up images, stickers, logos or overlays to a video, or asked "which PNG fits here?". Index and prep rules for the 78 images in "png for claude/" (logos, AI robots, number stickers, exam props, money, reactions, places); full per-file entries are in catalog.md.
---

> **Scope: asset catalog. Describes the 78 pop-up images on Raghu's Mac (see PATHS-AND-SETUP.md). The images are NOT in this zip.**

# PNG / pop-up library

Folder: `/Users/raghusai/Downloads/claude/png for claude/` (`Png's/` is a duplicate). 78 images plus 1 broken shortcut.
`catalog.md` (copied unchanged): sections per category, each file has Shows / Use when / Quality / Info (resolution, style, background) / Prep / Keywords / optional warning note. Search with `grep -i -B2 -A6 '<keyword>' catalog.md`.

## Picking a pop-up
1. Load `my-editing-rules` first; Deepak's personal rules override this file.
2. Pop the image on the exact word it illustrates (brand, object, number, emotion). Match nouns literally ("Amazon" -> Amazon logo); match emotions/concepts via the Use-when line.
3. Scan the index below, confirm in catalog.md, and always read Prep: most files are not transparent despite `.png`.

## Professional-first rule (2026-09-29)
Always choose the most professional asset. Quality tags: Pro = clean, sharp, no watermark (default); Usable = fine with care (small, fake checkerboard, faint watermark; state the fix, use only if no Pro fits); Avoid = visible watermark, tiny or duplicate (suggest a replacement to source). If only Usable/Avoid fit, say so.

## Prep cheat-sheet
- Truly transparent: `Clock.png`, `coding.png`, `fall png.png`, `scalarr.png`.
- White background: Multiply blend on light footage, or remove background.
- Black background (number stickers, `microsoft.jpg`, `cursor.jpeg`, `settings icon.png`): Screen blend.
- Fake checkerboard baked in (`ai 2.jpg`, `atm.jpeg`, `books.jpeg`, `building.jpg`, `bus.jpeg`, `delivery boys.jpg`, `drone.jpeg`, `hand.jpg`, `money.jpg`, `pani puri.jpeg`, `test paper.jpeg`): must remove background; blend modes will not work.
- Full-frame images, not stickers (`black.jpeg`, `letter.jpg`, `coding.jpg`, `trap.jpg`, both `ChatGPT Image ...png`, `d9874cf...jpg`, `mask.png`): use as full-screen cutaway or cut out the subject.

## Gotchas
- `1 number sticker_motion graphics (1).jpeg` actually shows 5; `4.jpeg` duplicates the 4 sticker; number set is 1-6.
- `eapcet jpeg.jpeg` is the TSCHE seal (council behind TS EAPCET), not an EAPCET logo.
- `gift.png` is a broken macOS shortcut.

## Category index (Pro / Usable / Avoid)
- Number stickers: Pro = the six number-sticker files (1-5 via the `N number sticker_motion graphics` files, 6 = `6.jpeg`); Avoid `4.jpeg`.
- Brand/app/company logos: Pro = Amazon (2 files), Gmail (2), Scaler, ChatGPT, Claude, Cursor, Facebook, Infosys, Microsoft, Myntra, reel, scalarr, settings icon, Uber, YouTube.
- AI, robots, gadgets: Pro `ai 1.jpg`, `ai.jpg`, `coding.jpg`, `coding.png`, `robo.jpg`; Usable `ai 2.jpg`, `hand.jpg`, `laptop.jpg`; Avoid `drone.jpeg`.
- Study, exams, college, documents: Pro book(s), certificate, eapcet, exam, file, letter, papers, scholar; Usable `books.jpeg`, `test.jpeg`; Avoid `test paper.jpeg`.
- Money and payments: no Pro; Usable `atm.jpeg`, `money.jpg`.
- People, reactions, concepts: Pro doubt/doubts (3), question, thug, trap, mask, go, me, you, yt man, tech boy deepak, Clock, fall, two ChatGPT images and two hash-named images; Usable `kid.png`; Avoid `layer png.jpeg`.
- Places, buildings, transport, food, objects: Pro `bullet train.jpeg`, `hospital.jpeg`, `time png.jpg`; Usable `black.jpeg`, `bus.jpeg`, `delivery boys.jpg`, `hyd.jpg`, `ticket png.jpeg`; Avoid `building.jpg`, `cafe.jpeg`, `pani puri.jpeg`.
(Exact filenames are in catalog.md.)

## Maintenance
Rules learned from Deepak get appended here by `skill-saver`. New/removed files: follow `skill-saver` section 4.


Full original notes (every detail, uncut): `_archive/original-full/png-library.md` in this folder.
