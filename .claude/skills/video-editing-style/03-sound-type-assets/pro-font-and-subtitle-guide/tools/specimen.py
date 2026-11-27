"""Font specimen sheet for the central library (skills/fonts-and-colours/assets/fonts).
Usage: python3 -I specimen.py <out.png> ["sample text"]
Latin fonts. Telugu fonts have their own sheet: telugu_check.py (raqm works since 2026-11-25, see GUIDE.md section 6).
"""
import sys
from PIL import Image, ImageDraw, ImageFont

F = "/Users/raghusai/Desktop/CLAUDE 2.0/skills/fonts-and-colours/assets/fonts/"
ROWS = [
    ("CAPTIONS  ·  short-form", [("Montserrat-Variable.ttf", {"wght": 800}, "Montserrat 800"), ("Inter-Black.ttf", None, "Inter Black"),
                                 ("Poppins-ExtraBold.ttf", None, "Poppins 800"), ("InterTight-900.ttf", None, "Inter Tight 900"),
                                 ("AtkinsonHyperlegibleNext-Bold.ttf", None, "Atkinson Hyperlegible Next 700")]),
    ("DISPLAY  ·  giants, titles, thumbnails", [("Anton-Regular.ttf", None, "Anton"), ("BebasNeue-Regular.ttf", None, "Bebas Neue"),
                                                ("Archivo-ExpandedBlack.ttf", None, "Archivo Expanded 900"), ("Oswald-Variable.ttf", {"wght": 700}, "Oswald 700"),
                                                ("Archivo-CondensedExtraBold.ttf", None, "Archivo Condensed 800")]),
    ("EDITORIAL SERIF  ·  the meaning word", [("Fraunces-SoftBoldItalic.ttf", None, "Fraunces Soft Bold Italic"),
                                              ("PlayfairDisplay-Italic-Variable.ttf", {"wght": 800}, "Playfair Display 800 Italic"),
                                              ("CormorantGaramond-SemiBoldItalic.ttf", None, "Cormorant Garamond 600 Italic"),
                                              ("EBGaramond-Italic-Variable.ttf", {"wght": 500}, "EB Garamond Italic"),
                                              ("DMSerifDisplay-Regular.ttf", None, "DM Serif Display"), ("Cinzel-Bold.ttf", None, "Cinzel 700")]),
    ("MODERN GROTESK  ·  lead-ins, UI, lower thirds", [("BricolageGrotesque-SemiBold.ttf", None, "Bricolage Grotesque 600"),
                                                      ("Inter-SemiBold.ttf", None, "Inter 600"), ("Poppins-SemiBold.ttf", None, "Poppins 600")]),
    ("SCRIPT / HAND  ·  one accent word only", [("MeaCulpa-Regular.ttf", None, "Mea Culpa"), ("Caveat-Bold.ttf", None, "Caveat 700"),
                                                 ("PermanentMarker-Regular.ttf", None, "Permanent Marker")]),
    ("MONO / TYPEWRITER  ·  HUD, code, documents", [("JetBrainsMono-Bold.ttf", None, "JetBrains Mono 700"), ("CourierPrime-Bold.ttf", None, "Courier Prime Bold"),
                                                    ("SpecialElite-Regular.ttf", None, "Special Elite")]),
]


def load(name, var, size):
    f = ImageFont.truetype(F + name, size)
    if var:
        axes = f.get_variation_axes()
        f.set_variation_by_axes([var.get(_tag(a), a["default"]) for a in axes])
    return f


def _tag(a):
    n = a.get("name", b"")
    n = n.decode() if isinstance(n, bytes) else str(n)
    return {"Weight": "wght", "Width": "wdth", "Optical size": "opsz"}.get(n, n)


def main():
    out = sys.argv[1]; sample = sys.argv[2] if len(sys.argv) > 2 else "kaani enduku ee Difference? ₹150"
    W = 1600; rowh = 92; H = 120 + sum(60 + rowh * len(r[1]) for r in ROWS)
    im = Image.new("RGB", (W, H), (20, 17, 15)); d = ImageDraw.Draw(im)
    lab = ImageFont.truetype(F + "BricolageGrotesque-SemiBold.ttf", 26); small = ImageFont.truetype(F + "BricolageGrotesque-Light.ttf", 22)
    d.text((40, 40), "FONT LIBRARY  ·  skills/fonts-and-colours/assets/fonts  ·  all free for commercial use (OFL / Apache)", font=lab, fill=(226, 170, 44))
    y = 110
    for title, fonts in ROWS:
        d.text((40, y + 14), title, font=lab, fill=(200, 72, 60)); y += 60
        for name, var, label in fonts:
            d.text((40, y + 34), label, font=small, fill=(160, 150, 138))
            f = load(name, var, 56)
            d.text((470, y + 58), sample, font=f, fill=(244, 239, 227), anchor="ls")
            y += rowh
    im.save(out); print("ok", out, im.size)


if __name__ == "__main__":
    main()
