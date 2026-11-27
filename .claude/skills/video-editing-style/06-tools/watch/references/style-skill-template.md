---
name: style-<slug>
description: Use when editing a video in the "<slug>" style. Applies the pacing, zooms, transitions, word by word captions, SFX and music rules learned from <source title or link>.
---

# Style: <slug>

Learned from: <video link or title>
Studied range: <start to end seconds>
Format: <vertical 9:16 or horizontal 16:9>, <fps>

Use this skill when the user says "edit in <slug> style" or asks for this look. Apply the rules below to the raw footage in `raw-videos/`. Copy the STYLE only. Never reuse the original creator's footage, voice or music.

## 1. Quick recap (5 lines)
- Pacing:
- Captions:
- Zooms and motion:
- SFX:
- Music:

## 2. Pacing and cuts
- Average shot length (seconds):
- Cuts per minute:
- Silences: cut out or kept (and how long a pause is allowed):
- Jump cut pattern:
- Hook speed (first cut at what second):

## 3. Framing and movement
- Main framing (close, medium, wide) and subject position:
- Punch-in zoom: how much, how often, on what kind of moments:
- Slow zoom or pan on long shots:
- Shake, whip, speed ramp:

## 4. Transitions
- Types used, in order of frequency:
- Duration of each type:
- Where they are used (topic change, emphasis, only at hard cuts):

## 5. Captions (word by word)
- Words shown at a time:
- Timing: on the spoken word, a little before, or a little after:
- Active word style (color, scale, background):
- Emphasis rules (which words get highlighted and how):
- Casing and punctuation:
- Font look (weight, family type, size relative to screen):
- Stroke, shadow, background box:
- Position and safe margins:
- Entry animation (pop, slide, fade, bounce) and exit:
- Emojis or icons near words:

## 6. Overlays and graphics
- Text cards, lower thirds, arrows, stickers, progress bars, logos:
- Color palette (hex values if seen):
- Screen recording treatment (border, shadow, zoom):

## 7. Color and look
- Grade (warm or cool, contrast, saturation):
- Filters, grain, vignette, glow:

## 8. Audio
- Voice: loudness feel, pace (words per second), processing (compression, EQ, noise):
- Music: mood, energy, volume under voice (in dB or percent), ducking, drops, start and end:
- SFX map (type, trigger moment, volume, how often):
  - Whoosh:
  - Pop:
  - Click or typing:
  - Riser or hit:
  - Other:
- SFX search keywords for Openverse or other free sources:

## 9. Hook (first 3 seconds)
- What the viewer sees:
- What the viewer hears:
- Pattern interrupt used:

## 10. Ending
- Last 5 seconds (CTA text, outro card, abrupt cut, loop):

## 11. Step by step recipe for a new video
1. Transcribe the raw video word by word with Whisper.
2. Remove silences and mistakes using the pacing rules above.
3. Add captions using section 5.
4. Add zooms and transitions using sections 3 and 4.
5. Add SFX and music using section 8.
6. Add overlays using section 6.
7. Render to `exports/` in the right size and check the first 3 seconds against section 9.

## 12. Do not
- (list anything the original style clearly avoids)

## References in this skill
- `references/timeline.md` frame by frame notes
- `references/words.json` word timings of the source video
- `references/audio_profile.json` loudness, silences, SFX hits
- `references/cuts.json` cut times
- `references/frames/` key example frames
