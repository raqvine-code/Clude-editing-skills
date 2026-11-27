---
name: sound-and-music-design
description: Use for any "improve the SFX / BGM / audio design" request, generic or repetitive-sounding edits, scoring a long-form video, building SFX from the scene engine's cue export, adding sound to a delivered mix, or checking a mix is dialogue-clear and phone-friendly. Audio-only redesign without touching picture, with numbers-based QA.
---

# Audio design (built on the Indian IT / Y2K / AI long-form, 2026-10-01)

Code: `edited videos by claude/4. Y2K to AI/code/audio2/`; intermediates `work/audio2/`; outputs `deliver/` (`AUDIO_DESIGN_v2.md`). Deepak's rules win: see `my-editing-rules` "Music & sound effects". [USED] = done on that video; (Claude) = my own rule, not yet approved.

## 1. Brief in practice
- Picture frozen: rebuild audio only, remux `-c:v copy`, check video-packet MD5 identical; keep the restored voice stem.
- Analyse first: transcript + scene index + engine cue export + contact sheets -> creative map (story, attention, emotional turns, reveals). Never add effects to look busy.
- Not generic: no CapCut/meme sounds, no excessive whooshes, no sample reused through the film; vary by action/emotion; every major SFX has a reason; subtle wins.
- Claude cannot listen: say so, verify with numbers, give Deepak a timestamped A/B pack (`deliver/ab_review/`, 12 moments v1 vs v2).

## 2. Measure the old mix first (Claude) [USED]
Per-second speech-band (200-5000 Hz) level of voice/music/SFX stems, LRA, share of cues from the same few samples. Y2K v1: music median -24 dB under voice, music+SFX only +0.1 dB over voice-only, 6 cue names = 52 % of cues, LRA 2.3.

## 3. Facts that shaped the design [USED]
- Deepak speaks continuously (89.6 % voiced, 4 pauses >= 0.5 s in 20 min): everything sits under speech; level relative to the voice, carve 1-3 kHz in sustained sounds, put weight where speech is not.
- Library BGMs are 30-90 % sub-bass: HPF music (scipy Butterworth 24 dB/oct @ 95 Hz); else bass eats the -14 LUFS budget and phones can't play it.
- Phone rule: hits made of 30-300 Hz vanish on a handset. Every hit gets a 250-1500 Hz knock + 2-5 kHz crack. Check phone loss = full-band RMS minus RMS above 300 Hz (sosfiltfilt): heroes 4 dB, impacts 7 dB, rest ~0; 300-1500 Hz within ~6 dB of 30-100 Hz.
- Clarity needs a number: extended STOI of (clean voice, full mix) per 12 s window (`pystoi`, `qa_stoi.py`, `stoi_lab*.py`). v1 0.943; v2 0.917 (p10 0.889, min 0.857); floor ~0.9. Each +3 dB music ~ -0.03 ESTOI; music alone caused the drop (SFX-only 0.976). A static pocket + level beat a masking-aware dynamic ducker (`dynduck.py`, only ~+2 dB music), so not used.
- Sync: audio early > 45 ms is noticed, late < 125 ms is not: transients at +20 ms; risers align by their peak, not onset.

## 4. Pipeline (run order) [USED]
1. `build/engine.js`: `c.sfx` records scene + call-site in EXPORT mode only; `node render.js --export work/audio2/cues_ctx.json` (7 s, no frames, same 430 cues/times as master).
2. `catalog_sfx.py` (decode every real SFX on the Mac) -> `real.py` (slice multi-sound files); `analyze_bgm.py` (tempo, beat grid, key, energy, sections); `analyze_voice.py`; `voiceref.py` (speech-band 100 ms voice level).
3. `plan.py`: score sections (anchors, D curves, `dD`, filter moves), tonal centre + tuning by time.
4. `kit.py` (procedural families) + `lib.py` (cache keyed with `KIT_VER`, pitch-shift, real slices) -> `events.py` (cue -> designed event; heroes/extras by hand; density governor) -> `build_events.py` (events.pkl + cue sheet) -> `sfx_render.py`.
5. `music.py` (anchors, calibration, bus, hand D curve, dip-filler, gap-healing, filter moves) -> `mix2.py --stems` (voice breath + hit dips + hero voice dips + sum + two-pass loudnorm -14 LUFS / -1.5 TP) -> `qa3.py`, `qa_stoi.py`, `qa_artifacts.py`, `key_check.py` -> `finalize.sh` (trim limiter's 5 ms delay, 150 ms end fade, AAC remux, FLAC stems, picture MD5) -> `ab_pack.py`, `make_docs.py`, `fig_before_after.py`.
Float32 intermediates only (PCM_24 clipped hot stems silently).

## 5. SFX palette [USED]
- Paper world: paper slide/flop, marker, stamp, wood/glass plucks in the music's key (lists climb, losses fall), bars landing with a tick, odometers = accelerating ticks + lock chime.
- Dark/AI: glass UI, orb swell + bloom, shimmer, short harmonic alerts, drone + heartbeat.
- Retro (Y2K): split-flap clacks, PC-speaker beeps, CRT power-on, DTMF/answer-tone/FSK chirp, typewriter strikes; no OS jingles.
- Hero moments: real riser (peak on the hit) + synthetic impact + pitched film impact + shimmer, each different (chapter hits climb F, G, Ab).
- Real before synthetic (v2: 102 real / 584 synthetic layers). Variation by round-robin pools, pitch, seed; consecutive events never share a lead sound.
- Tiers vs local voice (speech band, p75 100 ms window): hero -1, impact -4, chime -9.5, whoosh -11, pluck -11, foley -12.5, tick -15.5, micro -19.5, drone -19, bed -21; plus peak cap vs local voice peak (hero 0, impact -2, whoosh -5, chime -6.5, pluck/foley -8.5, tick -12.5, micro -15.5). g = min(RMS-based, peak-based). (Claude)
- ~22 events/min across all tiers (Deepak wants UI sound on every graphic element), ~12/min audible; collisions < 0.22 s keep the heavier; a cluster of the same cue = one gesture; no accent on paper -> paper cuts.
- Hero hits dip the voice 1.5 dB for 0.3 s instead of letting the limiter pump; SFX bus has its own look-ahead limiter (ceiling -1 dBFS).

## 6. Music scoring [USED]
- Few purposeful sections (12 for 20 min) in tempo/key families (123 BPM D/C minor -> 117.5 BPM C#/F minor -> 103 BPM -> 95.7/112 BPM -> Ab major -> Bb major): tension resolves to major.
- Pin a musical event to the picture (`anchor=(track_t, video_t)`, `hard=True`): read the 0.25-0.5 s energy curve and pick the real drop (K-S/flux guesses missed twice; Relentless Pursuit's drop is at 19.6 s, not 6 s). A track's own silence -> hit is the single removal.
- Level by speech-band D (voice minus music, 200-5000 Hz, p75) measured before the second pocket, then `dD` per section: hook ~12, drops ~12-14, explanation 22-25 after pockets. Bus: HPF 95, -2 dB shelf <170, -1.5 @260, -3 @1.9 kHz, -2 shelf >9.5 k; second pocket: -3.5 @300, -2 @700, -1.5 @2.6 k, -1.5 @5.5 k. Phrase "breath" -2.5 dB (120 ms/550 ms), pre-hit dips -3..-6 dB.
- Dip-filler (lift anything > 6 dB under section median, slow up/instant down) and gap-healing (repeat previous bar into dead-silent holes >= 0.35 s) because library tracks' breakdowns read as accidental removals; planned gaps opt out (`fill=False`).
- Filter moves instead of cuts: muffled agenda (LPF 1.7 kHz), pre-crash HPF thinning, darkened Tension 4 (LPF 650 Hz) under the drone so the bed never leaves.
- Pitched SFX: K-S key + pentatonic; drop degrees whose pitch class < 5 % of music chroma (`key_check.py`); apply each section's measured tuning (<= +-12 cents). Chroma-peak palettes failed (percussion pollutes chroma).

## 7. QA without ears (Claude)
Integrated/LRA/true peak of the delivered mp4; ESTOI per window (floor ~0.9); voice-minus-music by section; music gaps > 0.4 s (only the planned one); SFX per minute by tier; unique sounds and same-lead repeats; phone loss + impact weight; mono fold-down (< 1.5 dB; use mean((L+R)/2)); limiter gain reduction (> 1 dB in 0.2 % windows ok); HF-impulse and digital-silence scan; decoded-mp4 vs wav lag = 0; plots of key windows (`viz_mix.py`). A listening list remains Deepak's job.

## 8. Where real sounds are (Mac, 2026-10-01)
`~/Downloads/ui sfx/`, `~/Downloads/ES_*.mp3`, `~/Desktop/file manager/Sfx /` (Epidemic UI/typewriter/shutter/risers/glitch + 38 `Button (n).wav`), `~/Downloads/Bgms/` (library BGMs + Epidemic Relentless Pursuit, Bonafide, Higher = Action 1), `~/Downloads/claude/bgm for claude/`. `~/Desktop/claude all assets/` disappeared mid-session: copy scored tracks into `work/audio2/music_src/`. Film/song BGMs not for YouTube masters; meme sounds never.
**Checked 2026-11-25:**
- `~/Desktop/file manager/Sfx /` is empty now.
- The UI / typewriter / button sounds live in `~/Downloads/ui sfx/`: `Button (n).wav`, `KEYBOARD 1 (1).wav`, `SPIN CLICKS (1).mp3`, `DATA 2 (8).wav`, `Select.wav`, and Epidemic typewriter, shutter, UI click and glitch files.
- 125 Mixkit / Freesound candidates, measured and peak-normalised, sit in `edits/tes2/plan_work/sfx_candidates/wav48/` (categories: whoosh_soft, whip, riser, impact, pop, ui_click, shimmer, paper, shutter, heartbeat, crowd, applause, awkward; log `_download_log.tsv`, picks `audition_cues.txt`).
  - **Do not use `fs_181773_48k.wav`** (the paper page turn): it is silent (peak about -107 dBFS), and shortkit's level matching would boost its noise floor (found 2026-11-26). For paper, use `mixkit_2995_48k.wav` (paper slide).
- The text-move picks (5 Mixkit files) are copied into `text-animation-moves/assets/sfx/` with their licence.
- Measure before choosing: `text-animation-moves/tools/sfx_measure.py` gives length, peak time, active time, brightness and transients (Claude cannot listen).

Epidemic search phrases for still-synthetic sounds: `Paper, Handle, Paper Slide, Movement` | `User Interface, Motion, Short Swish, Swipe` | `Swooshes, Whoosh, Designed, Swoosh, Light` | `Objects, Writing, Text, Highlight Drag, Marker Highlighter` | `Objects, Office, Stamp, Press, Marking Document` | `Designed, Impact, Hit, Big, Dark, Cinematic` | `Designed, Granular, Complex, Warp, Morphs` | `Designed, Drone, Tension, Low` | `Heartbeat, Cinematic, 65 BPM` | `Alarms, Electronic, Emergency, Malfunction` | `Connecting to Internet Via Modem` | `Computers, Hard Drive, Vintage, Floppy` | `Designed, Riser, Reverse`.

## 9. Gotchas
- `pedalboard.Limiter` adds ~+7 dB make-up (SFX came out 4-7 dB hot): use `dsp.lookahead_limit`. `pedalboard.HighpassFilter` is 6 dB/oct.
- `tonic_low(lo, hi)` must not assume the interval holds the pitch class.
- Bump `KIT_VER` when a recipe changes or the cache serves the old sound.
- Cue time = animation start (hit at +20 ms); level by RMS window AND cap by peak.
- `alimiter` delays 240 samples; `pyloudnorm` on 20 min is very slow (use ffmpeg ebur128).
- First imports of matplotlib/pedalboard/numba take minutes; scratchpad venv is lost between sessions (`pip install numpy scipy soundfile librosa pyloudnorm matplotlib pedalboard pillow pystoi`).
- Another session may saturate CPU: iterate on windows, full render only at checkpoints, never run two chains writing the same stem.

## 10. Adding sound to a delivered mix without touching it (video 13 v2, 2026-10-13)
- Keep the old SFX stem bit-identical: re-render from the old cue export with same code and seed; diff cue sheets (194/194 identical).
- Render new cues to a second stem with the same tier system, sum both under the voice, re-master to -14 LUFS / -1.5 dBFS.
- Proof: in a window with no new cues, new master vs delivered AAC differed by -42 dB (codec noise only).
- New-layer palette from his library: short whoose_10 on every cut into B-roll; ui-pop on caption words/chips; Ui 5/6 + small sub knock on keycaps; glassy shimmer on line draws; phone tap on cursor clicks; Epidemic "Magic ... Synth Stings" on every AI click; impact 1 + sub on the AI slam; Shutter + tick bed + hit on the match cut; SciClose + low swell into the B&W pause, impact when colour returns.


Full original notes (every detail, uncut): `_archive/original-full/sound-and-music-design.md` in this folder.
