---
name: pro-video-editing
description: Use when planning, editing, animating, reviewing or rendering a short-form or talking-head video in a premium creator style learned from the user's reference library (glass spotlight motion ads, editorial red studio, podcast magazine edits, before/after showcases, red-gradient YouTube explainers), or when new reference videos/screenshots are added to "/Users/raghusai/Desktop/training claude" and the knowledge base must be updated.
---

# Pro Video Editing (reference-learned)

A modular editing knowledge system built from the user's reference folder `/Users/raghusai/Desktop/training claude/` (16 unique videos, 53 screenshots; scanned 2026-11-15, +4 videos 2026-11-17). Load only the files you need.

## Evidence labels
V = verified frame by frame or measured; S = seen on 0.5 s sheets; SC = screenshot only (no motion claims); E = estimated reconstruction. Never state an E or SC item as fact; never claim a render that was not made and checked.

## Choosing a profile (do not blend profiles in one video)
| Need | Profile file |
|---|---|
| 6-10 s brand/agency/value ad, music-led, cut-out subject + glass frame + 3-tier type | `profiles/P1-glass-spotlight-motion-ad.md` |
| Personal-brand / hiring intro on light studio, giant red italic words, halftone + streak transitions | `profiles/P2-editorial-red-studio.md` |
| Podcast clip or quote reel as a magazine page, serif italic keywords, B-roll strips | `profiles/P3-podcast-magazine.md` |
| Portfolio post: raw vs edit, price or results comparison shell | `profiles/P4-results-showcase-shell.md` |
| 16:9 talking-head explainer (and its Shorts cut), red gradient, glass UI cards, behind-head words | `profiles/P5-red-gradient-explainer.md` |
| Numbered tips talking head, violet grade, condensed giant word behind head, chapter cards, list pills | `profiles/P6-violet-condensed-tips.md` |
| Dark brand/agency opinion clip, red giant word, B&W silhouette-stroke grid, stat slam, grain dissolve, logo bug | `profiles/P7-noir-red-kinetic.md` |
| Real-estate / finance Q&A reel, orange two-tier captions, split comparison, B&W B-roll + gold word, icon halo | `profiles/P8-real-estate-orange-explainer.md` |
| White-studio personal brand, lime 3D ribbon, serif italic word behind, circle crop, search UI (+ Claude promo shell) | `profiles/P9-lime-studio-personal-brand.md` |
| Seated educator "3 tips / 3 mistakes" reel, dark studio + amber: typed search-bar title scenes, one-word chest captions, background takeover behind the speaker, themed paint wipe | `profiles/P10-amber-ui-educator-tips.md` |
| Podcast / interview clip: light two-size captions, every quotable line becomes a full-screen scene with the words placed inside it, palette from the guest's clothes | `profiles/P11-podcast-scene-inserts.md` |
| Faceless voice-over explainer (finance / business facts, "X owns Y%", product or template promo): light studio cutout scenes that flip once to dark glow object scenes, blur-in two-font captions, logo stat wedge, light-leak flashes, a sound on every scene change | `profiles/P12-editorial-cutout-explainer.md` (pointer; full skill in `04-styles/faceless-explainer-reel-edit-style/`) |
| Talking-head tips / opinion / client A-roll, heavy edit: small line + one big role-coloured keyword, three modes switched in the breaths, hidden jump cuts, speaker inside graphics, pedestal lists | `profiles/P13-two-tier-kinetic-talking-head.md` (pointer; full skill `02-craft/event-map-reel-edit-style`) |
| Faceless voice-over story (history, news, mystery): stills as 2.5D dioramas, camera never stops, scene changes as moves, text only when the word is the picture, SFX grammar with no music | `profiles/P14-faceless-2p5d-documentary.md` (pointer; full skill `02-craft/event-map-reel-edit-style`) |
| Calm premium talking-head tips / list short: small sans + one blue italic-serif keyword, UI pills over a darkened lower band, split and full-screen off-white scenes, 1-2-3 step pill | `profiles/P15-ultimate-editors-sans-script.md` (pointer; full skill `04-styles/ultimate-editors-shortform-style`) |
| Aesthetic, advanced talking head at Instagram-editor level (Naveen bro client): dark warm grade, M4 haldi-kumkum blur-reveal captions, cut every 2-2.5 s, literal B-roll per noun, one quiet insert every 6-8 s (paper cut-out scene + haldi ribbon, face HUD, face ring, number giants) | `profiles/P16-aesthetic-pro-reel.md` (pointer; full skill `04-styles/aesthetic-pro-reel-edit-style`) |
| Looks seen only in screenshots (bold yellow Shorts, whiteboard doodle, storyboard frames) | `profiles/screenshot-only-styles.md` |

## Libraries
- `library/typography-motion.md`: T1-T14 type techniques, M1-M12 motion elements (what/why/how/when/evidence, frame counts).
- `library/transitions-effects.md`: X1-X14 transitions with frame counts and build steps; grades/textures; what to avoid.
- `library/timing-sound.md`: measured pacing per profile, word-sync rules, duration cheat sheet, sound design.
- `library/shortform-online-research.md`: platform mechanics from web research (hook, length, captions, 1080x1920 safe zones, -14 LUFS) with sources; label ONL.
- `workflow.md`: brief -> ingest -> story cut -> shot-by-shot plan -> build -> sound -> review -> deliver.
- `qc.md`: automatic checks, visual checklist, side-by-side test against references.
- `knowledge/reference-index.md`: every source file, creator, specs, profile, screenshot mapping.
- `knowledge/observations-frames.md`: frame-numbered evidence per video. `observations-raw.md`: sheet-level notes.

## Core principles (all V across >= 2 references)
1. Hook moves within the first 3 frames (blur-in, glitch, card shrink).
2. Hierarchy over decoration: small lead + one big keyword; one accent colour per video.
3. Keyword graphics land 0.1-0.35 s before or on the spoken word.
4. Fast entries (2-8 frames at 30 fps) with motion blur; slow moves only for camera pans / card shrinks (~1.3 s).
5. Transitions are motivated by motion (streak, whip, wipe, shrink, morph); no generic dissolves.
6. Showcase shells stay still; motion lives in one place at a time.
7. Behind-subject giant words need a clean person matte.

## Applying to new footage
First `python3 tools/analyze_raw.py <video> <project_dir>` (facts, silences, word transcript, sheets, pre-filled PLAN.md), then complete PLAN.md (template `01-process/mastery/05-PLAN-TEMPLATE.md`, incl. 2-3 "Claude's idea" moves) before any editing. Follow `workflow.md`. Always write the shot-by-shot plan (time | words | on-screen text tier | element | transition | SFX) before building. Render a 10-15 s sample first, run `qc.md`, then the full video. Respect the user's standing rules in `my-editing-rules` (e.g. -14 LUFS master, Mixkit/Freesound/Pixabay for SFX).

## Continuous learning (when the user adds references)
1. `python3 tools/refscan.py "/Users/raghusai/Desktop/training claude"` - hashes every file; only NEW/CHANGED videos are analysed (probe, loudness, cuts on the active picture area, 0.5 s sheets, frame-diff); unchanged files are skipped; duplicates and removals are reported.
   - Deep study of ONE new reference video for the fewest tokens: `bash tools/learnkit/learn_video.sh "<video>" "<study_dir>"` (one frame per shot, OCR of all on-screen text, face-size punch-in stats, stereo music/SFX analysis, transcript). Read `tools/learnkit/README.md` first; view the shot sheets instead of the 2-fps sheets.
2. `~/.local/share/whisper-venv/bin/python tools/transcribe.py` - adds word-timed transcripts for new cache entries only.
3. View only the new `knowledge/cache/<hash>/sheet_*.jpg`; then `tools/vstrip.py <video> t0 t1 out.jpg [fps] [tile_w] [cols]` (env `CROP=w:h:x:y` for letterboxed clips) on each new technique.
4. Add findings to `knowledge/observations-frames.md`, update or create a profile (new profile only if the look differs in type system + colour + motion grammar), update `reference-index.md`, and append to `knowledge/CHANGELOG.md`. Promote screenshot-only styles when their videos arrive. Never delete earlier verified findings; mark superseded ones.
Token rules: never re-view unchanged sheets; read cache JSON/notes instead of re-extracting; strips only around events.
