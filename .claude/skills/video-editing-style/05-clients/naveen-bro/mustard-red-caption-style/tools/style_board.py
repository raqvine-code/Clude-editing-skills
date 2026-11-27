"""One-page style board for a client pitch (2400x1350): look name, palette, fonts, three 9:16 frames.
Usage: python3 -I style_board.py <out.png> <frame1.jpg> <frame2.jpg> <frame3.jpg> ["caption 1|caption 2|caption 3"]
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

F = "/Users/raghusai/Desktop/CLAUDE 2.0/skills/fonts-and-colours/assets/fonts/"
HALDI, KUMKUM, CREAM, INK, PAPER = (226, 170, 44), (200, 55, 45), (244, 239, 227), (26, 20, 16), (240, 234, 222)


def f(name, size):
    return ImageFont.truetype(F + name, size)


def main():
    out, frames = sys.argv[1], sys.argv[2:5]
    caps = (sys.argv[5] if len(sys.argv) > 5 else "ghost line, haldi keyword|hero word on a haldi brush|kumkum on the negative word").split("|")
    W, H = 2400, 1350
    bd = Image.new("RGB", (W, H), (22, 18, 15))
    d = ImageDraw.Draw(bd)
    # paper grain on the left panel
    panel = Image.new("RGB", (900, H), PAPER)
    noise = Image.effect_noise((900, H), 18).convert("L").filter(ImageFilter.GaussianBlur(0.6))
    panel = Image.blend(panel, Image.merge("RGB", (noise, noise, noise)), 0.06)
    bd.paste(panel, (0, 0))
    d = ImageDraw.Draw(bd)
    x0 = 90
    d.text((x0, 80), "CAPTION STYLE · SHORTS", font=f("BricolageGrotesque-SemiBold.ttf", 30), fill=(120, 104, 88))
    d.text((x0, 300), "Haldi", font=f("Fraunces-SoftBlackItalic.ttf", 150), fill=HALDI, anchor="ls")
    t2 = "& Kumkum"
    d.text((x0, 450), t2, font=f("Fraunces-SoftBlackItalic.ttf", 120), fill=INK, anchor="ls")
    dot_x = x0 + f("Fraunces-SoftBlackItalic.ttf", 120).getlength(t2) + 6
    d.ellipse([dot_x, 424, dot_x + 26, 450], fill=KUMKUM)
    body = f("BricolageGrotesque-Light.ttf", 34)
    lines = ["Turmeric yellow and vermilion red:", "the two colours every Telugu home knows,", "worn softly, like an editorial magazine."]
    for i, ln in enumerate(lines):
        d.text((x0, 520 + i * 48), ln, font=body, fill=(70, 60, 50))
    # palette
    sw = [("Haldi", "#E2AA2C", HALDI, "the keyword"), ("Kumkum", "#C8372D", KUMKUM, "negative words, the dot"),
          ("Cream", "#F4EFE3", CREAM, "every other word"), ("Ink", "#1A1410", INK, "outline and shadow")]
    lab, small = f("BricolageGrotesque-SemiBold.ttf", 30), f("BricolageGrotesque-Light.ttf", 26)
    y = 700
    for name, hx, col, role in sw:
        d.rounded_rectangle([x0, y, x0 + 86, y + 86], radius=18, fill=col, outline=(200, 190, 175), width=2)
        d.text((x0 + 116, y + 36), f"{name}  {hx}", font=lab, fill=INK, anchor="ls")
        d.text((x0 + 116, y + 74), role, font=small, fill=(110, 96, 82), anchor="ls")
        y += 112
    # fonts
    y += 20
    d.text((x0, y + 40), "luxury", font=f("Fraunces-SoftBoldItalic.ttf", 64), fill=HALDI, anchor="ls")
    d.text((x0 + 250, y + 40), "Fraunces Soft Italic, keyword", font=small, fill=(110, 96, 82), anchor="ls")
    d.text((x0, y + 100), "idi kaadu", font=f("BricolageGrotesque-SemiBold.ttf", 44), fill=INK, anchor="ls")
    d.text((x0 + 250, y + 100), "Bricolage Grotesque, lead-in", font=small, fill=(110, 96, 82), anchor="ls")
    # frames
    fw, fh = 420, 747
    for i, (pth, cap) in enumerate(zip(frames, caps)):
        im = Image.open(pth).convert("RGB").resize((fw, fh))
        fx = 990 + i * (fw + 34)
        sh = Image.new("RGBA", (fw + 60, fh + 60), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([30, 36, fw + 30, fh + 36], radius=28, fill=(0, 0, 0, 160))
        bd.paste(sh.filter(ImageFilter.GaussianBlur(16)), (fx - 30, 230 - 30), sh.filter(ImageFilter.GaussianBlur(16)))
        m = Image.new("L", (fw, fh), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, fw, fh], radius=28, fill=255)
        bd.paste(im, (fx, 230), m)
        d = ImageDraw.Draw(bd)
        d.text((fx + 4, 1040), f"0{i + 1}", font=f("Fraunces-SoftBoldItalic.ttf", 44), fill=HALDI, anchor="ls")
        d.text((fx + 64, 1038), cap, font=f("BricolageGrotesque-Light.ttf", 24), fill=CREAM, anchor="ls")
    d.text((990, 1260), "Original look  ·  free OFL fonts, safe for commercial use  ·  1080 x 1920",
           font=f("BricolageGrotesque-Light.ttf", 24), fill=(150, 138, 124), anchor="ls")
    bd.save(out)
    print("ok", out)


if __name__ == "__main__":
    main()
