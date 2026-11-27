# External tools the owner listed (2026-11-27): checked, with a verdict

The owner forwarded "10 free GitHub repos (+1 bonus) to turn Claude into a video editor". Each public repository was cloned shallow and READ (licence, structure, skills, install steps, requirements). Nothing was executed. **None is installed as a skill**, for the reasons in the last column: every installed skill puts its description into every future session, and the four big repos alone would add 29 + 14 + 13 + 19 skill descriptions that overlap with this skill. Sounds and ideas that were worth taking were taken (see "Taken").

| # | Tool | Licence | What it is (verified) | Verdict | Taken |
|---|---|---|---|---|---|
| 1 | **Motion Skills** `iart-ai/motion-skills` | MIT | an index of 19 separate packs (56 skills), each installed with `npx skills add iart-ai/<pack>`: tiktok-video, kinetic-typography, b-roll, lower-thirds, explainer, data-animation and more | not installed: each pack is its own repo and adds skills; on request install `kinetic-typography-skills` first, then `b-roll-skills` | the pack list |
| 2 | **yt-dlp** `yt-dlp/yt-dlp` | Unlicense | downloads videos from YouTube and many sites | not cloned (well known). Downloading other creators' videos is for study only (`CLAUDE.md` Rule 1.4); the owner uploads references, so not needed | - |
| 3 | **Whisper** `openai/whisper` | MIT | speech to text | already covered: this skill uses `faster-whisper` (same models); auto-editor also has a `whisper` subcommand | - |
| 4 | **FFmpeg Skill** `kajisho5/ffmpeg-skill` | MIT | 42 ffmpeg tools for agents (cut, caption, reframe, loudness, per-platform export); install `npx ffmpeg-skill`. The repo is 119 MB (demos) and also carries the author's own development skills in `.claude/skills/`, which must NOT be installed | optional; ffmpeg and our scripts already do these jobs. The product skill is `skills/ffmpeg-skill/` | - |
| 5 | **Ghost Editor** `kurbaitaev/ghost-editor` | MIT | one skill; edits talking-head reels in 19 styles through 18 layout recipes; built for **Apple-silicon Macs** (macOS OCR check, Homebrew), untested on Linux | not installed (Mac pipeline). Studied: **recipes, the house-look / components rule, the two-worlds idea** | `04-styles/editor-showcase-caption-edit-style/references/ghost-editor-recipes.md`; `GUIDE.md` 10b rules 8-10; 8 CC0 sounds (`assets/ghost-cc0/`); 51 Mixkit sound ids and 23 music ids (`assets/mixkit-restore-list.json`, fetched by `06-tools/tools/mixkit_fetch.py`, tested on 23 files) |
| 6 | **Claude Shorts** `AgriciDaniel/claude-shorts` | MIT | long video to 9:16 shorts: scores moments, 3 caption styles (Bold, Bounce, Clean), Remotion render, last commit 2026-04-10 | not installed; overlaps this skill and is older | - |
| 7 | **HyperFrames** `heygen-com/hyperframes` | Apache-2.0 | write HTML, render MP4 (headless Chrome + ffmpeg); 29 skills; about 450 ready-made blocks (transitions, overlays, text) in `registry/`; needs **Node 22+ and FFmpeg: both are present in the cloud container** | **the most promising upgrade for varied motion graphics** (CSS fonts, easing, SVG instead of our PIL cards). Not installed and not tested yet; a pilot (one card rendered with transparency, then placed with `layers`) needs the owner's yes | - |
| 8 | **Three.js Skills** `CloudAI-X/threejs-skills` | MIT | 13 skills on three.js (materials, loaders, lighting, post-processing) | not needed for talking-head shorts | - |
| 9 | **Remotion Agent Skills** `remotion-dev/skills` | no licence file in the skills repo; **Remotion itself needs a paid company licence above a small team size: confirm at remotion.pro before use** | 14 skills for writing Remotion (React) video code | not installed; same job as HyperFrames with a licence question | - |
| 10 | **Auto-Editor** `WyattBlue/auto-editor` | Unlicense (public domain) | cuts silence and dead air, exports to Premiere / Resolve / Final Cut; 5 skills; also transcribes and adds transitions | optional; a talking head with few pauses needs little of it. Useful when the owner sends long raw takes | - |
| + | **MotionClone** `motionclone.lol` | n/a | Windows app that rebuilds a reference video as an editable HyperFrames project; its AI step uses the user's own ChatGPT login | not used: Windows app, personal login, and it re-creates other creators' videos (Rule 1.4) | - |

## How to try one on demand (read-only first)
```bash
git clone --depth 1 https://github.com/<owner>/<repo> <scratch>/<repo>     # then read README.md, SKILL.md and the licence
```
Install a skill into `.claude/skills/` only after the owner says yes, and only the product skill, not the whole repo. Check its description length (the skill-creator validator allows 1,024 characters). `build_index.py` covers only this rulebook, not outside skills.

## Next best step if the owner agrees
A HyperFrames pilot: scaffold a project, build ONE card (hero word + lead-in on a transparent background), render it with alpha, place it through shortkit `layers`, compare with `caption_moves.py` output. If it renders here, motion cards can be designed in HTML/CSS with the owner's fonts and far more varied animation than the PIL cards.
