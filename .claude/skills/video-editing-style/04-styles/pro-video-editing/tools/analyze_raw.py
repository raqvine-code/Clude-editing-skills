"""Analyse one video BEFORE editing and start its plan (Rule 2 in CLAUDE 2.0/CLAUDE.md).

usage: python3 analyze_raw.py <video> <project_dir> [--model small|base|medium] [--lang en|te|hi]
Writes into <project_dir>/analysis/:
  facts.json       probe, loudness, cuts (active picture area), silences, speech stats
  transcript.json  word timestamps (faster-whisper via ~/.local/share/whisper-venv)
  transcript.txt   readable segments with times
  sheet_NN.jpg     0.5 s contact sheets (CUT marked)
and <project_dir>/PLAN.md = VIDEO EDITING MASTERY/05-PLAN-TEMPLATE.md with section A pre-filled.
The source video is only read, never modified."""
import sys, os, re, json, subprocess, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import refscan  # probe(), video() pieces, FF

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))  # .../CLAUDE 2.0
TEMPLATE = os.path.join(ROOT, "VIDEO EDITING MASTERY", "05-PLAN-TEMPLATE.md")
WPY = os.path.expanduser("~/.local/share/whisper-venv/bin/python")

src, proj = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "small"
lang = sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else None
out = os.path.join(proj, "analysis")
os.makedirs(out, exist_ok=True)

meta = refscan.probe(src)
os.environ.pop("WHISPER_PY", None)            # transcription done below with VAD + chosen model
refscan.video(src, out, meta)                 # wav, loudness, active-area cuts, sheets

# silences (pauses) from the voice track
e = subprocess.run([refscan.FF, "-hide_banner", "-i", os.path.join(out, "a16.wav"), "-af",
                    "silencedetect=noise=-35dB:d=0.3", "-f", "null", "-"], capture_output=True, text=True).stderr
st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", e)]
en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", e)]
sil = [(round(a, 2), round(b, 2)) for a, b in zip(st, en)]
meta["silences"] = sil
meta["silence_total_s"] = round(sum(b - a for a, b in sil), 2)

# transcript with word timing
tj = os.path.join(out, "transcript.json")
code = ("import sys,json;from faster_whisper import WhisperModel as M;"
        "m=M(sys.argv[3],device='cpu',compute_type='int8');"
        "s,i=m.transcribe(sys.argv[1],word_timestamps=True,vad_filter=True,language=(sys.argv[4] or None));"
        "json.dump({'lang':i.language,'segs':[{'s':round(x.start,2),'e':round(x.end,2),'t':x.text.strip(),"
        "'w':[[round(w.start,2),round(w.end,2),w.word] for w in (x.words or [])]} for x in s]},open(sys.argv[2],'w'),ensure_ascii=False)")
if os.path.exists(WPY):
    r = subprocess.run([WPY, "-c", code, os.path.join(out, "a16.wav"), tj, model, lang or ""], capture_output=True, text=True)
    if r.returncode:
        print("transcription failed:", r.stderr[-400:])
words, segs, tlang = [], [], None
if os.path.exists(tj):
    T = json.load(open(tj)); segs, tlang = T["segs"], T["lang"]
    words = [w for s in segs for w in s["w"]]
    with open(os.path.join(out, "transcript.txt"), "w", encoding="utf-8") as f:
        for s in segs:
            f.write(f"[{s['s']:7.2f} - {s['e']:7.2f}] {s['t']}\n")
gaps = sorted(((round(b[0] - a[1], 2), round(a[1], 2)) for a, b in zip(words, words[1:])), reverse=True)[:8]
speech_s = sum(w[1] - w[0] for w in words)
meta["speech"] = {"lang": tlang, "words": len(words),
                  "words_per_s": round(len(words) / meta["dur"], 2) if meta["dur"] else None,
                  "longest_word_gaps_s_at": gaps}
json.dump(meta, open(os.path.join(out, "facts.json"), "w"), indent=1)

# PLAN.md with section A pre-filled
L = meta.get("loudness", {})
orient = "vertical 9:16" if meta["h"] > meta["w"] else "horizontal" if meta["w"] > meta["h"] else "square"
fill = {
    "- File / duration / resolution / fps / orientation:":
        f"- File / duration / resolution / fps / orientation: `{src}` / {meta['dur']} s / {meta['w']}x{meta['h']} / {meta['fps']} fps / {orient}" + (f" (active picture {meta['active_crop']})" if meta.get("active_crop") else ""),
    "- Loudness (LUFS, LRA, peak) and noise/room notes:":
        f"- Loudness (LUFS, LRA, peak) and noise/room notes: {L.get('I_LUFS')} LUFS, LRA {L.get('LRA')}, peak {L.get('peak_dBFS')} dBFS; noise/room: (check by ear/spectrum)",
    "- Speech: words, words per second, longest pauses, silence total (pauses > 0.3 s are cut candidates):":
        f"- Speech: {len(words)} words, {meta['speech']['words_per_s']} words/s; longest gaps (s, at): {gaps[:5]}; silence > 0.3 s total {meta['silence_total_s']} s in {len(sil)} pauses",
    "- Language (English / Telugu / Tenglish / Hindi):": f"- Language (detected): {tlang} (confirm by reading)",
    "- Already cut? (jump cuts found / polished?) -> keep the user's cut unless told otherwise:":
        f"- Already cut? {len(meta['cuts'])} cuts detected at {meta['cuts'][:20]} -> " + ("looks edited: keep the user's cut unless told otherwise" if len(meta['cuts']) >= 3 else "looks raw/single take"),
}
plan = open(TEMPLATE, encoding="utf-8").read()
for k, v in fill.items():
    plan = plan.replace(k, v)
plan = plan.replace("# PLAN TEMPLATE - copy to `<project_dir>/PLAN.md` and fill every section before editing",
                    f"# PLAN - {os.path.basename(src)}\nAnalysis files: `analysis/` (sheets, transcript.txt, facts.json). Status: DRAFT - fill B-J before editing.")
pp = os.path.join(proj, "PLAN.md")
if os.path.exists(pp):
    pp = os.path.join(proj, "PLAN.auto.md")   # never overwrite a plan already being written
open(pp, "w", encoding="utf-8").write(plan)
print(json.dumps({"plan": pp, "sheets": meta.get("sheets"), "cuts": len(meta["cuts"]), "silences": len(sil),
                  "words": len(words), "lang": tlang, "loudness": L}, indent=1))
