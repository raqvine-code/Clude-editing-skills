# Where real sound effects come from, and how to hear them (2026-11-27)

**Why this file exists.** The owner rejected the redo of the "story you tell yourself" short: "do not add proper SFX". Measured on that edit: 71 cues from 18 files, one pop used 16 times, 61 cues from files made by code, and nothing was ever heard by the editor (a cloud session has no ears). The owner then named three sources: Openverse, the Real SFX skill, and earshot. This file records what each one is, what works from a cloud container, and the rules that follow.

## 1. The three sources, checked
| Source | What it is | Licence | From a cloud container (2026-11-27) |
|---|---|---|---|
| **Openverse** (`api.openverse.org/v1/audio/`) | search over openly licensed audio from Freesound, Wikimedia Commons and others; every result carries its licence and creator | CC0, CC BY, CC BY-SA ... **per file: read `license`, `creator`, `foreign_landing_url`; keep CC0 / PDM first, CC BY needs the credit line in the delivery notes** | API answers, but the **anonymous quota is 1,000 requests per day per connection and was already used up** ("available in about 11.5 h"; the response headers `x-ratelimit-available-anon_sustained: 0`). A free registered key (name, description and an email at `/v1/auth_tokens/register/`, then a bearer token) lifts it; the email is the owner's, so ask first. Do not retry in a loop. The openverse.org website itself is blocked (403) |
| **Real SFX skill** (clipwing.pro/skills/real-sfx, `.skill` = zip) | a Claude Code skill that places library sounds on cues; **ships no recordings** except the `uisfx` npm package: 78 UI cues x 12 sound themes = 936 mp3 | the sounds are **CC0**; the scripts are the publisher's | the zip downloads. **Its own `manifest.json` says "Deterministic UI SFX synthesis recipes": the pack is synthesised, not recorded.** Good for ticks, toggles, list pops, success / error; it has no whooshes, hits or foley. We copied three themes (studio, minimal, organic) into `assets/uisfx-synth-cc0/` with their licence. The skill itself was not installed (a second auto-triggering skill would clash with this one) |
| **earshot** (`github.com/Leonxlnx/earshot`, MIT) | CLI + Python + MCP server; makes sounds **in code** (922 designs, some learned from public-domain recordings) and **listens**: CLAP + AudioSet models describe a sound, judge real vs synthesised (`realness`), score a soundtrack (`critique`), list events against the picture (`timeline`) | MIT; its sounds are rendered by code, so they count as **synthesised** | installs in a venv (CPU torch, ~1.1 GB of models, fetched in about 15 s, 50 GB disk was free). Code was read first: models pinned and loaded as safetensors, only ffmpeg subprocesses, no network except the one model download (the optional Gemini call stays off) |
| Mixkit | real recordings | Mixkit Sound Effects Free License | category pages now return a Cloudflare bot check from the container (not bypassed); only sounds whose preview URL (`assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3`) is already known can be fetched. 12 are in the earlier session's `edit/assets/sfx` |
| Wikimedia Commons API, Internet Archive | real, licence per file | per file | Commons answered 429 (shared rate limit); archive.org answers but most audio items carry no licence field: do not use without reading the item page |

## 2. Install earshot (cloud container, one time per session, about 5 min)
```bash
python3 -m venv earshot_env/venv
earshot_env/venv/bin/pip install torch --index-url https://download.pytorch.org/whl/cpu
git clone --depth 1 https://github.com/Leonxlnx/earshot earshot_env/src          # public repo; GIT_LFS_SKIP_SMUDGE=1 if it ever needs it
earshot_env/venv/bin/pip install "earshot_env/src[listen,measure]"
export EARSHOT_HOME=$PWD/earshot_env/home
earshot_env/venv/bin/earshot doctor --fetch                                      # downloads the two listening models
```
Read the code before running third-party tools; review it again when the version changes.

## 3. How to use the ears (the part a cloud session lacked)
| Job | Command |
|---|---|
| Is this sound a real recording or code? | `earshot realness <file or folder>`: tag every candidate; a folder of mine came back 8 "likely code-synthesized", 6 "uncertain" (the hand-made set) vs 8 + 10 "real or pro-produced" (the Mixkit set) |
| What does a candidate sound like / does it fit the word? | `earshot describe <file>`, `earshot match <file> "a soft paper whoosh"`, `earshot rank <folder> "a soft click"` |
| Find the best moment in a long recording | `earshot find <file> "a whoosh"` |
| Score the finished mix against the reference reels | `earshot critique --profile 03-sound-type-assets/sound-and-music-design/references/showcase-reels-sound-profile.json <video>` |
| Events against the picture | `earshot timeline <video>` (cuts and big changes with no sound near them are listed) |
| Build a new profile from references | `earshot profile -o <profile.json> <folder of reference reels>` |
The bundled `critique` profile is for SaaS launch films; for shorts always pass `--profile` with the showcase profile above.

## 4. What the four showcase reels sound like (earshot profile of R5-R8, medians; p10-p90 in brackets)
| Metric | Reels | The rejected redo |
|---|---|---|
| Integrated loudness / true peak | -14.2 LUFS / -0.7 dBTP | -14.0 / -1.5 (ok) |
| Music present (5 s windows) | 93 % (68-100) | 0 % |
| Longest silent gap inside the film | 0.00 s (always something under the voice) | 0.42 s |
| Onsets per second | 5.8 (5.1-7.1) | 4.7 |
| Salient hits per second | 1.9 (1.7-2.1) | 1.8 (ok) |
| Sound within 100 ms of a visual event | 94 % (85-100) | 78 % (5 of 49 events had no sound: 6.27, 14.23, 15.03, 26.20, 41.53 s) |
| Stereo width (side vs mid) | -18.9 dB (-24 to -16.5) | -27.6 dB (near mono) |
| Low 60-250 Hz share | -4.2 dB | -8.8 dB |
| Sub 20-60 Hz share | -12.2 dB | -27.7 dB |
| Presence 4-8 kHz share | -16.2 dB | -25.1 dB (dull) |
| Loudness range | 3.0 LU | 2.2 LU |
Reading it: the references are never silent, carry about 6 sound onsets a second (a bed plus ticks plus hits), are clearly stereo and have real low end. **All four have music**; the client rule "no BGM" for this video removes that bed, so replace its job: a quiet room-tone / texture bed so no gap is silent, stereo-panned effects, a sub layer under hits, bright (4-8 kHz) transients.

## 5. Rules that follow (also enforced by the gate)
1. **Real recordings first.** Synthesised cues (code-made, `uisfx`, earshot's own) are at most 20 % of the cues and only for UI ticks. The gate counts any file whose path contains `synth`.
2. **No file more than 3 times in a 47 s video; distinct files at least 60 % of cues.** Choose by what moves, then by `earshot match`.
3. **Check the licence of every file and write it in the delivery notes**; keep the source URL and the creator for CC BY.
4. **Listen before delivery:** run `earshot critique` with the showcase profile and `earshot timeline`; fix every event with no sound near it and every silent gap over 0.25 s (use a bed, not a louder cue).
5. **Pan with the motion** (`pan` / `sweep` in the EDL `sfx` entries); a near-mono mix is a defect.
6. State in the delivery message that the mix was checked by measurement and by earshot's ears, not by a person listening.
