---
name: client-video-editing-process
description: Deepak's second-generation, end-to-end pipeline for turning a plain talking-head (client or own) into a professional, high-engagement motion-graphics short — footage analysis and selective colour correction, live reference research (Behance/Dribbble/LottieFiles/Pinterest) via a multi-agent workflow, concept panel and judging, the HTML/GSAP build kit (camera keyframe track, person-mask depth, colour worlds, odometers, countdown, flat map, 3D flip), procedural SFX + music fitting + mastering, motion-blur supersampled rendering, and a six-lens QA workflow (run once on the v4 master: 32 heavy findings skeptic-checked, the confirmed ones fixed before delivery). Built from the "Mr. Unbox — iPhone 18 Pro" edit (draft 2); §10 adds draft 3, the SaaS-style IKKO MindOne product review (tracked UI objects on footage, B-roll edit list, music-led bed, highlight + match cut, zsh/mask gotchas). Load for any client edit request, "make this boring video high-engagement", "professional motion graphics", camera keyframes/zooms/rolls, price/number reveals, map/route beats, or when reusing the build kit in edited videos by claude/2. Mr Unbox iPhone 18 Pro/code/.
---

# Client reel — professional motion-graphics pipeline (Draft 2)

> **Note (2026-10-06):** `experiment/` paths in this skill are historical — that folder was cleared. Final videos + edit notes: `Raghu and claude/edited videos by claude/`. Reusable code: the `code/` folder inside each video folder. Reference analyses were folded into the skills and deleted.

Project: `experiment/claude3/` — source clip `/Users/raghusai/Movies/CapCut/Claude, 3rd video .mp4` (25.4 s, English, 1440x2560@60), channel **Mr. Unbox**, topic: iPhone 18 Pro / Pro Max via Blinkit, prices, Dubai/USA discount tip. Deliverables live in `experiment/claude3/deliver/`. Reusable code: `edited videos by claude/2. Mr Unbox iPhone 18 Pro/code/` (see §5). Previous project (draft 1) is `reel-editing-method`; this skill supersedes its tooling and adds research, QA and new components. Look/feel rules still live in `motion-graphics-style` and `my-editing-rules` (Deepak's latest instruction wins).

## 0. Rules learned in this project (read first)
- **Client videos are not Deepak's own exports.** Deepak's own CapCut exports already carry keyframes (never add more). A client clip with no keyframes gets a full camera-keyframe language (punch-ins on words, 2–5° rolls, pushes, a freeze-frame hit). `(2026-09-30)`
- **Brand:** use the *client's* name/sign-off (here "Mr. Unbox", spoken at the end). Never leak Tech Boy Deepak branding; never invent a social handle. `(2026-09-30)`
- **Fact discipline:** on-screen facts = only what is spoken. No invented prices/specs/dates. Editorial paraphrase (e.g. "YOU GET", "DELIVERED") must not create a new claim. Where the speaker points at material we don't have ("the prices are showing here"), leave a clearly labelled pointer, never fabricate the data. `(2026-09-30)`
- **Maps and borders (India):** do NOT draw or fill country polygons of India (or any disputed region). Use the land silhouette (no internal borders) + soft glow regions + nodes/labels only. `(2026-09-30, from the panel's feasibility judge)`
- **Third-party marks:** typographic stand-ins only (uppercase "BLINKIT" on a plain yellow pill; generic phone with no Apple logo). Lowercase logo lookalikes were rejected. `(2026-09-30)`
- **Deliver honestly:** placeholder SFX are procedural; say so and ship the cue sheet for Epidemic Sound swaps (`EPIDEMIC_API_KEY` was not set).
- **Stages must clear the mouth.** A lower-third stage (price panel, map card, coupon, ticket, countdown, chips) must start below his chin: with the camera lifted (`y -45`, `s >= 1.045` on every settle) the stage top is **y >= 1000**; nothing may straddle the lips. Test at every stage beat (3.6, 8.5, 17.5, 20.5 s ...). The v4 master hid his mouth for ~60 % of the runtime because every stage started at y 900. `(2026-09-30, QA)`
- **Whisper word times can be 0.5 s wrong at the end of a clip** ("Mr." was stamped 24.08 but is voiced at 24.57 after a 0.25 s pause). For hero words verify the onset with a 20 ms RMS envelope of the voice stem, not just the transcript. `(2026-09-30, QA)`
- **Never show a fake zero.** A price odometer must not idle on "0,00,000" while the speaker is still saying "the price is": hold the place with the sealed-price dots and reveal the digits at `tOdo0 - 0.1`. `(2026-09-30, QA)`
- **Don't invent product facts in illustrations.** Two phones of different colourways implied colours nobody said: both are neutral graphite; "less than 10 minutes" keeps its "UNDER" on the ticket; no "02" series numbers, no "INDIA" label the speaker didn't say. `(2026-09-30, QA)`
- **Wide words cannot sit behind a head.** A 900 px word behind a face is fully occluded (only "DI...UN" showed). Behind-head type must be short (18 / PRO) or sit above the hair; wide words (DISCOUNT, "10 min") go in the front layer as outlined type (`WebkitTextStroke` + `paintOrder: stroke fill`). `(2026-09-30, QA)`
- **Ask the user to open the Browser pane** before screenshot research (it is hidden by default and screenshots fail). Text-only research is much weaker and slower.

## 1. Pipeline (do in this order)
1. **Analyse the clip** (10 min): ffprobe; 0.5 s contact sheets; `silencedetect` for jump cuts; transcript with `faster-whisper large-v3`, `language="en"`, word timestamps (English needs no chunking; Telugu did — see draft 1). **Verify every number with a second pass** (small model + beam/prompt variants) before putting it on screen. Measure colour (wall/face RGB, luma percentiles), audio (LUFS, true peak, clipped samples, spectrum), head position per frame from masks.
2. **Write `BRIEF.md`** for the panel: client request verbatim, footage facts, transcript table, FACT DISCIPLINE, stack, quality bar. (`experiment/claude3/BRIEF.md` is the template.)
3. **Research + concepts + judging = one Workflow** (`claude3-research-concepts-judging`): 4 parallel researcher agents (one per site, each in its own browser tab; screenshots if the pane is visible, otherwise text-only), 3 concept agents (angles: typography-led / product+depth / quick-commerce pop), 3 judges (retention, craft, feasibility+facts). Always mix: the winning direction is a synthesis, never one concept and never a reference copied. Budget ≈ 45 min wall clock; run it in the background while you build the foundations.
4. **Foundations while the panel runs:** selective colour correction + un-mirror + head-top table; SFX kit v2; mix script; camera/typography/component kit; renderer.
5. **Build scenes** beat by beat from word timestamps; check every beat with 0.5-scale key frames (`render.js --times`), then a full-length low-res pass.
6. **Final render** with 4× temporal supersampling (true motion blur), mix audio, encode.
7. **QA workflow** (`qa_workflow.js`): six lenses (typography, sync, footage/grade, engagement, facts, audio) → adversarial verifier per critical/major finding → fix → re-render.
8. **Deliver:** master + upload MP4, stems, cue sheet, CapCut keyframe table, reference board, breakdown, source.

## 2. Footage correction recipe (selective, mask-based)
- The wall had a mint/green cast (118,141,128); a global fix pushed skin magenta. **Correct background and subject separately** using the per-frame person mask (MediaPipe selfie model 0, 540x960 → CSS/PIL mask). Script: `correct.py` logic — subject: gamma 0.94, +5 % saturation (hue-preserving), +5 % contrast; background: channel gains R 1.035 / G 0.955 / B 1.015, saturation 0.78, brightness 0.93, contrast 1.04; mask edge = MaxFilter(5) + Gaussian 3 + bilinear upscale. Skin stays R>G>B and natural.
- **Un-mirror** selfie footage (shirt text was reversed): flip frames AND masks.
- **Headroom guard** in `runtime.js`: measured head top per frame (`headtop.js`, 134–214 px); after any camera transform keep ≥ 84 px above the hair (pushes the frame down when needed).
- Creative grade in-browser: `contrast(1.12) saturate(1.0) brightness(.95)`, cool top/bottom multiply tint, warm top screen light, vignette, per-frame grain.

## 3. Design system used
Tokens: ink `#08090B`, off-white `#F5F5F2`, cream `#EFE9DD`; **yellow `#FFD60A` = speed/price/delivery**, **cyan `#6EE7DF` = brand + route + Pro Max**, **green `#3DDC84` = savings only**. Type: Bricolage Grotesque 800 (numbers/display, −0.035 em), Instrument Serif italic (soft words), Inter (UI), JetBrains Mono (labels, ≥ 30 px, tracked). Rules: min text 30 px, min stroke 4 px, safe area x 60–1020 / y 120–1700, one hero per beat, every graphic has a sound, blur-in entrances, exits faster than entries, no glitch/RGB-split, no starburst badges, no coin rain.
**Colour worlds behind him (via person mask) are the cuts:** yellow opener (0–1.3 s, ink "18") → room + dark stage → yellow delivery world (4.28–5.92, ink "10 min", black countdown disc) → dark price stage → cream paper "But…" interrupt (0.38 s, 5-frame freeze) → dark map stage → green savings world (20.2–22.6).

## 4. Beat structure that worked (25 s)
hook (giant type behind head + push-out) → model names (phones + MAX sticker) → brand stand-in ticket → countdown (stepped, ends with a drawn check) → **sealed-price pill from frame 0 that morphs into the price panel** → two prices (odometers with digit locks on the syllables + glint) → cream "But…" → kinetic "what I SUGGEST" → map (Gulf → whip west → wide → phone rides the arc, "bring one" set on the arc → macro push) → **map card flips in 3D into the coupon** → discount (word behind head) → "prices" pointer → sign-off ("Thank you" serif → "Mr. Unbox" lockup + orbs). Music: two beat-aligned segments joined inside the "But…" silence; a 0.3 s **vacuum** before the discount hit.

## 5. Build kit (files in `edited videos by claude/2. Mr Unbox iPhone 18 Pro/code/`)
| File | What |
|---|---|
| `index.html` / `runtime.js` | layers (bg, base, bg2, behind, person, world, front, hud, fx), fonts (fontsource CSS), `__seek(t, frame)`, camera transform + head guard + micro-drift, frame/mask loading |
| `core.js` | GSAP master timeline, `sfx()`, `musicKey()`, **camera keyframe track** (`camKey/camMove/camPunch` — punches anticipate the word by 2 frames), shakes, freeze holds, `personOn()`, blurIn/pop/slam/whipX/chars/maskLine/typewriter helpers |
| `components.js` | `phoneBack` (generic Pro phone SVG, 4 colourways), `odometer` (rolling digits, Indian grouping, per-digit `locks`), `countdownFlip` (stepped ring, squash-flip numerals, drawn check), `ticket` (notched card), `glass`, `makeFlatMap` (print-style map, tracking camera, nodes, hairline routes + comet head, carriers, text on a route, pulses, glows), `burst`, `speedLines`, `makeGlobe` (kept but rejected as cliché) |
| `scenes.js` | the edit (all timings, text, cues) |
| `render.js` | puppeteer renderer: `--sub 4 --shutter 0.5` writes sub-frames `%06d.jpg`; ffmpeg `tmix=frames=4,select='eq(mod(n\,4)\,3)'` averages them into true motion blur; `--sfxout` exports cues/music/camera keys |
| `sfx_synth_v2.py` | 58-sound procedural kit (whooshes, sub hits, risers, glass ticks, cha-ching bell, Doppler pass-bys, semitone ladder, shing) |
| `mix2.py` | voice restoration (adeclip, 72 Hz HPF, EQ −3.2 dB@420, +3.4 dB@2.8k, −3 dB@5.4k, air shelf, 2.4:1 comp) → −16 LUFS; SFX bus; two-segment music with low-pass automation + voice ducking; master −14 LUFS / −1 dBTP |
| `export_cues.js`, `make_docs.py` | cue export, CapCut keyframe CSV, cue sheet |
| `audit_scenes.py`, `splice_windows.py`, `render_final.sh` | comment-swallow / call-count audit after every patch; 24-sample whip windows spliced into the 4-sub-frame sequence; the whole final-render chain in one script |
| `qa_workflow.js` (in `experiment/claude3/`) | six-lens QA + adversarial verification |

## 6. Gotchas (all hit in this project)
- GSAP does not render zero-time `set`s on an exact-0 seek → seek `max(t, 1e-4)`.
- Half-scale previews: use `Page.captureScreenshot` `clip.scale`, not `deviceScaleFactor`.
- One Chrome per worker (tabs starve each other). Render ≈ 4–5 frames/s ×4 sub-frames with 5 workers (≈ 7 min for 25 s).
- Fonts: import fontsource CSS (unicode-range) or ₹ falls back; `document.fonts.load(..., '₹')`.
- `overflow:hidden` + geometry morph (pill → panel) works; keep decor in a container faded in after the morph.
- Text-on-path and phone icons are drawn in screen space (constant size) from a bezier sampled in screen coords.
- Comments swallowing code (`// ... ; nextStatement()` on one line) — put comments at the end of the line. **It happened again in v6**: a patch appended a `//` note to a line that also held `tl.to(tMax, {opacity:0}, 3.86)`, so the MAX sticker stayed on screen for 22 s and only the check of the *delivered* file caught it (`node --check` cannot). Run `build/audit_scenes.py scenes.js <backup>` after every patch, and always look at frames of the final MP4 at 10+ times before sending.
- Reversed swells/risers **climax at their end**: start them `duration` earlier so the climax lands on the hit.
- Music beat-fit: score beat-grid alignment of the key hit times per segment; Tech beat: segment 1 offset 0.908 s, segment 2 offset 3.56 s, join at 12.26 s.
- **Fast map moves need more shutter samples:** 4 sub-frames make a 224 px/frame whip look like 6-8 stacked ghosts. Re-render only the fast windows (whip 14.75-15.32, pull-back 15.95-16.58, macro push + flip 19.42-19.96, card entry 13.98-14.25) with `--sub 24 --shutter 0.5`, then average groups of 6 into the 4 expected sub-frames (`splice.py`) so the normal `tmix=frames=4` encode still works (121 frames, ~3 extra minutes).
- **JPEG frames are full-range BT.601:** encode with `scale=in_range=pc:in_color_matrix=bt601:out_range=tv:out_color_matrix=bt709,format=yuv420p` plus `-colorspace/-color_primaries/-color_trc bt709 -color_range tv`; the default came out `yuvj420p(pc)` and would shift colours on some players. Check `ffprobe` says `yuv420p(tv, bt709)`.
- **Phone-speaker test for SFX:** procedural hits were 97 % below 150 Hz. Add a 150-500 Hz body and a 1.4-4.2 kHz crack (x2.6 / x2.2) and re-measure 200 Hz-9 kHz RMS 0.15 s after each hit; v6 raised it 3-8 dB (about 12 dB under the voice) - still short of a 6 dB goal, so swap in licensed hits.
- **Sub-frames before t=0** (motion-blur shutter) land outside the person window and rendered a washed, unmasked frame 0: clamp `t = max(t, 1e-4)` at the top of `__seek`, and make frame 0 a designed impact frame (blurred giant "18" mid-slam), not an empty poster.
- **Camera edge exposure:** a pull-back to `s = 1.0` with a positive `y` shows a black bar (12 px at 22.9 s). Clamp `y` to `[1500 (1 - s), 420 (s - 1)]` in `__seek` and never end a pull-back below `s = 1.02`.
- **Map labels:** clamp every pin label >= 30 px inside the card and freeze the wide framing (no lon/z drift) once both end labels are placed; a label offset of +92 px sliced INDIA to "IN" for 3 s. Pull the map back **before** the word so the place is on screen when spoken.
- **Multiplicative grade tints turn brand colours to mud:** a bottom `multiply` tint of .30 made #FFD60A olive (#C9AE1E); keep it <= .13 or move it under the graphics layers.
- **Stage shade must start below the chin** (stops 50 % / 62 %), otherwise the face is 25 % darker in stage beats than in person-mask beats and pops at the switch.
- **Impacts lead the visual by 30-40 ms** (audio-early is invisible) so the transient survives phone speakers; SFX kits are ~70 % sub-150 Hz, so add a mid-band layer to hits when a real library is not available.
- **Mask edges near the end of a clip:** MediaPipe mattes are 540x960 and leave a 9-11 px rim at full-res; erode 1 px, steepen (`clip((a - .35) / .30)`), blur sigma .5, and max-blend with the previous frame only where a motion-blurred limb flickers.
- **Chime/sparkle stacks bury the last word:** on the sign-off keep chime at -19 dB and sparkle at -24 dB under the voiced name.
- Sub-agents share one Browser pane: run text research in parallel with own tabs; screenshots need the pane visible and the tab fronted.

## 7. What worked / what did not
Worked: colour worlds behind the mask as cuts; behind-head giant type; sealed pill → panel morph; odometer locks on syllables; map as a tracking camera with a phone riding the arc; map card 3D flip into the coupon; cream interrupt; two-segment music with vacuum; camera anticipation of 2 frames; supersampled motion blur; six-lens QA.
Did not / rejected: glowing globe (cliché), clip-art plane, pin-drop bounce, filled India polygon, lowercase "blinkit"+bolt lookalike, chat-bubble UI, gold coin rain, starburst badge, red-on-navy countdown, global colour fix that pinked the skin.

## 8. QA workflow outcome (v4 master -> v5) — what six lenses + skeptics found
`qa_workflow.js` ran 38 agents (6 lenses, one skeptic per critical/major finding, ~21 min). 32 heavy findings were skeptic-checked (10 confirmed, 19 partly confirmed with a corrected fix, 3 refuted as nits) plus 45 light ones; a partly-confirmed finding usually kept its problem but not the reviewer's proposed fix, so always read the skeptic's revised fix. Fixed in v5:
| Finding | Fix |
|---|---|
| INDIA pill sliced to "IN" 16.7-19.6 s, USA clipped 18.5+ | fixed symmetric wide framing (lon -6, z .44), INDIA pin dx 0 / DUBAI dx -110, label clamp >= 30 px, pull-back finishes at 16.54 |
| Every stage hid the mouth (3-22 s) | camera settles `y -45`, stages start y 1000, chip moved to the card's bottom strip, coupon 690 tall |
| Price panel half empty 6.3-9.3 s | panel one row tall, grows to 690 at 9.26 s; sealed dots instead of "0,00,000" |
| Frame 0 washed/unmasked | `t = max(t, 1e-4)`, "18" already mid-slam at frame 0 |
| Black bar at top 22.9-23.9 s | pull-back ends at `s 1.02, y -6` + edge clamp |
| DISCOUNT unreadable ("DI...UN"); "min" clipped | front layer, 182 px outlined; "10 min" front layer with yellow halo |
| Odometer overshoot clipped at card edge | size 152, pulse 1.025, row pitch 300 |
| "Mr." slammed 0.5 s early | slam at 24.56 (voiced onset), hard cut of "Thank you", swell moved to 23.66 |
| Coins on lips/numerals | emitter on the tick badge, `ang -1.45`, 7 discs |
| Face pops 107 -> 136 luma at 20.1 s | stage shade starts below the chin |
| Green face flash at 20.2 s | flash .45 -> .22 |
| Countdown "10" shown 0.85 s before it is said | `numAt: 5.14`; a bolt holds the ring meanwhile |
| Invented colourways / "less than" dropped | graphite phones, "UNDER 10 MIN" ticket, "YOU SAVE" coupon |
| Audio: true peak -0.9, chopped tail, thin sibilance | limiter .84 + TP -1.5, 250 ms tail fade, 7.2 kHz dip / softer 2.8 k + 9 k, chime -19 dB |
| Camera "metronome" | rolls kept only on 5.14, 12.44, 15.06, 17.86, 20.20, 21.34 |
| Regression pass (19 agents): stepped map-whip blur, yellow bleed in hair mattes, PRICES arrow aiming at the shirt print, FOR WATCHING on the shirt print, phone-band SFX | 24-sample whip windows, matte temporal-max + smoothstep (0-1.6 s, 4.25-6.2 s), arrow removed, text shadows, SFX mid layer + music-bus EQ |
| Sign-off/edge polish | wordmark 190 px inside the safe area, orbs inside, confetti gone by 25.3 |
Not fixed (documented): the source is 30 fps duplicated to 60 (interpolating the base is a possible upgrade); the SFX kit is procedural (swap via `sfx_cue_sheet.csv`); the "But..." card still holds 0.38 s with an invisible freeze (a design choice).

## 9. Checklist for the next client reel
☐ Number check with two transcripts ☐ Brief written ☐ Pane visible for research ☐ Selective correction + un-mirror ☐ Head-top guard ☐ Camera keys on words (2-frame lead) ☐ ≤ 1 hero per beat ☐ Colour worlds as cuts ☐ Every graphic has a cue ☐ Digit locks on syllables ☐ No polygons of disputed borders ☐ Brand stand-ins only ☐ Music segments fitted + vacuum before the payoff ☐ Master −14 LUFS/−1 dBTP ☐ Stage tops >= y 1000 (mouth visible at every stage beat) ☐ Voice-onset check of the last words ☐ Frame 0 and last frame inspected ☐ QA workflow run, criticals fixed, key frames re-checked ☐ Deliverables + cue sheet + keyframes

## 10. Draft 3 — IKKO MindOne review (SaaS-style product review, 2026-09-30)
Project `experiment/claude4/` (build kit in `build/`, deliverables in `deliver/`). Source: `main Video for mini smartphone .mp4` (33.2 s, Mr. Unbox, already jump-cut at every sentence) + 14 B-roll clips in `brolls for small phone/` (12 vertical 4K 10-bit HEVC at 50 fps, 2 at 1080p 29.97). Brief: senior editor + motion designer, SaaS references as the benchmark (see `my-editing-rules` → product-review brief). Result: 32.73 s, 14 cuts, one colour system, `EDIT_BREAKDOWN.md` holds the full timestamped creative map.
**What worked (reuse):**
- **SaaS on a talking head** = UI objects that each explain one spoken fact. Figma-style **selection boxes** tracked to the phone and palm are the hook ("smaller than my palm"), and return on the top-down size shot. A **diagonal dimension line** tracked corner to corner on the screen gives "4-inch". **Spec pills** land on each word. **AF viewfinder brackets** lock on the camera for "this camera". A **segmented toggle Back → Front** morphs into one pill ("one camera for both"). A **heads-up notification** drops from the top for "global internet" and grows a Wi-Fi row whose toggle turns off while "Connected" stays green. The CTA is a **comment box → follow chip** with a cursor. The name gets a type-on with tracking collapse and a bloom.
- **Accent sampled from the product's own screen** (lock-screen periwinkle #8C9BFF→#B49CFF), green only for success, Geist Sans/Mono (`@fontsource/geist-sans`, `geist-mono`).
- **Music-led bed** (recipe b): the track's own drop placed on the hero spec (Loop 5 offset 10.32 s → drop at 11.40 s on "50MP"). A filtered dip under "but the coolest part" and a 1.25 s riser into the drop. No removals, no ducking.
- **Deepak's every-video HL + MC with no source documents:** the highlight is a brush underline under the product name (dark-UI variant, video accent colour). The match cut pins that highlighted name while eight feature B-roll shots flash behind it for 7 frames each on "this many features" (see `text-highlight-match-cut`).
**Gotchas hit (fix first next time):**
- **zsh does not word-split `$A`.** A patch render run as `node render.js ... $A` from the tool shell passed all paths as one argument, so every patched frame rendered with no footage (mean luma 8–12). This has now happened twice. Always run renders through a bash script (`render_final.sh`, `render_patch.sh`), and check the mean luma of patched frames before encoding.
- **Masks must carry alpha.** MediaPipe masks saved as greyscale `L` PNGs make the CSS mask fully opaque, so the person layer covers everything and behind-head text disappears. Save them as `LA`/RGBA (alpha = matte).
- **Check for baked-in zooms before adding camera keys:** head width per segment from the masks (here 290–325 px everywhere means no zoom keyframes, so punch-ins are safe).
- **Verify the product name on the device**, not from Whisper: "EcoMind One" was printed "ikko / MindOne" on the back (read from a 4K B-roll crop).
- **B-roll:** extract at the native fps and index frames by clip time (`1 + floor(t × fps)`); no fps conversion. Grade each clip with an SVG `feColorMatrix` (`color-interpolation-filters=sRGB`) whose gains are measured against the A-roll wall and face. Any translate on a scaled shot needs `s ≥ 1 + |y|/960` and `s ≥ 1 + |x|/540`, or the frame edge shows (a 60 px shift at s 1.06 exposed 2 px).
- **Tracking without OpenCV:** the phone screen is the largest bright, low-saturation blob; take extreme points for the quad and smooth over 7–9 frames. Derive the palm box from the phone box plus fixed offsets. Hand-key small dark objects (the camera module) at 4–6 times and interpolate.
- **Voice from a CapCut export can be clipped** (2,469 samples over full scale here, boomy +15 dB at 250–1000 Hz): adeclip, −3.5 dB @300 Hz, −2 @550, +3.5 @3 kHz, +3 dB shelf @8.5 kHz, 2:1 compression.
- **UI SFX need about −20 to −10 dBFS cue gains** to be heard on a −14 LUFS master with a voice. The first pass at −25 to −29 made the notification and toggle inaudible (14 dB under speech RMS).
- **Render speed:** full res with 4 sub-frames ≈ 5.7 frames/s with 6 workers (6 min for 33 s); 24-sample windows ≈ 0.8 frames/s.
**Independent senior-editor review (one agent, stills from the delivered file), fixed in v4:**
- **Hook text on frame 1.** Show the whole hook line dim (white at 50 %) from the first frame and light each word as it is spoken. A line that builds from nothing leaves 0.9 s of empty frame, and grey words vanish on a grey wall.
- **Top UI band at y ≥ 236 px** (headlines, eyebrows, notification, CTA). Keep lower UI above y ≈ 1450 and out of x > 960 between y 1150 and 1750 (Instagram's buttons). Stack pills upward from the object instead of downward.
- **Never set a key spoken fact in the smallest type** (the "SONY CAMERA" eyebrow went 29 → 40 px). A descriptor that sits on an object moves, or the B-roll gets reframed (scale 1.14–1.17, y +130–150).
- **A bright shot between dark ones needs ≥ 0.9 s and about ⅔ of a stop down.** At 0.6 s and luma 148 among 45s, the desk shot read as a flash frame.
- **Match cut quality:** 5–7 shots (not 8) of distinct features. Dim the backgrounds 25 % so the white anchor holds. Reframe every shot so the product lands under the anchor (uniform scale 1.25, offsets clamped to the scale margin, 40 px whip). Use a hard-cut exit in premium/SaaS looks; the white corner flash read as a preset.
- **Marker-weight highlight:** a band 0.44 em tall behind the lower half of the letters, in a deeper accent (#4E5FE0 → #8A6CF0) so white text keeps 5:1 contrast. A 0.25 em underline read as an underline, not a highlight.
- **CTA:** put it in the top band, away from the shirt print and Instagram's username row. Use a face crop from the footage as the avatar, spell the brand as printed ("Mr.Unbox"), and park the cursor clear of the label after the click. **End hard for a loop**, with no fade to black.
- **Hair behind white type:** steepen the matte (`clip((a − 0.5) / 0.14)`, blur 0.6 px) for the text-behind-head frames. The soft MediaPipe edge painted a grey fringe onto the letters.
- **Hard cuts vs motion-blur sub-frames:** footage is frame-quantised but graphics and the camera are time-continuous. Any switch placed exactly on a cut frame (camera reframe, element on/off) splits that frame's 4 sub-frames 2/2, giving a one-frame double face or a 50 % ghost (seen at 11.30, 15.60, 23.98 and 27.90 s and on the first match-cut frame). Put every cut-coincident switch at `F/60 − 0.006` (F = first frame of the new shot). Write shot and edit-list boundaries as exact frames (`130 / 60`), never rounded decimals: `2.1667` left frame 130 outside the B-roll shot and flashed the next talking-head take for one frame. QC: average the 4 sub-frames of every cut frame and look for doubles.
