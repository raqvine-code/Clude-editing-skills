"""Font-pairing board on the client's own footage (mustard-red-caption-style section 8, 2026-11-25).
Shows the client's six font pairings (5 carousel combos + the "Grind szn" reel) re-made with FREE fonts
in the M4 haldi / kumkum / cream palette, one 1080x1920 tile each, plus a labelled board.
Run with the venv that has PIL + mediapipe (for the behind-the-head tile):
  ~/.local/share/whisper-venv/bin/python -I pairing_board.py <raw.mp4 stills dir> <out dir>
The stills dir holds f_<time>.jpg frames of the raw (any size, 9:16).
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

F = "/Users/raghusai/Desktop/CLAUDE 2.0/skills/fonts-and-colours/assets/fonts/"
HALDI, KUMKUM, CREAM, INK = (226, 170, 44), (210, 72, 60), (244, 239, 227), (26, 20, 16)
W, H = 1080, 1920


def font(name, size, var=None):
    f = ImageFont.truetype(F + name, size)
    if var:
        axes = f.get_variation_axes()
        tags = {"Weight": "wght", "Width": "wdth", "Optical size": "opsz"}
        vals = []
        for a in axes:
            n = a.get("name", b"")
            n = n.decode() if isinstance(n, bytes) else str(n)
            vals.append(var.get(tags.get(n, n), a["default"]))
        f.set_variation_by_axes(vals)
    return f


def text_width(f, s, track=0):
    return f.getlength(s) + track * (len(s) - 1)


def draw_text(layer, xy, s, f, fill, track=0, anchor="ls", alpha=255):
    """Draw s with letter tracking (px, may be negative). anchor: ls / ms / rs on the baseline."""
    d = ImageDraw.Draw(layer)
    w = text_width(f, s, track)
    x, y = xy
    if anchor[0] == "m":
        x -= w / 2
    elif anchor[0] == "r":
        x -= w
    col = fill + (alpha,)
    if track == 0:
        d.text((x, y), s, font=f, fill=col, anchor="ls")
    else:
        for ch in s:
            d.text((x, y), ch, font=f, fill=col, anchor="ls")
            x += f.getlength(ch) + track
    return w


def shadowed(base, layer, blur=10, off=(0, 6), strength=0.55, outline=0):
    """Composite a text layer with a soft ink shadow (and an optional ink outline for red words)."""
    a = layer.split()[3]
    if outline:
        a_out = a.filter(ImageFilter.MaxFilter(outline * 2 + 1))
        ol = Image.new("RGBA", layer.size, INK + (0,))
        ol.putalpha(a_out)
        base = Image.alpha_composite(base, ol)
    sh = Image.new("RGBA", layer.size, INK + (0,))
    sh.putalpha(a.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * strength)))
    base = Image.alpha_composite(base, sh.transform(sh.size, Image.AFFINE, (1, 0, -off[0], 0, 1, -off[1])))
    return Image.alpha_composite(base, layer)


def grade(im):
    """Quick P16 look for the board only: a little contrast, warm, vignette (the real grade is shortkit's)."""
    x = np.asarray(im.convert("RGB")).astype(np.float32) / 255
    x = np.clip((x - 0.5) * 1.12 + 0.5, 0, 1)
    x[..., 0] *= 1.03
    x[..., 2] *= 0.96
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H * 0.45) / (H / 2)) ** 2)
    x *= (1 - 0.34 * np.clip(r - 0.55, 0, 1))[..., None]
    return Image.fromarray((np.clip(x, 0, 1) * 255).astype(np.uint8)).convert("RGBA")


def person_matte(im):
    import mediapipe as mp
    seg = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=0)
    m = seg.process(np.asarray(im.convert("RGB"))).segmentation_mask
    m = (np.clip((m - 0.35) / 0.3, 0, 1) * 255).astype(np.uint8)
    return Image.fromarray(m).filter(ImageFilter.GaussianBlur(2))


def blur_reveal(layer, p):
    """State of the blur-to-sharp reveal at progress p (0..1), as the reel does it (about 0.2 s)."""
    r = (1 - p) * 14
    out = layer.filter(ImageFilter.GaussianBlur(r)) if r > 0.3 else layer
    a = out.split()[3].point(lambda v: int(v * (0.35 + 0.65 * p)))
    out.putalpha(a)
    return out


def fit(f_name, s, max_w, size, track=0, var=None):
    f = font(f_name, size, var)
    while text_width(f, s, track) > max_w and size > 20:
        size -= 4
        f = font(f_name, size, var)
    return f


def tile_a(bg):  # carousel 2/7: Playfair Display italic + Poppins caps
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    big = fit("Poppins-ExtraBold.ttf", "INGREDIENTS", 900, 150, track=-5)
    draw_text(L, (W / 2, 610), "INGREDIENTS", big, HALDI, track=-5, anchor="ms")
    it = font("PlayfairDisplay-Italic-Variable.ttf", 120, {"wght": 800})
    draw_text(L, (W / 2 - 420, 480), "same", it, CREAM, track=-3)
    return shadowed(bg, L)


def tile_b(bg):  # carousel 3/7: brush script over condensed caps (Billion Dreams + Anton -> Yellowtail + Anton)
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    caps = fit("Anton-Regular.ttf", "WASTE", 700, 300, track=-4)  # 25 % smaller than the first try (beginner-to-pro rule 1)
    draw_text(L, (W / 2, 630), "WASTE", caps, KUMKUM, track=-4, anchor="ms")
    out = shadowed(bg, L, outline=5)
    S = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_text(S, (W / 2 - 40, 440), "ekkuva", font("Yellowtail-Regular.ttf", 170), CREAM, anchor="ms")
    return shadowed(out, S, blur=8)


def tile_c(bg):  # carousel 4/7: bold grotesk + heavy serif italic (Acumin + Times -> Inter Tight + DM Serif Display Italic)
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    big = fit("DMSerifDisplay-Italic.ttf", "difference?", 940, 210, track=-6)
    draw_text(L, (W / 2, 600), "difference?", big, HALDI, track=-6, anchor="ms")
    draw_text(L, (W / 2 - 330, 455), "kaani enduku ee", font("InterTight-800.ttf", 74), CREAM, track=-3)
    return shadowed(bg, L)


def tile_d(bg):  # carousel 5/7: condensed serif caps + formal script + dot (Spire + Italianno -> Instrument Serif + Italianno)
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    caps = font("InstrumentSerif-Regular.ttf", 150)
    wcap = draw_text(L, (W / 2 + 20, 400), "ANNI", caps, CREAM, track=-2, anchor="ms")
    d = ImageDraw.Draw(L)
    cx, cy, r = W / 2 + 20 + wcap / 2 + 40, 375, 15
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=KUMKUM + (255,))
    script = fit("Italianno-Regular.ttf", "Companies", 940, 300)
    draw_text(L, (W / 2 - 10, 610), "Companies", script, HALDI, anchor="ms")
    return shadowed(bg, L)


def tile_e(bg, matte):  # carousel 6/7: small bold sans + huge wide caps behind the subject (Satoshi -> Archivo Expanded + Bricolage)
    G = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    caps = fit("Archivo-ExpandedBlack.ttf", "SHARE", 960, 300, track=-6)
    draw_text(G, (W / 2, 735), "SHARE", caps, CREAM, track=-6, anchor="ms")
    out = shadowed(bg, G, blur=14, strength=0.45)
    person = bg.copy()
    person.putalpha(matte)
    out = Image.alpha_composite(out, person)  # the head sits in front of the giant's feet
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_text(L, (W / 2, 430), "prathi woman ki", font("BricolageGrotesque-ExtraBold.ttf", 84), HALDI, track=-2, anchor="ms")
    return shadowed(out, L)


def tile_f(bg):  # the "Grind szn" reel: lowercase bold sans words + one script keyword, stacked, word by word, blur reveal
    out = bg
    # Stair-step stack in the plain wall above the head: a thin formal script is unreadable on the checked shirt.
    sans = font("Poppins-ExtraBold.ttf", 76)
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_text(L, (190, 380), "vaallaki", sans, CREAM, track=-2)
    draw_text(L, (330, 455), "kooda", sans, CREAM, track=-2)
    out = shadowed(out, L)
    K = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_text(K, (W / 2 + 40, 625), "teliyaali", font("PinyonScript-Regular.ttf", 210), HALDI, anchor="ms")
    K = blur_reveal(K, 0.8)  # caught near the end of the reveal, as in the reel's frames at 3.85-3.95 s
    return shadowed(out, K, blur=8)


TILES = [
    ("f_17.85.jpg", tile_a, "Playfair 800 Italic + Poppins caps", "client 2/7: Playfair + Poppins"),
    ("f_22.55.jpg", tile_b, "Yellowtail + Anton (kumkum)", "client 3/7: Billion Dreams + Anton"),
    ("f_19.35.jpg", tile_c, "Inter Tight + DM Serif Italic", "client 4/7: Acumin Pro + Times New Roman"),
    ("f_25.65.jpg", tile_d, "Instrument Serif + Italianno + dot", "client 5/7: Spire + Italianno"),
    ("f_40.35.jpg", tile_e, "Bricolage + Archivo Exp., behind head", "client 6/7: Satoshi"),
    ("f_41.30.jpg", tile_f, "Poppins + Pinyon Script stack", "client reel: word stack, blur reveal"),
]


def main():
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    tw, th, lab = 480, 853, 92
    board = Image.new("RGB", (40 + 3 * (tw + 20), 120 + 2 * (th + lab + 20)), (20, 17, 15))
    d = ImageDraw.Draw(board)
    hf, lf, sf = font("BricolageGrotesque-SemiBold.ttf", 34), font("BricolageGrotesque-SemiBold.ttf", 22), font("BricolageGrotesque-Light.ttf", 20)
    d.text((40, 40), "Client font pairings on Pink Tax  ·  free fonts  ·  M4 haldi / kumkum / cream", font=hf, fill=HALDI)
    for i, (still, fn, name, ref) in enumerate(TILES):
        bg = grade(Image.open(os.path.join(src, still)).convert("RGB").resize((W, H), Image.LANCZOS))
        im = fn(bg, person_matte(bg)) if fn is tile_e else fn(bg)
        im.convert("RGB").save(os.path.join(out, f"pairing_{i + 1}.jpg"), quality=92)
        x, y = 40 + (i % 3) * (tw + 20), 110 + (i // 3) * (th + lab + 20)
        board.paste(im.convert("RGB").resize((tw, th), Image.LANCZOS), (x, y))
        d.text((x, y + th + 12), f"{i + 1}. {name}", font=lf, fill=CREAM)
        d.text((x, y + th + 46), ref, font=sf, fill=(170, 160, 146))
    board.save(os.path.join(out, "PAIRINGS_board.jpg"), quality=90)
    print("ok", out, board.size)


if __name__ == "__main__":
    main()
