# R9: logo reveal, frame measurements

Source: one file the owner uploaded on 2026-11-27 (26.65 s, 720x748, 30 fps, 796 frames, stereo AAC). Study only; the frames are not stored here. Method: every frame read; "lit area" = pixels brighter than 40 of 255; "box" = bounding box of lit pixels; colours = median of lit pixels. Median frame-to-frame change 0.01 of 255 and no hard cuts: every change is a fade, wipe or glow.

## Picture timeline

| Time (s) | Event | Measurement |
|---|---|---|
| 0.00-0.07 | black | lit area 0 |
| 0.10-0.60 | badge uncovered from the top | box bottom moves from y 297 to y 379 in 0.5 s; top edge fixed at y 277 |
| 0.60-1.30 | badge brightens | mean grey 83 to 131 |
| 1.30-2.60 | hold | area 2909 px, constant |
| 2.67-3.00 | light sweep: glow orange at the top, travelling down, magenta at the bottom | lit area 2909 to 15683 px (5.4x) in 0.33 s; top glow about #AC8057, bottom about #A76CA6 |
| 3.00-3.80 | glow decays; the star stays magenta longest | area back to 3888 px by 3.80 s; neutral again by about 4.5 s |
| 4.5-7.2 | hold | - |
| 7.27-8.00 | badge wiped away toward its bottom-right corner | box left edge 306 to 367, top edge 277 to 339, over 0.7 s |
| 8.07-8.43 | black | 0.4 s |
| 8.47 | wide-tracked two-line caps appear in one frame, bright and soft | lit area 10016 px, frame brightness 2.56 |
| 8.47-9.2 | line sharpens and settles | brightness falls to 1.48 (ratio 1.7); area to about 5100 px |
| 9.2-13.2 | hold | 4.0 s |
| 13.2-13.57 | fade out | 0.37 s |
| 13.6-14.17 | black | 0.6 s |
| 14.2-16.1 | neon outline of the numeral drawn top to bottom | box bottom y 218 to 465 in 1.8 s (about 137 px/s, steady); left-facing edges pink, right-facing edges orange; soft outer glow |
| 15.7-16.6 | inside fills from the bottom, dark purple | lit area 23431 to 78044 px |
| 16.4-18.2 | fill brightens into the gradient, glow fades, mark shrinks | box 153-537 wide to 176-507 (384 to 331 px: scale 1.16 to 1.00; 1.13 used); mean colour rgb(61,22,58) to rgb(146,61,124) |
| 18.5-19.6 | three-line wordmark wiped on from the top-left, line by line | line 1 complete 18.9, line 2 19.2, line 3 19.5 |
| 19.6-22.7 | hold | 3.1 s |
| 22.77-23.10 | diagonal wipe out, top-left first | box left edge 176 to 452 in 0.3 s |
| 23.1-26.65 | black | 3.5 s |

Final gradient of the numeral, top to bottom (median per eighth of the height): #544998, #7B3B9E, #AC33A3, #C43D91, #C5537E, #C55E60, #C6694A, #C36D49. Wordmark face #BDBAC3, outline #1E0624.

## Sound timeline (earshot `timeline`; tags are model guesses, times and levels are measured)

| Time (s) | What | Level |
|---|---|---|
| 0.00-4.65 | orchestral bed, stabs at 0.03, 1.74, 4.20 | -19 LUFS |
| 4.65-14.70 | the same bed, louder; loudest 11.5-14.5 s | -12 LUFS (short-term peak -9.1) |
| 14.70 | change to single electric-guitar notes | -17 LUFS |
| 17.5-18.0, 19.5 | near silence | RMS -30 to -38 dB |
| 18.23, 18.53, 19.58, 20.47, 21.83, 22.81, 23.48, 25.61 | notes, 13-25 dB over the bed | peaks about -6 dBFS |

Integrated -14.2 LUFS, range 7.9 LU, true peak +0.4 dBTP. Band shares: sub -25 dB, low -5, low-mid -5, mid -5, presence -14, air -24. The low band falls from about -20 to -43 dB at 14.7 s: the bass leaves when the numeral arrives.

## Poster measurements

- **Poster A** (2160x2700): dominant colours #060101 (57 % of the area), #420303 (12 %), #942315 (11 %), white type 4 %. Title about 67 % of the width, two lines, centred at about 45 % of the height. Pill label about 23 % of the width. Body copy three lines at 88-92 % of the height.
- **Poster B** (2160x2700): sky #2F3D9E (top) to #866EE5 (middle) to #FCCAED (low), horizon #F65C89. Title outline #31072C; shape stroke #FEB423; arrow #9EFE3C; tag #FA3BB1. Title three lines, about 62 % of the width, top third of the frame; subject fills the lower 55 %.
