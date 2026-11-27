"""Technique test render for profile P1 (Glass Spotlight): rebuilds the f00ae5949170 statement build with the
library frame counts, on an abstract background (no reference footage).  usage: render_p1_test.py out.mp4 [lead] [accent] [word1] [word2] [slide]
Techniques: X1 blur-in (f0-2), M1 glass frame scale-in (f2-9), M2 sparkle pops (f4-8), T3 type-on (f11-17),
T2 keyword slam with motion blur (f26-30), T5 accent write-on + glow decay (f27-34), swap smear + M4 circle (f60-74),
X2 whip (f80-88)."""
import sys, os, math, subprocess, tempfile, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refscan import FF

W, H, FPS, N = 720, 1280, 30, 100
LIME = (205, 240, 60)
out = sys.argv[1]
LEAD, ACC, K1, K2, SLIDE = (sys.argv[2:7] + ["You're not", "competing on", "price", "value", "show"][len(sys.argv[2:7]):])[:5]


def font(cands, size):
    for c in cands:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


SUP = "/System/Library/Fonts/Supplemental/"
def face(path, size, index, fallback):
    try:
        return ImageFont.truetype(path, size, index=index)
    except Exception:
        return font(fallback, size)


# lead = light grotesk, accent = script, keyword = heavy geometric (Avenir Next Heavy ~ Inter Black / Satoshi Black)
F_LEAD = face("/System/Library/Fonts/HelveticaNeue.ttc", 40, 7, [SUP + "Arial.ttf"])
F_ACC = font([SUP + "SnellRoundhand.ttc", SUP + "Georgia Italic.ttf"], 64)
F_KEY = face("/System/Library/Fonts/Avenir Next.ttc", 196, 8, [SUP + "Arial Black.ttf"])

ease_out = lambda t: 1 - (1 - max(0, min(1, t))) ** 4          # quart out
expo_out = lambda t: 1 if t >= 1 else 1 - 2 ** (-10 * max(0, t))
prog = lambda f, a, b: (f - a) / max(1, (b - a))


def background():
    bg = Image.new("RGB", (W, H), (8, 8, 9))
    g = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(g)
    for r in range(520, 0, -8):  # spotlight cone + floor pool
        d.ellipse((W / 2 - r * 0.9, H * 0.78 - r * 0.22, W / 2 + r * 0.9, H * 0.78 + r * 0.22), fill=int(70 * (1 - r / 520)))
    d.polygon([(W / 2 - 40, 0), (W / 2 + 40, 0), (W / 2 + 330, H * 0.8), (W / 2 - 330, H * 0.8)], fill=26)
    g = g.filter(ImageFilter.GaussianBlur(40))
    return Image.composite(Image.new("RGB", (W, H), (210, 210, 205)), bg, g)


BG = background()


def text_layer(txt, fnt, fill, anchor_xy, alpha=255):
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(L).text(anchor_xy, txt, font=fnt, fill=fill + (alpha,), anchor="mm")
    return L


def key_layer(word, fnt, xy, alpha=255, col=(245, 245, 245)):
    """Keyword with an accent-coloured full stop (T1), tracking -3 %."""
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(L)
    trk = -0.03 * fnt.size
    widths = [d.textlength(c, font=fnt) + trk for c in word]
    total = sum(widths) + d.textlength(".", font=fnt)
    x = xy[0] - total / 2
    for c, w in zip(word, widths):
        d.text((x, xy[1]), c, font=fnt, fill=col + (alpha,), anchor="lm")
        x += w
    d.text((x, xy[1]), ".", font=fnt, fill=LIME + (alpha,), anchor="lm")
    return L


def motion_blur_layer(make, x0, x1, samples=None):
    samples = samples or max(8, int(abs(x1 - x0) / 5))
    acc = None
    for i in range(samples):
        L = make(x0 + (x1 - x0) * i / (samples - 1))
        acc = L if acc is None else Image.blend(acc, L, 1 / (i + 1))
    return acc


def glass(scale, alpha):
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if scale <= 0:
        return L
    w, h = 420 * scale, 760 * scale
    box = (W / 2 - w / 2, 120 + (760 - h) / 2, W / 2 + w / 2, 120 + (760 + h) / 2)
    d = ImageDraw.Draw(L)
    d.rounded_rectangle(box, radius=70 * scale, fill=(255, 255, 255, int(18 * alpha)), outline=(255, 255, 255, int(70 * alpha)), width=2)
    d.rounded_rectangle((W / 2 - 40 * scale, box[1] + 26 * scale, W / 2 + 40 * scale, box[1] + 38 * scale), radius=6, fill=(255, 255, 255, int(230 * alpha)))
    return L


def sparkle(L, xy, s, rot, col):
    d = ImageDraw.Draw(L)
    for a in (0, 90):
        ang = math.radians(rot + a)
        dx, dy = math.cos(ang) * s, math.sin(ang) * s
        d.line((xy[0] - dx, xy[1] - dy, xy[0] + dx, xy[1] + dy), fill=col + (255,), width=max(3, int(s / 2.6)))


def frame(f):
    im = BG.copy().convert("RGBA")
    if f < 85:
        im.alpha_composite(glass(0.85 + 0.15 * expo_out(prog(f, 2, 9)) if f >= 2 else 0, min(1, prog(f, 2, 9)) if f < 62 else max(0, 1 - prog(f, 62, 67))))
        sp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for (x, y, d0) in ((585, 300, 4), (150, 250, 5), (180, 640, 6)):
            t = prog(f, d0, d0 + 4)
            s = 0 if t <= 0 else (34 * (1.2 * t / 0.7) if t < 0.7 else 34 * (1.2 - 0.2 * (t - 0.7) / 0.3)) if t < 1 else 34
            if s > 0:
                sparkle(sp, (x + math.sin(f / 9) * 4, y), s * (0.6 if d0 == 6 else 1), 45 + 15 * math.sin(f / 7), LIME)
        im.alpha_composite(sp)
        # lead line type-on (1 frame per char)
        n = max(0, min(len(LEAD), f - 10))
        if n and f < 82:
            im.alpha_composite(text_layer(LEAD[:n], F_LEAD, (235, 235, 235), (W / 2, 425)))
        # accent write-on with glow decay
        if 27 <= f < 82:
            t = min(1, prog(f, 27, 34))
            acc = text_layer(ACC, F_ACC, LIME if f < 40 else tuple(int(LIME[i] + (235 - LIME[i]) * min(1, prog(f, 40, 52))) for i in range(3)), (W / 2, 478))
            mask = Image.new("L", (W, H), 0)
            ImageDraw.Draw(mask).rectangle((0, 0, W / 2 - 160 + 330 * t, H), fill=255)
            acc.putalpha(ImageChops.multiply(acc.getchannel("A"), mask))
            glow_amt = max(0, 1 - prog(f, 34, 46))
            if glow_amt > 0:
                g = acc.filter(ImageFilter.GaussianBlur(12))
                g.putalpha(g.getchannel("A").point(lambda v: int(v * glow_amt)))
                im.alpha_composite(g)
            im.alpha_composite(acc)
        # keyword slam (f26-f30) / swap smear (f60-f64) / new keyword (f64-f66)
        if 26 <= f < 64:
            t = ease_out(prog(f, 26, 30))
            x_now, x_prev = -200 + (W / 2 + 200) * t, -200 + (W / 2 + 200) * ease_out(prog(f - 1, 26, 30))
            if f >= 60:
                x_prev, x_now = W / 2 + 120 * ease_out(prog(f - 1, 60, 64)), W / 2 + 120 * ease_out(prog(f, 60, 64))
            mk = lambda x: key_layer(K1, F_KEY, (x, 560), 255 if f < 60 else int(255 * (1 - prog(f, 60, 64))))
            im.alpha_composite(motion_blur_layer(mk, x_prev, x_now) if abs(x_now - x_prev) > 2 else mk(x_now))
        if f >= 64:
            sc = 1.06 - 0.06 * ease_out(prog(f, 64, 67))
            F2 = F_KEY.font_variant(size=int(196 * sc))
            im.alpha_composite(key_layer(K2, F2, (W / 2, 560), int(255 * min(1, prog(f, 63, 66)))))
            t = min(1, prog(f, 64, 74))
            fade = 1 - max(0, prog(f, 76, 82))
            if t > 0 and fade > 0:
                L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                ImageDraw.Draw(L).arc((W / 2 - 290, 380, W / 2 + 290, 690), start=200, end=200 + 360 * t, fill=LIME + (int(255 * fade),), width=5)
                im.alpha_composite(L)
        im = im.convert("RGB")
        if f < 3:
            im = im.filter(ImageFilter.GaussianBlur(20 * (1 - f / 3)))
        if 82 <= f < 85:  # whip out: scale up + blur
            k = prog(f, 82, 85)
            z = 1 + 0.25 * k
            im = im.resize((int(W * z), int(H * z))).crop((int(W * (z - 1) / 2), int(H * (z - 1) / 2), int(W * (z - 1) / 2) + W, int(H * (z - 1) / 2) + H)).filter(ImageFilter.BoxBlur(10 * k))
        return im
    # whip in: next slide enters from left with motion blur (f85-f88), then holds
    im = Image.new("RGBA", (W, H), (5, 5, 6, 255))
    t0, t1 = ease_out(prog(f - 1, 85, 88)), ease_out(prog(f, 85, 88))
    xa, xb = -300 + (W / 2 + 300) * t0, -300 + (W / 2 + 300) * t1
    F3 = F_KEY.font_variant(size=210)
    mk = lambda x: text_layer(SLIDE, F3, (240, 250, 200), (x, 640))
    im.alpha_composite(motion_blur_layer(mk, xa, xb) if abs(xb - xa) > 2 else mk(xb))
    im.alpha_composite(text_layer("Does your content", F_LEAD, (230, 230, 230), (W / 2 - 80, 540)))
    return im.convert("RGB")


tmp = tempfile.mkdtemp()
for f in range(N):
    frame(f).save(f"{tmp}/{f:04d}.png")
subprocess.run([FF, "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{tmp}/%04d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", out], check=True)
shutil.rmtree(tmp)
print("rendered", out, N, "frames")
