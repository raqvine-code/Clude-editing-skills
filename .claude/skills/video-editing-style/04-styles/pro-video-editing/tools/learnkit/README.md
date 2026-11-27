# learnkit: study one reference video for the fewest tokens

Built 2026-11-20 while learning the second Tharun Speaks long-form video. One command does all the measuring locally (free); Claude then reads a few small text files and 6-15 images instead of dozens of 2-fps contact sheets.

```bash
bash learn_video.sh "<video>" "<study_dir>"      # WHISPER_MODEL=small (default), WHISPER_LANG=en optional
```

## What it produces (in <study_dir>)
| File | What | Read it? |
|---|---|---|
| `shots_stats.txt` | cuts/min, shot-length stats, cuts per minute | yes (tiny) |
| `shots/shots_NN.jpg` | ONE mid-frame per shot, labelled `#shot time length` (42 shots per sheet landscape, 30 portrait) | yes, all of them: this is the whole video |
| `face_stats.txt` | framing sizes, punch-in ratio, push-in, A-roll share | yes |
| `audio_stats.txt` | voice vs stereo layer (music/SFX) level per 10 s, dropouts, bursts vs cuts | yes |
| `text_stats.txt`, `captions_compact.txt`, `headlines.txt` | all on-screen text (OCR at 5 fps): density, sizes, positions, every caption | yes |
| `sync_stats.txt`, `transcript.txt` | speech rate, pauses, caption lag and coverage, SFX vs graphics; transcript in 12 s lines | yes |
| `text_timeline.txt`, `text_events.json`, `shots/shots.json`, `faces.txt` | raw data | only if a number looks odd |

## Then look closer only where it matters
```bash
cd <study_dir> && python3 <learnkit>/strip.py name:start_s:dur_s:fps ...   # 24-frame strips into strips/name.jpg
```
Use 8-12.5 fps over 2-3 s for an entrance animation, 3-5 fps over 5-8 s for a whole graphic scene. 6-10 strips are usually enough.
For fonts and texture, grab 6-12 full-quality stills from the ORIGINAL file and tile them into 1-2 images.

## Token budget (V2 Tharun, 11:47): 6 shot sheets + 9 strips + 2 still sheets ≈ 35k tokens of images, about 12k of text.

## Notes
- Run `refscan.py` on the library ROOT (`/Users/raghusai/Desktop/training claude`), not on the new video's subfolder, so the video is registered in `knowledge/manifest.json` without dropping the others. Run it in the background: a new long video takes several minutes.
- Before starting, check `ps` for another `learn_video.sh` on the same file; two runs at once make the OCR and transcript take 40+ minutes. View `shots/` and cut strips as soon as they exist instead of waiting for the script to end.
- Side-channel audio only sees stereo content; if the source is mono the script says so.
- OCR cannot read text hidden behind the speaker; take giant headlines from the shot sheets.
- Needs: `imageio_ffmpeg`, numpy, scipy, Pillow, the whisper venv, and `swiftc` (first run compiles `ocr` and `face`).
- After studying: write findings into the matching skill (Measured / Observed / Suggested labels), append its LEARNING-REPORT or LEARNING-LOG, rebuild `INDEX.md`.

## Shorts (under ~60 s)
A short packs several graphics into one shot, so one frame per shot is not enough. After `learn_video.sh`, view the whole video as time strips instead:
```bash
cd <study_dir> && python3 <learnkit>/strip.py all:0:<duration>:2        # calm reel: 2 fps; fast reel: 3 fps in two halves
python3 <learnkit>/stills.py "<original video>" stills.jpg 6 256 t1 t2 ...   # 10-12 full-quality stills on one sheet
```
Then 2-3 strips at 15 fps on the hook and the best transitions. Two shorts studied this way cost about 20k tokens of images in total.
