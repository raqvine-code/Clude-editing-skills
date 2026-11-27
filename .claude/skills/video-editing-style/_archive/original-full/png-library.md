---
name: png-library
description: Catalog of all 78 PNG/pop-up images in "png for claude/" (logos, AI robots, number stickers, exam/study props, money, reactions, places) with what each shows, when to pop it up, and how to prep it (transparent vs white/black/checkerboard background). Use whenever adding pop-up images, stickers, logos or overlays to a video, or asked "which PNG fits here?".
---

# PNG / Pop-up Library

Folder: `/Users/raghusai/Downloads/claude/png for claude/`
Full descriptions: [catalog.md](catalog.md) — every file has **Shows / Use when / Info / Prep / Keywords / ⚠ Note**.

## How to pick a pop-up for a script line
1. Load `my-editing-rules` first — Deepak's personal rules override this file.
2. A PNG pops up on the **exact word** it illustrates (brand name, object, number, emotion). Match nouns and names literally ("Amazon" → Amazon logo). Match emotions and concepts by the **Use when** line.
3. Scan the index below, then confirm in `catalog.md` (`grep -i -B2 -A6 '<keyword>' catalog.md`).
4. Always check **Prep**. Most files are NOT transparent even when named `.png`.

## Professional-first rule (Deepak, 2026-09-29)
These folders are Deepak's everyday editing kit. **Always pick the most professional-looking asset.** Every catalog entry has a **Quality** line:
- ⭐ **Pro:** clean edges, sharp, no watermarks — true transparency or an easy blend/cutout. **Default choice.**
- ✅ **Usable:** fine *with care*. It's small, has a fake checkerboard that needs background removal, or has a faint watermark. Use only if no ⭐ fits, and state the fix needed.
- ⛔ **Avoid:** visible stock watermarks, tiny, or a duplicate. Don't use it in a final edit; suggest a replacement to download instead.

If only ✅/⛔ assets fit a line, say so and suggest what pro PNG to source instead of settling.

## Background / prep cheat-sheet
- **Truly transparent, ready to overlay:** `Clock.png`, `coding.png`, `fall png.png`, `scalarr.png`.
- **White background** → Multiply blend (on light footage) or remove the background.
- **Black background** (number stickers, `microsoft.jpg`, `cursor.jpeg`, `settings icon.png`) → Screen blend.
- **Fake checkerboard printed into the image** (`ai 2.jpg`, `atm.jpeg`, `books.jpeg`, `building.jpg`, `bus.jpeg`, `delivery boys.jpg`, `drone.jpeg`, `hand.jpg`, `money.jpg`, `pani puri.jpeg`, `test paper.jpeg`) → must remove the background. A blend mode won't work on these.
- **Full-frame images, not stickers** (`black.jpeg`, `letter.jpg`, `coding.jpg`, `trap.jpg`, both `ChatGPT Image ...png`, `d9874cf...jpg`, `mask.png`) → use as a full-screen cutaway, or cut out the subject.
- Watermarked files are flagged in ⚠ notes. Keep them small or avoid them in final exports.

## Gotchas
- `1 number sticker_motion graphics (1).jpeg` actually shows **5**. `4.jpeg` duplicates the 4 sticker. Number set available: 1–6.
- `eapcet jpeg.jpeg` is the TSCHE seal (Telangana council behind TS EAPCET), not an "EAPCET" logo.
- `gift.png` is a broken macOS shortcut, not an image.

## Category index (⭐ Pro · ✅ Usable · ⛔ Avoid)
- **Number stickers (list/step counters)**
  - ⭐ `1 number sticker_motion graphics (1).jpeg`, `1 number sticker_motion graphics.jpeg`, `2 number sticker_motion graphics.jpeg`, `3 number sticker_motion graphics.jpeg`, `4 number sticker_motion graphics.jpeg`, `6.jpeg`
  - ⛔ `4.jpeg`
- **Brand, app & company logos**
  - ⭐ `Amazon logo.pngg.jpeg`, `Amazon.jpeg`, `Gmail logo.jpeg`, `Scaler_Logo_WhiteBG (1).jpg`, `chatgpt.jpg`, `claude.jpg`, `cursor.jpeg`, `facebook logo.jpeg`, `gmail.jpeg`, `infosys.jpeg`, `microsoft.jpg`, `myntra.jpg`, `reel .jpeg`, `scalarr.png`, `settings icon.png`, `uber logo png.jpg`, `yt.jpeg`
- **AI, robots & tech gadgets**
  - ⭐ `ai 1.jpg`, `ai.jpg`, `coding.jpg`, `coding.png`, `robo.jpg`
  - ✅ `ai 2.jpg`, `hand.jpg`, `laptop.jpg`
  - ⛔ `drone.jpeg`
- **Study, exams, college & documents**
  - ⭐ `book.jpg`, `books.jpg`, `certificate png.jpeg`, `eapcet jpeg.jpeg`, `exam.jpg`, `file.jpg`, `letter.jpg`, `papers.jpg`, `scholar.png`
  - ✅ `books.jpeg`, `test.jpeg`
  - ⛔ `test paper.jpeg`
- **Money & payments**
  - ⭐ —
  - ✅ `atm.jpeg`, `money.jpg`
- **People, reactions & concepts**
  - ⭐ `30834b30e608bc6ae177ace2c61eb32e.jpg`, `ChatGPT Image Nov 2, 2025, 03_38_24 PM.png`, `ChatGPT Image Oct 11, 2025, 11_45_34 PM.png`, `Clock.png`, `d9874cf39316445896bd70980c9817c1.jpg`, `doubt.jpg`, `doubts .jpeg`, `doubts.jpg`, `fall png.png`, `go.jpeg`, `mask.png`, `me.jpeg`, `question.jpeg`, `tech boy deepak .jpeg`, `thug.jpg`, `trap.jpg`, `you.jpg`, `yt man.jpeg`
  - ✅ `kid.png`
  - ⛔ `layer png.jpeg`
- **Places, buildings, transport, food & objects**
  - ⭐ `bullet train.jpeg`, `hospital.jpeg`, `time png.jpg`
  - ✅ `black.jpeg`, `bus.jpeg`, `delivery boys.jpg`, `hyd.jpg`, `ticket png.jpeg`
  - ⛔ `building.jpg`, `cafe.jpeg`, `pani puri.jpeg`

## Rules learned from Deepak
_(Added by `skill-saver` — pop-up choices, sizes, positions and animations Deepak liked or rejected, and why.)_

## Maintenance
New or removed files → follow `skill-saver` section 4.
