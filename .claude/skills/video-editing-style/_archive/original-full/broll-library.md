---
name: broll-library
description: Catalog of all 272 B-roll clips/images in "brolls for claude/" with what each shows and when to use it. Use whenever editing a video, placing B-roll on a script/voiceover line, searching for footage (coding, AI, college, exams, money, salary, jobs, motivation, emotions, flags, social-media CTAs, icons, backgrounds, transitions), or asked "which B-roll fits this part?".
---

# B-roll Library

Folder: `/Users/raghusai/Downloads/claude/brolls for claude/`
Full descriptions: [catalog.md](catalog.md) — every file has **Shows / Use when / Info / Keywords / ⚠ Note**.

## How to pick a B-roll for a script line
1. Load `my-editing-rules` first — Deepak's personal rules override this file.
2. Get the *meaning* of the line (e.g. "I was stuck for months" = confusion/stuck, not "months").
3. Scan the category index below, then read the full entries in `catalog.md` (`grep -i -B2 -A5 '<keyword>' catalog.md`) and compare the **Use when** lines.
4. Pick 1 main choice + 1 backup per line, ⭐ Pro first. Give the filename exactly as written (spaces and odd names included), plus a trim if the clip is long.
5. Always read the ⚠ **Note** — some clips need trimming (credits or promo cards at the end), rotating, or have watermarks.
6. If nothing fits well, say so. Don't force a weak match — suggest what kind of B-roll to download instead.

## Professional-first rule (Deepak, 2026-09-29)
These folders are Deepak's everyday editing kit. **Always pick the most professional-looking asset.** Every catalog entry has a **Quality** line:
- ⭐ **Pro:** clean, sharp enough for a 1080×1920 reel, no third-party watermarks. **Default choice.**
- ✅ **Usable:** fine *with care*. It's soft full-screen (use it framed, split-screen or small), needs a trim/rotate/cleanup, or carries copyright risk. Use only if no ⭐ fits, and state the fix needed.
- ⛔ **Avoid:** watermarked, burned-in foreign captions, too low resolution, other creators' promo cards, or a duplicate. Don't use it in a final edit; suggest a replacement to download instead.

If only ✅/⛔ assets fit a line, say so and suggest what pro B-roll to source instead of settling.

## Technical rules (derived from the files themselves)
- **Green-screen clips** (style says green-screen): apply a chroma key / Ultra Key. Examples: `comment.mp4`, `dollar.mp4`, `save.mp4`, `share.mp4`, `tech boy follow.mp4`, `subscribe button .mp4`, `mobile view.mp4` (green phone screen — put footage inside it).
- **Black-background motion graphics** (icons, arrows, neon, light leaks, `Money .mp4`, `cash .mp4`): use **Screen** or **Add** blend mode so the black disappears.
- **Real transparency:** only `Money Rain.mp4.mov` (ProRes 4444) — overlay directly. `follow.mp4` *looks* transparent, but the checkerboard is printed into the H.264 video, so it needs keying or masking.
- **Orientation:** check the **Info** field. Horizontal clips in a 9:16 reel need scale/crop or a blurred-background fill.
- **Templates** (`template*`, `templates*`) are empty animated backgrounds for text or explainer slides. Don't use them as story B-roll.
- **Branded assets for CTAs/outros:** `tbd.mp4`, `outro.mp4`, `subscribe button .mp4`, `tech boy follow.mp4`. `abhi follow button.mp4` and `bargav follow button.mp4` are *other creators'* cards — use them only when mentioning those people.
- Known duplicates: `AI 1.mp4` = `aiii.mp4`; `typing.mp4` = `typing 3.mp4`.

## Category index (⭐ Pro · ✅ Usable · ⛔ Avoid)
- **Coding, laptops & tech setups**
  - ⭐ `87.gif`, `arrange.mp4`, `coding 3.mp4`, `coding 4.mp4`, `edit.mp4`, `game set up.mp4`, `laptop 1.mp4`, `laptops.mp4`, `mouse.mp4`, `work 1.mp4`, `work.mp4`
  - ✅ `coding 1.mp4`, `coding 2.mp4`, `codings.mp4`, `editing 1.mp4`, `editing.mp4`, `laptop.mp4`, `typing 1.mp4`, `typing 3.mp4`
  - ⛔ `typing.mp4`
- **AI, tech companies & logos**
  - ⭐ `ai flow.mp4`, `ai tools.mp4`, `chips.mp4`, `drive.jpeg`, `google logo.mp4`, `insta .mp4`, `microsoft.mp4`, `python.mp4`
  - ✅ `2ef870a917d917edcbeb721c88420269.jpg`, `AI 1.mp4`, `insta logo.jpg`, `meta png.jpeg`
  - ⛔ `aiii.mp4`, `faang.jpeg`
- **Electronics (ECE), factories & engineering**
  - ⭐ `ece 1.mp4`, `ece 3.mp4`, `ece 4.mp4`, `ece 6.mp4`, `ece.mp4`, `energy .mp4`, `factory 1.mp4`
  - ✅ `factory.mp4`
- **Study, exams & books**
  - ⭐ `From KlickPin CF Creative Book Reveal – Motion Inspiration _ Video.mp4`, `list.jpg`, `maths.mp4`, `study 3.mp4`, `study 5.mp4`, `studying.mp4`, `write 1.mp4`, `writing.mp4`
  - ✅ `book 1.mp4`, `books.mp4`, `study 1.mp4`, `write.mp4`
  - ⛔ `study 2.mp4`, `study 4.mp4`
- **College, school & students**
  - ⭐ `class 2.mp4`, `college.mp4`, `discuss 1.mp4`, `enjoy.png`, `fees video.mp4`, `graduate.mp4`, `hope students.png`, `stage fear.mp4`, `student.png`, `students.png`
  - ✅ `class 1.mp4`, `college 1.mp4`, `parents.mp4`, `school.mp4`
  - ⛔ `class.mp4`
- **Jobs, office, meetings & interviews**
  - ⭐ `From Klickpin.com- Discover Trending small kitchen organization for your next inspiration board using ideas that balance beauty and everyday funct.mp4`, `From Main Klickpin CF- Man taking property of orphan - lcLrO1H7G.mp4`, `bag video.mp4`, `boss.mp4`, `call .mp4`, `discuss 2.mp4`, `discuss.mp4`, `friends.mp4`, `i Handshake.mp4`, `interview 1.mp4`, `interview 2.mp4`, `meetings.mp4`, `office bag.mp4`, `office work.mp4`, `students.mp4`
  - ✅ `interview.mp4`, `meeting 1.mp4`
- **Money, salary, payments & finance**
  - ⭐ `Digital pay 1 .mp4`, `Money .mp4`, `Money Rain.mp4.mov`, `cash .mp4`, `cash.png`, `coin.jpg`, `digital pay.mp4`, `dollar.mp4`, `ece 5.mp4`, `money 1.mp4`, `money chase.mp4`, `money count.mp4`, `money graph.mp4`, `money lose.mp4`, `money smell.mp4`, `money.mp4`, `moneys.mp4`, `pursue.mp4`, `tax.mp4`, `trading 1.mp4`
  - ✅ `money 2.mp4`, `money machine.mp4`
  - ⛔ `hook.jpg`
- **Emotions & people (confused, stressed, sad, shocked, crowds)**
  - ⭐ `211052630dea3ffefda0596d193be199_720w.mp4`, `angry.png`, `burden.jpg`, `cbd95149bd6ac829583c53b12aaa5cfd.jpg`, `confusee.jpg`, `doubts.mp4`, `doubtssss.jpg`, `explain.jpg`, `eyes.mp4`, `mobile use.mp4`, `peoples.mp4`, `sad .mp4`, `shock.mp4`, `sleep.mp4`, `stress.png`, `toy.mp4`, `unknown man.jpg`
  - ✅ `confuse boy.mp4`, `confuse.jpg`, `peoples 1.mp4`, `time pass.mp4`
  - ⛔ `pngtree-surprised-expressive-happy-man-celebrating-with-excitement-png-image_16504464.png`
- **Motivation, success, growth & ideas**
  - ⭐ `726e40b9a3d5f4ca43c48bb84a363f3e.mp4`, `bow.mp4`, `brain.mp4`, `brains.mp4`, `bulb.mp4`, `c1f327799c7c2a0c34b469c7b434580f.jpg`, `chess.mp4`, `exercise.mp4`, `eye.mp4`, `graph 1.mp4`, `help.mp4`, `idea.png`, `lv_0_20260526163945.mp4`, `man.jpeg`, `motivate.mp4`, `rise.mp4`, `running.mp4`, `sucess.jpg`, `think.jpeg`, `traingle.mp4`, `ups 1.mp4`, `ups.mp4`
  - ✅ `batman.mp4`, `dream.mp4`, `fall.mp4`, `hands mp4.mp4`, `ideas.jpg`, `route.mp4`, `star png.jpg`, `superman.mp4`, `trophy.jpeg`, `win.mp4`
- **Social media, engagement & Tech Boy Deepak branding**
  - ⭐ `chat.png`, `comment.mp4`, `like.mp4`, `message.mp4`, `mobile view.mp4`, `outro.mp4`, `save.mp4`, `savee.mp4`, `share button.mp4`, `share.mp4`, `social media.mp4`, `sub button.mp4`, `subscribe button .mp4`, `tbd.mp4`, `tech boy follow.mp4`, `views increse.mp4`
  - ✅ `abhi follow button.mp4`, `bargav follow button.mp4`, `follow.mp4`, `sent.mp4`, `views.mp4`, `viewsss.mp4`
  - ⛔ `upload.mp4`
- **Icons, arrows, counters & motion-graphic elements**
  - ⭐ `10 min.mp4`, `73 Family Dinner Ideas for Weekends - Pin-1084874997737814236.mp4`, `From KlickPin CF think3 _ Digital Marketing Agency Derby on Instagram Circles in motion 🟣 Drawing inspi...recent project we conducted a small study on shape anima… _ Motion design Motion design animation Motion graphics design.mp4`, `arrow 1.mp4`, `arrow 2.mp4`, `arrows.mp4`, `ball.mp4`, `battery icon.mp4`, `bubble.mp4`, `cd2bcdf6808749bc0ffa83572507a4b0.jpg`, `circle.mp4`, `correct.mp4`, `dates.mp4`, `document.mp4`, `e9aed732150bd7df4643302e146fdd91.jpg`, `finding.mp4`, `i Home.mp4`, `loading.mp4`, `loadingg.mp4`, `maps.mp4`, `numbers.mp4`, `on png.mp4`, `reuse.mp4`, `ring.mp4`, `smoke.mp4`, `sound video.mp4`, `sound.mp4`, `timee.mp4`, `vibrate.mp4`, `wrong.mp4`, `years.mp4`
  - ✅ `80 perc.mp4`, `arrow.mp4`, `arrowss.mp4`, `count.mp4`, `numberss.mp4`, `roadmap.mp4`
- **Countries, flags, maps & Earth**
  - ⭐ `UAE.mp4`, `china.mp4`, `earth video.mp4`, `earth.mp4`, `india png.jpeg`, `map.mp4`
  - ✅ `india flag.mp4`, `indo map.mp4`, `iran map.mp4`, `japan flag.mp4`, `saudi arabia.mp4`
- **Health, lifestyle, cars, food, movies & misc**
  - ⭐ `covid.mp4`, `driving .mp4`, `food test.mp4`, `old age.mp4`, `photography.mp4`, `play game.mp4`, `premium.mp4`
  - ✅ `anime 1.mp4`, `anime 2.mp4`, `anime 4.mp4`, `body.mp4`, `car 1.mp4`, `elonmusk.mp4`, `hollywood.mp4`, `popcorn png.jpeg`
  - ⛔ `health issue.mp4`, `health.mp4`, `heart beat.mp4`, `images.jpeg`
- **Backgrounds, templates & transitions**
  - ⭐ `template 16.mp4`, `template 2.mp4`, `template 3.mp4`, `template 4.mp4`, `template 5.mp4`, `template 6.mp4`, `template 7.mp4`, `template 8.mp4`, `template 9.mp4`, `template1 .mp4`, `templates 10.mp4`, `templates 11.mp4`, `templates 13.mp4`, `transisition.mp4`, `transistion .mp4`
  - ✅ `template 15.mp4`, `transisition 1.mp4`
- **Audio (not B-roll):** `ES_Relentless Pursuit - Howard Harper-Barnes.mp3`

## Rules learned from Deepak
_(Added by `skill-saver` — B-roll choices Deepak liked or rejected, and why.)_

## Maintenance
New or removed files → follow `skill-saver` section 4 (frame extractor: `scripts/sheet.swift`).
