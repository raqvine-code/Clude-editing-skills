# Web research, 2026-11-17 (label ONL)

**How to read this file**
- Almost every source is a vendor or creator blog. There are no official YouTube, Meta or TikTok numbers for most items.
- Use these figures for platform mechanics only. Deepak's measured references win on style.

## Hooks
- **"Viewed vs swiped away"** (YouTube Studio > Content > Shorts): 70 %+ is strong, 75-80 % a good target. Unofficial. Sources: shortimize.com, vidiq.com, 1of10.com.
- **Stacked hooks:** visual interrupt + spoken promise + on-screen text in 1-2 s is the consensus, with no data behind it (dev.to/bulkdl).
- **Counter-view:** the full arc matters more than the first 3 s (autoclip.dev).

## Pacing
- **Visual change:** every 3-5 s is the common rule (TikTok/Shorts 3-4, Reels 4-5); some say 2-3 s. Vary the interval, since a fixed rhythm gets tuned out (socialync.io, joyspace.ai).
- **Pauses:** cut those over about 0.5 s but keep breaths between ideas (jupitrr.com, 1of10.com). Deepak's reference ref61 is stricter: 0.3 s.
- **Punch-ins:** 10-15 % scale, anchored on sentence starts rather than a timer (socialync.io, vizard.ai).
- **Shorts length:** up to 3 min, square or taller, since 2024-10-15 (9to5google).
- **View counting:** from 2025-03-31 public Shorts views count every play and replay. "Engaged views" (the old metric) still drive earnings (techcrunch). So loop endings raise visible views.

## Captions
- **Convention:** 1-3 words, heavy sans, one highlighted keyword.
- **Vendor test:** +34 % watch time for coloured word-by-word emphasis vs plain captions. Confounded, so low confidence (blitzcutai.com).
- **Academic:** no retention difference for word-by-word captions (par.nsf.gov 10253921, not short-form). Deaf and hard-of-hearing viewers prefer 6-12 word lines.
- **Safe zones** conflict between sources.
  - Shorts: right about 48 px, bottom about 300.
  - TikTok: top 108-200, bottom 250-370, right 120-164.
  - Reels: the audio bar added about 50 px at the bottom in late 2025.
  - Practical union: bottom ≥ 420, top ≥ 210, right ≥ 120.
  - Sources: reap.video, adaptlypost.com.

## Zooms
- 4-frame hard punch with a whoosh vs 12-frame smooth push; there is no tested standard (premierecopilot).
- Too many jump cuts look frantic; hide cuts with zooms or B-roll.

## B-roll
- Cut to B-roll when the speech is concrete. Some say 30-50 % coverage (unsourced).

## Sound
- **Music under voice:** -18 to -25 dB, with dialogue peaks at -12 to -6 dBFS (storyblocks.com).
- **Ducking:** 6-12 dB, attack 30-80 ms, release 250-700 ms. Over-ducking by 15-20 dB on every line is the common mistake (mubert docs).
- **Voice:** about 3:1 compression, about -16 LUFS. Master -14 LUFS / -1 dBTP is the common target (openclip, dev.to).

## Export
- **Spec:** 1080x1920, constant fps, H.264, AAC 48 kHz 192-320k, 8-16 Mbps. Instagram re-encodes everything, and the file cap is 4 GB (argil.ai).
- **Grid crop:** the Reels profile grid crops to 3:4 (1080x1440) since January 2025; the feed shows 4:5. Centre the cover subject.
- **Trial Reels:** shown to non-followers only, so they are a free hook test.
- **Reels length:** sources conflict (3, 15 or 20 min). Reels over 3 min may not be pushed to new audiences (inro.social).

## Older research
- `pro-video-editing/library/shortform-online-research.md` (2026-11-15).
