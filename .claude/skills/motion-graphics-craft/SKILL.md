---
name: motion-graphics-craft
description: Method and reference library for planning, prompting, building, rendering and reviewing code-built motion graphics videos (kinetic-type showreels, one-take UI motion loops, product and brand launch films, concept pieces and data poems, narrative shorts, look-driven pieces such as risograph or engraving) made with HTML, Canvas, WebGL, Three.js, Remotion or HyperFrames and rendered to MP4 at 60 fps. Built from a frame-by-frame review of 242 Claude-made videos on prompt-motion.com, with the original prompts of the 33 best, seven style profiles, a build pipeline recipe (deterministic seek(t), closed-form springs, subframe motion blur, beat-grid audio), a prompt template, a quality checklist and two QC scripts. Use whenever the user wants to make, prompt, storyboard, build, render or critique a motion graphics video, showreel, kinetic typography piece, UI animation, launch film or loop, wants a prompt that gives a distinctive result instead of a generic one, or wants a motion reference analysed.
---

# Motion graphics craft (from 242 reviewed videos)

Evidence base: 242 videos and prompts on prompt-motion.com (Claude Opus 5.5 era, Sep-Oct 2026), all viewed as frame sheets and measured; 72 examined closely; 33 picked. Labels used throughout the references: `[prompt]` = the creator's own prompt says so, `[seen]` = visible in sampled frames, `[measured]` = computed from the files. I did not rebuild the pipelines and I could not hear audio. Verify visual claims against the frame sheets in the pack's `visual-reference/` when it is available.

## Workflow

1. **Choose a profile** (`references/style-profiles.md`): M1 narrative short, M2 concept piece, M3 format-play, M4 type-and-shape showreel, M5 look-driven, M6 one-take UI, M7 launch film. The profile sets length, pace, text amount and prompt style.
2. **Find the one governing idea.** Every strong piece has one: a photon, a point, a poster breaking its frame, a white ball, an orange dot, a medium. If you cannot state it in one sentence, stop and find it before writing anything.
3. **Write the brief** (`references/prompt-patterns.md`). Open brief for M1/M2; one-line rule for M3; named medium for M5; showreel one-liner plus one decisive constraint for M4; the structured template (`<inputs> <direction> <structure> <build> <gotchas> <start>`) for M6/M7 or anything that must be polished and loopable. Add a **Banned:** list.
4. **Plan the beats before code.** Fix a tempo and count beats when music is involved ("120 BPM, 54 beats, something happens on every beat"). Write each beat as what physically becomes what. Show the beat map and four stills to the user before the long render.
5. **Build deterministically** (`references/techniques.md` section 1): every frame a pure function of time in `seek(t)`; closed-form springs; one camera transform with log-space zoom; real assets, never placeholders.
6. **Link scenes by transformation, not cuts** (`techniques.md` section 2): morph, flood-and-contract (overscale past the corners, about 0.3 s), shared-element handoff, iris, match cut. Hard cuts only on beats.
7. **Sound**: analyse the track (tempo, grid, drop); sound effects as real recordings placed by measured peak; normalise near -14 LUFS; licensed audio only.
8. **Render with subframe motion blur** (3-16 Playwright subframes per frame blended with `ffmpeg tmix`; 8 is a good default for fast moves).
9. **QC** with `scripts/qc_render.py` (pops, loop boundary, loudness) and `scripts/contact_sheet.py` (frame grid plus a 70 ms burst), then go through `references/quality-bar.md`.

## Rules that held across the best pieces

- One accent colour or one medium for the whole piece; neutrals chosen on purpose.
- Something happens on every beat; no hold over about one second unless it is a designed rest; no dead time.
- Springs with a tiny overshoot at most; two edges on two springs for stretchy UI; squash on impact.
- Hero objects never teleport. The first and last frame match if it loops, cursor and speed included.
- Short text, set against a counter-weight (serif italic against grotesk). Do not put full stops on screen text.
- No corner furniture (labels, timecodes, tick marks) unless it is the idea; it is the most visible sign of generic showreel output.
- Treat glows, particle bursts, lens flares and crossfades as decisions, not defaults.
- A prompt that only says "make a showreel" gives the generic look: 28 entries share one prompt and only a few stood out, by carrying one idea to the end.

## Numbers worth knowing [measured]

| | All 242 | 33 picks |
|---|---|---|
| Median length | 20 s | 29 s |
| At 60 fps | 57 % | 67 % |
| Median frame-to-frame change | 2.0 | 3.1 |
| Static share of the time | 7 % | 3 % |
| Sudden jumps (cuts, flashes) per 10 s | 6.9 | 5.0 |
| Has an audio track | 210 / 242 | 33 / 33 |

Per profile: M1 narrative 0.4 jumps/10 s; M2 2.3; M3 12.5; M4 20; M5 4.3; M6 2.1; M7 13.9 (see `style-profiles.md`).

## Files

| File | Use it for |
|---|---|
| `references/style-profiles.md` | Choosing and executing M1-M7, with exemplars and measured figures |
| `references/techniques.md` | Build pipeline, transitions, type, camera, motion feel, look systems, sound, loops, gotchas, bans |
| `references/prompt-patterns.md` | What prompts people wrote, five patterns, the structured template with a fill-in version |
| `references/quality-bar.md` | How the picks were chosen, weaknesses seen, delivery checklist |
| `references/picks.md` | The 33 picks with their original prompts, verbatim |
| `scripts/qc_render.py` | Report resolution, fps, audio, loop-boundary difference, loudness, candidate single-frame pops (optionally saves a strip per candidate) |
| `scripts/contact_sheet.py` | Timecoded contact sheet of a video, with an optional 6-frame burst at 70 ms steps |

The pack this skill shipped in also holds `data/` (all 242 entries with prompts, measurements and my grades), `visual-reference/` (frame sheets) and `tools/` (a script to refetch and re-measure the whole collection). The skill works without them.

## Limits

- Judgements about look and pacing come from sampled frames and frame-difference measurements. Re-view a reference before copying a detail, and do not claim to have heard anything.
- Technical recipes marked `[prompt]` are the creators' statements; test them before relying on them.
- Videos and prompts belong to their creators. Use the patterns, not the pieces; keep any copies for your own study.
- Entry-level grades are one reviewer's judgement.
