# Learning report: aasil-khan-longform-edit-style

## 2026-11-21: first reference video
| Source | Coverage |
|---|---|
| "I Made 8.85 Lakh From Content in One Month. Copy Me", first 707 s of the video, 1920x1080, 29.97 fps. Stored at `/Users/raghusai/Desktop/training claude/training videos/asil-khan-longform/` | Every shot viewed once (227 mid-shot frames). 18 frame-by-frame strips at 2-30 fps. 18 full-quality stills. Face box at 5 fps. Per-frame brightness and colour for all 21,189 frames. Loudness, stereo side-channel and level-floor analysis. Word-level transcript (2,492 words). All on-screen text read by OCR at 5 fps (3,535 frames) plus a 27-frame caption sample for exact sizes. Studied with `pro-video-editing/tools/learnkit`. |

### Confidence
| Area | Level | Why |
|---|---|---|
| Cut rhythm, shot mix, runtime per world | Measured | Cut detection + face tracking over the whole file |
| Framing, punch-in ratio, speaker shift | Measured | Face box, 2,361 frames |
| Flash transition (count, length, colour) | Measured | Brightness spikes over every frame + one 30 fps strip |
| Recurring devices and their timings | Measured | 18 strips cover each device at least once |
| Colours | Measured, ±5% | Sampled from compressed frames |
| Loudness and music placement | Measured | R128 on the original; music after 2:00 is "faint or absent" (a mono bed would not show in the side channel) |
| Sound-effect placement | Weak | Stereo bursts only; types not identified |
| Speech rate, pauses, script order | Measured | Word-level transcript of the whole file |
| Caption sizes and positions | Measured on a sample | OCR on 27 caption frames |
| Text coverage (39% of words on screen), text-to-voice timing | Measured | Full OCR pass matched against the transcript |
| Fonts | Observed | Matches by eye |
| Ending, outro, end screen | Not seen | The file stops at 11:47, mid-section |

### Not done / weak
- One video only: the creator's constants are not yet separated from this video's choices. A second video would settle which devices are habits (flash cuts, white + navy worlds, staircase) and which belong to this topic.
- The ending was not supplied.
- Nothing in this skill has been tested by producing an edit yet. The typed-notes staircase, the recap chart and the light-leak flash still need to be built once as templates.

### To raise confidence
1. Supply one or two more long videos from the same creator, complete to the end.
2. Build a 60 s test edit on the user's own footage and compare side by side with the reference.
