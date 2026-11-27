---
name: text-highlight-match-cut
description: Deepak's two must-use-in-every-video effects — (1) brush-stroke TEXT HIGHLIGHTING on article/news/screenshot/document text (yellow marker wiping under the key phrase, Dhruv Rathee style) and (2) the keyword-anchored MATCH CUT (one highlighted word stays pinned while 5–7 sources flash-cut behind it every 3–4 frames). Load for any edit — documentary, gaming, tech explanation, Deepak's own reels — whenever the script quotes a source, cites a number/fact, names a person/company/tool, says "according to…", "reports say…", "search…", or when a beat needs proof or a montage of evidence. Learned frame by frame from refs 12–13 (analysis in experiment/06_references_12-13_highlight_matchcut_analysis.md).
---

# Text highlight + match cut

> **Note (2026-10-06):** `experiment/` paths in this skill are historical — that folder was cleared. Final videos + edit notes: `Raghu and claude/edited videos by claude/`. Reusable code: the `code/` folder inside each video folder. Reference analyses were folded into the skills and deleted.

Deepak (2026-09-30): "very important roles in every video… very simple, but it creates a demand. In my videos, try to use these effects: match cut and highlighting text." So **every edit plan must contain at least one highlight beat, and at least one match-cut beat where the script allows it.** Flag it in the plan as `HL` and `MC`.

## 1. Highlighting text (ref12)

**When:** any on-screen text that proves what he is saying — news headline, article line, Wikipedia/Google result, salary figure on a job site, a syllabus line, a tweet, a chat/DM screenshot, a doc, a terminal/log line in coding videos, patch notes in gaming videos.

**Recipe (CapCut):**
1. Put the screenshot on a soft, dark, slightly blurred background (ref12 uses a blurred newsroom photo with dust particles; Deepak's B-roll backgrounds from `broll-library` → "backgrounds" work). Scale the screenshot so the target line is ≥ 40 px tall on a 1080×1920 canvas; drop-shadow it.
2. Add a **rough-edged brush/marker stroke** (Canva "paint brush stroke" element, or a CapCut sticker "marker highlight"), colour **#F5C400 yellow**, rotate −1…−2°, height ≈ 1.3× the line height, ends overshooting the words by 2–4 %.
3. Layer order: stroke **below** the text screenshot only if the screenshot has a transparent background; otherwise put the stroke *above* at 75–85 % opacity with the **Multiply** blend so black text stays crisp.
4. Reveal with a **linear mask wipe left → right**, 0.4–0.7 s for a headline, up to 1.5 s for a long body line (ref12's is ≈ 1.5–2 s and reads a little slow; keep ours tighter to Deepak's pace). Ease-out, no bounce.
5. Start the wipe **on the spoken word** (≤ 1 frame late, like every other picture cut in the playbook). Add a soft paper "marker scribble" or short "swish" SFX at −18 dB, or nothing at all under captions (Tharun rule).
6. Highlight **one line per beat**; a second line only if the voice-over actually reads it. Never highlight a whole paragraph.
7. Same yellow every time in a video (one accent colour rule). On dark UI screenshots (terminal, Discord, dark-mode sites) use the same yellow at 60 % Multiply, or a yellow **underline stroke** instead of a block.

## 2. Match cut on the highlighted word (ref13)

**When:** the script says something is *everywhere* / *repeated* / *searched* / *reported by many* ("every site says…", "search his name and…", "10 companies posted the same…", "every review mentions…"), or a name/number needs weight. Also the go-to for "quick evidence montage" in documentary edits and "everyone is talking about this patch" in gaming edits.

**Recipe:**
1. Pick the anchor: the highlighted keyword (or a logo/number). Build **5–7 different sources** that contain it: different page layouts, fonts, sizes and text densities so each cut reads as a new document (ref13: about-page, Wikipedia, news, quote spread, industry spotlight, wiki overview, home page). Off-white paper texture, near-mono, only the highlight in yellow.
2. **Pin the anchor to one exact screen position** (ref13: ≈ 38 % from the top, left edge ≈ 20 % of width). Every source is repositioned/scaled so its instance of the word lands on that spot. This is the whole trick: the word never moves, the world jumps.
3. **Cut every 3–4 frames** (0.10–0.13 s) — 17 cuts in 2.3 s in ref13. If the beat is longer than ~1.2 s, loop the same order again rather than making more sources.
4. Put a **directional motion blur** (or CapCut "Blur → motion" / a 2-frame zoom-blur transition) on the *backgrounds only*, not on the anchor, so the jumps feel like a camera whip.
5. Sound: one whoosh-in on the first cut, a continuous ticking/texture bed under the run, one **hit on the last cut**; do not put a tick on every cut. Volume per playbook (bed −11…−13 dB under a hook line).
6. Exit: **white flash from a corner (5–6 frames)** into the next shot or a small label (ref13: "First search"), or hard cut back to the talking head on the next spoken word.
7. Limit: **one match-cut run per 20–30 s of video**, and always after a highlight beat that introduced the anchor (highlight → match cut is one system).

## 3. Variants (same rule, other subjects)
- **Gaming:** anchor = a weapon/character/patch-note line; sources = patch notes, Reddit thread, tweet, wiki, YouTube title.
- **Documentary:** anchor = a person's name or a date; sources = newspaper clippings, court doc, Wikipedia, book page, tweet.
- **Tech explanation:** anchor = a tool/company name or a price; sources = docs page, pricing page, GitHub README, Play Store listing, news.
- **Deepak's own reels (students / careers):** anchor = a college name, a salary figure, a company logo, "EAPCET"; sources = counselling site, LinkedIn job posts, Glassdoor, news, official notification PDF.

## 4. QC
- Anchor drift ≤ 2 px between cuts (check by scrubbing frame by frame).
- Highlight wipe starts on the word, yellow is identical across the video, text still readable.
- No more than one highlight per beat and one match-cut run per 20–30 s; if the plan has zero of either, say why.

## 5. Variant used when the script has no source documents *(IKKO MindOne review, 2026-09-30 — Claude's adaptation, not yet approved by Deepak)*
- **HL on the product name:** the name is the only on-screen text that matters. Use the dark-UI **underline stroke** from §1.7, wiped left to right on the spoken word (0.5 s) under the type-on. The colour is the **video's accent** (periwinkle, sampled from the product's screen), not yellow, so the video keeps one accent colour. Switch to #F5C400 if Deepak wants the classic yellow.
- **MC recalls the same highlighted name** as the pinned anchor (38 % height, dark radial scrim) on the one line that means "many" ("this many features"). The sources are the review's own B-roll, one feature per shot. **Final version: 6 shots × 6 frames at 60 fps (0.1 s).** Backgrounds are dimmed 25 %, and each is reframed at scale 1.25 so the phone lands under the word. Each background whips in 40 px and settles (expo.out, 24-sample motion blur); the anchor never moves. Sound: whoosh in, one ticking bed under the run, sub + whoosh on the last cut. Exit: a **hard cut** onto his face for "features". The first version (8 shots, corner white flash) was judged flickery and preset-like by the QC review.
- The highlight is **marker weight** (0.44 em behind the lower half of the letters, deeper accent for contrast), and the same stroke is used on the name and on the anchor.
- Never fabricate a "source" screenshot (product page, article) to create a highlight beat. If none exists, use this variant and say so in the plan.

## 6. Real-source capture for HL + MC *(video 13 v2, 2026-10-13)*
- **`capture.js`** (puppeteer, 1600×900 at DPR 2):
  - loads the article and hides cookie, consent and paywall overlays with CSS (never clicks them);
  - finds the Nth text match of a regex and scrolls it to the centre;
  - saves the PNG plus the phrase's client rects (JSON).
  - Headless Chrome got TechCrunch, The Stack, The New Stack, Illinois Tech and the Accel job board. Sifted's paywall covers the text, so it was dropped.
- **HL:**
  - the real TechCrunch headline (white on green): yellow `#F5C400` multiply at 78 % of the line height, wiped left to right on "recently";
  - **include the currency sign** in a money highlight ($1 billion);
  - source tag bottom-left.
- **MC:**
  - re-capture every source with the anchor regex alone ("forward[- ]deployed");
  - scale each page so the rect height maps to one line height (92 px), and pin its left edge and top (560, 470);
  - background 62 % brightness, the anchor crop at full brightness with the yellow behind it;
  - 5 sources × 0.1 s × 2 loops, hit on the last cut, then hold.

## 7. Match cut on a company name across real headlines *(AI Tech News ep 02, 2026-10-15)*
- When one company runs through several stories, pin its name: "OpenAI" over 7 real headlines of the fortnight (SF Standard, XenoSpectrum, BetaNews, Cybernews ×2, AP ×2), 0.1 s each × 2 loops, landing on the story being introduced (11:11).
- Measure the anchor word on each page with `textbox.py` word runs; dark pages need the marker in screen blend.
- **Never zoom out a clipped match-cut layer:** its page is cut at the layer edge. Fade the pinned page and hand off to a separately cropped headline card, then highlight the new words.
