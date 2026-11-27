"""Incremental reference-library scanner for the pro-video-editing skill.

usage: python3 -I refscan.py <reference_folder> [--force] [--reroot]
       Always pass the library ROOT (the folder holding "training videos" and "images"), not a subfolder.

For every video/image under the folder (recursive):
  - content hash (sha1 of bytes, 12 chars); unchanged files are skipped (cache in ../knowledge/cache/<hash>/)
  - videos: probe, 16 kHz wav, EBU R128 loudness, per-frame scene score, cut list,
    2-fps contact sheets (6x5, time-labelled), optional transcript (WHISPER_PY=/path/to/python with faster_whisper)
  - images: size, dHash; matched to the closest video frame (sampled at 5 fps) -> source video + timestamp
Writes ../knowledge/manifest.json (path -> hash, kind, meta, status) and prints NEW / CHANGED / REMOVED / DUPLICATE.
Original reference files are only read, never modified.
"""
import sys, os, json, hashlib, subprocess, re, shutil, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
KB = os.path.join(os.path.dirname(HERE), "knowledge")
CACHE = os.path.join(KB, "cache")
VID = {".mp4", ".mov", ".m4v", ".mkv", ".webm"}
IMG = {".jpg", ".jpeg", ".png", ".webp"}


def ffmpeg():
    for c in (os.environ.get("FFMPEG"), shutil.which("ffmpeg"), "/opt/homebrew/bin/ffmpeg"):
        if c and os.path.exists(c):
            return c
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


FF = ffmpeg()


def sha(p):
    h = hashlib.sha1()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()[:12]


def probe(p):
    e = subprocess.run([FF, "-hide_banner", "-i", p], capture_output=True, text=True).stderr
    d = re.search(r"Duration: (\d+):(\d+):([\d.]+)", e)
    v = re.search(r"Video: .*?(\d{3,5})x(\d{3,5}).*?([\d.]+) fps", e)
    a = re.search(r"Audio: .*?(\d+) Hz", e)
    return {"dur": round(int(d[1]) * 3600 + int(d[2]) * 60 + float(d[3]), 3) if d else None,
            "w": int(v[1]) if v else None, "h": int(v[2]) if v else None,
            "fps": float(v[3]) if v else None, "audio_hz": int(a[1]) if a else None}


def video(p, out, meta):
    os.makedirs(out, exist_ok=True)
    wav = os.path.join(out, "a16.wav")
    subprocess.run([FF, "-v", "error", "-y", "-i", p, "-ac", "1", "-ar", "16000", wav], check=False)
    e = subprocess.run([FF, "-hide_banner", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    tail = e[e.rfind("Summary"):]
    g = lambda k: (re.search(k + r":\s+(-?[\d.]+)", tail) or [None, None])[1]
    meta["loudness"] = {"I_LUFS": g("I"), "LRA": g("LRA"), "peak_dBFS": g("Peak")}
    # per-frame scene score
    r = subprocess.run([FF, "-v", "error", "-i", p, "-vf", "scale=160:-2,select='gte(scene,0)',metadata=print:file=-",
                        "-an", "-f", "null", "-"], capture_output=True, text=True).stdout
    ts, sc = [], []
    for line in r.splitlines():
        if line.startswith("frame:"):
            ts.append(float(re.search(r"pts_time:([\d.]+)", line)[1]))
        elif "scene_score" in line:
            sc.append(float(line.split("=")[1]))
    json.dump({"t": ts, "score": sc}, open(os.path.join(out, "scene.json"), "w"))
    # ffmpeg scene score under-reports on motion-graphics / letterboxed reels, so cuts come from our own
    # frame difference (64x114 gray) with an adaptive threshold: diff > max(14, 5 x local median).
    import numpy as np
    # letterboxed uploads (16:9 inside 9:16): measure only the active picture area
    cd = subprocess.run([FF, "-ss", str(meta["dur"] * 0.3), "-i", p, "-t", "5", "-vf", "cropdetect=24:2:0", "-f", "null", "-"],
                        capture_output=True, text=True).stderr
    crops = re.findall(r"crop=(\d+:\d+:\d+:\d+)", cd)
    crop = max(set(crops), key=crops.count) if crops else None
    if crop and int(crop.split(":")[1]) < 0.9 * meta["h"]:
        meta["active_crop"] = crop
    else:
        crop = None
    W_, H_ = 64, 114
    vf = (f"crop={crop}," if crop else "") + f"scale={W_}:{H_},format=gray"
    pr = subprocess.Popen([FF, "-v", "error", "-i", p, "-vf", vf, "-f", "rawvideo", "-"],
                          stdout=subprocess.PIPE)
    prev, diffs = None, []
    while True:
        b = pr.stdout.read(W_ * H_)
        if len(b) < W_ * H_:
            break
        a = np.frombuffer(b, np.uint8).astype(np.int16)
        diffs.append(0.0 if prev is None else float(np.abs(a - prev).mean()))
        prev = a
    diffs = np.array(diffs)
    fps = meta["fps"] or 30
    k = max(3, int(fps))
    med = np.array([np.median(diffs[max(0, i - k):i + k]) for i in range(len(diffs))])
    idx = [i for i in range(1, len(diffs)) if diffs[i] > max(14, 5 * med[i]) and diffs[i] >= diffs[max(0, i - 1):i + 2].max()]
    np.save(os.path.join(out, "framediff.npy"), diffs)
    merged = []
    for i in idx:
        c = round(i / fps, 3)
        if not merged or c - merged[-1] > 0.2:
            merged.append(c)
    meta["cuts"] = merged
    sl = [b - a for a, b in zip([0] + merged, merged + [meta["dur"]])]
    meta["shots"] = {"n": len(sl), "mean": round(sum(sl) / len(sl), 2), "median": round(sorted(sl)[len(sl) // 2], 2),
                     "per_min": round(len(sl) / meta["dur"] * 60, 1)}
    sheets(p, out, meta)
    wp = os.environ.get("WHISPER_PY")
    if wp and os.path.exists(wp):
        code = ("import sys,json;from faster_whisper import WhisperModel as M;m=M('base',device='cpu',compute_type='int8');"
                "s,i=m.transcribe(sys.argv[1],word_timestamps=True);"
                "json.dump({'lang':i.language,'segs':[{'s':x.start,'e':x.end,'t':x.text.strip(),"
                "'w':[[w.start,w.end,w.word] for w in x.words]} for x in s]},open(sys.argv[2],'w'))")
        subprocess.run([wp, "-c", code, wav, os.path.join(out, "transcript.json")], check=False,
                       capture_output=True)


def sheets(p, out, meta, step=0.5):
    from PIL import Image, ImageDraw, ImageFont
    tmp = tempfile.mkdtemp()
    tw = 240
    th = int(tw * meta["h"] / meta["w"]) if meta["w"] else 427
    subprocess.run([FF, "-v", "error", "-i", p, "-vf", f"fps={1/step},scale={tw}:{th}", "-q:v", "3", f"{tmp}/%05d.jpg"], check=True)
    fs = sorted(os.listdir(tmp))
    try:
        fb = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 13)
    except Exception:
        fb = ImageFont.load_default()
    C, R, LH = 8, 3, 16
    per = C * R
    n = 0
    for s in range(0, len(fs), per):
        sh = Image.new("RGB", (C * tw, R * (th + LH)), (20, 20, 20))
        d = ImageDraw.Draw(sh)
        for k, f in enumerate(fs[s:s + per]):
            i = s + k
            t = i * step
            x, y = (k % C) * tw, (k // C) * (th + LH)
            sh.paste(Image.open(f"{tmp}/{f}"), (x, y + LH))
            cut = any(t - step / 2 <= c < t + step / 2 for c in meta["cuts"])
            d.text((x + 3, y + 1), f"{t:5.1f}s" + (" CUT" if cut else ""), fill=(255, 80, 80) if cut else (255, 214, 0), font=fb)
        n += 1
        sh.save(os.path.join(out, f"sheet_{n:02d}.jpg"), quality=80)
    meta["sheets"] = n
    shutil.rmtree(tmp)


def dhash(im, n=12):
    from PIL import Image
    g = im.convert("L").resize((n + 1, n), Image.BILINEAR)
    px = list(g.getdata())
    return [px[r * (n + 1) + c] > px[r * (n + 1) + c + 1] for r in range(n) for c in range(n)]


def video_hashes(p, meta, out):
    """dHash of frames at 5 fps, cached."""
    hp = os.path.join(out, "dhash5.json")
    if os.path.exists(hp):
        return json.load(open(hp))
    from PIL import Image
    tmp = tempfile.mkdtemp()
    subprocess.run([FF, "-v", "error", "-i", p, "-vf", "fps=5,scale=90:160", f"{tmp}/%05d.png"], check=True)
    hs = [[i / 5, dhash(Image.open(f"{tmp}/{f}"))] for i, f in enumerate(sorted(os.listdir(tmp)))]
    shutil.rmtree(tmp)
    json.dump(hs, open(hp, "w"))
    return hs


def match_image(ip, vids):
    """Phone screenshots carry app UI: compare the central band of the screenshot to video frames,
    trying several crops to allow for status bars / letterboxing. Returns best (video, t, distance)."""
    from PIL import Image
    im = Image.open(ip).convert("RGB")
    W, H = im.size
    best = (None, None, 999)
    for top, bot in ((0.0, 1.0), (0.045, 0.85), (0.06, 0.82), (0.25, 0.62), (0.03, 0.80)):
        crop = im.crop((0, int(H * top), W, int(H * bot)))
        h = dhash(crop.resize((90, 160)))
        for vp, hs in vids.items():
            for t, vh in hs:
                dist = sum(a != b for a, b in zip(h, vh))
                if dist < best[2]:
                    best = (vp, t, dist)
    return best


def main():
    root = os.path.abspath(sys.argv[1])
    force = "--force" in sys.argv
    os.makedirs(CACHE, exist_ok=True)
    mp = os.path.join(KB, "manifest.json")
    man = json.load(open(mp)) if os.path.exists(mp) else {"root": root, "files": {}}
    # Guard (2026-11-21): the manifest holds ONE root. Scanning a subfolder used to rewrite it with only that
    # subfolder's files and drop every other entry. Now a subfolder scan is redirected to the registered root,
    # and any other root needs --reroot.
    reg = os.path.abspath(man.get("root") or root)
    if reg != root and "--reroot" not in sys.argv:
        if root.startswith(reg + os.sep):
            print(f"NOTE: scanning the registered root {reg} (asked for its subfolder {root})")
            root = reg
        else:
            sys.exit(f"manifest root is {reg}, not {root}. Pass --reroot to rebuild the manifest for the new root.")
    old = man["files"]
    new = {}
    report = {"NEW": [], "CHANGED": [], "UNCHANGED": [], "REMOVED": [], "DUPLICATE": []}
    seen = {}
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            ext = os.path.splitext(f)[1].lower()
            if ext not in VID | IMG:
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root)
            h = sha(p)
            kind = "video" if ext in VID else "image"
            ent = {"hash": h, "kind": kind}
            if h in seen:
                ent["duplicate_of"] = seen[h]
                report["DUPLICATE"].append(rel)
            else:
                seen[h] = rel
            prev = old.get(rel)
            status = "UNCHANGED" if prev and prev["hash"] == h and not force else ("CHANGED" if prev else "NEW")
            report[status].append(rel)
            if status == "UNCHANGED":
                ent = prev
            new[rel] = ent
    report["REMOVED"] = [r for r in old if r not in new]
    # analyse videos
    for rel, ent in new.items():
        if ent["kind"] != "video" or "duplicate_of" in ent or ("meta" in ent and rel in report["UNCHANGED"]):
            continue
        p = os.path.join(root, rel)
        out = os.path.join(CACHE, ent["hash"])
        meta = probe(p)
        print("analysing", rel, meta)
        video(p, out, meta)
        ent["meta"] = meta
        ent["cache"] = os.path.relpath(out, KB)
    # match images (only new/changed, or all when new videos arrived)
    vids = {}
    newvid = any(new[r]["kind"] == "video" for r in report["NEW"] + report["CHANGED"])
    for rel, ent in new.items():
        if ent["kind"] == "video" and "duplicate_of" not in ent:
            vids[rel] = video_hashes(os.path.join(root, rel), ent["meta"], os.path.join(KB, ent["cache"]))
    for rel, ent in new.items():
        if ent["kind"] != "image":
            continue
        if "match" in ent and not newvid and rel in report["UNCHANGED"]:
            continue
        vp, t, d = match_image(os.path.join(root, rel), vids)
        ent["match"] = {"video": vp, "t": t, "dist": d, "confidence": "high" if d <= 22 else "medium" if d <= 34 else "low/none"}
    man = {"root": root, "files": new}
    json.dump(man, open(mp, "w"), indent=1, ensure_ascii=False)
    for k, v in report.items():
        if k != "UNCHANGED":
            print(k, len(v), *v[:50], sep="\n  ")
    print("UNCHANGED", len(report["UNCHANGED"]))


if __name__ == "__main__":
    main()
