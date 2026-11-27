#!/usr/bin/env python3
"""score_reel.py - run the event-map scorecard (reel_metrics.py, untouched from the zip 2 pack) on this Mac.

usage: python3 score_reel.py VIDEO [--words N] [--crop W:H:X:Y] [--json out.json] [--transcribe [model]]

What it adds around the pack script:
- ffmpeg (the imageio binary when none is on PATH) and an ffprobe stand-in are put on PATH for the run;
- a video that is not 30 fps is scored on a temporary 30 fps copy (audio copied untouched), because the
  script's thresholds (0.1 s = 3 frames) and the reference ranges assume 30 fps;
- --words N: word count from an existing transcript -> the words-per-minute line (no faster-whisper needed).
"""
import json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def find_ffmpeg():
    ff = os.environ.get("SCORE_FFMPEG") or shutil.which("ffmpeg")
    if not ff:
        import imageio_ffmpeg
        ff = imageio_ffmpeg.get_ffmpeg_exe()
    return ff


def info(ff, video):
    err = subprocess.run([ff, "-hide_banner", "-i", video], capture_output=True, text=True).stderr
    out = {"duration": 0.0, "fps": 30.0}
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    if m:
        out["duration"] = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    v = next((l for l in err.splitlines() if "Video:" in l), "")
    m = re.search(r", (\d{2,5})x(\d{2,5})[ ,\[]", v)
    if m:
        w, h = int(m.group(1)), int(m.group(2))
        if re.search(r"rotation of -?(90|270)", err):
            w, h = h, w
        out.update(width=w, height=h)
    m = re.search(r"([\d.]+) fps", v) or re.search(r"([\d.]+) tbr", v)
    if m:
        out["fps"] = float(m.group(1))
    a = next((l for l in err.splitlines() if "Audio:" in l), "")
    m = re.search(r"(\d+) Hz, ([^,\n]+)", a)
    if m:
        lay = m.group(2).strip()
        out.update(sample_rate=int(m.group(1)), channels={"mono": 1, "stereo": 2}.get(lay, 6 if "5.1" in lay else 2))
    return out


def as_ffprobe(argv):
    """Answer the one ffprobe call reel_metrics.py makes (-show_entries ... -of json VIDEO)."""
    i = info(find_ffmpeg(), argv[-1])
    streams = []
    if "width" in i:
        streams.append({"codec_type": "video", "width": i["width"], "height": i["height"], "r_frame_rate": f"{i['fps']}/1"})
    if "sample_rate" in i:
        streams.append({"codec_type": "audio", "sample_rate": str(i["sample_rate"]), "channels": i["channels"]})
    print(json.dumps({"streams": streams, "format": {"duration": str(i["duration"])}}))


def main():
    args = sys.argv[1:]
    if args and args[0] == "--as-ffprobe":
        return as_ffprobe(args)
    words = None
    if "--words" in args:
        k = args.index("--words")
        words = int(args[k + 1])
        del args[k:k + 2]
    if not args or args[0].startswith("-"):
        sys.exit(__doc__)
    video, rest = args[0], args[1:]
    ff = find_ffmpeg()
    i = info(ff, video)
    with tempfile.TemporaryDirectory() as td:
        if not shutil.which("ffmpeg"):
            os.symlink(ff, os.path.join(td, "ffmpeg"))
        if not shutil.which("ffprobe"):
            shim = os.path.join(td, "ffprobe")
            with open(shim, "w") as fo:
                fo.write(f'#!/bin/sh\nexec "{sys.executable}" "{os.path.abspath(__file__)}" --as-ffprobe "$@"\n')
            os.chmod(shim, 0o755)
        target = video
        if abs(i["fps"] - 30.0) > 0.5:
            target = os.path.join(td, os.path.splitext(os.path.basename(video))[0] + "_30fps_copy.mkv")
            print(f"source is {i['fps']:g} fps: scoring a temporary 30 fps copy (audio untouched)", flush=True)
            r = subprocess.run([ff, "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-vf", "fps=30",
                                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "16", "-c:a", "copy", target])
            if r.returncode != 0:
                sys.exit("could not make the 30 fps copy")
        env = dict(os.environ, PATH=td + os.pathsep + os.environ.get("PATH", ""), SCORE_FFMPEG=ff)
        rc = subprocess.run([sys.executable, os.path.join(HERE, "reel_metrics.py"), target] + rest, env=env).returncode
    if words and i["duration"]:
        wpm = words / i["duration"] * 60
        tag = "PASS" if 120 <= wpm <= 230 else "LOOK"
        print(f"  [{tag}] Words per minute (from --words {words}): {wpm:.0f} wpm  (refs: faceless 128-163, talking head 204-224)")
        if "--json" in rest:
            p = rest[rest.index("--json") + 1]
            if os.path.exists(p):
                j = json.load(open(p))
                j.update(words=words, wpm=wpm, source_file=os.path.basename(video), source_fps=i["fps"])
                json.dump(j, open(p, "w"), indent=1)
    sys.exit(rc)


if __name__ == "__main__":
    main()
