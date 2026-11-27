---
name: beginner-to-pro-edit-tips
description: Use on EVERY edit that has graphics or animation (reels, long-form, intros, thumbnails), while designing and again in final QC - three rules heard in the user's training video of 2026-11-22 - (1) stop oversizing, make every element 25 % smaller, (2) stop overusing effects, keep them for the elements that must grab attention, (3) use dull colours, no harsh black, harsh white or bright red. Trigger words - looks amateur, looks beginner, too big, too many effects, harsh colours, premium / high-end look, "beginner to pro".
---

# Beginner to pro: three rules for every animation

**Source:** the user's training video, 2026-11-22: "listen words carefully for editing tips". Two files with the same script: the raw talking head `~/Downloads/3 things from beginner to pro.mp4` (76.3 s) and the finished reel `~/Downloads/WhatsApp Video 2026-11-22 at 16.40.13.mp4` (49.75 s). Both are another creator's work: study only, never reuse the footage (CLAUDE.md Rule 1.6).
Word-for-word transcript of both: `references/transcript.md`. How the finished reel itself follows the rules: `04-styles/ultimate-editors-shortform-style/references/reference-reel-3-mistakes.md`.

Labels: **Heard** = said in the video. **Measured** = numbers from the finished reel. **Claude** = my way of applying it, not said in the video.

## Rule 1: stop oversizing everything
- **Heard:** the biggest beginner sign is huge icons and huge shape layers. Rule of thumb: next time, make every element 25 % smaller.
- **Measured (the reel does it):** the coloured keyword is only 3.7-4.5 % of the frame height over the speaker and 6.5 % on a full-screen scene; the plain line is about half of that; UI pills are about 29 % of the frame width; cards leave wide empty margins.
- **Claude, how to apply:**
  1. Lay out the scene at the size that feels right, then scale every icon, shape layer, card, UI panel and sticker to **0.75x** and re-centre. Compare both in one still; keep the smaller one unless something becomes unreadable on a phone.
  2. Empty space is part of the design: at least 8 % of the frame width free on each side of a full-screen scene.
  3. Scope: the video said icons and shape layers "in an animation". Caption and headline sizes still come from the chosen style. If that style has one giant element (behind-subject headline, giant keyword), that is the only oversized thing in the scene; everything else gets the 0.75x pass.
  4. Floor: never shrink below what reads on a phone (use the style's minimum; if none, text x-height 1.5 % of frame height).

## Rule 2: stop overusing effects
- **Heard:** less is more. The less an effect is used, the more special it is. Reserve visual effects for the elements that really need to grab attention.
- **Measured:** in 49.75 s the reel uses one soft blur-in for all text, one particle burst (once, on the "25 % smaller" moment), glow only on the coloured keyword, no shake, no glitch, no flash train.
- **Claude, how to apply:**
  1. Name the ONE element per scene that must grab attention. Only it may get a "special" effect (glow, particles, shake, glitch, flash, 3D spin, speed ramp). Everything else moves with plain position / scale / opacity / blur-in.
  2. Budget: one special effect per section, and the same special effect at most once per 30 s. A second use needs a reason written in PLAN.md.
  3. This does not lower the event rate. "Something new every 1.3 s" (`event-map-reel-edit-style`) stays; a new event can be a word, a card or a camera move. New event is not the same as new effect.
  4. Sound follows the same idea: risers and hits only where the viewer should feel a build (`ue-sound-design` Pass 3).

## Rule 3: use more dull colours
- **Heard:** beginners always use harsh blacks, harsh whites and bright reds. Luxury brands use dull colours, dull blues and dull greens. Duller colours always look more high-end.
- **Measured:** background off-white `#F0EEEA` (not `#FFFFFF`), dark scenes are deep navy `#0B1E34` (not `#000000`), the "mistake" red is `#D24E5A` (not `#FF0000`), one accent blue `#3D77F3` for every keyword.
- **Claude, how to apply:**
  1. No fill, background or large text in pure `#000000`, pure `#FFFFFF` or pure `#FF0000`. Swap to the nearest dull version: black to a tinted near-black (`#0E1418`, `#0B1E34`), white to a warm off-white (`#F0EEEA`, `#F5F3EE`), red to a dulled red (`#D24E5A`, `#C8483F`).
  2. Keep saturation of any large area under about 75 %; only the single accent may be the most saturated colour in the frame.
  3. One accent colour per video, taken from `fonts-and-colours` (change it per video as that skill says); neutrals carry everything else.
  4. Premium topics (money, brands, luxury, career): reach for dull blue or dull green first.
  5. Small white caption text over video may stay near-white (`#F7F7F5`) for legibility.

## Final QC (add to the export check of every edit)
- [ ] Sizes: one still per graphic scene; nothing is larger than it needs to be; the 0.75x pass was tried on every icon, shape, card and UI panel.
- [ ] Effects: for each scene, one named attention element; special effects counted and inside the budget.
- [ ] Colours: sampled the frame; no pure black, pure white or pure red in fills or backgrounds; one accent.

## When another skill disagrees (tell the user before continuing)
- A style with huge type everywhere (some MrBeast / Hormozi looks in `top-editor-styles`) goes against Rule 1.
- A brief asking for "more effects" or an effect on every cut goes against Rule 2.
- A palette built on pure black + pure white + bright red (some P-profiles, for example noir red) goes against Rule 3.
In each case say which rule the request breaks and ask whether to follow the style or the rule.
