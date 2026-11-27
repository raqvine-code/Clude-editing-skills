---
name: reel-editing-method
description: Use when editing a talking-head video into a high-engagement 9:16 reel with motion graphics, captions, HUD elements, behind-the-head text, SFX and music, or when asked to "edit it like the AI-AGI-ASI video". Full methodology from Deepak's first motion-graphics edit (68 s): structure, pacing, type, effects, audio, colour, transitions, IF-THEN decision rules, HTML/GSAP render pipeline, what worked/failed, QC checklist.
---

# Reel editing method (AI vs AGI vs ASI, draft 1)

Source: Deepak's Telugu talking head, 68.3 s, 1440x2560, 60 fps, CapCut keyframes already applied. Tags: [USED] done in this edit; [REC] recommendation, untested. Note: `experiment/` paths are historical; finals + notes live in `Raghu and claude/edited videos by claude/` (timings: `1. AI vs AGI vs ASI/code/comp.js`, beats: `EDIT_BREAKDOWN.md`). Related: `my-editing-rules` (Deepak always wins), `motion-graphics-style`, `broll-library`, `png-library`, `where-to-find-assets`.

Copy the method (analyse -> spine -> beat map -> tokens -> helpers -> preview loop -> mix -> QC), never this video's timings, colours or danger-meter idea.

## 1. Philosophy
- One visual system carries the whole video (here a danger meter: 3 levels, 3 colours, a climbing gauge, a running countdown), not a pile of effects.
- Viewer path: second-0 slam that stops the scroll; visible promise ("explained in 1:00"); something new every 2-4 s; tension rising to a payoff question as the timer hits 0:00; frictionless CTA in the last 5 s.
- Professional feel: fixed tokens (3 accents, Montserrat 500-900 display, JetBrains Mono for HUD, Caveat for annotations, one glass-card style); text *behind* the speaker via person mask; UI mock-ups that look like real apps; every graphic and transition has a sound; text lands on the exact word from a word-timestamped transcript; no preset transitions (only blur, motion-blur whip, glitch, flash, hazard-tape wipe).
- Speaker is the base layer; graphics never hide the face while he makes a point. One keyword = one graphic. On-screen text = his own words (translated), not marketing copy. Do not add keyframes to his footage. Design for phone: nothing important in bottom 15% or top 8%.

## 2. Structure (68 s)
| Section | Time | Job |
|---|---|---|
| Hook | 0-5.5 | Slam 3 words, "do you know?", promise 1 minute |
| Definitions | 5.5-12.4 | Calm glass card, 3 rows build word by word |
| Danger-meter intro | 12.4-14.6 | Full-screen takeover, gauge shrinks into HUD |
| Level 1 AI | 14.6-24.9 | ChatGPT UI story, 3 phases |
| Level 2 AGI | 24.9-45 | Glitch, header, bars, paper beat, stamp, example card |
| Level 3 ASI | 45-58 | Red flash, movie card, multiplying chips, chart blows out |
| Blackout question | 58-63 | Lights off, spotlight, ticker, giant "?", timer 0 |
| CTA | 63-68.3 | Light-leak reset, comment box, follow card, thank-you |

- Hook: first three spoken words = the three biggest graphics (440/400 px behind head), each with impact SFX and 0.2 s shake; dark grid background for the hook only; question caption right after; promise made concrete (big 1:00 flies to corner and counts).
- Pacing: new visual at least every 2-4 s; micro-events every 0.25-0.8 s inside cards; cards live 2-10 s, anything over ~4 s keeps changing internally; breathers after heavy cards.
- Each level change has a signature (AI = whoosh + card; AGI = RGB glitch + amber header; ASI = red flash + heavy glitch + alarm + red header).
- Tension: 2 s riser + red vignette before the ASI cut (43.5-45 s), released by flash. Final question drops the music; silence + drone = "important".
- Persistent countdown (top-right) and gauge (top-left) change state each level, so there are always two reasons to keep watching.

## 3. Timeline rules
- Jump cuts found from audio micro-silences (60-150 ms) are card boundaries. Never enter a card across a jump cut; enter just before/after.
- Every element timed to a word timestamp (faster-whisper large-v3). Enter 0.05-0.1 s before the word; exit on the next jump cut or when space is needed.
- Cut music once per video, on the single most important line (58.0-63.0 s here).
- No speed changes on talking heads (ramps break lip sync). No added camera moves; at most a 1-2% slow push on static cards.
- His CapCut zoom-out can expose a black band (~300 px at top; here 25.47-26.97 and 45.03-46.87 s): cover with a designed header strip starting one frame *before* the band.
- Rhythm big -> small -> big; never two takeovers back to back.
- Hold times: captions 0.6-1.5 s per phrase; keyword slams 0.4-0.6 s; cards 2-10 s with internal changes; end cards 3-4 s.

## 4. Text and typography
- Caption every spoken sentence that carries the argument; filler gets a small caption or nothing. Brand/app names get logos, not text. Numbers/lists get their own UI.
- Hierarchy: setup line (Montserrat 600, 46 px, 92% opacity) above one keyword (800, 70-84 px). Behind-head giants: Montserrat 900, 178-440 px, letter-spacing -0.035 em, line-height 0.9, auto-fit max 1000 px. HUD labels: JetBrains Mono 19-30 px, tracking 0.1-0.24 em, grey #8B8D93. Handwriting: Caveat 700, 92-112 px, red #D7261E, rotated -5 to -8 deg.
- Positions: captions centred, top y 1250 (over chest, not face), 1210 when a bottom card needs room. Cards 940 px wide, 70 px side margins, top 1030-1130, height 470-640. Behind-head words top 60-90 px (2026-11-25: that is inside the top UI band of Reels / Shorts / TikTok, so use y 270 or lower: `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`); measure head top per scene from masks (e.g. 156-350 px). Gauge (30,126), timer (818,126); nothing else in top 300 px except headers.
- Caption word animation: fade + rise 26 px + scale 0.9->1 + blur 10->0, back.out(1.8), 0.17 s, one word on its timestamp. Keyword slam: scale 1.45->1 + blur 14->0, expo.out 0.26 s, then 0.2 s decaying shake. Grey -> black/white "light up" 0.18 s after spoken. Exits: fade + rise -12 to -20 px + blur 8-14, power2.in, 0.14-0.2 s (exits always faster than entries). Typewriter: one char per tick, block cursor, key-click every 2nd char.
- Emphasis: accent colour on key word; hand-drawn ellipse and strike-through; outlined text (-webkit-text-stroke) for second word of a pair; rotated -5 deg stamp with shake for a verdict.
- Safe area x 60-1020, y 120-1700; follow card at y 1180-1510.
- Max one caption line + one card at a time; when a full card is up, drop the caption; never more than ~6 words per caption.

## 5. Motion graphics
Inventory used: behind-head slam words (hook); countdown timer (2.9-63 s); danger gauge SVG arc + needle (12.5-63 s); full-screen DANGER takeover + hazard-tape wipe; glass explainer cards; ChatGPT UI mock-up (chips into core, loading bar, typed prompt, streamed answer, capability rows); level header strips (also hide CapCut black bands); paper scene with giant grey->black words + handwritten aside; "THAT'S AGI" stamp; film-strip movie card with laser-scan reveal; multiplying AI chips + "AI x n" counter; intelligence bar that overshoots frame; blackout + spotlight + ticker; giant red outlined "?"; light-leak; Instagram comment composer and follow card with cursor click.

Principles: enter fast with overshoot (back.out 1.6-2.4 or expo.out), exit faster (power2.in/power3.in); blur on every entrance (16 -> 0); objects arrive from an edge or scale 0.2-0.5, never from nowhere; persistent widgets change state with needle overshoot (back.out 2.2), elastic settle for ASI; idle motion on anything staying >3 s (needle jitter, timer flash last 10 s, slow star rotation, chip waves).
Numbers: card entrance y 90->0, scale 0.97->1, blur 16->0, 0.32-0.36 s. Pop scale 0.4-0.7->1 back.out(2.2) 0.34 s. Slam 1.3-1.8->1 in 0.22-0.26 s, shake 8-14 px decaying 0.18-0.3 s. Stamp rot -14 -> -5 deg, scale 1.8->1. Counter/bar fills power1.inOut/power2.out 0.7-1.0 s; ASI bar power4.in. Timer flight scale 1->0.22 to corner, power3.in 0.34 s.
Layers bottom to top: base footage -> bgrep (dark grid/paper/red grid/black) -> behind (giant words, chips) -> person (footage clipped by per-frame person mask) -> front (cards, captions) -> hud -> fx (vignette, red pulse, flash, grain, glitch bars). Cards use backdrop-filter blur 26 px.

## 6. Effects
| Effect | Use | Avoid | Strength |
|---|---|---|---|
| Blur in/out | every entrance/exit | leaving half-blurred on hold | 8-16 px -> 0, 0.15-0.35 s |
| Glass backdrop | info cards over speaker | full-screen takeovers (solid bg) | 26 px, bg rgba(12,13,16,.78) |
| Glow | accent badges, gauge, timer, ASI bar | body text | 0 0 40-60px colour 40-66 alpha |
| Shake | after slam/stamp/impact | captions/small text; >0.3 s | 8-14 px, 0.18-0.3 s, seeded random |
| Motion blur (SVG feGaussianBlur X) | whip full cards | on text alone | stdDev 60-70 -> 0 over 0.18-0.24 s |
| RGB split glitch + scan bars | level changes, hard cut into ASI | >~3/min, calm sections | 0.14-0.22 s, dx 8-34 px, skew +-3 deg |
| Flash | section resets, impacts | back-to-back | white 0.18-0.5 over 0.22-0.32 s; red for ASI |
| Hazard-tape wipe | once, into danger meter | anywhere else | 0.17 in / 0.2 out |
| Light-leak | once, out of blackout into CTA | mid-argument | screen-blend radials 0.22 in / 0.45 out |
| Red pulse vignette | ASI section only | low/medium levels | opacity 0.2 +-0.13 at 0.9 Hz |
| Vignette + grain | always on | - | grain 0.075 moving each frame; vignette 0.38 |
| Person-mask compositing | hook, paper, chips, blackout | when mask edge is visibly wrong | MediaPipe selfie, smoothing 0.65/0.35, 1.2 px feather |
| Colour on footage | global only | per-scene grades shifting skin | contrast 1.06, saturate 1.07, brightness 1.02 |
Rules: one signature transition per section change (hazard tape and light-leak once only); every flash/glitch paired with a sound; shake the graphic not the frame (except hook); never blur the face longer than a transition.

## 7. B-roll
This edit was graphics-led; PNG assets used as graphic elements (ChatGPT logo -> white transparent, robo greyscale multiplied on paper, face crop for avatars).
[REC] B-roll is the fallback for beats with no good graphic; check `broll-library` first (professional-first). Hold 1.5-3 s, enter/exit with the same blur/whip language, keep HUD on top, tint toward level colour, never reuse a clip/PNG in two sections, match the spoken noun literally.

## 8. Music
- Pick: constant energy or slow swells, 100-125 BPM for tech, no vocals, no hook that competes with speech. Used "Tech beat" (~118 BPM). Rejected: Smooth 1 (10+ dB energy jumps), Interstellar (60 s silent intro), Loop 5 (unaligned drop).
- Start 0.02 s under first impact; fade last 0.6 s. Dip -5 dB from 44.6 s through the ASI hit. Full cut at 58.0 s replaced by low synth drone; back at 63.35 s under the light-leak. Never music under the key question, a heartbeat/drone moment, or when the speaker goes very quiet.
- Levels: voice bus 0 dB, music bus -15 dB (voice -15 LUFS vs music -33 LUFS, ~18 LU under); ducking up to -5 dB while voice > -40 dB RMS (attack k 0.5, release k 0.06, 10 ms frames). Master peak-normalised -1 dB, limiter 0.84 -> -13.8 LUFS, -1.3 dBFS (target -14 LUFS). Music at -22 dB was inaudible on phone; -15 is the floor.
- Beat-sync only when there is no VO or music is the point.

## 9. Sound design
- Kit: 29 procedural placeholder sounds (whooshes, swipe, pops, click, tick, 4 keys, impacts, risers, reverse swell, glitches, ding, notify, alarm, buzz, thump, shutter, scan, sparkle). Swap for Mixkit/Freesound/Pixabay sounds using `sfx_cue_sheet.csv` (147 cues); say so when delivering.
- Cues: whoosh on every card entrance (-4 to -10 dB, shorter for faster motion); pop on every chip/badge/row (-5 to -13; high pop small, low pop large); impact on 3 hook words (-1 dB, middle -3), ASI hit 0 dB, bar overshoot -3; tick/click for UI state (-2 to -12); keys every 2nd char (-14 to -18); riser 1.5 s before big change; glitch under every RGB split (-6 to -12); alarm under warnings (-13 to -16); scan under bar fills, ding at 100%; thump x3 under final question; buzz at timer 0; sparkle on Follow -> Following.
- Timing: SFX starts at the graphic's first frame (impacts may lead 1 frame). Density one per 0.4-0.8 s; never two whooshes within 0.25 s (drop the sound, not the graphic); pops >= 0.08 s apart may stack; impact + glitch + flash may stack.
- Hierarchy: voice > impacts > whooshes > pops/clicks > typing/ticks > drone > music. SFX bus -5 dB. Drone 55/82/110 Hz only in the blackout (0.6 s in, 0.15 s out).

## 10. Colour
- Palette: ink #0B0C0E, charcoal #141518, paper #E9E7E2, off-white #F4F4F1, grey #8B8D93; lime #C6FF33 (AI/low), amber #FFB020 (AGI/medium), red #FF3B30 (ASI/extreme), IG blue #0095F6, handwriting red #D7261E.
- One global filter on speaker, skin natural; vignette + moving grain on top. Alternate light/dark scenes (dark cards, bright paper, black blackout with warm spotlight).
- Glass cards: inner top highlight inset 0 1px 0 rgba(255,255,255,.08), 40-80 px drop shadow. Text on footage always has text-shadow 0 6px 26px rgba(0,0,0,.55).
- Level colour appears in gauge, header, badge, caption highlight and card accent simultaneously; never two accents in one card unless comparing. Mono B&W beats desaturate imagery to match references.

## 11. Transitions
Blur out/in (default, 0.15-0.35 s); whip with horizontal motion blur for full-frame cards (consistent direction in a sequence); RGB glitch for level changes (<=3/min); flash (never two within 1 s, pair with a hit); hazard tape once; light-leak once; hard cut on the speaker's own jump cuts (no transition on top); fly-to-corner when a big element must persist. If two cards are the same style, blur-swap; no zoom transitions, spins or preset slide wipes.

## 12. Decision rules (IF -> THEN)
- 2-5 named things -> colour + badge + persistent widget state each; widget is the spine.
- Duration promise -> real countdown ending on the payoff line.
- First sentence names subjects -> giant words behind head with impacts, no caption in first 1.5 s.
- Names an app -> mock-up of its UI, explanation plays out inside it in phases.
- Lists capabilities -> rows icon + label + check, one per spoken item, pop + tick.
- Compares two things -> two columns/bars, animate the difference last.
- References a movie -> titled film-strip card, one caption line, under 4 s.
- "like humans/us" -> paper/editorial look, handwritten aside.
- Argument peaks -> riser 1.5 s before, flash + hit + glitch, pulsing vignette after.
- Closing question -> cut music, black bg, spotlight, drone, heartbeat thumps, biggest symbol behind him.
- CapCut black band -> header strip one frame early.
- Card would cover his face -> y >= 1030 or split top/bottom; never over eyes while talking.
- Same layout twice -> change background or card style first.
- Caption > 6 words -> setup line + keyword, or drop setup.
- Element > 3 s -> idle motion. Graphic silent -> add pop/whoosh.
- Telugu/Hinglish -> transcribe per jump-cut chunk with large-v3 + domain prompt, caption in English keywords, keep proper nouns as spoken.

## 13. Tools and workflow
- Stack (no Remotion): HTML + GSAP rendered by headless Chrome. Transcription faster-whisper large-v3 int8 CPU, word timestamps, clip_timestamps from `silencedetect n=-38dB d=0.06`, condition_on_previous_text=False, domain initial_prompt. Small model and un-chunked large both hallucinated "AI, AI, AI..."; chunking fixed it (~15 min CPU for 68 s).
- Masks: MediaPipe selfie model 0 at 540x960, blend 0.65/0.35 within a shot, reset on scene cuts, S-curve, 1.2 px feather -> RGBA PNG per frame as CSS mask-image.
- Composition: `index.html` + `comp.js` (one paused GSAP timeline, `window.__seek(t)`, `window.__sfx` cue collector). Renderer `render.js` (puppeteer-core, one browser per worker, captureScreenshot JPEG q94, `--times`, `--scale 0.5` via clip scale, `--sfxout`). Audio: `sfx_synth.py`, `mix.py`, ffmpeg alimiter. Encode libx264 -preset slow -crf 17 master (bt709, full->tv), upload copy -crf 20 -maxrate 22M, AAC 320k/48k. ffmpeg came from imageio-ffmpeg wheel.
- Helpers in comp.js: blurIn/blurOut/pop/slam/shake/flash/glitch/whipIn/whipOut/typeText/caption/card/header; `textAt`+`applyTexts` (GSAP set textContent is not seek-safe); `fit(el,maxWidth)` canvas-measured; `rng(seed)` for repeatable shake/glitch; PERSON ranges set when mask applies.
- Preview: render 15-30 hand-picked timestamps at half scale -> contact sheet -> fix -> full render (4 workers ~18 fps at 1080x1920) -> QA sheet from the *encoded* MP4 at 2 fps -> pixel checks for black bands.
- Fixes: chunk Whisper by jump cuts; half-scale via clip.scale not deviceScaleFactor; one Chrome per worker; read the token map before using a key (IG blue vanished); start band cover >=1 frame early; ffmpeg drawtext has no fonts here, use PIL; pad SFX reverb wet to dry length.

## 14. What worked
One spine (gauge + timer); behind-the-head text (biggest pro signal for one segmentation pass); word-timed captions; app mock-ups; section signatures; music cut on closing question; header strips covering CapCut bands; previewing by timestamp; QA sheet from the final MP4 (caught a one-frame band gap).

## 15. What did not work
Hook words over the face (move above hairline after measuring masks); "HUMANS?" outlined behind hair (use two big "?" offset left/right); "like us!" on cheek (move to upper-right gap, scale 0.72); poster-like Robo card (title y 410-460, robots y 760, caption y 1330); AI x n counter colliding with caption (y 1452); "DANGER LEVEL" wrapping in HUD (use "DANGER"); BGM -22 dB; thin procedural SFX. Untried: desaturating speaker to match B&W refs, real B-roll cut-ins, beat-synced cuts.

## 16. Checklist
- Story: one-sentence spine; 6-8 sections with intensity curve; one peak, one quiet beat, one CTA.
- Hook (0-2 s): biggest graphic, impact SFX, no caption clutter, promise visible.
- Pacing: new visual <=4 s; micro-event <=0.8 s inside cards; cards enter just before the word; breather after every takeover.
- Text: setup + one keyword; <=6 words; word-timed; grey->bright; never over eyes; safe area.
- Graphics: one token set; blur on entrances; overshoot in, faster out; idle motion >3 s; behind-head layer used at least twice.
- Assets: pro only; literal noun match; no asset twice; tinted to palette.
- Effects: one signature transition per change; <=3 glitches/min; every flash has a hit; grain + vignette.
- Audio: flat-energy track ~18 LU under voice with -5 dB ducking; one full cut on key line; fade last 0.6 s; every graphic has a sound; riser before peak; cue sheet exported.
- Colour: accent = section state everywhere; skin untouched; light/dark alternate.
- Final QC: key-frame sheet; QA sheet from encoded MP4; black bands covered from first frame; -14 LUFS / peak <= -1 dB; deliver master + upload MP4 + stems + breakdown; save new Deepak rules via `skill-saver`.

## 17. Applying to a new video
1. Analyse: ffprobe, 1 fps contact sheets, jump cuts from audio, per-chunk word transcript, head position per shot from masks, locate black bands.
2. Find the spine (meter, checklist, map, scoreboard, timeline, phone screen); else use the two-size type system from `motion-graphics-style`.
3. Map beats to graphics via section 12, one graphic per beat, colour token per section.
4. Build with comp.js helpers (keep layers, `__seek`, `textAt`, `fit`, `rng`).
5. Preview by timestamps -> fix -> full render -> QA from MP4.
6. Mix: voice 0 dB, SFX -5 dB, BGM -15 dB ducked, master -14 LUFS; export stems + cue sheet.
7. Deliver master + upload + breakdown.


Full original notes (every detail, uncut): `_archive/original-full/reel-editing-method.md` in this folder.
