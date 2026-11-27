---
name: mistakes-to-avoid
description: Deepak's rejected moves from delivered videos, with the fix for each — the 9 disliked frames from Day 03 "How Machines Are Trained" (2026-10-07) plus his "pacing not in sync" note. Load before ANY edit, before every style frame, and in the final QA pass of every video, so none of these ever appear again. Covers: coloured backgrounds behind his cut-out, floating thumbnail cards, element clutter, decorative mono labels, phone mock-ups of himself, oversized highlighted hero words, sentence-length captions, and word-sync on Telugu speech.
---

# Mistakes to avoid (Deepak's rejected frames)

Source: 9 screenshots Deepak saved to `Desktop/dislike frames/` after watching Day 03 (2026-10-07), plus his note *"pacing not sync"*. He said: *"Don't repeat next time these mistakes."* Every rule below is a hard rule, not a preference. Check the whole list on every style frame and again in the final QA.

## A. Backgrounds
1. **Never replace his room with a colour behind his cut-out.** The full-yellow "world" behind his person matte (title at 0:15, RLHF at 10:00) was rejected twice (*"I don't like it"*). His real room stays visible at all times. The accent colour lives on text, markers and small chips only.
   - Allowed ways to go big: ink words printed on the wall behind him (plant in front), the faded-black bottom gradient, the notes-page split, a dark card beside his head.

## B. Clutter on the footage
2. **One graphic element on his footage at a time** (plus at most one small label). The frame with the thumbnail card + rings + dotted arrow + "LINK ↗ TOP RIGHT" chip + series rail was rejected. If a second element must appear, the first leaves first.
3. **No floating thumbnail cards over the room.** Two video thumbnails placed over his monitor were rejected. Show a previous video as one card inside the faded black, or in the notes page, never as pictures pinned onto the set.
4. **No drawn arrows or leader lines across his footage** ("the link is top right" dotted arc). Say it with a small chip or nothing.
5. **No series rail / progress strip sitting on the footage.** Rails belong on cards or pages, not over the room.

## C. Labels and small type
6. **No decorative mono labels** ("P. 07", "PARADIGM 03 / 04", "01 / 06", eyebrows, footers). They mean nothing to a viewer and were rejected on their own. A label is allowed only when it carries information he spoke (a definition number he says, a source name, "ILLUSTRATIVE").
7. **Nothing on screen under 24 px at 1080p stage.** If it has to be small, it should not be there.

## D. Gimmicks
8. **No phone / device mock-up with his own footage inside it.** The "your story" phone with him inside was rejected. For "share / tag me" moments, use a plain handle chip (@tech.boy.deepak) in the faded black.
9. **No oversized yellow-block hero words.** The tilted "FINE-TUNED" card with a frame-wide yellow block was rejected. The yellow marker is a highlighter (0.4–0.5 em behind a line of text), never a slab behind a 200 px word. Match-cut cards stay plain paper with normal-size text and a thin highlight on the keyword.
10. **No tilted / rotated cards.** Cards sit straight.
10b. **No mass grids of fake/generated thumbnails, and never his face pasted into loud clickbait templates** (sunburst gradients, Impact words, red circles). On the "Top 5 skills" TASTE beat, 100 generated thumbnails with one picked was rejected before render: *"I don't like these 100-thumbnail frames. Remove this concept… clean, professional visuals that match the video's style."* Fix: show "many outputs → one choice" as a clean typographic/counter beat in the video's own palette (e.g. a counter 100 → 1,000 in mute ink, then one accent "1"). — *Deepak, 2026-10-13* `(2026-10-13)`

## E. Captions
11. **Keyword captions only, never a sentence.** The Grok line ("Mar 2025: when provoked, Grok replied in Hindi slang — India's IT ministry said it was 'in touch' with X." + an outlet list) was rejected. Max 1–4 words per caption; a source is one outlet name, not a list. If a fact needs a sentence, it goes on a notes page or a source card, not on his footage.
12. **No outlet / credit lists on screen.** Credits go in the description.

## F. Pacing and sync (his note: "pacing not sync")
13. **Sync the graphics to the Telugu, not to an English ASR.** Day 03 was timed with an English Whisper pass on Telugu speech; where the aligner had no English word, timings were set by eye (~6:44 "remember", 8:55, 9:55, 11:31–11:52). That is where it drifted. Required method:
    - Transcribe in Telugu (Whisper `te`, or his transcript file when it is the right video), romanise it, and align with MMS_FA on the romanised text.
    - Verify every hero word on a spectrogram onset (RMS envelope), not on the aligner alone.
    - Send him a 30–60 s **sync check clip** before the full render, not just still frames.
    - **Refinement from video 11 (Claude's finding, not yet reviewed by Deepak, 2026-10-08):** English-translation word times drift up to ~2 s inside long Telugu sentences, and MMS keyword spotting is unreliable for numbers and brand names (low scores). What worked: Whisper large-v3 `te` with word timestamps on **short 3–6 s windows** around each graphic (ignore the first word, it snaps to the window start), confirmed against the 20 ms level onset of the voice. A first pass timed from English had ~40 elements early by 0.3–2.2 s; every one was moved to the spoken word.
14. **One beat per spoken idea.** Don't stack an entrance, a counter and a camera punch on the same half-second, and don't let a graphic arrive before the word. Late by ≤ 1 frame is fine; early is never fine.
15. **Hold long enough to read.** A card with more than three words stays ≥ 2 s; a notes-page definition stays until he finishes the sentence.

## G. Reference patterns that break the rules above (Claude's conflict check, 2026-10-09 — not Deepak's words)
Studied in refs 67–68 (`motion-graphics-style` → "Motivation red world and frosted-glass explainer"). Take the principle, never the pattern:
- **Drawn arrow on footage** (ref67, bar chart on the room with a hand-lettered label + curved arrow) → breaks B4. Use a chip or nothing; a chart on footage is the single element.
- **Coloured world behind the cut-out** (ref68, violet ribbon world) → breaks A1.
- **Full-sentence caption on a faded-black lower third** (ref68) → breaks E11. Keep only the glow, the tight tracking and the black fade, for 1–4 words.
- **Thumbnail / toast / idea cards stacked on the room** (ref68) → breaks B2/B3.
- **Tiny axis labels, 2 px lines and sub-24 px text** (both videos) → breaks C7. Scale labels up even when the reference's are small.
- **Violet palette** (ref68) → disliked on Day 2.
- **Reference timing is not Telugu timing** (F13): copy the reference's rhythm (ease-out rise ≈ 1 s, hold ≈ 0.5 s, glow strike), then place it on his spoken word.


## H. "Only text and basic sound effects" (video 13, Top 5 Skills, rejected 2026-10-13)
Deepak: *"This video is the worst output I got. You just added the text and basic sound effects. That is what my editor is also doing."* What went wrong, and the fix:
16. **Text on footage is not motion graphics.** About 80 of the 107 beats were wall words and keyword captions, and the full-screen scenes were flat slides (bars, dots, a grid, a chat window). Fix: most beats must be built visuals with depth (camera moving through a scene, layered parallax, light, texture, real objects/UI, footage); a caption is the exception, not the default.
17. **Never drop B-roll because the library doesn't have it.** I used zero B-roll because nothing local was 1440p+. Fix: source it (Pexels/Mixkit 4K per `where-to-find-assets`, list the files and ask once), or generate the visual; never ship a talk with no footage.
18. **"Continue without stopping" does not cancel the sample gate in his brief.** His brief said style frames + a 30–60 s sync clip and WAIT for OK; I skipped it and rendered 12 minutes he never saw. Fix: always send a short finished sample at full quality before the full render, then continue fast. **Exception:** when I ask and he explicitly picks "no sample, finish everything" (v2 redo of video 13, 2026-10-13), render the whole video without the gate.
19. **Pacing must match the brief, measured.** He asked for a cut about every 2.5 s, 0.5 s montages at emotional turns, transitions (B&W flash, zoom punch, whip into scenes). I shipped one beat every 5–6 s with almost no transitions. Fix: count changes per minute before rendering.
20. **Sound must be designed, not reused.** I re-ran the Day 6 sound script (pops, ticks, one hit type). Fix: a sound plan per scene (whooshes into scenes, impacts on turns, risers, textures), varied, checked moment by moment.
21. **The bar is "explain deeply with motion", built from internet references, with smooth UI animation (Deepak, 2026-10-13: "I expected high professional motion graphics and explaining deeply, taking references from the internet, smooth UI animations... you gave 10 out of 5").** Fix, in this order, before any build: (a) search the web (Dribbble, Behance, LottieFiles, Pinterest, YouTube explainers) and write down 5+ references per scene type; (b) each concept is explained by an animated visual (a flow, a product UI doing the task, a before/after, a live number), not by a caption; (c) every UI scene uses the `app-product-animation` motion rules (ease-out, morph, cursor as the actor, glow on impact); (d) load the craft skills (`video-intro-design`, `text-highlight-match-cut`, `app-product-animation`, `where-to-find-assets`, `client-video-editing-process`), not only the rule skills; (e) test with a full-quality hook sample before anything else.

## I. Designed stand-ins that read as evidence (ep 02 v1 → v2, Deepak 2026-10-16)
- ✗ A designed "document" for a real one: an executive-order page with grey lines and a drawn signature, an "Accord" page with a seal, a "U.S. District Court" name card, a "Tip submitted" record. → ✓ Capture the real page (whitehouse.gov, justice.gov, the company's report) and highlight the spoken words; if no page exists, show no document.
- ✗ Initials or a company logo where a real person is named (EM, JC, MA, JK). → ✓ A credited portrait (public domain or CC).
- ✗ A drawing of an object when the authorities published photos (the recorder behind the TV). → ✓ The official photos, with "Figure 1 · DOJ" source lines.
- ✗ A UI mock-up of a real product shown as if it were real (the ChatGPT ad screen). → ✓ Keep it only with an ILLUSTRATION tag, and say in the notes that the real format has not been shown.
- ✗ An unverified detail in a label ("at a conference"). → ✓ Only what a source says.

## How to use this skill
- **Before style frames:** go through A–E on every frame.
- **Before the full render:** run the sync check (F13) and get his OK.
- **Final QA:** step through a frame every 5 s and tick every rule; any frame that breaks a rule is re-rendered before delivery.
- When Deepak sends new disliked frames, add them here as numbered rules with the fix, and mark the matching pattern in `motion-graphics-style` as rejected.
