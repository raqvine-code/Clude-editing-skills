"""Telugu shaping check + specimen (2026-11-25, after `brew install fribidi` made Pillow's raqm work).
Usage: ~/.local/share/whisper-venv/bin/python -I telugu_check.py <out.png> ["Telugu sample"]
Prints whether raqm is active, then draws every Telugu font in the library twice:
left = BASIC layout (what we had before: vowel signs and conjuncts break), right = RAQM (correct shaping).
If the right column ever looks like the left one, raqm is gone again: run `brew install fribidi` (Pillow wheels bundle raqm
and harfbuzz; they only need libfribidi.dylib from Homebrew at run time).
"""
import sys

from PIL import Image, ImageDraw, ImageFont, features

F = "/Users/raghusai/Desktop/CLAUDE 2.0/skills/fonts-and-colours/assets/fonts/"
FONTS = [
    ("NotoSansTelugu-Variable.ttf", {"wght": 700}, "Noto Sans Telugu 700", "caption"),
    ("AnekTelugu-Variable.ttf", {"wght": 700}, "Anek Telugu 700", "caption"),
    ("HindGuntur-Bold.ttf", None, "Hind Guntur 700", "caption"),
    ("Mandali-Regular.ttf", None, "Mandali", "small / lead-in"),
    ("BalooTammudu2-ExtraBold.ttf", None, "Baloo Tammudu 2 800", "keyword / display"),
    ("Ramabhadra-Regular.ttf", None, "Ramabhadra", "display"),
    ("NTR-Regular.ttf", None, "NTR", "display"),
    ("Gidugu-Regular.ttf", None, "Gidugu", "display, light"),
    ("NotoSerifTelugu-Bold.ttf", None, "Noto Serif Telugu 700", "serif accent"),
    ("TiroTelugu-Regular.ttf", None, "Tiro Telugu", "serif accent"),
    ("Suranna-Regular.ttf", None, "Suranna", "serif accent (no ₹)"),
    ("TenaliRamakrishna-Regular.ttf", None, "Tenali Ramakrishna", "playful accent"),
]
TAGS = {"Weight": "wght", "Width": "wdth", "Optical size": "opsz"}


def load(name, var, size, engine):
    f = ImageFont.truetype(F + name, size, layout_engine=engine)
    if var:
        vals = []
        for a in f.get_variation_axes():
            n = a.get("name", b"")
            n = n.decode() if isinstance(n, bytes) else str(n)
            vals.append(var.get(TAGS.get(n, n), a["default"]))
        f.set_variation_by_axes(vals)
    return f


def main():
    out = sys.argv[1]
    sample = sys.argv[2] if len(sys.argv) > 2 else "కానీ ఎందుకు ఈ తేడా? ₹150"
    raqm = features.check_feature("raqm")
    print("raqm:", raqm, "| fribidi:", features.version_feature("fribidi"), "| harfbuzz:", features.version_feature("harfbuzz"))
    W, rowh = 1800, 104
    im = Image.new("RGB", (W, 130 + rowh * len(FONTS)), (20, 17, 15))
    d = ImageDraw.Draw(im)
    lab = ImageFont.truetype(F + "BricolageGrotesque-SemiBold.ttf", 24)
    small = ImageFont.truetype(F + "BricolageGrotesque-Light.ttf", 20)
    d.text((30, 30), "TELUGU SHAPING CHECK", font=lab, fill=(226, 170, 44))
    d.text((430, 70), "BASIC layout (broken)", font=lab, fill=(200, 72, 60))
    d.text((1110, 70), "RAQM layout (correct)" if raqm else "RAQM NOT ACTIVE", font=lab, fill=(226, 170, 44))
    y = 120
    for name, var, label, role in FONTS:
        d.text((30, y + 24), label, font=lab, fill=(244, 239, 227))
        d.text((30, y + 56), role, font=small, fill=(160, 150, 138))
        d.text((430, y + 70), sample, font=load(name, var, 52, ImageFont.Layout.BASIC), fill=(170, 160, 150), anchor="ls")
        if raqm:
            d.text((1110, y + 70), sample, font=load(name, var, 52, ImageFont.Layout.RAQM), fill=(244, 239, 227), anchor="ls")
        y += rowh
    im.save(out)
    print("ok", out, im.size)
    return 0 if raqm else 1


if __name__ == "__main__":
    sys.exit(main())
