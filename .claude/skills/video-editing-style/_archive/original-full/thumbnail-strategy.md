---
name: thumbnail-strategy
description: How to plan, design, critique and A/B-test YouTube thumbnails for Tech Boy Deepak like a click strategist, not just a designer — glanceability (the ~0.5 s decision), one dominant focal point (max 2–3), face emotion and gaze, contrast and subject separation, colour harmony that survives light AND dark mode, 1–4 words of readable text, the thumbnail+title "1+1=3" information gap, the six thumbnail formulas (action→consequence, reaction face, before/after, paused peak moment, cinematic shocker, minimal visual story), honest curiosity (pay it off in the first 30 s), and a mobile-size QA test. Use for any "make/improve/review my thumbnail", "which thumbnail is better", title+thumbnail pairing, CTR problems, or A/B test variants.
---

# Thumbnail strategy

Source: ref61, HimanshuG "Science Behind Thumbnails That Actually Work" (2026-10-04, 14:46, Hindi; analysed from the English auto-translated transcript and the video's own thumbnail at `refs/ref61_himanshug_click_science.jpg`). The video file could not be downloaded (YouTube 403), so on-screen example thumbnails were not studied. Full notes are in [principles.md](principles.md).

A thumbnail is not a poster. It is **one half of a sentence**: the title is the other half. Its only job is to make the right viewer stop scrolling, and the video must then keep the promise.

## The decision the viewer makes (why every rule below exists)

Creator's model, built on Mary Potter's MIT work on rapid scene recognition (the 13 ms figure is from that research; the later stages are the creator's framing):
1. **~13 ms:** the brain gets the gist (a face, a car, a lab). → *The subject must be recognisable as a silhouette.*
2. **~17–50 ms:** a complexity filter. Too chaotic means skip. → *Fewer elements, flat background.*
3. **~100–150 ms:** an emotional hook fires on high-contrast things like faces and background tone. → *Strong expression, strong contrast.*
4. **~300–500 ms:** they read the title, the context closes, they decide. → *The title finishes the thought the image started.*

## Rules

1. **One idea, readable in half a second.** If you need to explain the thumbnail, it fails. Describe it in 5 words before designing.
2. **One dominant focal point. Two is the sweet spot for storytelling. Never more than three.** Every extra focal point adds cognitive load, and CTR drops as impressions grow.
3. **Two focal points follow the eye: left → right, zigzag.** First point is big and sharp (the hook), second gives context. In ref61 the glowing vial (foreground, left) comes first, then the creator's face (right), then the title.
4. **Put focal points on rule-of-thirds or golden-ratio intersections**, not dead centre by default. The eyes and the object of interest should sit on power points.
5. **Face = emotion engine.** One clear, exaggerated but honest expression (shock, confusion, smug, worried). Eyes visible and sharp. **Gaze points at the second focal point or the text,** because viewers follow eye direction. Big face: at least ~30–40 % of frame height.
6. **Separate the subject from the background:** rim light or glow, a darker or blurred background, an outline or cutout, and complementary colour between subject and background. If the subject and background share a tone, it vanishes at mobile size.
7. **Text is optional, at most 1–4 words, and must never repeat the title.** Text adds what the image can't say (a feeling, a number, a stake). Heavy sans or handwritten, high contrast, readable at 168 px wide.
8. **1+1=3: thumbnail and title carry different information.** The thumbnail gives the feeling or question; the title gives the reason or the stakes. Bad pairing: title "How I bought my house at 22" + thumbnail text "Bought my house at 22" = 1+1=1, no gap.
9. **Curiosity must be honest.** A gap the video really answers is information asymmetry; a gap it never answers is clickbait. **Pay off the thumbnail + title within the first 30 seconds** of the video, or retention collapses and trust drops.
10. **Colour: complementary, split-complementary or triadic,** with one accent colour reserved for the focal point. Avoid many saturated colours that compete.
11. **Design for both light and dark mode.** Most designers work in dark-UI apps, but many viewers are in light mode. Test on white AND near-black backgrounds (`scripts/feed_test.py`). A thumbnail whose edges fade into one mode loses its frame.
12. **Never upload one thumbnail. Make 3 variants** that change one variable each (expression, colour, text, or crop), and use YouTube's built-in Test & Compare.
13. **Keep the bottom-right corner clear** (the duration badge covers it) and don't put key text along the very bottom edge (progress bar on watched videos). *(strategist addition, not from ref61)*

## The six formulas (pick one before designing)

| Formula | Thumbnail does | Title does | Fits Deepak topics like |
|---|---|---|---|
| **Action → consequence** | Shows the small mistake or action | States the cost or stake ("lost ₹5 lakh") | "This one resume mistake…", wrong branch choice |
| **Reaction face** | Shocked or confused face creates the gap by itself | Can state the topic plainly | AI news, salary reveals, new model launches |
| **Before / after** | Split-screen visual transformation | Adds **time frame or method** ("in 90 days", "using only free tools") | Fresher → ₹12 LPA, beginner → developer |
| **Paused peak moment** | Frame frozen at the climax, so it feels like hitting play continues it (Sourav Joshi style) | Sets up the moment | Vlog-style, unboxing, results day |
| **Cinematic shocker** | One striking, high-production visual that stands out from the feed | Context | Big explainers (Y2K, AGI) |
| **Minimal visual story** | Almost no text, one strange image (Veritasium style) | Carries the meaning | Science/concept explainers |

## Workflow

1. Read the script and pick the **one promise** the video truly delivers in its first 30 s.
2. Write the title first, then choose a formula, then write the thumbnail's 0–4 words so title + thumbnail = 1+1=3.
3. Sketch 3 concepts as one sentence each: *focal point 1 → focal point 2 → emotion → text*.
4. Build: subject cutout, separation (glow or rim light), background simplified, accent colour on the focal point, text placed on the gaze line.
5. Run the QA below, then make 3 A/B variants (change one variable each).
6. Check the video's first 30 s actually pays off the thumbnail. If not, change the thumbnail, not the truth.

## QA checklist (run on every thumbnail)

- [ ] `python3 scripts/feed_test.py thumb.png` → look at the 168 px and 320 px versions on light and dark backgrounds. Can you name the subject and emotion in under 1 s?
- [ ] Squint test / blur test: does the focal point still win?
- [ ] Count focal points: 1–2 (3 max).
- [ ] Text ≤ 4 words, readable at 168 px, and not a copy of the title.
- [ ] Title + thumbnail read as one sentence with a gap; the gap is answered in the first 30 s.
- [ ] Bottom-right corner clear; nothing critical on the outer 5 %.
- [ ] 1280×720, 16:9, under 2 MB, sRGB.
- [ ] Title and metadata in pure English (Deepak's English-only metadata rule, 2026-10-05).
- [ ] 3 variants exported for Test & Compare.
