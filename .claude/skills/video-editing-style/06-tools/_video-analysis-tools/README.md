# Video analysis tools

Python helpers for reference-video analysis (copied unchanged). Run with `python -I`. Most need numpy, soundfile, scipy or PIL; ffmpeg path comes from the `FF` env var or an argument. Scripts that hardcode an old ffmpeg path (`refsheet.py`, `strip.py`, `vidsheet.py`, `sfx_analysis.py`) need that constant edited.

- `track.py`: tracks one shape per frame at 60 fps (modes light/dark/nonwhite/green/bluepx/sat/luma; metrics w/h/cx/cy/area/x0/x1/y0/y1) and classifies easing: duration, t10/t50/t90 vs templates, overshoot. `FF=... track.py video t0 t1 mode metric [thr]`.
- `motion_curve.py`: 60 fps frame-difference, luma and saturation per second, biggest jumps (hard cuts). `motion_curve.py <ffmpeg> <video>`.
- `gsheet.py`: aspect-agnostic (16:9, 1:1, 9:16) contact sheets with time labels. `FF=... gsheet.py video t0 t1 fps cols tile_w outprefix [rows]`.
- `strip.py`: frame-accurate labelled strip, 8 per row. `strip.py video t0 t1 fps out.jpg [tile_w]`.
- `vidsheet.py`: overview sheets (1 frame per step, 6x5 tiles) with SRT text under each frame. `vidsheet.py video srt outdir [step] [t0] [t1]`.
- `refsheet.py`: same overview sheets but labelled with words from YouTube json3 auto-captions. `refsheet.py ref.mp4 captions.json3 outdir [step] [t0] [t1]`.
- `band_onsets.py`: for a mono WAV, loudness, energy share per band (sub/low/mid/hi/air), per-band onset times, 1 s RMS profile.
- `spectrogram_log.py`: log-frequency spectrogram PNG with second ticks, plus low-band tempo guess and onset list. `spectrogram_log.py <wav> <out.png>`.
- `specpanel.py`: spectrogram panels of the accompaniment stem around given event times with a red line at the picture event. `specpanel.py no_vocals.wav out.jpg "t1:label,..." [pre] [post]`.
- `sfx_analysis.py`: SFX/music forensics from Demucs stems plus a visual-event cut list: music-bed presence, voice-vs-bed level, classified onsets with nearest visual event, written to JSON. `sfx_analysis.py video stems_dir cuts.txt out_prefix`.

## Browser reference capture (added 2026-11-25)
`browser_reference_capture.js` studies Instagram reels and YouTube Shorts **without downloading them**. It was used for the 11 mustard-red references and the 11 P16 Instagram reels. It runs in the built-in browser pane, view only: no likes, follows, comments or saves, and nothing captured goes into a delivered edit (CLAUDE.md Rule 1.6).
1. Open a search: `https://www.instagram.com/explore/search/keyword/?q=<words>` (signed in already; never sign out). Paste the file with `javascript_tool`, then `await RC.search()` lists post codes. With the pane hidden only about 3 results load, so run several short queries.
2. `await RC.post(code)` reads account, likes, comments, date and caption from the post's `og:description` (the `/api/v1/` search endpoints return 404).
3. Open `https://www.instagram.com/reel/<code>/` (it redirects to `/reels/`; the first `<video>` is that reel, a 1080x1920 MSE blob that can be drawn to a canvas). Re-paste the file after every navigation.
4. `await RC.grid(RC.every(0, 30, 1))` draws a 216x384 tile grid with time labels and caption-band guides; `resize_window` 1320x830, one screenshot, then `RC.clear()` and `resize_window` preset `desktop`. A split-screen reel takes `{crop: [sx, sy, sw, sh]}`.
5. `await RC.cuts(0, 30)` counts hard cuts from frame differences at 4 fps (threshold 38): cuts per second and average shot length, the numbers in `aesthetic-pro-reel-edit-style` section 1.
6. YouTube Shorts: the same on `https://www.youtube.com/shorts/<id>`, or a quick look without a page at `https://i.ytimg.com/vi/<id>/hq1.jpg` / `hq2` / `hq3` (frames at 25 / 50 / 75 %).
7. **Measuring how text arrives** (used on the "Grind szn" reel, 2026-11-25):
   - Grid 12-16 frames at 1/30 s steps over one word's entry, cropped to the text: `RC.grid(RC.every(3.55, 4.10, 0.0334), {w: 320, h: 180, cols: 4, crop: [sx, sy, sw, sh]})`.
   - Count the frames from dim/soft to full white and sharp: a fade of about 5 frames, a blur reveal of about 7 frames.
   - A **landscape** reel needs `{w: 320, h: 180}` (or 640x360) tiles. Check `videoWidth` / `videoHeight`, and pick the `<video>` whose rectangle is on screen; it is usually index 0.
   - For a short reel, run `RC.cuts` at `{fps: 8, thr: 30}` to catch sub-0.5 s shots.
8. **Lessons from 2026-11-25:**
   - **Use `https://www.instagram.com/p/<code>/`** when the browser pane is hidden: `/reels/<code>/` then shows no video, but `/p/` loads it.
   - **Re-paste the file after every navigation.**
   - **Keep the grid inside the viewport** (rows x tile height ≤ 830 at 1320x830). A taller grid is scaled down. Resize the window again if the screenshot size changes.
   - **The `computer` zoom region is in screenshot pixels, not page pixels.** For detail, draw a bigger cropped tile (`{w: 640, h: 320, crop: [...]}`) instead.
   - **"$5 vs $80 edit" comparison reels stack several versions in one post.** Find each tier on an overview grid, then crop only the pro tier.
   - **To catch a letter-by-letter type-on, grid 1/30 s steps across the spoken word.** Count letters per frame (8 letters in 0.37 s on shami.mp4).
   - **Faceless reels: run `RC.cuts` at `{fps: 10, thr: 30}`.** It found 22 cuts in 9.3 s on yp.motionstudio.
9. Write what was measured into the style's `references/` (table: id, account, likes, cut rate, caption fonts and colours, inserts), then into the skill. A video file the user gives goes to `watch` instead.
