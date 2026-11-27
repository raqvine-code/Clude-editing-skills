---
name: youtube-long-video-editing
description: Use when editing any 16:9 long-form YouTube explainer (10-30 min, multi-segment CapCut exports), combining segments into one film, or rendering HTML/GSAP motion graphics over a long talking head. Pipeline (EDL join, graded base frames, scene engine, frame render, mix, encode), gotchas, layout/rhythm QA rules, and per-video kits (Y2K, AI News ep1/2, RAG, Day 03, Sale phones, Day 06, video 13 add-on).
---

# Long-form explainer pipeline

First built on the Indian IT / Y2K / AI video (2026-09-30). `experiment/` paths are historical; finals and reusable `code/` folders live in `CLAUDE 2.0/edited videos by claude/<n>. <title>/`. Look/feel: `motion-graphics-style`; Deepak's rules: `my-editing-rules` (his word wins). Rules marked (Claude) are my own QA rules, not yet approved by Deepak.

## 1. Pipeline
1. **Transcript first:** faster-whisper small, language="en" (translates Telugu/Tenglish), word timestamps, VAD. Map to output time through the EDL (`edl.py` -> `edl.json`, `transcript_out.json`, `anchors.py`).
2. **Join:** butt-join segments; cut only true duplicates/false starts on CapCut's single frames of digital silence; 12 ms audio cross-fades.
3. **Base frames:** one graded JPEG per output frame (`make_base2.py`, 4 parallel ffmpeg jobs, 3000-frame chunks; ~43 min for 71,695 frames at 1440p), then `verify_base.py`.
4. **Scenes:** HTML + GSAP, one global clock, scenes built lazily and destroyed 40 s away (`engine.js`), components in `lib.js`, edit in per-segment scene files. Every graphic calls `c.sfx()`.
5. **Stills QA** (section 3) before the long render; then `render_all.sh` (6 Chrome workers, 4-sample motion blur only in slide windows), `post_frames.py`, `encode.sh`.
6. **Mix** (`mix.py`): voice chain -> -16 LUFS, downward expander in pauses, SFX from cue export, music by hand per section (no sidechain), loudnorm two-pass -> -14 LUFS / -1.5 dBTP.
7. **Final QA** (`qa_final.sh`): streams/tags, frame count, freeze + black detection, loudness, 10 s contact sheets, first/last frame.

## 2. Gotchas
- **Never blend a looped still (`-loop 1 -i mask.png`) with trimmed video in one ffmpeg graph:** output froze after ~7,600 frames. Use single-input chain, exact per-chunk seek `-ss (a-0.5)/fps` before `-i`, `-fps_mode passthrough`, `-frames:v n`, `-start_number o`; put vignettes in the browser.
- **Verify extraction by bytes:** re-decode 90 frames before every chunk seam and compare JPEG bytes; scan for identical consecutive frames. Single duplicate pairs are normal (CapCut), runs are a bug.
- BT.709 source -> browsers decode JPEG as BT.601 (~0.5 level skin shift); add `out_color_matrix=bt601`.
- Give every layer (`L_under...L_hud`) its own z-index or scene roots escape and the framed head renders black.
- GSAP `set innerHTML:'01'` becomes number 1: use a text-swap helper. `.replace(/C/g, colour)` on SVG paths destroys curve commands: use a `{c}` placeholder. Round-cap stroke shows a dot before `drawIn`: keep path at opacity 0 until the draw.
- Auto-fit keyword cards: measure with a canvas, never fixed width.
- Temp venvs vanish between sessions: `python3 -m venv ... && pip install pillow numpy soundfile scipy`. Render with absolute paths only (relative `--base` -> ERR_INVALID_URL). A `#thFade` black-fade layer was removed; add per scene if ever needed.

## 3. Layout and rhythm QA (Claude)
- Render the end state of every scene (t1 - 0.25 s) plus the middle of scenes > 8 s at half scale, 12 per contact sheet; read every sheet before the full render.
- Measure each paper scene's content box at end state (`measure_layout.js`): re-centre if content centre is above y 420 or > 400 px of the bottom is empty.
- A lone chart sits centred and slides left (0.6 s, power3.inOut, soft paper whoosh) when its partner arrives; never leave half the frame empty 9-12 s.
- Framed talking head: fade side content out 0.12 s before the frame returns to full screen.
- Labels follow the speaker's own definitions, not generic ones.
- A punch line needs >= 0.8 s on screen; extend the scene rather than cut after 0.5 s.
- Never idle on a fake zero: counters stay hidden until counting starts; an empty ring/bar may wait, "$0"/"0%" may not.
- No dead openings: every hard-cut scene shows content within 0.3 s (`measure_first.js`); fill gaps with a setup line or a "before" state that flips on the word.
- No static hold over ~4 s while he talks: run `freezedetect` (n -55 dB, d 1.5 s, 480x270) on the master, map holds to scenes, add word-synced micro-beats. Talking-head time must show zero holds. Deepak's target: longest hold about 5 s.
- Check the original Telugu before echoing words on screen (English ASR turned a sentence into four "What should I do?"); time visuals to the SRT meaning.
- Review final frames (contact sheet every 10 s of `work/frames`) before encoding; fix, delete only those frame ranges, re-render with `--skipdone`, encode once.

## 4. Audio redesign (2026-10-01)
Rebuild audio without touching picture (`sound-and-music-design` has numbers). Reuse the cue export (`render.js --export`), keep `work/mix/voice.wav`, remux onto the existing video `-c:v copy -c:a aac_at -b:a 320k`. Never re-render frames for an audio change.

## 5. AI Tech News ep 1 kit
- 1440p: 1920x1080 CSS at DPR 4/3 -> 2560x1440 JPEG; base plates yuvj444p with explicit BT.601; 6 workers ~25 fps, 41,572 frames ~30 min.
- Tenglish word timing: forced-align the romanized SRT with torchaudio MMS_FA (torch/torchaudio 2.2.2 is last Intel-mac wheel). Resumable per cue, run with `nohup` (30 min background limit killed the first run). `words.js`: `w(q, near)` logs mismatched cue; `cw(i,q,k)` anchors to cue i for common words.
- Auto-fit wall captions to space left of x 1868; build scenes with root `display:block; visibility:hidden` so scrollWidth is real.
- Gotchas: upd-driven transform and GSAP x/y on same element fight (wrap one in the other); never store elements on a `.role` property; `maskUp` must start >= 140%; split layouts: clip inset in wrapper's local coordinates.
- Review loop: `review.py` (3 stills/scene, DPR 0.5, 12/sheet) -> read -> `pick.py` re-check. First pass found dead openings, captions off the right edge, black gap in splits, camera upd cancelling a slide, highlight scheduled after scene end.
- Audio: voice EQ/de-ess/2.5:1/expander -> -16 LUFS; 281 cues tiered against local voice, +18 ms after picture; 9-section bed switching on chapter hits; masters -14 LUFS / -1 dBTP with and without music.
- v2 correction: rhythm audit (wrap tl.fromTo/tl.to and lib helpers in export mode so every event lands in `window.__vis`, merge with scene cuts, list holds > 4.8 s; ep 1 went from 22 holds over 5.4 s to longest 5.2 s). Recipe: move frames -> `frames_v1`, masters -> `deliver/_v1/`, re-export, regenerate `subwin.json`, full render (~35 min) rather than patching 30+ ranges, rerun `audio.py sfx` + mix, then encode + QA.
- More gotchas: quote cycler in fixed-height overflow:hidden holder must offset in px; `.lbl` is nowrap (use whiteSpace normal for wrapped tags); check right edges inside camera-pushed wrappers at pushed scale; read new beats at DPR 1 crops.
- Green-screen brand card: `chromakey=0x00AE3E:0.10:0.06,despill` to RGBA PNGs via `c.media`; offset clip so click frame lands on spoken word; its audio goes in as chime-tier SFX cue.

## 6. RAG explainer kit (9:29.6, uncut, no BGM, 71 scenes)
- Gemini SRTs can't be trusted: drift up to +-15 s, 11 cues never spoken. Align the whole file once with `align_rag.py` (MMS_FA emissions in 24 s chunks + 3 s context, one global CTC alignment, star token between cues). Find unspoken cues with `emis_rag.py` (greedy-decode, similarity < 0.5 or score < 0.2 = suspect), drop and re-align.
- YouTube reference download (with his permission): Python 3.9 yt-dlp too old, use `uv python install 3.12`, venv with `yt-dlp[default]`, `--js-runtimes node`; `android_vr` returns 403; pull auto-captions (`--write-auto-subs --sub-format json3`). Tools in `06-tools/_video-analysis-tools/`.
- Components: `words()`, `hlType()`, `sideLabels()`, `card(world)` (light/canvas/char/night), `chapterCard()` with architecture rail, `itemCard()`, `mythCard()`, `splitPanel()`+`splitTH()` (black panel from right, footage slides -540 px), `chunkPage()`, `dbTable()`, `chatWindow()`+`chatStack()`, `node/link/curveArrow/tile/food` (drawn icons).
- Cards need content in first ~0.3 s: start chapter/question cards <= ~0.6 s before first word, extend previous scene. White text on his bright wall needs the light bottom fade.
- Numbers: 1,548 visual events, longest gap 4.66 s; full-screen 75% / face 25% (4 scenes moved to split panels); 316 SFX cues (33/min) tiered micro -24, tick -21, foley -18, chime -14, impact -9 dB; master -14 LUFS / -1 dBTP.

## 7. Day 03 kit — "How machines are trained" (12:57)
Graphics live in the room with him, not on slides (`motion-graphics-style` -> "In-the-room editorial system").
- Layers: `L_wall` (behind him, follows camera) -> `L_plant` (plate masked by static plant alpha) -> `L_person` (Vision matte, LA PNG on even frames) -> front. Per-scene ranges: `_person`, `_opaque`, `_slides`, `_fx`, `_grain`, `_noPlant`.
- Props mask: mic foam and shock mount are solid shapes, mic arm left out; coloured worlds fade to black under it.
- Camera: framing changes only on his ~80 jump cuts (wide <-> 1.075) plus 2.5% drift per shot; `camPunch(t,s)` snaps on a hero word and holds to next cut.
- Matte safety: `render.js` skips frames with missing matte (`__maskMissing`); re-run `--skipdone`. Export samples even frames only, so a scene starting on an odd frame needs matte f-1.
- Speed: drop swscale `accurate_rnd+full_chroma_int` (7x cost, 1.4 level difference); 5 chunks ~28 fps. ~1 fps per Chrome worker at 1440p under load. Split long ranges into parallel jobs with disjoint ranges. Kill Chrome children (`user-data-dir=...chrome_r<pid>_*`) with the renderer. Don't `pgrep -f` pattern inside own bash loop; wait on log line or PID.
- Segment encodes as chapters finish with identical x264 params (`-g 120 -keyint_min 120 -sc_threshold 0`), join with concat demuxer `-c copy`, mux audio last. AAC adds ~0.6 dB true peak: limit master at -2.2 dBFS to deliver -1.0 dBTP.
- "Make it fast" parallel authoring: lock the look; write `KIT.md` (brief, API, rules, SFX vocab, stills command); one IIFE scene file per chapter with `test_*.html`. Pages load scene files once: a render started before an agent's last edit is stale.

## 8. Sale-phones kit (client buying guide, 11:30.7)
- EDL with reorder: `keep.json` ordered kept SOURCE ranges; `edl.py` writes `edl.js`: `EDL_SRC` (output frame -> source frame), `EDL_CUTS`, `S(t)` (source -> output s). Author scenes in source time wrapped in `S()` so trims never break scenes. `audio.py` cuts voice through the same list on frame boundaries (800 samples/frame at 48k) with 6 ms fades.
- Timing audit: `clips_te.py` (Whisper large-v3 te, beam 5; ~10 s CPU per audio second; 10-14 s windows often noise, 3-6 s clean), `kw.py` (MMS keyword spot + level onset), `audit_match.py`.
- Render only ranges with final timing at `nice -n 19` (`render_range.sh`); 18 fps free, ~10 fps beside Whisper. Fix after render without re-rendering: mute an 80 ms stray syllable in `audio.py` instead of moving it.
- Proof captures: `grab_mark.js` returns the phrase's exact rectangles so the highlighter lands on the words (`K.hl` multi-line wipes). Encode CRF 17 preset faster, 2560x1440p60 -> 3.1 GB / 36 Mb/s (~24 min).

## 9. Day 06 kit — "Classification vs Regression" (16:37)
- Same engine; look locked on 8 style frames + 54 s sync clip, then chapters built one by one, each beat checked on stills (`stills.py ... test_<chapter>.html`). Helper agents per chapter produced nothing; building myself took ~3 h for 9.3 min of graphics. Keep KIT.md/EDIT_PLAN.md as checklist.
- Helpers: `K.pulse/glow/lite/ring/dim/gone/badge/strike`; `K.roll(...,{tight:true})`; `rawAt(cue,'/')` for symbol tokens (`cw(cue,'/')` silently returns first word).
- Canvas devices: wide canvas with camera pan between ideas (`CAM` 3840 wide + `K.ccam`); tree morphing into comparison headers; ghost "?" slots filling on the spoken word; "this process = X" typed into a cyan block; same-input comparisons; plant at 3:01 paid off at 13:48.
- Stills-first findings: diagrams too small (scale ~1.15x, margins >= 120 px); 1-5 s empty canvas after a cut (cut on the word that brings content, carry an object, or ghost slot); label rows > ~22 chars auto-shrink to ~34 px (split the row); counter/result collision; axis labels under moving tag.
- Telugu numbers: MMS aligner was right for 0/1/90/90%; Whisper te drifted 0.2-0.35 s early on digits. Trust the aligner when the envelope agrees (check at 20-30 ms).
- Ops: after restart resume with `--skipdone`, delete only stale frames; merge sub-frames per range only behind the render front; encode finished segments during render (~25% slower render, similar total); `rhythm.py` found two holds > 5 s.
- Numbers: 68 scenes, ~3,500 events, 488 SFX cues (19-40/min), face visible 44%, -14 LUFS, no BGM, no grade.

## 10. Video 13 render ops and add-on kit
- Absolute `--base/--masks/--out`; on restart `kill -9` the old node process and confirm with `ps` (stale run wrote black frames). Patches after a render starts need that range re-rendered. Mattes on even frames: odd start range needs previous even frame.
- Wall-word boxes: matte one frame per 2 s at 480x270, take head right edge -> box from head+40 px to x 1780, y 70-440 (above lamp); anchor punch-in right of head. Word-swap montages need 0.05 s exit with no blur.
- Add-on-top: `make_base_v2.py` grabs only on-footage ranges from the delivered master (`-ss (a-0.5)/60`, 709 tv -> 601 full JPEG); use camera identity (`camera_v2.js`) and `GRAIN_TH=0`; `engine_v2.js` adds `sc.gray(t)`. Render frames `ceil(t0*60)...ceil(t1*60)-1` (10,295 frames, 21 min, 6 workers); `--sub 3` only in fast windows; `merge_sub.py` averages in linear light (gamma 2.2).
- `final_encode.py` passthrough: master decoded to raw yuv420p, untouched frames straight to x264, v2 JPEGs -> RGB -> BT.709 TV 4:2:0 in numpy with 4 prefetch threads inside a 6 s window; crf 16 fast ~19 fps (~38 min / 43k frames). Check each rendered frame matches its own master frame best (PSNR ~45 dB at k=0 vs ~44 at +-1).
- **Tag the raw input** (`-color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709` before `-i -`); untagged rawvideo is treated as 601 and silently converted, frames 2.5 Y darker. Measure passthrough frames by exact index (`select=eq(n,N)`) before delivering.
- Audio v2: rebuild v1 SFX stem from v1 export (same seed), render `sfx_v2.wav`, mix sums voice + both stems.
- Hand label must finish writing >= 0.15 s before its scene ends; GSAP 3 has no `className` (use `attr:{class}`); never `tl.set` innerHTML (switch text in `c.upd`); upd-driven transform overwrites a GSAP pop on same node (wrap one in other); one ERR_FILE_NOT_FOUND per worker for a symbol-glyph font subset is harmless.

## 11. AI Tech News ep 02 kit (16:10, premium SaaS news show)
- Tenglish timing in minutes: large-v3 te on 16 min would take ~3 h on this Intel Mac. Instead `emis.py` (MMS_FA emissions for whole voice, ~16 min CPU, `mms_emis.npy` + greedy romanised heard stream), `heard.py t0 t1` (1 s ticks), `kw.py 'word|variant' t0 t1` (score >= -1 reliable, <= -3 check by eye; English loanwords and names spot cleanly). large-v3 translate (~14 min) gives meaning; onsets 0.1-0.5 s later than its word times. venv: torch==2.2.2 torchaudio==2.2.2 'numpy<2' on Python 3.9.
- Real sources instead of screenshots: `capture.js` re-captured 17 pages at 2x; `textbox.py img x0 y0 x1 y1 dark|light thr gap` returns headline line boxes for the marker (gap 0.14 big headlines); upscale his 800 px screenshots 2x (Lanczos + light unsharp); dark pages use screen blend 0.42.
- Engine: `sc_frame` (rounded footage card with shadow), `sc_split`, `sc_subscribe`, `K.mc` (match cut), `K.chapter`, `K.cap` right-anchored, `camera.js` alternates framing only on verified jump cuts (frame-difference ratio >= 8).
- QA caught: match-cut pull-out clipped at layer edge (hand-off card); `freezedetect n=-55dB d=4` on encoded master found 7 holds of 5.2-7 s the event audit missed (add word-timed micro-beats, re-render only those ranges, re-encode affected segments).
- Ops: 58,188 frames in 70 min (6 workers, ~14 fps with encodes alongside); 4 segments with closed 120-frame GOPs joined by concat -c copy; CRF 16 + grain ~71 Mb/s (8.6 GB), use CRF 18 when size matters. `python3 -I` hides user site; zsh doesn't word-split `$var` (use Python loops); foreground `sleep` blocked (use Monitor/`until` loops).
- v2 real-evidence pass (swap content, keep the edit): `K.photo`, `K.face/facify`, `K.ntag`, `K.footage`, `K.illus`; 20 scenes (273 s, 16,383 frames, ~18 min) rendered with `--ranges` into `work/frames`; export + cue diff (8 cues) -> `audio.py sfx` + mix; all 4 segments re-encoded. Stills at 28 beats before full render caught 5 layout issues (seal cut by crop, two source lines touching, chip covering evidence, cut-off quote, too-dark plate).


Full original notes (every detail, uncut): `_archive/original-full/youtube-long-video-editing.md` in this folder.
