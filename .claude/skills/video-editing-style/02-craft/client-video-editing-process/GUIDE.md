---
name: client-video-editing-process
description: Use for any client edit request, "make this boring video high-engagement", professional motion graphics on a talking head, camera keyframes/zooms/rolls, price/number reveals, map/route beats, SaaS-style product reviews, or when reusing the Mr. Unbox build kit. End-to-end pipeline (analysis, selective colour correction, research panel, HTML/GSAP kit, SFX/music, supersampled render, six-lens QA) from the Mr. Unbox iPhone 18 Pro edit plus draft 3 (IKKO MindOne review).
---

# Client reel — professional motion-graphics pipeline

Draft 2 = Mr. Unbox iPhone 18 Pro (25.4 s, English, 1440x2560@60; prices via Blinkit, Dubai/USA tip). Reusable code: `edited videos by claude/2. Mr Unbox iPhone 18 Pro/code/` (`experiment/` paths are historical). Supersedes tooling in `reel-editing-method`. Look/feel: `motion-graphics-style`, `my-editing-rules` (latest Deepak instruction wins).

## 0. Rules learned (read first)
- Client clips have no keyframes, so give them a full camera language (punch-ins on words, 2-5 deg rolls, pushes, a freeze-frame hit). Deepak's own CapCut exports already carry keyframes: never add more.
- Use the client's name/sign-off (Mr. Unbox); never leak Tech Boy Deepak branding; never invent a social handle.
- Fact discipline: on-screen facts = only what is spoken. No invented prices/specs/dates; paraphrase must not create a new claim. Where he points at material we lack, leave a labelled pointer, never fabricate data.
- Maps: never draw/fill polygons of India or any disputed region; use land silhouette (no internal borders) + soft glow regions + nodes/labels.
- Third-party marks: typographic stand-ins only (uppercase "BLINKIT" on plain yellow pill; generic phone, no Apple logo). Lowercase logo lookalikes rejected.
- Deliver honestly: procedural SFX are placeholders; ship the cue sheet for swaps from Mixkit/Freesound/Pixabay (user decision 2026-11-14).
- Stages must clear the mouth: any lower-third stage (price panel, map card, coupon, ticket, countdown, chips) starts at y >= 1000 with camera lifted (y -45, s >= 1.045 on every settle). Nothing straddles the lips; test at every stage beat. (v4 hid his mouth ~60% of runtime with stages at y 900.)
- Whisper word times can be 0.5 s wrong at clip end ("Mr." stamped 24.08, voiced 24.57): verify hero-word onsets with a 20 ms RMS envelope of the voice stem.
- Never show a fake zero: hold price odometer with sealed dots, reveal digits at tOdo0 - 0.1.
- Don't invent product facts in illustrations (neutral graphite phones, keep "UNDER" on the ticket, no series numbers, no unspoken labels).
- Wide words cannot sit behind a head (900 px word showed "DI...UN"): behind-head type short (18 / PRO) or above hair; wide words (DISCOUNT, "10 min") go in the front layer as outlined type (WebkitTextStroke + paintOrder stroke fill).
- Ask the user to open the Browser pane before screenshot research; text-only research is much weaker.

## 1. Pipeline
1. **Analyse** (10 min): ffprobe; 0.5 s contact sheets; silencedetect for jump cuts; faster-whisper large-v3 language="en" word timestamps; verify every number with a second pass (small model + beam/prompt variants). Measure colour (wall/face RGB, luma percentiles), audio (LUFS, true peak, clipped samples, spectrum), head position per frame from masks.
2. **Write `BRIEF.md`**: client request verbatim, footage facts, transcript table, fact discipline, stack, quality bar.
3. **Research + concepts + judging = one Workflow:** 4 parallel researcher agents (one per site: Behance/Dribbble/LottieFiles/Pinterest, own browser tab), 3 concept agents (typography-led / product+depth / quick-commerce pop), 3 judges (retention, craft, feasibility+facts). Winner is always a synthesis, never one concept or a copied reference. ~45 min, run in background.
4. **Foundations while panel runs:** selective colour correction + un-mirror + head-top table; SFX kit; mix script; camera/typography/component kit; renderer.
5. **Build scenes** beat by beat from word timestamps; check each at 0.5 scale (`render.js --times`), then a full low-res pass.
6. **Final render** with 4x temporal supersampling, mix, encode.
7. **QA workflow** (`qa_workflow.js`): six lenses (typography, sync, footage/grade, engagement, facts, audio) -> adversarial verifier per critical/major finding -> fix -> re-render.
8. **Deliver:** master + upload MP4, stems, cue sheet, CapCut keyframe table, reference board, breakdown, source.

## 2. Footage correction (selective, mask-based)
- Wall had a mint cast (118,141,128); a global fix pushed skin magenta. Correct subject and background separately with the per-frame person mask (MediaPipe selfie model 0, 540x960).
- Subject: gamma 0.94, +5% saturation (hue-preserving), +5% contrast. Background: gains R 1.035 / G 0.955 / B 1.015, saturation 0.78, brightness 0.93, contrast 1.04. Mask edge = MaxFilter(5) + Gaussian 3 + bilinear upscale. Skin stays R>G>B.
- Un-mirror selfie footage (flip frames AND masks).
- Headroom guard in `runtime.js`: measured head top 134-214 px; after any camera transform keep >= 84 px above hair.
- In-browser grade: contrast(1.12) saturate(1.0) brightness(.95), cool top/bottom multiply tint (<= .13 or brand yellow turns olive), warm top screen light, vignette, per-frame grain.

## 3. Design system
Tokens: ink #08090B, off-white #F5F5F2, cream #EFE9DD; yellow #FFD60A = speed/price/delivery; cyan #6EE7DF = brand/route/Pro Max; green #3DDC84 = savings only. Type: Bricolage Grotesque 800 (numbers/display, -0.035 em), Instrument Serif italic, Inter (UI), JetBrains Mono (labels >= 30 px, tracked). Min text 30 px, min stroke 4 px, safe area x 60-1020 / y 120-1700, one hero per beat, every graphic has a sound, blur-in entrances, exits faster, no glitch/RGB split, no starburst badges, no coin rain.
Colour worlds behind him (via person mask) are the cuts: yellow opener (0-1.3 s) -> room + dark stage -> yellow delivery world (4.28-5.92) -> dark price stage -> cream "But..." interrupt (0.38 s, 5-frame freeze) -> dark map stage -> green savings world (20.2-22.6).

## 4. Beat structure (25 s)
Hook (giant type behind head + push-out) -> model names (phones + MAX sticker) -> brand stand-in ticket -> countdown (stepped ring, drawn check) -> sealed-price pill from frame 0 morphing into price panel -> two prices (odometers with digit locks on syllables + glint) -> cream "But..." -> kinetic "what I SUGGEST" -> map (Gulf -> whip west -> wide -> phone rides arc, "bring one" on arc -> macro push) -> map card 3D-flips into coupon -> discount word behind head -> "prices" pointer -> sign-off ("Thank you" serif -> "Mr. Unbox" lockup + orbs). Music: two beat-aligned segments joined inside the "But..." silence; 0.3 s vacuum before the discount hit.

## 5. Build kit (`.../code/`)
- `index.html`/`runtime.js`: layers (bg, base, bg2, behind, person, world, front, hud, fx), fontsource fonts, `__seek(t, frame)`, camera transform + head guard + micro-drift.
- `core.js`: GSAP master timeline, `sfx()`, `musicKey()`, camera keyframe track (`camKey/camMove/camPunch`, punches anticipate the word by 2 frames), shakes, freeze holds, `personOn()`, blurIn/pop/slam/whipX/chars/maskLine/typewriter.
- `components.js`: `phoneBack`, `odometer` (Indian grouping, per-digit locks), `countdownFlip`, `ticket`, `glass`, `makeFlatMap` (tracking camera, nodes, routes + comet head, text on route), `burst`, `speedLines`, `makeGlobe` (rejected as cliche).
- `scenes.js` (the edit), `render.js` (`--sub 4 --shutter 0.5`; ffmpeg `tmix=frames=4,select='eq(mod(n\,4)\,3)'`; `--sfxout`), `sfx_synth_v2.py` (58 sounds), `mix2.py` (voice: adeclip, 72 Hz HPF, -3.2 dB@420, +3.4@2.8k, -3@5.4k, air shelf, 2.4:1 comp -> -16 LUFS; two-segment music with low-pass automation + ducking; master -14 LUFS / -1 dBTP), `export_cues.js`, `make_docs.py`, `audit_scenes.py`, `splice_windows.py`, `render_final.sh`, `qa_workflow.js`.

## 6. Gotchas
- GSAP skips zero-time sets at exact-0 seek: seek `max(t, 1e-4)`; make frame 0 a designed impact frame (blurred giant "18" mid-slam), not an empty poster.
- Half-scale previews: `clip.scale`, not deviceScaleFactor. One Chrome per worker. ~4-5 fps x4 sub-frames with 5 workers (~7 min for 25 s).
- Fonts: fontsource CSS (unicode-range) or the rupee sign falls back; `document.fonts.load(..., '₹')`.
- Pill -> panel geometry morph with overflow:hidden; keep decor in a container faded in after.
- Text-on-path and phone icons drawn in screen space (constant size).
- **Comments swallowing code:** `// ... ; next()` on one line (happened twice; a MAX sticker stayed 22 s). Put comments at line end, run `audit_scenes.py scenes.js <backup>` after every patch, and look at frames of the final MP4 at 10+ times. `node --check` cannot catch it.
- Reversed swells/risers climax at their end: start them `duration` earlier.
- Music beat-fit: score beat-grid alignment of key hit times per segment (Tech beat: seg 1 offset 0.908 s, seg 2 offset 3.56 s, join 12.26 s).
- Fast map moves need more shutter samples: re-render only fast windows (whip 14.75-15.32, pull-back 15.95-16.58, macro push + flip 19.42-19.96, card entry 13.98-14.25) with `--sub 24 --shutter 0.5`, average groups of 6 into 4 sub-frames (`splice.py`).
- JPEG frames are full-range BT.601: encode with `scale=in_range=pc:in_color_matrix=bt601:out_range=tv:out_color_matrix=bt709,format=yuv420p` + bt709/tv tags; verify ffprobe says `yuv420p(tv, bt709)`.
- Phone-speaker test: procedural hits were 97% below 150 Hz. Add 150-500 Hz body and 1.4-4.2 kHz crack (x2.6/x2.2); re-measure 200 Hz-9 kHz RMS 0.15 s after each hit (raised 3-8 dB, still short of the 6 dB goal: swap licensed hits). Impacts lead visual by 30-40 ms.
- Camera edge exposure: clamp y to [1500(1-s), 420(s-1)]; never end a pull-back below s = 1.02.
- Map labels: clamp pin labels >= 30 px inside card; freeze wide framing once both end labels placed (a +92 px offset sliced INDIA to "IN"); pull back before the word.
- Stage shade starts below the chin (stops 50%/62%) or the face is 25% darker in stage beats and pops at the switch.
- Mask edges near clip end: 9-11 px rim; erode 1 px, steepen `clip((a-.35)/.30)`, blur sigma .5, max-blend with previous frame only where limbs flicker.
- Chime -19 dB and sparkle -24 dB under the voiced name on the sign-off. Sub-agents share one Browser pane: parallel text research with own tabs; screenshots need the pane visible and tab fronted.

## 7. What worked / rejected
Worked: colour worlds behind mask as cuts; behind-head type; pill -> panel morph; odometer locks; map as tracking camera; 3D card flip; cream interrupt; two-segment music with vacuum; 2-frame camera anticipation; supersampled blur; six-lens QA.
Rejected: glowing globe, clip-art plane, pin-drop bounce, filled India polygon, lowercase "blinkit"+bolt, chat-bubble UI, gold coin rain, starburst badge, red-on-navy countdown, global colour fix that pinked skin.

## 8. QA outcome (v4 -> v5)
38 agents, ~21 min: 32 heavy findings skeptic-checked (10 confirmed, 19 partly confirmed with a corrected fix, 3 refuted) + 45 light. Always read the skeptic's revised fix. Fixes: symmetric wide map framing (lon -6, z .44), labels clamp; stages start y 1000, coupon 690 tall; price panel one row tall growing to 690 at 9.26 s; `t = max(t,1e-4)`; pull-back ends s 1.02 y -6 + edge clamp; DISCOUNT front layer 182 px outlined; odometer size 152, pulse 1.025, row pitch 300; "Mr." slam at 24.56; coins from tick badge, 7 discs; stage shade below chin; green flash .45 -> .22; countdown `numAt: 5.14`; graphite phones, "UNDER 10 MIN", "YOU SAVE"; audio limiter .84 + TP -1.5, 250 ms tail fade, 7.2 kHz dip, softer 2.8k/9k; camera rolls kept only at 5.14, 12.44, 15.06, 17.86, 20.20, 21.34; regression pass (stepped whip blur -> 24-sample windows, matte temporal-max + smoothstep, PRICES arrow removed, text shadows, SFX mid layer); wordmark 190 px inside safe area.
Not fixed: source is 30 fps duplicated to 60 (interpolation possible); procedural SFX; "But..." card holds 0.38 s with invisible freeze.

## 9. Checklist
Number check with two transcripts / Brief written / Pane visible for research / Selective correction + un-mirror / Head-top guard / Camera keys on words (2-frame lead) / <= 1 hero per beat / Colour worlds as cuts / Every graphic has a cue / Digit locks on syllables / No disputed-border polygons / Brand stand-ins only / Music fitted + vacuum before payoff / Master -14 LUFS / -1 dBTP / Stage tops >= y 1000 / Voice-onset check of last words / Frame 0 and last frame inspected / QA workflow run, criticals fixed, key frames re-checked / Deliverables + cue sheet + keyframes.

## 10. Draft 3 — IKKO MindOne review (SaaS-style, 32.73 s, 14 cuts)
Source: Mr. Unbox 33.2 s already jump-cut per sentence + 14 B-roll clips (12 vertical 4K 10-bit HEVC 50 fps, 2 at 1080p 29.97). `EDIT_BREAKDOWN.md` holds the timestamped map.
**Reuse:**
- SaaS on talking head = UI objects each explaining one spoken fact: Figma-style selection boxes tracked to phone and palm (hook, return on top-down size shot); diagonal dimension line corner to corner ("4-inch"); spec pills landing on each word; AF viewfinder brackets on the camera; segmented toggle Back -> Front morphing to one pill; heads-up notification dropping from top and growing a Wi-Fi row (toggle off, "Connected" green); CTA comment box -> follow chip with cursor; name type-on with tracking collapse and bloom.
- Accent sampled from the product's own screen (periwinkle #8C9BFF -> #B49CFF), green only for success, Geist Sans/Mono.
- Music-led bed: track's drop on the hero spec (Loop 5 offset 10.32 s, drop 11.40 s on "50MP"); filtered dip under "but the coolest part", 1.25 s riser into drop; no removals, no ducking.
- Every-video HL + MC with no source docs: brush underline under the product name; match cut pins the name while 5-7 feature B-roll shots flash behind it (see `text-highlight-match-cut`).
**Gotchas (fix first next time):**
- **zsh does not word-split `$A`:** a patch render with `node render.js ... $A` rendered no footage (luma 8-12); happened twice. Run renders via a bash script and check mean luma of patched frames before encoding.
- **Masks must carry alpha:** greyscale `L` PNGs make the person layer fully opaque and hide behind-head text; save LA/RGBA.
- Check for baked-in zooms before adding camera keys (head width per segment from masks; 290-325 px everywhere = none).
- Verify the product name on the device (4K B-roll crop), not Whisper ("EcoMind One" printed "ikko / MindOne").
- B-roll: extract at native fps, index `1 + floor(t*fps)`, no conversion; grade each clip with SVG feColorMatrix (sRGB) gains measured against A-roll wall and face; any translate on a scaled shot needs s >= 1 + |y|/960 and s >= 1 + |x|/540.
- Tracking without OpenCV: phone screen = largest bright low-saturation blob, extreme points for quad, smooth over 7-9 frames; palm box from phone box + fixed offsets; hand-key small dark objects at 4-6 times.
- CapCut voice may be clipped (2,469 samples): adeclip, -3.5 dB@300, -2@550, +3.5@3k, +3 shelf@8.5k, 2:1 comp.
- UI SFX need about -20 to -10 dBFS cue gains on a -14 LUFS master (-25 to -29 was inaudible).
- Render: 4 sub-frames full res ~5.7 fps with 6 workers (6 min for 33 s); 24-sample windows ~0.8 fps.
**Senior-editor review fixes (v4):**
- Hook text on frame 1: whole hook line dim (white 50%) from first frame, light each word as spoken.
- Top UI band at y >= 236 px; lower UI above y ~1450 and out of x > 960 for y 1150-1750 (Instagram buttons); stack pills upward from the object.
- Never set a key spoken fact in the smallest type (eyebrow 29 -> 40 px); reframe B-roll (scale 1.14-1.17, y +130-150) if a descriptor sits on an object.
- A bright shot between dark ones needs >= 0.9 s and ~2/3 stop down.
- Match cut: 5-7 distinct shots, backgrounds dimmed 25%, product reframed under the anchor (scale 1.25, offsets clamped, 40 px whip), hard-cut exit (white corner flash read as a preset).
- Marker highlight: band 0.44 em tall behind lower half of letters, deeper accent (#4E5FE0 -> #8A6CF0) keeping 5:1 contrast; a 0.25 em underline reads as underline.
- CTA in the top band away from shirt print and IG username row; face-crop avatar; spell brand as printed ("Mr.Unbox"); park cursor clear after click; end hard for loop, no fade to black.
- Hair behind white type: steepen matte `clip((a-0.5)/0.14)`, blur 0.6 px.
- **Hard cuts vs sub-frames:** any switch exactly on a cut frame splits its 4 sub-frames 2/2 (double face/ghost at 11.30, 15.60, 23.98, 27.90 s). Put every cut-coincident switch at `F/60 - 0.006`. Write boundaries as exact frames (`130/60`), never rounded decimals (2.1667 flashed the next take). QC: average the 4 sub-frames of every cut frame and look for doubles.


Full original notes (every detail, uncut): `_archive/original-full/client-video-editing-process.md` in this folder.
