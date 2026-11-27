---
name: shorts-editing-pro
description: Use for ANY 9:16 short, reel or YouTube Short edit (talking head first): cut to the voice, hook, word-by-word captions, punch-in zooms, B-roll, sound design and 1080x1920 export. One playbook built from Deepak's rules, the measured Tharun Speaks style, top-editor styles, the reference library (P1-P5), 2026 web research and every past short edit. Keeps LEARNING-LOG.md, updated after every edit.
---

# Shorts editing pro (9:16)

The single entry point for short-form edits. It distils the other skills; it does not replace them. When rules conflict, this order wins:

1. Deepak's latest instruction in chat.
2. `my-editing-rules` and `mistakes-to-avoid` (hard rules).
3. `LEARNING-LOG.md` in this folder (lessons from delivered shorts).
4. This file and `references/`.
5. Web research (`references/web-research-2026.md`): platform mechanics only, never taste.

## Workflow (lean: low credits is a standing rule)

0. **Before-edit gate (CLAUDE.md Rule 0, 2026-11-26).** Follow `01-process/before-edit/README.md`: read every skill in its list (craft skills too), fill `PRE-EDIT.md` with the speech -> visual map and the motion-graphics plan (designed MG every 8 s, 3+ kinds, >= 25 % of runtime, HL + MC), log the asset search (local catalogs first).
1. **Skills line.** Read this file plus `LEARNING-LOG.md` and `edit-kit-playbook` (sections 3-4 beat grammar + speech-to-visual map, 6 captions, 8 cue sync, 9 QA). Open a reference file only when a step needs it. Tell Deepak in one line which skills and which ONE style are in use.
2. **Analyse.** Run `python3 04-styles/pro-video-editing/tools/analyze_raw.py <raw> edits/<id> --lang en`. Then look at the 0.5 s sheets (small) and read the whole transcript.
3. **Decide the cut.** If it is a raw take, cut to the voice (step 5). If it is already rough-cut or polished, keep the cut and add only the missing layers.
4. **PLAN.md.** Keep it to about one page: goal, story (hook / turn / payoff / loop), style + reason, shot table, captions plan, B-roll list, SFX list, 2-3 "Claude's idea" moves, three weakest moments + fixes, QC targets. Deepak gave full autonomy, so don't wait for approval unless it is a new client or style.
5. **Build with `tools/shortkit.py`**, driven by one `edl.json` (keeps, zooms, captions, B-roll, flashes, SFX). Run `01-process/before-edit/tools/pre_edit_gate.py edl.json` on the draft EDL and fix every FAIL first. Then render a 5-8 s sample at half scale, check frames, and render the full video.
6. **QC** (section "QC") on the encoded MP4. Fix, then deliver.
7. **Deliver** per `my-editing-rules` section 2B: numbered folder in `CLAUDE 2.0/edited videos by claude/`, notes, brain copy, README row there. Then **append to `LEARNING-LOG.md`**: what was made, what was new, what went wrong, and Deepak's feedback when it arrives.

**Credit rules.**
- No Workflow and no subagent fan-out. Web research only when something is truly new.
- Read skills in slices; view contact sheets at small size; never re-read big plans.
- Reuse `shortkit.py` and its asset lists instead of writing a new kit per video.

**Promoted from LEARNING-LOG (seen twice, 2026-11-21).**
- Check every hero word's caption time against the voice level (5-10 ms steps) before the full render; ASR is up to 0.3 s off around silences.
- Never delete render caches to force a re-render: give changed B-roll slots a new key and overwrite frames in place (`edits/telugu1/tools/rerender.py`).
- After a kit-wide change (2026-11-26: the `SWS` colour-rounding fix), `video` still reuses every existing frame ("rendered 0 frames"): move `work/frames` aside, don't delete it. On a "no colour grading" request, measure the rendered A-roll against the source (Y plane at zoom 1.00, target under 1 level).
- Deliver a CRF 19 copy capped at 20 Mbps (keyframe every 1 s); keep the CRF 16 master in the project.
- B-roll: Pexels portrait search first (built-in browser for the search page, curl for the files). Mixkit video is 720p personal-use only since 2026-11; its SFX and music are still fine.
- Check the LAST frame like the cover frame (no blink, matches frame 0) when the short loops.

**Promoted from LEARNING-LOG (seen again on 2026-11-22, 22. Grayscale Tip).**
- Telugu words: Whisper large-v3 `te` in windows of 6 s or less with a plain sentence prompt, beam 3, temperature 0 and no repetition penalty; redo a looped window with no prompt. Set the onset threshold from the raw's level percentiles.
- Designed scenes are pre-rendered clips played as B-roll slots (versioned keys); objects behind his head are RGBA `layers`.
- One keyword per caption group; drop a lead-in that would leave its keyword under 0.4 s; no caption may cross a cut into another picture.
- Measure the hair top on a still before placing a giant word (only the feet of the letters go behind the head); the first giant starts before frame 0.
- Sound: a short sharp airy flick on every visible cut (slow whooshes do not count on the scorecard), SFX panned or swept, every sub hit paired with a mid-rich hit.
- Run the builder's checks before rendering: event gaps (1.3 s), framing change of 16 % or more on every visible jump cut, caption edges.

## The 12 rules of an attractive short

1. **Hook in frame 0.** Something moves by frame 3, and the strongest line opens the video. Stack three hooks inside 1.5 s:
   - visual: a punch-in, flash or B-roll;
   - verbal: a promise, contrarian claim or question;
   - text: 1-3 giant words.
   No logo, greeting or intro. Target viewed-vs-swiped 70 %+.
2. **Cut to the voice.**
   - Remove pauses over 0.3 s, keeping comma breaths of about 0.15 s.
   - Remove stumbles, false starts and repeats. Never speed up or re-time the voice.
   - Cut on word boundaries, about 1 frame before the next word, with 8-10 ms audio crossfades in room tone.
3. **One thought:** hook → turn → proof or example → payoff. End on the payoff word with no outro, so it loops. 15-45 s is the sweet spot; a tight 20 s beats a loose 50 s.
4. **Something changes every 1-3 s, at varied intervals.** That can be a cut, a scale change, B-roll, a caption stack or a flash. Never let a shot hold more than 2.5 s without a change, and never use a fixed metronome.
5. **Jump cuts change size.**
   - Alternate about 100 % and 115-140 % framing, anchored on the eyes (eye line at about 35-38 % of frame height).
   - Use a slow push of 1-3 %/s on holds.
   - Snap-zoom (4-6 frames, expo-out) on hero words: snap OUT on a hero word, snap IN on a negative or shocking word.
6. **Word-by-word captions.**
   - One beat per word, with glue words joined; at most 3 words on screen.
   - Hard pop on the word's first frame, scaled in (scale 1.15→1, 3-4 frames). No typewriter, slide or bounce.
   - White heavy sans with a soft shadow, plus one accent keyword per phrase that is bigger (1.3-1.75x) or accent-coloured.
   - Place the block centre at 58-65 % of the height (y about 1110-1250), just under the chin, never over the mouth; bottom above y 1470 (researched 2026-11-25: `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`).
   - Write them in sentence case as spoken. Telugu is written in English letters (Tenglish).
7. **Every concrete noun gets a picture, on the word or up to 0.3 s before it, never after.** That can be B-roll, a PNG, an icon, a number or a proof screenshot. Use B-roll for 25-50 % of the runtime, in 0.6-2.5 s bursts, with whip or blur-zoom entries. Use 1440p+ Pexels or Mixkit clips graded to match.
8. **One graphic element on his footage at a time.** Use the behind-the-head giant word 1-3 times per short, only with a clean matte. Captions leave while a giant word or full-screen graphic is up.
9. **Accents, not effects.**
   - Hard cuts by default.
   - Negative flash (2 frames) at 1-3 section turns. White flash (1-2 frames) in or out of B-roll.
   - Blur-zoom (3-5 frames) into a hero B-roll shot.
   - Never use a flash train, glitch spam, random shake or preset transitions.
10. **Sound is half the edit.**
    - Clean voice chain first.
    - Every cut, pop-up and flash gets a designed SFX: whoosh about 90 ms before a cut, sub-hit plus mid knock on slams, soft pop on captions only for hero words, and a riser into the payoff.
    - Vary the samples. Main master is voice + SFX; music is an optional alt master about 18-22 dB under speech, ducked, cut once on the key line.
11. **One look.**
    - Bright, punchy grade: face luma 135-150, skin hue natural, background darker than the face.
    - Vignette and fine grain. One accent colour that changes every video (see `fonts-and-colours`), and one font per role.
12. **Export.**
    - 1080x1920, source frame rate (constant), H.264 High, CRF 16-18 (or about 12-20 Mbps), BT.709 tv range, AAC 320k 48 kHz.
    - -14 LUFS integrated, -1 dBTP or quieter.
    - The first frame doubles as the cover: face plus hook word, centred for the 3:4 grid crop.

## Numbers cheat sheet

| Thing | Value | Source |
|---|---|---|
| Canvas | 1080x1920; work at source fps (often 60 or 24p-in-60 pulldown) | rules |
| Safe zone | text inside x 120-960, y 270-1470 (union of Reels, Shorts and TikTok UI; ads keep the bottom 35 % / 660 px clear); nothing key in the right 164 px between y 1000 and 1750 (buttons) | researched 2026-11-25, `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md` |
| Caption size | 96-130 px regular, keyword up to 1.75x, never wider than 900 px, nothing under 24 px | Tharun, mistakes |
| Caption beat | median 0.24 s; stack hold 0.5-1.3 s | Tharun (measured) |
| Light caption model (P10/P11, premium or podcast look) | light sans, lowercase; one word (box 4.5% of frame height) or tiny lead-in 2% + keyword 5.9%; centre x, y 45-60% (chest); lands on the word (+0.04 s) | P10, P11 (measured) |
| Scene inserts | full-screen designed scenes take 28-41% of runtime, alternate with A-roll every 1-5 s, enter by hard cut | P10, P11 (measured) |
| Blur-in two-font reveal (P12 designed scenes only) | bold sans line + italic serif line, max 2 lines, 2-6 words each; per word opacity 0→100, blur 14→0 px, y +10→0, 6-8 f ease-out; 4 f between glue words; hero words still on the voice | P12 (measured on frame sheets; px estimated) |
| Light-leak flash | 10-12 f at act turns, max 3 per short, same leak each time; bloom seeded on the hero object 1-2 f early; last frame = new scene under scanlines for 1 f | P12 (measured) |
| Stat wedge | angle = percent x 3.6°, clockwise from 12 o'clock, about 34 f; colour only inside the wedge | P12 (measured) |
| Faceless scene length | average 3.0 s, range 1.3-4.3 s; punchline is the shortest scene; endcard holds 1 s after its last word | P12 (measured) |
| Event cadence (every short) | something new on screen at least every 1.3 s; in the hook one event every 0.6-1.0 s; every VO pause of 0.5 s or more carries a move + a sound; the turn ("But...") sits at 60-77 % of runtime and gets the biggest device of the second half | event-map pack, 5 reels (measured) |
| Two-tier caption (P13) | small lead-in (1-3 words in our edits: house rule is keyword captions only, the reference ran the whole sentence) + ONE big keyword per group, 3-9 words in the reference, about 1.3 s, clears in 1 f; small words 0 to +2 f after the word, keyword starts 6-8 f early and settles on the word; keyword colour = role (topic / threat / pivot) | P13 (measured) |
| Long take | up to 7 s allowed ONLY if the background behind the speaker animates or a graphic changes every second | P10 (measured) |
| Cut rhythm | median about 1.1-2.0 s, range 0.25-2.5 s | ref61, Tharun |
| Punch-in | 115-143 % on jump cuts; hook push 100→116 % over 0.7 s | Tharun, web 10-15 % |
| Graphic timing | on the word, or up to 0.3 s early, never late | all refs |
| Pause trim | ≤ 0.3 s kept; breaths 0.1-0.15 s | ref61 |
| Speech pace | about 3.9 words/s after the cut | ref61 |
| SFX | about 1 structural hit per 2-4 s in a short; whoosh -10 dB, hit -4 dB, pop -14 dB re voice; all ≥ 0.25 s apart | sound skill |
| Music (alt) | 18-22 dB under the voice, duck 6-10 dB (attack 50 ms, release 400 ms) | web, rules |
| Loudness | -14 LUFS I, ≤ -1 dBTP (voice stem about -16 LUFS) | rules |

## Style picker (ONE per video)

| Video | Style | Reference |
|---|---|---|
| Talking-head advice, motivation, tech (default) | **Tharun Speaks 9:16 grammar**, raised with external B-roll | `tharun-speaks-edit-style` |
| Business or contrarian rant, fast | Hormozi: all-caps captions with keyword highlight, 1-3 s cuts, emoji or PNG pops | `top-editor-styles` |
| Premium personal brand | Iman Gadzhi: lowercase light-to-bold captions, smooth zooms, one palette | `top-editor-styles` |
| Story with stakes | MrBeast-lite: counters, 3-4-word text, music phases | `top-editor-styles` |
| Ad or value reel, 6-15 s, music-led | P1 glass spotlight / P2 editorial red | `pro-video-editing` |
| "3 tips / 3 mistakes" educator | P6 violet condensed tips | `pro-video-editing` |
| Brand / agency opinion, dark room | P7 noir red kinetic | `pro-video-editing` |
| Real estate, finance, "X vs Y" explainer | P8 orange explainer (= Edit-Kit Agent Story) | `pro-video-editing`, `edit-kit-playbook` |
| White-studio personal brand / hiring | P9 lime studio | `pro-video-editing` |
| Seated educator in a dark studio, AI / software / editing tips | P10 amber UI educator (typed title scenes, one-word chest captions, background takeover on long takes) | `pro-video-editing` |
| Podcast or interview clip with quotable lines | P11 podcast scene inserts (two-size light captions + a designed scene per key line) | `pro-video-editing` |
| Voice-over or script with no camera footage; "X owns Y%" facts, finance / business idea, product or template promo | P12 editorial cutout explainer (light cutout act → one flash → dark object act; blur-in two-font captions, stat wedge, light-leak flashes). Its dark object scenes also work as inserts in a talking-head short | `faceless-explainer-reel-edit-style` (= P12) |
| Talking-head tips / opinion / client A-roll that must look heavily edited (speaker inside graphics, hidden jump cuts, pedestal lists) | P13 two-tier kinetic talking head | `event-map-reel-edit-style` (= P13) |
| Story, history, news or mystery told by voice-over, no camera footage | P14 faceless 2.5D documentary (dioramas, camera never stops, text only when the word is the picture) | `event-map-reel-edit-style` (= P14) |
| Calm premium talking-head tips / list / "mistakes" short (editing, design, business), clean dark studio shot | P15 Ultimate Editors sans + script (small sans + one blue italic-serif keyword, overlay / split / full-screen off-white scenes, 1-2-3 step pill) | `ultimate-editors-shortform-style` (= P15) |
| Naveen bro client shorts, or any "aesthetic / premium / advanced Instagram-editor" talking head | P16 aesthetic pro reel (dark warm grade, M4 Haldi-Kumkum captions with blur reveal, cut every 2-2.5 s, literal B-roll per noun, one quiet insert every 6-8 s: paper scene, face HUD, ring, number giant) | `aesthetic-pro-reel-edit-style` (= P16) + `mustard-red-caption-style` |
| Caption-led talking head like the Instagram editor showcases ("Raw vs My Edit", "$10 vs $80", "Edited by"); the owner's 2026-11-27 references | P17 type cards + inversion, P18 brand-colour caps + pills, P19 under-chin kinetic (safest base), P20 script + sans. Pick ONE; captions on the chest (chin + 17 % of the height), one hero word per card, focus-pull returns, `caption_moves.py` layers | `editor-showcase-caption-edit-style` (= P17-P20) |
| Any other form (vlog, tutorial, UGC ad, wedding teaser, fan edit) | the matching row of the atlas | `video-styles-atlas` |

Details and what to borrow from each: `references/style-profiles.md`.

## QC (run on the encoded MP4)

- **Frames and black frames:** frame count and duration match the plan; no black or frozen frames except planned ones.
- **Contact sheet:** check every 0.5 s against these questions:
  - Does the hook move by frame 3?
  - Is anything static for more than 2.5 s?
  - Is any caption over the mouth or outside the safe zone?
  - Are there two elements on the footage at once?
  - Is there any caption longer than 3 words?
  - Is there more than one accent colour?
- **Sync:** every caption pop and B-roll lands 0-1 frames late or up to 0.3 s early. Check 5 random words on a strip.
- **Audio:** -14 ±0.5 LUFS and ≤ -1 dBTP. No SFX masks a word: 300-4000 Hz energy check 0.3 s after each cue.
- **Loop seam:** last frame vs frame 0 mean luma differs by less than 10, and the last word flows into the first.
- **Senior pass:** remove anything that has no job. Watch at phone size, muted and unmuted. List the three weakest moments.

## Files

- `LEARNING-LOG.md`: every edit and every piece of feedback, newest first. **Append after every edit.**
- `references/hook-and-story.md`: hook types, story shapes, loops, CTA.
- `references/cut-pacing-camera.md`: silence cutting, rhythm, zooms, transitions.
- `references/captions-type-colour.md`: caption system, fonts, accent, grade.
- `references/broll-graphics.md`: B-roll sourcing and timing, PNG, MG, behind-head text.
- `references/sound-design.md`: voice chain, SFX map, music, mastering.
- `references/export-qc.md`: export spec, safe zones per platform, QC commands.
- `references/style-profiles.md`: Tharun / Hormozi / Iman / MrBeast / calm / P1-P5 in brief, plus P10-P14.
- `references/web-research-2026.md`: sourced platform facts (label ONL).
- `tools/shortkit.py`: the lean renderer (edl.json → 1080x1920 MP4 + mix). Usage at the top of the file. Since 2026-11-22 it also draws the P13 two-tier keyword (role colour, track-in, letter stagger, pivot bar, strike), RGBA layers behind / in front of the speaker, a black-and-white stretch, text outline and panned SFX. Working example: `edited videos by claude/22. Grayscale Tip/code/`. Since 2026-11-23 also a second keyword font (`"font": "serif"`), giant strike and font, and one music removal (`music.gaps`); example `edited videos by claude/23. Uncertainty Truth/code/`.

### shortkit keys added 2026-11-25 (all optional; old EDLs render unchanged)
| Key | What it draws | Skill that uses it |
|---|---|---|
| `style.cap_color` | lead-in colour (default white); one word may carry `{"c": "#hex"}` | `mustard-red-caption-style` |
| `style.ghost: 0.30` | lead-in line waits at 30 % opacity, each word goes solid on its time (one token per word) | `mustard-red-caption-style` M4 |
| `style.reveal: "blur"` | every word arrives blur-to-sharp in 0.18 s (alpha 35→100 %, scale 1.05→1) instead of the pop | `aesthetic-pro-reel-edit-style` |
| `style.mono_font` | font for HUD labels (default CourierPrime-Bold) | `aesthetic-pro-reel-edit-style` |
| keyword `"font"`: `"serif"` / `"script"` / a file name such as `"Italianno-Regular.ttf"`; `style.script_font` | serif or script keyword, or any file in `fonts-and-colours/assets/fonts` (an absolute path also works). `giants` still need the full path | `mustard-red-caption-style` 2c (pairing moments) |
| group `"y"` | moves one caption group (pairing moments go on the plain wall above the head, y 300-640) | `mustard-red-caption-style` 2c |
| env `SHORTKIT_LAYOUT=basic` | old text layout without raqm kerning, only for partial re-renders of projects first rendered before 2026-11-25 | this skill |
| keyword `"brush": "#hex"` / `"dot": "#hex"` | haldi brush stroke behind the word / kumkum full stop after it (no dot after ?!.,) | `mustard-red-caption-style` M4 |
| `brackets[].label`, `.shape: "corners"/"ring"`, `.color` | viewfinder corners or a thin glowing ring round the face, mono label + live X/Y | `aesthetic-pro-reel-edit-style` (face HUD, ring) |
| `paper: [{t0, t1, color, ribbon, text, key, path: "swoosh"/"arc"}]` | room replaced by textured off-white paper, speaker cut out with a soft shadow, haldi ribbon draws on in 0.45 s; captions turn ink | `aesthetic-pro-reel-edit-style` (paper scene) |
| `stacks: [{t0, t1, y, x, align, size, ratio, lead, fx, ghost, behind, out, c, cs, font, lines: [[[t, text, "s" or "b", {fx, c, font, size, d, dur}]]]}]`; style `stack_font`, `stack_small_font`, `stack_size`, `stack_ratio`, `stack_lead`, `stack_fx`, `stack_color` | word stack that builds word by word (2-5 lines, big meaning words + small link words, fixed layout); token fx `cut` / `fade` / `blur` / `rise` / `grain` / `pop` / `type` (letters one by one across the spoken word); captions hide while a stack is up | `text-animation-moves` |
| sfx `"ss"` (with `"dur"`) | slice of the sound file: start + length (a typing burst cut to the word) | `text-animation-moves` section 5 |
Range render: `video edl --from A --to B` writes frames only (`work/frames/%06d.jpg`, numbered by absolute frame); encode them with imageio ffmpeg `-framerate 60 -start_number N` and mux the audio with `-ss/-t`. Example EDL with every new key: `edits/mustard-red-captions/code/pinktax_PRO_edl.json`.
Fonts: `pro-font-and-subtitle-guide` (which file for which role; 7 fonts have no ₹). Telugu script renders correctly since 2026-11-25 (Homebrew fribidi turned on Pillow's raqm; check with `pro-font-and-subtitle-guide/tools/telugu_check.py`). Captions stay Tenglish unless the video asks for script. For a partial re-render of an older project, set `SHORTKIT_LAYOUT=basic`, because Latin kerning changed by up to 1.6 %.
