#!/usr/bin/env python3
"""Turn a transcript into caption beats in the Tharun Speaks edit style.

Rules it applies (all measured on the reference reel):
  * one word per beat; a quick glue word joins the next word ("he built", "in the")
  * every beat hard-pops on the frame its first word is spoken and is replaced by the next beat
  * a keyword marked with *asterisks* becomes an emphasis stack:
      small lead-in (the 1-2 words before it), BIG keyword, small trailer (the 1-2 words after it)
  * keyword size depends on length: up to 5 letters 1.75x, 6-8 letters 1.45x, 9+ letters 1.30x

Input, either:
  --words words.json   list of {"word": "...", "start": seconds, "end": seconds}
                       (a Whisper-style {"segments": [{"words": [...]}]} file also works)
  --text "..."         plain text; timings are then only a DRAFT estimated from a speaking rate

Mark keywords in the text or in the word field with asterisks: it was finally *acquired*.
With --words you can also pass --emphasis "acquired,seriously".

Examples:
  python3 caption_beats.py --text "So before it's too late, here are the *5 things* you should build." --html
  python3 caption_beats.py --words words.json --emphasis "acquired,complex" --out beats.json --srt captions.srt
"""
import argparse, json, re, sys

GLUE = {"a", "an", "the", "of", "to", "in", "on", "at", "it", "is", "are", "was", "he", "she", "we", "you", "i",
        "so", "if", "or", "and", "be", "by", "as", "my", "no", "up", "one", "just", "this", "that", "for", "out"}
CLAUSE_END = re.compile(r"[.,!?;:]$")


def load_words(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict):
        data = [w for seg in data.get("segments", []) for w in seg.get("words", [])] or data.get("words", [])
    words = []
    for w in data:
        text = str(w.get("word", w.get("text", ""))).strip()
        if text:
            words.append({"text": text, "start": float(w["start"]), "end": float(w["end"])})
    return words


def words_from_text(text, wpm):
    """Draft timings only: spread words by length, add short pauses after punctuation."""
    tokens = text.split()
    sec_per_char = 60.0 / wpm / 5.2          # about 5.2 characters per spoken word, spaces included
    t, words = 0.0, []
    for tok in tokens:
        dur = max(0.10, (len(tok.strip("*")) + 1) * sec_per_char)
        words.append({"text": tok, "start": t, "end": t + dur})
        t += dur + (0.25 if re.search(r"[.!?]\*?$", tok) else 0.12 if re.search(r"[,;:]\*?$", tok) else 0.0)
    return words


def mark_keys(words, emphasis):
    """Set key=True on marked words. *5 things* marks both words as one keyword phrase."""
    wanted = {e.strip().lower() for e in emphasis.split(",") if e.strip()} if emphasis else set()
    inside = False
    for w in words:
        raw = w["text"]
        starts, ends = raw.startswith("*"), raw.rstrip(".,!?;:").endswith("*")
        w["text"] = raw.replace("*", "")
        w["key"] = inside or starts or w["text"].strip(".,!?;:").lower() in wanted
        if starts and not ends:
            inside = True
        elif ends:
            inside = False
    return words


def key_scale(text):
    n = len(re.sub(r"[^A-Za-z0-9]", "", text))
    return 1.75 if n <= 5 else 1.45 if n <= 8 else 1.30


def build_beats(words, fps, max_pair_chars=10, quick_glue_s=0.18, hold_after_frames=8, min_stack_hold=12):
    fr = lambda s: int(round(s * fps))
    n, i, beats = len(words), 0, []
    used_as_lead = set()

    def clause_break(k):          # True when word k ends a clause
        return bool(CLAUSE_END.search(words[k]["text"]))

    while i < n:
        w = words[i]
        # look ahead: is a keyword coming within the next two words of the same clause? then this word is a lead-in
        j = i
        while j < n and not words[j]["key"] and j - i < 2 and not clause_break(j):
            j += 1
        if j < n and words[j]["key"] and (j == i or j - i <= 2):
            lead = words[i:j]
            if len(lead) == 2 and len(lead[0]["text"]) + 1 + len(lead[1]["text"]) > 10:
                first = lead[0]                           # lead-in too long: the first word becomes its own beat
                beats.append({"type": "pop", "in": fr(first["start"]), "end_hint": fr(first["end"]), "text": first["text"]})
                lead = lead[1:]
            k = j
            while k + 1 < n and words[k + 1]["key"] and not clause_break(k):
                k += 1                                    # multi-word keyword
            key = words[j:k + 1]
            trail, m = [], k + 1
            if not clause_break(k):
                while m < n and len(trail) < 2 and not words[m]["key"]:
                    trail.append(words[m]); m += 1
                    if clause_break(m - 1):
                        break
                if not trail or not clause_break(m - 1) or sum(len(x["text"]) for x in trail) > 12:
                    trail, m = [], k + 1                  # only keep a trailer that finishes the clause and stays short
            parts = []
            if lead:
                parts.append({"role": "lead", "text": " ".join(x["text"] for x in lead), "in": fr(lead[0]["start"])})
            key_text = " ".join(x["text"] for x in key)
            parts.append({"role": "key", "text": key_text, "in": fr(key[0]["start"]), "scale": key_scale(key_text)})
            if trail:
                parts.append({"role": "trail", "text": " ".join(x["text"] for x in trail), "in": fr(trail[0]["start"])})
            last = (trail or key)[-1]
            beats.append({"type": "stack", "in": parts[0]["in"], "end_hint": fr(last["end"]), "parts": parts,
                          "min_hold": min_stack_hold})
            i = m
            continue
        # plain beat, maybe a glue pair
        text, end = w["text"], w["end"]
        nxt = words[i + 1] if i + 1 < n else None
        if (nxt and not nxt["key"] and not clause_break(i) and w["text"].lower().strip("'") in GLUE
                and (w["end"] - w["start"]) < quick_glue_s and len(w["text"]) + 1 + len(nxt["text"]) <= max_pair_chars
                and not nxt["text"][:2].isupper()         # keep acronyms and brand names on their own beat
                and not (i + 2 < n and words[i + 2]["key"] and not clause_break(i + 1))):
            text, end = w["text"] + " " + nxt["text"], nxt["end"]
            i += 1
        beats.append({"type": "pop", "in": fr(w["start"]), "end_hint": fr(end), "text": text})
        i += 1

    # out points: replaced by the next beat; cleared a few frames after the word if a pause follows
    for b, nb in zip(beats, beats[1:] + [None]):
        natural = b["end_hint"] + hold_after_frames
        if b["type"] == "stack":
            natural = max(natural, b["parts"][-1]["in"] + b.pop("min_hold"))
        b["out"] = max(b["in"] + 2, min(natural, nb["in"]) if nb else natural)
        b.pop("end_hint")
    return beats


def to_html(beats):
    cls = {1.75: "key s", 1.45: "key", 1.30: "key l"}
    out = []
    for b in beats:
        if b["type"] == "pop":
            out.append(f'<div class="beat" data-in="{b["in"]}" data-out="{b["out"]}">{b["text"]}</div>')
        else:
            spans = "".join(
                f'<span class="{cls[p["scale"]] if p["role"] == "key" else p["role"]}" data-in="{p["in"]}">{p["text"]}</span>'
                for p in b["parts"])
            out.append(f'<div class="beat" data-in="{b["in"]}" data-out="{b["out"]}"><span class="stack">{spans}</span></div>')
    return "\n".join(out)


def to_srt(beats, fps):
    def tc(f):
        ms = int(round(f / fps * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    rows = []
    for k, b in enumerate(beats, 1):
        text = b["text"] if b["type"] == "pop" else "\n".join(p["text"].upper() if p["role"] == "key" else p["text"] for p in b["parts"])
        rows.append(f"{k}\n{tc(b['in'])} --> {tc(b['out'])}\n{text}\n")
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--words"); ap.add_argument("--text"); ap.add_argument("--emphasis", default="")
    ap.add_argument("--fps", type=float, default=25); ap.add_argument("--wpm", type=float, default=180)
    ap.add_argument("--out"); ap.add_argument("--srt"); ap.add_argument("--html", action="store_true")
    a = ap.parse_args()
    if not a.words and not a.text:
        ap.error("give --words words.json or --text \"...\"")
    words = load_words(a.words) if a.words else words_from_text(a.text, a.wpm)
    beats = build_beats(mark_keys(words, a.emphasis), a.fps)
    result = {"fps": a.fps, "draft_timings": not a.words, "beats": beats}
    if a.out:
        json.dump(result, open(a.out, "w", encoding="utf-8"), indent=1)
    if a.srt:
        open(a.srt, "w", encoding="utf-8").write(to_srt(beats, a.fps))
    if a.html:
        print(to_html(beats))
    elif not a.out and not a.srt:
        json.dump(result, sys.stdout, indent=1); print()
    durs = [b["out"] - b["in"] for b in beats]
    print(f"{len(beats)} beats, median {sorted(durs)[len(durs) // 2]} frames at {a.fps:g} fps"
          + ("  (DRAFT timings: replace with real word timestamps)" if not a.words else ""), file=sys.stderr)


if __name__ == "__main__":
    main()
