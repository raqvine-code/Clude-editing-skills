# Learning log: shorts-editing-pro

**When to update.** Append one entry after EVERY short edit, newest first, and again when Deepak gives feedback on it.
**Format.**
- Date · video · what was made.
- What was new.
- What went wrong and the fix.
- Feedback (quoted).
- Rule changes, which also go into GUIDE.md or the reference file.

**Promotion.** A lesson seen twice becomes a rule in `GUIDE.md`. A rejection also goes into `mistakes-to-avoid` via `skill-saver`.

---

## 2026-11-28 (cloud session) · "GTA 6: why it took 13 years" v2 · the owner's 9 changes
- **Feedback (quoted):**
  1. "Remove starting frame and keep my face"
  2. "Remove tanglish captions entire video"
  3. "Remove (why) word in that frame"
  4. "Remove top sentences entire video"
  5. "Remove time symbol, I dont like that may be add good one"
  6. "At 34 sec remove frame"
  7. "At 41 sec remove that frame"
  8. "At 46 sec that letter (13 years of development keep small and add that lines on the words properly its not straight"
  9. "At 50 sec remove that frame"
- **Done:**
  - face from the first frame, with a punch-in on "GTA 6";
  - no captions;
  - no handwritten "why?";
  - no top label or kicker (the frame lines stay);
  - a flip calendar (real dates peel, NOV 19 2026 circled) instead of the clock;
  - his face at 34, 41 and 50 s;
  - "13 YEARS of development" at 118 / 72 px, with straight strikes measured from each line's text box;
  - the removed graphics' sounds taken out;
  - gentle 5 % punch-ins on stressed words in the face scenes.
- **Numbers:**
  - 82 cues from 62 real files, 0 masking the voice;
  - −14.0 LUFS, −1.5 dBTP;
  - earshot sync 77 % (target 78 %: the new punch-ins have no sound, on purpose);
  - gate NOT READY with 4 FAILs, all from the owner's choices: font families (approved), no match cut (it lived in the 34 s frame), the longest stretch without a graphic 10.0 s (the 41 s frame), event gaps (captions removed).
- **Lesson:** this owner wants his face and a few strong designed beats, not data-heavy full-screen cards, running captions, kickers or doodles. Saved in P21 GUIDE section 6c.

## 2026-11-27 (cloud session) · "GTA 6: why it took 13 years" (owner's own Telugu facts video), 57.7 s · delivered
- **Brief (quoted):** "combine all 6 clips in the correct order ... DO NOT START EDITING IMMEDIATELY ... frames and references for each scene ... GTA 6 gameplay B-rolls, research-evidence B-rolls, motion graphics ... No background music ... No colour grading." The owner approved the storyboard and chose **"framed window opt B"** and **"Tinglish opt B"**.
- **Built with:**
  - style P21 (vice-neon titles) plus motion-graphics-craft M2 (numbers and counters drive the motion), and the browser compositor;
  - 21 scenes, with one governing idea: GTA V's sales line never fell, so GTA VI's clock kept running;
  - B-roll: official Rockstar media (animated cover, character clips, 4K screenshots and artwork, GTA V images) and evidence cards from Guinness, PC Gamer, Outlook Respawn, Game Informer and Engadget.
- **What went wrong and the fix:**
  1. The concat-copy join drifted the voice 0.27 s by the last clip. Joined again with the concat filter, each clip's audio trimmed to its own picture.
  2. Whisper on the whole Telugu file looped. Transcribed per clip, with a vocabulary prompt for unclear spots; the meaning-critical word "pattaledu" was checked on three crops.
  3. YouTube refused downloads from the cloud server. Not bypassed: official Rockstar media instead, and the owner was offered trailer files as an option.
  4. Earshot sync started at 68 %. Hits had silence before the attack and sat 8-11 dB under continuous speech. Fixed by placing hits on their loudest point, adding a short real attack on every cut at about −10 dB under the voice, and lowering the two cues that masked "Kaani". Sync rose to 78 %.
  5. Frame extraction by seeking was slow. Read sequentially instead: 3462 frames in 20 s.
- **Numbers:**
  - 3462 frames at 60 fps, rendered in 7.3 min;
  - 104 cues from 71 real files, at most 3 uses each, none masking the voice;
  - −14.0 LUFS, −1.4 dBTP; picture and audio sync 0 frames / 0.000 s against the master;
  - earshot 20 of 23 in range: music is excluded by the owner's rule, density 4.4 onsets/s against 4.7 in music-backed references, low end thin (minor);
  - gate: one FAIL (3 font families), approved by the owner on the storyboard.
- **Rule changes:** P21 GUIDE section 10 (layout B and caption band, official media first, the earshot lesson), CHANGELOG entry.

## 2026-11-27 (cloud session) · "The story you tell yourself" v4, 45.0 s · three fixes after the owner's notes on v3
- **Feedback (quoted):** "1. Every cursue caption or letters is cut the edges once you see and fix it . 2.At 39 sec the frame is move fast like it doesn't sync the voice check the once and fix it sync the voice 3.Add some proper motion graphics make sure don't add messy type of random graphics" (screenshots at 0:08 "luck frame", 0:32 "seeing", 0:39 the two bubbles).
- **What went wrong 1, script letters cut:** the write-on mask (a moving gradient) stopped at 110 % of the word box, so the last tenth of every script word stayed half transparent ("frame" lost its "e"), and Great Vibes swashes, tails and capitals overhang the glyph box, so the masked box cut them off ("seeing" lost the tail of its "g"). **Fix:** the mask runs to 124 % and is removed (`mask: none`) the frame the word is complete; script spans get padding `.22em .36em .34em` with equal negative margins, so the mask box covers the overhang without moving the layout.
- **What went wrong 2, 0:39 out of sync:** the right speech bubble played his footage from another moment, so a second mouth moved to words that were not being said. **Fix:** the second bubble is a still, closed-mouth "listening" frame (source 8.98 s) with a 5 % push; measured frame-to-frame change in that window is 1.3 (still).
- **What went wrong 3, more MG:** three overlays tied to one word each, drawn above the captions: a glass lens slides over "the facts of my life" and magnifies each word as it passes; a gold pen nib rides the write-on edge of "self-narrative"; an amber stroke draws under "only", reaches under "way" and lands its arrowhead 0.12 s after "way", then leaves with the caption. First arrow version started on "way" and its head landed during the caption exit (a flicker); caught on a frame sequence and fixed before delivery.
- **Numbers:** 85 cues + room-tone bed, 66 real files, at most 2 uses; gate READY (designed MG 49 %, longest gap 7.6 s); -14.0 LUFS, -1.5 dBTP; earshot 19 of 23 in range, the only critical flag is music (client rule: no BGM); 3 of 43 visual events have no matched onset (two soft cut whooshes, one gesture foley).
- **Rule changes:** `04-styles/editor-showcase-caption-edit-style/GUIDE.md` section 11 (three QC checks), CLIENT-BAR row.

## 2026-11-27 (cloud session) · "The story you tell yourself" v3, 45.0 s · delivered, superseded by v4
- **Process:** master brief (R7 > R6 > R5 > R8, R8 fonts, no BGM, no grade, keep B-roll) -> fonts matched to R8 -> light trim (2.6 s) -> four preview boards -> owner approved, rejected panels 3, 13, 16 -> three redesigns + motion upgrades -> render -> gate READY -> earshot 19 of 23 in range (only music flagged, excluded by the client rule).
- **New tools:** the browser compositor (`04-styles/editor-showcase-caption-edit-style/references/worked-example-v4/`), `audio.py` (real sounds by role, least-used first, at most 3 uses), earshot critique against the showcase profile.
- **Numbers:** 1351 frames rendered in about 2 min; 82 sound cues from 66 real files; -14.0 LUFS, -1.3 dBTP; caption centre at chin + 17 %; footage colour within about 2 levels of the source.
- **What went wrong and the fix:** the camera-app card, the dark highlight card and the phone share sheet read as templates (owner rejected them): use cinematic, footage-based designs. Soft cloth sounds on hidden cuts did not register as onsets: use a short airy whoosh with its peak on the cut.
- **Feedback:** pending.

---

## 2026-11-27 (cloud session) · "The story you tell yourself" REDO, 47.6 s English talking head · delivered, feedback pending
- **What was made:** the same four clips, rebuilt to the gate: P19 under-chin captions as the base, P17 object cards as inserts. 9 card layers (hook card, good-things B-roll card, luck frame, FACTS -> FRAMES inversion, 1-2-3 tiles, PATTERNS match cut, HL quote card, mirror, CTA card = the hook card again), 6 literal B-roll clips, 71 sound cues, no music, no grade. Worked example: `04-styles/editor-showcase-caption-edit-style/references/worked-example/`.
- **Numbers (gate READY, QC):** 13 designed MG events, 47 % of runtime, longest stretch 8.4 s, HL + MC, 29 caption groups, caption block centre 61 % of the height (chin + 17 %), nothing above the head, colour within 1.5 levels of the source (no grade), -14.0 LUFS, true peak -1.5 dBTP, 1428 frames.
- **What was new:** the six card kinds in `caption_moves.py`; camera face-follow (`anchor_track`); B-roll `dy`; focus pull as a `dims` entry; gate counts only object layers as MG.
- **What went wrong and the fix:** (1) `anchor_track` crashed the multi-frame render (numpy array used with `or`; stills had hidden it): always run a short `video --from --to` render, not only stills, after a kit change. (2) The sunset clip showed only sky inside the card window: use `dy` + `z`. (3) Hero text stayed on the footage while a card opened: it now fades during `release`. (4) Tiles collided with the hero line: tiles at y 1388, size 84. (5) The `neg` flash leaves one black frame (kit design).
- **Time:** 1428 frames at 1080x1920 took about 17 min on 4 cores; layers about 5 min; do the layer render in the background while writing the sheets.
- **Feedback (2026-11-27):** "Then why you edited the previous video? Because I don't like that video. The caption, typographies, subtitles, even fonts also. Also, do not add proper SFX. Also, every frames you did like same pattern using. I don't like that also. So improve your editing skill. Already I provided zip file... if you have any doubt, ask me now. Also, before you will do video editing, give me the frames and your plan."
- **Why it failed (measured on the redo's EDL):** 6 cards on one layout; 29 captions at one height, 17 of them the same "small grey words + one gold CAPS word"; faint, half-transparent small words and ghosted future words; 71 sound cues from 18 files (one pop 16 times, many synthesised, none heard by me). The ZIP's numbers were used, its variety was not.
- **Rule changes:** (1) NEW PROCESS RULE: after a rejection, or when the owner asks, show the plan AND storyboard frames (stills on the real footage, one per distinct layout) and wait for approval before any full render. (2) Variety rules, `editor-showcase-caption-edit-style` 10b. (3) Gate rows for sound variety.
- **Open:** the owner will give the client rules for this video; real recordings only (Mixkit) were asked for, but Mixkit's category pages now return a Cloudflare bot check from this container, so only IDs already known can be downloaded; no music, no grade.

---

## 2026-11-26 (cloud session) · "The story you tell yourself", 47 s English talking head · REJECTED
- **What was made:** four consecutive clips joined into one 9:16 short with stock B-roll, kinetic titles, music, sound effects and a grade. It was built in a cloud session WITHOUT this rulebook (the zip arrived a day later).
- **What went wrong:** music and a colour grade were added (this speaker's set looks like the Naveen bro English shorts, where the latest word is no BGM and no grade: confirm the client with the owner); titles and captions sat above the head; inserts were stock clips and text on footage; no designed motion graphics, no HL, no MC; no gate, no PRE-EDIT sheet.
- **Feedback:** "I dont like this edit, you need to learnt so much edits".
- **Fix for the redo:** Full mode. Client bar first, gate floors, P19 caption base on the chest (chin + 17 %), object cards and tiles from `04-styles/editor-showcase-caption-edit-style`, focus-pull returns, a sound on every insert, no music and no grade unless the owner says otherwise.
- **Rule changes:** none new; the rules that would have prevented it already existed (Rule 0, client bar). The lesson is to load the client and pass the gate even in a cloud session.

---

## Seed: lessons from shorts delivered before this skill existed

### 18. Go All In · 2026-11-17 · 16.4 s, Tharun grammar + external 4K B-roll
- **New:**
  - Liquid-fill type: hollow at 0 % → 30 % → 100 % across the video.
  - Open-loop dive: a freeze in the hook, the splash at the payoff.
  - Light-rise on the turning word.
- **Lessons:**
  - Check that the raw still exists before reusing an old analysis. NCC maps keeps onto a moved file.
  - Freeze only on a whole source frame.
  - One level map per B-roll clip.
  - Measure SFX vs the voice per word (4 of 28 cues collided).
  - Lean was enough: no subagents, one search, a one-page plan.
- **Feedback:** none recorded yet.

### 17. Embarrassment Short · 2026-11-16 · tes2
- **Lessons:**
  - Keep the Mac awake for long builds; 4.8 h were lost to sleep.
  - A 12-agent plan was too heavy.
  - "Brighter" needs a light pass that actually fires.
  - Text behind a subject fails when the subject fills the centre.
  - Lay out stacks by ink metrics.
  - Slams overshoot safe zones on frame 1.
  - Measure contrast over bright B-roll.

### 16. Uncertainty Short · 2026-11-15 · 1115
- **Lessons:**
  - ASR onsets up to 0.31 s off: verify on the envelope.
  - 24p-in-60 pulldown.
  - Measure the face before setting levels.
  - Baked vignette and grain plus page overlays double up.
- **Feedback:** "looks like not that much pretty". It needs proper B-roll, SFX and motion graphics from external sources, and to be "attractive as much as possible".
- **Diagnosis:**
  - A third of the frames were flat ink cards.
  - Muddy olive face grade.
  - Small captions.
  - 720p B-roll.

### Standing rules distilled from these
- External 1440p+ B-roll and designed MG with depth; no flat black cards.
- A bright, punchy grade on the face.
- Big designed captions.
- Low credits: direct build, small kit, no fan-out (2026-11-17, Deepak: "use low credits as possible").

---

## Edits made with this skill

### 19. Self Story · 2026-11-17 · 35.8 s, Tharun grammar + Mixkit B-roll · first edit with this skill
- **Made:**
  - A 48.4 s raw cut to the voice: 4 lines removed (ramble, stumble, repeat, fragment) and pauses trimmed to 0.2 s.
  - Camera: hook push, a size change at every cut, 4 zoom punches.
  - Grade: coral accent; Tactic Sans normal for captions, Extended for giant words.
  - Graphics: word-pop captions with big coral keywords; STORY and FACTS→FRAMES behind the head; viewfinder brackets on "luck frame"; mirror split on "talking to yourself".
  - B-roll: 7 Mixkit clips. Sound: 24 SFX. Masters -14.2 LUFS / -1.4 dBFS, with and without music.
- **New:**
  - `tools/shortkit.py` replaced the browser kit. The stills check took about 1 min, the full render about 7 min, and the whole edit about 1.5 h, including writing the skill.
  - Mixkit search works with curl (Pexels returns 403).
- **Went wrong → fix:**
  - Giant words floated above the head: y 470, not 360.
  - Two B-roll in-points were bad (a back, a white frame): check a 1 fps strip first.
  - Words from removed lines leaked into the captions: snap only inside the planned keeps.
  - Stutter "again, we | we": cut at the envelope dip.
  - scipy can't read MP3: shortkit decodes it.
- **Feedback:** pending.
- **Rule changes:** none yet (the lessons above go into GUIDE.md if they repeat).

## 2026-11-17 - training batch (no edit): Edit-Kit + 4 reference reels
- **Learned:** `edit-kit-playbook` (distilled from 40 vendored kit skills in `07-edit-kit-reference/`) and profiles P6-P9 in `pro-video-editing`.
- **Apply on every short from now:** speech-to-visual map (lists -> chips, numbers -> counters, "not X" -> strike), caption model drop/rail/embed with ONE behind-subject hero per beat, cue SFX on the impact frame, keyframe every 1 s on the final file, safe zone x 150-930 / y 210-1530.
- **Standing instruction (user, 2026-11-17):** every attached video is edited with ALL trained skills; until new training arrives these skills are the standard.
- **Tool fix:** shortkit's default ffmpeg path was gone; it now falls back to PATH / Homebrew / imageio_ffmpeg.
- **Feedback:** pending.

## 2026-11-20 - training batch (no edit): 2 reference shorts -> P10, P11
- **Learned:** P10 amber UI educator (Uzbek "3 mistakes" reel, 29.3 s) and P11 podcast scene inserts (English guest clip, 34.5 s). Both studied whole with `pro-video-editing/tools/learnkit` (strips, stills, OCR, face, stereo audio).
- **Apply on every short from now:**
  - Choose the caption model on purpose: heavy word-pop (Tharun grammar) for energetic advice, or the light chest-level model (one word, or lead-in + keyword) for premium, calm or podcast clips.
  - Mark the 5-7 most quotable lines in the PLAN and give each a designed scene with the words placed inside the scene; caption the rest lightly.
  - A take longer than 2.5 s is fine if the background behind the speaker animates (person matte) or a new graphic arrives every second.
  - Take the palette from the speaker's clothes or room; red only for negatives.
  - Try one transition themed to the topic per video (paint wipe, typed bar, page turn) instead of a stock whoosh.
  - Put scene-change hits on the cuts into designed scenes; leave caption pops silent.
- **Measured reference numbers:** P10 18.5 cuts/min, text on 77% of frames, 177 wpm, -14.1 LUFS. P11 34.9 cuts/min, text on 90% of frames, 60% of words captioned, 226 wpm, -14.3 LUFS.
- **Not tested yet:** shortkit.py has not built a typed-UI scene, a background takeover or an in-scene text insert. First edit that uses P10/P11 must check what the kit can do and log it here.
- **Feedback:** pending.

### 20. Speed Game (telugu 2 video) · 2026-11-21 · 83.3 s, Tharun grammar + designed scene inserts · first Telugu short with this skill
- **Made:**
  - His rough cut kept whole (27 jump cuts confirmed by frame difference plus head jump); only the tail silence was trimmed. Project `edits/telugu2/`.
  - Grade from a flat, dark raw (face luma 100 to 142-151, frame mean 77 to about 90). Signal yellow `#FFD21F` accent; Inter Tight 800/900 captions with Anton giants (new pair).
  - 43 word-pop caption groups (121 of about 220 spoken words), giants behind the head on STOCK MARKET, INVESTOR, DATA to ACCESS, RISK, LOOPHOLES; a size change on every cut plus 8 added inside the long takes; 4 snap zooms.
  - 8 designed scene inserts (27.0 s, 32% of runtime): one dark-green "signal map" (Chicago to New York) that gains one thing per visit: route, price gap, $300 million cable, 5 ms pulse, Algorithm BUY then SELL, masts.
  - 42 SFX from the tes2 Mixkit set, no music. Final: 1080x1920, 60 fps, 17 Mbps, keyframe every 1 s, -14.2 LUFS, peak -1.4 dBFS.
- **New (first use of the 2026-11-20 lessons):**
  - **In-scene text inserts work** as pre-rendered clips: `edits/telugu2/tools/scenes.py` (PIL + cv2, one `draw(ev, t)` function driven by word-timed events in `scenes.json`) writes MP4s, and shortkit plays them as B-roll slots with `entry: blurzoom, shade: false`. No kit change needed. Put a version suffix in the slot key whenever a scene changes, because shortkit caches prepped slots by key.
  - **Typed-UI scene and background takeover: not built.** The takeover (a shape growing on the wall behind the speaker) conflicts with `mistakes-to-avoid` A1, so it should stay out unless the user asks. A typed bar was not needed for this topic. Both remain untested in shortkit.
  - The light chest caption model (P10/P11) was rejected on purpose: a busy checked shirt and moving hands would swallow thin type. Check the shirt and hands before choosing it.
  - shortkit now encodes with a keyframe every 1 s and closed GOP (mistakes K8).
- **Telugu transcript method (cost: about 50 minutes of CPU, almost no credits):**
  - One whole-file large-v3 pass gave 3 lines for 83 s. Windows of 9-12 s still truncated: Telugu script hits Whisper's 448-token limit. **Use windows of 6 s or less, split at level dips.**
  - About 4 minutes per window on this Mac. Start it in the background first, in two processes, and plan while it runs.
  - A domain `initial_prompt` was echoed back as the transcript in one quiet window. Re-run such windows with a plain sentence prompt, and get one English `task=translate` pass as a meaning check.
- **Went wrong and the fix:**
  - Onset snapping took the LAST quiet-to-loud edge near the ASR time and put PERSPECTIVE 0.12 s late (stop consonants make a second edge inside the word). Take the edge NEAREST the ASR time.
  - A caption stayed one frame into a scene (float rounding at the scene start). End captions 0.006 s before a scene or giant.
  - `pkill -f "shortkit.py video"` leaves the spawned workers and their ffmpeg readers alive; they ran the load to 26 and starved the next job. Kill the `ffmpeg -v error -ss` readers too, and never rename the frames folder under a live render.
  - A shell loop that waits with `pgrep -f <pattern>` matches its own command line and never ends. Wait on an output file instead.
  - Giants sized 380 px put their ink top above the safe zone and hid letters behind the head. make_edl now measures the ink with PIL and keeps the top at y 221 or lower.
  - Five SFX sat within 6 dB of the voice in 300-4000 Hz (an impact tail masked "access"). Lowered them and cut the impact to 0.5 s.
  - CRF 16 with grain and a 1 s GOP gave a 68 Mbps master (708 MB). Deliver a CRF 19 copy capped at 20 Mbps (177 MB).
  - Frame 0 showed the hook word at 35% opacity. Start the first giant at t0 = -0.05 so the cover frame is solid.
- **Not verified:** nobody listened to it. Telugu spellings come from ASR plus reading, not from the ear: check "bali ayyedi evaru?" (59.1 s), "LOOPHOLE" (21.1 s), "perugutadi", "peragadaniki". The company name at 12.8 s was left off. SFX taste was judged by numbers only.
- **Feedback:** pending.
- **Rule candidates (promote if they repeat):** 6 s Telugu windows; nearest-onset snapping; scene inserts as versioned B-roll slots; delivery copy capped at 20 Mbps; first giant starts before frame 0.

### 21. Fan Idea (telugu ruff cut 1) · 2026-11-21 · 57.6 s, Tharun grammar + Pexels B-roll + one designed "oil line" world · music bed asked for
- **Brief (user, this video):** hook in 2 s, every pause out, word-pop captions with coloured keywords, "B-rolls add more" (every 3-4 s), motion graphics, SFX, zooms, trending-style music ducked, flash or whip only, loop ending, no approval stops. Mid-edit: "use how much needed credits, don't waste credits".
- **Made:**
  - His rough cut kept (25 jump cuts, no pause over 0.29 s, first line already the hook). Trimmed 1.43 s: one false start, six pauses of 0.17-0.29 s down to 0.10 s, the tail. Project `edits/telugu1/`.
  - Lime `#B9FF3C` accent (red only on PROBLEM, the empty bottle, COSTLY); Poppins 800/900 captions (98 / 150 px) with Bebas Neue giants; 52 caption groups; giants WORKER IDEA, PROBLEM, SIMPLE behind the head.
  - 12 Pexels vertical B-roll slots and 4 designed scenes (problem, costly sensor, fan fix, savings) on one conveyor: 32.1 s of cutaways (56 %). Size change on every cut and on every return from a cutaway; 5 snap zooms.
  - 49 SFX, Mixkit music 32 at -20 dB ducked 7 dB. Finals 1080x1920, 60 fps, keyframe every 1 s, -14.1 LUFS, peak -1.2 dBFS; delivery copy CRF 19 capped at 20 Mbps (148 MB).
- **New:**
  - **Mixkit video is out for this channel:** on 2026-11-21 free downloads were 720p under a "Restricted License" (personal use), 1080p / 4K behind Envato. Mixkit SFX and music licences still allow commercial use.
  - **Pexels works and is better for shorts:** search through the built-in browser (curl gets 403 on pexels.com), take `videos.pexels.com/video-files/...` links from the search HTML, download with curl. `?orientation=portrait` gives vertical 1440p-4K clips.
  - `edits/telugu1/tools/scenes.py`: one "world" drawn with PIL + OpenCV (sprites made once at 4x, belt time can slow down, world zoom separate from the words). `tools/rerender.py` overwrites chosen output ranges in place, then `shortkit.py video` only encodes.
  - Loop seam with a CTA kept: snap back to the frame-0 size in the last 0.30 s and bring the hook giant back; frame 0 vs last frame luma differs by 3.5.
- **Went wrong and the fix:**
  - Whisper loops (prompt echoed; one word repeated for 6 minutes with temperature fallback). Use no prompt, `temperature=0`, `no_repeat_ngram_size=3`, `repetition_penalty=1.25`, and cut windows at his jump cuts.
  - Captions at 84 px read small, and lines over about 16 characters shrink. 98 / 150 px, short groups.
  - shortkit draws all `k` words of a group at the same spot: ONE keyword per group.
  - Giants at y 420-430 lost two letters behind his tall hair (hair top is at about y 375-390 with eye line 700). Centre y 335-350.
  - Scene art drawn at 100 % was too small for a phone; draw the world at 130 %.
  - Sub-only hits (Mixkit 2303, 2299, 2909) are 27 dB under the voice in 300-4000 Hz. Pair with 2655 or 563. Whooshes and late-onset hits need `align: "peak"` (their peaks sit 0.3-0.5 s after the file start; 2909 and 2901 are swells, not hits).
  - ASR put KOTLU 0.13 s late (silence before the stop). Check every hero word against the 5 ms level before the render.
  - One stock clip showed another company's pack design; swapped. Check B-roll for brand marks at full size.
  - Ran the mux while the encoder was still writing ("moov atom not found"). Wait for the process to end.
  - The last frame was a blink; the loop frame must be checked like the cover frame. Ended 6 frames earlier.
  - A wildcard cleanup after `cd` is blocked by the app. Don't delete render caches; overwrite or version them.
- **Not verified:** nobody listened (SFX and music taste by numbers only). Telugu spellings from ASR: "em cheyali?" (24.5 s), "vellalani" (45.3 s); 22.9-23.6 s has unclear words and no caption. "SHARE" shows about 0.5 s before the word. The numbered delivery folder was made this time (21); 20. Speed Game still has none.
- **Feedback:** pending.
- **Rule candidates:** Pexels portrait search first; peak-aligned whooshes; mid-rich partner for every sub hit; one keyword per caption group; loop frame blink check. Second time seen (promote): delivery copy capped at 20 Mbps; hero-word onset check against the level; versioned slot keys instead of deleting caches.

## 2026-11-21 - training batch (no edit): "zip 1" analysis pack -> P12
- **Learned:** P12 editorial cutout explainer, a faceless voice-over finance reel (29.9 s, 10 scenes, -14.2 LUFS). The zip held no video: a ready skill file, 3 fps sheets, 13 frame-numbered sheets, transcript and audio data. Every sheet was viewed and the pack's claims were checked against its own frame numbers and transcript. Saved as its own skill `04-styles/faceless-explainer-reel-edit-style/` (GUIDE.md + LEARNING-REPORT.md + the pack in `references/pack/`); P12 in `pro-video-editing` points to it.
- **Apply on every short from now:**
  - A percentage on screen becomes a wedge (percent x 3.6°), colour only inside it.
  - A contrast pair (stop/start, myth/fact, before/after) becomes ONE object that changes state; caption colour follows it and the second caption moves to a new place.
  - Plan one line per short that has no caption because the graphic says it.
  - A list of three in the hook: same template, same length, entrance only on the first.
  - The punchline gets the shortest scene; the endcard holds 1 s after its last word.
  - Act turns may use the light-leak flash (10-12 f, last frame scanlines) in place of the white flash; 3 at most.
  - One sub boom per short, under the biggest reveal; a whoosh or click on every scene change.
  - Blur-in two-font captions are a third caption model, for designed scenes and full faceless builds only.
- **Corrections to the pack (from the frame sheets):**
  - Word reveals are not locked to each spoken word within 3 f. Hook words follow the voice within about 5 f; dark-scene words step at an even 4 f and can run up to 0.35 s ahead; after a flash the first word is 6-10 f late.
  - The punchline cut lands about 10 f after its sentence starts, not before it.
  - Speech is about 179 wpm overall (88 words in 29.5 s), not 160.
  - Its headline sits at y 150-190 of 1920, inside our unsafe top band; its true peak is -0.2 dBTP. Neither is copied.
- **Measured reference numbers:** 9 scene changes (3 light-leak flashes, 2 hard cuts, 1 re-stage, 1 object wipe, 1 invert, 1 zoom-through); scenes 1.3-4.3 s; 4 of 896 frames still; sentence gaps 0.30-0.60 s; about 30 airy SFX onsets in 30 s; one sub boom at 13.9-15.2 s.
- **Not tested yet:** nothing was rendered. shortkit.py has no blur-in reveal, two-font line, wedge or light leak; the plan is pre-rendered scene clips dropped in as B-roll slots. Font names and px sizes are estimates from 720p frames. Audio was measured, not heard. The first edit that uses P12 logs what worked here.
- **Feedback:** pending.

## 2026-11-22 - training batch (no edit): "zip 2" analysis pack -> event-map method, P13, P14
- **Learned:** `02-craft/event-map-reel-edit-style`: one method measured on 5 reels (R0 = the P12 reel again) plus P13 two-tier kinetic talking head (R1, R4) and P14 faceless 2.5D documentary (R2, R3). No video in the zip. Read: pack skill file, format B / C, transitions, devices, cross-reel table; viewed 4 overview sheets + 2 detail sheets; per-reel notes stored, not read.
- **Apply on every short from now:**
  - PLAN.md shot table is an event map; check no gap over 1.3 s and one event every 0.6-1.0 s in the hook.
  - Every visual event sits on a word (sync table in the skill, section 3); mode changes go in breaths.
  - Every scene change has a sound; every VO pause of 0.5 s or more carries a move + a sound.
  - Plan the turn ("But...", 60-77 % of runtime) first and give it the biggest device of the second half.
  - Second half keeps at least 70 % of the first half's event rate; CTA 12 % of runtime or less and still moving.
  - Keyword colour = role (opportunity / threat / pivot), one keyword per caption group.
  - Spell-check every overlay against the spoken words (all 5 references shipped a typo).
- **Checked against the pack's own data:** wpm, hard cuts, loudness, peaks and turn positions match; the turn range is 60-77 % (R1 is 77 %), not 60-75 %.
- **Claude's observation:** R4's threat word enters as a letter stagger (about 4 f per letter), not tracking-in.
- **Not copied:** true peaks above -1 dBTP, 2.3x keyword size, keyword fade from 35 % opacity, strobe bursts, news logos on generated headlines, chapter cards that only repeat the spoken word.
- **Not tested yet:** nothing rendered; the scorecard now runs here through `02-craft/event-map-reel-edit-style/tools/score_reel.py` (set up 2026-11-22; baseline on 17. Embarrassment Short: quiet stretch 0.60 s PASS, airy sound on only 11 % of cuts and a near-mono mix, to check by ear); shortkit.py has no two-tier typed caption, pedestal or 2.5D camera yet.
- **Feedback:** pending.

### 22. Grayscale Tip (telugu 3.mp4) · 2026-11-22 · 58.35 s, P13 two-tier kinetic talking head · first edit with the event-map skill, first render of P13
- **Made:**
  - His rough cut kept whole (28 jump cuts, longest pause 0.41 s); only the tail trimmed. Project `edits/telugu3/`, delivered to `edited videos by claude/22. Grayscale Tip/`.
  - Topic: parents, cartoons and phones for small children; the tip is grayscale mode. Turn at 43.5 s (74.5 %).
  - Two-tier captions: Montserrat ExtraBold 88 px lead-in (1-3 words) + Montserrat Black 150 px keyword, 28 groups, 67 of about 185 words on screen. Colour = role: ice cyan `#35D6FF` topic / tip, red `#FF4338` threat, white + cyan bar on the two pivots (KAANI, INKO POINT). Oswald Bold giants PARENTS (frame 0) and FUTURE (last frame) for the loop.
  - 9 Pexels portrait B-roll slots + 3 designed scenes on one "screen world" (bright screen, screen that cuts with a "2 SEC" label, phone whose Grayscale switch drains the colour) = 18.3 s of cutaways (31 %). A Fluent 3D brain behind his head on three lines (overstimulated, ADDICT in red, growth gauge that stalls).
  - Claude's idea that carried the edit: the whole video goes black and white on "grayscale" (47.5-51.4 s) and colour returns on "normal".
  - 89 SFX, no music. Delivery copy 1080x1920, 60 fps, CRF 19 capped at 20 Mbps (150 MB), -14.4 LUFS, -1.3 dBTP.
- **What worked (event-map method):**
  - The event map as the PLAN shot table, then `make_edl.py` printing every gap between events: the 1.3 s rule was checked before rendering (5 gaps found and closed with camera events). 117 events, 58 / 59 by half.
  - Scorecard on the delivery file: all PASS. Static frames 0 %, longest quiet stretch 0.83 s, quiet frames 8.7 %, 190 wpm, airy sound on 85 % of detected cuts.
  - Planning the turn first: it got scene S3 + the black-and-white stretch, the biggest device of the second half.
  - Hidden jump cuts: a rule in the builder forces a framing change of 16 % or more on every visible cut; two push-throughs (9.27 s, 30.62 s) built only from camera keys.
  - A caption-free line (crying toddler, hard cut to a child frozen at a screen) reads without text.
- **What did not work, and the fix:**
  - First scorecard run: airy sound on only 58 % of cuts. Slow whooshes (Mixkit 1490, 2611) have no sharp onset. Now every cut gets a short sharp flick (2384, 3115, 2637, 175, 2995) and the whoosh is only the body under it; click 1117 must be aligned by its peak (its body is 0.09 s into the file).
  - The mix is still near-mono (side / mid 0.10) although the SFX stem is wide (0.66) and cues are panned or swept: one centred voice with no music bed dominates. The scorecard's "SFX per 10 s" line stays unmeasured in a voice + SFX master.
  - 89 cues = 15 per 10 s, above the references' 5-10; 36 of them are quiet cut swishes. To judge by ear.
  - P13's "keyword starts 6-8 f early" was not used: `mistakes-to-avoid` F14 says never early. The keyword starts ON the word and its letter-spacing settles in 0.2 s.
  - P13's speaker-inside-graphics mode was reduced to objects behind his head with the room visible (`mistakes-to-avoid` A1). Pedestal list, search-bar hook and video card were not needed for this script and are still unbuilt.
  - A lead-in that starts under 0.4 s before the next group makes its keyword unreadable (two cases): drop the lead-in.
  - Six captions lingered 1-5 frames across a cut into another picture. The builder now prints any caption that crosses a B-roll edge.
  - Giants at y 455 lost their middle letters behind his head (hair top y 456 at the 1.25 size in this wider raw). y 372-376.
  - Red keywords were weak on the red checked shirt: new 5 px dark outline (`style.stroke`).
  - A 13-letter keyword (CHOOPINCHODDU) is fitted down to lead-in size. Keywords over about 10 letters need a shorter word or two lines.
- **Telugu transcript (again):** `repetition_penalty=1.25` produced mixed-script garbage on this voice; the plain sentence prompt, beam 3, temperature 0 and no penalties worked for 10 of 12 windows. Redo a looped or prompt-echo window with no prompt and `no_repeat_ngram_size=3`. Windows under 4 s with a prompt echo the prompt. About 1 minute per 6 s window here (two processes, 3 threads each); the English pass can use two long windows per process. The raw was 13 dB quieter than the last two, so the onset threshold moved from -33 to -40 dB: set it from the level percentiles, not from the last project.
- **shortkit.py additions (all backward compatible):** keyword opts `c` (role colour), `fx: track | stagger`, `bar`, `strike`, `size`; caption group `y`; `layers` (RGBA PNG sequences behind or in front of the speaker); `dims`; `desat`; `style.stroke`; SFX `pan` and `sweep`. Still not built: pedestal list, typed search bar, live video card, 2.5D camera.
- **Not verified:** nobody listened. Telugu spellings and the times of "2 SEC" (22.45 s), "MUSIC" (24.14 s) and the second COCOMELON (37.44 s) come from ASR and the voice level. No caption at 19.5-21.7 s and 33.4-37.3 s because the words are unsure. Not watched on a phone.
- **Feedback:** pending.
- **Rule candidates:** sharp airy flick on every cut; builder checks (event gaps, 16 % framing change, caption crossing a cut); text outline on patterned clothes; onset threshold from level percentiles. Seen again (promoted to GUIDE.md today): 6 s Telugu windows with the plain prompt; scene inserts as versioned B-roll slots; one keyword per caption group; giant placed from the measured hair top; first giant starts before frame 0.

## 2026-11-22 - training batch (no edit): 5 skills received -> P15, ue-sound-design, beginner-to-pro-edit-tips, watch, ae-builder
- **Received:** `Prompts List.docx` (master prompt for a Remotion short-form brief; the brief link was not in the file), `UE-Sound-Design-Claude-Training-COMPLETE.md`, `watch-skill.zip`, `ae-builder.skill`, one finished reel (49.75 s) + its raw (76.3 s) with the instruction "listen words carefully for editing tips".
- **Stored:** `04-styles/ultimate-editors-shortform-style` (= P15), `03-sound-type-assets/ue-sound-design` (document word for word + local section), `02-craft/beginner-to-pro-edit-tips` (always read), `06-tools/watch` and `06-tools/ae-builder` (unchanged + local section).
- **Heard (three rules):** make every element 25 % smaller; keep effects for the elements that must grab attention; dull colours, no harsh black / white / bright red.
- **Measured on the reel:** 65 % of the raw kept, 191 wpm, keyword 3.7-4.5 % of frame height, accent `#3D77F3`, off-white `#F0EEEA`, lower 45 % darkened for overlays, layouts 43 / 26 / 31 % (overlay / split / full-screen), 24 sound hits, a hit on every detected cut.
- **Tooling:** `06-tools/watch/scripts/watch_mac.py` runs the received extractor here (imageio ffmpeg, ffprobe stand-in, faster-whisper). Its scene detection at 0.3 found 5 of about 12 layout changes: use 0.15 or read the pairs.
- **Not done / not verified:** the brief was not received; the UE sound library and a Remotion project are not on this Mac; the ae-builder gate was not run (blocked by the app's safety check); nobody listened to the reel; only the hook and one scene change were viewed at 10 fps.
- **Sound clash, answered 2026-11-22 ("use when it required"):** `ue-sound-design` is used when the job calls for it (UE / Joseph style, Remotion, the P15 look, or asked by name); `sound-and-music-design` stays the rule on his own channel edits (music under graphics, whoosh count, texture level, 2-3 frame lead, approval stops).
- **Rule candidates:** 0.75x pass on every icon / shape / card; one named attention element per scene; frame colour sample in export QC.

### 23. Uncertainty Truth ("Telugu short.mp4") · 2026-11-22/23 · 60.38 s, Tharun 9:16 grammar + motivational two-voice type, event-map method
- **Made:**
  - His rough cut kept whole (41 jump cuts, no pause over 0.3 s except one 1.0 s gap at 46.1 s). Project `edits/telugu4/`, delivered to `edited videos by claude/23. Uncertainty Truth/`.
  - Topic: "Uncertainty is the only universal truth"; life is not a government-exam syllabus; Gita 2.47 (focus on the work, not the result); embrace uncertainty. Turn at 38.6 s (64 %).
  - Type trio: Inter Tight 800 lead-in + 900 caps keyword for facts, Playfair Display ExtraBold Italic keyword for meaning words (truth, uncertain, embrace, adventure, happiness), Impact giants. Dull saffron `#E89B45`, dull red `#D24E5A` on negatives.
  - 10 Pexels B-roll slots, 3 designed scenes (blueprint sheet in two states: plan -> struck SYLLABUS whose path breaks into question marks; Gita page with "chese pani" lit and "result" struck), a CONTROL meter layer above his head that drains on "nijam kaadu". Loop: giant CERTAIN struck on "kaadu" at the end, frame 0 = UNCERTAINTY.
  - 109 SFX, masters -14.0 LUFS / -1.4 dBFS: voice + SFX, and a with-music alt (Mixkit 587 at -21 dB, ducked, one removal under the Gita turn).
- **New:**
  - Code-mixed Telugu: the `te` pass loops on windows full of English words. A `language="en"` transcribe pass on 4-5 s windows gives the English words' times (marks, job, restaurant, result, control, share); the level dips at his jump cuts give phrase starts.
  - shortkit: keyword `"font": "serif"` (+ `"glow"`), giant `"font"` and `"strike"`, music `"gaps"` (one BGM removal with fade back).
  - The scorecard's quiet-frame test uses 6 x 10 blocks: thin lines and small labels on a flat scene background read as still (and look still on a phone). Designed scenes need one bold change every ~1 s: spread pops across the words, glowing lines 11 px+, a moving element (dot walking the path) in any beat over 1 s.
- **Went wrong and the fix:**
  - Hair top moves from 420 px (zoom 1.25) to 328 px (1.52) during the hook push: giants at y 392 lost middle letters. Gentle hook push (1.25 -> 1.34, snap out not in), giants size 262 at y 314-318. An 11-letter giant fits only at 0.69: keep the long word small, swap to a short one big.
  - My SFX density filter (drop a cut flick within 0.15 s of a designed cue) also dropped the flick paired with each cutaway whoosh: airy-sound-on-cut fell to 76 %. Flicks paired with whooshes are marked `keep`; 96 % after.
  - PIL here has no raqm: Telugu / Devanagari script cannot be drawn in scenes; romanise.
- **Not verified:** nobody listened; Telugu spellings from ASR (nachinattu, penchaaru, chetilo ledu, bratikela); no caption 5.0-7.6 s (words unsure); mix near-mono (side / mid 0.09), second time after 22.
- **Feedback:** pending.
- **Rule candidates:** English-mode pass for code-mixed words; bold change every ~1 s inside designed scenes; gentle push while a giant is up. Seen twice (22, 23): voice + SFX master stays near-mono; the with-music alt is the wider one.

### 24. Pink Tax ("ammailu.mp4") · 2026-11-25 · 43.90 s, P8 "X vs Y" explainer + event-map method
- **Made:**
  - His rough cut kept whole (25 jump cuts). Project `edits/ammailu/`, delivered to `edited videos by claude/24. Pink Tax/`, copy `Desktop/Naveen bro edits/Telugu shorts/Telugu short 5.mp4`.
  - Topic: the pink tax (haircut / lip balm / razor cost girls more for the same thing; "luxury kaadu"; question it, share it). Turn at 29.3 s (67 %).
  - Type trio: Tactic Sans Bold lead-in + Black caps keyword (first use of the user's own font), EB Garamond Bold Italic for "luxury", Impact giants. Dull rose `#E2799E` = girls / the tax, steel `#8EA3B8` = boys' price, dull red only on the strike.
  - Designed pieces in `tools/scenes.py`: split price board used twice (haircut, razor: steel half / rose half, the girls' tag shows the boys' price, then rolls up and turns rose), lip-balm tags hanging behind his head (RGBA layer), receipt payoff (rose marker sweep, PINK TAX stamp, pen circle on "question"). 9 Pexels B-roll slots, giants AMMAYILU (frame 0 and loop) and PINK TAX.
  - 106 SFX, masters -14.3 LUFS / -1.4 dBTP; with-music alt (Mixkit 543 at -21 dB, ducked, removed under the receipt). Delivery copies CRF 19 capped at 20 Mbps (113 MB).
- **New:**
  - Unclear spoken prices: five passes per span (te windows, en mode, hi decoder, beam 5, temperatures). Show only what every pass shares ("₹150", "₹200+", "₹80+") and say so in QC. Never fill a number in.
  - Counter roll across layouts: parse numbers with a regex and use the target's layout ("30-40" -> "80+").
  - Tactic Sans has no ₹: rupee in Montserrat Black at 0.8x + Tactic Black digits as one word.
- **Went wrong and the fix:**
  - Receipt price columns 114 px apart touched: wider paper, fixed column centres (caught on the scene sheet).
  - Rose serif "luxury" on a pink bottle did not read: off-white there (contrast beats colour-role on a same-colour picture).
  - `stagger` on a 13-letter word with 0.6 s on screen never finished: removed; use it only with 1 s+.
  - Punches after a push-through stacked the zoom to 1.95: cap 1.80.
  - Receipt entrance cluster at -4.9 dB against the voice: thinned to riser + light whoosh + one tick.
  - Full-frame mask per dash made the receipt render slowly (about 6 min for 127 frames): draw dashes into one mask.
- **Not verified:** nobody listened; lip balm and girls' razor prices partly unsure; Telugu spellings from ASR.
- **Feedback:** pending.
- **Rule candidates:** show only the agreed part of an unclear number; stagger only with 1 s+ on screen; zoom cap 1.80; check every keyword colour against the B-roll under it. Seen twice (23, 24): 20 Mbps delivery copy.

### Client feedback · 2026-11-25 · caption style change (applies to the Naveen bro shorts, videos 16-24)
- **Feedback:** the client is disappointed with the current edits. Subtitles must be **aesthetic** and use **mustard yellow + red**; everything else ("rest all good") stays: cuts, B-roll, SFX, giants, grade.
- **Done:** four mustard/red caption looks mocked on a clean frame of the Pink Tax raw (`edits/mustard-red-captions/previews/`, code in `code/caption_options.py`): A retro offset (Tactic Sans caps, deep-red hard offset shadow), B editorial serif (Inter Tight lead-in + Playfair ExtraBold Italic mustard keyword, red underlined negative), C highlighter (Montserrat Black cream text, thin mustard / red marker bands), D word pop (Poppins ExtraBold caps, spoken word mustard, negative red). Colours: mustard `#DCA632`, dull red `#C9443A`, deep red `#8A2620` (shadow), cream `#F4EFE3`, ink `#1A1410`.
- **Seen:** his red-white checked shirt sits right under the caption zone: red text needs an ink outline (3-7 px) or a marker band to read.
- **Open (asked the user):** which look; red's role (negatives only vs second keyword colour); fixed palette for every video of this client vs the per-video accent rotation in `fonts-and-colours`; caps vs lowercase; 1-3 words vs full sentence; reference videos (`edits/mustard-red-captions/inbox/`).
- **Rule candidate:** a client's requested caption palette overrides the per-video accent rotation for that client's videos.
- **Follow-up, same day (research):** studied 8 reference shorts on YouTube and Instagram for "aesthetic mustard + red subtitles" and saved the style as its own skill `05-clients/naveen-bro/mustard-red-caption-style/` (references measured in `references/reference-reels.md`). Three looks: M1 podcast serif (Figuring Out: cream caps + mustard bold-italic serif keyword) = default, M2 golden caps (Kobe / Hormozi: one line of caps, keyword mustard), M3 film subtitle (Instagram vintage trend; breaks keyword-only, client must pick it). Palette fixed: mustard `#E2AA2C`, brick red `#D2483C` (negatives only, 1 group in 4 at most), cream `#F4EFE3`, ink `#1A1410`.
  - shortkit: `style.cap_color` + per-word `{"c"}` on lead-in words (default white, old EDLs unchanged). Engine test on Pink Tax stills passed (M1 and M2).
  - Seen: an M2 line of 4 words shrinks to fit 900 px and reads small: 2-3 words per M2 line.
  - Tooling: YouTube Shorts frames can be read without downloading (canvas from the playing video, colours from pixels); Instagram search in the hidden browser pane is unreliable (lazy images, 360p, feed jumps): ask the user to screen-record Instagram references.

### Research + signature look · 2026-11-25 · mustard-red round 2 (aesthetic) and round 3 (Instagram advanced pro edits), Naveen bro client
- **Asked:** (1) research aesthetic editing, captions and fonts so the client is impressed; (2) design an original look of my own for exactly this client; (3) "some Instagram channels do aesthetic font subtitle edits; the client needs that, fully advanced pro edits, not a normal edit".
- **Done, round 2:** 3 more YouTube references (A1 to A4: moody low-saturation grade, mixed-weight type, ghost words, documentary highlighter). Free OFL fonts added with the user's OK: Fraunces (Soft Bold / Black Italic), Bricolage Grotesque, Bebas Neue, DM Serif Display. **M4 "Haldi-Kumkum"** (Claude's own: turmeric + vermilion) is now the default caption look in `mustard-red-caption-style`. `tools/restyle_edl.py` converts any EDL; `tools/style_board.py` makes the client pitch board. shortkit: `style.ghost`, keyword `brush` and `dot`. Sample `edits/mustard-red-captions/previews/signature/Pink_Tax_HaldiKumkum_sample.mp4`.
- **Done, round 3:** 11 Instagram reels measured (amro.films, kienobifilms, dopemotionzone, the_nicks_edit, viashaan, sam.john.creates, mazeirons, vinaytheeditor, kreatize_, twenty.fourth.edit (Telugu), prime_animator). Saved as the new skill **`aesthetic-pro-reel-edit-style` (= P16)**: layer stack, insert menu, event grid, sound, QC. shortkit gained `style.reveal: "blur"`, `paper` (off-white paper scene, speaker cut out, haldi ribbon, ink captions), `brackets.label` (mono HUD + live X/Y) and `brackets.shape: "ring"`. Sample `Pink_Tax_PRO_sample.mp4` (same 18.3-29.9 s range as the M4 sample, for comparison).
- **Measured:** pro talking-head clips cut every 1.9-2.5 s, change the text every ~1 s, use two fonts per line, and add a quiet designed insert every 5-8 s; Telugu editors put a literal B-roll on every concrete noun and show numbers as big type. No reference stacks two special moves at once.
- **Went wrong and the fix:**
  - "?." after "difference?": no kumkum dot after punctuation.
  - Brush too low: centre at ky + 0.16 kh, height 0.50 kh.
  - Ghost words do not show on Pink Tax because its lead-ins are phrase tokens: split lead-ins into word tokens when the EDL is made.
- **Not verified:** the client has not seen either sample. Nobody watched them on a phone. The pro sample reuses the delivered Pink Tax audio, so the new inserts have no sounds of their own yet (paper slide, HUD tick, ring bloom are in the P16 sound table).
- **Rule candidates:** a client's requested palette overrides the per-video accent rotation (seen twice: 24 + this); "advanced" means more layers spread out, never more effects at one moment; a HUD label says the script's own words, never an invented number.

### Research · 2026-11-25 · fonts for every video type, subtitle standards, editing styles
- **Asked:** "search for best fonts for short form and long form videos and other forms, aesthetic subtitles, best editing styles ... learn and push to skills folder; every edit uses those skills" (no stops wanted).
- **Done:**
  - 17 more Instagram font reels read (harrisonniap, thesanjaysingha 99K, kalylsfilms, bytheway.deshna, aasil_khan_ and others), plus web guides and the Netflix English / Telugu / timing specs and the BBC numbers.
  - 22 free fonts downloaded from google/fonts plus 17 static weights, so the central folder now holds 70 files, 13 of them Telugu.
  - Two new always-read skills: `pro-font-and-subtitle-guide` (pick by video type, library, subtitle numbers, safe zones, Telugu, licences, QC; specimen sheet + `tools/specimen.py`) and `video-styles-atlas` (every video form, with new sections for vlog, wedding / brand film, tutorial, UGC ad, fan edit).
- **Found:**
  - DM Serif Display, Cinzel, Permanent Marker, JetBrains Mono, Courier Prime and Special Elite have no ₹ (they draw an empty box).
  - Archivo Expanded 900 overflows a full caption line: 1-2 words only.
  - PIL here has no raqm, so Telugu script would render with broken vowel signs. `brew install libraqm` was blocked by the permission check; the user decides.
- **Rule candidates:** at most 3 font families per video; the ₹ check on every price; Telugu subtitles at 22 cps, no italics.

### Client brief · 2026-11-25 · font pairings (round 4), Naveen bro client
- **What came in:** six screenshots of a "font pairings you must try" carousel (raktimcreates) and one reel (tobydeboer "Grind szn", 8.1 s) showing how words should appear. The user's words: take them as reference, "not like that".
- **What was learned:**
  - The carousel: two fonts per moment, contrasting on two axes; the big word 2.5-4x the small one; tight tracking; lines overlap; type in the empty part of the frame.
  - The reel: 22 cuts in 8 s; one word per shot; lowercase bold sans plus a formal script on the emotional words; a 0.17 s fade or 0.23 s blur reveal; stacks built word by word.
  - Saved to `mustard-red-caption-style` section 2c + `references/client-font-brief.md`, and to `pro-font-and-subtitle-guide` section 2b.
- **Made:**
  - A pairing board on Pink Tax stills (`edits/mustard-red-captions/previews/pairings/PAIRINGS_board.jpg`).
  - 6 new library fonts (Italianno, Pinyon Script, Yellowtail, Instrument Serif x2, Playfair 800 Italic static).
  - shortkit: keyword `"font"` now takes `"script"` (style.script_font) or any library file name.
- **Went wrong / lesson:**
  - Italianno in the chest zone over the checked shirt is unreadable. Thin scripts go only on the plain wall above the head (y 300-640) or on paper; the chest keeps Fraunces.
  - Wide caps behind the head must sit high enough that only their feet are covered (SHARE baseline 735, hair top about 660).
- **Waiting:** the client's pick of pairings; nothing rendered as video yet.

### Toolchain · 2026-11-25 (night) · Telugu script renders now
- **Fix:** `brew install fribidi` (3 packages built from source, about 25 min). Pillow's raqm turned on (`features.check_feature("raqm")` True); `libraqm` itself was not needed (it would have meant 36 source builds).
- **Test:** shortkit drew "కానీ ఎందుకు ఈ / తేడా?" correctly. Lead-in: Anek Telugu SemiBold static (the variable file loads thin). Keyword: Baloo Tammudu 2 ExtraBold in haldi.
- **Lessons:**
  - Check `telugu_check.py` before any Telugu-script render.
  - Gidugu and Suranna have no ₹.
  - Latin captions are now kerned (up to 1.6 % narrower): for partial re-renders of older projects use `SHORTKIT_LAYOUT=basic`.
  - Homebrew has no Intel bottles any more, so every new formula builds from source. Pick the smallest formula that gives the needed library.


### Learning · 2026-11-25 (late) · text animation moves (no edit; "dont do edits now just learn skills")
- **Studied** (built-in browser, `browser_reference_capture.js`, 1/30 s grids):
  - shami.mp4 `DKC2AJ0z6s0`, a "$5 vs $80 edit". The pro version builds word stacks on alternating sides, types "everyone" letter by letter in 0.37 s and clears each stack on a hard cut.
  - yp.motionstudio `DYnW0cCIlry`, faceless kinetic type: 22 cuts in 9.3 s, speeding up, with background flips and grain / slam arrivals.
- **Built in shortkit:**
  - `stacks`: 2-5 line word stack, layout fixed from all tokens, big + small words sharing baselines, alignment center / left / right / stagger, behind-head, ghost, fade-out.
  - Token fx: `cut` / `fade` / `blur` / `rise` / `grain` / `pop` / `type`.
  - SFX `"ss"` slice start.
- **Tested:** stills only, on the client's raw (`02-craft/text-animation-moves/references/frames/STACKS_test_sheet.jpg`). Audio collision table: all 7 cues 18-30 dB under the voice.
- **Lessons:**
  - At camera 1.25 the client's hair top rises to about y 460, so the wall space is y 100-450, not 300-640. Measure the head on a still for every video.
  - Link words at ratio 0.42 must stay 44 px or more.
- **Saved:** new skill `02-craft/text-animation-moves` (move menu, layout rules, sound per move with files on this Mac, faceless notes, QC, gaps).

### Feedback · 2026-11-25 · subtitles too heavy above the head; no Telugu font
- **The user's words:** "dont use telugu font max and full subtitles in upper head looks heavy adjust not all text in upper head. adjust subtitles."
- **Cause:** the first word-stack test put every stack on the wall above the head.
- **Fix:**
  - Subtitles and stacks now run in the lower caption zone (y about 1120, ink outline 3; red on the red check needs 5).
  - Above the head only 2-3 moments per 45 s short (hook, one middle, loop line), counting every kind of above-head text.
  - No Telugu-script font: Tenglish in Latin fonts unless the user asks.
- **Checked:** a new stills sheet and full-size crops of the chest zone. Every word is readable with the outline, including "aren't" in kumkum (stroke 5).
- **Saved:** `text-animation-moves`, `aesthetic-pro-reel-edit-style` rules 8-9, `mustard-red-caption-style` 2c, `pro-font-and-subtitle-guide` section 6, CLAUDE.md Rule 4.4.

### Research · 2026-11-25 · where text goes in a vertical short ("don't create by your own, research")
- **Sources:**
  - platform safe zones (Meta Reels ads 14 / 35 / 6 %, TikTok 240 / 660 / 120 px, vendor numbers for ordinary posts);
  - eye tracking (Kurzhals CHI 2017, BBC Dynamic Subtitles 2015);
  - about 15 reels studied earlier.
  - Full write-up: `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`.
- **Rule:**
  - subtitle block centre at 58-65 % of the height (y 1110-1250), under the chin, never on the mouth, bottom above y 1470, lines within x 120-960;
  - above the head only 1-3 accents per short (hook title, number, label), below y 270;
  - beside the face only with real empty space.
- **Lesson:** my earlier numbers were guesses; placement now comes from the research file. The demo's above-head accent had been at y 140, inside the top UI band, and is now at y 285.

### Edit · 2026-11-26 · 25. Uncertainty Truth English (Naveen bro client, "Rough cut 3.mp4")
- **The user's words:** "dont add bgm and dont add color grading, do perfectly based on clients requirements"; mid-edit: "use only best font combination"; "Bricolage Grotesque with Fraunces Soft Italic dont use these use i gaved image from you trained fonts from those take best fonts combinations".
- **Style:** P16 aesthetic pro reel + event-map method; his cut kept whole (OUT 56.00).
  - Inserts: 12 literal B-rolls, two paper scenes (thesis lines), a Gita artwork plate, a face ring and a neg flash.
  - Text: a hook title stack above the head, 2 chest word stacks, and a giant "uncertainty" on paper 2. Above-head accents: 2.
- **Fonts:** Poppins + Playfair Display ExtraBold Italic only (the client's carousel pairing A). M4 palette and mechanics kept.
- **Scorecard:**
  - static 0.30 %; longest quiet stretch 0.47 s; -14.1 LUFS / -1.4 dBTP; 91 % of hard cuts with air.
  - Quiet share 17 % (LOOK): a slow speaker at 175 wpm with long pauses; his cut is kept.
- **Fixed after the stills:**
  - Paper-scene captions turned ink on his brown shirt and vanished; they are now cream + outline (new paper key `stroke`).
  - The Gita crop put haldi on the gold chariot; it became the whole painting as a plate on paper.
  - Phone screen: ink lead-ins.
  - Three B-roll starts moved onto phrase starts so no caption is cut by an edge.
- **Kit fix (no-grade QC):**
  - shortkit darkened every render by about 2.5 luma levels (swscale fast rounding on the source decode, the B-roll prep and the final encode, plus a truncating LUT). Added `SWS` accurate-rounding flags and a rounded LUT.
  - The `video` command renders only missing frames, so after a kit-wide change move `work/frames` aside before re-rendering, or the old frames are reused ("rendered 0 frames").
- **Other lessons:** Pexels titles can lie (34565141 "Gita" = a wedding card). `fs_181773_48k.wav` is silent. 2637 / 1490 flicks don't read as air on cuts.
- **Rule candidates:** measure rendered vs source colour on every no-grade request; artwork plate for portrait art; caption-edge check drives B-roll starts.

### Feedback · 2026-11-26 · video 25 not impressed by the client: use ALL skills, real motion graphics
- **The user's words:** "this is edit not impressed by client i told you use all skills what you learned still now espicially yesterday's learned things. from next time onwards should use perfect skills i mean brolls, motion graphics and other things like pro editor? create a before edit things in folder."
- **Cause (measured with the new gate):**
  - Only 4 designed motion graphics (2 paper, 1 plate, 1 ring) = 11 % of runtime, with nothing designed from 0 to 17.8 s.
  - No HL / MC, though `my-editing-rules` 11 asks for them and the Gita quote was the place.
  - Everything else was captions, stacks and stock clips: `mistakes-to-avoid` 16 again.
  - The craft skills (`motion-graphics-style`, `text-highlight-match-cut`, `video-intro-design`, `app-product-animation`, `client-video-editing-process`) were not opened.
- **Fix:** new folder `CLAUDE 2.0/before edit/` and CLAUDE.md Rule 0.
  - Reading list of all 36 skills (newest lessons first) and the pro move menu with floors.
  - A PRE-EDIT sheet per project, the client bar, and the post-mortem.
  - `tools/pre_edit_gate.py`: video 25 = 5 FAIL. Earlier edits 22-24 also fail the "no 9 s without MG" floor, so the floor is a real step up.
- **Rule:** for every short, designed MG every 8 s, 3+ kinds, >= 25 % of runtime, HL + MC, and literal B-roll per noun; the gate must say READY on the draft EDL before any full render.

### Edit · 2026-11-26 · video 25 v2 rebuild: Uncertainty Truth English ("Rough cut 3.mp4"), to the `01-process/before-edit/` gate
- **The user's words:** "Yes, rebuild it / every thing that how pro editor do edit? with every thing brolls, captions, motion graphics and other things needs and also you researched yesterday why dont you use those knowledge use whole knowledge and edit best."
- **Process:** all 23 skill rows ticked in `edits/roughcut3/PRE-EDIT.md`. Then the speech -> visual map, a 13-row MG plan, HL + MC, and an asset log. The gate ran on the draft EDL before any full render: 1 FAIL, then READY.
- **Built (`edits/roughcut3/tools/mg.py`, one `Canvas` class for scene clips and RGBA layers):**
  - match-cut window behind the head (7 sources x 8 frames under the typed title);
  - checklist card x3: tick on each word, bloom, then struck out on "but the truth";
  - exam syllabus sheet with a "?" stamp;
  - control card: the bar fills 0 -> 100 %, then drains on "isn't true", and the card drops;
  - real Wikisource Gita 2.47 page with marker + underline (HL);
  - share card with a cursor tap;
  - loop window (last frame = frame 0).
- **Gate:** 15 MG events, 46 % of runtime, longest gap 7.4 s, HL + MC, 9 footage B-rolls, no 1.3 s event gaps, all pauses covered.
- **Scorecard:** static 1.25 %, longest quiet 0.77 s, -14.1 LUFS / -1.3 dBTP, 88 % of cuts with air; quiet share 21 % (LOOK: calm speaker, no music). Colour vs source within 0.14 levels.
- **Fixed after the renders:**
  - 0.6 s freeze on the held 100 % card: slow float + longer camera push.
  - "isn't true" caption on the falling card: earlier drop, caption at 33.70.
  - Edge flicks dropped by the dedupe (air on cuts 54 %): every hard cut keeps its flick.
- **Kit / gate lessons:**
  - The gate now reads `meta.mg_events` (beats inside built scenes).
  - After re-rendering a scene under the same key, move `work/broll/<key>_full` aside.
  - A camera change re-chains the framing of the next segment, so move those frames aside too.
- **Delivered:** `edited videos by claude/25. Uncertainty Truth English/Uncertainty_Truth_EN_v2.mp4` (v1 in `v1-rejected/`) + `Naveen bro edits/English shorts/English short 5 (v2).mp4`.
- **Rule candidates:** every list of 3+ becomes a ticking card; every "X is under control / is fixed" claim becomes a number or bar that fails on the turn; the hook's MC window returns as the loop.
