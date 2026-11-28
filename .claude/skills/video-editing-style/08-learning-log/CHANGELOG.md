# Skills changelog: everything learned, by date

Newest first. Each entry says what was learned, where it was saved, and what is still open. The edits themselves are logged in `shorts-editing-pro/LEARNING-LOG.md` (shorts) and `../edited videos by claude/README.md` (all deliveries, 25 so far). Add an entry here after every skill change (README section 7).

## 2026-11-28 (saved to GitHub): Wan 3.0 animation guide as its own skill; the back-to-facts project files
**The owner's words:** "Of course you will save in to github repo and another question are you saving every trained data ..."

**Saved:**
- New skill `.claude/skills/wan3-animation-styles/` (a separate module, not part of video-editing-style): the SFERRO guide "5 AI Animation Styles You Can Make With Wan 3.0". One file per style (image prompt + Wan 3.0 prompt + sounds + Option B), the workflow, the 5-shot example, his 8 working rules, and the PDF itself in `source/`.
- The two places where his pasted copy differed from the PDF (style 1 and style 5 lock paragraphs) were fixed to the PDF wording and listed in its SKILL.md.
- `05-clients/move-with-raghu/worked-example-back-to-facts/`: compositor, sound script, plan, caption script and approved frames of the delivered video.

**Open:** his skill order (rule 2) and skill index (rule 6) were blank templates; the Wan 3.0 skill uses the guide's own order as a working default until he confirms.

## 2026-11-28 ("back to facts" update, preview stage): typography from his reference; text never on his face
**The user's words:**
- "I don't like the font and fonts placement also ... I send it to one reference, not exactly, but do inspire for my reference. And typography maintain."
- Then: "the font on my face. I don't like that, so don't repeat again. And Pull down the captions and reduce a little bit, not a more."

**Saved:**
- `05-clients/move-with-raghu/PROFILE.md`: owner's rules, the face-clearance rule, the approved lockup typography, the channel facts.
- The compositor rule: lockup top is at least the lowest chin of the phrase plus 46 px. An automatic face-overlap check runs over every 0.1 s and must show 0.

**Then (typography v4):** "3 lines ... look like more fonts, it look like disturbing ... add only 2 lines rather than 3 lines."
- Saved to `PROFILE.md`: two lines at most per phrase; split long phrases instead of dropping words; no on-screen element that repeats his words.
- Compositor: lockups auto-fit a 1000 px column; chin clearance now follows each moment's own scene when a phrase crosses a cut; the exit fade waits 0.1 s after the last word.

**Delivered** after he approved the v4 frames ("Yeah now start the video editing"): log in `02-craft/shorts-editing-pro/LEARNING-LOG.md`. **v2** (his two notes: varied comments, better SFX): done, see the LEARNING-LOG entry. Lesson for his videos: put a low layer under the big reveals and shelf the SFX bus at 55 Hz; with no music, the sub band is otherwise empty. **Open:** a clean Instagram photo.

## 2026-11-28 (P21 edit v2): the owner's nine changes to the GTA 6 video
**The user's words:** "There are few mistakes you should change in this video: 1. Remove starting frame and keep my face 2. Remove tanglish captions entire video ... 5. Remove time symbol, I dont like that may be add good one ... 8. At 46 sec that letter (13 years of development keep small and add that lines on the words properly its not straight ..."
- **Saved:**
  - P21 GUIDE section 6c: his taste (face first, no captions, no top sentences, no doodles, no clock icons, straight measured strikes, small text over the face, fewer data cards);
  - worked example updated: engine, sound plan, a before/after sheet;
  - learning-log entry.
- **New component:** the flip calendar for "timing" (real dates peel off from the top edge; the release day is circled), plus measured straight strike-throughs (`getBoundingClientRect` per line).
- **Gate:** 4 FAILs caused by the owner's removals, reported to him, gate not edited.
- **Open:** the owner's verdict on v2.

## 2026-11-27 (first P21 edit): "GTA 6: why it took 13 years", framed window and Tenglish captions
**The user's words:** "Edit my GTA 6 facts video ... DO NOT START EDITING IMMEDIATELY ... Show me the visual frames and references for each scene ... No background music (BGM). No colour grading." Then: "Ok it looks fine the storyboard and I select these 1.framed window opt B 2.Tinglish opt B."
- **Saved:** `04-styles/vice-neon-title-edit-style/references/worked-example-gta6/` (README, compositor, timeline, Tenglish captions, sound plan, plan, storyboards, final key moments, credits). GUIDE section 10 holds the lessons.
- **New know-how:**
  - official game media pages (Rockstar's media page offers zips "to download and share") come first; YouTube blocks cloud downloads, and that is not bypassed;
  - evidence cards are Playwright clips of a page's `h1` or key paragraph;
  - per-clip Whisper for Telugu;
  - the concat-filter join for split phone exports;
  - Shorts-safe caption band (y about 1460-1560, right edge clear);
  - hits must land on the cut, about −10 dB under the voice, or earshot (and viewers) do not hear an attack.
- **Open:** the owner's feedback on the edit; trailer gameplay if the owner supplies the files.

## 2026-11-27 (new style P21): vice-neon titles learned from a logo reveal and two type posters
**The user's words:** "Learn these fonts and pictures and video also, because after learn this I will send you one video. It's all about a man. It's my video. I am telling about GTA 6 facts, means why GTA 13 years takes time and that type of. So use your entire creativity. Go and first of all you learn this, then after I will send you one video."
- **Studied:** one 26.65 s logo reveal (every frame measured: reveal, light sweep, flash-and-settle line, neon edge draw, fill and bloom, diagonal wordmark wipe; sound: an orchestral build, then sparse notes the moves land on) and two type posters (editorial serif on deep red; stacked game title on a blue-to-pink sky).
- **Saved:** `04-styles/vice-neon-title-edit-style/` (GUIDE, `references/r9-logo-reveal-measured.md`, `tools/vice_neon_titles.html` + `render.js` + `fetch_fonts.sh`), profile **P21** in `04-styles/README.md`, router rows in `SKILL.md` and `README.md`.
- **Fonts:** Pricedown Black for the game-title voice (free for commercial use; not committed, fetched by script), Noto Serif Display (width 78 %, tight tracking) for the editorial serif after 11 candidates were rendered beside the poster, Patrick Hand for the handwritten aside after 6 candidates. The poster's own serif was not found under a free commercial licence.
- **Proof:** a 13.5 s original test (a neon "13", "years in the making", a serif chapter card, a game-title card with our own striped sun) rendered with the tool and sent to the owner.
- **Rule kept:** no studio or game logo is redrawn; game footage only if the owner supplies it.
- **Second skill installed the same day:** `.claude/skills/motion-graphics-craft/` (the owner's motion-graphics pack, profiles M1-M7), with the full pack unzipped at the repository root; the owner said "Keep it as it is".
- **Open:** the owner's GTA 6 facts video (to come); plan plus storyboard frames before any render.

## 2026-11-27 (re-edit, v4): script letters whole, the 0:39 bubble in sync, three keyword motion graphics
**The user's words:** "Every cursue caption or letters is cut the edges ... At 39 sec the frame is move fast like it doesn't sync the voice ... Add some proper motion graphics make sure don't add messy type of random graphics".
- **Cause and fix, clipped script:** the write-on mask never fully cleared and swash glyphs overhang their box. The mask now runs past the word and is removed when the word is complete; script spans are padded with matching negative margins. Saved in `worked-example-v4/hc/engine.js` (`writeOn`) and `hc/stage.html` (`.w.script`).
- **Cause and fix, out of sync:** never show a second window of the same speaker talking at a different moment next to live speech; use a still, closed-mouth frame with a slow push (or the same live frame). Saved in GUIDE section 11.
- **New overlays (one per keyword, drawn above the captions):** lens over "the facts", pen nib on the script write-on, a two-stage arrow under "only way". Logged in COMPONENTS-LOG.
- **QC added:** crop every fully written script word at full size; play every motion graphic as a frame sequence and check it finishes at least 0.1 s before its caption leaves.
- **Open:** earshot's minor notes (thin low end, dull presence) stay, as in v3; the owner's feedback on v4.

## 2026-11-27 (re-edit, delivered): v3 rendered after the owner's approval with three panels redesigned
**The user's words:** "approved but improved motion graphics and render the video, DONT LIKED FRAMES IS 3,13,16".
- **Client taste saved:** no fake app UI and no flat dark text plates for Naveen bro (CLIENT-BAR). Three redesigns and motion upgrades (typing dots, converge spark, pill overshoot, frame corners, match-cut pulse, card drift, a circular arrow on "change").
- **Sound:** `audio.py` in the worked example; earshot score 19 of 23 metrics in range against the four reference reels (music excluded by the client rule).
- **Components logged** in `02-craft/shorts-editing-pro/COMPONENTS-LOG.md`; credits for CC BY sounds in `worked-example-v4/sfx_credits.md`.

## 2026-11-27 (re-edit, preview stage): storyboard built with a browser compositor, waiting for approval
**The user's words:** the master brief (R7 > R6 > R5 > R8; new captions, typography, SFX, icons and motion; keep the B-roll; no BGM, no grade; previews first), then "For fonts use R8 fonts and for caption placement use R7 and R6 and for typography use all reference videos".
- **Fonts matched to R8 by side-by-side renders:** Great Vibes (closest swash capitals and contrast of 13 scripts tried) + Arimo (R8's sans is Helvetica / Arial-like). Accent sampled from the footage.
- **New renderer:** HTML/CSS pages drawn frame by frame in the pre-installed Chromium (Playwright): real typography, blur, masks, shadows; about 0.05-0.08 s per frame. Files: `04-styles/editor-showcase-caption-edit-style/references/worked-example-v4/` (`build.py` timeline, `hc/engine.js` 12 components and 6 caption treatments, `hc/render.js`, `boards.py` review boards).
- **Light trim:** 2.6 s removed (one filler + six pause tightenings), each cut verified by transcription.
- **Self-review fixes before showing the owner:** word spacing, deep-green board layering, sentence capitals, last words held at least 0.34 s, small words raised to 56 px, echo restacked.
- **Open:** owner approval of the four boards; then sound (real bank), full render, earshot critique, gate.

## 2026-11-27 (feedback on the redo): "same pattern in every frame", fonts, captions and SFX not liked
**The user's words:** "Then why you edited the previous video? Because I don't like that video. The caption, typographies, subtitles, even fonts also. Also, do not add proper SFX. Also, every frames you did like same pattern using. I don't like that also. So improve your editing skill. Already I provided zip file, right? ... if you have any doubt, ask me now. Also ... before you will do video editing, give me the frames and your plan."
- **Process rule (CLAUDE.md-level):** after a rejection, or whenever the owner asks, send the plan plus storyboard frames and wait for approval before rendering. Added to `CLAUDE.md` Rule 0.
- **Variety rules:** `04-styles/editor-showcase-caption-edit-style/GUIDE.md` 10b (no two neighbouring cards share a layout, 4+ caption treatments, no ghosted words, readable small words, varied real sounds).
- **Gate:** three new sound rows in `pre_edit_gate.py` (no file over 3 uses in a 47 s video, distinct files >= 60 % of cues, synthesised cues <= 20 %). The redo would have failed all three.
- **The owner then named three sound sources** (Openverse, the Real SFX skill, earshot). Checked and saved in `03-sound-type-assets/sound-and-music-design/references/sfx-sources-and-ears.md`: Openverse's anonymous quota was already spent for the container; the Real SFX pack is CC0 but **synthesised** (its manifest says so), 3 of its 12 themes were copied to `assets/uisfx-synth-cc0/`; earshot was code-reviewed, installed in a venv and used to listen: it rated the hand-made cues "likely code-synthesized" and scored the rejected redo against a profile of the four reference reels (music 0 % vs 93 %, longest silent gap 0.42 s vs 0.00 s, 4.7 onsets/s vs 5.8, near-mono, thin low end, dull top; 5 of 49 visual events had no sound).
- **Real sound bank built the same day:** the owner approved registering a free Openverse key (their email; the filter blocked the first attempt, then the same one-line command was run after the owner confirmed the address in chat). 124 real Freesound recordings were collected in 16 roles, ranked by earshot against plain-words descriptions, checked with `realness` (102 real, 17 uncertain, 5 code-made); the best 75 are in `03-sound-type-assets/sound-and-music-design/assets/openverse-real/` (50 CC0, 25 CC BY: credit line needed). Scripts: `06-tools/tools/openverse_token.py`, `openverse_harvest.py`.
- **The owner then forwarded a list of 10 GitHub tools (+1 bonus).** All eight public repos were cloned shallow and read; none installed as a skill (context bloat, Mac-only, overlaps, one licence question): verdicts in `06-tools/EXTERNAL-REPOS.md`. Taken from **Ghost Editor**: the house-look vs components rule and the two-worlds idea (GUIDE 10b rules 8-10, `references/ghost-editor-recipes.md`), a components log (`02-craft/shorts-editing-pro/COMPONENTS-LOG.md`, PRE-EDIT row), 8 CC0 sounds (`assets/ghost-cc0/`), and 51 Mixkit sound ids + 23 music ids (`assets/mixkit-restore-list.json`, `06-tools/tools/mixkit_fetch.py`; the Mixkit files are fetched by id because their category pages are behind a bot check but the preview files are not; 23 fetched and tested). **HyperFrames** (Apache-2.0, needs Node 22 + FFmpeg, both present here) is the candidate upgrade for richer motion cards; a pilot needs the owner's yes.
- **Owner's question: "Why didn't install 3.js and YT DLP and auto editor?"** My skip was a judgement call, and for yt-dlp and auto-editor it was the wrong kind of call (they are tools, adding nothing to context). All three were installed and tested the same day: yt-dlp and auto-editor in a venv (auto-editor cut 0.16 s from a 12.42 s clip; yt-dlp listed a public YouTube video's formats), plus 5 auto-editor skills and 13 three.js skills (22 skills in all, about 2,500 tokens of descriptions per session). Lesson: when the owner forwards a list of tools, install the ones that are tools, explain any that are skipped with a reason that is a fact (licence, platform, safety), and ask before skipping on taste.
- **Three sound skills installed** at the owner's request ("Download these skills also, it will help you for Music and SFX packages"): `.claude/skills/real-sfx` (the owner's uploaded `.skill`, byte-identical to clipwing.pro's, MD5 aebc35ad), `.claude/skills/real-sound` and `.claude/skills/earshot` (both from the earshot repository, MIT). Read before installing: no hidden network or install steps; the only external call is an optional Gemini upload that needs explicit consent. The router and the precedence rules are in `SKILL.md` 6b.
- **Open:** client rules and fonts for this video (owner will say); the no-BGM rule removes the bed the references all have, so a quiet room-tone bed (from the bank) is planned instead.

## 2026-11-27 (redo): the rejected short rebuilt with the new workflow
**The user's words:** "Redo the rejected short with this workflow".
- **Built to the gate:** PRE-EDIT + PLAN, then 9 designed card layers, 6 B-roll clips, 71 sound cues, no music, no grade, captions on the chest (centre 61 %), gate READY (13 MG events, 47 %, HL + MC), -14.0 LUFS. The full record is `04-styles/editor-showcase-caption-edit-style/references/worked-example/` and `02-craft/shorts-editing-pro/LEARNING-LOG.md`.
- **Tool upgrades made while building it:** `caption_moves.py` gained `quote` (HL), `mc` (MC), `tiles` labels, `typecard` heroes / `solid_t` / `release` / `border` / `strike` / `icons` / `bg_alpha`, `--only`; `shortkit.py` gained `anchor_track` (camera follows the speaker) and B-roll `dy`; `pre_edit_gate.py` ignores `txt_` layers and focus-pull `dims`.
- **Open:** client feedback on the redo. The owner's first brief asked for music and a colour grade; the Naveen bro bar says none of either. The redo follows the bar; adding music or a grade is a one-line change.

## 2026-11-27: four editor-showcase references -> P17-P20, a caption-move tool, and one skill folder
**The user's words:** "I dont like this edit, you need to learnt so much edits" (about a 47 s English talking-head short edited in a cloud session on 2026-11-26), then, with four reference shorts and this rulebook as a zip: "Reverse-engineer their caption styles, typography, text animations, motion graphics, transitions, timing, and visual effects. Understand the techniques behind the references, not just their appearance ... Integrate everything into my existing Claude video-editing skill without losing previous learnings."
- **Why the edit was rejected (checked against this rulebook):** it was made without it. Music and a colour grade were added, captions and titles sat above the head, the inserts were stock clips and text, and nothing was designed: the same "text on a talking head" failure as video 25. Logged in `02-craft/shorts-editing-pro/LEARNING-LOG.md`.
- **New style skill:** `04-styles/editor-showcase-caption-edit-style/` (P17 type cards + colour inversion, P18 brand-colour condensed caps + pills, P19 under-chin kinetic captions in one focal zone, P20 script word + small sans). Measured frame by frame: `references/reel-notes-R5-R8.md`, boards in `references/frames/`.
- **What the four share:** captions on the chest at 54-59 % of the height (chin + 17 %), one hero word per card sized to 72-87 % of the width with a tiny lead-in, one accent colour from the footage, a focus pull on every return to the speaker, the speaker shrinking into a card, 7-10 sound events per 10 s. R7 states the rule in its own script: "if you make people's eyes move, you lose their attention".
- **New tool:** `04-styles/editor-showcase-caption-edit-style/tools/caption_moves.py` renders `writeon`, `pill`, `converge`, `typecard` (with `invert` and a speaker `window`) and `tiles` as RGBA frames for shortkit `layers`. Tested through `shortkit.py stills`. Focus-pull return = a `dims` entry with `amt` 1.0 and `blur` 16 (no kit change needed).
- **Gate made stricter:** `pre_edit_gate.py` no longer counts a `layers` entry keyed `txt_` (a text move) or a `dims` entry with `amt` >= 0.99 (a focus pull) as designed MG, so the new text layers cannot pass as motion graphics.
- **Saved also in:** `04-styles/README.md` (P17-P20, next = P21), `04-styles/pro-video-editing/profiles/P17...P20`, `video-styles-atlas`, `shorts-editing-pro` style picker, `01-process/before-edit/1-READ-THESE-SKILLS.md` (A5, C), `2-PRO-MOVE-MENU.md` (three MG kinds, text moves, focus pull), `3-PRE-EDIT-SHEET.md`, `text-animation-moves` (move table), `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md` (four measured rows, the chin + 17 % formula), `skill-saver` map.
- **Structure change:** this rulebook now IS the Claude skill `video-editing-style`. One `SKILL.md` at the root is the entry point; every skill file inside the layers is named `GUIDE.md` (a skill folder may hold only one `SKILL.md`). The earlier five-reel skill is kept whole in `02-craft/event-map-reel-edit-style/references/event-map-method-full.md`; its font-board study is in `05-clients/naveen-bro/mustard-red-caption-style/references/typography-pairings-measured.md`.
- **Cloud notes:** `PATHS-AND-SETUP.md` has a new section (what runs in a cloud session, what does not: no person matte, no Mac asset folders, Pexels blocked).
- **Clashes stated, house rule kept:** keyword timing (references start 6-8 frames early; house rule is never early), hero width (87 % vs the x 120-960 zone). See the new skill, section 9.
- **Open:** the rejected short is not rebuilt yet (do it to the gate, P19 base + object cards, client bar). `caption_moves.py` has no letter-level write-on, no phone bezel and no true scale-down of the footage into a card. Sound kinds in the four references are inferred from measurement, not heard. Ask the owner whether keywords may start early.

## 2026-11-26 (rebuild): video 25 v2 built to the gate
**The user's words:** "Yes, rebuild it / every thing that how pro editor do edit? with every thing brolls, captions, motion graphics and other things needs..."
- **Reference build:** `edits/roughcut3/tools/mg.py` holds 9 designed pieces (MC window behind the head, checklist card x3, syllabus sheet, control bar card, real-page HL, share card with cursor, loop window). It is listed in `01-process/before-edit/2-PRO-MOVE-MENU.md` section 1 as the example to copy from.
- **Gate:** `01-process/before-edit/tools/pre_edit_gate.py` reads `edl["meta"]["mg_events"]` (beats animated inside a scene clip or layer) for the event-gap and pause checks. Video 25 v2: READY (15 MG, 46 %, HL + MC).
- **Kit notes** (`shorts-editing-pro` LEARNING-LOG):
  - move `work/broll/<key>_full` aside after re-rendering a scene under the same key;
  - held UI cards need a slow float, or the scorer sees a freeze;
  - keep the air flick on every hard cut next to designed cues.
- **Closed:** the open item below (video 25 rebuilt, delivered as `Uncertainty_Truth_EN_v2.mp4`).

## 2026-11-26 (feedback): client not impressed by video 25, so a `01-process/before-edit/` gate
**The user's words:** "this is edit not impressed by client i told you use all skills what you learned still now espicially yesterday's learned things. from next time onwards should use perfect skills i mean brolls, motion graphics and other things like pro editor? create a before edit things in folder."
- **New folder `CLAUDE 2.0/before edit/`**, plus CLAUDE.md Rule 0. It holds:
  - the reading list of all skills (yesterday's lessons mapped to edit actions, craft skills required);
  - the pro move menu with floors (designed MG every 8 s, 3+ kinds, >= 25 % of runtime, no 9 s gap, HL + MC, literal B-roll per noun, a sound on every insert);
  - the PRE-EDIT sheet template, the Naveen bro client bar, and the video 25 post-mortem;
  - `tools/pre_edit_gate.py`, the EDL check (video 25: 5 FAIL).
- **Saved also in:**
  - `mistakes-to-avoid` 21b, `my-editing-rules` 11 (MG floor), `aesthetic-pro-reel-edit-style` 3 (floor box);
  - `shorts-editing-pro` workflow step 0 + the gate before the sample render, LEARNING-LOG feedback;
  - `INDEX.md` order step 0, `05-PLAN-TEMPLATE.md` F.
- **Open:** video 25 itself is not rebuilt yet. (Closed the same day: v2, see above.)

## 2026-11-26: video 25 (Uncertainty Truth English): client font pair, no-grade edit
**The user's words:** "dont add bgm and dont add color grading"; "use only best font combination"; "Bricolage Grotesque with Fraunces Soft Italic dont use these use i gaved image ... take best fonts combinations".
- **Client fonts:** ONE carousel pairing. Default is Poppins (SemiBold lead-ins, ExtraBold caps) + Playfair Display ExtraBold Italic; no Bricolage / Fraunces. Saved in `mustard-red-caption-style` 2b, `aesthetic-pro-reel-edit-style` layer 3 and the topic giant, and CLAUDE.md Rule 4.4.
- **No colour grading:** a neutral grade dict with vignette 0 and grain 0 set explicitly. Saved in `aesthetic-pro-reel-edit-style` clashes.
- **Paper scenes:** captions over the shirt stay cream + haldi with the outline. New paper key `stroke` in `shorts-editing-pro/tools/shortkit.py`. Saved in `aesthetic-pro-reel-edit-style` section 3.
- **Artwork plate insert:** a portrait painting shown whole on paper, with the caption in ink below. Saved in `aesthetic-pro-reel-edit-style` section 3.
- **B-roll:** stock titles can lie, so check the frames; on white screens use ink lead-ins. Saved in `broll-library` rules 7-8.
- **Sound:** `fs_181773_48k.wav` is silent; use 2995. Saved in `sound-and-music-design` section 8.
- **shortkit colour fix:** fast swscale rounding plus a truncating LUT darkened every render by about 2.5 luma levels. `SWS` accurate-rounding flags now apply on the source decode, the B-roll prep and the encode, and the LUT rounds, so the round trip is exact (0.00 levels). `video` reuses existing frames, so after a kit-wide change move `work/frames` aside. Saved in `shorts-editing-pro` GUIDE.md rule and LEARNING-LOG.

## 2026-11-25 (end of day): everything stored
**The user's words:** "store skills folder what you learned still now". Today's lessons that were not yet in a skill are now saved:
- **README:**
  - The `pro-font-and-subtitle-guide` row names the placement research.
  - The `text-animation-moves` row now says stacks go on the chest (above the head only as an accent); the same wording is fixed in that skill's description and in CLAUDE.md Rule 1.
  - Known gaps: Telugu script is not used for the client; PDFs can't be read on this Mac.
- **`MAC-TOOLCHAIN.md`:** no PDF reader (no pypdf, no poppler); `brew install poppler` would build from source, so ask first.
- **`sound-and-music-design` section 8:**
  - `~/Desktop/file manager/Sfx /` is empty; UI / typing sounds are in `~/Downloads/ui sfx/`.
  - 125 measured candidates are in `edits/tes2/plan_work/sfx_candidates/wav48/`.
  - The text-move picks are in `text-animation-moves/assets/sfx/`; measure with `sfx_measure.py`.
- **`06-tools/_video-analysis-tools/README.md` step 8:** `/p/<code>/` when the pane is hidden, re-paste after navigation, keep grids inside the viewport, zoom uses screenshot pixels, crop the pro tier of "$5 vs $80" reels, 1/30 s grids for type-on, `RC.cuts` at 10 fps for faceless reels.

**Where today's learning lives:**
| What | Where |
|---|---|
| Text moves, word stacks, a sound per move | `text-animation-moves` |
| Where text goes in a vertical short | `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md` |
| Client rules: subtitles on the chest, 1-3 accents above the head, no Telugu font | `aesthetic-pro-reel-edit-style` rules 8-9, `mustard-red-caption-style` 2c, CLAUDE.md Rule 4.4 |
| shortkit `stacks`, `stack_stroke`, SFX `ss` | `shorts-editing-pro` keys table |
| Telugu script rendering, the toolchain | `MAC-TOOLCHAIN.md`, `pro-font-and-subtitle-guide` section 6 |

## 2026-11-25 (research): where text goes in a vertical short
**The user's words:** "first dont create by you own just research and which is best place to put in shorts in vertical videos", then "also you have seen many short form videos also use that information with this".
- **New reference:** `pro-font-and-subtitle-guide/references/vertical-text-placement-research.md`. It combines three sources:
  - **Platform UI safe zones:** Meta Reels ads 14 / 35 / 6 %; TikTok In-Feed 240 / 660 / 120 px; vendor numbers for ordinary posts and Shorts.
  - **Eye-tracking studies:** Kurzhals et al. CHI 2017 (n = 40: subtitles near the speaker mean less eye travel) and BBC R&D Dynamic Subtitles 2015 (gaze closer to viewers with no subtitles; never cover the mouth).
  - **About 15 short-form reels studied earlier:** Tharun A / B, the motion-graphics library, the P profiles, R4, P6, P8, Ultimate Editors reel 3, the mustard references (Kobe, Raj Shamani, Hormozi), P10.
- **Finding:** with a centred speaker, the running subtitles sit at 55-68 % of the height (median about 63 %), just under the chin. Text above the head is only an accent: hook title, numbers, labels. No studied reel runs its subtitles above the head.
- **Rule now in the skills** (it replaces Claude's own "y 1120 / 2-3 above-head moments" numbers):
  - Subtitle block centre at 58-65 % (y about 1110-1250), its bottom above y 1470, lines within x 120-960, never on the mouth or eyes.
  - Above the head: 1-3 accents per short, below y 270.
  - Beside the face: only with real empty space.
  - Ads: keep the block above y 1250.
- **Updated:**
  - `pro-font-and-subtitle-guide` section 5 + QC;
  - `shorts-editing-pro` caption rule 6 + the safe-zone row (the house centre was y 1150-1300; it is now 58-65 %; the safe zone is now x 120-960, y 270-1470);
  - `text-animation-moves` section 3 + QC;
  - `aesthetic-pro-reel-edit-style` rules 4 and 8;
  - `mustard-red-caption-style` 2c and `client-font-brief.md`;
  - `reel-editing-method` (its behind-head "top 60-90 px" sits inside the top UI band, so it is noted as y 270 or lower);
  - CLAUDE.md Rule 4.4; the shortkit comment.
- **Demo:**
  - The chest stacks are now centred at about 63 %.
  - The above-head accent is one line at y 285; it had been at y 140, inside the top UI band.
  - New overlay check: `text-animation-moves/references/frames/STACKS_safe_zone_check.jpg`.
- **Not read:** the full text of the two studies (the PDF could not be opened on this Mac: no poppler). Their findings are from the abstracts and search summaries.

## 2026-11-25 (feedback): subtitles off the top of the head, no Telugu font
**The user's words:** "dont use telugu font max and full subtitles in upper head looks heavy adjust not all text in upper head. adjust subtitles."
- **Rule: subtitles run in the lower caption zone.**
  - Word stacks default to the chest (top at y about 1120, big words 100-110 px, ratio 0.5, ink outline 3; a red word on the red-checked shirt needs 5).
  - Above the head go only 2-3 moments per 45 s short: the hook, at most one middle moment and the loop line, counting giants, pairings, number giants and stacks together. Each moment is up for 2 s at most, with 2 lines at most, and never two in a row.
  - Saved in `text-animation-moves` section 3 + QC, `aesthetic-pro-reel-edit-style` rule 8 (plus the insert-menu counts and the event grid), `mustard-red-caption-style` 2c, `client-font-brief.md` C and CLAUDE.md Rule 4.4.
- **Rule: no Telugu-script font.** The client's subtitles are Tenglish in Latin fonts; Telugu script only if the user asks for it by name. Saved in `pro-font-and-subtitle-guide` section 6, `mustard-red-caption-style` 2c rule 5, `aesthetic-pro-reel-edit-style` rule 9, `text-animation-moves` rule 10 and CLAUDE.md Rule 4.4.
- **shortkit:**
  - `style.stack_stroke` and per-stack `"stroke"` now also outline the type-on letters.
  - The demo EDL moved to the lower zone. New sheets: `STACKS_test_sheet.jpg` and `STACKS_lower_zone_fullsize.jpg`; the old all-above-head sheet is kept as `STACKS_v1_all_above_head_REJECTED.jpg`.

## 2026-11-25 (latest): text animation moves (learning only, no edit)
The user said "dont do edits now just learn skills", so the gaps between our shorts and the client's references were closed in the skills and tools. Tests are stills only.
- **New skill `text-animation-moves`:**
  - **Measured references:** a "$5 vs $80 edit" pro version (shami.mp4) and a faceless kinetic-type reel (yp.motionstudio), plus the earlier Grind szn reel.
    - Word stacks on alternating sides.
    - A letter-by-letter type-on: 8 letters in 0.37 s.
    - A hard clear at the end of each sentence.
    - Cuts every 0.40 s that speed up towards the end, with grain and slam arrivals.
  - **Rules:** a move menu (cut / fade / blur / rise / grain / pop / type), the stack layout rules, QC and gaps.
  - **Sound per move:** files on this Mac, measured with the new `tools/sfx_measure.py`. Five Mixkit files are copied into `assets/sfx/` with their licence.
  - **Demo:** `tools/stack_demo_edl.json` and its sheet `references/frames/STACKS_test_sheet.jpg`.
- **shortkit:**
  - new `stacks` key: 2-5 line word stack, layout fixed from all tokens, big + small words, center / left / right / stagger, behind the head, ghost, fade-out; captions hide while a stack is up;
  - token fx `type`, `grain`, `rise`, `cut`, `fade`, `blur`, `pop`;
  - SFX `"ss"` slice start.
  - Backup before the change: the scratchpad `shortkit.before_stacks.py`.
- **Linked from:**
  - `aesthetic-pro-reel-edit-style`: a "Word stack" insert row and a sound line.
  - `mustard-red-caption-style` 2c.
  - the `shorts-editing-pro` keys table and LEARNING-LOG.
  - README, CLAUDE.md Rule 1, the skill-saver map.
- **Lint:** OK (36 skills). QUICK-INDEX rebuilt.
- **Lesson:** at camera 1.25 the client's hair top rises to about y 460, so the wall space for stacks is y 100-450.
- **Open:**
  - The ink matte transition, invert-background word scenes and the mask-wipe reveal are not built.
  - The reference reels' sound can't be measured (picture only).

## 2026-11-25 (late night): everything stored
- **`MAC-TOOLCHAIN.md`** (new, top of `skills/`): this Mac's tools in one place, moved from Claude's private notes so the skills hold them too.
  - ffmpeg path, no ffprobe, range-render encode.
  - Render venv versions, packages that can't be installed.
  - Telugu shaping via fribidi, Homebrew building from source on Intel, downloads with curl.
  - Font library, the `.zshrc` fix.
- **`shorts-editing-pro`** shortkit keys table: keyword `"font"` (serif / script / any library file), group `"y"`, `SHORTKIT_LAYOUT=basic`.
- **`06-tools/_video-analysis-tools/README.md`:** how to measure text arrival frame by frame (1/30 s grids, cropped), landscape reels, `RC.cuts` at 8 fps for very short shots.
- **CLAUDE.md:** the mustard line names the font-pairing brief (section 2c); Fast access lists `MAC-TOOLCHAIN.md` and `CHANGELOG.md`.

## 2026-11-25 (night): Telugu script renders (raqm on)
- **Fix:** Homebrew `fribidi` 1.0.18. The user approved full access; it was installed in a terminal tab.
  - Pillow's wheel already bundles raqm + harfbuzz and only looks for `libfribidi.dylib` when it runs.
  - The `libraqm` formula was stopped, because it wanted 36 packages built from source on this Intel Mac (Homebrew has dropped Intel bottles).
- **Proof:**
  - `pro-font-and-subtitle-guide/tools/telugu_check.py` prints raqm True. Its sheet (`references/telugu_shaping_check.png`) shows all 12 Telugu fonts, basic vs raqm.
  - A shortkit still of "కానీ ఎందుకు ఈ / తేడా?" on Pink Tax (`references/telugu_caption_test.jpg`).
- **Library:** 79 files, with new statics Anek Telugu SemiBold / Bold and Noto Sans Telugu Bold (the variable files load thin in shortkit).
- **Findings:**
  - Gidugu and Suranna have no ₹.
  - raqm also kerns Latin text: captions up to 1.6 % narrower. shortkit has a new `SHORTKIT_LAYOUT=basic` switch for partial re-renders of older projects.
- **Updated:**
  - `pro-font-and-subtitle-guide` section 6 + QC.
  - `shorts-editing-pro`.
  - `mustard-red-caption-style` 2c rule 5.
  - README known gaps.
  - FONTS-README.

## 2026-11-25 (later): the client's font-pairing brief (round 4)
- **Brief:** six screenshots of a font-pairing carousel (raktimcreates) and one reel (tobydeboer "Grind szn"), to take "as reference, not like that".
  - Measured in `mustard-red-caption-style/references/client-font-brief.md`.
  - Screenshots in `references/frames/client-font-brief/`.
- **`mustard-red-caption-style` section 2c:** six pairing moments for the client, as two-font titles in the plain wall above the head. One or two pairings per video; M4 stays the running caption.
  - Playfair + Poppins
  - Yellowtail + Anton
  - Inter Tight + DM Serif Italic
  - Instrument Serif + Italianno
  - wide caps behind the head
  - a Pinyon word stack with blur reveal
  - Board on Pink Tax: `references/frames/PAIRINGS_board.jpg` (tool `tools/pairing_board.py`).
- **`pro-font-and-subtitle-guide` section 2b:** the same six pairing recipes as general knowledge for any video.
- **`aesthetic-pro-reel-edit-style`:** "pairing moment" added to the insert menu.
- **Fonts:** 76 files now; new are Italianno, Pinyon Script, Yellowtail, Instrument Serif regular + italic, and a static Playfair Display 800 Italic. None has ₹.
- **shortkit:** keyword `"font"` takes `"script"` (style.script_font) or any library file name. Old EDLs unchanged.
- **Lessons:**
  - Thin scripts are unreadable over the checked shirt, so they only go on plain wall or paper.
  - Wide caps behind the head show only their feet behind the hair.
- **Open:** the client hasn't picked pairings yet; no video sample rendered.

## 2026-11-25: the Naveen bro client's look, fonts for every form, every editing style
**Client request (videos 16-24, Telugu / English shorts):** aesthetic mustard yellow + red subtitles, then "fully advanced pro edits, aesthetic font subtitles like the Instagram channels".
- **`mustard-red-caption-style`** (new):
  - Built from 11 measured YouTube / Instagram references (`references/reference-reels.md`, three research rounds).
  - Four looks:
    - **M4 Haldi-Kumkum** (Claude's own, the default until the client picks): Bricolage SemiBold cream lead-in that ghosts at 30 % and goes solid word by word; a Fraunces Soft Bold Italic haldi keyword; a haldi brush stroke on up to 4 hero words; a kumkum dot full stop.
    - **M1** podcast serif.
    - **M2** golden caps.
    - **M3** film subtitle.
  - Fixed palette: haldi `#E2AA2C`, kumkum `#C8372D`, cream `#F4EFE3`, ink `#1A1410`. Red only on negative words.
  - Tools: `restyle_edl.py` (re-skin an existing EDL to M1-M4), `style_board.py`, `style_frames.py`.
  - Samples: `edits/mustard-red-captions/previews/signature/`.
- **`aesthetic-pro-reel-edit-style`** (new, = **P16**):
  - Built from 11 measured Instagram reels (I1-I11 in `references/instagram-references.md`).
  - What "advanced pro" means in numbers: a cut or punch every 1.9-2.5 s; a text change about every 1 s; two fonts per line; blur-to-sharp word arrival; a literal B-roll per concrete noun; a dark warm grade; one quiet designed insert every 6-8 s.
  - Layer stack, insert menu, 45 s event grid, sound levels and QC.
  - Sample: `Pink_Tax_PRO_sample.mp4`, which the client has not seen yet.
- **`shorts-editing-pro/tools/shortkit.py`**, new optional EDL keys (table in that GUIDE.md, Files section):
  - `style.cap_color`, `style.ghost`, `style.reveal: "blur"`, `style.mono_font`.
  - Keyword `brush` / `dot`.
  - `brackets` with `label`, `shape: "ring"` and `color` (face HUD and ring).
  - `paper` (off-white paper scene with the speaker cut out and a ribbon that draws on).
  - Old EDLs render unchanged.
- **`pro-font-and-subtitle-guide`** (new, always read):
  - Rule of three font families.
  - Fonts picked by video type and by role.
  - A library table with ₹ and Telugu support.
  - Subtitle numbers:
    - Netflix: 42 characters per line, 2 lines, 20 cps in English and 22 cps in Telugu, 0.83-7 s on screen, a 2-frame gap.
    - BBC: 160-180 wpm, 68 % width.
  - Safe zones for 1080x1920.
  - Netflix Telugu rules: no italics, numbers 1-10 in words.
  - Licences, font QC, `tools/specimen.py`.
- **`video-styles-atlas`** (new, always read): one table of every video form with its rhythm, captions, grade, moves, sound, length and deep skill. New sections for the forms no skill covered: vlog, cinematic brand / wedding film, tutorial / SaaS screen recording, ad / UGC, meme / gaming / fan edit, and the cross-form pro rules.
- **`fonts-and-colours/assets/fonts/`** grew to 70 free files (OFL / Apache, 23 licence files):
  - Families: Inter, Archivo (expanded, condensed), Cormorant Garamond, EB Garamond, Cinzel, Atkinson Hyperlegible Next, Caveat, JetBrains Mono, Mea Culpa, Permanent Marker.
  - Telugu: Noto Serif Telugu, Baloo Tammudu 2, Mandali, NTR, Gidugu, Suranna, Hind Guntur, Tiro Telugu, Tenali Ramakrishna.
  - Plus copies of Anton, Poppins and Inter Tight used in earlier edits.
- **`06-tools/_video-analysis-tools/browser_reference_capture.js`** (new): study an Instagram reel or YouTube Short in the built-in browser without downloading it (frame grids, cut count, likes and caption). Linked from `watch`.
- **Structure:**
  - `README.md` rebuilt by category, with the P1-P16 profile map, folder rules and known gaps.
  - This changelog started.
  - `06-tools/tools/build_index.py` checks the structure (all 35 skills pass); the skill-saver map caught up with the 9 skills it was missing.
  - `shorts-editing-pro` style picker gained P16 and the atlas row.
  - CLAUDE.md Rule 1 always-read list gained the fonts guide and the atlas.
- **Open:**
  - Telugu script cannot be shaped: PIL has no raqm. (Fixed the same night with `brew install fribidi`, see above.)
  - Seven fonts lack ₹.
  - The M4 and P16 samples have not been client-approved or checked on a phone.
  - The new paper / HUD / ring inserts have no SFX in the sample yet.
- **Video 24 Pink Tax** delivered, in P8 "X vs Y" with the event-map method.

## 2026-11-23
- shortkit: a second keyword font (`"font": "serif"`), giant strike and font, and one music removal (`music.gaps`).
- Video 23 Uncertainty Truth: Tharun 9:16 grammar with motivational two-voice type.

## 2026-11-22: event-map method, five received skills, Rule 3
- **`event-map-reel-edit-style`** (= **P13** two-tier kinetic talking head and **P14** faceless 2.5D documentary). Built from the "zip 2" pack of 5 reels:
  - Something new every 1.3 s.
  - Every visual caused by a word, and every change has a sound.
  - About 20 transition recipes, chosen by meaning.
  - Used on every short since.
- **Received and stored unchanged**, each with an "On this Mac" section:
  - `ultimate-editors-shortform-style` (= **P15**; its linked brief has not arrived).
  - `ue-sound-design` (three sound families, four passes).
  - `beginner-to-pro-edit-tips` (25 % smaller, fewer effects, dull colours; always read).
  - `watch` (learn a style from a video file).
  - `ae-builder` (After Effects rebuild scripts).
- shortkit gained: the P13 two-tier keyword (role colour, track-in, letter stagger, pivot bar, strike), RGBA layers behind and in front of the speaker, a black-and-white stretch, text outline and panned SFX.
- Promoted to `shorts-editing-pro`:
  - Whisper large-v3 Telugu settings.
  - Designed scenes as B-roll slots.
  - One keyword per caption group.
  - Measure the hair line before placing a giant.
  - A sharp flick on every visible cut.
- CLAUDE.md **Rule 3**: pick skills without being asked; say when a request clashes with a skill before continuing.
- Mac toolchain audit:
  - ffmpeg only through imageio (no ffprobe).
  - A whisper venv.
  - A central fonts folder.
  - `yt-dlp` missing.
- Video 22 Grayscale Tip: the first P13 render.

## 2026-11-21: one folder for skills, one for finished videos
- Folder map: `skills/` and `edited videos by claude/` (numbered folders plus `brain/`). The Downloads copy is now old.
- **`faceless-explainer-reel-edit-style`** (= **P12** editorial cutout explainer), from the "zip 1" pack:
  - Light cutout act, then dark object act.
  - Blur-in two-font captions.
  - Stat wedge.
  - Light-leak flash.
  - Transitions X15-X19.
- **`aasil-khan-longform-edit-style`**: numbers / roadmap / framework long-form (white + navy UI scenes, recap chart, staircase, flash cuts).
- `shorts-editing-pro` promoted:
  - Hero-word timing checked against the voice.
  - Never delete render caches.
  - CRF 19 delivery capped at 20 Mbps.
  - Pexels before Mixkit (Mixkit video is 720p personal-use only).
  - The loop frame.
- Videos 20 Speed Game and 21 Fan Idea (the first Telugu shorts).

## 2026-11-20: learning from training videos
- `pro-video-editing` **P10** amber UI educator and **P11** podcast scene inserts.
- Learning workflow: `pro-video-editing/tools/learnkit` with the lowest-credit pass.
- `tharun-speaks-longform-edit-style` covers 2 videos.

## 2026-11-17: Edit-Kit and the shorts playbook
- **`edit-kit-playbook`** (always read): the 40-skill Edit-Kit vendored unmodified in `07-edit-kit-reference/` and distilled into a router, beat grammar, speech-to-visual map, caption model, motion seam law, cue sync and QA.
- **`shorts-editing-pro`** became the entry point for every 9:16 short, with `tools/shortkit.py` and `LEARNING-LOG.md`.
- `pro-video-editing`: profiles **P6-P9** (violet condensed tips, noir red kinetic, real-estate orange explainer, lime studio personal brand) and the P4 shell layouts.
- Every attached video is edited with all trained skills. Lean edits: no big workflows, and a fresh session per video.
- Videos 18 Go All In and 19 Self Story.

## 2026-11-15 / 16: skills before every edit, analyse then plan
- CLAUDE.md **Rule 1** (read the skills before every edit) and **Rule 2** (`analyze_raw.py` and PLAN.md, with Claude's own ideas, before any edit).
- **`pro-video-editing`**: the "training claude" reference library, `refscan.py` and profiles **P1-P5**.
- `tharun-speaks-longform-edit-style` started.
- `tharun-speaks-edit-style` (measured 9:16 Tharun Speaks look) and `top-editor-styles` (MrBeast, Hormozi, Johnny Harris, Iman Gadzhi, calm).
- 2026-11-16: full autonomy for edits (no approval stops; external stock downloads allowed).
- Videos 16 Uncertainty Short and 17 Embarrassment Short.

## 2026-10 (first set, distilled from `Downloads/claude/Raghu and claude/skills/`)
- **Rules, assets and catalogues:**
  - Rules: `my-editing-rules`, `mistakes-to-avoid`, `fonts-and-colours`.
  - Assets and sources: `broll-library` (272 clips), `png-library` (78), `where-to-find-assets`.
  - Long originals kept as `original-full.md`.
- **Style and method skills:**
  - `motion-graphics-style` (82 reference reels).
  - `reel-editing-method`, `app-product-animation`, `motivational-video-editing`, `client-video-editing-process`, `text-highlight-match-cut`.
  - `youtube-long-video-editing`, `video-intro-design`, `thumbnail-strategy`.
  - `sound-and-music-design`.
  - `06-tools/_video-analysis-tools/` (reference forensics scripts).
- **Process:**
  - `skill-saver`.
  - 2026-10-06: the automatic routine (reference video, then analysis, then the skill; edit, then delivery with notes and code).
- **Videos 1-15:** AI explainers, Mr Unbox client reels, the 20-minute Y2K long-form, the RAG / ML / Day-series long-forms, AI Tech News and the Mini LED reel.
