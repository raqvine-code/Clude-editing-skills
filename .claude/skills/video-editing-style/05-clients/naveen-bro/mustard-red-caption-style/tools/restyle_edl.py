"""Restyle the captions of an existing shortkit EDL into a mustard-red look. Only "style" and "captions" change.
Usage: python3 -I restyle_edl.py <edl.json> <out.json> [M4|M1|M2] [--project <dir>]
  M4 = Haldi-Kumkum signature (Claude's look, default): ghost lead-ins in Bricolage Grotesque SemiBold, keyword in
       Fraunces Soft Bold Italic mustard, red (kumkum) on negative words, haldi brush on up to 4 hero keywords,
       kumkum dot at the end of up to 1 statement per 8 s.
  M1 = podcast serif (Montserrat Bold caps + Playfair ExtraBold Italic keyword), M2 = golden caps (one line, Bebas Neue).
Rules from skills/mustard-red-caption-style/GUIDE.md. Override per word in the EDL with {"role": "neg"|"key"|"hero"|"dot"}.
"""
import json, sys, copy, re

R = "/Users/raghusai/Desktop/CLAUDE 2.0"
F = R + "/skills/fonts-and-colours/assets/fonts/"
HALDI, KUMKUM, CREAM = "#E2AA2C", "#C8372D", "#F4EFE3"
NEG = {"kaadu", "kaadhu", "ledu", "leru", "vaddu", "kadu", "not", "no", "never", "waste", "scam", "fake", "wrong",
       "extra", "loss", "problem", "mistake", "danger", "stop", "tax", "fail", "kharchu", "mosam", "mosapotunnaru"}
STYLES = {
    "M4": {"cap_font": F + "BricolageGrotesque-SemiBold.ttf", "key_font": F + "Fraunces-SoftBoldItalic.ttf",
           "cap_size": 60, "key_size": 150, "key_max_w": 860, "stroke": 3, "ghost": 0.30},
    "M1": {"cap_font": R + "/edits/telugu3/assets/fonts/Montserrat-Bold.ttf",
           "key_font": R + "/edits/telugu4/assets/fonts/PlayfairDisplay-ExtraBoldItalic.ttf",
           "cap_size": 62, "key_size": 150, "key_max_w": 880, "stroke": 4},
    "M2": {"cap_font": F + "BebasNeue-Regular.ttf", "cap_size": 118, "stroke": 5},
}


def bare(w):
    return re.sub(r"[^a-z]", "", w.lower())


def main():
    src, out = sys.argv[1], sys.argv[2]
    look = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].startswith("--") else "M4"
    e = json.load(open(src))
    if "--project" in sys.argv:
        e["project"] = sys.argv[sys.argv.index("--project") + 1]
    e["style"].update(STYLES[look]); e["style"].update({"accent": HALDI, "cap_color": CREAM})
    caps = e["captions"]
    # hero keywords (M4 brush): longest-held keyword group in each 12 s window, at most 4, never a negative word
    hero = set()
    if look == "M4":
        win = {}
        for i, c in enumerate(caps):
            ks = [w for w in c["words"] if w[2] == "k"]
            if not ks or bare(ks[0][1]) in NEG: continue
            d = c["t1"] - ks[0][0]
            if d >= 0.9:
                b = int(c["t0"] // 12)
                if b not in win or d > win[b][0]: win[b] = (d, i)
        hero = {i for _, i in sorted(win.values(), reverse=True)[:4]}
    last_dot = -99.0
    for i, c in enumerate(caps):
        nxt = caps[i + 1]["t0"] if i + 1 < len(caps) else c["t1"] + 1
        new = []
        for w in c["words"]:
            o = dict(w[3]) if len(w) > 3 else {}
            role = o.pop("role", None)
            for kx in ("fx", "c", "bar"):
                o.pop(kx, None)
            neg = role == "neg" or bare(w[1]) in NEG
            if look == "M2":                                   # one line of caps; colour rides on the word itself
                col = KUMKUM if neg else (HALDI if w[2] == "k" or role == "key" else None)
                new.append([w[0], w[1].upper(), "n"] + ([{"c": col}] if col else []))
                continue
            if w[2] == "n":
                txt = w[1].upper() if look == "M1" else w[1].lower()
                new.append([w[0], txt] + (["n", {"c": KUMKUM}] if neg else ["n"]))
                continue
            o["c"] = KUMKUM if neg else HALDI
            if look == "M4":
                o["glow"] = 0.0 if neg else 0.25
                if (i in hero or role == "hero") and not neg:
                    o["c"], o["brush"], o["glow"] = CREAM, HALDI, 0.0
                end = nxt - c["t1"] >= 0.35 or role == "dot"
                if end and not w[1].rstrip()[-1:] in "?!.," and c["t1"] - w[0] >= 0.5 and w[0] - last_dot >= 8.0 and role != "nodot":
                    o["dot"] = KUMKUM; last_dot = w[0]
            new.append([w[0], w[1].lower(), "k", o])
        c["words"] = new
    json.dump(e, open(out, "w"), indent=1)
    n_k = sum(1 for c in caps for w in c["words"] if len(w) > 3 and w[3].get("c") == KUMKUM)
    n_b = sum(1 for c in caps for w in c["words"] if len(w) > 3 and w[3].get("brush"))
    n_d = sum(1 for c in caps for w in c["words"] if len(w) > 3 and w[3].get("dot"))
    print(f"{look}: {len(caps)} groups, red words {n_k}, brush {n_b}, dots {n_d} -> {out}")


if __name__ == "__main__":
    main()
