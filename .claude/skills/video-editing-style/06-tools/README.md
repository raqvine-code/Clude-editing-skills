# 06-tools: learn, rebuild, save

| Need | Use |
|---|---|
| Learn a style from a video FILE (frame pairs, words, sound hits); saves `04-styles/<slug>-edit-style/` | `watch/` (`scripts/watch_mac.py`) |
| Study an Instagram or YouTube LINK without downloading it (frame grids, cut count) | `_video-analysis-tools/browser_reference_capture.js` (steps in its README) |
| Reference forensics: easing tracker, contact sheets, spectrograms, SFX onsets | `_video-analysis-tools/` (10 Python scripts; check ffmpeg paths before running) |
| After Effects project rebuilt from an animation (code, MP4, storyboard, HTML), its errors, easing mismatch | `ae-builder/` |
| Save a rule, a correction or an approved insight; catalogue new assets; create a skill | `skill-saver/` |
| Rebuild `INDEX.md` and check the structure (names, descriptions, missing paths) | `python3 06-tools/tools/build_index.py` |
| What is installed on the Mac (ffmpeg path, render venv, Telugu shaping, Homebrew on Intel) | `MAC-TOOLCHAIN.md` |

Known gaps in the original notes (checked 2026-11-25; recheck before relying on them): no PDF reader on the Mac; `yt-dlp` was not installed (a link cannot be downloaded, only studied with the browser capture); Mixkit video is 720p and personal-use only (Pexels first).
