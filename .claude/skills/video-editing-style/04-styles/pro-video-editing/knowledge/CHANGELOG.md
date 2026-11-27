# Knowledge base changelog

## 2026-11-15 - initial build
- Scanned `/Users/raghusai/Desktop/training claude/`: 13 videos (12 unique), 53 screenshots (51 unique).
- Pass 1: 0.5 s contact sheets for all 12 videos (all viewed). Pass 2: native-fps strips on 22 key moments across 11 videos (cab9/7a74/1ef4/94a1 letterbox-cropped). Transcripts (faster-whisper base) for 9 videos with speech; 3 motion ads are music-only.
- Profiles created: P1-P5 (video-verified), screenshot-only S1-S4.
- Tool fixes: cut detection moved from ffmpeg scene score (under-reported on motion graphics) to adaptive frame difference on the active picture area (letterbox crop).
- Validation (tools/render_p1_test.py -> knowledge/tests/): P1 statement build re-rendered on an abstract background. Measured change frames: glass frame f3-f9 (plan f2-f9), keyword slam f27-f30 (plan f26-f30), swap f61-f67 (plan f60-f66), whip f82-f89 (plan f82-f88) = within 1 frame. Side-by-side `p1_vs_ref.jpg`: hierarchy, colour, glass frame, circle and whip match; differences: no person plate (no footage supplied), reference light streak and loading squares not rebuilt, fonts are system substitutes (Avenir Next Heavy / Helvetica Neue Light / Snell Roundhand). Test swap placed at f60 (reference f89) to fit a 100-frame test.
- Added `library/shortform-online-research.md` (web research: hook, length, captions, safe zones, loudness; label ONL, sources listed).
- Added `tools/matte.py` (MediaPipe 0.10.14 + OpenCV in ~/.local/share/whisper-venv); tested on 94a17cc80891 @8 s: text-behind-subject composite works, hair edges slightly blocky.
- Known gaps: SFX not identified; fonts are matches not identifications; 5 screenshot sets have no video; beat-sync verified in only 1 of 7 music-led clips.

## 2026-11-16 - first real edit with this skill: "16. Uncertainty Short" (raw 1115, 64.5 s -> 47.5 s)
- Pipeline that worked: analyze_raw.py -> plan workflow (6 skill readers, 3 planners, 2 judges, synthesiser, adversarial reviewer) -> PLAN.md -> one authoritative frame map -> 4 parallel build tracks (footage plates + Vision mattes + mask grade; audio voice cut + SFX + mix; B-roll slots; word onsets) -> HTML/GSAP kit (Mr Unbox) scenes -> 47 stills -> 13.7 s sample -> full render (4 shutter sub-frames, 24 in fast windows) -> QC -> save routine.
- Measured gotchas: 60 fps file was 24p 2:3 cadence; plan face sample and head top were wrong (measure, don't trust); ASR word starts ~1 word early (adjudicate on syllable landmarks); baked vignette/grain + page overlays double up; inline comment before `}` broke scenes.js (node --check); IMPACT_FILM transient 0.832 s; stereo widener notches knocks in mono.
- New code-level QC: caption groups < 0.5 s / keywords < 0.35 s are logged; wrapped connector lines balanced (no orphans); wall words anchored to measured head top in the framing incl. 0.55 parallax.
- Output and notes: `Downloads/claude/Raghu and claude/edited videos by claude/16. Uncertainty Short/`; project `CLAUDE 2.0/edits/1115/`.

## 2026-11-16 - v2 of "16. Uncertainty Short": real source page on the Gita beat
- User OK'd the web capture; row 25 swapped from the typeset fallback card to a real Wikisource capture (Besant 4th ed., 1922, Discourse 2 v.47) with a #F5C400 multiply highlight wiped on "action". Lessons added to `text-highlight-match-cut` section 8 (scroll fix, read the year off the page, Layout 2 fixed column, marker inside the page's isolated band).
- Patch render: only frames 31.9-35.15 s re-rendered into a clone of the v1 frame folder (`cp -c`, APFS clone), then re-encoded and re-muxed with the unchanged mixes.

## 2026-11-16 - second real edit: "17. Embarrassment Short" (raw tes2, 46.3 s -> 32.9 s)
- External assets: 14 Pexels 4K clips (Mixkit video is now 720p personal-use only; Coverr free is 1080p), Fluent 3D emoji (MIT), a LottieFiles twinkle, a Wiktionary capture, and 33 Mixkit / Freesound CC0 SFX, all logged in CREDITS.txt.
- Build: 5 parallel tracks (plates/grade, audio, B-roll, MG components, words), then integration, 2 samples, 2 reviewers (taste + sync), a fix pass, and the full render (23 min at 6 workers, 4 sub-frames, 24 in fast windows).
- Gotchas: the Mac slept on a dead battery mid-build (use keep-awake + caffeinate); `render.js` could hang on `browser.close()` at 7 workers (now a 20 s race, then exit); grade region targets met but whole frames stayed dim, so a light pass (`post_light_tes2.py`) was added on top; two-line caption stacks need ink-based gaps; slams scale from the cap top.
- Process lesson: a 2.8 h, 12-agent plan was too slow for a 33 s short. Next: one planner + one reviewer, reusing this kit.

## 2026-11-17 - "18. Go All In" (1115 (1)(1).mp4 -> 16.4 s), built lean on the tes2 kit
- Lean run: no workflow, no subagents, 1 web search, a 2-page PLAN.md. The tes2 kit was copied and patched (grade + light pass, captions, slots, transitions, render, voice chain, limiter). New code: a B-roll time-map prep (speed ramps, freeze), a 120-line cue mixer and a `fillWord` canvas component.
- Raw moved: the user now sorts CapCut into `to be edit by claude/` and `edited by claude/`. Old keeps were remapped to the new file by sample-level audio NCC (7/9 lines at 0.99+, whole-frame offsets). Check the raw exists before reusing an analysis.
- Canvas: after a `source-in` fill, switch to `source-atop` for every later draw (highlights, bubbles), or each shape erases the rest. Verify canvas effects by pixel read-back, not only stills.
- Slow-mo freezes must land on a whole source frame (time x fps integer), or the freeze is a ghosted blend. B-roll levels: one map per clip (a per-frame map pumped confetti 0.75-1.45x).
- Sound: measure every SFX against the voice in 300-4000 Hz for 0.3 s after landing. Move hero hits to the picture event just before the word (splash 4 f before "want.") and duck them.

## 2026-11-17 - 4 references + Edit-Kit learned
- refscan: 4 NEW videos (copied from Downloads into `training claude/training videos/`), 66 unchanged, transcripts added. Viewed as 1 fps compact sheets + one close-up strip only (low-credit run).
- New profiles: P6 violet condensed tips, P7 noir red kinetic, P8 real-estate orange explainer, P9 lime studio personal brand; P4 gained shell layouts C-F.
- Edit-Kit (40 skills) vendored to `07-edit-kit-reference/`, distilled into `02-craft/edit-kit-playbook/`.
- Tool fix: `shorts-editing-pro/tools/shortkit.py` default ffmpeg path (aimldl_reels/bin) no longer exists; now falls back to PATH / Homebrew / imageio_ffmpeg.

## 2026-11-21 - "zip 1" analysis pack learned -> P12
- Source was a zip with a ready skill file, 3 fps contact sheets, 13 frame-numbered sheets, 3 stills, transcript, scene scores and audio band data; no video, so refscan and learnkit were not run. Pack stored in `04-styles/faceless-explainer-reel-edit-style/references/pack/`.
- New profile: P12 editorial cutout explainer (faceless voice-over reel, light act then dark act). Full text lives in its own skill `04-styles/faceless-explainer-reel-edit-style/GUIDE.md`; `profiles/P12-editorial-cutout-explainer.md` is a pointer.
- Libraries: X15 light-leak flash with scanline landing, X16 object wipe, X17 one-frame invert, X18 zoom-through, X19 re-stage; T15 blur-in two-font word reveal, T16 random character fade; M13 stat wedge, M14 metaphor object with a state, M15 line-art draw-on, M16 ghost word, M17 rise entrance with creep; P12 row in timing-sound.
- Pack claims corrected from its own frames: reveal timing against the voice, punchline cut position, speech rate. Nothing rendered yet.

## 2026-11-22 - "zip 2" analysis pack learned -> event-map method, P13, P14
- Source was a zip (39 MB, 275 files) with a ready skill file, reference files and per-reel sheets + data for 5 reels; no video, so refscan and learnkit were not run. Stored in `02-craft/event-map-reel-edit-style/` (pack under `references/pack/`).
- New profiles (pointers): P13 two-tier kinetic talking head, P14 faceless 2.5D documentary. R0 of the pack is the P12 reel again. P4 gained the measured RAW vs EDITED layout.
- Libraries: one pointer entry each in transitions-effects, typography-motion and timing-sound; the recipes stay in the skill's `references/transitions.md` and `references/devices.md`.
- Pack numbers checked against its transcripts and scorecards; turn range widened to 60-77 %. Nothing rendered; scorecard script not run on this Mac.

## 2026-11-22 - five skills received -> P15 + ue-sound-design + beginner-to-pro-edit-tips + watch + ae-builder
- Sources: `Prompts List.docx` (master prompt; linked brief not received), `UE-Sound-Design-Claude-Training-COMPLETE.md`, `watch-skill.zip`, `ae-builder.skill`, one finished reel 49.75 s + its raw 76.3 s (words transcribed with large-v3).
- New profile (pointer): P15 Ultimate Editors sans + script talking head; full text in `04-styles/ultimate-editors-shortform-style/`.
- The reel was studied with the received `watch` skill through `watch/scripts/watch_mac.py` (working folder `edits/_watch-studies/ue-3-mistakes-reel/`); refscan and learnkit were not run and the two videos were not copied into `training claude`.
- Not verified: sound (nobody listened), ae-builder gate (not run), anything in the missing brief.
