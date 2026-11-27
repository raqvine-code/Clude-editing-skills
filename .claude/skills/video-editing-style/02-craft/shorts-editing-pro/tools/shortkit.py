"""shortkit: lean 9:16 short renderer for the shorts-editing-pro skill (one file, no browser, no subagents).

Run with the venv that has cv2 + mediapipe + scipy + PIL:
  (Telugu script needs raqm: `features.check_feature("raqm")` True, i.e. Homebrew fribidi installed. For a partial re-render of a
   project rendered before 2026-11-25 set SHORTKIT_LAYOUT=basic so new frames match the old ones.)
  PY=~/.local/share/whisper-venv/bin/python
  $PY shortkit.py video  edl.json [--from S] [--to S] [--scale 0.5] [--workers 6]   -> work/frames/*.jpg + work/video.mp4
  $PY shortkit.py stills edl.json 0.5,3.2,7.9 [--scale 0.5]                         -> work/stills/*.jpg + sheet.jpg
  $PY shortkit.py audio  edl.json                                                   -> audio/voice.wav, sfx.wav, mix_main.wav (+ mix_music.wav)
  $PY shortkit.py mux    edl.json                                                   -> export/<name>.mp4 (+ _with_music.mp4) + qc.txt

EDL (all times in OUTPUT seconds unless named src):
{ "name": "Self_Story", "src": "/path/raw.mp4", "fps": 60, "project": "/path/edits/<id>",
  "keeps": [[src_in, src_out], ...],                      # source seconds; output = concatenation (frame-exact, 800 samples/frame)
  "anchor": [720, 820], "eye_y": 700,                      # source px of the eye line centre, screen y it should sit at
  "camera": [[t, scale, ease], ...],                       # keyframes; two keys at the same t = hard jump (cut); ease of the segment INTO a key
  "grade": {"exp": 0.35, "contrast": 1.10, "pivot": 0.42, "sat": 1.08, "warm": 0.02, "teal": 0.03, "face": 0.22, "vignette": 0.32, "grain": 0.035, "black": 0.02},
  "broll": [{"key": "coins", "file": "...", "src": 1.0, "t0": 3.4, "t1": 5.1, "speed": 1.0, "cx": 0.5, "z": [1.0, 1.06],
             "entry": "whip|whipL|blurzoom|cut", "gain": 1.0, "gamma": 1.0, "sat": 1.0, "bw": false, "shade": true}],
  "flashes": [{"t": 7.5, "type": "white|neg"}],
  "captions": [{"t0": 0.0, "t1": 1.0, "y": 1300, "words": [[t, "text", "n|k", {opts}], ...]}],   # n = small lead-in words, k = keyword line (big)
      # P13 two-tier (2026-11-22): optional "y" per group; keyword opts {"c": "#hex" role colour, "fx": "track" (letter-spacing settles in 0.2 s,
      # starting ON the word) | "stagger" (letters arrive one by one, use once on the worst-news word), "bar": true|"#hex" pivot underline wipe, "size": 1.0,
      # "strike": {"t": 38.5, "c": "#FF4338"} line through the keyword ("not X"), "font": "serif" (style.serif_font, the meaning word) | "script" (style.script_font) | "Italianno-Regular.ttf" (any library file), "glow": 0.3}
  "desat": [{"t0": 46.9, "t1": 51.3, "fade": 0.12}],                           # whole frame to black and white (captions included)
  "layers": [{"key": "ped_v1", "dir": "/abs/dir of %05d.png RGBA frames (1-based, 1080x1920)", "t0": 3.0, "t1": 6.0, "behind": true}],  # designed objects behind / in front of the speaker
  "dims": [{"t0": 9.0, "t1": 11.0, "amt": 0.46, "blur": 8, "fade": 0.25}],     # dim-and-overlay: speaker darker + defocused under a front layer
  "giants": [{"t0": 0, "t1": 1.2, "text": "STORY", "y": 330, "size": 260, "behind": true, "color": "#FFFFFF",
              "swap": {"t": 2.0, "text": "FRAMES", "color": "#FF6F61"}, "font": "...ttf (optional)", "strike": {"t": 2.5, "c": "#D24E5A", "h": 22, "dy": 0}}],
  "brackets": [{"t0": 8.0, "t1": 9.0, "w": 520, "h": 640, "dy": 40,           # viewfinder corners around the face
                "label": "FACE 0.94", "shape": "corners|ring"}],               # 2026-11-25 (aesthetic-pro-reel-edit-style): mono HUD label + live X/Y; ring = thin glowing circle
  "paper": [{"t0": 19.6, "t1": 21.2, "color": "#EFE7D6", "ribbon": "#E2AA2C", "text": "#1A1410", "key": "#B9831A"}],
      # 2026-11-25: off-white paper scene - room replaced by textured paper, speaker cut out with a soft shadow, a haldi ribbon swoosh wipes on
      # behind them; captions turn ink (key = keyword colour on paper); giants with behind=true sit between paper and speaker
      # 2026-11-26: optional "stroke" (outline width on paper, default 0). Captions over the speaker's shirt: "text" cream, "key" haldi, "stroke" 3
  "stacks": [{"t0": 1.0, "t1": 2.35, "y": 330, "x": 540, "align": "center|left|right|stagger", "max_w": 900, "size": 128, "ratio": 0.42,
               "lines": [[[1.0, "If you", "s"]], [[1.2, "don't wanna", "b"]], [[1.5, "everyone", "b", {"fx": "type"}], [1.9, "else", "s"]]],
               "fx": "fade", "ghost": 0.0, "behind": false, "out": "cut|fade", "c": "#hex big", "cs": "#hex small", "font": "serif|script|file"}],
      # 2026-11-25 word stack (skills/text-animation-moves): s = small link word, b = big meaning word; tokens in one line share a baseline;
      # token opts {"fx": "cut|fade|blur|rise|grain|pop|type", "c", "font", "size", "d" (seconds), "dur" (type), "glow", "stroke"};
      # style keys stack_font, stack_small_font, stack_size, stack_ratio, stack_lead, stack_fx, stack_color, stack_stroke. Captions hide while a stack is up.
      # Placement (researched 2026-11-25, skills/pro-font-and-subtitle-guide/references/vertical-text-placement-research.md): stacks on the chest,
      # block centre 58-65 % of the height (y 1110-1250), 2 lines max, "stroke" 3 on a busy shirt; above the head only 1-3 accent texts per short.
  "mirror": [{"t0": 30.0, "t1": 31.4}],                                         # split: face panel + its mirror
  "style": {"accent": "#FF6F61", "cap_font": "...Bold.otf", "key_font": "...Black.otf", "giant_font": "...Extended-Black.otf",
            "cap_size": 92, "key_size": 150, "cap_y": 1240, "key_max_w": 900, "stroke": 5,    # stroke = dark outline px (busy shirt)
            "cap_color": "#F4EFE3",    # lead-in colour (default white); a lead-in word may carry {"c": "#hex"} too (skills/mustard-red-caption-style)
            "ghost": 0.30,             # lead-in line waits at 30 % and each word goes solid on its time (needs one token per word)
            "reveal": "blur",          # every word arrives blur-to-sharp in 0.18 s (alpha 35 -> 100 %, scale 1.05 -> 1) instead of the pop
            "mono_font": "...ttf"},    # HUD labels (default fonts-and-colours CourierPrime-Bold)
      # keyword opts (mustard-red-caption-style M4): "brush": "#hex" haldi stroke behind the word, "dot": "#hex" kumkum full stop after it
  "sfx": [{"t": 0.0, "file": "...wav", "db": -4, "align": "start|peak", "lead": 0.0, "pitch": 0, "pan": -0.5, "sweep": [-0.8, 0.8],
           "ss": 0.12, "dur": 0.35}],   # pan -1..1; sweep = pan moves across the sound; ss/dur = slice of the file (fade-out 30 ms)
      # db = the cue's loudest 100 ms against the speech average (-10 = 10 dB under the voice); text-move recipes: skills/text-animation-moves
  "music": {"file": "...", "db": -20, "duck": 7, "src": 0.0, "fade_out": 0.8, "gaps": [[38.6, 46.5, 0.65]]} }
"""
import sys, os, json, math, subprocess, shutil
import numpy as np

def _find_ff():
    # the old aimldl_reels/bin/ffmpeg was removed (checked 2026-11-17); fall back through PATH, Homebrew, imageio
    for c in (os.environ.get("FF"), "/Users/raghusai/Downloads/claude/pending videos/aimldl_reels/bin/ffmpeg",
              shutil.which("ffmpeg"), "/opt/homebrew/bin/ffmpeg", "/usr/local/bin/ffmpeg"):
        if c and os.path.exists(c):
            return c
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


FF = _find_ff()
# fonts: env EDIT_FONTS overrides; default = the font folder of this brain (only 6 fonts ship in the zip)
FONT_DIR = os.environ.get("EDIT_FONTS") or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                       "..", "..", "..", "03-sound-type-assets", "fonts-and-colours", "assets", "fonts")
SR = 48000


def load(p):
    e = json.load(open(p))
    e.setdefault("fps", 60)
    e["_dir"] = e.get("project") or os.path.dirname(os.path.abspath(p))
    fps = e["fps"]
    seg, of = [], 0
    for a, b in e["keeps"]:
        f0, f1 = round(a * fps), round(b * fps)
        seg.append((of, f0, f1 - f0)); of += f1 - f0
    e["_seg"], e["_N"] = seg, of
    return e


def arg(name, default=None, cast=str):
    return cast(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


# ------------------------------------------------------------------ easing / camera
EASE = {"linear": lambda p: p, "sine": lambda p: 0.5 - 0.5 * math.cos(math.pi * p),
        "expo": lambda p: 1 - 2 ** (-10 * p) if p < 1 else 1.0, "out3": lambda p: 1 - (1 - p) ** 3,
        "in2": lambda p: p * p}


def cam_scale(e, t):
    ks = e["camera"]; i = 0
    for j, k in enumerate(ks):
        if k[0] <= t + 1e-9: i = j
    if i + 1 < len(ks) and ks[i + 1][0] > ks[i][0]:
        p = (t - ks[i][0]) / (ks[i + 1][0] - ks[i][0])
        return ks[i][1] + (ks[i + 1][1] - ks[i][1]) * EASE[ks[i + 1][2] if len(ks[i + 1]) > 2 else "linear"](min(max(p, 0), 1))
    return ks[i][1]


def cam_matrix(e, s, W, H, sw, sh, k):
    """affine src->out. k = output scale factor (1 or 0.5). s = zoom (1 = full source width)."""
    base = W / sw * s                      # px out per px src
    ax, ay = e["anchor"]; ey = e["eye_y"] * k
    # src rect visible: x0 = ax - (W/2)/base ...; clamp inside source
    x0 = min(max(ax - (W / 2) / base, 0), sw - W / base)
    y0 = min(max(ay - ey / base, 0), sh - H / base)
    return np.float32([[base, 0, -x0 * base], [0, base, -y0 * base]]), (ax - x0) * base, (ay - y0) * base


# ------------------------------------------------------------------ text sprites (PIL)
_FONT, _SPR = {}, {}


def font(path, size):
    from PIL import ImageFont
    key = (path, size)
    if key not in _FONT:
        # 2026-11-25: Pillow now has raqm (Telugu shaping + kerning). SHORTKIT_LAYOUT=basic restores the old layout for
        # partial re-renders of projects first rendered before that date (Latin widths differ by up to 1.6 %).
        eng = ImageFont.Layout.BASIC if os.environ.get("SHORTKIT_LAYOUT") == "basic" else None
        _FONT[key] = ImageFont.truetype(path, size, layout_engine=eng)
    return _FONT[key]


def hex2bgr(h):
    h = h.lstrip("#"); return (int(h[4:6], 16), int(h[2:4], 16), int(h[0:2], 16))


def sprite(text, path, size, color="#FFFFFF", shadow=True, glow=0.0, stroke=0):
    """BGRA float32 sprite (premultiplied-free) with soft shadow / glow (+ optional dark outline of `stroke` px for text on busy clothes).
    Returns (img HxWx4 0..1, ink_top, ink_h)."""
    key = (text, path, size, color, shadow, glow, stroke)
    if key in _SPR: return _SPR[key]
    from PIL import Image, ImageDraw, ImageFilter
    f = font(path, size)
    l, t, r, b = f.getbbox(text)
    pad = int(size * 0.45) + 40
    w, h = r - l + 2 * pad, b - t + 2 * pad
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).text((pad - l, pad - t), text, font=f, fill=255)
    a = np.asarray(m, np.float32) / 255
    rgb = np.zeros((h, w, 3), np.float32); col = np.array(hex2bgr(color), np.float32) / 255
    out_a = np.zeros((h, w), np.float32)
    if shadow:
        s1 = np.asarray(m.filter(ImageFilter.GaussianBlur(max(2, size * 0.09))), np.float32) / 255
        s2 = np.asarray(m.filter(ImageFilter.GaussianBlur(max(4, size * 0.28))), np.float32) / 255
        s1 = np.roll(s1, int(size * 0.05), axis=0)
        out_a = np.clip(0.80 * s1 + 0.45 * s2, 0, 1)
    if stroke > 0:
        ms = Image.new("L", (w, h), 0); ImageDraw.Draw(ms).text((pad - l, pad - t), text, font=f, fill=255, stroke_width=int(stroke), stroke_fill=255)
        out_a = np.maximum(out_a, np.asarray(ms.filter(ImageFilter.GaussianBlur(0.8)), np.float32) / 255 * 0.92)
    if glow > 0:
        g = np.asarray(m.filter(ImageFilter.GaussianBlur(max(6, size * 0.18))), np.float32) / 255 * glow
        rgb = rgb * out_a[..., None] + col * g[..., None]; out_a = np.clip(out_a + g, 0, 1)
        rgb = np.where(out_a[..., None] > 1e-4, rgb / np.maximum(out_a[..., None], 1e-4), 0)
    rgb = rgb * (1 - a[..., None]) + col * a[..., None]
    out_a = a + out_a * (1 - a)
    spr = (np.dstack([rgb, out_a]).astype(np.float32), pad, b - t, r - l)
    _SPR[key] = spr
    return spr


def blit(frame, spr, cx, cy, scale=1.0, alpha=1.0, sy=1.0):
    """composite sprite centred at (cx, cy) onto float32 BGR frame (0..1)."""
    import cv2
    img = spr[0]
    if abs(scale - 1) > 1e-3 or abs(sy - 1) > 1e-3:
        img = cv2.resize(img, (max(1, int(img.shape[1] * scale)), max(1, int(img.shape[0] * scale * sy))), interpolation=cv2.INTER_LINEAR)
    h, w = img.shape[:2]; x0, y0 = int(round(cx - w / 2)), int(round(cy - h / 2))
    H, W = frame.shape[:2]
    xa, ya, xb, yb = max(x0, 0), max(y0, 0), min(x0 + w, W), min(y0 + h, H)
    if xa >= xb or ya >= yb: return
    s = img[ya - y0:yb - y0, xa - x0:xb - x0]; a = s[..., 3:4] * alpha
    frame[ya:yb, xa:xb] = frame[ya:yb, xa:xb] * (1 - a) + s[..., :3] * a


def layer_blit(layer, spr, cx, cy, scale=1.0, alpha=1.0, sy=1.0):
    """same as blit but into a BGRA layer (for behind-subject text)."""
    import cv2
    img = spr[0]
    if abs(scale - 1) > 1e-3 or abs(sy - 1) > 1e-3:
        img = cv2.resize(img, (max(1, int(img.shape[1] * scale)), max(1, int(img.shape[0] * scale * sy))), interpolation=cv2.INTER_LINEAR)
    h, w = img.shape[:2]; x0, y0 = int(round(cx - w / 2)), int(round(cy - h / 2))
    H, W = layer.shape[:2]
    xa, ya, xb, yb = max(x0, 0), max(y0, 0), min(x0 + w, W), min(y0 + h, H)
    if xa >= xb or ya >= yb: return
    s = img[ya - y0:yb - y0, xa - x0:xb - x0]; a = s[..., 3:4] * alpha
    layer[ya:yb, xa:xb, :3] = layer[ya:yb, xa:xb, :3] * (1 - a) + s[..., :3] * a
    layer[ya:yb, xa:xb, 3:4] = layer[ya:yb, xa:xb, 3:4] * (1 - a) + a


# ------------------------------------------------------------------ grade
# 2026-11-26 (video 25, no-grade QC): swscale's default fast rounding darkened every render by about 2.3 luma levels
# (1.1 on the source decode to bgr24, 1.2 on the jpg -> yuv420p encode). These flags make the round trip exact (+0.01).
SWS = ["-sws_flags", "accurate_rnd+full_chroma_int+full_chroma_inp"]


def make_lut(g):
    x = np.arange(256, dtype=np.float32) / 255
    y = x * (2 ** g.get("exp", 0))
    y = y / (1 + max(0, g.get("exp", 0)) * 0.35 * y)               # soft shoulder so exposure lift doesn't clip
    y = np.clip(y, 0, 1)
    c, pv = g.get("contrast", 1.0), g.get("pivot", 0.45)
    y = np.clip(pv + (y - pv) * c, 0, 1)
    y = g.get("black", 0.0) + y * (1 - g.get("black", 0.0))
    lut = np.stack([y, y, y], 1)                                    # B G R
    sh = (1 - x) ** 2; hi = x ** 2
    lut[:, 0] += g.get("teal", 0) * sh - g.get("warm", 0) * hi     # B
    lut[:, 1] += g.get("teal", 0) * sh * 0.5
    lut[:, 2] += -g.get("teal", 0) * sh + g.get("warm", 0) * hi    # R
    return (np.clip(lut, 0, 1) * 255 + 0.5).astype(np.uint8).reshape(256, 1, 3)     # round (truncation lost 0.2 levels, 2026-11-26)


def radial(W, H, cx, cy, rx, ry):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    return np.exp(-(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2))


class Look:
    def __init__(s, e, W, H):
        g = e["grade"]; s.g = g; s.W, s.H = W, H
        s.lut = make_lut(g)
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        d = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H * 0.45) / (H * 0.62)) ** 2)
        s.vig = (1 - g.get("vignette", 0.3) * np.clip(d - 0.35, 0, 1) ** 1.6)[..., None].astype(np.float32)
        rng = np.random.default_rng(7)
        s.noise = rng.normal(0, 1, (H + 64, W + 64)).astype(np.float32)

    def aroll(s, img_u8, fx, fy, k):
        import cv2
        x = cv2.LUT(img_u8, s.lut).astype(np.float32) / 255
        lum = x @ np.float32([0.114, 0.587, 0.299])
        x = lum[..., None] + (x - lum[..., None]) * s.g.get("sat", 1.0)
        if s.g.get("face", 0):
            m = radial(s.W, s.H, fx, fy + 90 * k, 360 * k, 520 * k)[..., None]
            x = x * (1 + s.g["face"] * m)
        return x

    def broll(s, img_u8, sl):
        x = img_u8.astype(np.float32) / 255
        x = np.clip(x * sl.get("gain", 1.0), 0, 1) ** sl.get("gamma", 1.0)
        lum = x @ np.float32([0.114, 0.587, 0.299])
        sat = 0.0 if sl.get("bw") else sl.get("sat", 1.0)
        x = lum[..., None] + (x - lum[..., None]) * sat
        if sl.get("shade", True):
            m = radial(s.W, s.H, s.W / 2, s.H * 0.65, s.W * 0.75, s.H * 0.16)[..., None]
            x = x * (1 - 0.38 * m)
        return x

    def finish(s, x, fi):
        x = x * s.vig
        if s.g.get("grain", 0):
            o = (fi * 37) % 64, (fi * 53) % 64
            n = s.noise[o[0]:o[0] + s.H, o[1]:o[1] + s.W][..., None]
            x = x + n * s.g["grain"] * 0.5 * (0.35 + 0.65 * np.sqrt(np.clip(x, 0, 1)))
        return np.clip(x, 0, 1)


# ------------------------------------------------------------------ B-roll prep
def slot_dir(e, sl, k):
    return os.path.join(e["_dir"], "work", "broll", "%s_%s" % (sl["key"], "full" if k == 1 else "half"))


def prep_slots(e, k):
    fps = e["fps"]
    for sl in e.get("broll", []):
        d = slot_dir(e, sl, k); n = round(sl["t1"] * fps) - round(sl["t0"] * fps) + 2
        if os.path.isdir(d) and len(os.listdir(d)) >= n: continue
        os.makedirs(d, exist_ok=True)
        pr = subprocess.run([FF, "-i", sl["file"]], capture_output=True, text=True).stderr
        import re
        w, h = map(int, re.search(r"Video:.*?(\d{3,5})x(\d{3,5})", pr).groups())
        zmax = max(sl.get("z", [1, 1.06]))
        OW, OH = int(1080 * k * zmax) // 2 * 2, int(1920 * k * zmax) // 2 * 2
        if w / h > 9 / 16:
            cw, ch = int(h * 9 / 16) // 2 * 2, h; x = int(min(max(sl.get("cx", 0.5) * w - cw / 2, 0), w - cw)); y = 0
        else:
            cw, ch = w, int(w * 16 / 9) // 2 * 2; x = 0; y = int(min(max(sl.get("cy", 0.5) * h - ch / 2, 0), h - ch))
        vf = "setpts=PTS/%g,fps=%d,crop=%d:%d:%d:%d,scale=%d:%d:flags=lanczos" % (sl.get("speed", 1.0), fps, cw, ch, x, y, OW, OH)
        subprocess.run([FF, "-v", "error", "-y", "-ss", str(sl.get("src", 0)), "-i", sl["file"], "-vf", vf, "-frames:v", str(n)] + SWS + [
                        "-q:v", "2", os.path.join(d, "%05d.jpg")], check=True)
        print("prepped", sl["key"], n, "frames", (OW, OH))


# ------------------------------------------------------------------ frame renderer
class Renderer:
    def __init__(s, e, k):
        import cv2
        s.e, s.k = e, k; s.W, s.H = int(1080 * k), int(1920 * k)
        pr = subprocess.run([FF, "-i", e["src"]], capture_output=True, text=True).stderr
        import re
        s.sw, s.sh = map(int, re.search(r"Video:.*?(\d{3,5})x(\d{3,5})", pr).groups())
        s.look = Look(e, s.W, s.H)
        st = e["style"]; s.st = st
        s.seg = None; s.proc = None; s.next_src = None
        s.seg_mask = None; s.prev_mask = None; s.prev_fi = -9

    # source frames: one ffmpeg pipe per keep, read sequentially
    def src_frame(s, fi):
        for (of, f0, n) in s.e["_seg"]:
            if of <= fi < of + n: src_f = f0 + fi - of; break
        if s.proc is None or s.next_src != src_f:
            if s.proc: s.proc.kill()
            seg_end = f0 + n
            s.proc = subprocess.Popen([FF, "-v", "error", "-ss", "%.6f" % (src_f / s.e["fps"]), "-i", s.e["src"],
                                       "-frames:v", str(seg_end - src_f)] + SWS + ["-f", "rawvideo", "-pix_fmt", "bgr24", "-"],
                                      stdout=subprocess.PIPE, bufsize=s.sw * s.sh * 3 * 2)
        buf = s.proc.stdout.read(s.sw * s.sh * 3)
        s.next_src = src_f + 1
        return np.frombuffer(buf, np.uint8).reshape(s.sh, s.sw, 3)

    def person(s, img_u8, fi):
        import cv2
        if s.seg_mask is None:
            import mediapipe as mp
            s.seg_mask = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=0)
        small = cv2.resize(img_u8, (s.W // 2, s.H // 2), interpolation=cv2.INTER_AREA)
        m = s.seg_mask.process(cv2.cvtColor(small, cv2.COLOR_BGR2RGB)).segmentation_mask.astype(np.float32)
        if s.prev_mask is not None and fi == s.prev_fi + 1: m = 0.6 * m + 0.4 * s.prev_mask
        s.prev_mask, s.prev_fi = m, fi
        m = cv2.resize(m, (s.W, s.H), interpolation=cv2.INTER_LINEAR)
        m = cv2.GaussianBlur(np.clip((m - 0.35) / 0.3, 0, 1), (0, 0), 1.6 * s.k + 0.4)
        return m[..., None]

    def frame(s, fi):
        import cv2
        e, k, W, H, fps = s.e, s.k, s.W, s.H, s.e["fps"]; t = fi / fps
        src = s.src_frame(fi)
        sc = cam_scale(e, t)
        M, fx, fy = cam_matrix(e, sc, W, H, s.sw, s.sh, k)
        a_u8 = cv2.warpAffine(src, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        x = s.look.aroll(a_u8, fx, fy, k)
        _pm = []
        def PM():                                              # person matte of this frame, computed once
            if not _pm: _pm.append(s.person((np.clip(x, 0, 1) * 255).astype(np.uint8), fi))
            return _pm[0]
        need_pm = any(round(ly["t0"] * fps) <= fi < round(ly["t1"] * fps) and ly.get("behind", True) for ly in e.get("layers", []))
        need_pm = need_pm or any(pp["t0"] <= t < pp["t1"] for pp in e.get("paper", []))
        if need_pm: PM()                                       # matte from the clean frame, before any dim
        s.on_paper = None
        # dim-and-overlay (speaker darker + defocused; the overlay itself is a front layer)
        for dm in e.get("dims", []):
            if dm["t0"] <= t < dm["t1"]:
                fd = dm.get("fade", 0.25); pd = EASE["sine"](max(0.0, min(1.0, (t - dm["t0"]) / fd, (dm["t1"] - t) / fd)))
                kb = int(dm.get("blur", 0) * k * pd) * 2 + 1
                if kb > 1: x = cv2.GaussianBlur(x, (kb, kb), 0)
                x = x * (1 - (1 - dm.get("amt", 0.46)) * pd)
        # RGBA layers behind the speaker (pedestals, objects rising behind the head): his room stays visible around them
        for ly in e.get("layers", []):
            f0 = round(ly["t0"] * fps)
            if f0 <= fi < round(ly["t1"] * fps) and ly.get("behind", True):
                im = s.layer_img(ly, fi - f0)
                if im is not None:
                    la = im[..., 3:4] * (1 - PM()); x = x * (1 - la) + im[..., :3] * la
        # paper scene (aesthetic-pro-reel-edit-style, 2026-11-25): room -> textured off-white paper, speaker cut out with a soft shadow
        for pp in e.get("paper", []):
            if pp["t0"] <= t < pp["t1"]:
                pm = PM(); bg = s.paper_bg(pp.get("color", "#EFE7D6")).copy()
                sh = cv2.GaussianBlur(np.roll(np.roll(pm[..., 0], int(18 * k), 0), int(10 * k), 1), (0, 0), 22 * k)
                bg *= (1 - 0.22 * sh)[..., None]
                if pp.get("ribbon"): s.ribbon(bg, pp["ribbon"], t - pp["t0"], pp.get("path", "swoosh"))
                x = bg * (1 - pm) + x * pm
                s.on_paper = pp
                break
        # mirror split (self-conversation)
        for mr in e.get("mirror", []):
            if mr["t0"] <= t < mr["t1"]:
                p = min(1, (t - mr["t0"]) / 0.12); pw = W // 2
                c0 = int(fx - pw / 2); c0 = min(max(c0, 0), W - pw)
                panel = x[:, c0:c0 + pw].copy()
                y = np.empty_like(x); y[:, :pw] = panel; y[:, pw:] = panel[:, ::-1]
                off = int((1 - EASE["out3"](p)) * pw)
                if off: y[:, pw:] = np.roll(y[:, pw:], off, axis=1); y[:, pw:pw + off] = x[:, pw:pw + off]
                y[:, pw - max(1, int(3 * k)):pw + max(1, int(3 * k))] *= 0.15
                x = y
        # giants (behind subject uses the A-roll person mask)
        gl = None
        for g in e.get("giants", []):
            if g["t0"] <= t < g["t1"]:
                if gl is None: gl = np.zeros((H, W, 4), np.float32)
                txt, col = g["text"], g.get("color", "#FFFFFF"); sy = 1.0
                sw_ = g.get("swap")
                if sw_:
                    if t >= sw_["t"]: txt, col = sw_["text"], sw_.get("color", col)
                    d = (t - sw_["t"]) * fps
                    if -3 <= d < 0: sy = max(0.05, -d / 3)
                    elif 0 <= d < 4: sy = max(0.05, d / 4)
                sz = int(g["size"] * k)
                sp = sprite(txt, g.get("font", s.st["giant_font"]), sz, col, shadow=False, glow=g.get("glow", 0.35))
                maxw = g.get("max_w", 1000) * k
                fit = min(1.0, maxw / max(sp[3], 1))
                p = (t - g["t0"]) * fps
                slam = 1 + g.get("slam", 0.18) * max(0, 1 - p / 5) ** 2
                al = min(1, p / 2 + 0.35)
                layer_blit(gl, sp, W / 2, g["y"] * k, fit * slam, al, sy)
                gk = g.get("strike")
                if gk and t >= gk["t"]:                        # "not X" on a giant: bar wipes across the ink in 0.12 s (behind the head too)
                    ps = EASE["out3"](min(1.0, (t - gk["t"]) / 0.12)); bw_ = sp[3] * fit * slam + 40 * k
                    x0 = int(W / 2 - bw_ / 2); y0 = int(g["y"] * k + gk.get("dy", 0) * k - gk.get("h", 22) * k / 2)
                    gl[y0:y0 + int(gk.get("h", 22) * k), x0:x0 + int(bw_ * ps), :3] = np.array(hex2bgr(gk.get("c", "#D24E5A")), np.float32) / 255
                    gl[y0:y0 + int(gk.get("h", 22) * k), x0:x0 + int(bw_ * ps), 3] = 1.0
        if gl is not None:
            behind = any(g["t0"] <= t < g["t1"] and g.get("behind", True) for g in e.get("giants", []))
            pm = PM() if behind else 0
            ga = gl[..., 3:4] * (1 - pm)
            x = x * (1 - ga) + gl[..., :3] * ga
        # B-roll slots replace the frame
        for sl in e.get("broll", []):
            f0, f1 = round(sl["t0"] * fps), round(sl["t1"] * fps)
            if f0 <= fi < f1:
                j = fi - f0
                img = cv2.imread(os.path.join(slot_dir(e, sl, k), "%05d.jpg" % (j + 1)))
                z0, z1 = sl.get("z", [1.0, 1.06]); zmax = max(z0, z1)
                z = z0 + (z1 - z0) * (j / max(1, f1 - f0 - 1))
                ent = sl.get("entry", "cut"); pe = j / 6.0
                bz = z
                if ent == "blurzoom" and pe < 1: bz = z * (1 + 0.22 * (1 - EASE["out3"](pe)))
                sc_ = bz / zmax
                Mb = np.float32([[sc_, 0, W / 2 - img.shape[1] * sc_ / 2], [0, sc_, H / 2 - img.shape[0] * sc_ / 2]])
                b = cv2.warpAffine(img, Mb, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
                if ent in ("whip", "whipL") and pe < 1:
                    q = 1 - EASE["out3"](pe); dx = int((1 if ent == "whip" else -1) * q * 0.35 * W)
                    b = np.roll(b, dx, axis=1); kl = int(2 + q * 90 * k)
                    b = cv2.blur(b, (kl, 1))
                if ent == "blurzoom" and pe < 1:
                    kb = int(1 + (1 - pe) * 24 * k) | 1; b = cv2.GaussianBlur(b, (kb, kb), 0)
                x = s.look.broll(b, sl)
                break
        # RGBA layers in front (overlays on the speaker or on a cutaway)
        for ly in e.get("layers", []):
            f0 = round(ly["t0"] * fps)
            if f0 <= fi < round(ly["t1"] * fps) and not ly.get("behind", True):
                im = s.layer_img(ly, fi - f0)
                if im is not None: x = x * (1 - im[..., 3:4]) + im[..., :3] * im[..., 3:4]
        # viewfinder brackets
        for br in e.get("brackets", []):
            if br["t0"] <= t < br["t1"]:
                p = min(1, (t - br["t0"]) * fps / 5); gs = 1 + 0.18 * (1 - EASE["out3"](p))
                bw_, bh_ = br["w"] * k * gs / 2, br["h"] * k * gs / 2; cy = fy + br.get("dy", 40) * k
                col = np.array(hex2bgr(br.get("color", s.st["accent"])), np.float32) / 255; L = int(70 * k); th = max(2, int(7 * k))
                if br.get("shape") == "ring":                  # thin glowing circle round the face (prime_animator, 2026-11-25)
                    m = np.zeros((H * 2, W * 2), np.uint8)
                    cv2.circle(m, (int(fx * 2), int(cy * 2)), int(bw_ * 2), 255, max(2, int(4 * k)) * 2, cv2.LINE_AA)
                    m = cv2.resize(m, (W, H), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
                    gw = cv2.GaussianBlur(m, (0, 0), 9 * k) * 1.6
                    a_ = np.clip(m + gw * 0.55, 0, 1)[..., None] * min(1.0, p * 1.6)
                    x = x * (1 - a_) + col * a_
                else:
                    th_ = max(2, int(br.get("th", 7) * k)); th = th_
                    for sx_ in (-1, 1):
                        for sy_ in (-1, 1):
                            X, Y = int(fx + sx_ * bw_), int(cy + sy_ * bh_)
                            xs = sorted((X, X - sx_ * L)); ys = sorted((Y, Y - sy_ * L))
                            x[max(0, Y - th // 2):Y + th // 2 + 1, max(0, xs[0]):xs[1]] = col
                            x[max(0, ys[0]):ys[1], max(0, X - th // 2):X + th // 2 + 1] = col
                if br.get("label") and p >= 1:                 # mono HUD label + live centre coordinates (viashaan "FACE 0.939 X 0700")
                    mf = s.st.get("mono_font", os.path.join(FONT_DIR, "CourierPrime-Bold.ttf"))
                    hx = "#%02X%02X%02X" % tuple(int(c * 255) for c in col[::-1])
                    lx = fx - bw_ + (0 if br.get("shape") != "ring" else bw_ * 0.30)
                    for li, ln in enumerate((br["label"], "X %04d  Y %04d" % (int(fx / k), int(cy / k)))):
                        sp = sprite(ln, mf, int(26 * k), hx, shadow=True)
                        blit(x, sp, lx + sp[3] / 2, cy - bh_ - (58 - li * 30) * k)
        # word stacks (2026-11-25, text-animation-moves): the stack IS the caption for its sentence
        stack_up = False
        for sk in e.get("stacks", []):
            if sk["t0"] <= t < sk["t1"]: x = s.stack(x, sk, t, PM); stack_up = True
        # captions (hidden while a giant or a word stack is up)
        if not stack_up and not any(g["t0"] <= t < g["t1"] for g in e.get("giants", [])):
            for cp in e.get("captions", []):
                if cp["t0"] <= t < cp["t1"]: s.caption(x, cp, t); break
        # flashes
        for fl in e.get("flashes", []):
            d = fi - round(fl["t"] * fps)
            if fl["type"] == "white" and 0 <= d < 3: x = x + (1 - x) * [0.85, 0.45, 0.15][d]
            if fl["type"] == "neg" and 0 <= d < 3:
                if d < 2:
                    l = x @ np.float32([0.114, 0.587, 0.299]); x = np.repeat((1 - l)[..., None], 3, 2) * 0.9
                else: x = x * 0.0
        for ds in e.get("desat", []):                          # black-and-white stretch (after captions, so they turn grey too)
            if ds["t0"] <= t < ds["t1"]:
                fd = ds.get("fade", 0.12); pg = max(0.0, min(1.0, (t - ds["t0"]) / fd, (ds["t1"] - t) / fd)) * ds.get("amt", 1.0)
                lm = (x @ np.float32([0.114, 0.587, 0.299]))[..., None]; x = x * (1 - pg) + lm * pg
        return s.look.finish(x, fi)

    def caption(s, x, cp, t):
        st, k, fps = s.st, s.k, s.e["fps"]
        acc = st["accent"]
        n_words = [w for w in cp["words"] if w[2] != "k"]; k_words = [w for w in cp["words"] if w[2] == "k"]
        cy = cp.get("y", st["cap_y"]) * k
        csz = int(st["cap_size"] * k * (1.0 if k_words else 1.08))
        pp = getattr(s, "on_paper", None)                      # paper scene: ink text, deeper haldi keyword, no outline
        stroke_k = pp.get("stroke", 0) if pp else st.get("stroke", 0)     # 2026-11-26: paper "stroke" keeps the outline when captions sit on the shirt
        def pcol(c):
            if not pp: return c
            if c.upper() == acc.upper(): return pp.get("key", "#B9831A")
            if c.upper() in ("#FFFFFF", "#F4EFE3", st.get("cap_color", "#FFFFFF").upper()): return pp.get("text", "#1A1410")
            return c
        # line 1: reserve full width, words pop in place
        if n_words:
            cc = st.get("cap_color", "#FFFFFF")                # 2026-11-25: lead-in colour (cream) + per-word "c" (mustard-red style)
            sps = [sprite(w[1], st["cap_font"], csz, pcol(w[3].get("c", cc) if len(w) > 3 else cc),
                          stroke=int(stroke_k * k * 0.7)) for w in n_words]
            space = csz * 0.28; tot = sum(sp[3] for sp in sps) + space * (len(sps) - 1)
            fit = min(1.0, st.get("key_max_w", 900) * k / max(tot, 1)); tot *= fit
            xx = x.shape[1] / 2 - tot / 2; ly = cy - (csz * 0.62 if k_words else 0)
            for w, sp in zip(n_words, sps):
                wd = sp[3] * fit
                if t >= w[0]:
                    if st.get("reveal") == "blur":
                        rs, ra, rz = s.reveal(sp, t - w[0]); blit(x, rs, xx + wd / 2, ly, fit * rz, ra)
                    else:
                        p = (t - w[0]) * fps; pop = 1 + 0.10 * max(0, 1 - p / 4)
                        blit(x, sp, xx + wd / 2, ly, fit * pop)
                elif st.get("ghost"):                           # ghost words: the line waits faint, each word goes solid on its time
                    blit(x, sp, xx + wd / 2, ly, fit, st["ghost"])
                xx += wd + space * fit
        for w in k_words:
            if t >= w[0]:
                o = w[3] if len(w) > 3 else {}
                col = o.get("c", acc)
                if pp and not o.get("brush"): col = pcol(col)
                ksz = int(st["key_size"] * k * o.get("size", 1.0))
                ky = cy + (ksz * 0.55 if n_words else 0)
                kf = s.key_font(o.get("font"))
                if o.get("fx") in ("track", "stagger"):
                    kw = s.key_letters(x, w[1], ksz, col, ky, t - w[0], o["fx"], kf)
                else:
                    sp = sprite(w[1], kf, ksz, col, stroke=int(stroke_k * k), glow=0.0 if pp else o.get("glow", 0.0))
                    fit = min(1.0, st.get("key_max_w", 900) * k / max(sp[3], 1))
                    p = (t - w[0]) * fps; pop = 1 + 0.16 * max(0, 1 - p / 5) ** 2; ra = 1.0; rs = sp
                    if st.get("reveal") == "blur": rs, ra, pop = s.reveal(sp, t - w[0])
                    if o.get("brush"): s.haldi_brush(x, o["brush"], sp[3] * fit, sp[2] * fit, ky, t - w[0])
                    blit(x, rs, x.shape[1] / 2, ky, fit * pop, ra); kw = sp[3] * fit
                    if o.get("dot"): s.kumkum_dot(x, o["dot"], w[1], kf, ksz, kw, fit, ky, t - w[0])
                sk = o.get("strike")
                if sk and t >= sk["t"]:                         # "not X": line through the keyword, wipes in 0.12 s
                    ps = EASE["out3"](min(1.0, (t - sk["t"]) / 0.12)); bc = np.array(hex2bgr(sk.get("c", "#FF4338")), np.float32) / 255
                    x0 = int(x.shape[1] / 2 - kw / 2 - 14 * k); y0 = int(ky - 4 * k); x1 = x0 + int((kw + 28 * k) * ps)
                    x[y0 + int(6 * k):y0 + int(22 * k), x0 + int(4 * k):x1 + int(4 * k)] *= 0.4
                    x[y0:y0 + int(16 * k), x0:x1] = bc
                if o.get("bar"):                                # pivot underline: wipes left to right in 0.1 s, 0.05 s after the word
                    pb = EASE["out3"](max(0.0, min(1.0, (t - w[0] - 0.05) / 0.10)))
                    if pb > 0:
                        bc = np.array(hex2bgr(o["bar"] if isinstance(o["bar"], str) else acc), np.float32) / 255
                        y0 = int(ky + ksz * 0.50); x0 = int(x.shape[1] / 2 - kw / 2)
                        x[y0 + int(6 * k):y0 + int(20 * k), x0 + int(4 * k):x0 + int(4 * k) + int(kw * pb)] *= 0.35     # soft drop shadow
                        x[y0:y0 + int(14 * k), x0:x0 + int(kw * pb)] = bc

    def key_font(s, name):
        """Keyword font: None = style.key_font, "serif" = style.serif_font, "script" = style.script_font (2026-11-25),
        or a font file (absolute path or a file name inside skills/fonts-and-colours/assets/fonts)."""
        st = s.st
        if not name: return st["key_font"]
        if name == "serif": return st.get("serif_font", st["key_font"])
        if name == "script": return st.get("script_font", st.get("serif_font", st["key_font"]))
        if os.path.isabs(name): return name
        return os.path.join(FONT_DIR, name)

    def reveal(s, sp, age, D=0.18):
        """aesthetic-pro-reel-edit-style (2026-11-25): blur-to-sharp word arrival (amro.films, viashaan). Returns (sprite, alpha, scale).
        Starts ON the word (never early), 35 % alpha + 4 blur steps -> sharp in 0.18 s, scale 1.05 -> 1."""
        import cv2
        if age >= D: return sp, 1.0, 1.0
        q = EASE["out3"](max(0.0, age) / D); L = int(round((1 - q) * 4))
        al, z = 0.35 + 0.65 * q, 1 + 0.05 * (1 - q)
        if L == 0: return sp, al, z
        key = ("rv", id(sp[0]), L)
        if key not in _SPR:
            img = sp[0]; a = img[..., 3:4]; sg = L * max(1.2, sp[2] * 0.03)
            pa = cv2.GaussianBlur(np.ascontiguousarray(img[..., :3] * a), (0, 0), sg)
            A = cv2.GaussianBlur(np.ascontiguousarray(a[..., 0]), (0, 0), sg)[..., None]
            _SPR[key] = (np.dstack([pa / np.maximum(A, 1e-4), A]).astype(np.float32), sp[1], sp[2], sp[3])
        return _SPR[key], al, z

    def paper_bg(s, colr):
        """off-white paper for the paper scene: base colour + soft blotches + fibre noise (static, cached)."""
        import cv2
        key = ("paper", colr, s.W, s.H)
        if key not in _SPR:
            rng = np.random.default_rng(11)
            base = np.array(hex2bgr(colr), np.float32) / 255
            blot = cv2.resize(rng.normal(0, 1, (12, 7)).astype(np.float32), (s.W, s.H), interpolation=cv2.INTER_CUBIC)
            fib = cv2.GaussianBlur(rng.normal(0, 1, (s.H, s.W)).astype(np.float32), (0, 0), 0.7)
            sh = 1 + 0.022 * blot + 0.018 * fib
            _SPR[key] = np.clip(base[None, None, :] * sh[..., None], 0, 1).astype(np.float32)
        return _SPR[key]

    def ribbon(s, bg, colr, dt, path="swoosh"):
        """haldi ribbon swoosh across the paper, behind the speaker; draws on along its length in 0.45 s (viashaan's bronze curve, our haldi)."""
        import cv2
        W, H = s.W, s.H; p = EASE["out3"](min(1.0, max(0.0, dt) / 0.45))
        u = np.linspace(0, 1, 240)[: max(2, int(240 * p))]
        if path == "swoosh":
            px = (-0.12 + 1.24 * u) * W
            py = H * (0.30 + 0.11 * np.sin(u * 2 * np.pi * 0.85 + 0.5) + 0.10 * u)
        else:                                                   # "arc": a loop behind the head
            px = W * (0.5 + 0.42 * np.cos(np.pi * (1.1 - 1.6 * u))); py = H * (0.30 - 0.14 * np.sin(np.pi * (1.1 - 1.6 * u)))
        S = 2; m = np.zeros((H * S, W * S), np.uint8)
        pts = np.stack([px * S, py * S], 1).astype(np.int32).reshape(-1, 1, 2)
        cv2.polylines(m, [pts], False, 255, int(0.050 * W * S), cv2.LINE_AA)
        m = cv2.resize(m, (W, H), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
        shd = cv2.GaussianBlur(np.roll(m, int(14 * s.k), 0), (0, 0), 10 * s.k)
        bg *= (1 - 0.18 * shd)[..., None]
        col = np.array(hex2bgr(colr), np.float32) / 255
        tex = 0.93 + 0.07 * np.sin(np.arange(H, dtype=np.float32)[:, None] * 0.9)   # fine dry-brush streaks
        a = (m * 0.96)[..., None]
        bg[:] = bg * (1 - a) + (col[None, None, :] * tex[..., None]) * a

    def haldi_brush(s, x, colr, kw, kh, ky, dt):
        """mustard-red-caption-style (2026-11-25): textured turmeric brush stroke behind the lower half of the keyword,
        wipes left to right in 0.22 s, 0.03 s after the word. Highlighter, not a slab (mistakes-to-avoid 9)."""
        import cv2
        pb = EASE["out3"](max(0.0, min(1.0, (dt - 0.03) / 0.22)))
        if pb <= 0: return
        bw, bh = max(8, int(kw * 1.10)), max(8, int(kh * 0.50))
        key = ("brush", bw, bh, colr)
        if key not in _SPR:
            rng = np.random.default_rng(bw * 31 + bh)
            yy, xx = np.mgrid[0:bh, 0:bw].astype(np.float32)
            xs = np.arange(bw, dtype=np.float32)
            top = bh * 0.12 + bh * 0.07 * np.sin(xs / bw * 9.0 + 1.3) + np.cumsum(rng.normal(0, 0.5, bw)) * bh * 0.004
            bot = bh * 0.90 - bh * 0.06 * np.sin(xs / bw * 7.0)
            a = ((yy >= top[None, :]) & (yy <= bot[None, :])).astype(np.float32)
            a *= 0.80 + 0.20 * rng.random(bh).astype(np.float32)[:, None]          # dry-brush rows
            a *= np.clip(np.minimum(xx / (bh * 0.9), (bw - xx) / (bh * 0.5)), 0, 1) ** 0.6   # soft ends
            a = cv2.GaussianBlur(a, (0, 0), 1.2) * 0.88
            col = np.array(hex2bgr(colr), np.float32) / 255
            _SPR[key] = (np.dstack([np.broadcast_to(col, (bh, bw, 3)), a]).astype(np.float32), 0, bh, bw)
        img = _SPR[key][0]; cut = max(1, int(bw * pb))
        blit(x, (np.ascontiguousarray(img[:, :cut]), 0, bh, cut), x.shape[1] / 2 - bw / 2 + cut / 2, ky + kh * 0.16)

    def kumkum_dot(s, x, colr, text, kf, ksz, kw, fit, ky, dt):
        """mustard-red-caption-style (2026-11-25): a small vermilion dot sits on the keyword's baseline, right after it,
        0.12 s after the word (pops from 1.5x in 0.12 s). The client's signature full stop; one per statement at most."""
        import cv2
        d = dt - 0.12
        if d < 0 or text.rstrip()[-1:] in "?!.,": return      # never a dot after punctuation
        f = font(kf, ksz); _, t_, _, b_ = f.getbbox(text); asc = f.getmetrics()[0]
        base = ky + (asc - (t_ + b_) / 2) * fit
        q = EASE["out3"](min(1.0, d / 0.12)); r = max(4.0, ksz * fit * 0.072) * (1.5 - 0.5 * q)
        cx, cy = x.shape[1] / 2 + kw / 2 + ksz * fit * 0.17, base - ksz * fit * 0.075
        R = int(r * 2.5 + 8); x0, y0 = max(0, int(cx) - R), max(0, int(cy) - R); x1, y1 = min(x.shape[1], int(cx) + R), min(x.shape[0], int(cy) + R)
        if x0 >= x1 or y0 >= y1: return
        roi = x[y0:y1, x0:x1]; SS = 4
        def disc(ox, oy, rr):
            m = np.zeros(((y1 - y0) * SS, (x1 - x0) * SS), np.uint8)
            cv2.circle(m, (int((cx - x0 + ox) * SS), int((cy - y0 + oy) * SS)), int(rr * SS), 255, -1, cv2.LINE_AA)
            return cv2.resize(m, (x1 - x0, y1 - y0), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
        sh = cv2.GaussianBlur(disc(0, ksz * fit * 0.03, r * 1.15), (0, 0), max(1.0, r * 0.45))
        roi *= (1 - 0.45 * sh[..., None])
        m = disc(0, 0, r); col = np.array(hex2bgr(colr), np.float32) / 255
        roi[:] = roi * (1 - m[..., None]) + col * m[..., None]

    def key_letters(s, x, text, ksz, col, ky, dt, fx, kf=None):
        """P13 keyword drawn letter by letter. track: letter-spacing eases from wide to normal over 0.2 s (it starts ON the word,
        full opacity: house rule "never early"). stagger: letters arrive one at a time 0.065 s apart, each rising half an em."""
        st, k = s.st, s.k
        kf = kf or st["key_font"]
        f = font(kf, ksz); n = len(text)
        adv = [f.getlength(text[:i]) for i in range(n + 1)]; tot = adv[-1]
        T, B = f.getbbox(text)[1], f.getbbox(text)[3]
        fit = min(1.0, st.get("key_max_w", 900) * k / max(tot, 1))
        q = 1 - EASE["out3"](min(1.0, max(0.0, dt / 0.2)))
        extra = 0.0
        if fx == "track" and n > 1: extra = min(0.5 * ksz, max(0.0, (1000 * k / fit - tot) / (n - 1))) * q
        W = x.shape[1]; x0 = W / 2 - (tot + extra * (n - 1)) * fit / 2
        for i, ch in enumerate(text):
            if ch == " ": continue
            l, t_, r, b = f.getbbox(ch)
            cx = x0 + (adv[i] + extra * i + (l + r) / 2) * fit; yy = ky + ((t_ + b) / 2 - (T + B) / 2) * fit; al = 1.0
            if fx == "stagger":
                d = dt - i * 0.065
                if d < 0: continue
                pp = min(1.0, d / 0.10); yy += (1 - EASE["out3"](pp)) * 0.5 * ksz * fit; al = 0.6 + 0.4 * pp
            blit(x, sprite(ch, kf, ksz, col, stroke=int(st.get("stroke", 0) * k)), cx, yy, fit, al)
        return tot * fit

    # ---------------------------------------------------------------- word stacks (text-animation-moves skill, 2026-11-25)
    def stack(s, x, sk, t, PM):
        """A phrase that builds word by word into a tight stack of 2-5 lines in the empty part of the frame (wall above the
        head, or beside an off-centre speaker). Measured on pro reels: small link words (~0.42 of the big size) between big
        meaning words, mixed sizes can share a baseline ("have" + "to"), lines almost touch, the whole stack clears on a hard
        cut when the sentence ends and the next one builds on the other side. The layout is fixed from all tokens first, so
        words never shift while the stack builds. Returns x (new array when behind=true)."""
        import zlib
        st, k, W = s.st, s.k, x.shape[1]
        big = sk.get("size", st.get("stack_size", 128)); ratio = sk.get("ratio", st.get("stack_ratio", 0.42))
        f_big = s.key_font(sk.get("font")) if sk.get("font") else st.get("stack_font", st["cap_font"])
        f_small = st.get("stack_small_font", f_big)
        c_small = sk.get("cs", st.get("cap_color", "#FFFFFF")); c_big = sk.get("c", st.get("stack_color", c_small))
        lines = sk["lines"]

        def tok(tk, fit):
            o = tk[3] if len(tk) > 3 else {}
            isb = tk[2] == "b"
            pth = s.key_font(o["font"]) if o.get("font") else (f_big if isb else f_small)
            sz = max(8, int(round(big * (1.0 if isb else ratio) * o.get("size", 1.0) * fit * k)))
            f = font(pth, sz); l_, t_, r_, b_ = f.getbbox(tk[1]); asc = f.getmetrics()[0]
            return dict(t=tk[0], text=tk[1], o=o, path=pth, size=sz, isb=isb, col=o.get("c", c_big if isb else c_small),
                        w=r_ - l_, up=asc - t_, dn=b_ - asc, l=l_, asc=asc, f=f)

        def layout(fit):
            L = []
            for ln in lines:
                ts = [tok(tk, fit) for tk in ln]
                gaps = [0.24 * min(a["size"], b["size"]) for a, b in zip(ts, ts[1:])]
                L.append((ts, gaps, sum(z["w"] for z in ts) + sum(gaps)))
            return L, max(z[2] for z in L)
        L, bw = layout(1.0)
        fit = min(1.0, sk.get("max_w", 900) * k / max(bw, 1))
        if fit < 0.999: L, bw = layout(fit)
        align = sk.get("align", "center"); bx = sk.get("x", 540) * k; y = sk.get("y", 330) * k
        lead = sk.get("lead", st.get("stack_lead", 0.06)) * big * k * fit
        gl = np.zeros(x.shape[:2] + (4,), np.float32)
        out_a = 1.0
        if sk.get("out") == "fade": out_a = max(0.0, min(1.0, (sk["t1"] - t) / 0.10))
        prev_dn = None
        for li, (ts, gaps, lw) in enumerate(L):
            up = max(z["up"] for z in ts); dn = max(max(z["dn"] for z in ts), 0)
            base = y + up if prev_dn is None else base + prev_dn * 0.55 + lead + up    # descenders may tuck under the next line
            prev_dn = dn
            if align == "left": x0 = bx - bw / 2
            elif align == "right": x0 = bx + bw / 2 - lw
            elif align == "stagger": x0 = bx - lw / 2 + (-1 if li % 2 == 0 else 1) * sk.get("stagger", 70) * k * fit
            else: x0 = bx - lw / 2
            for z, g in zip(ts, gaps + [0]):
                s.stack_token(gl, z, x0, base, t, sk, zlib)
                x0 += z["w"] + g
        a = gl[..., 3:4] * out_a
        if sk.get("behind"): a = a * (1 - PM())
        return x * (1 - a) + gl[..., :3] * a

    def stack_token(s, gl, z, x0, base, t, sk, zlib):
        """one stack word. fx (token opt, else stack "fx", else style "stack_fx", else fade):
        cut = on the frame, no move (yp.motionstudio slam) | fade = 0.10 s (small) / 0.17 s (big) |
        blur = blur-to-sharp 0.18 s | rise = slides up 0.35 em while fading, 0.20 s |
        grain = speckled dither dissolve, 0.10 s (yp.motionstudio) | pop = 1.12 -> 1 in 5 frames |
        type = letters appear one by one across the spoken word, each fading in over 0.07 s (shami.mp4 pro edit, "everyone")."""
        st, fps = s.st, s.e["fps"]
        o = z["o"]; age = t - z["t"]
        ghost = sk.get("ghost", st.get("stack_ghost", 0.0))
        if age < 0 and not ghost: return
        stk = int(o.get("stroke", sk.get("stroke", st.get("stack_stroke", 0))) * s.k)   # ink outline: needed on the checked shirt (lower zone)
        sp = sprite(z["text"], z["path"], z["size"], z["col"], shadow=sk.get("shadow", True), glow=o.get("glow", 0.0), stroke=stk)
        cx = x0 + z["w"] / 2; cy = base - z["up"] + sp[2] / 2
        if age < 0:
            layer_blit(gl, sp, cx, cy, 1.0, ghost); return
        fx = o.get("fx", sk.get("fx", st.get("stack_fx", "fade")))
        if fx == "type":
            text, f = z["text"], z["f"]; n = max(1, len([c for c in text if c != " "]))
            dur = o.get("dur", min(0.6, max(0.15, 0.045 * n))); ox = x0 - z["l"]; j = 0
            for i, ch in enumerate(text):
                if ch == " ": continue
                d = age - j * dur / n; j += 1
                if d < 0: break
                l_, t_, r_, b_ = f.getbbox(ch)
                csp = sprite(ch, z["path"], z["size"], z["col"], shadow=sk.get("shadow", True), glow=o.get("glow", 0.0), stroke=stk)
                layer_blit(gl, csp, ox + f.getlength(text[:i]) + (l_ + r_) / 2, base + (t_ + b_) / 2 - z["asc"],
                           1.0, EASE["out3"](min(1.0, d / 0.07)))
            return
        if fx == "cut":
            layer_blit(gl, sp, cx, cy); return
        if fx == "blur":
            rs, ra, rz = s.reveal(sp, age); layer_blit(gl, rs, cx, cy, rz, ra); return
        if fx == "pop":
            p = age * fps; layer_blit(gl, sp, cx, cy, 1 + 0.12 * max(0, 1 - p / 5) ** 2); return
        if fx == "grain":
            D = o.get("d", 0.10); q = min(1.0, age / D)
            if q >= 1: layer_blit(gl, sp, cx, cy); return
            img = sp[0]; rng = np.random.default_rng(zlib.crc32(z["text"].encode()))
            nz = rng.random(img.shape[:2], dtype=np.float32)
            g2 = img.copy(); g2[..., 3] *= (nz < 0.15 + 0.85 * q)
            layer_blit(gl, (g2, sp[1], sp[2], sp[3]), cx, cy); return
        if fx == "rise":
            D = o.get("d", 0.20); q = EASE["out3"](min(1.0, age / D))
            layer_blit(gl, sp, cx, cy + (1 - q) * 0.35 * z["size"], 1.0, q); return
        D = o.get("d", 0.17 if z["isb"] else 0.10)
        layer_blit(gl, sp, cx, cy, 1.0, EASE["out3"](min(1.0, age / D)))

    def layer_img(s, ly, j):
        import cv2
        img = cv2.imread(os.path.join(ly["dir"], "%05d.png" % (j + 1)), cv2.IMREAD_UNCHANGED)
        if img is None or img.ndim < 3 or img.shape[2] < 4: return None
        if img.shape[1] != s.W: img = cv2.resize(img, (s.W, s.H), interpolation=cv2.INTER_AREA)
        return img.astype(np.float32) / 255


def worker(args):
    import cv2
    edl, k, fr, out = args
    e = load(edl); r = Renderer(e, k)
    for fi in fr:
        x = r.frame(fi)
        cv2.imwrite(os.path.join(out, "%06d.jpg" % fi), (x * 255 + 0.5).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])
    if r.proc: r.proc.kill()
    return len(fr)


def cmd_video(edl, stills=None):
    import multiprocessing as mpc
    e = load(edl); k = arg("--scale", 1.0, float); fps = e["fps"]
    prep_slots(e, k)
    if stills:
        out = os.path.join(e["_dir"], "work", "stills"); os.makedirs(out, exist_ok=True)
        for f in os.listdir(out): os.remove(os.path.join(out, f))
        frs = [min(e["_N"] - 1, round(float(t) * fps)) for t in stills.split(",")]
        jobs = [(edl, k, [f], out) for f in frs]
    else:
        out = os.path.join(e["_dir"], "work", "frames" + ("" if k == 1 else "_half")); os.makedirs(out, exist_ok=True)
        a = round(arg("--from", 0, float) * fps); b = min(e["_N"], round(arg("--to", 1e9, float) * fps))
        todo = [f for f in range(a, b) if not os.path.exists(os.path.join(out, "%06d.jpg" % f))]
        nw = arg("--workers", 6, int); ch = math.ceil(len(todo) / nw) if todo else 0
        jobs = [(edl, k, todo[i:i + ch], out) for i in range(0, len(todo), ch)] if todo else []
    with mpc.get_context("spawn").Pool(min(len(jobs), arg("--workers", 6, int)) or 1) as pool:
        print("rendered", sum(pool.map(worker, jobs)), "frames ->", out)
    if stills:
        files = sorted(os.listdir(out)); cols = min(6, len(files))
        subprocess.run([FF, "-v", "error", "-y", "-pattern_type", "glob", "-i", os.path.join(out, "*.jpg"), "-vf",
                        "scale=270:-1,tile=%dx%d" % (cols, math.ceil(len(files) / cols)), "-frames:v", "1",
                        os.path.join(e["_dir"], "work", "stills_sheet.jpg")], check=True)
        print("sheet:", os.path.join(e["_dir"], "work", "stills_sheet.jpg"))
        return
    if a == 0 and b == e["_N"]:
        v = os.path.join(e["_dir"], "work", "video%s.mp4" % ("" if k == 1 else "_half"))
        subprocess.run([FF, "-v", "error", "-y", "-framerate", str(fps), "-i", os.path.join(out, "%06d.jpg"), "-frames:v", str(e["_N"])] + SWS + [
                        "-vf", "scale=in_range=pc:in_color_matrix=bt601:out_range=tv:out_color_matrix=bt709,format=yuv420p",
                        "-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "16",
                        "-g", str(fps), "-keyint_min", str(fps), "-sc_threshold", "0", "-flags", "+cgop",   # keyframe every 1 s, closed GOP (scrubs in Premiere)
                        "-x264-params", "colorprim=bt709:transfer=bt709:colormatrix=bt709",
                        "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-an", v], check=True)
        print("encoded", v)


# ------------------------------------------------------------------ audio
def rd(p):
    from scipy.io import wavfile
    if not p.lower().endswith(".wav"):                       # mp3 etc: decode once next to the project audio
        tmp = os.path.join(os.path.dirname(os.path.abspath(sys.argv[2])), "audio", os.path.basename(p) + ".wav")
        if not os.path.exists(tmp):
            subprocess.run([FF, "-v", "error", "-y", "-i", p, "-ac", "2", "-ar", str(SR), "-c:a", "pcm_f32le", tmp], check=True)
        p = tmp
    sr, a = wavfile.read(p)
    a = a.astype(np.float32) / (32768.0 if a.dtype == np.int16 else 2 ** 31 if a.dtype == np.int32 else 1.0)
    if a.ndim == 1: a = np.stack([a, a], 1)
    if sr != SR:
        from scipy.signal import resample_poly
        g = math.gcd(sr, SR); a = resample_poly(a, SR // g, sr // g, axis=0).astype(np.float32)
    return a[:, :2]


def wr(p, a):
    from scipy.io import wavfile
    wavfile.write(p, SR, a.astype(np.float32))


def band(a, lo, hi):
    from scipy.signal import butter, sosfiltfilt
    return sosfiltfilt(butter(4, [lo, hi], "bandpass", fs=SR, output="sos"), a.mean(1))


def cmd_audio(edl):
    from scipy.signal import butter, sosfilt, resample
    e = load(edl); d = os.path.join(e["_dir"], "audio"); os.makedirs(d, exist_ok=True)
    spf = SR // e["fps"]
    s48 = os.path.join(d, "src48.wav")
    if not os.path.exists(s48):
        subprocess.run([FF, "-v", "error", "-y", "-i", e["src"], "-vn", "-ac", "2", "-ar", str(SR), "-c:a", "pcm_f32le", s48], check=True)
    src = rd(s48); N = e["_N"] * spf
    v = np.zeros((N, 2), np.float32); fade = int(0.004 * SR); ramp = np.linspace(0, 1, fade, dtype=np.float32)[:, None]
    for i, (of, f0, n) in enumerate(e["_seg"]):
        g = 10 ** (e.get("keep_gain_db", {}).get(str(i), 0) / 20)
        c = src[f0 * spf:(f0 + n) * spf].copy() * g
        c[:fade] *= ramp; c[-fade:] *= ramp[::-1]
        v[of * spf:of * spf + len(c)] = c
    v = sosfilt(butter(2, 75, "highpass", fs=SR, output="sos"), v, axis=0).astype(np.float32)
    # speech-active reference RMS (100 ms windows above -40 dBFS)
    w = int(0.1 * SR); r = np.sqrt(np.mean(v[:len(v) // w * w].reshape(-1, w, 2) ** 2, axis=(1, 2)))
    ref = float(np.sqrt(np.mean(r[r > 10 ** (-40 / 20)] ** 2)))
    sfx = np.zeros_like(v); log = []
    for c in e.get("sfx", []):
        a = rd(c["file"])
        if c.get("pitch"): a = resample(a, int(len(a) / 2 ** (c["pitch"] / 12)), axis=0).astype(np.float32)
        if c.get("ss"): a = a[int(c["ss"] * SR):]                     # 2026-11-25: slice start in the file (typing burst cut to the word)
        if c.get("dur"): a = a[:int(c["dur"] * SR)]; a[-int(0.03 * SR):] *= np.linspace(1, 0, int(0.03 * SR))[:, None]
        rr = np.sqrt(np.convolve(a.mean(1) ** 2, np.ones(w) / w, "same")); pk = int(np.argmax(rr)); lvl = float(rr.max()) + 1e-9
        a = a * (ref * 10 ** (c.get("db", -10) / 20) / lvl)
        if "pan" in c or "sweep" in c:                          # constant-power placement; sweep moves the sound across the stereo field
            p0, p1 = c.get("sweep", [c.get("pan", 0.0)] * 2); th = (np.linspace(p0, p1, len(a), dtype=np.float32) + 1) * (math.pi / 4)
            mono = a.mean(1); a = np.stack([mono * np.cos(th), mono * np.sin(th)], 1).astype(np.float32) * math.sqrt(2)
        st = int((c["t"] + c.get("lead", 0)) * SR) - (pk if c.get("align") == "peak" else 0)
        lo, hi = max(st, 0), min(st + len(a), N)
        if hi > lo: sfx[lo:hi] += a[lo - st:hi - st]
        log.append((c["t"], os.path.basename(c["file"]), c.get("db", -10)))
    wr(os.path.join(d, "voice.wav"), v); wr(os.path.join(d, "sfx.wav"), sfx)
    # collision check: SFX vs voice in 300-4000 Hz, 0.3 s after each cue
    vb, sb = band(v, 300, 4000), band(sfx, 300, 4000)
    print("cue  t     sfx-vs-voice(dB, 300-4k, 0.3 s)  file")
    for t, f, db in log:
        a0, a1 = int(t * SR), int((t + 0.3) * SR)
        ve = np.sqrt(np.mean(vb[a0:a1] ** 2)) + 1e-9; se = np.sqrt(np.mean(sb[a0:a1] ** 2)) + 1e-9
        flag = "  <-- masks voice?" if 20 * np.log10(se / ve) > -6 and ve > ref * 0.2 else ""
        print("%6.2f  %+6.1f  %s%s" % (t, 20 * np.log10(se / ve), f, flag))
    mixes = {"mix_main": v + sfx}
    m = e.get("music")
    if m:
        a = rd(m["file"])[int(m.get("src", 0) * SR):]
        a = np.resize(a, (N, 2)) if len(a) < N else a[:N]
        a = sosfilt(butter(2, 95, "highpass", fs=SR, output="sos"), a, axis=0).astype(np.float32)
        ma = np.sqrt(np.mean(a ** 2)) + 1e-9; a = a * (ref * 10 ** (m.get("db", -20) / 20) / ma)
        env = np.abs(v.mean(1)); att, rel = math.exp(-1 / (0.05 * SR)), math.exp(-1 / (0.4 * SR))
        # envelope follower on 10 ms blocks
        b = int(0.01 * SR); blk = np.sqrt(np.mean(env[:len(env) // b * b].reshape(-1, b) ** 2, 1)); on = (blk > ref * 0.25).astype(np.float32)
        g = np.zeros_like(on); cur = 0.0
        for i, o in enumerate(on):
            cur = o + (cur - o) * (math.exp(-1 / 5) if o > cur else math.exp(-1 / 40)); g[i] = cur
        gain = 10 ** (-m.get("duck", 7) * np.repeat(g, b) / 20); gain = np.pad(gain, (0, N - len(gain)), constant_values=gain[-1])
        a = a * gain[:, None]
        for g0, g1, *fi in m.get("gaps", []):                  # BGM removal (0-1 per video): out in 0.08 s at g0, back over fi s (default 0.65) from g1
            i0, i1 = int(g0 * SR), int(g1 * SR); fo_, fi_ = int(0.08 * SR), int((fi[0] if fi else 0.65) * SR)
            a[max(0, i0 - fo_):i0] *= np.linspace(1, 0, min(fo_, i0))[:, None]; a[i0:i1] = 0
            a[i1:i1 + fi_] *= np.linspace(0, 1, len(a[i1:i1 + fi_]))[:, None]
        fo = int(m.get("fade_out", 0.8) * SR); a[-fo:] *= np.linspace(1, 0, fo)[:, None]; a[:int(0.05 * SR)] *= np.linspace(0, 1, int(0.05 * SR))[:, None]
        wr(os.path.join(d, "music.wav"), a); mixes["mix_music"] = v + sfx + a
    for name, mx in mixes.items():
        raw = os.path.join(d, name + "_raw.wav"); wr(raw, mx); master(raw, os.path.join(d, name + ".wav"))


def master(raw, out, I=-14.0, TP=-1.5):
    import re
    s = subprocess.run([FF, "-hide_banner", "-i", raw, "-af", "loudnorm=I=%g:TP=%g:LRA=11:print_format=json" % (I, TP), "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    j = json.loads(s[s.rindex("{"):s.rindex("}") + 1])
    af = ("loudnorm=I=%g:TP=%g:LRA=11:measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:offset=%s:linear=true"
          % (I, TP, j["input_i"], j["input_tp"], j["input_lra"], j["input_thresh"], j["target_offset"]))
    subprocess.run([FF, "-v", "error", "-y", "-i", raw, "-af", af + ",aresample=48000", "-ar", "48000", "-c:a", "pcm_f32le", out], check=True)
    q = subprocess.run([FF, "-hide_banner", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    print(os.path.basename(out), " ".join(re.findall(r"I:\s+[-\d.]+ LUFS|Peak:\s+[-\d.]+ dBFS", q)[-2:]))


def cmd_mux(edl):
    e = load(edl); d = e["_dir"]; os.makedirs(os.path.join(d, "export"), exist_ok=True)
    v = os.path.join(d, "work", "video.mp4"); qc = []
    for mix, suf in (("mix_main", ""), ("mix_music", "_with_music")):
        a = os.path.join(d, "audio", mix + ".wav")
        if not os.path.exists(a): continue
        o = os.path.join(d, "export", e["name"] + suf + ".mp4")
        subprocess.run([FF, "-v", "error", "-y", "-i", v, "-i", a, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "320k",
                        "-ar", "48000", "-shortest", "-movflags", "+faststart", o], check=True)
        s = subprocess.run([FF, "-hide_banner", "-i", o, "-map", "0:v", "-vf", "blackdetect=d=0.01:pix_th=0.06,freezedetect=n=0.003:d=0.6",
                            "-af", "ebur128=peak=true", "-map", "0:a", "-f", "null", "-"], capture_output=True, text=True).stderr
        import re
        fr = re.findall(r"frame=\s*(\d+)", s)
        qc.append("== %s\n frames %s (target %d)\n %s\n %s" % (os.path.basename(o), fr[-1] if fr else "?", e["_N"],
                  "\n ".join(re.findall(r"black_start:\S+ black_end:\S+|freeze_start: \S+|freeze_end: \S+", s)) or "no black/freeze",
                  " ".join(re.findall(r"I:\s+[-\d.]+ LUFS|Peak:\s+[-\d.]+ dBFS", s)[-2:])))
    sheet = os.path.join(d, "export", "contact_0p5s.jpg")
    subprocess.run([FF, "-v", "error", "-y", "-i", v, "-vf", "fps=2,scale=180:-1,tile=10x%d" % math.ceil(e["_N"] / e["fps"] * 2 / 10),
                    "-frames:v", "1", sheet], check=True)
    open(os.path.join(d, "export", "qc.txt"), "w").write("\n".join(qc) + "\ncontact sheet: " + sheet + "\n")
    print("\n".join(qc))


if __name__ == "__main__":
    c, edl = sys.argv[1], sys.argv[2]
    if c == "video": cmd_video(edl)
    elif c == "stills": cmd_video(edl, stills=sys.argv[3])
    elif c == "audio": cmd_audio(edl)
    elif c == "mux": cmd_mux(edl)
