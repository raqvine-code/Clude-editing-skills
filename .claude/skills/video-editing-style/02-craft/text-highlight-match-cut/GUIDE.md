---
name: text-highlight-match-cut
description: Use in every video edit when the script quotes a source, cites a number/fact, names a person/company/tool, says "according to…" / "reports say…" / "search…", or needs proof or an evidence montage. Covers (1) brush-stroke text HIGHLIGHT on article/news/screenshot text (yellow marker wipe, Dhruv Rathee style) and (2) the keyword-anchored MATCH CUT (one highlighted word pinned while 5-7 sources flash behind it every 3-4 frames), plus capture workflow and variants.
---

# Text highlight (HL) + match cut (MC)

Deepak's must-use effects: simple but they create demand. Every edit plan must contain at least one HL beat and, where the script allows, one MC beat. Flag them in the plan as `HL` and `MC`. If the plan has zero of either, say why.

## 1. Highlight (HL)
**When:** on-screen text that proves what is being said: headline, article line, Wikipedia/Google result, salary figure on a job site, syllabus line, tweet, DM screenshot, document, terminal/log line (coding), patch notes (gaming).

**Recipe (CapCut):**
1. Place the screenshot on a soft, dark, slightly blurred background (blurred newsroom photo with dust, or a B-roll "backgrounds" clip). Scale so the target line is **>= 40 px tall on a 1080x1920 canvas**; add a drop shadow.
2. Add a rough-edged brush/marker stroke (Canva "paint brush stroke" or CapCut "marker highlight" sticker): colour **#F5C400**, rotated -1 to -2 deg, height about **1.3x line height**, ends overshooting the words by 2-4 %.
3. Layer: stroke below the text only if the screenshot is transparent; otherwise stroke above at **75-85 % opacity, Multiply blend** so black text stays crisp.
4. Reveal with a **linear mask wipe left to right**, ease-out, no bounce: 0.4-0.7 s for a headline, up to 1.5 s for a long body line (keep tighter than ref12's 1.5-2 s).
5. Start the wipe **on the spoken word** (at most 1 frame late). Optional soft marker/swish SFX at -18 dB, or nothing under captions.
6. **One line per beat**; a second only if the voice reads it. Never highlight a paragraph.
7. Same yellow all video. On dark UI (terminal, Discord, dark sites) use the same yellow at 60 % Multiply or a yellow **underline stroke** (screen blend on dark pages).

## 2. Match cut (MC)
**When:** the script says something is everywhere / repeated / searched / reported by many ("every site says…", "search his name…", "10 companies posted the same…"), or a name/number needs weight. Also the quick evidence montage in documentaries and "everyone is talking about this patch" in gaming.

**Recipe:**
1. Anchor = the highlighted keyword (or logo/number). Build **5-7 sources** containing it, each with a different layout, font, size and density so every cut reads as a new document (about-page, Wikipedia, news, quote spread, spotlight, wiki overview, home page). Off-white paper texture, near-mono, only the highlight in yellow.
2. **Pin the anchor to one exact screen position** (ref13: about 38 % from top, left edge about 20 % of width). Reposition/scale every source so its word lands there. The word never moves, the world jumps.
3. **Cut every 3-4 frames** (0.10-0.13 s); ref13 has 17 cuts in 2.3 s. For longer beats loop the same order instead of adding sources.
4. Directional motion blur (CapCut Blur-motion or a 2-frame zoom-blur) on the **backgrounds only**, not the anchor.
5. Sound: whoosh-in on the first cut, one continuous tick/texture bed under the run (bed -11 to -13 dB under a hook line), one **hit on the last cut**. No tick per cut.
6. Exit: white flash from a corner (5-6 frames) into the next shot or a small label, or a hard cut back to the talking head on the next spoken word.
7. **One MC run per 20-30 s of video**, and after a highlight beat that introduced the anchor (HL then MC is one system).

## 3. Variants by subject
- Gaming: anchor = weapon/character/patch line; sources = patch notes, Reddit, tweet, wiki, YouTube title.
- Documentary: anchor = name or date; sources = clippings, court doc, Wikipedia, book page, tweet.
- Tech: anchor = tool/company/price; sources = docs, pricing page, README, Play Store, news.
- Deepak's student/career reels: anchor = college name, salary, company logo, "EAPCET"; sources = counselling site, LinkedIn jobs, Glassdoor, news, official PDF.

## 4. QC
- Anchor drift <= 2 px between cuts (scrub frame by frame).
- Wipe starts on the word; yellow identical across the video; text readable.
- Max one HL per beat, one MC run per 20-30 s.

## 5. No source documents (IKKO MindOne variant; Claude's adaptation, not yet approved)
- **HL on the product name**: dark-UI underline stroke wiped left to right on the spoken word (0.5 s) under the type-on, in the video's accent (sampled from the product screen, e.g. periwinkle) instead of yellow, unless Deepak wants classic yellow. Marker weight: 0.44 em behind the lower half of the letters, deeper accent for contrast; same stroke on name and anchor.
- **MC recalls that name** pinned at 38 % height on a dark radial scrim, on the line meaning "many". Sources = the review's own B-roll, one feature per shot. Final: **6 shots x 6 frames at 60 fps (0.1 s)**, backgrounds dimmed 25 %, each reframed at scale 1.25 so the phone sits under the word, each whipping in 40 px and settling (expo.out, 24-sample motion blur); anchor never moves. Whoosh in, tick bed, sub + whoosh on the last cut, **hard cut** onto his face. (The 8-shot version with a corner white flash was judged flickery/preset-like.)
- **Never fabricate a source screenshot** (product page, article). If none exists use this variant and say so in the plan.

## 6. Real-source capture (video 13 v2)
- `capture.js` (puppeteer, 1600x900, DPR 2): load the article, hide cookie/consent/paywall overlays with CSS (never click them), find the Nth regex text match, scroll it to centre, save PNG + the phrase's client rects as JSON. Worked: TechCrunch, The Stack, The New Stack, Illinois Tech, Accel job board; Sifted's paywall covered the text, so dropped.
- HL: real TechCrunch headline (white on green), #F5C400 multiply at **78 % of line height**, wiped left to right on the word; **include the currency sign** in money highlights ($1 billion); source tag bottom-left.
- MC: re-capture each source with the anchor regex alone ("forward[- ]deployed"); scale each page so the rect height equals one line height (**92 px**) and pin its left/top at **(560, 470)**; background at 62 % brightness, anchor crop at full brightness with yellow behind; **5 sources x 0.1 s x 2 loops**, hit on the last cut, then hold.

## 7. MC on a company name across real headlines (AI Tech News ep 02)
- Pin one company ("OpenAI") over 7 real headlines of the fortnight, 0.1 s each x 2 loops, landing on the story being introduced.
- Measure the anchor word on each page with `textbox.py` word runs; dark pages need the marker in screen blend.
- **Never zoom out a clipped MC layer** (the page is cut at the layer edge). Fade the pinned page and hand off to a separately cropped headline card, then highlight the new words.

## 8. Real public-domain text page (16. Uncertainty Short v2, 2026-11-16)
- Ask once before any web capture. Then capture with `capture_page.js` (in `edited videos by claude/16. Uncertainty Short/code/`; env `VW VH DPR TOPY`): hides overlays with CSS, clicks nothing, saves PNG + phrase rects JSON.
- Scroll with `document.scrollingElement`. On Wikisource, an `html,body{overflow:auto}` override left `window.scrollBy` doing nothing (the phrase stayed at y 8246).
- Read edition, year and verse number off the captured page, never from memory: the plan said Besant 1905, the page header said 1922 (4th edition); verse checked by "(47)" and "॥ ४७ ॥".
- Wikisource "Layout 2" keeps a fixed ~576 CSS px text column; a narrow viewport or the mobile site does not rewrap it (the mobile capture cut lines off). Use the desktop page and crop the column full-bleed on 1080: 1.7 canvas px per CSS px gives 27 px text and a 44 px line (meets the 40 px rule), with the verse number still in frame after a 105 % push.
- Build: page band with top/bottom fades into ink; the marker sits inside the same isolated band as the page image so multiply blends (black text stays crisp); rough edge = seeded SVG `feTurbulence` + `feDisplacementMap` (static, no boil); wipe = per-frame `clip-path: inset()` ease-out. 1.25x the glyph box keeps the marker off the neighbouring lines.
- Captions on an evidence-yellow card stay all warm white (no saffron in the same frame).

Full original notes (every detail, uncut): `_archive/original-full/text-highlight-match-cut.md` in this folder.
