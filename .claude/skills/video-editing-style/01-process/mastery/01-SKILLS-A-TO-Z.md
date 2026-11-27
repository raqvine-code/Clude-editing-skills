# Video Editing Skills: A to Z

What Claude has learned about video editing in this account, and where each piece lives on this Mac.
This overview is from 2026-11-15 and covers the first 23 skills; there are now 36 (see `INDEX.md`).

**Honest note:** Claude does not "train" in the machine-learning sense. Each skill below is a written, reusable knowledge file built from studying your references, your feedback on delivered videos, and research. Claude reads the relevant skill at the start of each edit. Knowledge is only as good as what was studied; gaps are listed at the end.

Evidence labels used inside the skills: **Measured/V** (read from frames, audio or transcripts), **Approx/S** (seen on contact sheets or fitted by eye), **Published/ONL** (public breakdowns or web research), **Suggested/E** (standard practice or Claude's reconstruction), **SC** (screenshot only).

---

## A. Always read first (every edit)
| Skill | What it teaches | Form |
|---|---|---|
| `my-editing-rules` | Master playbook for Tech Boy Deepak: channel context, automatic save routine, standard workflow, "keep his cut", briefs per video type, Shorts rules (5 best moments as 40-60 s 9:16 shorts, rough cuts first, colour + captions first), hooks, pacing (one meaningful visual change ~every 5 s), B-roll/PNG/captions/CTA, music & SFX, transitions, dislikes | Short + Long |
| `mistakes-to-avoid` | Rejected moves with fixes: coloured backgrounds behind his cut-out, clutter, decorative labels, mock-ups, oversized hero words, sentence captions, Telugu sync, text-only edits, designed stand-ins posing as evidence | Short + Long |
| `fonts-and-colours` | Approved fonts + free stand-ins, one font per role, change every video, fonts/palettes already used or disliked, palettes measured from references | Short + Long |

## B. Assets and sourcing
| Skill | What it teaches |
|---|---|
| `broll-library` | Index + selection rules for 272 B-roll clips in `brolls for claude/` (coding, AI, college, money, jobs, emotions, flags, CTAs, transitions) |
| `png-library` | Index + prep rules for 78 pop-up images in `png for claude/` |
| `where-to-find-assets` | Fixed site list + decision tree (Behance -> LottieFiles/Mobbin -> Pexels/Mixkit -> Mixkit/Freesound -> Freepik/Figma); Pexels workflow; real photos/documents for news (Wikimedia, public-domain government media). SFX/BGM from Mixkit / Freesound / Pixabay (your decision 2026-11-14) |

## C. Short-form (9:16) editing
| Skill | What it teaches | Evidence |
|---|---|---|
| `reel-editing-method` | Full method from Deepak's first motion-graphics reel (68 s): structure, timeline rules (elements enter 0.05-0.1 s before the word, cut music once on the key line, no speed ramps on talking heads), type, motion graphics, effects, B-roll, music, SFX, colour, transitions, IF->THEN decision rules, hold times (captions 0.6-1.5 s, keyword slams 0.4-0.6 s, cards 2-10 s) | Delivered video |
| `tharun-speaks-edit-style` | Tharun Speaks vertical reel style, measured frame by frame from 2 reels: word-pop captions, behind-subject headlines, punch-in cuts, lime labels, flash transitions; AE recipes, style tokens, fonts, caption-beat script | Measured |
| `pro-video-editing` | 5 premium short-form profiles from your "training claude" library (12 videos, 53 screenshots): P1 Glass Spotlight motion ad, P2 Editorial Red studio, P3 Podcast Magazine, P4 Before/After showcase, P5 Red-gradient explainer; 14 type techniques, 12 motion elements, 14 transitions with frame counts; incremental reference scanner; person-matte tool; online short-form research (hooks, safe zones, -14 LUFS) | V + ONL |
| `faceless-explainer-reel-edit-style` | Faceless voice-over explainer reel (profile P12), learned 2026-11-21 from the "zip 1" analysis pack: light cutout act then dark object act, blur-in two-font captions, stat wedge, object-with-a-state, light-leak flash, a sound on every scene change; includes how to borrow its devices in talking-head shorts | Analysis pack (frame sheets + data), nothing rendered yet |
| `event-map-reel-edit-style` | Event-map method for every short (three laws, word → event sync offsets, transition-by-meaning table, SFX grammar, QC checklist) plus two styles learned 2026-11-22 from the "zip 2" analysis pack: P13 two-tier kinetic talking head and P14 faceless 2.5D documentary story; measured RAW vs EDITED wrapper layout; transition and device recipe files; scorecard script (not run here yet) | Analysis pack (5 reels: sheets + data), nothing rendered yet |
| `ultimate-editors-shortform-style` | P15 Ultimate Editors short-form look (2026-11-22): sans lead-in + one blue italic-serif keyword, three layouts (overlay on darkened lower band 43 %, split 26 %, full-screen off-white 31 %), four animation categories, 1-2-3 step pill; from the user's master prompt + one measured 49.75 s reel; the linked brief is still missing |  |
| `ue-sound-design` | Ultimate Editors (Joseph) sound design: whooshes = movement, textures = events, risers + hits = anticipation; passes in fixed order, levels -12/-10, -6/-7, -5, music -19 dB under the talking head only; Remotion track rules; its last section lists the clashes with the older sound rules and what is missing on this Mac (library, Remotion) |  |
| `beginner-to-pro-edit-tips` | Three rules heard in the 2026-11-22 training video, with numbers measured from the reel: every element 25 % smaller, special effects only on the one attention element, dull colours (off-white `#F0EEEA`, navy `#0B1E34`, dulled red `#D24E5A`); QC checklist |  |
| `watch` | Received skill: study a video (frame pairs, cuts, word timings, sound hits), turn it into measurable rules and save a new style skill from its template; `scripts/watch_mac.py` runs it on this Mac |  |
| `ae-builder` | Received skill: write one After Effects ExtendScript that rebuilds an animation as a clean project (rigs, fitted keyframes within 2 % of the source curve, slider-driven expressions, fonts + assets in the zip), strict mock dry-run gate; gate not yet run on this Mac |  |
| `motivational-video-editing` | Motivation / motivation+AI edits: colour, type, text animation, pacing, story, devices, B-roll; what made the video 13 v2 redo work | Delivered video |
| `video-intro-design` | 20-40 s dense intros/cold opens from one locked-off take: pixel-exact punch-ins on a 2560x1440 plate, Vision person mattes for giant type behind the head, measured accent colour, dither-through-black transitions, phone-speaker-safe SFX, six-lens QA | Delivered video |

## D. Long-form (16:9) editing
| Skill | What it teaches | Evidence |
|---|---|---|
| `youtube-long-video-editing` | 10-30 min explainer pipeline: transcript -> EDL join -> graded base frames -> HTML/GSAP scene engine -> stills QA -> render -> mix (-14 LUFS / -1.5 dBTP) -> final QA; layout & rhythm rules; per-video kits (Y2K, AI News ep1/ep2, RAG, Day 03, Sale phones, Day 06, video 13) | Delivered videos |
| `tharun-speaks-longform-edit-style` | Tharun Speaks long-form (10 min, 2:1, 25 fps): warm A-roll vs chalkboard graphic scenes, 20.9 cuts/min, median shot 2.4 s, behind-head headlines popping in 1 frame, keyword captions, wireframe brain/glass graphics, -10.3 LUFS | Measured |
| `aasil-khan-longform-edit-style` | Aasil Khan long-form (16:9, 30 fps, first 707 s of one video): low-key A-roll 58% / white scenes 26% / navy UI scenes 12%, 19 cuts/min, median shot 2.6 s, punch-in 1.21x, 26 light-leak flashes, recap chart + 4-part navigator + 3-stage staircase + split panel, typed notes synced to voice, measured hex palette, -16.5 LUFS | Measured |
| `motion-graphics-style` | Kinetic type, cards, charts, diagrams, split/framed talking-head layouts, luxury serif, dark neon, red-glass, frosted glass, editorial print-grain (default for 16:9 career/company/economics explainers), grade, SFX timing, fast-flow creator edit (Tharun, Somrat), podcast intros | Refs + delivered |
| `top-editor-styles` | 5 creator playbooks: MrBeast challenge, Hormozi talking-head, Johnny Harris documentary, Iman Gadzhi premium, calm educational; shared rules + QC list | Published |
| `text-highlight-match-cut` | Brush-stroke highlight on article/news text (marker wipe) and keyword-anchored match cut across real headlines; real-source capture | Delivered videos |
| `app-product-animation` | SaaS/product motion graphics with no talking head: motion grammar, type, grade, measured easing/duration ladder, SFX recipe, showreel formats, talking-head product review adaptation, premium SaaS news show | Refs + delivered |
| `client-video-editing-process` | End-to-end client pipeline: analysis, selective mask-based colour correction, research panel, HTML/GSAP kit, SFX/music, supersampled render, QA; "make this boring video high-engagement" | Delivered client edits |

## E. Sound
| Skill | What it teaches |
|---|---|
| `sound-and-music-design` | Audio-only redesign: measure the old mix first, SFX palette, music scoring, QA without ears (spectrograms, onsets, loudness), phone-speaker rule, adding sound to a delivered mix without touching it |

## F. Thumbnails
| Skill | What it teaches |
|---|---|
| `thumbnail-strategy` | Glanceability, focal point, face/gaze, separation, text, the 1+1=3 information gap, six formulas, honest 30 s payoff, mobile feed QA |

## G. Tools and maintenance
| Item | Use |
|---|---|
| `skill-saver` | Where every new rule, correction, asset or reference goes; how skills are created (82 references processed before this library) |
| `06-tools/_video-analysis-tools/` | 10 Python scripts: contact sheets, frame strips, motion curves, easing tracker, band onsets, spectrograms, SFX forensics |
| `pro-video-editing/tools/` | `refscan.py` (incremental reference scanner), `transcribe.py` (faster-whisper word timing), `vstrip.py` (aspect-correct frame strips, letterbox crop), `matte.py` (MediaPipe person matte), `render_p1_test.py` (technique test render) |
| Installed on this Mac | ffmpeg (imageio-ffmpeg), Python 3.15 + PIL/numpy/scipy, `~/.local/share/whisper-venv` (faster-whisper, OpenCV, MediaPipe), Node 20, HyperFrames (installed, not yet used for a final render) |

---

## Known gaps (what is NOT learned yet)
1. MrBeast / Hormozi / Johnny Harris / Iman Gadzhi rules are from public breakdowns, not measured from their videos.
2. Five screenshot-only looks in `training claude` (josephvideoediting bold yellow, whiteboard doodle, nikhil storyboard frames, canvers 50X, aslani product reel) need their videos.
3. Individual SFX in references are not identified (no stem separation run on the new library).
4. Fonts in references are matched, not identified.
5. `pro-video-editing` has not yet been used on your own raw footage; the first real edit will be its real test.
