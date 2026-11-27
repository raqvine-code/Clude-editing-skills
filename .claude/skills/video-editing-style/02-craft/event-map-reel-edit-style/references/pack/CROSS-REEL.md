# Cross-reel measurements

Produced with `skill-video-editing-style/scripts/reel_metrics.py` (R4 measured on its EDITED panel crop
`392:696:285:291`). wpm = words ÷ total runtime with pauses included; SFX = distinct events detected on the stereo
side channel (misses mono sub hits; not measurable on near-mono mixes).

| Reel | Length s | wpm | Hard cuts | Longest quiet stretch s | Frozen frames % | Median frame change | LUFS | True peak dBTP | Side/mid | SFX per 10 s |
|---|---|---|---|---|---|---|---|---|---|---|
| R0 editorial explainer | 29.9 | 163 | 7 | 1.30 | 0.4 | 2.2 | -14.2 | -0.2 | 0.13 | n/a (near-mono) |
| R1 talking-head tips | 34.0 | 224 | 10 | 0.40 | 2.4 | 1.8 | -14.1 | -0.8 | 0.11 | n/a (near-mono) |
| R2 faceless documentary | 40.9 | 150 | 7 | 0.13 | 0.5 | 5.8 | -14.9 | +1.3 | 0.59 | 5.4 |
| R3 faceless news mystery | 42.6 | 128 | 9 | 0.37 | 1.2 | 5.8 | -15.2 | +3.4 | 0.39 | 6.6 |
| R4 talking-head showcase (EDITED panel) | 35.6 | 204 | 8 | 0.93 | 0.2 | 3.1 | -14.7 | +2.9 | 0.32 | 9.5 |

## What the numbers say

- **Cadence is the constant.** Whatever the look, nothing stayed visually quiet for more than 1.30 s, and frozen
  frames stayed under 2.5 %.
- **Energy budget differs by format.** Talking heads change little frame to frame (1.8–3.1) and rely on captions and
  reframes; faceless stills move constantly (5.8) because a still that stops reads as a slideshow.
- **Speech rate differs by format.** Faceless storytelling ran 128–163 wpm with sentence gaps for the picture to
  breathe; talking heads ran 204–224 wpm.
- **Every reel got loudness roughly right and peaks wrong.** Integrated −14.1 to −15.2 LUFS, but all five peaked
  above −1 dBTP, three of them above 0 dBTP.
- **Turn position.** The "but…" turn landed at 60–76 % of runtime in all five (R0 61–74 %, R1 76 %, R2 62 %,
  R3 63–65 %, R4 73 %).

Correction note: an early event list double-counted SFX with several peaks (R4 "42 SFX / 11.8 per 10 s");
distinct events are ≈34 (9.5 per 10 s). The skill and the R4 notes carry the corrected figure.
