---
name: youtube-long-video-editing
description: Build kit and QA rules for Deepak's 16:9 long-form YouTube explainers (20–30 min, multi-segment CapCut exports) — segment join/EDL, graded base-frame extraction, HTML/GSAP scene engine rendered frame by frame, layout QA of every scene, music/SFX mix, encode and final checks. Use when editing any long-form explainer, combining segments into one film, or rendering motion graphics over a long talking head.
---

# Long-form explainer pipeline (first built on the Indian IT / Y2K / AI video, 2026-09-30)

> **Note (2026-10-06):** `experiment/` paths in this skill are historical — that folder was cleared. Final videos + edit notes: `Raghu and claude/edited videos by claude/`. Reusable code: the `code/` folder inside each video folder. Reference analyses were folded into the skills and deleted.

Project: `experiment/claude5_y2k/` (`build/` = code, `work/` = intermediates, `deliver/` = outputs). Look/feel rules live in `motion-graphics-style` → "Editorial print-grain explainer"; Deepak's rules in `my-editing-rules` (his word wins). Tags: **[USED]** done on this video · *(Claude, not yet approved by Deepak)* = my own QA rule.

## 1. Pipeline [USED]
1. **Transcript first:** faster-whisper small, `language="en"` (translation of Telugu/Tenglish), word timestamps, VAD → `work/asr/`. Map to output time through the EDL (`edl.py` → `edl.json`, `transcript_out.json`, `anchors.py` word lookup).
2. **Join:** butt-join the segments; cut only true duplicates/false starts on CapCut's single frames of digital silence; 12 ms audio cross-fades (`make_voice_raw.py`).
3. **Base frames:** one graded JPEG per output frame (`make_base2.py`, 4 parallel ffmpeg jobs, 3000-frame chunks, ~43 min for 71,695 frames at 1440p source). Then `verify_base.py`.
4. **Scenes:** HTML + GSAP, one global clock, scenes built lazily and destroyed 40 s away (`engine.js`), components in `lib.js`, the edit in `scenes1-4.js` (one per segment). Every graphic calls `c.sfx()`.
5. **Stills QA** before the long render (see §3), then `render_all.sh` (6 Chrome workers, 4-sample motion blur only inside slide windows), `post_frames.py`, `encode.sh`.
6. **Mix** (`mix.py`): voice chain → −16 LUFS, downward expander in pauses, SFX map from the cue export, music by hand per section (no sidechain), one removal, loudnorm two-pass → −14 LUFS / −1.5 dBTP.
7. **Final QA** (`qa_final.sh`): streams/tags, frame count, freeze + black detection, loudness, 10-s contact sheets, first/last frame.

## 2. Gotchas (all hit on this video)
- **Never blend a looped still (`-loop 1 -i mask.png`) with a trimmed video in one ffmpeg graph.** The output silently froze after ~7,600 frames (thousands of byte-identical JPEGs) and every preview after that point showed a still face. Use a single-input chain, exact per-chunk seek `-ss (a-0.5)/fps` before `-i`, `-fps_mode passthrough`, `-frames:v n`, `-start_number o`; put vignettes in the browser instead.
- **Verify extraction by bytes:** re-decode 90 frames before every chunk seam in one continuous run and compare the JPEG bytes with the chunk's first frames (identical when correct); scan for byte-identical consecutive frames. CapCut itself duplicates the odd frame (Segment 1 frames 510/511 are identical in the source) — single pairs are normal, runs are a bug.
- 1440p BT.709 source → mjpeg writes BT.709 YCbCr that browsers decode as BT.601: ≈0.5 level shift on skin, acceptable; add `out_color_matrix=bt601` next time.
- **Stacking contexts:** give every layer (`L_under … L_hud`) its own z-index or scene roots escape and the framed talking head renders black.
- GSAP `set` of `innerHTML: '01'` becomes the number 1 → use a text-swap helper for digits.
- `.replace(/C/g, colour)` on SVG path strings destroys `C` curve commands → use a `{c}` placeholder.
- A round-cap stroke shows a dot before `drawIn` starts → keep the path at opacity 0 until the draw.
- Auto-fit keyword cards: measure text with a canvas, never a fixed width (“Faster work = fewer j…” got clipped).

## 3. Layout QA rules *(Claude, not yet approved by Deepak)*
- Render the **end state of every scene** (t1 − 0.25 s) plus the middle of scenes longer than 8 s at half scale, 12 per contact sheet, and read every sheet before the full render.
- Measure each paper scene's visible content box at its end state (`measure_layout.js`): if the content centre is above y 420 or more than 400 px of the bottom is empty, re-centre it (a lone pair of cards, a lone chart, a quote block).
- **A lone chart sits centred and slides left (0.6 s, power3.inOut, soft paper whoosh) when its partner chart arrives** — never leave half the frame empty for 9–12 s.
- **Framed talking head:** fade the side content out 0.12 s before the frame grows back to full screen, or the text sits on top of his face for the whole exit.
- **Labels follow the speaker's own definitions** (he defined Level 2 = senior engineers, Level 3 = managers; generic "developers · team leads / architects" labels contradicted him).
- A punch line needs at least 0.8 s on screen; extend the scene into the next sentence rather than cut it after 0.5 s.
- **Never idle on a fake zero:** a number that counts up from 0 stays hidden until it starts counting (built into `counter()`); an empty ring or bar may wait, a "$0" / "0%" may not.
- **No dead openings:** every hard-cut scene shows content within 0.3 s (`measure_first.js`). If the speaker talks before the key word, fill the gap with a setup line ("Many people are asking…") or a "before" state (a calm "Payments running" card that flips to the red failure on the word).
- **No static hold over ~4 s while he keeps talking:** run `freezedetect` (n −55 dB, d 1.5 s, 480×270) on the master, map every hold to its scene, and give each long one a word-synced micro-beat (DROPPED/KEPT labels, a playhead rolling 1999 → 2000, marker on the numbers he repeats, a "3 years" span). Talking-head time must show zero holds.
- **Check the original Telugu before echoing his words on screen:** the English ASR turned "AI vastundi, 10 mandi kaavalasina deggara iddare theesukuntundi" into four repeats of "What should I do?". Time visuals to `transcript_y2k.srt` meaning, not to translation artifacts.
- **Review the final frames before encoding:** a contact sheet every 10 s of `work/frames` caught idle zeros and empty panels that the per-scene stills missed; fix, delete only those frame ranges, re-render with `--skipdone`, then encode once.

## 4. Notes (2026-10-01)
- Temp venvs (`scratchpad/venv`) disappear between sessions: recreate with `python3 -m venv … && pip install pillow numpy soundfile scipy`.
- Render with absolute paths only (`--base`, `--out`); a relative `--base` gives `ERR_INVALID_URL`.
- A black-fade layer (`#thFade` inside `#thWrap`) was prototyped and removed; if ever needed, add it per scene, not as a default.

## 5. Audio redesign pass (2026-10-01)
The v1 mix (placeholder procedural SFX, 15 library tracks at −24 dB under the voice) was rebuilt without touching the picture: `build/audio2/`, method and numbers in the **`sound-and-music-design`** skill. Re-use the scene engine's cue export (`engine.js` records `scene` + call-site in EXPORT mode; `node render.js --export work/audio2/cues_ctx.json`), keep `work/mix/voice.wav` as the voice, and remux the new master audio onto the existing video with `-c:v copy` (`-c:a aac_at -b:a 320k`). Never re-render frames for an audio change.

## 6. AI Tech News ep 1 kit (2026-10-02) — `experiment/claude9_ainews01_edit/`
- **1440p output:** stage 1920×1080 CSS at DPR 4/3 → 2560×1440 JPEG frames; base plates 2560×1440 `yuvj444p` with an explicit BT.601 matrix (Chrome decodes JPEG as 601); 6 workers ≈ 25 fps on this Mac, 41,572 frames ≈ 30 min. Seams verified by bytes, 0 duplicate runs.
- **Word timing for Tenglish:** forced-align the romanized SRT with `torchaudio.pipelines.MMS_FA` (torch/torchaudio 2.2.2 is the last Intel-mac wheel; venv in the scratchpad; star tokens absorb speech outside each cue). Make it resumable per cue and run it with `nohup` — the tool's background limit (30 min) killed the first run and lost everything. `make_words.py` → `words.js`: `w(q, near)` logs when the match lands in another SRT cue than `near`; `cw(i, q, k)` anchors to cue *i* (use it for common words like "So", "Ee", "updates").
- **Auto-fit wall captions:** measure each line and shrink it to the space left of x 1868; scenes are built with the root `display:block; visibility:hidden` so `scrollWidth` is real.
- **Gotchas:** an upd-driven transform (`cam`, `drift`) and a GSAP x/y tween on the same element fight (the upd wins) → wrap one in the other · never store elements on a custom `.role` property (Chrome reflects ARIA `role` as a string; GSAP then treats it as a selector) · `maskUp` must start at ≥ 140 % or tall glyphs peek through the padding · split layouts: the clip inset is in the wrapper's *local* coordinates (`clip = panelWidth − dx`).
- **Review loop:** `review.py` (3 stills per scene at DPR 0.5, 12 per sheet, ~40 s for the whole film) → read every sheet → `pick.py` for a focused re-check of the fixed scenes. First pass found: dead openings (a label alone for 2–5 s before its word), captions running off the right edge, a black gap in split layouts, a camera upd cancelling a slide, a highlight scheduled after its scene ended.
- **Audio:** `audio.py` (voice EQ/de-ess/2.5:1/expander → −16 LUFS stem; 281 cues from the export → real library slices + synthetic sub/knock/click hits, tiered against the local voice level, +18 ms after the picture; 9-section bed from `bgm for claude/` switching on the chapter hits, D 17–23 dB; masters −14 LUFS / −1 dBTP with and without music).
- **v2 correction pass (2026-10-02):**
  - **Rhythm audit:** in export mode, wrap `tl.fromTo` / `tl.to` and the lib helpers (`V()` in cam keys, `textSwap`, `typeOn`, `counter`, ladder cuts, clip frames) so every visual event lands in `window.__vis`; merge it with the scene cuts and list holds over 4.8 s. Deepak's target is a longest hold of about 5 s (ep 1 went from 22 holds over 5.4 s to a longest of 5.2 s).
  - **Recipe:** move `work/frames` → `work/frames_v1` and the masters → `deliver/_v1/`; re-export and regenerate `subwin.json`; do a full render (~35 min) rather than patching 30+ ranges; run `audio.py sfx` then `mix` (music unchanged); re-export only the SFX stem; then `encode.sh` and `qa_final.sh`.
  - **Gotchas:**
    - A quote cycler inside a fixed-height `overflow:hidden` holder must offset in px. A 2-line quote at `yPercent:130` still showed inside a 240 px holder.
    - `.lbl` is `nowrap`, so wrapped tags need `whiteSpace:'normal'`.
    - Check the right edge of anything inside a camera-pushed wrapper at the pushed scale.
    - Read every new beat at DPR 1 crops, not only on the 0.5 contact sheets.
  - **Green-screen brand card:**
    - Key with ffmpeg `chromakey=0x00AE3E:0.10:0.06,despill` to RGBA PNGs, fed frame-accurately via `c.media`.
    - Offset the clip so its click frame lands on the spoken word.
    - Its own audio goes in as an SFX cue (`chime` tier, no one-frame offset).

## 7. RAG concept explainer kit (2026-10-03/04) — `experiment/claude10_rag_edit/`
Full 9:29.6 talking head, kept uncut. Build: `build/lib.js` + `s0…s7_*.js`, 71 scenes. No BGM.

**Script SRTs from other tools can't be trusted for timing.**
- Gemini's SRT drifted up to ±15 s from the audio, and 11 of its cues were never spoken.
- Fix: align the *whole file* in one pass with `build/align_rag.py`. It computes MMS_FA emissions in 24 s chunks with 3 s context, then runs one global CTC alignment with a star token between cues.
- Find unspoken cues with `build/emis_rag.py`: greedy-decode the emissions into a romanised "heard" string and compare it with each cue's text (similarity < 0.5 or score < 0.2 = suspect). Drop those cues and re-align.

**Reference download (YouTube, with his permission):**
- Python 3.9's yt-dlp is too old. Use `uv python install 3.12`, a venv with `yt-dlp[default]`, and run with `--js-runtimes node`.
- The `android_vr` client lists HD formats but returns 403s.
- Pull the auto-captions too (`--write-auto-subs --sub-format json3`) so the frame sheets carry the spoken words. Tools are in `skills/_video-analysis-tools/`.

**Components:**
- `words()`: words appear as spoken.
- `hlType()`: key term typed into a colour block.
- `sideLabels()`: labels open from a line, right-aligned beside the face.
- `card(world)`: light / canvas / char / night.
- `chapterCard()` with the architecture rail.
- `itemCard()`: "01. Cost".
- `mythCard()`: rising blue planet.
- `splitPanel()` + `splitTH()`: black panel from the right; his footage slides −540 px.
- `chunkPage()`: a page cut into chunks with dashed scissors cuts, then separated.
- `dbTable()`, `chatWindow()` + `chatStack()`: bottom-anchored messages that push the old ones out of the window.
- `node()`, `link()`, `curveArrow()`, `tile()`, `food()` (drawn food icons, no stock).

**Gotchas:**
- A round-cap SVG stroke at dashoffset = length still draws a dot. Keep the path at opacity 0 until its draw starts (fixed in `drawIn`).
- A card must have content in its first ~0.3 s. Start chapter or question cards no more than about 0.6 s before their first word, and extend the previous scene to meet them.
- White text on his bright wall needs the light bottom fade (playbook rule).

**Numbers:**
- 1,548 visual events, longest gap 4.66 s.
- Full-screen 75 %, his face 25 % (4 scenes moved to split panels to keep him present).
- 316 SFX cues (33/min) tiered against the local voice: micro −24, tick −21, foley −18, chime −14, impact −9 dB.
- Master −14 LUFS / −1 dBTP, no BGM.

## 8. Day 03 kit — "How machines are trained" (12:57, 2026-10-07) — `edited videos by claude/10. How Machines Are Trained/code/`
**Look (approved on 5 stills):** graphics live *in the room with him*, not on slides. Details in `motion-graphics-style` → "In-the-room editorial system".

**Engine upgrades (`engine.js`, `lib.js`):**
- **Layers:** `L_wall` (behind him, follows the camera) → `L_plant` (the plate masked by a **static plant alpha**, so leaves sit in front of wall text) → `L_person` (Vision matte, LA PNG on even frames) → front.
- **Kit registers ranges per scene:** `_person`, `_opaque`, `_slides` (split-panel slide eases from the camera track), `_fx` (blur/shade plates), `_grain`, `_noPlant`.
- **Props mask:** the mic foam and shock mount are solid shapes; the mic arm is left out (a threshold mask looked ragged), and coloured worlds fade to black underneath it.
- **Camera:** framing changes only on his ~80 jump cuts (wide ↔ 1.075), plus a 2.5 % drift per shot. `camPunch(t, s)` snaps on a hero word and holds to the next cut.
- **Matte safety:**
  - `render.js` skips any frame whose matte isn't on disk yet (`__maskMissing`); a re-run with `--skipdone` fills the gaps.
  - The export samples even frames only, so a scene starting on an **odd** frame needs the matte for f−1. Check for missing frames after each pass.

**Speed lessons (measured on this Mac):**
- **Extraction:** the `accurate_rnd+full_chroma_int` swscale flags cost **7×** (54 s vs 8 s per 90 frames) for a mean difference of 1.4 levels, so drop them. 5 parallel chunks then run at about 28 fps.
- **Render cost under load:** about 1 fps per Chrome worker at 1440p (seek 0.3 s + capture 0.65 s).
  - Split long ranges into parallel jobs with **disjoint** ranges.
  - The frame list is fixed when a job starts, so a second job on an overlapping range duplicates work.
- **Killing a renderer:** kill its Chrome children too (`user-data-dir=…chrome_r<pid>_*`), or they keep eating CPU.
- **Waiting on a process:** `pgrep -f "<pattern>"` inside a bash loop matches its own command line, so wait on a log line or a PID instead.
- **Segment encodes:** encode chapter segments as they finish, with identical x264 params (`-g 120 -keyint_min 120 -sc_threshold 0`). Join them with the concat demuxer `-c copy` and mux the audio last. The joins verified frame-exact.
- **AAC overshoot:** AAC adds about 0.6 dB of true peak, so limit the master at −2.2 dBFS to deliver −1.0 dBTP.

**Parallel authoring (when Deepak says "make it fast"):**
- Lock the look first.
- Write `KIT.md`: the brief, the API, design rules, an SFX vocabulary, and a stills command.
- One scene file per chapter, each wrapped in an IIFE, with its own `test_*.html` page.
- Three agents built three chapters in 60–100 min while I built intro, vocabulary and outro.
- **Gotcha:** a Chrome page loads the scene files once. A render started before an agent's last edit is stale and must be re-rendered.

## 9. Sale-phones kit (client buying guide, 11:30.7, 2026-10-08) — `edited videos by claude/11. Sale Phones Buying Guide/code/`
**Edit decision list with reorder:** `keep.json` = ordered kept SOURCE ranges (a hook can move ahead of the promo). `edl.py` writes `edl.js`: `EDL_SRC` (output frame → source frame, used by the engine for plates, mattes and the live bubble), `EDL_CUTS` (shot changes incl. his own jump cuts) and `S(t)` (source → output seconds). Scenes are authored in **source** time and wrapped in `S()`, so a trim or reorder never breaks a scene. `audio.py` cuts the voice through the same list on frame boundaries (800 samples per frame at 48k) with 6 ms fades at each join.
**Timing audit tools:** `clips_te.py` (Whisper large-v3 `te`, beam 5, word times for short windows, one model load), `kw.py` (MMS keyword spot + level onset), `audit_match.py` (every timed event in the scene files next to the Telugu words and speech bursts around it). Measured on this Mac: ~10 s of CPU per second of audio with beam 5; a 10–14 s window often decodes as noise, 3–6 s windows are clean.
**Render while auditing:** render only the ranges whose timing is final, at `nice -n 19` (`render_range.sh`), and fix later ranges; a Chrome page loads the scene files at start, so a range started before an edit is stale only if the edit falls inside it. Speeds: 18 fps with 6 workers at 1440p when the CPU is free, ~10 fps at nice 19 beside Whisper.
**Fix after render without re-rendering:** a trim that left an 80 ms syllable was muted in the audio (mute list in `audio.py`), not moved, which kept 30,000 rendered frames valid.
**Proof captures:** `grab_mark.js` screenshots the paragraph that contains a phrase and returns the phrase's exact rectangles in image pixels, so the highlighter lands on the words (multi-line wipes supported in `K.hl`).
**Encode:** CRF 17, preset faster, 2560×1440p60 → 3.1 GB / 36 Mb/s for 11.5 min (≈ 24 min encode).

## 10. Day 06 kit — "Classification vs Regression" (16:37, 2026-10-12) — `edited videos by claude/12. Classification vs Regression/code/`
**Build:** same engine as Day 03/RAG (HTML/GSAP, one clock, DPR 4/3 → 1440p, 4-sample motion blur in SUBWIN windows). Look locked on 8 style frames + a 54 s sync clip, then the chapters were built one by one, each beat checked on stills (`stills.py … test_<chapter>.html`) before the full render.
- **Helper agents per chapter (KIT.md + EDIT_PLAN.md) produced nothing.** They were stopped and the Mac restarted mid-run. Building the chapters myself in sequence, one stills sheet per beat, took ~3 h for 9.3 min of graphics. Keep KIT.md/EDIT_PLAN.md anyway: they are the checklist.
- **New kit helpers** (`lib.js` §20):
  - `K.pulse` / `glow` / `lite` (chip turns cyan) / `ring` (card outline) / `dim` / `gone` / `badge` (cyan ✓ circle) / `strike` (red or cyan line across an element).
  - `K.roll(..., {tight:true})` sizes each digit column to its final digit, so "100" never reads "1 00".
  - `rawAt(cue, '/')` finds symbol tokens ("/", "*"), which the letter-only word matcher cannot see: `cw(cue,'/')` silently returns the cue's first word.
- **Canvas devices that worked:**
  - **A wide canvas with a camera pan between two ideas** (`CAM` div 3840 wide + `K.ccam`), e.g. binary → multi-class.
  - **A tree that morphs into comparison headers.** GSAP x/y on centred nodes; the rest of the tree fades.
  - **Ghost "?" slots that fill on the spoken word** (price, categories, the forest). The frame is never empty and nothing is shown early.
  - **"this process = X" typed into the cyan block,** reused for every definition.
  - **Same-input comparisons:** one photo → one category vs many labels; one table → Pass/Fail left, marks right.
  - **A plant at 3:01 paid off at 13:48:** the logistic node slides sides and its "?" becomes ✓.
- **Stills-first findings** (fix before rendering, see §3):
  - Diagrams too small for the frame: scale up to ~1.15× and rebalance margins to ≥ 120 px.
  - 1–5 s of empty canvas after a cut: cut to the canvas on the word that brings content, carry an object over, or show a ghost slot.
  - Label rows over ~22 characters get auto-shrunk to ~34 px: split the row.
  - A counter and a result line colliding.
  - Axis labels under a moving tag.
- **Numbers in Telugu speech:** the MMS aligner was right for 0 / 1 / 90 / 90 % (it matched the voice-envelope onsets after silences). Whisper large-v3 `te` on 3–5 s windows drifted 0.2–0.35 s early on digits, or garbled "65 lakhs" entirely. Trust the aligner when the envelope agrees; check the envelope at 20–30 ms.
- **Ops:**
  - **After a restart:** the render resumes with `--skipdone`. Delete only stale frames, e.g. the 3 boundary frames rendered with a placeholder scene.
  - **Merge sub-frames per range** (`merge_ranges.py`) only behind the render front.
  - **Encode finished segments while the render runs.** It costs ~25 % render speed, and the total time is similar.
  - **Rhythm audit:** `rhythm.py` on the full export found only two holds over 5 s; one was split by a camera punch-in, which the audit does not count.
- **Numbers:** 68 scenes, ~3,500 visual events, 488 SFX cues (19–40 per minute), his face visible 44 % (labels, captions, notes pages), master −14 LUFS, no BGM, no grade.

## Render-ops gotchas (video 13, 2026-10-13)
- Pass **absolute** `--base/--masks/--out` paths to `render.js` (relative ones give `ERR_INVALID_URL` and black frames). When restarting, `kill -9` the old node process and confirm with `ps`: a stale run kept writing black frames into the same folder.
- Render pages load the scene code at launch: any patch made after a render starts means deleting and re-rendering that time range.
- Person mattes are on even frames; a matte range that starts on an odd frame also needs the even frame before it, or the renderer skips that frame.
- Wall-word boxes: matte one frame every 2 s at 480×270 (`matte … balanced`), take the head's right edge → box from head+40 px to x 1780, y 70–440 (above the lamp); anchor the punch-in right of the head so the word stays in frame.
- Word-swap montages on the wall need a 0.05 s exit with no blur, or two words overlap.

## 11. Add-on-top kit (video 13 v2, 2026-10-13) — `edited videos by claude/13. Top 5 Skills AI Era/code/` (v2 files)
**Base plates from the delivered master.**
- `make_base_v2.py` grabs only the on-footage ranges: `-ss (a-0.5)/60` before `-i`, `-fps_mode passthrough`, then 709 tv → 601 full-range JPEG.
- Use the camera identity (`camera_v2.js`) and `GRAIN_TH=0`, because the master already carries the camera and the grain.
- `engine_v2.js` adds `sc.gray(t)` for B&W pause beats.

**Render only v2 frames.**
- Frames are `ceil(t0*60) … ceil(t1*60)-1` per scene (`frames_v2.json`, `ranges_v2.json`).
- 10,295 frames took 21 min with 6 workers.
- Motion blur:
  - `--sub 3` only in the fast-move windows;
  - `merge_sub.py` averages in linear light (gamma 2.2), saves 4:4:4 q95 and deletes the subs.

**`final_encode.py` passthrough.**
- The master is decoded to raw yuv420p; untouched frames go straight to x264 as bytes.
- v2 JPEGs → RGB → BT.709 TV YUV 4:2:0 in numpy, prefetched by 4 threads inside a 6 s window (a full-buffer wait deadlocks).
- crf 16 / fast ran at about 19 fps (about 38 min for 43k frames).
- **Check:** each rendered frame must match its own master frame best (PSNR ≈ 45 dB at k = 0 vs ≈ 44 at ±1).

**Audio.**
- `audio_v2.py` rebuilds the v1 SFX stem from the v1 export (same seed, so the cue sheet is identical) and renders `sfx_v2.wav` from the v2 export.
- `mix` sums voice + both stems.
- In a window without new cues, the delivered audio matched to −42 dB (AAC noise only).

**Gotchas.**
- **Tag the raw input** (`-color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709` before `-i -`). Untagged rawvideo is treated as BT.601, and ffmpeg 7 then silently converts 601 → 709 because the output is tagged 709: every frame came out 2.5 Y darker (PSNR 35 dB vs the source). Tagged: mean diff 0.0, PSNR 48–52 dB. Always measure passthrough frames by exact index (`select=eq(n,N)`) against the source before delivering.
- A hand label must finish writing at least 0.15 s before its scene ends ("always changing" was cut at "CHANG").
- GSAP 3 has no `className`: use `attr: {class: …}`.
- Never `tl.set` `innerHTML` (backward seeks don't revert it): switch text in a `c.upd`.
- An upd-driven `transform` overwrites a GSAP pop on the same node, so wrap one inside the other.
- `ERR_FILE_NOT_FOUND` once per worker was a font subset for a symbol glyph, which is harmless.

## 12. AI Tech News ep 02 kit — premium SaaS news show (16:10, 2026-10-15) — `edited videos by claude/14. AI Tech News EP02/code/`
- **Tenglish timing in minutes, not hours.** Whisper large-v3 `te` on 16 min would take ≈ 3 h on this Intel Mac (Telugu script costs many tokens). Instead:
  - `emis.py`: MMS_FA emissions for the whole voice track (24 s chunks + 3 s context, ≈ 16 min CPU, saved as `mms_emis.npy` + a greedy romanised "heard" stream).
  - `heard.py t0 t1`: prints the heard stream with 1 s ticks; reading it is how the beats were found.
  - `kw.py 'word|variant' t0 t1`: local CTC alignment with a free start and end on the emissions. A score ≥ −1 is reliable; ≤ −3 means check the heard stream by eye. English loanwords and names (OpenAI, Starlink, Ambani, Jasmine Wang) spot cleanly.
  - large-v3 `translate` (≈ 14 min) gives the meaning. Spoken onsets landed 0.1–0.5 s later than its word times.
  - venv: `torch==2.2.2 torchaudio==2.2.2 'numpy<2'` on Python 3.9 (uroman has no 3.9 wheel and is not needed). The MMS_FA weights are cached in `~/.cache/torch/hub/checkpoints/model.pt`.
- **Real sources instead of screenshots.** `capture.js` re-captured 17 article pages at 2× (its rects are CSS px; ×2 for image px). `textbox.py img x0 y0 x1 y1 dark|light thr gap` returns headline line boxes and word runs to place the marker (gap 0.14 for big headlines). His 800 px screenshots were upscaled 2× (Lanczos + light unsharp) where a page could not be captured. On dark pages (X posts, TechNode) the marker uses screen blend at 0.42.
- **Engine additions:** `sc_frame` (footage-card framing: th() returns `{s, x, y, free, radius}` with a rounded clip and a card shadow) · `sc_split` returns the panel to fill · `sc_subscribe` (keyed brand card, cursor click on the word) · `K.mc` (match cut) · `K.chapter` (glass key row + dip) · `K.cap` right-anchored so long chips never leave the frame · `camera.js` alternates framing only on verified jump cuts (scene-detect, then a frame-difference ratio ≥ 8 against the neighbours).
- **QA that caught real problems:**
  - contact sheets of the *rendered* frames every 2 s, read while the render ran: a match-cut pull-out clipped its page at the layer edge (fixed with a hand-off card, re-rendered 4 s);
  - `freezedetect n=-55dB d=4` on the encoded master found 7 graphic holds of 5.2–7 s that the event audit missed (upd-driven changes and slow drifts don't count): add word-timed micro-beats, re-render only those ranges (2,592 frames, 3 min), re-encode only the affected segments.
- **Ops:** 58,188 frames in 70 min (6 workers, ≈ 14 fps with segment encodes running alongside); 4 segments with closed 120-frame GOPs joined by concat `-c copy`; CRF 16 + grain = ≈ 71 Mb/s (8.6 GB for 16 min), so use CRF 18 when size matters. Gotchas: `python3 -I` hides the user site (faster-whisper "missing"); zsh does not word-split `$var` (`set -- $spec` fails, use Python loops); foreground `sleep` is blocked (use Monitor or `until` loops in background jobs).
- **v2 real-evidence pass (2026-10-16): swap content, keep the edit.** New helpers in `lib.js`: `K.photo` (rounded credited photo card; same `crop/k` contract as `K.shot`, so `K.mark` works on it), `K.face`/`K.facify` (real-photo avatar with a company badge), `K.ntag` (name tag on a person in a photo), `K.footage` (a JPEG frame sequence as moving footage through `c.media`), `K.illus` (ILLUSTRATION tag). 20 scenes changed = 273 s, 16,383 frames rendered in ≈ 18 min with `--ranges` straight into `work/frames`; `render.js --export` then a cue diff (8 cues changed) → `audio.py sfx` + `mix`; all 4 segments re-encoded because the changes spanned them. Test stills at 28 beats (`--times`) before the full render caught 5 layout issues (a seal cut by the crop, two source lines touching, a chip covering evidence text, a cut-off quote line, a too-dark background plate).
