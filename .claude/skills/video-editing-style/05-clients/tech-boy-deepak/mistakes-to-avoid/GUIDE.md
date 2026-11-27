---
name: mistakes-to-avoid
description: Use before ANY video edit, before every style frame, and in the final QA pass of every video. Deepak's rejected moves from delivered videos (Day 03, video 13 Top 5 Skills, AI Tech News ep 02) with the fix for each - coloured backgrounds behind his cut-out, clutter, decorative labels, mock-ups, oversized hero words, sentence captions, Telugu sync, text-only edits, designed stand-ins posing as evidence.
---

> **Scope: client (Tech Boy Deepak). Sections A-G, I, J are his taste: apply them only to his videos. Sections H and K (text on footage is not motion graphics; the bar is explaining deeply with motion; Edit-Kit lessons) apply to EVERY client: read them in final QC of every edit.**

# Mistakes to avoid (Deepak's rejected frames)

Origin: 9 screenshots Deepak saved after Day 03 (2026-10-07), his note "pacing not sync", and later rejections. He said "Don't repeat next time these mistakes." Every rule is HARD. Check the list on every style frame and again in final QA.

## A. Backgrounds
1. **Never replace his room with a colour behind his cut-out.** The full-yellow "world" behind his person matte (title 0:15, RLHF 10:00) was rejected twice. His real room stays visible always; accent colour lives on text, markers and small chips only.
   - Allowed ways to go big: ink words printed on the wall behind him (plant in front), faded-black bottom gradient, notes-page split, dark card beside his head.

## B. Clutter on the footage
2. **One graphic element on his footage at a time** (plus at most one small label). Thumbnail card + rings + dotted arrow + "LINK TOP RIGHT" chip + series rail was rejected. If a second must appear, the first leaves first.
3. **No floating thumbnail cards over the room** (two thumbnails over his monitor rejected). Show a previous video as one card inside the faded black or in the notes page.
4. **No drawn arrows or leader lines across footage.** Use a small chip or nothing.
5. **No series rail / progress strip on the footage.** Rails belong on cards/pages.

## C. Labels and small type
6. **No decorative mono labels** ("P. 07", "PARADIGM 03 / 04", "01 / 06", eyebrows, footers). A label is allowed only if it carries something he spoke (a definition number, a source name, "ILLUSTRATIVE").
7. **Nothing on screen under 24 px at 1080p.** If it must be that small, it should not be there.

## D. Gimmicks
8. **No phone/device mock-up with his own footage inside.** For "share / tag me" use a plain handle chip (@tech.boy.deepak) in the faded black.
9. **No oversized yellow-block hero words.** The yellow marker is a highlighter (0.4-0.5 em behind a line of text), never a slab behind a 200 px word. Match-cut cards stay plain paper, normal-size text, thin highlight on the keyword.
10. **No tilted/rotated cards.** Cards sit straight.
10b. **No mass grids of fake/generated thumbnails; never his face in loud clickbait templates** (sunburst, Impact words, red circles). The 100-thumbnail TASTE beat was rejected. Show "many outputs -> one choice" as a clean typographic/counter beat in the video's palette (counter 100 -> 1,000 in mute ink, then one accent "1"). (2026-10-13)

## E. Captions
11. **Keyword captions only, never a sentence.** Max 1-4 words; a source is one outlet name, not a list. A fact needing a sentence goes on a notes page or source card, not on his footage.
12. **No outlet/credit lists on screen.** Credits go in the description.

## F. Pacing and sync ("pacing not sync")
13. **Sync graphics to the Telugu, not to an English ASR.** Day 03 used English Whisper on Telugu speech; by-eye timings drifted (~6:44, 8:55, 9:55, 11:31-11:52). Required:
    - Transcribe in Telugu (Whisper `te`, or his transcript file if it is the right video), romanise, align with MMS_FA on the romanised text.
    - Verify every hero word on a spectrogram/RMS onset, not the aligner alone.
    - Send a 30-60 s **sync check clip** before the full render, not just stills.
    - Video 11 refinement (Claude's finding): English-translation times drift up to ~2 s in long Telugu sentences; MMS spotting is unreliable for numbers/brands. What worked: Whisper large-v3 `te` with word timestamps on short 3-6 s windows around each graphic (ignore the first word, it snaps to the window start), confirmed against the 20 ms voice level onset. A first pass timed from English had ~40 elements early by 0.3-2.2 s.
14. **One beat per spoken idea.** Don't stack entrance + counter + camera punch in the same half-second; never let a graphic arrive before the word. Late by <= 1 frame is fine; early never.
15. **Hold long enough to read.** A card with > 3 words stays >= 2 s; a notes-page definition stays until he finishes the sentence.

## G. Reference patterns that break the rules (Claude's conflict check, 2026-10-09)
From refs 67-68 (`motion-graphics-style`). Take the principle, never the pattern:
- Drawn arrow/hand label on a chart over the room (ref67) breaks B4: use a chip or nothing; a chart on footage is the single element.
- Coloured world behind the cut-out (ref68 violet ribbon) breaks A1.
- Full-sentence caption on faded-black lower third (ref68) breaks E11: keep only the glow, tight tracking and black fade, for 1-4 words.
- Thumbnail/toast/idea cards stacked on the room (ref68) breaks B2/B3.
- Tiny axis labels, 2 px lines, sub-24 px text breaks C7: scale labels up.
- Violet palette: disliked on Day 2.
- Reference timing is not Telugu timing (F13): copy the rhythm (ease-out rise ~1 s, hold ~0.5 s, glow strike) but place it on his spoken word.

## H. "Only text and basic sound effects" (video 13 Top 5 Skills, rejected 2026-10-13)
Deepak: "worst output I got... you just added the text and basic sound effects. That is what my editor is also doing."
16. **Text on footage is not motion graphics.** ~80 of 107 beats were wall words/captions, and full-screen scenes were flat slides. Fix: most beats are built visuals with depth (camera through a scene, layered parallax, light, texture, real objects/UI, footage); a caption is the exception.
17. **Never drop B-roll because the library lacks it.** Source it (Pexels/Mixkit 4K per `where-to-find-assets`, list files, ask once) or generate it; never ship a talk with no footage.
18. **"Continue without stopping" does not cancel the sample gate in his brief.** Send style frames + a 30-60 s sync clip and wait for OK; always send a short finished full-quality sample before the full render, then continue fast. Exception: he explicitly picks "no sample, finish everything" (v2 of video 13, 2026-10-13).
19. **Pacing must match the brief, measured.** He asked a cut ~every 2.5 s, 0.5 s montages at emotional turns, transitions (B&W flash, zoom punch, whip). I shipped one beat per 5-6 s. Count changes per minute before rendering.
20. **Sound must be designed, not reused.** Per-scene sound plan (whooshes into scenes, impacts on turns, risers, textures), varied, checked moment by moment; don't re-run the previous video's pop/tick script.
21. **The bar is "explain deeply with motion" from internet references with smooth UI animation** (he rated the result "10 out of 5"). Before any build: (a) search Dribbble, Behance, LottieFiles, Pinterest, YouTube explainers and write 5+ references per scene type; (b) explain each concept with an animated visual (flow, product UI doing the task, before/after, live number), not a caption; (c) every UI scene uses `app-product-animation` rules (ease-out, morph, cursor as actor, glow on impact); (d) load the craft skills (`video-intro-design`, `text-highlight-match-cut`, `app-product-animation`, `where-to-find-assets`, `client-video-editing-process`), not only rule skills; (e) test a full-quality hook sample first.
21b. **Repeated on video 25 (Naveen bro, 2026-11-26: "not impressed by client").** Clean captions, stacks and 11 stock clips, but only 11 % designed motion graphics, nothing designed for the first 17.8 s, and no HL / MC, so it read as text on a talking head. Fix: the `01-process/before-edit/` gate (CLAUDE.md Rule 0): a PRE-EDIT sheet with the motion-graphics plan, designed MG every 8 s (3+ kinds, >= 25 % of runtime), and `pre_edit_gate.py` READY before any full render. Post-mortem: `08-learning-log/VIDEO-25-POSTMORTEM.md`.

## I. Designed stand-ins that read as evidence (ep 02 v1 -> v2, 2026-10-16)
- Designed "document" for a real one (executive order, accord with seal, court name card, "Tip submitted" record): capture the real page (whitehouse.gov, justice.gov, company report) and highlight the spoken words; if none exists, show no document.
- Initials/logo where a real person is named: use a credited portrait (public domain or CC).
- Drawing of an object when authorities published photos (the recorder behind the TV): use the official photos with "Figure 1 - DOJ" source lines.
- UI mock-up of a real product shown as real (ChatGPT ad screen): keep only with an ILLUSTRATION tag and note that the real format was not shown.
- Unverified detail in a label ("at a conference"): only what a source says.

## J. "Not that pretty" (16. Uncertainty Short, feedback 2026-11-16)
User: the last edit "looks like not that much pretty"; next edits need "proper brolls and sfx and motion graphics", "not only what you trained", "take external sources", "make video attractive as much as possible".
Claude's diagnosis from the 1 fps sheet (unconfirmed by him):
- About a third of the frames were flat ink cards with thin line art (ladder, path lines, plain CONTROL word, clip-art stick figures).
- The face grade stayed muddy olive.
- Small connector captions.
- Mixed-quality 720p library B-roll and a cheap chalkboard clip.
- No light, colour or depth (glow, gradients, 3D, texture).
Fix:
- Use high-quality external B-roll (Pexels / Mixkit / Coverr, 1440p+), graded to match.
- Build designed MG with depth and colour (glass, glow, light, 3D emoji or icons, real textures) instead of black cards.
- Use a brighter, punchier grade and bigger designed captions.
- Use a varied SFX set sourced from Mixkit / Freesound / Pixabay.
- Black cards only as a rare accent.

## How to use
- Before style frames: go through A-E on every frame.
- Before the full render: run the sync check (F13), get his OK.
- Final QA: step a frame every 5 s and tick every rule; re-render any breaking frame.
- New disliked frames from Deepak: add here as numbered rules with the fix, and mark the matching pattern in `motion-graphics-style` as rejected.


Full original notes (every detail, uncut): `_archive/original-full/mistakes-to-avoid.md` in this folder.

## K. Learned from the Edit-Kit and 2026-11-17 references (pre-emptive, not yet user feedback)
1. Wide-tracked uppercase mono kickers read as "AI-made": use sentence-case sans labels, tracking about -0.015em on big words with .08em word-spacing.
2. Em/en dashes in on-screen copy: rewrite the line.
3. Numbers in the viewer's language: "94%", never "%94" (an RTL habit seen in ref 48a38ca593e4).
4. A visual that contradicts the words ("3 AM" over daylight, reels on "100 clients"): pick a matching real UI or stay on the speaker with one key word.
5. Two embedded (behind-subject) words co-visible, or embeds closer than 0.6 s: one hero per beat.
6. Captions shorter than 0.5 s on screen, or a caption group that mounts after its first word starts.
7. SFX timed to the start of an animation: the cue goes on the impact frame (within 1 frame).
8. Final file with sparse keyframes: re-encode with a keyframe every 1 s (closed GOP) so it scrubs in Premiere.
