---
name: watch
description: Watch any video link (YouTube long-form, YouTube Shorts, Instagram Reels, TikTok) or local video file frame by frame, learn its editing style (cuts, zooms, transitions, word-by-word captions, SFX, music, pacing, hook) and save it as a reusable style skill inside this project. Use when the user says "watch", "learn this video", "learn this editing style", "copy this style", or pastes a video link to study.
---

> **Scope: tool. A newly learned style is saved as `04-styles/<slug>-edit-style/` in this layout.**

# Watch: learn an editing style from any video

Goal: take one video link, study it frame by frame (two frames at a time) plus its audio, and save the learned style as a new skill in this project so future videos can be edited in the same style.

Work from the project root (the main workspace folder). Never edit the original video. Learn the STYLE only. Do not reuse the creator's footage, voice, music or exact graphics.

## Step 0: Check tools

Make sure these exist. Install only what is missing.
- ffmpeg and ffprobe
- yt-dlp
- whisper (openai-whisper) for word-level timestamps
- Python packages: pillow, numpy

If something fails to install, fix it yourself before asking the user.

## Step 1: Run the extractor

Run the helper script that ships with this skill:

```
python3 .claude/06-tools/watch/scripts/extract.py "<VIDEO_LINK_OR_FILE>" --name "<style-name>"
```

Notes:
- If the user gave a style name, use it. Otherwise make a short slug from the video title.
- If the script is not at that path, search for `extract.py` inside any folder named `watch`.
- Output goes to `references/watch/<slug>/`:
  - `source.mp4` (the video)
  - `frames/` (sampled frames, scene cut frames included)
  - `pairs/` (two frames side by side with timestamps, in order)
  - `cuts.json` (every detected cut time)
  - `words.json` (every spoken word with start and end time)
  - `audio_profile.json` (loudness, silences, sudden hits that are probably SFX, music hints)
  - `summary.json` (shot length stats, cuts per minute, words per second, counts)
- For videos longer than 3 minutes the script samples thinly. Do a first pass, then re-run on interesting parts with `--start 0 --end 120` (seconds) to go denser. Always start with the first 60 seconds densely, because the hook decides the style.

Read `summary.json` first.

## Step 2: Frame pair pass

Open the images in `pairs/` using Read, about 10 at a time. Each image shows frame A and frame B with timestamps. For every pair, compare A to B and write a short note into `references/watch/<slug>/analysis/timeline.md`.

For each pair note:
- Time range
- Shot type: talking head, b-roll, screen recording, text card, graphic, product shot
- Framing and size: close, medium, wide, position of subject
- Change from A to B: hard cut, zoom in or out, punch-in, pan, whip, fade, glitch, shake, speed ramp, none
- On-screen text: exact words, position, font look (bold, thin, serif, sans), size, colors, outline or shadow, background box
- Overlays: emojis, stickers, arrows, icons, lower thirds, progress bars, logos
- Color look: warm, cool, contrast, saturation, filters, vignette, grain

Save progress to the file after every batch. Do not keep it all in memory. If the video is long, say clearly which time ranges were studied densely and which were sampled.

## Step 3: Captions, word by word

Using `words.json` and the caption frames, work out:
- How many words appear at a time (1, 2, 3, full line)
- Do words appear exactly at the spoken time, or slightly before or after
- Does the active word change color, scale or style
- Which words get emphasis (numbers, keywords, verbs) and how
- Casing (UPPER, Title, lower), punctuation shown or hidden, emojis near words
- Position on screen, safe margins, font, size, stroke, shadow, animation (pop, slide, fade, bounce)
- Typical words per second and the longest time a caption stays on screen

## Step 4: Audio, SFX and music

Using `audio_profile.json`, `cuts.json` and `words.json`:
- Voice: pace (words per second), pauses, whether silences are cut out (jump cuts), loudness feel
- Music: present or not, mood, energy, where it ducks under voice, drops or builds, how it starts and ends
- SFX map: line up each audio hit with the nearest cut, caption pop, zoom or transition. Name the likely type (whoosh, pop, click, riser, hit, swoosh, camera shutter, typing, glitch). Write how often they happen and at what moments (for example: a whoosh on every hard cut, a pop on every emphasized word)
- When unsure what a sound is, look at the frame at that timestamp and guess from what is on screen
- Write search keywords for each SFX type so they can be found later on Openverse or other free SFX sources

## Step 5: Hook and ending

Study the first 3 seconds and the last 5 seconds:
- What the viewer sees and hears in second 0 to 3
- How fast the first cut happens
- Any pattern interrupt (zoom, sound hit, text slam)
- How the video ends (CTA text, outro card, abrupt cut, loop)

## Step 6: Combine into numbers and rules

Turn all notes into clear, measurable rules. Prefer numbers over adjectives.
Example: "Average shot 1.8 seconds. Punch-in zoom 110 percent on every third cut. Captions 2 words at a time, yellow highlight on active word, bottom third. Whoosh SFX at 40 percent volume on every hard cut."

## Step 7: Save as a new style skill

1. Create `.claude/skills/style-<slug>/` in this project.
2. Fill `references/style-skill-template.md` (inside this watch skill) with the learned rules and save it as `.claude/skills/style-<slug>/GUIDE.md`. The frontmatter description must say when to use it, for example: "Use when editing a video in the <slug> style".
3. Copy these into `.claude/skills/style-<slug>/references/`: `timeline.md`, `words.json`, `audio_profile.json`, `cuts.json`, and 6 to 10 representative frames (hook, caption look, a zoom, a transition, an overlay, the ending).
4. Add one line under a "Learned styles" heading in the project `CLAUDE.md`: the style name and when to use it. Create the heading if it does not exist.
5. If an editor skill already exists in `.claude/skills/` (for example a folder with "editor" in its name), add one short line to it pointing to the new style skill. Do not rewrite that editor skill.

## Step 8: Tell the user

Reply short and simple:
- Style skill name and where it is saved
- 5 bullet recap of the style (pacing, captions, zooms, SFX, music)
- One example prompt, like: "Edit my raw video in the style-<slug> style"
- Anything you could not learn and why

## Rules

- Only analyze videos the user gives you. Learn style, never copy assets.
- If a download fails, try again once with a fresh yt-dlp update (`pip install -U yt-dlp`). If it still fails, ask the user to download the video and give the file path.
- Keep every written note concrete and measurable.
- If a style skill with the same name exists, ask before overwriting, or save as `style-<slug>-v2`.

---

## On this Mac (added by Claude, 2026-11-22; not part of the received skill)

Received as `watch-skill.zip` and unpacked here unchanged. Everything above is the skill as written; these lines map it to this workspace.

- **Run it with the wrapper:** `python3 "06-tools/watch/scripts/watch_mac.py" "<local video file>" --name <style-name>` (same arguments as `extract.py`, which is untouched). This Mac has no ffmpeg / ffprobe on PATH and no openai-whisper; the wrapper supplies the imageio ffmpeg, an ffprobe stand-in and faster-whisper from `~/.local/share/whisper-venv` (`WATCH_WHISPER_MODEL=small` by default). Tested 2026-11-22 on a 49.75 s reel: 110 frames, 55 pairs, 157 words, 24 sound hits.
- **Links:** `yt-dlp` is not installed, so a YouTube / Instagram / TikTok link cannot be downloaded here. Step 0 says "install only what is missing", but installing a downloader is a program download, so ask the user first (or ask for the file).
- **A link instead of a file (2026-11-25):** without yt-dlp, study the reel in the built-in browser with `06-tools/_video-analysis-tools/browser_reference_capture.js` (frame grids, cut count, likes and caption; view only, nothing downloaded). Steps in `06-tools/_video-analysis-tools/README.md`, section "Browser reference capture". Audio cannot be measured this way, so the sound section of the new style stays marked "not measured".
- **Where things go** (the workspace folder map wins over `.claude/skills/`):
  | The skill says | Here |
  |---|---|
  | `references/watch/<slug>/` | `edits/_watch-studies/<slug>/` (the wrapper's default `--out-root`) |
  | `.claude/skills/style-<slug>/GUIDE.md` | `04-styles/<slug>-edit-style/GUIDE.md`, filled from `references/style-skill-template.md` |
  | one line under "Learned styles" in CLAUDE.md | a line in CLAUDE.md Rule 1 + a row in `INDEX.md` + the next P number in `pro-video-editing/profiles/` |
  | "apply to the raw footage in `raw-videos/`", "render to `exports/`" | raws in the CapCut folders, finals in `edited videos by claude/` |
- **Cut detection misses soft transitions:** the default scene threshold 0.3 found 5 of about 12 layout changes in the test reel (slides and split-screen changes are not hard cuts). Re-run with `--scene-threshold 0.15`, or read layout changes from the frame pairs.
- **Token cost:** Step 2 opens every pair (55 pairs for 50 s is about 25k tokens). For the lean pass the user asked for, view one 1 fps overview sheet first, then only the pairs around each graphic, and write in the timeline which ranges were viewed densely.
- **Same job, older tool:** `pro-video-editing/tools/learnkit/learn_video.sh` adds OCR of all on-screen text and face framing. For a long video run learnkit as well; for a short, this skill is enough.
