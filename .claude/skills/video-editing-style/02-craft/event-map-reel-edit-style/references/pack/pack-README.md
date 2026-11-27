# video-editing-style: skill + full analysis of 5 reference reels

Everything learned in this project: an editing methodology reverse-engineered frame by frame from five vertical
reels, packaged as a Claude skill, plus the evidence behind it. The source videos themselves are not included.

## Start here

1. **`skill-video-editing-style/GUIDE.md`**: the method (three laws, format chooser, event-map workflow, story
   spine, hook and sync rules, text systems, camera, transitions, sound, colour, QC checklist).
2. **`CROSS-REEL.md`**: the five reels side by side in measured numbers.
3. **`analysis/<reel>/NOTES.md`**: the full frame-by-frame notes for one reel.

## Install the skill

Copy `skill-video-editing-style/` to `.claude/skills/video-editing-style/` in a project, or to
`~/.claude/skills/video-editing-style/` for all projects. Claude then uses it for planning, editing, captioning,
sound-designing or reviewing reels, and for analysing reference videos.

## Contents

| Path | What it is |
|---|---|
| `skill-video-editing-style/GUIDE.md` | The core method |
| `skill-video-editing-style/references/format-a…`, `format-b…`, `format-c…` | One file per format: editorial motion graphics (version-1 analysis, intact), talking head + before/after showcase, faceless 2.5D documentary |
| `skill-video-editing-style/references/transitions.md`, `devices.md` | Transition and device recipes with frame counts |
| `skill-video-editing-style/references/reels/` | The four new reels' notes, as bundled with the skill |
| `skill-video-editing-style/scripts/reel_metrics.py` | Scorecard: checks any render against the reference ranges (cuts, quiet stretches, frozen frames, loudness, true peak, SFX, wpm) |
| `skill-video-editing-style/scripts/frame_sheets.sh` | Frame-numbered contact sheets for frame-by-frame review |
| `CROSS-REEL.md` | Measured comparison table and what it shows |
| `analysis/R0…R4/NOTES.md` | Per-reel notes: beat sheet, hook, typography, motion, transitions, devices, colour, sound, retention, weaknesses, steal list |
| `analysis/R*/contact_sheets/` | Whole-reel timelines (3 fps sheets and a 1 fps overview) |
| `analysis/R*/evidence_sheets/` | Frame-numbered sheets of each transition and animation (label = source frame at 30 fps) |
| `analysis/R*/stills/` | Full-resolution stills and crops |
| `analysis/R*/data/` | Word-timed transcripts, cut lists, audio band and onset analysis, stereo SFX events, loudness, scorecards, measurement outputs (camera moves, colours, caption timing) |
| `analysis/R*/scripts/` | The measurement scripts written for that reel |
| `tools/` | The shared analysis pipeline: `prep.sh` (sheets, frames, audio), `vmetrics.py`, `ametrics.py`, `transcribe.py`, `side_events.py`, `cross.py`, `sheet.sh`, `still.sh` |

The reels: R0 finance explainer (editorial motion graphics), R1 "remember your script" tips (talking head), R2
Semmelweis story (faceless documentary), R3 Russian scientist mystery (faceless news mystery), R4 realtor/AI reel
inside a RAW vs EDITED showcase.

## How it was verified

- Skill structure passes the official skill validator; every file it references exists.
- An independent fact-check compared every number in the skill with these notes and data: 13 wrong, misattributed
  or unsourced figures were found and corrected (plus rounding).
- A test editor planned a reel using only the skill: the 7 gaps it reported (word budget, turn timing, hook text,
  colour rules, missing default frame counts, word timing, follow CTA) were filled.
- Both scripts were run on fresh files at 720p and 1080p.

## Caveats

- Sound findings come from measurement (spectra, stereo separation, onset detection), not listening.
- Font names are visual guesses; ≈ marks values read off sheets rather than measured.
- Images in `analysis/` were downscaled to ≤ 1800 px wide and recompressed to keep the zip small.
- Some analyst scripts reference the working folder layout they ran in (`src/reel.mp4`, `fr/`, `d/`); point them at
  your own copy of a video to rerun.
