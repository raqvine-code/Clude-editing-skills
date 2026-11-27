# Export and QC

## Export spec
- **Video:** 1080x1920, constant source frame rate (60 or 30; never VFR).
  - H.264 High, `-preset slow -crf 16-18`, yuv420p.
  - BT.709 tagged, tv range: `-colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv`.
  - Convert full-range RGB frames with `scale=out_color_matrix=bt709:out_range=tv`.
- **Audio:** AAC 320k, 48 kHz stereo. `-movflags +faststart`.
- **Upload copy** (optional): `-crf 20 -maxrate 16M -bufsize 32M`. Platforms re-encode; more than about 12 Mbps gains little (ONL).
- **Length:** Shorts up to 3 min (square or taller); Reels are pushed best under 90 s to 3 min. Keep 15-45 s unless the story needs more.
- **Cover:** frame 0 must work as a thumbnail. Keep the subject centred for the 3:4 grid crop (1080x1440) and the 4:5 feed crop.

## Safe zones (1080x1920, union of platforms, ONL)
**Superseded 2026-11-25** by `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`: text inside x 120-960, y 270-1470; subtitle block centre at 58-65 % of the height, under the chin. The numbers below are kept for history.

| Edge | Keep text and key graphics out of |
|---|---|
| Top | 0-210 px (status bar, tabs) |
| Bottom | 1500-1920 px (caption, username, audio bar, which grew about 50 px in late 2025) |
| Right | 960-1080 px between y 1000 and 1750 (like / comment / share column) |
| Left | 0-60 px |

Captions sit at y about 1150-1300; nothing smaller than 24 px.

## QC commands (ffmpeg `FF` from the kit: `/Users/raghusai/Downloads/claude/pending videos/aimldl_reels/bin/ffmpeg`)
- **Frames:** `FF -i out.mp4 -map 0:v -f null - 2>&1 | grep frame=`
- **Black:** `-vf blackdetect=d=0.01:pix_th=0.06`. **Freeze:** `-vf freezedetect=n=0.003:d=0.5`.
- **Loudness:** `-af ebur128=peak=true -f null -` (I, LRA, true peak).
- **Contact sheet** every 0.5 s: `-vf fps=2,scale=216:-1,tile=8x5`. View it small.
- **Sync strip:** 6 frames around 5 random caption words. The caption must appear on the onset frame ±1.
- **Loop seam:** mean luma of the last frame vs frame 0.

## Senior-editor eye pass
- **Hook:** moves by frame 3, and the promise is clear in 1.5 s.
- **Pace:** nothing static over 2.5 s; one element at a time; every effect has a job.
- **Captions:** in the safe zone, never on the mouth, at most 3 words.
- **Look:** one accent; the face bright and natural.
- **Ending:** ends on the payoff; loops.
- Then list the three weakest moments and either fix them or note them.

## Event-map scorecard (added 2026-11-22)
`python3 02-craft/event-map-reel-edit-style/tools/score_reel.py <render.mp4> --words <word count>` checks frozen frames, the longest visually quiet stretch (1.3 s or less), loudness, true peak, sound on cuts and wpm against five measured reference reels. Each LOOK line gets a fix or a written reason in the QC notes. How to read it: `02-craft/event-map-reel-edit-style/GUIDE.md` section 11.
