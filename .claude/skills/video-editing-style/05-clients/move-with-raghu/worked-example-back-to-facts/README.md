# Worked example: "I'm back to facts" channel update (Move with Raghu, 49.85 s, 60 fps)

Telugu talking-head video, 4 clips joined, framed-window layout B, no BGM, no colour grade. Real sound recordings only. Delivered as `Back_To_Facts.mp4`, then v2 after two notes (varied comments, fuller sound). The rules he gave while we made it are in `../PROFILE.md` ("Owner's rules (2026-11-28)").

## What is in this folder
| File | What it does |
|---|---|
| `build.py` | key-word times `K`, scenes `S`, Tenglish caption words `W`, the 20 two-line phrase lockups `LK`; writes `hc/timeline.json` |
| `hc/stage.html`, `hc/engine.js` | the browser compositor: `renderAt(t)` is a pure function of time. `camAt()` drives both the picture punch-ins and the text placement; `drawLockups()` puts every phrase below the chin and fits it to a 1000 px column; scene components (switch, comments, stat cards, channel cards and arrow, poll, follow card) |
| `hc/render.js` | `node render.js stills OUT t1,t2,.. B v2` for preview frames; `node render.js video OUT [from to]` for the full frame sequence (JPEG, about 250 s for the whole video) |
| `hc/overlap_check.js` | scans every 0.1 s: no text box may overlap the face box (must print 0) |
| `audio.py` | 88 real-recording cues on his words and the picture moves; writes `proj/edl.json` for `shortkit.py audio` and the gate |
| `boards_v4.py`, `shotboards_v4.js` | the preview sheets sent for approval |
| `PLAN.md`, `caption_script_tenglish.txt` | the plan as first presented and the caption script. Typography was changed after he saw the first frames (his reference, then "never on my face", then "2 lines at most"): the final rules are in `../PROFILE.md` |
| `frames/` | final contact sheet, the approved v4 typography sheets, before/after of the two face and line-count changes |

## Order that worked
1. Join the 4 clips with the concat **filter**, each clip's audio trimmed to its own video length (concat-copy drifted).
2. Whisper large-v3 per clip (11-14 s each); re-decode bad spans in short windows without a prompt.
3. Face track: Haar cascade every 6 frames, interpolated and smoothed, written to `face_track.json` (cx, cy, face width in picture coordinates; not included, regenerate from the footage).
4. `build.py`, then stills with `render.js`, then `overlap_check.js` = 0, then boards, then wait for his approval.
5. Full render, `audio.py`, `shortkit.py audio`, SFX-bus EQ (high shelf 4.5 kHz +4, low shelf 90 Hz +4.5, low shelf 55 Hz +5), two-pass loudnorm to -14 LUFS / -1.5 dBTP, encode 60 fps with the bt709 tags, gate, earshot critique.

## Not included, and why
Footage and the master (his), the fonts (Montserrat, Great Vibes and Cormorant Garamond are free on Google Fonts: download them into `hc/fonts/`), his channel screenshots and avatars, the rendered frames and the MP4 (too large). The scripts have the scratch folder hard-coded at the top (`P = ...`): change it to your project folder.

## Numbers from the delivery
Gate: 1 FAIL (B-roll 0 %), reported on purpose: he asked for designed graphics instead of B-roll. earshot after v2: 85 % of metrics in range, sync 83 % (target 78 %), realness 0.99, sub-bass in range. Audio offset against the master 0.0 ms.
