"""Style frames for the mustard-red caption style (M1 podcast serif, M2 golden caps, M3 film subtitle).
Usage: python3 -I style_frames.py <frame_1080x1920.png> <out_dir> ["lead|KEY|neg"]
Draws one caption group per look on the client's own frame, plus a 3-up sheet (lower 60 % of each frame).
Fonts come from the CLAUDE 2.0 project folders (all on the fonts-and-colours list or its central fonts folder).
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path("/Users/raghusai/Desktop/CLAUDE 2.0")
FONTS = {
    "mont_bold": ROOT / "edits/telugu3/assets/fonts/Montserrat-Bold.ttf",
    "mont_black": ROOT / "edits/telugu3/assets/fonts/Montserrat-Black.ttf",
    "playfair_xbi": ROOT / "edits/telugu4/assets/fonts/PlayfairDisplay-ExtraBoldItalic.ttf",
    "oswald": ROOT / "skills/fonts-and-colours/assets/fonts/Oswald-Variable.ttf",
    "inter500": ROOT / "edits/telugu2/assets/fonts/InterTight-500.ttf",
    "inter800": ROOT / "edits/telugu4/assets/fonts/InterTight-800.ttf",
}
# palette (GUIDE.md section 2): measured references, dulled per beginner-to-pro-edit-tips rule 3
MUSTARD = (226, 170, 44)      # #E2AA2C keyword
MUSTARD_SOFT = (224, 190, 96)  # #E0BE60 film-subtitle body
RED = (210, 72, 60)           # #D2483C brick red: negatives / warnings only
CREAM = (244, 239, 227)       # #F4EFE3 lead-in words
INK = (26, 20, 16)            # #1A1410 outline + shadow


def font(key, size, weight=None):
    f = ImageFont.truetype(str(FONTS[key]), size)
    if weight:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def layer(size, items):
    """items: (text, font, fill, x, baseline_y, stroke_px). Returns an RGBA layer."""
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    for t, f, fill, x, y, sw in items:
        d.text((x, y), t, font=f, fill=fill, anchor="ls", stroke_width=sw, stroke_fill=INK)
    return lay


def shadow(base, lay, blur=14, alpha=0.7, dy=6):
    a = lay.split()[3].point(lambda v: int(v * alpha))
    sh = Image.new("RGBA", base.size, INK + (0,))
    sh.putalpha(a)
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)), (0, dy))


def m1_podcast_serif(img, lead, key, neg):
    """M1 (ref: Figuring Out official short): small cream geometric caps + big mustard bold-italic serif keyword;
    the red word is small caps under it, right-aligned to the keyword. Stack sits at chest height."""
    W = img.width
    f_lead, f_key, f_neg = font("mont_bold", 58), font("playfair_xbi", 158), font("mont_black", 60)
    kw = f_key.getlength(key)
    kx = W / 2 - kw / 2
    base = 1290
    items = [
        (lead.upper(), f_lead, CREAM, kx + 12, base - 150, 3),
        (key, f_key, MUSTARD, kx, base + 10, 0),
        (neg.upper(), f_neg, RED, kx + kw - f_neg.getlength(neg.upper()) - 4, base + 96, 4),
    ]
    out = img.copy()
    lay = layer(out.size, items)
    shadow(out, lay, blur=16, alpha=0.8, dy=6)
    glow = layer(out.size, [items[1]]).filter(ImageFilter.GaussianBlur(20))
    glow.putalpha(glow.split()[3].point(lambda v: int(v * 0.35)))
    out.alpha_composite(glow)
    out.alpha_composite(lay)
    return out


def m2_golden_caps(img, lead, key, neg):
    """M2 (refs: Kobe motivation edit, Hormozi 2026 shorts): one line of condensed caps, 2-3 words,
    cream words + the spoken keyword in mustard + a negative word in red; dark outline + soft drop shadow."""
    W = img.width
    f = font("oswald", 112, weight=700)
    words = [(lead.upper(), CREAM), (key.upper(), MUSTARD), (neg.upper(), RED)]
    gap = 26
    widths = [f.getlength(w) for w, _ in words]
    total = sum(widths) + gap * (len(words) - 1)
    scale = min(1.0, 900 / total)
    if scale < 1.0:
        f = font("oswald", int(112 * scale), weight=700)
        widths = [f.getlength(w) for w, _ in words]
        total = sum(widths) + gap * (len(words) - 1)
    x = W / 2 - total / 2
    items = []
    for (w, c), wd in zip(words, widths):
        items.append((w, f, c, x, 1300, 5))
        x += wd + gap
    out = img.copy()
    lay = layer(out.size, items)
    shadow(out, lay, blur=10, alpha=0.85, dy=7)
    out.alpha_composite(lay)
    return out


def m3_film_subtitle(img, lead, key, neg):
    """M3 (ref: Instagram 'vintage yellow subtitles' reels): small sentence-case sans in soft mustard,
    centred low (above the platform UI), thin dark edge; one word in red. Calm, cinematic."""
    W = img.width
    f = font("inter500", 54)
    parts = [(lead.capitalize() + " ", MUSTARD_SOFT), (key + " ", MUSTARD_SOFT), (neg + ".", RED)]
    total = sum(f.getlength(t) for t, _ in parts)
    x = W / 2 - total / 2
    items = []
    for t, c in parts:
        items.append((t, f, c, x, 1500, 3))
        x += f.getlength(t)
    out = img.copy()
    lay = layer(out.size, items)
    shadow(out, lay, blur=8, alpha=1.0, dy=3)
    shadow(out, lay, blur=22, alpha=0.6, dy=0)
    out.alpha_composite(lay)
    return out


def tag(img, label):
    d = ImageDraw.Draw(img)
    f = font("inter800", 46)
    w = f.getlength(label)
    d.rounded_rectangle([40, 60, 40 + w + 48, 142], radius=40, fill=(20, 18, 16, 215))
    d.text((64, 120), label, font=f, fill=CREAM, anchor="ls")
    return img


def main():
    frame, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    lead, key, neg = (sys.argv[3] if len(sys.argv) > 3 else "idi|luxury|kaadu").split("|")
    out_dir.mkdir(parents=True, exist_ok=True)
    img = Image.open(frame).convert("RGBA").resize((1080, 1920))
    looks = [("M1", "Podcast serif", m1_podcast_serif), ("M2", "Golden caps", m2_golden_caps),
             ("M3", "Film subtitle", m3_film_subtitle)]
    tiles = []
    for k, name, fn in looks:
        o = fn(img, lead, key, neg)
        o.convert("RGB").save(out_dir / f"{k}_{name.lower().replace(' ', '_')}.png")
        t = tag(o.copy(), f"{k} · {name}")
        crop = t.crop((0, 700, 1080, 1700)).resize((540, 500))
        crop.paste(t.crop((0, 40, 760, 162)).resize((380, 61)), (0, 0))
        tiles.append(crop)
    sheet = Image.new("RGB", (540 * 3 + 40, 500), (14, 14, 14))
    for i, c in enumerate(tiles):
        sheet.paste(c.convert("RGB"), (i * 560, 0))
    sheet.save(out_dir / "mustard_red_style_sheet.png")
    print("ok", out_dir)


if __name__ == "__main__":
    main()
