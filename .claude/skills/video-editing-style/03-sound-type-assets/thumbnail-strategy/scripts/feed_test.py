#!/usr/bin/env python3
"""Mobile + light/dark feed test for thumbnails.

Usage: python3 feed_test.py thumb1.png [thumb2.png ...] [-o out.jpg]
Renders every thumbnail at real feed sizes (168, 246, 320, 640 px wide) on a
light (#FFFFFF) and a dark (#0F0F0F) YouTube background, plus a blurred
"squint" copy, into one contact sheet. Needs Pillow.
"""
import sys
from PIL import Image, ImageDraw, ImageFilter

SIZES = [168, 246, 320, 640]          # search/sidebar, small phone, phone feed, desktop
BGS = [("light", (255, 255, 255)), ("dark", (15, 15, 15))]
PAD = 24


def main():
    args = sys.argv[1:]
    out = "feed_test.jpg"
    if "-o" in args:
        i = args.index("-o")
        out = args[i + 1]
        args = args[:i] + args[i + 2:]
    if not args:
        sys.exit(__doc__)
    thumbs = [Image.open(p).convert("RGB") for p in args]

    row_h = max(int(s * 9 / 16) for s in SIZES) + PAD * 2
    row_w = sum(SIZES) + 320 + PAD * (len(SIZES) + 2)
    sheet = Image.new("RGB", (row_w, row_h * len(thumbs) * len(BGS)), (128, 128, 128))
    y = 0
    for t in thumbs:
        for name, bg in BGS:
            band = Image.new("RGB", (row_w, row_h), bg)
            x = PAD
            for s in SIZES:
                im = t.resize((s, int(s * 9 / 16)), Image.LANCZOS)
                band.paste(im, (x, PAD))
                x += s + PAD
            squint = t.resize((320, 180), Image.LANCZOS).filter(ImageFilter.GaussianBlur(6))
            band.paste(squint, (x, PAD))
            ImageDraw.Draw(band).text((x, PAD + 185), f"{name} | squint", fill=(128, 128, 128))
            sheet.paste(band, (0, y))
            y += row_h
    sheet.save(out, quality=90)
    print(out)


if __name__ == "__main__":
    main()
