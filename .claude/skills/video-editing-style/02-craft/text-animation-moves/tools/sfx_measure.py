"""sfx_measure: numbers for choosing a sound when Claude cannot listen (text-animation-moves, 2026-11-25).
Usage: python3 -I sfx_measure.py <file> [<file> ...]      (wav, mp3, anything ffmpeg reads)
Prints per file: length, time of the loudest 20 ms (use it with shortkit "align": "peak"), onset, active time
(within 20 dB of the peak: how long it is really heard), peak RMS in dBFS, share of energy above 4 kHz (bright = ticks,
shimmers; dark = thumps, pops) and the number of transients (many = typing / clicks / gears).
Pick by the move: a type word wants many transients and an active time >= the word's type duration; a pop wants one transient
and a peak in the first 40 ms; a rise wants a soft whoosh with its peak 0.3-0.5 s in (align peak to the fastest frame).
"""
import sys, subprocess, numpy as np
FF = "/Library/Frameworks/Python.framework/Versions/3.15/lib/python3.15/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-x86_64-v9.0.2"
for p in sys.argv[1:]:
    raw = subprocess.run([FF, "-v", "error", "-i", p, "-ac", "1", "-ar", "48000", "-f", "f32le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32)
    if a.size == 0: print("EMPTY", p); continue
    w = 960; n = a.size // w; e = (a[:n * w].reshape(n, w) ** 2).mean(1)
    pk = e.argmax(); db = 10 * np.log10(e + 1e-12); top = db.max()
    on = np.argmax(db > top - 30) * w / 48000; act = (db > top - 20).sum() * w / 48000
    # brightness: share of energy above 4 kHz
    sp = np.abs(np.fft.rfft(a[:min(a.size, 48000 * 2)])) ** 2; fr = np.fft.rfftfreq(min(a.size, 48000 * 2), 1 / 48000)
    hi = sp[fr > 4000].sum() / sp.sum()
    # transient count (onsets): rises of > 9 dB between 20 ms windows
    ons = int(((db[1:] - db[:-1]) > 9).sum())
    print("%-70s len %5.2fs  peak@%5.3fs  onset %4.2fs  active %4.2fs  peakRMS %6.1f dBFS  hi>4k %3.0f%%  onsets %d" % (
        p.split("/")[-1][:70], a.size / 48000, pk * w / 48000, on, act, top, hi * 100, ons))
