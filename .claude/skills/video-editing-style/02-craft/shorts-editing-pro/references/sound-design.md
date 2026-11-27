# Sound design (shorts)

## Voice chain (first, always)
1. HPF 80 Hz.
2. De-noise light (only if the room hum is audible).
3. De-ess at 6-8 kHz, -3 to -5 dB.
4. Compressor 3:1, attack 5 ms, release 80 ms.
5. Presence shelf +2 dB above 3 kHz, and -2 dB at 250-350 Hz if boomy.
6. Voice stem at about -16 LUFS.

Level-match splices, then use 8-10 ms crossfades at every cut.

## SFX map (main master = voice + SFX)
| Event | Sound | Level re voice | Timing |
|---|---|---|---|
| Hook slam / giant word | sub boom + mid knock + HF click | -3 to -5 dB | on the frame (may lead 1 f) |
| Cut into B-roll | short whoosh | -10 to -12 | starts about 90 ms before the cut |
| Whip in montage | whip, varied pitch | -10 | on the whip |
| Zoom punch | short punch whoosh or tick | -12 | on the zoom start |
| Hero caption / stack | soft pop or tick | -14 to -18 | on the word frame |
| Flash | shutter or camera click + low thud | -8 | on the flash |
| Payoff build | riser 1.2-1.8 s, peak on the hit | -8 → -4 | peak aligned to the hit |
| Action B-roll | foley (splash, crowd, wind) | -10 to -14 | on the picture event |
| Freeze | tape-stop or shutter + thud | -8 | on the freeze frame |

**Density and spacing**
- About 1 audible SFX per 0.6-1.5 s in a 15-30 s short. Ordinary captions stay silent.
- Never put two whooshes within 0.25 s, or the same sample twice in a row (pitch ±1-3 semitones or round-robin).

**Phone rule**
- Every hit needs 250-1500 Hz body and a 2-5 kHz crack; sub-only vanishes on phones.

**Collision check**
- Measure 300-4000 Hz energy 0.3 s after each cue. If a cue masks a word, move it to the picture event just before, or duck it 3-6 dB.

**Sources**
- Mixkit, Freesound or Pixabay (free).
- Local: `edits/1115a/assets/sfx_ext`, the tes2 library, `~/Downloads/ui sfx/`, `~/Desktop/file manager/Sfx /`.
- Never meme sounds. Never film or song BGM on a YouTube master.

## Music (alt master only, unless Deepak asks)
- Library or Mixkit track with no vocals, 100-125 BPM, constant energy.
- HPF the music at 95 Hz.
- Level 18-22 dB under speech. Duck 6-10 dB under words (attack 30-80 ms, release 250-700 ms). Never syllable pumping.
- At most one removal: a riser → cut → fade-back, ≤ 8 s, on the key line. Fade the last 0.6 s.

## Master
- Sum voice + SFX (+ music).
- Look-ahead limiter, then loudnorm: two-pass -14 LUFS I, -1.5 to -1 dBTP, LRA about 2-6.
- Check with ffmpeg `ebur128=peak=true`.
