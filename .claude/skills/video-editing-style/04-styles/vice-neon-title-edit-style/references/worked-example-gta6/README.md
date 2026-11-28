# Worked example: "GTA 6 · why it took 13 years" (owner's own channel, Telugu, 57.7 s)

> Frames removed on 2026-11-28 to save storage (owner's request). Only `final_key_moments.jpg` is kept; other image names below are no longer in the repo. Everything else here is the working code and numbers.

The first edit built with P21. The plan and storyboard were approved before any render. The owner chose **layout B** (his 4:5 picture in a framed window between two neon lines) and **Tenglish captions**.

## Files

| File | What it does |
|---|---|
| `build.py` | Key-word times snapped to the audio, and 20 scene windows. Writes `hc/timeline.json`. |
| `tenglish.py`, `captions.py` | The Tenglish script, one entry per Whisper token, split into caption lines. GTA stays glued to its number and 13 to "years". |
| `hc/stage.html`, `hc/engine.js` | Browser compositor: P21 tokens, 21 scenes, layout B frame, caption band, scene-start zoom-blur punch. |
| `hc/render.js` | `node render.js stills OUT t1,t2,... [A\|B] [none\|te\|tg]` or `node render.js video OUT [from to]` (60 fps JPEG frames). |
| `frames.py` | Speaker frames: 1080x1368 crops of the picture window. **Read sequentially**: seeking every frame is about 50 times slower. |
| `audio.py` | 88 real-recording cues on key words and moves, then the EDL for `shortkit.py audio` and the gate, plus credits. |
| `boards.py` | Numbered storyboard boards (6 panels per board: frame, words, visual, sound). |
| `PLAN.md` | The plan the owner approved. |
| `storyboard_*.jpg` | What the owner saw before the render. |

**Not stored here** (licences or size):
- The fonts: run `../../tools/fetch_fonts.sh`.
- Rockstar's media zips: download from rockstargames.com/VI/media.
- The footage and the rendered frames.

## Pipeline (as run)

1. **Join the clips.**
   - The six CapCut clips were joined with the concat *filter*, each clip's audio trimmed to its own video length.
   - `-f concat -c copy` drifted the voice 0.27 s late by clip 6 (AAC priming).
2. **Transcribe.**
   - Whisper large-v3 transcribed **each clip separately** (11 s or less).
   - On the whole 58 s Telugu file it looped and repeated one sentence.
   - Unclear spots were re-run with a vocabulary prompt.
   - One meaning-critical word ("pattaledu" = didn't take) was checked on three different crops.
3. **Research and B-roll.**
   - YouTube refused downloads from the cloud server ("confirm you're not a bot"); this was not bypassed.
   - Rockstar's official media page gave zips "to download and share": 9 clips, 138 4K screenshots and 28 artworks, phone versions included.
   - Evidence cards: Playwright screenshots clipped to each `h1` or key paragraph at 2x DPR.
4. **Plan, storyboard, approval** (CLAUDE.md Rule 0 step 3).
5. **Captions and layout.**
   - Captions sit in a Shorts-safe band, centred at y 1500.
   - Every scene keeps y 1440-1560 clear.
   - Nothing important sits at the right edge (x > 940, y 1000-1700, under the like and share buttons) or below y 1600.
6. **Sound and gate.**
   - `audio.py`, then `shortkit.py audio`.
   - EQ on the SFX bus, then loudnorm to −14 LUFS / −1.5 dBTP. The source was −6.3 LUFS with peaks above 0 dB.
   - Gate: one FAIL left on purpose. Font families are 3 (Pricedown, Noto Serif Display, Inter Tight): the P21 look the owner asked for and approved on the storyboard.
7. **Render, encode, QC, deliver.**
