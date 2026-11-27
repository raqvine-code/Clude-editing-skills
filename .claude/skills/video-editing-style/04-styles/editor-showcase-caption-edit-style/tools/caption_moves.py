#!/usr/bin/env python3
"""caption_moves.py - renders the caption / card moves of profiles P17-P20 as RGBA frame folders for shortkit `layers`.

    python3 caption_moves.py SPEC.json OUT_DIR [--sheet]

Each move in the spec becomes OUT_DIR/<key>/00001.png ... (RGBA 1080x1920, 1-based), ready for an EDL entry
    {"key": "<key>", "dir": "<OUT_DIR>/<key>", "t0": <start>, "t1": <start + dur>, "behind": false}
--sheet also writes OUT_DIR/<key>_sheet.jpg (every 3rd frame on a dark plate) so the move can be checked before a render.
Times inside a move are seconds from the move's own start. Leave no `captions` group under a move (the move carries the words).

SPEC = {"fps": 30, "fonts": {"bold": ".../Poppins-ExtraBold.ttf", "sans": ".../Poppins-SemiBold.ttf",
                             "script": ".../GreatVibes-Regular.ttf", "caps": ".../BebasNeue-Regular.ttf"},
        "moves": [ ... ]}
Font values are absolute paths, or paths relative to the spec file. A move may name another font with "font": "<key or path>".

kinds (numbers are the measured defaults from references/reel-notes-R5-R8.md):
  writeon  (P20)  script phrase uncovered left to right through a soft blur, small sans words beside it
      {"key","kind":"writeon","dur":1.2,"x":540,"y":1130,"script":{"text":"If you look","size":170,"color":"#FFFFFF","opacity":0.9,"wipe":0.5,"t":0.0},
       "small":{"words":[[0.0,"at"],[0.17,"your"],[0.37,"edits"]],"size":44,"pos":"under-right|over-left","color":"#FFFFFF"}}
  pill     (P18)  dark full-radius pills with a glow blob, wiping in left to right, stacked
      {"key","kind":"pill","dur":1.8,"x":540,"y":1150,"size":52,"items":[{"text":"THE INSECURITIES","t":0.0},{"text":"THE FLAWS","t":0.9}],
       "fill":"#130C05","text":"#F9E1CB","glow":"#DF622C","wipe":0.2,"gap":14}
  converge (P18)  two hero words slide in from the left and right edges with motion blur; a small word fades in between
      {"key","kind":"converge","dur":1.1,"y":1130,"size":190,"color":"#F29656","move":0.3,
       "left":{"text":"NINE","x":300},"right":{"text":"TEN TIMES","x":740},"mid":{"text":"out of","t":0.33,"x":470,"size":40,"color":"#FFFFFF"}}
  typecard (P17)  full-frame colour plate + hero word (ghost to solid) + tiny lines; hard colour inversions; optional window
                  (a transparent rounded hole that closes in from full frame, so the live speaker sits inside a card)
      {"key","kind":"typecard","dur":1.75,"bg":"#0F4232","fg":"#FFFFFF","invert":[[0.38,0.88]],
       "hero":{"text":"Wins","width":0.78,"y":1000,"t":0.0},
       "lines":[{"text":"Every single","t":0.40,"pos":"over-left"},{"text":"time.","t":0.90,"pos":"under-right"}],
       "window":{"rect":[190,300,890,1000],"radius":48,"shrink":0.25}}
  tiles    (P20)  numbered diamond tiles pop one by one (ghost, then lit); one flies to a new spot with rotation, the rest fade
      {"key","kind":"tiles","dur":2.9,"x":540,"y":1290,"n":3,"size":120,"gap":44,"fill":"#0A2DB4","rim":"#4466F0","text":"#FFFFFF",
       "pop":[0.5,0.7,1.03],"fly":{"i":0,"t":1.5,"dur":0.55,"to":[250,1150],"rot":-200},"fade_others":[1.83,0.2]}
"""
import sys, os, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
out3 = lambda p: 1 - (1 - min(1.0, max(0.0, p))) ** 3
smooth = lambda p: (lambda q: q * q * (3 - 2 * q))(np.clip(p, 0, 1))
hexrgb = lambda h: np.array([int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255


def sprite(text, font, size, color, glow=0.0):
    """straight-alpha RGBA float sprite of one text run, tight to the ink plus padding"""
    f = ImageFont.truetype(font, int(size)); pad = int(size * 0.45) + 8
    l, t, r, b = f.getbbox(text)
    im = Image.new("L", (r - l + 2 * pad, b - t + 2 * pad), 0)
    ImageDraw.Draw(im).text((pad - l, pad - t), text, font=f, fill=255)
    a = np.asarray(im, np.float32) / 255
    if glow: a = np.clip(a + glow * np.asarray(im.filter(ImageFilter.GaussianBlur(size * 0.12)), np.float32) / 255, 0, 1)
    sp = np.zeros(a.shape + (4,), np.float32); sp[..., :3] = hexrgb(color); sp[..., 3] = a
    return sp


def fit(text, font, width_px, color, glow=0.0):
    """sprite whose ink is width_px wide (the hero word is sized to the frame, not to a point size)"""
    f = ImageFont.truetype(font, 200); l, t, r, b = f.getbbox(text)
    return sprite(text, font, 200 * width_px / max(1, r - l), color, glow)


def ink(sp):
    """ink box (x0, y0, x1, y1) inside a sprite"""
    ys, xs = np.where(sp[..., 3] > 0.5)
    return (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1) if len(xs) else (0, 0, sp.shape[1], sp.shape[0])


def blur(sp, rx, ry=None):
    im = Image.fromarray((np.clip(sp, 0, 1) * 255).astype(np.uint8), "RGBA")
    if ry is None: return np.asarray(im.filter(ImageFilter.GaussianBlur(rx)), np.float32) / 255
    a = np.asarray(im.split()[3].filter(ImageFilter.BoxBlur((rx, ry))), np.float32) / 255     # directional (motion) blur on alpha only
    out = sp.copy(); out[..., 3] = a; return out


def put(cv, sp, cx, cy, alpha=1.0, mask=None):
    """composite a straight-alpha sprite, centred on (cx, cy), over the premultiplied canvas"""
    h, w = sp.shape[:2]; x0, y0 = int(round(cx - w / 2)), int(round(cy - h / 2))
    a = sp[..., 3] * alpha
    if mask is not None: a = a * mask
    sx0, sy0 = max(0, -x0), max(0, -y0); sx1, sy1 = min(w, W - x0), min(h, H - y0)
    if sx1 <= sx0 or sy1 <= sy0: return
    a = a[sy0:sy1, sx0:sx1, None]; c = sp[sy0:sy1, sx0:sx1, :3]
    d = cv[y0 + sy0:y0 + sy1, x0 + sx0:x0 + sx1]
    d[..., :3] = c * a + d[..., :3] * (1 - a); d[..., 3:4] = a + d[..., 3:4] * (1 - a)


def rrect(w, h, r, ss=3):
    im = Image.new("L", (w * ss, h * ss), 0)
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], radius=int(r * ss), fill=255)
    return np.asarray(im.resize((w, h), Image.LANCZOS), np.float32) / 255


class Kit:
    def __init__(s, spec, base):
        s.fps = spec.get("fps", 30)
        s.fonts = {k: (v if os.path.isabs(v) else os.path.join(base, v)) for k, v in spec.get("fonts", {}).items()}
        s.base = base

    def font(s, m, role):
        v = m.get("font") if isinstance(m, dict) and m.get("font") else role
        if v in s.fonts: return s.fonts[v]
        if os.path.isabs(v) or os.path.exists(os.path.join(s.base, v)): return v if os.path.isabs(v) else os.path.join(s.base, v)
        sys.exit("font '%s' is not in spec.fonts and is not a file" % v)

    # ---- P20: script phrase written on through a blur, small sans words beside it
    def writeon(s, m):
        sc = m["script"]; sp = sprite(sc["text"], s.font(sc, "script"), sc.get("size", 170), sc.get("color", "#FFFFFF"), glow=sc.get("glow", 0.25))
        sp[..., 3] *= sc.get("opacity", 0.9); soft = blur(sp, sc.get("size", 170) * 0.06)
        h, w = sp.shape[:2]; x0, y0, x1, y1 = ink(sp); e = (x1 - x0) * 0.20; xs = np.arange(w, dtype=np.float32)[None, :]
        sm = m.get("small"); words = []
        if sm:
            f = s.font(sm, "sans"); sz = sm.get("size", 44); gap = sz * 0.28
            sps = [sprite(t_w[1], f, sz, sm.get("color", "#FFFFFF")) for t_w in sm["words"]]
            boxes = [ink(q) for q in sps]; tot = sum(b[2] - b[0] for b in boxes) + gap * (len(sps) - 1)
            cx, cy = m.get("x", W / 2), m.get("y", 1130)
            left = cx - w / 2 + x0; right = cx - w / 2 + x1
            if sm.get("pos", "under-right") == "under-right": xx, yy = right - tot, cy - h / 2 + y1 + sz * 0.55
            else: xx, yy = left, cy - h / 2 + y0 - sz * 0.55
            for (t_w, q, b) in zip(sm["words"], sps, boxes):
                words.append((t_w[0], q, xx + (b[2] - b[0]) / 2 + (q.shape[1] / 2 - (b[0] + b[2]) / 2), yy)); xx += b[2] - b[0] + gap

        def frame(cv, t):
            p = (t - sc.get("t", 0.0)) / sc.get("wipe", 0.5)
            if p > 0:
                c1 = x0 - e + min(1.0, p) * (x1 - x0 + 3 * e); m1 = smooth((c1 - xs) / e + 0.5); m2 = smooth((c1 - e - xs) / e + 0.5)
                put(cv, soft, m.get("x", W / 2), m.get("y", 1130), 0.7, mask=(m1 - m2)); put(cv, sp, m.get("x", W / 2), m.get("y", 1130), 1.0, mask=m2)
            for (tw, q, qx, qy) in words:
                if t >= tw: put(cv, q, qx, qy, out3((t - tw) / 0.10))
        return frame

    # ---- P18: stacked dark pills with a glow blob, wiping in left to right
    def pill(s, m):
        sz = m.get("size", 52); f = s.font(m, "bold"); padx, pady = sz * 0.75, sz * 0.42; items = []
        y = m.get("y", 1150)
        for it in m["items"]:
            tx = sprite(it["text"], f, sz, m.get("text", "#F9E1CB")); b = ink(tx)
            pw, ph = int(b[2] - b[0] + 2 * padx), int(sz * 0.74 + 2 * pady)
            body = np.zeros((ph, pw, 4), np.float32); body[..., :3] = hexrgb(m.get("fill", "#130C05")); body[..., 3] = rrect(pw, ph, ph / 2)
            gx = np.exp(-((np.arange(pw)[None, :] - pw * 0.10) / (pw * 0.22)) ** 2) * np.exp(-((np.arange(ph)[:, None] - ph * 0.85) / (ph * 0.55)) ** 2)
            body[..., :3] = body[..., :3] * (1 - 0.85 * gx[..., None]) + hexrgb(m.get("glow", "#DF622C")) * 0.85 * gx[..., None]
            halo = np.zeros((ph + 80, pw + 80, 4), np.float32); halo[..., :3] = hexrgb(m.get("glow", "#DF622C"))
            halo[40:-40, 40:-40, 3] = body[..., 3] * 0.55; halo = blur(halo, 16)
            items.append((it.get("t", 0.0), body, tx, halo, y + ph / 2, pw, b)); y += ph + m.get("gap", 14)

        def frame(cv, t):
            for (t0, body, tx, halo, cy, pw, b) in items:
                if t < t0: continue
                p = out3((t - t0) / m.get("wipe", 0.2)); cx = m.get("x", W / 2)
                wm = (np.arange(body.shape[1])[None, :] < p * body.shape[1]).astype(np.float32)
                put(cv, halo, cx, cy, 0.6 * p); put(cv, body, cx, cy, 1.0, mask=wm)
                wt = (np.arange(tx.shape[1])[None, :] < b[0] + p * (b[2] - b[0]) + 4).astype(np.float32)
                put(cv, tx, cx + (tx.shape[1] / 2 - (b[0] + b[2]) / 2), cy + (tx.shape[0] / 2 - (b[1] + b[3]) / 2), p, mask=wt)
        return frame

    # ---- P18: two hero words converge from the frame edges with motion blur
    def converge(s, m):
        f = s.font(m, "caps"); sz = m.get("size", 190); mv = m.get("move", 0.3); parts = []
        for side, sign in (("left", -1), ("right", 1)):
            sp = sprite(m[side]["text"], f, sz, m[side].get("color", m.get("color", "#F29656")), glow=m.get("glow", 0.3))
            start = -sp.shape[1] / 2 if sign < 0 else W + sp.shape[1] / 2
            parts.append((sp, start, m[side]["x"]))
        mid = m.get("mid"); msp = sprite(mid["text"], s.font(mid, "sans"), mid.get("size", 40), mid.get("color", "#FFFFFF")) if mid else None

        def frame(cv, t):
            for (sp, a, b) in parts:
                p = out3(t / mv); x = a + (b - a) * p; v = abs((b - a) * 3 * (1 - min(1.0, t / mv)) ** 2 / mv) / s.fps
                put(cv, blur(sp, min(60, v * 0.5), 0) if v > 3 else sp, x, m.get("y", 1130))
            if mid and t >= mid.get("t", mv): put(cv, msp, mid.get("x", W / 2), mid.get("y", m.get("y", 1130) - sz * 0.42), out3((t - mid.get("t", mv)) / 0.12))
        return frame

    # ---- P17: full-frame type card with hard colour inversions and an optional speaker window
    def typecard(s, m):
        hero = m["hero"]; fb = s.font(hero, "bold"); fs = s.font(m, "sans"); cache = {}
        yy_, xx_ = np.mgrid[0:H, 0:W].astype(np.float32)

        def build(fg):
            hs = fit(hero["text"], fb, hero.get("width", 0.78) * W, fg); b = ink(hs); hh = b[3] - b[1]; ls = []
            cy = hero.get("y", 1000); left = W / 2 - (b[2] - b[0]) / 2; right = W / 2 + (b[2] - b[0]) / 2
            for ln in m.get("lines", []):
                q = sprite(ln["text"], s.font(ln, "sans") if ln.get("font") else fs, ln.get("size", hh * 0.20), fg); qb = ink(q)
                if ln.get("pos", "over-left") == "over-left": qx, qy = left + (qb[2] - qb[0]) / 2 + 8, cy - hh / 2 - (qb[3] - qb[1]) * 0.9 - hh * 0.06
                else: qx, qy = right - (qb[2] - qb[0]) / 2 - 8, cy + hh / 2 + (qb[3] - qb[1]) * 0.9 + hh * 0.06
                ls.append((ln.get("t", 0.0), q, qx + (q.shape[1] / 2 - (qb[0] + qb[2]) / 2), qy + (q.shape[0] / 2 - (qb[1] + qb[3]) / 2)))
            return hs, ls, cy + (hs.shape[0] / 2 - (b[1] + b[3]) / 2), W / 2 + (hs.shape[1] / 2 - (b[0] + b[2]) / 2)

        def frame(cv, t):
            inv = any(a <= t < b for a, b in m.get("invert", []))
            bg, fg = (m.get("fg", "#FFFFFF"), m["bg"]) if inv else (m["bg"], m.get("fg", "#FFFFFF"))
            if fg not in cache: cache[fg] = build(fg)
            hs, ls, hy, hx = cache[fg]
            cv[..., :3] = hexrgb(bg); cv[..., 3] = 1.0
            th = hero.get("t", 0.0)
            if t >= th:
                p = out3((t - th) / 0.20); put(cv, hs, hx, hy + 10 * (1 - p), 0.35 + 0.65 * p)
            for (tl, q, qx, qy) in ls:
                if t >= tl: put(cv, q, qx, qy, out3((t - tl) / 0.12))
            wn = m.get("window")
            if wn:                                                # hole: full frame -> card rect, so the plate closes in round the speaker
                p = out3(t / wn.get("shrink", 0.25)); r = wn["rect"]
                x0, y0, x1, y1 = r[0] * p, r[1] * p, W + (r[2] - W) * p, H + (r[3] - H) * p; rad = max(1.0, wn.get("radius", 48) * p)
                dx = np.maximum(np.maximum(x0 + rad - xx_, xx_ - (x1 - rad)), 0); dy = np.maximum(np.maximum(y0 + rad - yy_, yy_ - (y1 - rad)), 0)
                inside = np.clip(rad - np.sqrt(dx * dx + dy * dy) + 0.5, 0, 1) * ((xx_ >= x0) & (xx_ <= x1) & (yy_ >= y0) & (yy_ <= y1))
                cv *= (1 - inside)[..., None]
        return frame

    # ---- P20: numbered diamond tiles (list device)
    def tiles(s, m):
        n, sz, gap = m.get("n", 3), m.get("size", 120), m.get("gap", 44); f = s.font(m, "bold"); ts = []
        for i in range(n):
            d = int(sz * 1.5); im = np.zeros((d, d, 4), np.float32); body = rrect(sz, sz, sz * 0.16); o = (d - sz) // 2
            im[o:o + sz, o:o + sz, :3] = hexrgb(m.get("fill", "#0A2DB4")); im[o:o + sz, o:o + sz, 3] = body
            rim = body - np.pad(rrect(sz - 10, sz - 10, sz * 0.14), 5); rim = np.clip(rim, 0, 1)[..., None]
            im[o:o + sz, o:o + sz, :3] = im[o:o + sz, o:o + sz, :3] * (1 - rim) + hexrgb(m.get("rim", "#4466F0")) * rim
            pil = Image.fromarray((im * 255).astype(np.uint8), "RGBA").rotate(45, resample=Image.BICUBIC)
            num = sprite(str(i + 1), f, sz * 0.62, m.get("text", "#FFFFFF")); nb = ink(num)
            ts.append((pil, num, (num.shape[1] / 2 - (nb[0] + nb[2]) / 2, num.shape[0] / 2 - (nb[1] + nb[3]) / 2)))
        step = sz * 1.42 + gap; xs0 = [m.get("x", W / 2) + (i - (n - 1) / 2) * step for i in range(n)]
        fly = m.get("fly"); fo = m.get("fade_others")

        def frame(cv, t):
            for i, (pil, num, off) in enumerate(ts):
                t0 = m["pop"][i]
                if t < t0: continue
                lit = t - t0 >= 0.099; a = 1.0 if lit else 0.35; sc = 1 + 0.15 * (1 - out3((t - t0 - 0.10) / 0.12)) if lit else 1.0
                x, y, rot = xs0[i], m.get("y", 1290), 0.0
                if fly and fly["i"] == i and t >= fly["t"]:
                    p = out3((t - fly["t"]) / fly.get("dur", 0.55)); x += (fly["to"][0] - x) * p; y += (fly["to"][1] - y) * p - 60 * np.sin(np.pi * p)
                    rot = fly.get("rot", -200) * (1 - p)
                elif fo and t >= fo[0]: a *= max(0.0, 1 - (t - fo[0]) / fo[1])
                if a <= 0: continue
                im = pil.rotate(rot, resample=Image.BICUBIC) if rot else pil
                if sc != 1.0: im = im.resize((int(im.width * sc), int(im.height * sc)), Image.BICUBIC)
                sh = np.zeros((im.height, im.width, 4), np.float32); sh[..., 3] = np.asarray(im.split()[3].filter(ImageFilter.GaussianBlur(10)), np.float32) / 255 * 0.45
                put(cv, sh, x, y + 14, a); put(cv, np.asarray(im, np.float32) / 255, x, y, a); put(cv, num, x + off[0], y + off[1], a)
        return frame


def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    spec = json.load(open(sys.argv[1])); out = sys.argv[2]; kit = Kit(spec, os.path.dirname(os.path.abspath(sys.argv[1])))
    for m in spec["moves"]:
        fn = getattr(kit, m["kind"])(m); n = int(round(m["dur"] * kit.fps)); d = os.path.join(out, m["key"]); os.makedirs(d, exist_ok=True); thumbs = []
        for j in range(n):
            cv = np.zeros((H, W, 4), np.float32); fn(cv, j / kit.fps)
            a = cv[..., 3:4]; rgb = np.where(a > 1e-4, cv[..., :3] / np.maximum(a, 1e-4), 0)       # un-premultiply for the PNG
            Image.fromarray((np.clip(np.concatenate([rgb, a], 2), 0, 1) * 255 + 0.5).astype(np.uint8), "RGBA").save(os.path.join(d, "%05d.png" % (j + 1)), compress_level=3)
            if "--sheet" in sys.argv and j % 3 == 0:
                bgp = np.empty((H, W, 3), np.float32); bgp[:] = np.linspace(0.30, 0.16, H)[:, None, None] * np.array([0.9, 1.0, 1.25])
                fr = Image.fromarray(((cv[..., :3] + bgp * (1 - a)).clip(0, 1) * 255).astype(np.uint8)).resize((216, 384), Image.LANCZOS)
                ImageDraw.Draw(fr).text((6, 4), "f%d %.2fs" % (j, j / kit.fps), fill=(255, 235, 120)); thumbs.append(fr)
        if thumbs:
            cols = min(10, len(thumbs)); rows = -(-len(thumbs) // cols); sheet = Image.new("RGB", (cols * 216, rows * 384), (20, 20, 20))
            for i, fr in enumerate(thumbs): sheet.paste(fr, ((i % cols) * 216, (i // cols) * 384))
            sheet.save(os.path.join(out, m["key"] + "_sheet.jpg"), quality=88)
        print("%-10s %-9s %3d frames -> %s" % (m["key"], m["kind"], n, d))


if __name__ == "__main__":
    main()
