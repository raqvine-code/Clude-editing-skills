---
name: sound-and-music-design
description: Deepak's sound-design method for a finished edit — audio-only redesign of SFX, BGM scoring and the mix without touching the picture (designed SFX palette per visual world, music scored to picture with tempo/key/downbeat anchors, voice-relative levelling, phone-first loudness, intelligibility-checked music level, numbers-based QA). Use for any "improve the SFX / BGM / audio design" request, "my sounds feel generic or repetitive", scoring a long-form video, building SFX from the scene engine's cue export, or checking whether a mix is dialogue-clear and phone-friendly.
---

# Audio design (first built on the Indian IT / Y2K / AI long-form, 2026-10-01)

Code: `edited videos by claude/4. Y2K to AI/code/audio2/` · intermediates `work/audio2/` · outputs `deliver/` (`AUDIO_DESIGN_v2.md` = the full write-up). Deepak's rules (his word wins): `my-editing-rules` → "Music & sound effects" (brief of 2026-10-01). Tags: **[USED]** done on this video · *(Claude, not yet approved by Deepak)* = my own rule. Phone-speaker finding is shared with `video-intro-design` §7.

## 1. What the brief means in practice
- **Picture is frozen.** Rebuild audio only; remux with `-c:v copy` and check the video-packet MD5 is identical. Keep the restored voice stem.
- **Analyse first:** transcript + scene index + the engine's exact cue export + contact sheets → a creative map (story, attention, emotional turns, reveals). Never "add effects to look busy".
- **Not generic:** no CapCut/meme sounds, no excessive whooshes, no sample reused through the film. Vary by action and emotion; every major SFX has a reason; subtle wins.
- Claude cannot listen: say so, verify with numbers, hand Deepak a timestamped A/B pack (`deliver/ab_review/`, 12 moments v1 vs v2).

## 2. Measure the old mix first *(Claude)* [USED]
Per-second speech-band (200–5000 Hz) level of voice/music/SFX stems, LRA, share of cues from the same few samples. Y2K v1: music median −24 dB under the voice, music+SFX +0.1 dB over voice-only, 6 cue names = 52 % of cues, LRA 2.3. "Generic" was measurable.

## 3. Facts that shaped the design [USED]
- **Deepak speaks continuously** (89.6 % voiced, only 4 pauses ≥ 0.5 s in 20 min). No gaps to hide sounds in → everything sits *under speech*: level relative to the voice, carve 1–3 kHz in sustained sounds, put weight where speech is not.
- **Library BGMs are 30–90 % sub-bass.** HPF the music (scipy Butterworth 24 dB/oct @ 95 Hz); the bass otherwise eats the −14 LUFS budget and phones cannot play it.
- **Phone rule:** a hit made of 30–300 Hz "vanishes" on a handset. Every hit gets a 250–1500 Hz knock + 2–5 kHz crack. Check *phone loss* = full-band RMS − RMS above 300 Hz (sosfiltfilt): v2 heroes 4 dB, impacts 7 dB, all else ≈ 0; and 300–1500 Hz within ~6 dB of 30–100 Hz.
- **Clarity needs a number.** Extended STOI of (clean voice, full mix) per 12 s window (`pystoi`, `qa_stoi.py`, tuning lab `stoi_lab*.py`). v1 0.943; v2 0.917 (p10 0.889, min 0.857). Rule of thumb measured here: **each +3 dB of music ≈ −0.03 ESTOI**; music alone caused the drop (SFX-only 0.976). A static pocket + level beat a masking-aware dynamic ducker (`dynduck.py`, only ≈ +2 dB more music at equal ESTOI), so the dynamic one was not used.
- Sync: audio early > 45 ms is noticed, late < 125 ms is not → transients at +20 ms, risers align by their **peak**, never their onset.

## 4. Pipeline (run order) [USED]
1. `build/engine.js`: `c.sfx` records `scene` + call-site in EXPORT mode only → `node render.js --export work/audio2/cues_ctx.json` (7 s, no frames; same 430 cues/times as the master).
2. `catalog_sfx.py` (decode every real SFX on the Mac) → `real.py` (slice multi-sound files) · `analyze_bgm.py` (tempo, beat grid, key, energy, sections) · `analyze_voice.py` · `voiceref.py` (speech-band 100 ms voice level).
3. `plan.py`: score sections (anchors, D curves, `dD`, filter moves), tonal centre + tuning by time.
4. `kit.py` (procedural families) + `lib.py` (cache keyed with `KIT_VER`, pitch-shift, real slices) → `events.py` (maps each cue to a designed event; heroes/extras by hand; density governor) → `build_events.py` (events.pkl + cue sheet) → `sfx_render.py`.
5. `music.py` (anchors, calibration, bus, hand D curve, dip-filler, gap-healing, filter moves) → `mix2.py --stems` (voice breath + hit dips + hero voice dips + sum + two-pass loudnorm −14 LUFS / −1.5 TP) → `qa3.py` `qa_stoi.py` `qa_artifacts.py` `key_check.py` → `finalize.sh` (trims the limiter's 5 ms delay, 150 ms end fade, AAC remux, FLAC stems, MD5 of the picture) → `ab_pack.py`, `make_docs.py`, `fig_before_after.py`.
Float32 intermediates only (PCM_24 clipped hot stems silently).

## 5. SFX palette [USED]
- **Paper world:** paper slide/flop, marker, stamp, wood/glass plucks in the music's key (lists climb, losses fall), bars that land with a tick, odometers = accelerating ticks + lock chime. **Dark/AI:** glass UI, orb swell + bloom, shimmer, short harmonic alerts, drone + heartbeat. **Retro (Y2K):** split-flap clacks, PC-speaker beeps, CRT power-on, DTMF/answer-tone/FSK chirp, typewriter strikes; no OS jingles. **Hero moments:** real riser (peak on the hit) + synthetic impact + pitched film impact + shimmer; each different (chapter hits climb F → G → A♭).
- Real before synthetic (v2: 102 real / 584 synthetic layers). Variation by round-robin pools, pitch, seed; consecutive events never share a lead sound.
- **Tiers vs the local voice** (speech band, p75 100 ms window): hero −1 · impact −4 · chime −9.5 · whoosh −11 · pluck −11 · foley −12.5 · tick −15.5 · micro −19.5 · drone −19 · bed −21, **and a peak cap vs the local voice peak** (hero 0, impact −2, whoosh −5, chime −6.5, pluck/foley −8.5, tick −12.5, micro −15.5). `g = min(RMS-based, peak-based)`. *(Claude)*
- ~22 events/min all tiers (Deepak wants UI sound on every graphic element), ≈ 12/min audible; < 0.22 s collisions keep the heavier one; a cluster of the same cue = one gesture; no accent on paper → paper cuts.
- **Hero hits dip the voice 1.5 dB for 0.3 s** instead of letting the limiter pump it; SFX bus has its own look-ahead limiter (ceiling −1 dBFS).

## 6. Music scoring [USED]
- **Few, purposeful sections** (12 for 20 min) in tempo/key families (123 BPM D/C minor → 117.5 BPM C♯/F minor → 103 BPM → 95.7/112 BPM → A♭ major → B♭ major): tension resolves to major.
- **Pin a musical event to the picture** (`anchor=(track_t, video_t)`, `hard=True`): read the 0.25–0.5 s energy curve around the guess and pick the real drop (K-S/flux guesses missed twice: Relentless Pursuit's drop is at 19.6 s, not 6 s). Use a track's own silence → hit as the single removal (Action 3 at the crash).
- **Level by speech-band D** (voice − music, 200–5000 Hz, p75) *measured before the second pocket*, then `dD` per section from the ESTOI lab: hook ~12, drops ~12–14, explanation 22–25 after pockets. Bus: HPF 95, −2 dB shelf <170, −1.5 @260, −3 @1.9 kHz, −2 shelf >9.5 k; second pocket after calibration: −3.5 @300, −2 @700, −1.5 @2.6 k, −1.5 @5.5 k. Phrase "breath" −2.5 dB (120 ms / 550 ms), pre-hit dips −3…−6 dB.
- **Dip-filler** (lift anything > 6 dB under the section median, slow up / instant down) and **gap-healing** (repeat the previous bar into dead-silent holes ≥ 0.35 s): library tracks have built-in breakdowns that read as accidental removals. Planned gaps opt out (`fill=False`).
- **Filter moves instead of cuts:** muffled agenda (LPF 1.7 kHz), pre-crash HPF thinning, darkened Tension 4 (LPF 650 Hz) under the drone so the bed never leaves.
- **Pitched SFX palette:** K-S key + pentatonic; drop pentatonic degrees whose pitch class is < 5 % of the music's chroma (`key_check.py`); apply each section's measured tuning (≤ ±12 cents). Chroma-peak "palettes" failed (percussion pollutes chroma → semitone clusters).

## 7. QA that can be done without ears *(Claude)*
Integrated / LRA / true peak of the **delivered mp4**; ESTOI per window (floor ≈ 0.9); voice-minus-music by section; music gaps > 0.4 s (only the planned one); SFX per minute by tier; unique sounds and same-lead repeats; phone loss + impact weight; mono fold-down (< 1.5 dB; use mean((L+R)/2), not the √2 formula); limiter gain reduction (> 1 dB in 0.2 % of windows is fine); HF-impulse and digital-silence scan; decoded-mp4 vs wav lag = 0; plots of key windows (`viz_mix.py`). A listening list is still Deepak's job.

## 8. Where the real sounds are (Mac, 2026-10-01)
`~/Downloads/ui sfx/`, `~/Downloads/ES_*.mp3`, `~/Desktop/file manager/Sfx /` (Epidemic UI/typewriter/shutter/risers/glitch + 38 `Button (n).wav`), `~/Downloads/Bgms/` (library BGMs + Epidemic *Relentless Pursuit*, *Bonafide*, *Higher* = Action 1), `~/Downloads/claude/bgm for claude/`. `~/Desktop/claude all assets/` disappeared mid-session: copy the tracks you score with into `work/audio2/music_src/`. Film/song BGMs are not for a YouTube master; meme sounds never.
**Epidemic search phrases for what is still synthetic:** `Paper, Handle, Paper Slide, Movement` · `User Interface, Motion, Short Swish, Swipe` · `Swooshes, Whoosh, Designed, Swoosh, Light` · `Objects, Writing, Text, Highlight Drag, Marker Highlighter` · `Objects, Office, Stamp, Press, Marking Document` · `Designed, Impact, Hit, Big, Dark, Cinematic` · `Designed, Granular, Complex, Warp, Morphs` · `Designed, Drone, Tension, Low` · `Heartbeat, Cinematic, 65 BPM` · `Alarms, Electronic, Emergency, Malfunction` · `Connecting to Internet Via Modem` · `Computers, Hard Drive, Vintage, Floppy` · `Designed, Riser, Reverse`.

## 9. Gotchas (all hit on this video)
**`pedalboard.Limiter` adds ~+7 dB make-up** (every SFX was 4–7 dB hotter than designed): use `dsp.lookahead_limit` · `pedalboard.HighpassFilter` is 6 dB/oct · `tonic_low(lo, hi)` must not assume the interval holds the pitch class · bump `KIT_VER` when a recipe changes or the disk cache serves the old sound · cue time = animation start (hit at +20 ms) · level by RMS window *and* cap by peak · `alimiter` delays 240 samples · `pyloudnorm` on 20 min is very slow (use ffmpeg ebur128) · first imports of matplotlib/pedalboard/numba take minutes and the scratchpad venv is lost between sessions (`pip install numpy scipy soundfile librosa pyloudnorm matplotlib pedalboard pillow pystoi`) · another session may saturate the CPU: iterate on windows, full render only at checkpoints, and do not start two chains that write the same stem.

## 10. Adding sound to a delivered mix without touching it *(video 13 v2, 2026-10-13)*
- Keep the old SFX stem bit-identical: re-render it from the old cue export with the same code and seed, and diff the cue sheets (194 / 194 rows identical).
- Render the new cues to a **second stem** with the same tier system (levelled against the local voice), sum both under the voice, and re-master to −14 LUFS / −1.5 dBFS.
- **Proof:** in a window with no new cues, the new master and the delivered AAC differed by −42 dB (codec noise only).
- New-layer palette, all from his library:
  - Short whoose_10 on every cut into B-roll;
  - ui-pop sounds on caption words and chips;
  - Ui 5/6 + a small sub knock on keycaps;
  - a glassy shimmer on line draws;
  - phone tap on cursor clicks;
  - the Epidemic "Magic … Synth Stings" on every AI click;
  - impact 1 + sub on the AI slam;
  - Shutter + tick bed + hit on the match cut;
  - SciClose + low swell into the B&W pause, impact when the colour returns.
