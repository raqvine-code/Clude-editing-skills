---
name: thumbnail-strategy
description: Use when making, improving, reviewing or A/B-testing a YouTube thumbnail for Tech Boy Deepak, pairing title + thumbnail, or fixing low CTR. Covers glanceability, focal points, face/gaze, separation, light/dark colour, text, the 1+1=3 information gap, six formulas, honest 30 s payoff and a mobile feed QA test.
---

> **Scope: mixed. Written for the Tech Boy Deepak channel; the principles (glanceability, focal point, face / gaze, title + thumbnail pairing, CTR) are general.**

# Thumbnail strategy

Source: ref61, HimanshuG "Science Behind Thumbnails That Actually Work" (2026-10-04, Hindi, English auto-translation). Video itself could not be downloaded (403), so only its thumbnail was studied (`refs/ref61_himanshug_click_science.jpg`). A thumbnail is one half of a sentence; the title is the other half. Its job is to stop the right viewer, and the video must keep the promise.
Full notes from that video (glanceability timeline, saccades, light/dark mode, 3-variant process, feed test): `principles.md`.

## Viewer decision timeline (why the rules exist)
- ~13 ms: gist (Potter/MIT research) -> subject must read as a silhouette.
- 17-50 ms: complexity filter, chaos = skip -> few elements, flat background.
- 100-150 ms: emotional hook from contrast, faces, background tone -> strong expression and contrast.
- 300-500 ms: title is read, decision made -> title finishes the image's thought.

## Rules
1. One idea readable in 0.5 s; describe it in 5 words before designing.
2. One dominant focal point; two is the storytelling sweet spot; never more than three (more = higher cognitive load, CTR falls).
3. Two focal points follow left -> right zigzag: first big and sharp (hook), second gives context.
4. Place focal points and eyes on rule-of-thirds / golden-ratio intersections, not dead centre.
5. Face = emotion engine: one clear, exaggerated but honest expression, sharp eyes, gaze toward the second focal point or text, face at least 30-40% of frame height.
6. Separate subject from background: rim light/glow, darker or blurred background, outline/cutout, complementary colour.
7. Text optional, 1-4 words, never repeats the title, heavy sans or handwritten, readable at 168 px wide.
8. 1+1=3: thumbnail gives feeling/question, title gives reason/stakes. Same info in both = no gap.
9. Curiosity must be honest; pay off thumbnail + title in the first 30 s of the video.
10. Colour: complementary, split-complementary or triadic, one accent reserved for the focal point.
11. Test on both white and near-black feeds (`scripts/feed_test.py`); creator claims mode can swing clicks about 20% (untested). Avoid near-white edges that merge into light mode.
12. Make 3 variants changing one variable each (expression, colour, text, crop); use YouTube Test & Compare. (Creator spent ~Rs 50,000 testing 3 variants on 10-15 videos.)
13. Keep bottom-right (duration badge) and bottom edge (progress bar) clear; nothing critical in outer 5%. (Strategist addition.)
14. Gaze steers attention; keep 1-2 constants (face position, accent colour, type) across the channel; for Deepak's students use concrete stakes (Rs figures, LPA, college/exam names, AI tool logos) as second focal point or the one word of text. (Strategist additions.)

## Six formulas (pick one first)
| Formula | Thumbnail | Title | Deepak fits |
|---|---|---|---|
| Action -> consequence | small mistake/action | cost or stake | resume mistake, wrong branch |
| Reaction face | shocked/confused face makes the gap | plain topic | AI news, salary reveals, launches |
| Before/after | split-screen transformation | adds time frame or method | fresher -> 12 LPA |
| Paused peak moment | frame frozen at climax (Sourav Joshi) | sets up moment | vlogs, unboxing, results |
| Cinematic shocker | one striking high-production visual | context | big explainers (Y2K, AGI) |
| Minimal visual story | almost no text, one odd image (Veritasium) | carries meaning | concept explainers |

## Ref61 thumbnail reading
Two focal points: glowing yellow vial (left, foreground, brightest) then raised-brow face (right third, eyes on upper-third line). Yellow vs teal/blue = complementary separation. Two handwritten white words with an arrow to the vial. Title gives honest context = 1+1=3. Feed test: at 168 px only the header, vial and face survive (stat chips become texture); blur copy still shows vial winning; in light mode its white/grey vignette edges lose the frame, in dark mode it pops.

## Workflow
1. Pick the one promise the video delivers in its first 30 s.
2. Write the title, choose a formula, write 0-4 words of text so title + thumbnail = 1+1=3.
3. Sketch 3 concepts as: focal 1 -> focal 2 -> emotion -> text.
4. Build: cutout, glow/rim separation, simplified background, accent on focal point, text on the gaze line.
5. Run QA, export 3 variants.
6. Check the first 30 s pays off the thumbnail; if not, change the thumbnail, not the truth.

## QA checklist
- `python3 scripts/feed_test.py thumb.png`: view 168 px and 320 px on light and dark; name subject and emotion in under 1 s.
- Squint/blur test: focal point still wins.
- 1-2 focal points (3 max); text <= 4 words, not a title copy.
- Title + thumbnail form one sentence with a gap answered in 30 s.
- Bottom-right clear; 1280x720, 16:9, under 2 MB, sRGB.
- Title/metadata in pure English (Deepak's rule, 2026-10-05).
- 3 variants ready for Test & Compare.


Full original notes (every detail, uncut): `_archive/original-full/thumbnail-strategy.md` in this folder.
