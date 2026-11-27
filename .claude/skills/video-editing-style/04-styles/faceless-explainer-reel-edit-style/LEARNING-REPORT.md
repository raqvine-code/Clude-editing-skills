# Learning report: faceless explainer reel edit style

## 2026-11-21 - first study ("zip 1 .zip" from Downloads)
- **Source:** an analysis pack, not a video. It held a ready skill file, five 3 fps contact sheets (the whole reel), 13 frame-numbered sheets of key moments, 3 full-size stills, a word-timed transcript, scene-change scores and audio band data for one 29.9 s finance reel (720x1280, 30 fps, 896 frames).
- **Method:** every sheet and still was viewed; every text file was read; the pack's claims were checked against its own frame numbers and transcript. refscan and learnkit were not run (no video file).
- **Written:** `GUIDE.md` (this folder), 5 transitions (X15-X19), 2 type techniques (T15-T16) and 5 motion elements (M13-M17) in the `pro-video-editing` libraries, rows in the shorts style picker and cheat sheet, and a training-batch entry in `shorts-editing-pro/LEARNING-LOG.md`.

### Corrections to the pack (from its own frames)
| Pack says | Frames show |
|---|---|
| Each word reveals on its spoken onset, within 3 f | Hook words follow the voice within about 5 f. Dark-scene words step at an even 4 f and can run up to 0.35 s ahead. After a flash the first word is 6-10 f late |
| Cuts land 0-2 f before the next sentence | True for most; the punchline cut lands about 10 f after its sentence starts |
| About 160 wpm | About 179 wpm overall (88 spoken words in 29.5 s) |
| Headline at 8-10% of height | That is y 150-190 of 1920, inside our unsafe top band; we use y 230 or lower |
| Reference peak -0.2 dBTP | Not copied; our master is -1 dBTP or lower |

### Not verified
- Nothing has been rendered in this style. `shortkit.py` has no blur-in reveal, two-font line, stat wedge or light leak yet.
- Font names, px sizes and blur radii are estimates from 720p frames.
- Sound findings come from spectra and onsets; nobody listened to the reel.
- The transcript is ASR (faster-whisper base.en) and can be 0.1-0.3 s off, so the reveal-timing numbers carry that error.
- The reference's own facts and figures were not checked.

### Next
The first edit that uses this style logs what worked in `shorts-editing-pro/LEARNING-LOG.md` and updates section 12 ("Kit status") of `GUIDE.md`.
