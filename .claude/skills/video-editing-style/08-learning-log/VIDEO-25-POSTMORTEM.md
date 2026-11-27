# 5. Post-mortem: video 25 "Uncertainty Truth English" (client not impressed, 2026-11-26)

## What the gate says (run afterwards, `tools/pre_edit_gate.py edits/roughcut3/edl.json`)
| Check | Video 25 | Floor |
|---|---|---|
| Designed motion graphics | 4 (2 paper, 1 artwork plate, 1 ring) | >= 7 |
| Share of runtime | 11 % | >= 25 % |
| Longest stretch with none | **17.8 s (0-17.8: the whole setup)** | <= 9 s |
| Text highlight / match cut | none / none | 1 + 1 |
| Footage B-roll | 11 stock clips, 34 % | ok |
| Fonts / placement / sync / loudness | all fine | ok |

It was a clean **text-on-a-talking-head** edit: 36 caption groups, 3 stacks and 1 giant, with stock clips between them. That is `mistakes-to-avoid` 16, the same mistake as video 13 ("you just added the text and basic sound effects"). With no music and no grade, nothing else carried the energy.

## Line by line: what a pro edit would have built
| t | Words | Video 25 did | Should have been |
|---|---|---|---|
| 0-2.6 | "Uncertainty is the only universal truth" | title stack above the head | the same title + a designed object in the first second (MC flash of 5-7 "uncertain" images behind the pinned word UNCERTAINTY: dice, forecast, a fork in the road, a chart, a coin toss) |
| 2.6-15.2 | "guarantee, secure job, what people say is fixed, blueprint of tomorrow... everyone wants everything predictable" | 5 stock clips + captions | **list device:** a cream checklist card (`dims` behind it) ticking each item on its word with a tick sound, "predictable" typed on; the stock clips as small windows inside the card |
| 15.8-18.6 | "But the truth is, my friend" | ring | the checklist falls / gets crossed out (contrast state change) + ring |
| 18.8-23.4 | "life isn't an exam syllabus where you know... the questions" | exam stock + crumple stock | a designed exam paper: syllabus lines with a big "?" where the questions should be (full-screen off-white scene) |
| 23.8-28 | the thesis again + "no life is truly..." | paper scene + ocean | paper scene + MC on "uncertainty" (callback of the hook) |
| 33.2 | "But that isn't true" (the turn) | neg flash | light-leak flash + the biggest device of the second half |
| 38.4-40.3 | "Even in Bhagavad Gita it is said that" | artwork plate | plate + **HL**: the verse (BG 2.47, transliteration + English) on the page, haldi brush under the spoken words |
| 40.6-42.6 | "focus on your action, not the outcome" | caption brush + strike | **contrast-pair object**: two cards, ACTION lit and moving, OUTCOME greying and sliding out of reach |
| 43-46 | "control was never in our hands" | sand stock | sand + B&W stretch (`desat`), the loss beat |
| 49.8-51.4 | "share it with someone" | phone stock | a designed share / DM card (UI pill over a dimmed band, `app-product-animation` motion), not stock |
| 51.4-55.7 | CTA + loop | captions | an object behind the head on "control", then the loop back to the frame-0 title |

## Why it happened (process, not taste)
1. I read the rule skills and skipped the craft skills (`motion-graphics-style`, `text-highlight-match-cut`, `video-intro-design`, `app-product-animation`, `client-video-editing-process`): `mistakes-to-avoid` 21d.
2. B-roll became the answer for every line; the speech -> visual map never asked "which line becomes a built scene?".
3. No count of designed MG before rendering; the QC numbers I checked (sync, loudness, colour) were all about polish, not substance.
4. No reference research for the scene types (`mistakes-to-avoid` 21a).
5. The skipped `my-editing-rules` 11 (HL + MC in every plan) had the perfect place in the Gita quote.

## Never again
`01-process/before-edit/` (this folder) runs first. `PRE-EDIT.md` holds the motion-graphics plan, and the gate must say READY on the draft EDL before any full render.

## The rebuild (v2, same day)
Built exactly from this table, in `edits/roughcut3/tools/mg.py`; the gate gave READY before the full render.
- **Hook:** MC window behind the head.
- **List:** checklist card with a video window, ticks, bloom, and the strike-out on "but the truth".
- **"life isn't an exam syllabus":** a syllabus sheet with a "?" stamp.
- **"under control" / "isn't true":** a bar card that fills, then fails.
- **Gita:** the real-page HL.
- **CTA:** a share card with a cursor.
- **Loop:** the window returns.
- **Result:** gate 15 MG, 46 % of runtime, HL + MC; delivered as `Uncertainty_Truth_EN_v2.mp4`.
- **Not used from the table:** the B&W stretch (skipped so nothing reads as grading); the contrast-pair cards for action / outcome (the HL page carries that line).
