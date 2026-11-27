# Motion graphics knowledge pack

What one study of prompt-motion.com produced: a skill, the data and the pictures behind it. Every one of the 242 videos on the site (Claude Opus 5.5 era, posted Sep 23 to Oct 21 2026) was fetched with its prompt, viewed as frame sheets and measured; the best 33 are written up with their original prompts. Reviewed 27 Nov 2026.

## Start here (for a new Claude Code chat)

1. Upload or unzip this folder in the project.
2. **Install the skill:** copy `skill-motion-graphics-craft/` to `.claude/skills/motion-graphics-craft/` in the project (or `~/.claude/skills/motion-graphics-craft/` for all projects). Claude then uses it whenever you ask to plan, prompt, build, render or critique a motion graphics video.
3. Without installing, tell the chat: "Read `skill-motion-graphics-craft/SKILL.md` first, then open only the reference you need."
4. Typical asks that work well: "Plan a 15-second launch film for X in profile M6 and write the structured prompt", "Review this render with the quality bar", "Show me the strongest examples of kinetic type and their prompts".

## What is in the pack

| Path | What it is |
|---|---|
| `skill-motion-graphics-craft/SKILL.md` | The method: workflow, rules, numbers |
| `skill-motion-graphics-craft/references/style-profiles.md` | Seven profiles (M1-M7) with exemplars and measured figures |
| `skill-motion-graphics-craft/references/techniques.md` | Build pipeline, transitions, type, camera, motion, looks, sound, loops, gotchas, bans |
| `skill-motion-graphics-craft/references/prompt-patterns.md` | The five prompt patterns, the structured template, a fill-in version |
| `skill-motion-graphics-craft/references/quality-bar.md` | Selection criteria, weaknesses seen, delivery checklist |
| `skill-motion-graphics-craft/references/picks.md` | The 33 picks with their original prompts, verbatim |
| `skill-motion-graphics-craft/scripts/` | `qc_render.py` (loop, pops, loudness) and `contact_sheet.py` |
| `data/entries-all-242.json` and `.csv` | Every entry: title, creator, tags, prompt (and English translation), model, stack, length, fps, size, audio, motion measurements, my grade and notes, profile, pick info |
| `data/profiles.json` | The seven profiles and their entries |
| `visual-reference/triage/` | 41 sheets, 8 frames for each of the 242 videos |
| `visual-reference/detail/` | 89 sheets for the shortlist: 18 frames plus a 6-frame burst at 70 ms steps |
| `visual-reference/INDEX.md` | Which sheet shows which entry |
| `tools/` | `fetch.sh` refetches the site and re-measures everything; the other scripts are its parts |

The source videos are not included (about 2.7 GB). Use `tools/fetch.sh OUT_DIR` to download them again.

## How it was made, and what it cannot tell you

- **Frames, not playback.** I judged look, type, transitions and pacing from sampled frames (8 per video for all 242; 18 plus a burst for the 89 shortlisted), plus numbers computed from the files. I did not watch the videos play, and **I could not hear any audio**. I only checked that an audio track exists and how loud it is.
- **No source code.** The site publishes the video and the prompt, not the code. Build recipes come from the creators' own prompts (the structured ones are detailed); I did not rebuild or run them.
- **Coverage.** 33 picked, 39 more examined closely, 18 shortlisted but not examined beyond the 8-frame triage, 152 seen only at triage. The status of every entry is in `data/entries-all-242.json` (`review_status`).
- **Grades are one reviewer's judgement** (A, A-, B+); they are not an objective ranking.
- **Measurements** (from `tools/metrics.py`): video sampled at 12 fps and 160x90 grey. `median_frame_diff` is the median change from one sample to the next (0-255), `static_share` the share of steps with almost no change, `spikes_per_10s` the count of sudden whole-frame jumps (hard cuts, flashes, flips) per 10 seconds. Rules of thumb, not film-grade analysis.
- **Prompts are verbatim.** They were extracted from the page and checked against its data; translations are the site's own. Five entries on the site are skills with no prompt.
- **Facts shown inside the videos (for example the astronomy figures) were not checked.**
- **Ownership.** Videos and prompts belong to their creators, who are credited with a link on every entry. The pack contains analysis, prompts and frame sheets for study, not the videos.

## How it relates to `video-editing-style`

`video-editing-style` is about vertical, voice-over-driven reels (editorial motion graphics, talking heads, 2.5D documentaries). This pack is about code-built, mostly 16:9, music-driven motion films (showreels, UI loops, launch films, concept pieces). They do not overlap much; transitions and sound rules in each can inform the other.

## Rerun or extend

```
tools/fetch.sh ./pm-run        # all 242 entries, about 2.7 GB of video; add a number to limit, e.g. tools/fetch.sh ./pm-run 5
```
Needs `curl`, `ffmpeg`/`ffprobe`, and Python 3 with `numpy` and `Pillow`. `fetch.sh` downloads the pages and videos and writes `data.json` (extraction, probing, motion measurements, prompt cross-check). Tested here on a 2-entry run, which reproduced the numbers in `data/`.

The other scripts in `tools/` are the ones I used to build this pack, kept for reference rather than as a turnkey pipeline: `strips.py` and `detail.py` made the frame sheets, `build_pack_data.py` and `build_picks_md.py` wrote `data/` and `picks.md` from my working files (`picks.json` is included; the grade tables are inside `build_pack_data.py`). Read them before reusing; they assume the folder layout `fetch.sh` creates.
