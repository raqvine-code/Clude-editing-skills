---
name: where-to-find-assets
description: Use when a script line needs an asset the local B-roll/PNG libraries lack, when stuck for a visual idea, or when asked "where do I get X" (footage, SFX, music, fonts, vectors, real photos/documents for news videos). Deepak's fixed website list plus decision tree and worked sourcing procedures.
---

# Asset sourcing (Deepak's fixed list)

Rule: do not use 30 sites each time; recommend only from this list, in decision-tree order. (2026-09-29)

## Step 0: local first
Search `broll-library` and `png-library` for a Pro asset. Go online only if nothing local fits or only usable/avoid items fit.

## Decision tree
- Don't know what to do -> Behance (find a concept)
- Know concept, not the motion -> LottieFiles / Mobbin
- Need footage -> Pexels / Mixkit
- Need SFX -> Mixkit / Freesound
- Need graphic/vector -> Freepik / Figma
- Then CapCut to build the edit.

## Site list (first = default)
- Ideas: Behance, Dribbble, ArtStation, Motionographer, Awwwards
- Motion references: LottieFiles, Mobbin, Page Flows, Figma Community
- Free assets: Mixkit, Motion Array Free, Freepik, Videvo, Videezy
- B-roll: Pexels, Pixabay, Coverr, Dareful
- SFX: Mixkit, Freesound, Pixabay
- Music: YouTube Audio Library, Pixabay, Mixkit
- Design: Google Fonts, Fontshare, Figma Community

## Recommending a download
Give: the site; exact search terms (e.g. `indian student laptop night`, `vertical`); what to pick (9:16 if possible, 1080p+, no watermark); where to save (B-roll -> `brolls for claude/`, images -> `png for claude/`), then catalog via `skill-saver` section 4.

Decided (user, 2026-11-14): source SFX/BGM from Mixkit / Freesound / Pixabay (free). This overrides the Epidemic Sound line in `my-editing-rules`; do not suggest Epidemic Sound unless asked.

## Pexels workflow (video 13 v2, 2026-10-13)
- Search in the built-in browser with a JS helper: fetch `/search/videos/<q>/?orientation=landscape`, collect `/video/<slug>-<id>/`, fetch each page and regex the `videos.pexels.com/video-files/<id>/...mp4` renditions.
- Prefer the `uhd_2560_1440` (or 2732x1440) rendition; it matches our output height.
- Download with curl from `videos.pexels.com` (`pexels.com/download/video/<id>/` 302-redirects to the default file).
- Review cheaply: poster images (`images.pexels.com/videos/<id>/...jpeg?w=480`) on one contact sheet, then 6 frames per downloaded clip to pick in-points.
- Licence: free commercial use, no attribution; still log IDs and in-points. Prefer Indian people for lines about Indian students, teachers, founders.

## Real photos, footage, documents for news videos (AI Tech News ep 02 v2, 2026-10-16)
- Preference order: primary source (government page, company post/report, court filing) -> public-domain official media (White House, DOJ/FBI, ODNI, NASA, NOAA, US Space Force) -> CC BY -> CC BY-SA (credit all). Never use deepfakes, AI images or "photo illustrations" as real visuals.
- Wikimedia Commons API (python urllib, descriptive User-Agent, 1.5 s between calls, back off on 429): person lead photo = Wikipedia `prop=pageimages&piprop=name`, then Commons `prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=1600` for `LicenseShortName`, `Artist`, date. Event photos: list a dated category and filter by White House filename date `P2026MMDD`. Commons also hosts public-domain White House videos (.webm).
- White House videos carry a "TEXT POTUS" banner in the bottom 15%: crop `1632:918:144:0` before scaling.
- DOJ press releases include FBI evidence photos (public domain). justice.gov blocks curl: load in puppeteer and save every `<img>` via in-page `fetch()` (`grab_imgs.js`).
- Agency portraits (ODNI, cabinet) are public domain; TechCrunch's Flickr is mostly CC BY 2.0 for tech executives; Bollywood/Tollywood stars usually have CC BY / BY-SA event photos.
- Document page captures: `capture2.js url "phrase1||phrase2" out.png` returns rects for each phrase after one scroll; `TOPY=n` puts the first phrase at y=n so it fits the 900 px viewport; image px = CSS px x 2.
- Avatar faces: square crops with head and a little shoulder (side about 0.75-0.9 of portrait width), verified on one sheet of circles before rendering (`faces.py`).


Full original notes (every detail, uncut): `_archive/original-full/where-to-find-assets.md` in this folder.
