# video-editing-style — skill + analysis data

Source: one 29.9 s vertical reel (720x1280, 30 fps, 896 frames). The source video itself is not included.

## Install the skill
Copy `skill/video-editing-style/` to `<your-project>/.claude/skills/` (project) or `~/.claude/skills/` (global).
Then ask for an edit, plan or review "in the video-editing-style style".

## Contents
- `skill/video-editing-style/GUIDE.md` — the reusable skill (pacing, type, motion, transitions, grade, sound, workflow, QC).
- `analysis/contact_sheets/s_01-05.jpg` — whole reel, 3 fps, timestamped.
- `analysis/detail_frames/*.jpg` — frame-numbered sheets (30 fps) of key moments:
  a_intro (entrance + word reveal), b_cut1 (hard cut), c_group (re-stage), d_know (pivot line + light-leak flash),
  e_pie (pie scene + wedge), f_flash2 (second flash), g_money (money rain), h_trans3 (money wipe),
  i_traffic (red→green), j_statue, k_glitch (flash into CTA), l_zoom (zoom-through), m_end (endcard).
- `analysis/key_stills/A-C.jpg` — full-resolution stills of the main looks.
- `analysis/data/` — scene_changes, word-timed transcript, audio band/onset analysis, gap/cut audio, spectrogram, source specs.
- `analysis/scripts/` — the Python used for transcription (faster-whisper) and audio analysis (numpy/scipy).

## Caveats
Audio findings are measured (spectra, onsets, loudness), not heard. Font names are visual best matches.
Sizes in the skill are scaled from 720x1280 to 1080x1920.
