#!/usr/bin/env python3
"""
extract.py - helper for the "watch" skill.

Takes a video link (YouTube, Shorts, Reels, TikTok...) or a local file and prepares
everything Claude needs to study the editing style:
  frames/        sampled frames (dense in the first 60s, plus frames around every cut)
  pairs/         two frames side by side with timestamps (frame A | frame B)
  cuts.json      detected cut times
  words.json     word by word transcript with timestamps (needs whisper)
  audio_profile.json  loudness, silences, sudden hits (probable SFX)
  summary.json   shot length stats, cuts per minute, words per second

Usage:
  python3 extract.py "<link or file>" --name my-style
  python3 extract.py "<link or file>" --name my-style --start 0 --end 120
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd, check=True, capture=True):
    return subprocess.run(
        cmd, check=check, text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )


def need(tool):
    if shutil.which(tool) is None:
        sys.exit(f"ERROR: '{tool}' is not installed. Install it first, then run again.")


def slugify(text):
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:40] or "video"


def is_url(s):
    return bool(re.match(r"^https?://", s.strip()))


def download(url, out_dir):
    need("yt-dlp")
    target = out_dir / "source.mp4"
    cmd = [
        "yt-dlp", "-f", "bv*[height<=1080]+ba/b[height<=1080]/b",
        "--merge-output-format", "mp4", "--no-playlist",
        "--write-info-json", "-o", str(out_dir / "source.%(ext)s"), url,
    ]
    r = run(cmd, check=False)
    if r.returncode != 0 or not target.exists():
        print(r.stderr[-1500:], file=sys.stderr)
        sys.exit(
            "ERROR: download failed. Try: pip install -U yt-dlp  and run again. "
            "If it still fails, download the video yourself and pass the file path."
        )
    title = None
    info = out_dir / "source.info.json"
    if info.exists():
        try:
            title = json.loads(info.read_text()).get("title")
        except Exception:
            pass
    return target, title


def probe(path):
    r = run([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ])
    data = json.loads(r.stdout)
    duration = float(data["format"].get("duration", 0))
    vstream = next((s for s in data["streams"] if s["codec_type"] == "video"), {})
    has_audio = any(s["codec_type"] == "audio" for s in data["streams"])
    fps = 0.0
    if vstream.get("r_frame_rate") and "/" in vstream["r_frame_rate"]:
        a, b = vstream["r_frame_rate"].split("/")
        fps = float(a) / float(b) if float(b) else 0.0
    return {
        "duration": duration,
        "width": vstream.get("width"),
        "height": vstream.get("height"),
        "fps": round(fps, 2),
        "has_audio": has_audio,
    }


def detect_cuts(src, start, end, threshold):
    """Scene change detection with ffmpeg. Returns list of cut times in seconds."""
    cmd = ["ffmpeg", "-hide_banner", "-nostats"]
    if start:
        cmd += ["-ss", str(start)]
    if end:
        cmd += ["-to", str(end)] if not start else ["-t", str(end - start)]
    cmd += [
        "-i", str(src),
        "-vf", f"select='gt(scene,{threshold})',showinfo",
        "-an", "-f", "null", "-",
    ]
    r = run(cmd, check=False)
    cuts = []
    for m in re.finditer(r"pts_time:([0-9.]+)", r.stderr or ""):
        cuts.append(round(float(m.group(1)) + (start or 0), 3))
    return sorted(set(cuts))


def build_timestamps(start, end, cuts, max_frames, dense_seconds=60, dense_step=0.5):
    ts = set()
    dense_end = min(end, start + dense_seconds)
    t = start
    while t < dense_end:
        ts.add(round(t, 2))
        t += dense_step
    remaining = end - dense_end
    budget = max(max_frames - len(ts) - 2 * len(cuts), 20)
    if remaining > 0:
        step = max(1.0, remaining / budget)
        t = dense_end
        while t < end:
            ts.add(round(t, 2))
            t += step
    # frames right before and after each cut, so every cut is visible in a pair
    for c in cuts:
        ts.add(round(max(start, c - 0.08), 2))
        ts.add(round(min(end - 0.05, c + 0.12), 2))
    ts = sorted(x for x in ts if start <= x < end)
    # trim if there are too many frames
    if len(ts) > max_frames * 1.5:
        keep_cut = set()
        for c in cuts:
            keep_cut.add(round(max(start, c - 0.08), 2))
            keep_cut.add(round(min(end - 0.05, c + 0.12), 2))
        others = [x for x in ts if x not in keep_cut]
        stride = max(1, len(others) // max(1, max_frames - len(keep_cut)))
        ts = sorted(set(others[::stride]) | keep_cut)
    return ts


def grab_frames(src, timestamps, frames_dir):
    frames_dir.mkdir(parents=True, exist_ok=True)
    out = []
    for t in timestamps:
        f = frames_dir / f"f_{int(round(t * 100)):07d}.jpg"
        r = run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", str(t), "-i", str(src), "-frames:v", "1",
            "-vf", "scale=-2:540", "-q:v", "3", str(f),
        ], check=False)
        if f.exists():
            out.append((t, f))
    return out


def fmt_time(t):
    m = int(t // 60)
    s = t - m * 60
    return f"{m:02d}:{s:05.2f}"


def make_pairs(frames, pairs_dir):
    from PIL import Image, ImageDraw
    pairs_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for i in range(0, len(frames) - 1, 2):
        (ta, fa), (tb, fb) = frames[i], frames[i + 1]
        ia, ib = Image.open(fa).convert("RGB"), Image.open(fb).convert("RGB")
        h = max(ia.height, ib.height)
        canvas = Image.new("RGB", (ia.width + ib.width + 12, h + 28), (20, 20, 20))
        canvas.paste(ia, (0, 28))
        canvas.paste(ib, (ia.width + 12, 28))
        d = ImageDraw.Draw(canvas)
        d.text((6, 8), f"A  {fmt_time(ta)}", fill=(255, 255, 255))
        d.text((ia.width + 18, 8), f"B  {fmt_time(tb)}", fill=(255, 255, 255))
        p = pairs_dir / f"pair_{i // 2:04d}_{int(round(ta * 100)):07d}.jpg"
        canvas.save(p, quality=80)
        made.append({"file": p.name, "a": ta, "b": tb})
    return made


def transcribe(src, out_dir, start, end):
    """Word level transcript. Returns list of {word, start, end}."""
    wav = out_dir / "audio.wav"
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    if start:
        cmd += ["-ss", str(start)]
    if end:
        cmd += ["-to", str(end)] if not start else ["-t", str(end - start)]
    cmd += ["-i", str(src), "-vn", "-ac", "1", "-ar", "16000", str(wav)]
    run(cmd, check=False)
    if not wav.exists():
        return [], "no audio track"
    try:
        import whisper  # type: ignore
    except Exception:
        return [], "whisper is not installed (pip install openai-whisper)"
    try:
        model = whisper.load_model("base")
        result = model.transcribe(str(wav), word_timestamps=True, verbose=False)
        words = []
        for seg in result.get("segments", []):
            for w in seg.get("words", []):
                words.append({
                    "word": w["word"].strip(),
                    "start": round(w["start"] + (start or 0), 3),
                    "end": round(w["end"] + (start or 0), 3),
                })
        return words, f"language={result.get('language')}"
    except Exception as e:  # pragma: no cover
        return [], f"whisper failed: {e}"


def audio_profile(src, start, end):
    """Loudness per 100 ms, silences, sudden hits (probable SFX)."""
    import numpy as np
    sr = 16000
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error"]
    if start:
        cmd += ["-ss", str(start)]
    if end:
        cmd += ["-to", str(end)] if not start else ["-t", str(end - start)]
    cmd += ["-i", str(src), "-vn", "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not r.stdout:
        return {"error": "no audio"}
    x = np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0
    win = sr // 10  # 100 ms
    n = len(x) // win
    if n < 3:
        return {"error": "audio too short"}
    frames = x[: n * win].reshape(n, win)
    rms = np.sqrt((frames ** 2).mean(axis=1) + 1e-12)
    db = 20 * np.log10(rms + 1e-9)
    # high frequency energy ratio helps tell whooshes/clicks from voice/music
    spec = np.abs(np.fft.rfft(frames, axis=1))
    freqs = np.fft.rfftfreq(win, 1 / sr)
    hi = spec[:, freqs > 3000].sum(axis=1)
    tot = spec.sum(axis=1) + 1e-9
    hi_ratio = hi / tot

    silence_thr = -45.0
    silences, cur = [], None
    for i, v in enumerate(db):
        if v < silence_thr:
            cur = i if cur is None else cur
        else:
            if cur is not None and (i - cur) >= 3:
                silences.append([round(cur / 10 + (start or 0), 2), round(i / 10 + (start or 0), 2)])
            cur = None

    # sudden hits: a window much louder than the average of the previous 0.5 s
    hits = []
    for i in range(5, n):
        prev = db[i - 5:i].mean()
        if db[i] - prev > 9 and db[i] > -30:
            if not hits or (i / 10 + (start or 0)) - hits[-1]["time"] > 0.3:
                hits.append({
                    "time": round(i / 10 + (start or 0), 2),
                    "jump_db": round(float(db[i] - prev), 1),
                    "high_freq_ratio": round(float(hi_ratio[i]), 2),
                })
    return {
        "window_seconds": 0.1,
        "loudness_db_mean": round(float(db.mean()), 1),
        "loudness_db_p10_p90": [round(float(np.percentile(db, 10)), 1), round(float(np.percentile(db, 90)), 1)],
        "silence_threshold_db": silence_thr,
        "silences": silences,
        "silence_total_seconds": round(sum(b - a for a, b in silences), 1),
        "probable_sfx_hits": hits,
        "loudness_timeline_db": [round(float(v), 1) for v in db[::5]],  # every 0.5 s
        "note": "Hits with high_freq_ratio above 0.4 are often whooshes, clicks or glitches. Confirm by looking at the frame at that time.",
    }


def stats(cuts, start, end):
    bounds = [start] + [c for c in cuts if start < c < end] + [end]
    lengths = [round(b - a, 3) for a, b in zip(bounds, bounds[1:]) if b - a > 0]
    if not lengths:
        return {}
    srt = sorted(lengths)
    return {
        "shots": len(lengths),
        "avg_shot_seconds": round(sum(lengths) / len(lengths), 2),
        "median_shot_seconds": srt[len(srt) // 2],
        "shortest_shot_seconds": srt[0],
        "longest_shot_seconds": srt[-1],
        "cuts_per_minute": round(len(cuts) / max((end - start) / 60, 0.01), 1),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="video link or local file")
    ap.add_argument("--name", default=None, help="style name used for the folder")
    ap.add_argument("--out-root", default="references/watch")
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--end", type=float, default=0.0)
    ap.add_argument("--max-frames", type=int, default=240)
    ap.add_argument("--scene-threshold", type=float, default=0.3)
    ap.add_argument("--no-transcribe", action="store_true")
    args = ap.parse_args()

    need("ffmpeg")
    need("ffprobe")
    try:
        import PIL  # noqa: F401
        import numpy  # noqa: F401
    except Exception:
        sys.exit("ERROR: run  pip install pillow numpy  and try again.")

    root = Path(args.out_root)
    tmp_slug = slugify(args.name) if args.name else "video-" + slugify(Path(args.source).stem if not is_url(args.source) else "link")
    out_dir = root / tmp_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    title = None
    if is_url(args.source):
        print("Downloading video...")
        src, title = download(args.source, out_dir)
        if not args.name and title:
            new_dir = root / slugify(title)
            if not new_dir.exists():
                out_dir.rename(new_dir)
                out_dir = new_dir
                src = out_dir / "source.mp4"
    else:
        p = Path(args.source).expanduser()
        if not p.exists():
            sys.exit(f"ERROR: file not found: {p}")
        src = out_dir / ("source" + p.suffix)
        if not src.exists():
            shutil.copy2(p, src)

    meta = probe(src)
    start = max(0.0, args.start)
    end = args.end if args.end and args.end > start else meta["duration"]
    end = min(end, meta["duration"])
    print(f"Video: {meta['width']}x{meta['height']} {meta['fps']}fps, {meta['duration']:.1f}s. Studying {start:.1f}s to {end:.1f}s")

    print("Detecting cuts...")
    cuts = detect_cuts(src, start, end, args.scene_threshold)
    (out_dir / "cuts.json").write_text(json.dumps(cuts, indent=2))

    print("Sampling frames...")
    ts = build_timestamps(start, end, cuts, args.max_frames)
    frames = grab_frames(src, ts, out_dir / "frames")

    print("Making frame pairs...")
    pairs = make_pairs(frames, out_dir / "pairs")
    (out_dir / "pairs_index.json").write_text(json.dumps(pairs, indent=2))

    words, tnote = [], "skipped"
    if not args.no_transcribe and meta["has_audio"]:
        print("Transcribing word by word...")
        words, tnote = transcribe(src, out_dir, start, end)
    (out_dir / "words.json").write_text(json.dumps(words, indent=2, ensure_ascii=False))

    print("Profiling audio...")
    audio = audio_profile(src, start, end) if meta["has_audio"] else {"error": "no audio track"}
    (out_dir / "audio_profile.json").write_text(json.dumps(audio, indent=2))

    wps = None
    if words:
        span = max(words[-1]["end"] - words[0]["start"], 0.01)
        wps = round(len(words) / span, 2)

    summary = {
        "source": args.source,
        "title": title,
        "folder": str(out_dir),
        "video": meta,
        "studied_range_seconds": [round(start, 2), round(end, 2)],
        "orientation": "vertical" if (meta["height"] or 0) > (meta["width"] or 0) else "horizontal",
        "cut_stats": stats(cuts, start, end),
        "frames_sampled": len(frames),
        "pairs_made": len(pairs),
        "words_transcribed": len(words),
        "words_per_second": wps,
        "transcription_note": tnote,
        "probable_sfx_hits": len(audio.get("probable_sfx_hits", [])) if isinstance(audio, dict) else 0,
        "silence_total_seconds": audio.get("silence_total_seconds") if isinstance(audio, dict) else None,
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    (out_dir / "analysis").mkdir(exist_ok=True)

    print("\nDONE")
    print(json.dumps(summary, indent=2))
    print(f"\nNext: open {out_dir}/pairs/ and study the images in order.")


if __name__ == "__main__":
    main()
