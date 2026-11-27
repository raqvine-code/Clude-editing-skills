# This Mac's editing toolchain (checked 2026-11-25)

**Why this file exists:** the skills assume these tools. Read it before installing anything or running a received script. Keep it current: add a dated line when something changes, and add an entry to `CHANGELOG.md`.

**Machine:** Intel Core i7-9750H, 32 GB RAM, macOS 26.7. Homebrew lives in `/usr/local`.

## Video and audio
- **ffmpeg** is not on PATH. Use the imageio binary, which has libass, drawtext, loudnorm, rubberband, vidstab, afftdn / arnndn, x264, x265, ProRes and VideoToolbox:
  - `/Library/Frameworks/Python.framework/Versions/3.15/lib/python3.15/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-x86_64-v9.0.2`
  - or `python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"`.
- **There is no ffprobe.** A received script that calls `ffmpeg` / `ffprobe` needs a PATH shim and an ffprobe stand-in that parses `ffmpeg -i` (the pattern is in `event-map-reel-edit-style/tools/score_reel.py`).
- **Range renders:** `shortkit.py video --from --to` writes frames only. Encode them with the binary above:
  - `-framerate 60 -start_number N`;
  - mux the audio with `-ss/-t`;
  - libx264 CRF 19, maxrate 20M.
- **Do not `brew install ffmpeg`:** it would land first on PATH, ahead of the imageio binary that shortkit expects.

## Python
- **The render / transcribe venv is `~/.local/share/whisper-venv/bin/python`** (Python 3.9.6). It has:
  - faster-whisper 1.2.1, with the base, small, medium and large-v3 models;
  - Pillow 11.3 with raqm, OpenCV 5.0, mediapipe 0.10.14, fontTools 4.60, scipy 1.13, numpy 2.0.
- **Use this venv to run:** `shortkit.py`, `analyze_raw.py`, `matte.py`, `pairing_board.py`, `specimen.py` and `telugu_check.py`.
- **System `python3` is 3.15.2.** It has numpy, scipy, Pillow, soundfile, imageio_ffmpeg and OpenCV headless.
  - No Intel wheels exist for rembg, onnxruntime, librosa, mediapipe or pedalboard; do not try again. Use the venv instead.
- **Variable fonts load at their default weight in Pillow** (often thin). Cut statics with `fontTools.varLib.instancer.instantiateVariableFont(font, {"wght": 700}, updateFontNames=False)`.
- **Telugu script shapes correctly since 2026-11-25.** Pillow's wheel bundles raqm and harfbuzz and only needs Homebrew's `libfribidi.dylib` when it runs.
  - Check: `pro-font-and-subtitle-guide/tools/telugu_check.py`.
  - If raqm reads False, run `brew install fribidi`.
  - raqm also kerns Latin text, so captions are up to 1.6 % narrower than before. For partial re-renders of older projects, set `SHORTKIT_LAYOUT=basic`.

## Homebrew on Intel
- **Since 2026-09 Homebrew builds no Intel bottles, so new formulae compile from source.**
  - `libraqm` alone meant 36 source builds (cmake, python, glib, icu4c, cairo...); `fribidi` meant 3 (about 25 minutes, most of it gettext's configure).
  - Before any install, find the smallest formula that provides the library that is actually needed. Check with `brew deps --include-build <formula>` (set `HOMEBREW_NO_AUTO_UPDATE=1`).
- **A long silence during `./configure` is normal.** Check that it is alive with `ps -Ao etime,command | grep configure`.
- **Installed formulae worth knowing:** fribidi, node and nvm (node v20 in `~/.nvm`), gh, go, cmake.

## Downloads and the web
- **Download with `curl`.** Python `urllib` fails SSL certificate checks here.
- **Free fonts:** `https://raw.githubusercontent.com/google/fonts/main/ofl/<family>/<file>`. Apache-licensed ones are under `apache/`. Get each licence file too.
- **Treat every download as untrusted:**
  - put it in its own scratch folder;
  - check it in Python with `-I`;
  - then copy it into the library.
  - Never clean up with an `rm` on a variable path.
- **The app blocks downloading and running programs from websites** (such as a static ffprobe). Download data files only.
- **No PDF reader (2026-11-25):** no `pypdf` / PyMuPDF in either Python, no `pdftotext`, and the Read tool needs poppler to render pages. A paper's PDF can be fetched but not read. Use its abstract page, an HTML copy or a search summary, and say so in the notes. `brew install poppler` would fix it; it builds from source on Intel, so ask first.
- **`yt-dlp` is not installed**, so a link can't be downloaded. Study Instagram / YouTube links in the built-in browser with `06-tools/_video-analysis-tools/browser_reference_capture.js` (picture only; sound is not measured).

## Fonts
- **The central library is `fonts-and-colours/assets/fonts/`:** 79 files, licences in `licences/`, roles in `FONTS-README.md` and `pro-font-and-subtitle-guide`. `~/Library/Fonts` has only 3 files.
- **System fonts** (Times New Roman, Impact...) can be rendered into a video but never shipped as files.

## Shell
- **2026-11-25:** `~/.zshrc` printed a parse error on every new terminal. The cause was an unfilled `export EPIDEMIC_API_KEY=<your key>` placeholder; it is now commented out (backup `~/.zshrc.bak-2026-11-25`). A real Epidemic Sound key goes on that line in quotes.
