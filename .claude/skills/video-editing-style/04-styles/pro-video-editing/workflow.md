# Professional Editing Workflow (raw footage -> export)

## 0. Brief (ask only what you cannot infer)
Objective (sell, teach, showcase, hire), audience, platform + aspect (9:16 / 16:9 / both), length, profile (P1-P5) or "pick for me", brand colour, CTA. Pick a profile with `GUIDE.md` "Choosing a profile".

## 1. Ingest and measure the raw footage
- `ffmpeg -i` for size/fps/duration; loudness (ebur128); transcript with word times (`~/.local/share/whisper-venv/bin/python` + faster-whisper, model base or small).
- Note usable takes, silences, energy peaks. Do not change original files; work on copies.

## 2. Story cut
- Hook first 1-2 s (P1: statement; P5: shrink-to-card + promise; P2: name + title).
- Remove dead air; keep speech 150-210 wpm feel. One idea per beat.

## 3. Shot-by-shot plan (write it before building)
Table: `t_in | t_out | spoken words | on-screen text (tier) | graphic/element | transition in | SFX`. Mark the keyword for each sentence, and the 1-3 behind-subject words for the whole video.

## 4. Build
- Background plates / mattes (person cut-out if behind-subject text is used): `~/.local/share/whisper-venv/bin/python tools/matte.py clip.mp4 mask_dir [t0] [t1]` -> PNG luma-matte sequence (MediaPipe selfie segmentation, EMA-smoothed). Tested 2026-11-15: works, but edges are slightly blocky on hair -> check edges at 100 % in QC; tighten with a 1-2 px choke or hand-fix key frames.
- Also apply the account's other editing skills where relevant: `my-editing-rules` (standing rules), `reel-editing-method` (9:16), `client-video-editing-process`, `sound-and-music-design`, `fonts-and-colours`, `broll-library` / `png-library` / `where-to-find-assets`, `mistakes-to-avoid`.
- Type system from the profile: fonts, sizes relative to frame width, colours.
- Animate with library recipes (frame counts given). Keep to 1 accent colour.
- Tools available here: ffmpeg + Python/PIL frame rendering (proven), HyperFrames (installed, untested here), user's NLE/After Effects for final if preferred. Give AE/Premiere/CapCut steps when the user edits manually.

## 5. Sound
Music choice by energy, SFX on entries/whips/pops, voice -14 LUFS master, -1 dBTP, duck music 8-12 dB under speech.

## 6. Review (see qc.md), render sample 10-15 s first, then full.

## 7. Deliver
H.264 high, 1080x1920 or 1920x1080, 30 fps (match source), AAC 48 kHz 192 kb/s+. Report what was rendered and verified; never claim a render that was not checked.

## Proven build path (16. Uncertainty Short, 2026-11-16)
1. `tools/analyze_raw.py` -> facts, sheets, transcript, draft PLAN.md. 2. Plan with readers + planners + judges + reviewer; reviewer measures onsets on the audio. 3. Write ONE frame map (`analysis/framemap_*.json`) and verify it against the plan's output times before any track starts. 4. Run parallel tracks with separate owned folders: plates (base frames in output order, Vision `matte` tool from `pending videos/aimldl_reels/build/tools/matte`, mask grade bake), audio (`make_audio.sh`, sample-exact voice cut, measured SFX transients), B-roll (`prep_broll.sh`, contact sheet before every in-point), words (`make_words.py`, landmark-adjudicated onsets). 5. Scenes on the Mr Unbox kit (`components_1115.js` has capRow / wallWord / brollSeq / worldScene / paperCard / pauseBW). 6. `check_page.js` stills (watch the [mg] SHORT / mismatch logs), sample render, full `render_all.sh`, contact sheets of the encoded MP4.
Code for reuse: `edited videos by claude/16. Uncertainty Short/code/`.
