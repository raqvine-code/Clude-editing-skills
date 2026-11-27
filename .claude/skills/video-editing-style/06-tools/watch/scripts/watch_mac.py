#!/usr/bin/env python3
"""
watch_mac.py - run the received extract.py on this Mac (added 2026-11-22, not part of the received skill).

This Mac has no ffmpeg / ffprobe on PATH, no openai-whisper and no yt-dlp. This wrapper:
  - puts the imageio ffmpeg binary on PATH as `ffmpeg`,
  - adds an `ffprobe` stand-in that answers the one call extract.py makes,
  - adds a `whisper` stand-in module that uses faster-whisper from ~/.local/share/whisper-venv,
  - runs extract.py unchanged with the whisper venv python.

Usage (same arguments as extract.py):
  python3 watch_mac.py "<local video file>" --name my-style
  python3 watch_mac.py "<file>" --name my-style --start 0 --end 120
Default output root: CLAUDE 2.0/edits/_watch-studies/<slug>/   (override with --out-root)
Env: WATCH_WHISPER_MODEL=small (default) | base | medium | large-v3
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))          # CLAUDE 2.0/
DEFAULT_OUT = os.path.join(WORKSPACE, "edits", "_watch-studies")
VENV_PY = os.path.expanduser("~/.local/share/whisper-venv/bin/python")

WHISPER_SHIM = '''
import os
from faster_whisper import WhisperModel

class _Model:
    def __init__(self, name):
        self.m = WhisperModel(name, device="cpu", compute_type="int8")
    def transcribe(self, path, word_timestamps=True, verbose=False, **kw):
        segs, info = self.m.transcribe(path, word_timestamps=True, vad_filter=True)
        out = []
        for s in segs:
            out.append({"start": s.start, "end": s.end, "text": s.text,
                        "words": [{"word": w.word, "start": w.start, "end": w.end} for w in (s.words or [])]})
        return {"segments": out, "language": info.language}

def load_model(name):
    return _Model(os.environ.get("WATCH_WHISPER_MODEL", "small"))
'''


def find_ffmpeg():
    ff = shutil.which("ffmpeg")
    if ff:
        return ff
    for py in (sys.executable, "python3", VENV_PY):
        try:
            r = subprocess.run([py, "-c", "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"],
                               capture_output=True, text=True)
            p = r.stdout.strip()
            if r.returncode == 0 and p and os.path.exists(p):
                return p
        except Exception:
            pass
    sys.exit("ERROR: no ffmpeg found (PATH or imageio_ffmpeg).")


def as_ffprobe(argv):
    """Answer: ffprobe -v error -print_format json -show_format -show_streams FILE"""
    video = argv[-1]
    ff = os.environ["WATCH_FFMPEG"]
    err = subprocess.run([ff, "-hide_banner", "-i", video], capture_output=True, text=True).stderr
    dur = 0.0
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", err)
    if m:
        dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    streams = []
    for line in err.splitlines():
        if "Video:" in line and "Stream #" in line:
            wh = re.search(r"[, ](\d{2,5})x(\d{2,5})[, \[]", line)
            fps = re.search(r"([\d.]+)\s*fps", line)
            f = float(fps.group(1)) if fps else 0.0
            streams.append({"codec_type": "video",
                            "width": int(wh.group(1)) if wh else None,
                            "height": int(wh.group(2)) if wh else None,
                            "r_frame_rate": f"{int(round(f * 1000))}/1000" if f else "0/1"})
        elif "Audio:" in line and "Stream #" in line:
            streams.append({"codec_type": "audio"})
    print(json.dumps({"format": {"duration": str(dur)}, "streams": streams}))
    return 0


def main():
    args = sys.argv[1:]
    if args and args[0] == "--as-ffprobe":
        return as_ffprobe(args)
    if not args:
        sys.exit(__doc__)
    if re.match(r"^https?://", args[0].strip()) and not shutil.which("yt-dlp"):
        sys.exit("ERROR: yt-dlp is not installed on this Mac, so links cannot be downloaded here.\n"
                 "Ask the user to download the video and give the file path (or to approve installing yt-dlp).")
    if "--out-root" not in args:
        args += ["--out-root", DEFAULT_OUT]
    ff = find_ffmpeg()
    py = VENV_PY if os.path.exists(VENV_PY) else sys.executable
    with tempfile.TemporaryDirectory() as td:
        os.symlink(ff, os.path.join(td, "ffmpeg"))
        if not shutil.which("ffprobe"):
            shim = os.path.join(td, "ffprobe")
            with open(shim, "w") as fo:
                fo.write(f'#!/bin/sh\nexec "{sys.executable}" "{os.path.abspath(__file__)}" --as-ffprobe "$@"\n')
            os.chmod(shim, 0o755)
        mods = os.path.join(td, "mods")
        os.mkdir(mods)
        have_whisper = subprocess.run([py, "-c", "import whisper"], capture_output=True).returncode == 0
        if not have_whisper:
            with open(os.path.join(mods, "whisper.py"), "w") as fo:
                fo.write(WHISPER_SHIM)
        env = dict(os.environ, WATCH_FFMPEG=ff,
                   PATH=td + os.pathsep + os.environ.get("PATH", ""),
                   PYTHONPATH=mods + os.pathsep + os.environ.get("PYTHONPATH", ""))
        return subprocess.run([py, os.path.join(HERE, "extract.py")] + args, env=env).returncode


if __name__ == "__main__":
    sys.exit(main())
