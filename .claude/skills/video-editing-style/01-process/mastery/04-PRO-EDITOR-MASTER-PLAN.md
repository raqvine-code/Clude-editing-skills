# Pro Editor Master Plan

How every video is edited from now on, to senior-editor standard. Steps 1-10 apply to both short-form and long-form; the differences are marked.

## Stage 0 - Skills first (every short and long edit, no exceptions)
Read the skills listed in `CLAUDE.md` for this video type, then tell the user in one line: "Using: <skills> - style: <one style>". If the video is already rough-cut or polished, keep that cut and add only the missing layer unless asked to re-cut.

## Stage 0.5 - Analyse, then write PLAN.md (no editing before this exists)
Run `04-styles/pro-video-editing/tools/analyze_raw.py <video> <project_dir>`, study its sheets and transcript, then fill `05-PLAN-TEMPLATE.md` into `<project_dir>/PLAN.md`, including 2-3 "Claude's idea" creative moves. Show the summary; wait for approval on new styles or client work.

## Stage 1 - Brief and story (before touching the timeline)
1. **Collect:** raw footage, script/transcript, platform (Reels / Shorts / YouTube), target length, goal (teach, sell, grow, hire), CTA, brand colour.
2. **Read standing rules:** `my-editing-rules`, `mistakes-to-avoid`, `fonts-and-colours`.
3. **Transcribe with word timing** (faster-whisper), read the whole transcript and watch every frame of the raw.
4. **Find the story:** hook line, stakes, 1 main idea (short) or numbered sections (long), payoff, CTA. Flag what is missing.
5. **Pick ONE style** (table in 02 / 03). If you named none, choose and say why in one line. Never mix styles.

## Stage 2 - Cut
6. **Story cut:** open on the strongest line at frame 0; remove dead air (pauses <= 0.3 s, keep breaths at commas); end on the payoff word.
   - Short: one complete thought, 15-60 s; 5 best moments from a long video.
   - Long: every section pays its promise; something new every 5-15 s.
7. **Camera rhythm on the A-roll:** alternate normal / punched-in framing on jump cuts (style values, e.g. Tharun 124-143 %), slow pushes on long takes; never speed-ramp a talking head.

## Stage 3 - Plan (written before building)
8. **Shot-by-shot plan table:** `time in | length | spoken words | on-screen text (tier) | graphic / B-roll | transition | SFX | note`.
   - Mark one keyword per sentence; 1-3 behind-subject words per short.
   - Each graphic lands on its word or 0.1-0.35 s before (never after).
   - List the three weakest moments and the fix for each.
   - Send this plan (and rough cut for shorts) for approval when the video is new or for a client.

## Stage 4 - Build
9. **Look:** colour correction first (exposure, white balance, skin), then grade to the style; one accent colour family.
10. **Type system:** one font per role (caption / display / label), sizes from the style, safe zones respected.
11. **Graphics & B-roll:** local libraries first (`broll-library`, `png-library`), then `where-to-find-assets`; real sources for facts (`text-highlight-match-cut`). Every noun that matters gets a picture; no decoration without a job.
12. **Motion:** entries 2-8 frames with motion blur, morphs ~15 frames, camera pans ~1.3 s; elements mostly don't animate out (cut instead).
13. **Mattes:** person cut-out for text behind the subject (`pro-video-editing/tools/matte.py` or Vision mattes) - check hair edges.
14. **Transitions:** only those in the style's library (hard cut default; flashes, whips, shrink-to-card, halftone, hexagon as the style allows).

## Stage 5 - Sound (`sound-and-music-design`)
15. Clean voice first (-16 LUFS voice chain), music chosen by energy and cut on the key line, SFX on entries/whips/pops with a mid knock + HF click for phone speakers, music 18-24 dB under voice.
16. Master -14 LUFS / -1 dBTP (YouTube, Reels), unless you choose louder.

## Stage 6 - Review like a senior editor
17. **Sample first:** render 10-15 s, check, then the full video.
18. **QC (automatic):** contact sheet every 0.5 s, frame strips at every transition, loudness, freeze/black detection, sync check (keyword graphic vs word time).
19. **QC (eye):** hook moves by frame 3 and makes a promise; nothing static > 2.5 s (short) or > 15 s (long); text readable >= 0.5 s; no text over eyes/mouth; one palette; no unmotivated effect; music never over voice; ends right after the payoff.
20. **Mobile test:** watch at phone size with sound off and on.

## Stage 7 - Deliver and learn
21. Export H.264, 1080x1920 (short) / 1920x1080 or 2560x1440 (long), source fps, AAC 48 kHz.
22. Report exactly what was rendered and checked.
23. **Save learning:** your feedback goes into `my-editing-rules` / `mistakes-to-avoid` via `skill-saver`; new reference videos go into `training claude` and `pro-video-editing/tools/refscan.py` updates the knowledge base incrementally.

## Senior-editor habits (from all skills)
- Story first, effects second; every cut, graphic and sound has a job.
- Pace comes from camera, graphic density and transitions - not from speeding up the voice.
- Leave the face on screen for human beats; full-screen graphics for evidence.
- Fewer, cleaner effects beat many loud ones; over-editing tires viewers.
- Make one change to any copied style so it becomes your own.
- Never claim a render that wasn't made and checked.

## Next steps to reach top-class
1. Send your first raw short; I edit it with this plan and a 10-15 s sample for approval.
2. Add 2-3 videos for each screenshot-only look and for any creator you want measured (MrBeast, Hormozi, Iman), so their rules move from Published to Measured.
3. After 3-5 delivered edits, review your feedback and tighten the rules.
