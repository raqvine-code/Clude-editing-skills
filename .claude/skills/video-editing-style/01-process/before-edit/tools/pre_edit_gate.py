#!/usr/bin/env python3
"""Pre-edit gate: checks a shortkit EDL (draft or final) against the pro-editor floor in `01-process/before-edit/2-PRO-MOVE-MENU.md`.
Run it on the DRAFT edl.json before any full render, and again before delivery. Any FAIL = the edit is not ready.

  python3 "01-process/before-edit/tools/pre_edit_gate.py" <project>/edl.json [--facts <project>/analysis/facts.json]

Counts (from the EDL keys of 02-craft/shorts-editing-pro/tools/shortkit.py):
- footage B-roll      = broll slots from stock / library files
- designed motion gfx = broll slots rendered from <project>/assets/scenes/ (or key prefix mg_ / scene_ / hl_ / mc_), plus
                        layers, paper, dims (on-screen UI band), mirror, desat. brackets (ring / HUD) count as light MG.
                        NOT counted (2026-11-27): layers keyed txt_ (text moves) and dims with amt >= 0.99 (focus pulls).
- HL / MC             = text highlight + match cut (my-editing-rules 11): a slot / layer key starting hl_ / mc_, or
                        edl["meta"]["hl"] / ["mc"]; edl["meta"]["skip_hl"] = "reason" accepts a written skip.
- text devices        = stacks + giants (running caption groups are listed separately: they are the subtitle layer, not MG)
- event gaps          = camera keys, inserts, caption words, stack tokens, giants, plus edl["meta"]["mg_events"]: the beats the
                        scene builder animates INSIDE a scene clip or layer (a row ticks, a bar fills, a cursor taps), 2026-11-26
Made 2026-11-26 after video 25 (client not impressed: text on footage, only 11 % designed motion graphics, no HL / MC)."""
import json, sys, os, re

def load(p): return json.load(open(p))

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    edl_p = sys.argv[1]; e = load(edl_p); proj = e.get("project") or os.path.dirname(os.path.abspath(edl_p))
    facts = None
    if "--facts" in sys.argv: facts = load(sys.argv[sys.argv.index("--facts") + 1])
    elif os.path.exists(os.path.join(proj, "analysis", "facts.json")): facts = load(os.path.join(proj, "analysis", "facts.json"))
    keeps = e["keeps"]; OUT = sum(b - a for a, b in keeps)
    def s2o(t):                                              # source second -> output second (None if cut)
        o = 0.0
        for a, b in keeps:
            if a <= t <= b: return o + t - a
            o += b - a
        return None
    meta = e.get("meta", {})
    is_mg_key = lambda k: re.match(r"^(mg|scene|hl|mc)_", k or "") is not None
    br = e.get("broll", [])
    scene_slots = [b for b in br if "/assets/scenes/" in (b.get("file") or "") or is_mg_key(b.get("key"))]
    footage = [b for b in br if b not in scene_slots]
    heavy = [(b["t0"], b["t1"], "scene:" + b["key"]) for b in scene_slots]
    # 2026-11-27 (editor-showcase-caption-edit-style 6): a layer whose key starts txt_ is a TEXT MOVE (write-on, pill, converge,
    # word-only type card) and a dims entry with amt >= 0.99 is a focus pull, not an on-screen-UI band: neither is designed MG.
    txt_layers = [x for x in e.get("layers", []) if (x.get("key") or "").startswith("txt_")]
    heavy += [(x["t0"], x["t1"], "layer:" + x.get("key", "")) for x in e.get("layers", []) if x not in txt_layers]
    heavy += [(x["t0"], x["t1"], "paper") for x in e.get("paper", [])]
    heavy += [(x["t0"], x["t1"], "dims/UI") for x in e.get("dims", []) if x.get("amt", 0.46) < 0.99]
    heavy += [(x["t0"], x["t1"], "mirror") for x in e.get("mirror", [])]
    heavy += [(x["t0"], x["t1"], "desat") for x in e.get("desat", [])]
    light = [(x["t0"], x["t1"], "ring" if x.get("shape") == "ring" else "HUD") for x in e.get("brackets", [])]
    def union(iv):
        iv = sorted((a, b) for a, b, _ in iv); tot = 0.0; cur = None
        for a, b in iv:
            if cur and a <= cur[1]: cur[1] = max(cur[1], b)
            else:
                if cur: tot += cur[1] - cur[0]
                cur = [a, b]
        return tot + (cur[1] - cur[0] if cur else 0.0)
    mg_all = sorted(heavy + light)
    mg_share = 100 * union(heavy) / OUT
    starts = [0.0] + sorted(a for a, _, _ in mg_all) + [OUT]
    mg_gap = max(b - a for a, b in zip(starts, starts[1:]))
    keys = [b.get("key", "") for b in br] + [x.get("key", "") for x in e.get("layers", [])]
    hl = any(k.startswith("hl_") for k in keys) or bool(meta.get("hl"))
    mc = any(k.startswith("mc_") for k in keys) or bool(meta.get("mc"))
    png = [k for k in keys if k.startswith("png_")]
    stacks, giants, caps = e.get("stacks", []), e.get("giants", []), e.get("captions", [])
    # fonts in use (families = file name before the first "-")
    st = e.get("style", {}); fonts = set()
    for k in ("cap_font", "key_font", "giant_font", "serif_font", "stack_font", "stack_small_font", "script_font", "mono_font"):
        if st.get(k): fonts.add(os.path.basename(st[k]))
    for g in giants:
        if g.get("font"): fonts.add(os.path.basename(g["font"]))
    for s in stacks:
        for ln in s["lines"]:
            for tk in ln:
                if len(tk) > 3 and tk[3].get("font") and tk[3]["font"] not in ("serif", "script"): fonts.add(os.path.basename(tk[3]["font"]))
    if st.get("mono_font") and not any(b.get("label") for b in e.get("brackets", [])):
        fonts.discard(os.path.basename(st["mono_font"]))          # the mono font only counts when a HUD label is drawn
    fam = sorted({re.split(r"[-_]", f)[0] for f in fonts if f})
    above = [g for g in giants if g.get("y", 999) < 700] + [s for s in stacks if s.get("y", 999) < 700]
    # events (for gaps and pauses)
    cam_t = [k[0] for k in e.get("camera", [])]
    ins_t = [b["t0"] for b in br] + [a for a, _, _ in mg_all] + [f["t"] for f in e.get("flashes", [])]
    txt_t = [w[0] for c in caps for w in c["words"]] + [tk[0] for s in stacks for ln in s["lines"] for tk in ln] + [g["t0"] for g in giants]
    scn_t = [float(t) for t in meta.get("mg_events", [])]                  # beats INSIDE built scenes / layers (row ticks, bar fill, cursor tap)
    ev = sorted(set(round(t, 2) for t in cam_t + ins_t + txt_t + scn_t if 0 <= t <= OUT))
    gaps = [(round(b - a, 2), a) for a, b in zip(ev, ev[1:]) if b - a > 1.3]
    sfx_t = [c["t"] for c in e.get("sfx", [])]
    no_sound = [round(t, 2) for t in sorted(set(round(x, 3) for x in ins_t)) if not any(abs(s - t) <= 0.15 for s in sfx_t)]
    pauses, bare = [], []
    if facts:
        for a, b in facts.get("silences", []):
            oa, ob = s2o(a), s2o(b)
            if oa is None or ob is None or ob - oa < 0.5 or oa < 0.2 or ob > OUT - 0.2: continue
            pauses.append((oa, ob))
            move = any(oa - 0.1 <= t <= ob + 0.1 for t in cam_t + ins_t + scn_t + [tk[0] for s in stacks for ln in s["lines"] for tk in ln])
            snd = any(oa - 0.1 <= t <= ob + 0.1 for t in sfx_t)
            if not (move and snd): bare.append((round(oa, 2), round(ob, 2), "move" if not move else "sound"))
    rows = []
    def row(name, ok, val, target, look=False):
        rows.append(("PASS" if ok else ("LOOK" if look else "FAIL"), name, val, target))
    need_mg = max(1, int(OUT // 8))
    row("Designed motion graphics (events)", len(mg_all) >= need_mg, "%d (%d heavy, %d ring/HUD)" % (len(mg_all), len(heavy), len(light)), ">= %d (one per 8 s)" % need_mg)
    row("Designed MG share of runtime", mg_share >= 25, "%.0f %%" % mg_share, ">= 25 % (P10/P11 28-41 %, P15 ~100 %)")
    row("Longest stretch with no designed MG", mg_gap <= 9, "%.1f s" % mg_gap, "<= 9 s")
    row("Text highlight (HL)", hl or bool(meta.get("skip_hl")), "yes" if hl else ("skipped: " + meta["skip_hl"] if meta.get("skip_hl") else "missing"), "1+ (my-editing-rules 11)")
    row("Match cut (MC)", mc or bool(meta.get("skip_mc")), "yes" if mc else ("skipped: " + meta["skip_mc"] if meta.get("skip_mc") else "missing"), "1+ (my-editing-rules 11)")
    row("Footage B-roll", len(footage) >= max(4, int(OUT // 7)), "%d slots, %.0f %% of runtime" % (len(footage), 100 * sum(b["t1"] - b["t0"] for b in footage) / OUT), ">= %d, <= 50 %%" % max(4, int(OUT // 7)))
    row("Event gaps over 1.3 s", not gaps, str(gaps[:6]) if gaps else "none", "none", look=len(gaps) <= 2)
    row("Pauses >= 0.5 s carrying a move AND a sound", not bare, ("%d of %d bare: %s" % (len(bare), len(pauses), bare[:6])) if facts else "no facts.json", "all", look=len(bare) <= 2)
    row("Inserts with a sound within 0.15 s", not no_sound, str(no_sound[:8]) if no_sound else "all", "all")
    row("Font families", len(fam) <= 2, ", ".join(fam), "<= 2")
    row("Above-head accents", len(above) <= 3, str(len(above)), "1-3")
    row("Text devices (stacks + giants + txt_ layers)", True, "%d (running caption groups: %d)" % (len(stacks) + len(giants) + len(txt_layers), len(caps)), "info: text is not MG (mistakes 16)")
    row("PNG pop-ups", True, str(len(png)), "info: 0-3 where an object is named (png-library)")
    print("PRE-EDIT GATE  %s  (%.2f s)" % (os.path.basename(proj), OUT))
    for r in rows: print("  [%s] %-44s %-34s target %s" % r)
    print("  designed MG list:", [(round(a, 2), round(b, 2), n) for a, b, n in mg_all])
    fails = [r for r in rows if r[0] == "FAIL"]
    print("RESULT:", "READY" if not fails else "NOT READY (%d FAIL)" % len(fails))
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
