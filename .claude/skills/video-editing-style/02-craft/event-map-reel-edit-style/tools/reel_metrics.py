#!/usr/bin/env python3
"""reel_metrics.py - objective scorecard for a short-form vertical edit.

Measures the things the video-editing-style skill sets numeric targets for, on a
reference reel or on your own render, so "does it match the style?" gets an
answer that is not a feeling. Reference ranges come from the five analysed reels.

usage:
  python3 reel_metrics.py VIDEO [--crop W:H:X:Y] [--transcribe [MODEL]] [--json OUT.json]

  --crop        analyse only this region of the frame (e.g. the edited panel of a
                side-by-side showcase); source pixels
  --transcribe  also run faster-whisper (default model: small) to get words per
                minute, pause structure, voice-vs-bed level and cut-vs-sentence timing

requires: ffmpeg + ffprobe on PATH, numpy, scipy, opencv-python(-headless)
optional: faster-whisper (only for --transcribe)
"""
import argparse, json, os, re, subprocess, sys, tempfile
import numpy as np


def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(video):
    r = sh(["ffprobe", "-v", "error", "-show_entries",
            "stream=codec_type,width,height,r_frame_rate,sample_rate,channels:format=duration",
            "-of", "json", video])
    j = json.loads(r.stdout or "{}")
    out = {"duration": float(j.get("format", {}).get("duration", 0) or 0)}
    for s in j.get("streams", []):
        if s.get("codec_type") == "video":
            a, b = (s.get("r_frame_rate", "30/1").split("/") + ["1"])[:2]
            out.update(width=s.get("width"), height=s.get("height"), fps=float(a) / float(b or 1))
        elif s.get("codec_type") == "audio":
            out.update(sample_rate=int(s.get("sample_rate", 0) or 0), channels=s.get("channels"))
    return out


def video_metrics(video, crop=None, width=360):
    import cv2
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    prev, diff, luma, sat, act, buf = None, [], [], [], [], []
    LAG = 3  # compare each frame with the one 0.1 s earlier so 6-8 frame fades still register
    while True:
        ok, im = cap.read()
        if not ok:
            break
        if crop:
            w, h, x, y = crop
            im = im[y:y + h, x:x + w]
        h0, w0 = im.shape[:2]
        im = cv2.resize(im, (width, int(round(h0 * width / w0))), interpolation=cv2.INTER_AREA)
        g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32)
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        diff.append(0.0 if prev is None else float(np.abs(g - prev).mean()))
        luma.append(float(np.median(g)))
        sat.append(float(hsv[..., 1].mean()) / 255.0)
        buf.append(g)
        if len(buf) > LAG:
            # activity = strongest change in any of 6x10 blocks: a caption popping in one
            # corner counts as much as a full-frame cut, slow drift does not
            blocks = cv2.resize(np.abs(g - buf[-1 - LAG]), (6, 10), interpolation=cv2.INTER_AREA)
            act.append(float(blocks.max()))
            buf.pop(0)
        else:
            act.append(99.0)
        prev = g
    diff, luma, sat, act = np.array(diff), np.array(luma), np.array(sat), np.array(act)
    n = len(diff)
    dur = n / fps
    # ffmpeg-style scene score: min(mafd, |mafd - prev_mafd|) / 100
    scene = np.zeros(n)
    scene[1:] = np.minimum(diff[1:], np.abs(np.diff(diff))) / 100.0
    cand = [i for i in range(1, n) if scene[i] > 0.25]
    groups = []
    for c in cand:
        if groups and c - groups[-1][-1] <= 6:
            groups[-1].append(c)
        else:
            groups.append([c])
    cuts = [g[int(np.argmax(scene[g]))] for g in groups]
    med = float(np.median(diff[1:])) if n > 1 else 0.0
    # quiet = no block changed by 8+ grey levels over 0.1 s (nothing new is happening anywhere)
    quiet = act < 8.0
    best = cur = start = best_start = 0
    for k, q in enumerate(quiet):
        if q:
            if cur == 0:
                start = k
            cur += 1
            if cur > best:
                best, best_start = cur, start
        else:
            cur = 0
    # luma flips: >= 60-level jumps of the per-second median luma (light <-> dark pattern interrupts)
    sec = [float(np.mean(luma[int(s * fps):int((s + 1) * fps)])) for s in range(int(dur))]
    flips = [s + 1 for s in range(len(sec) - 1) if abs(sec[s + 1] - sec[s]) >= 60]
    return dict(frames=n, fps=fps, duration=dur, median_diff=med,
                static_pct=100.0 * float((diff[1:] < 0.05).mean()) if n > 1 else 0.0,
                hard_cuts=[round(c / fps, 2) for c in cuts],
                longest_quiet_stretch_s=best / fps, longest_quiet_at_s=round(best_start / fps, 2),
                quiet_share_pct=100.0 * float(quiet.mean()) if n else 0.0,
                first_hard_cut_s=(cuts[0] / fps) if cuts else None,
                luma_median=float(np.median(luma)), sat_mean=float(sat.mean()),
                luma_flip_times_s=flips)


def audio_metrics(video, cut_times, words=None, duration=None):
    from scipy.io import wavfile
    from scipy.signal import stft, find_peaks
    out = {}
    r = sh(["ffmpeg", "-hide_banner", "-i", video, "-af", "loudnorm=print_format=summary", "-f", "null", "-"])
    for key, pat in (("integrated_lufs", r"Input Integrated:\s*(-?[\d.]+)"),
                     ("true_peak_dbtp", r"Input True Peak:\s*([+-]?[\d.]+)"),
                     ("lra_lu", r"Input LRA:\s*([\d.]+)")):
        m = re.search(pat, r.stderr)
        if m:
            out[key] = float(m.group(1))
    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, "a.wav")
        sh(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-vn", "-ac", "2", "-ar", "44100", wav])
        if not os.path.exists(wav):
            return out
        sr, x = wavfile.read(wav)
    x = x.astype(np.float32) / 32768.0
    if x.ndim == 1:
        x = np.stack([x, x], axis=1)
    mid, side = (x[:, 0] + x[:, 1]) / 2, (x[:, 0] - x[:, 1]) / 2
    out["side_mid_ratio"] = float(np.sqrt((side ** 2).mean()) / (np.sqrt((mid ** 2).mean()) + 1e-12))
    # SFX density from the stereo side channel: centred voice cancels in L-R, stereo SFX and beds do not.
    # Only meaningful when the mix is reasonably wide (side/mid >= 0.2); refs R2-R4 gave 5.4-9.5 per 10 s.
    if out["side_mid_ratio"] >= 0.2:
        from scipy.ndimage import median_filter
        _, ts, Zs = stft(side, sr, nperseg=2048, noverlap=2048 - 441)
        env = 20 * np.log10(np.sqrt((np.abs(Zs) ** 2).sum(axis=0)) + 1e-9)
        above = env - median_filter(env, size=201, mode="nearest")
        pk, _ = find_peaks(above, height=7, distance=12, prominence=5)
        starts = set()
        for p_ in pk:
            k = p_
            while k > 0 and above[k - 1] > 3:
                k -= 1
            starts.add(k)
        out["sfx_events_per_10s"] = 10.0 * len(starts) / (len(side) / sr)
    f, t, Z = stft(mid, sr, nperseg=2048, noverlap=2048 - 441)
    A = np.abs(Z)
    i = (f >= 6000) & (f < 16000)
    fl = np.maximum(0, np.diff(np.log1p(50 * A[i]), axis=1)).sum(axis=0)
    fl /= fl.max() + 1e-9
    p, _ = find_peaks(fl, height=0.30, distance=8)
    air = t[p + 1]
    if len(cut_times) and len(air):
        off = [float(air[np.argmin(np.abs(air - c))] - c) for c in cut_times]
        out["sfx_on_cut_pct"] = 100.0 * float(np.mean([abs(o) <= 0.10 for o in off]))
        out["cut_to_air_onset_offsets_s"] = [round(o, 2) for o in off]
    if words:
        ws = np.array([w for w, _ in words])
        end = duration or float(t[-1])
        sp = np.zeros(len(t), bool)
        gp = np.zeros(len(t), bool)
        for k, w in enumerate(ws):
            nxt = ws[k + 1] if k + 1 < len(ws) else end
            sp |= (t >= w) & (t < min(w + 0.28, nxt))
            if nxt - w > 0.75:
                gp |= (t >= w + 0.55) & (t < nxt - 0.10)
        band = (f >= 300) & (f < 3000)

        def lvl(mask):
            return 20 * np.log10(np.sqrt((A[band][:, mask] ** 2).mean()) + 1e-9) if mask.any() else float("nan")
        out["voice_minus_bed_db"] = float(lvl(sp) - lvl(gp))
    return out


def transcribe(video, model):
    from faster_whisper import WhisperModel
    from scipy.io import wavfile
    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, "a16.wav")
        sh(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "16000", wav])
        sr, x = wavfile.read(wav)
    x = x.astype(np.float32) / 32768.0
    segs, info = WhisperModel(model, device="cpu", compute_type="int8").transcribe(x, word_timestamps=True)
    words, sent_starts, text = [], [], []
    for s in segs:
        sent_starts.append(float(s.start))
        text.append(s.text.strip())
        for w in s.words:
            tok = w.word.strip()
            # whisper splits "20%" into "20" + "%" and "site.com" into "site" + ".com": count those once
            if not any(ch.isalnum() for ch in tok) or (tok.startswith(".") and len(tok) > 1):
                continue
            words.append((float(w.start), tok))
    return words, sent_starts, " ".join(text)


# (label, key, low, high, unit, note) - ranges measured on the five reference reels
REF = [
    ("Static frames", "static_pct", 0.0, 2.5, "%", "refs 0.2-2.4; nothing should sit frozen"),
    ("Longest visually quiet stretch", "longest_quiet_stretch_s", 0.0, 1.3, "s", "refs 0.13-1.30; something changes at least this often"),
    ("Share of quiet frames", "quiet_share_pct", 0.0, 9.0, "%", "refs 0.5-8.0"),
    ("Integrated loudness", "integrated_lufs", -15.5, -13.5, "LUFS", "refs -15.2 to -14.1"),
    ("True peak", "true_peak_dbtp", -99.0, -1.0, "dBTP", "refs ran hot (-0.8 to +3.4): beat them"),
    ("Hard cuts with an airy SFX within 0.10 s", "sfx_on_cut_pct", 75.0, 100.0, "%", "refs 57-86; a hi-hat bed inflates this, check by ear"),
    ("SFX events per 10 s (stereo side channel)", "sfx_events_per_10s", 5.0, 12.0, "/10s", "refs 5.4-9.5; misses mono subs; n/a on near-mono mixes"),
    ("Words per minute", "wpm", 120.0, 230.0, "wpm", "refs: faceless 128-163, talking head 204-224"),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--crop")
    ap.add_argument("--transcribe", nargs="?", const="small", default=None)
    ap.add_argument("--json")
    a = ap.parse_args()
    crop = tuple(int(v) for v in a.crop.split(":")) if a.crop else None
    res = {"file": os.path.basename(a.video)}
    res.update(probe(a.video))
    v = video_metrics(a.video, crop)
    res.update(v)
    words = None
    if a.transcribe:
        try:
            words, sent_starts, text = transcribe(a.video, a.transcribe)
            res["words"] = len(words)
            res["wpm"] = len(words) / v["duration"] * 60 if v["duration"] else 0
            ws = [w for w, _ in words]
            res["pauses_over_0.6s"] = int(sum(1 for g in np.diff(ws) if g > 0.6))
            res["first_word_s"] = ws[0] if ws else None
            if v["hard_cuts"] and sent_starts:
                st = np.array(sent_starts)
                res["cut_minus_nearest_sentence_start_s"] = [round(float(c - st[np.argmin(np.abs(st - c))]), 2) for c in v["hard_cuts"]]
            res["transcript"] = text
        except Exception as e:  # keep the rest of the scorecard usable
            res["transcribe_error"] = str(e)
    res.update(audio_metrics(a.video, v["hard_cuts"], words, v["duration"]))

    print(f"== {res['file']}  {res.get('width')}x{res.get('height')} @ {res['fps']:.0f} fps, {res['duration']:.2f} s, {res['frames']} frames")
    print(f"hard cuts ({len(res['hard_cuts'])}): {res['hard_cuts']}")
    print(f"luma median {res['luma_median']:.0f}/255, mean saturation {res['sat_mean']:.2f}, light/dark flips at {res['luma_flip_times_s']} s")
    print(f"longest quiet stretch starts at {res['longest_quiet_at_s']} s (look there first)")
    for k in ("lra_lu", "side_mid_ratio", "voice_minus_bed_db", "pauses_over_0.6s", "first_word_s",
              "cut_to_air_onset_offsets_s", "cut_minus_nearest_sentence_start_s"):
        if k in res:
            val = res[k]
            print(f"{k}: {val:.2f}" if isinstance(val, float) else f"{k}: {val}")
    print("\nSCORECARD (reference range from the analysed reels)")
    for label, key, lo, hi, unit, note in REF:
        if key not in res or res[key] is None:
            print(f"  [ -- ] {label}: not measured")
            continue
        val = res[key]
        ok = lo <= val <= hi
        rng = f"<= {hi:g}" if lo in (0.0, -99.0) else f"{lo:g} to {hi:g}"
        print(f"  [{'PASS' if ok else 'LOOK'}] {label}: {val:.2f} {unit}  (target {rng}; {note})")
    if a.json:
        with open(a.json, "w") as fo:
            json.dump(res, fo, indent=1)
        print(f"\njson -> {a.json}")


if __name__ == "__main__":
    main()
