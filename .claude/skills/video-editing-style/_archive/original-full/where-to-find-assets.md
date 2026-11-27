---
name: where-to-find-assets
description: Deepak's fixed list of websites for finding editing ideas, motion references, free assets, B-roll footage, SFX, music, fonts and vectors, plus the decision tree for which site to open. Use whenever a script line needs an asset the local B-roll/PNG libraries don't have, when stuck on a visual idea, when asked "where do I get X", or when recommending a download.
---

# Asset Sourcing — Deepak's website library

**Rule: don't use 30 websites every time.** Only recommend sites from this list, in the order the decision tree gives. — `(2026-09-29)`

## Step 0 — check the local kit first
Before going online, search `broll-library` and `png-library` for a ⭐ Pro asset. Go online only when nothing local fits, or when only ✅/⛔ assets fit.

## Decision tree

```
"I don't know what to do here."          → BEHANCE — find a visual concept
"I know the concept, but how should it move?" → LOTTIEFILES / MOBBIN
"I need actual footage."                 → PEXELS / MIXKIT
"I need an SFX."                         → MIXKIT / FREESOUND
"I need a graphic/vector."               → FREEPIK / FIGMA
                    ↓
                 CAPCUT → build the edit
```

## The library

| Need | Sites (first = default) | Use it for |
|---|---|---|
| 🧠 **Ideas** | Behance, Dribbble, ArtStation, Motionographer, Awwwards | Visual concepts, layouts, styles when the idea is unclear |
| 🎬 **Motion references** | LottieFiles, Mobbin, Page Flows, Figma Community | How an element should animate: UI flows, icon motion, app screens |
| 📦 **Free assets** | Mixkit, Motion Array Free, Freepik, Videvo, Videezy | Templates, overlays, motion elements, vectors |
| 🎥 **B-roll** | Pexels, Pixabay, Coverr, Dareful | Real footage |
| 🔊 **SFX** | Mixkit, Freesound, Pixabay | Whooshes, pops, clicks, risers |
| 🎵 **Music** | YouTube Audio Library, Pixabay, Mixkit | Background music |
| ✍️ **Design** | Google Fonts, Fontshare, Figma Community | Fonts, text styles, design files |

## How to recommend a download
When a script line has no good local asset, give:
1. **Site** (from the table, following the decision tree).
2. **Exact search terms** to type (e.g. `indian student laptop night`, `vertical`).
3. **What to pick:** vertical 9:16 when possible, 1080p or higher, no watermark (the professional-first rule in `my-editing-rules`).
4. **Where to save it:** B-roll → `brolls for claude/`, images → `png for claude/`. Then catalog it with `skill-saver` section 4.

## ⚠ Open question — SFX & music source
`my-editing-rules` also has a rule that says to source all SFX and BGM from **Epidemic Sound**. This list names Mixkit / Freesound / Pixabay (SFX) and YouTube Audio Library / Pixabay / Mixkit (music) instead. Until Deepak confirms which wins, mention both options when recommending SFX or music.

## Pexels in practice *(video 13 v2, 2026-10-13 — worked end to end)*
- **Search** in the built-in browser: a JS helper fetches `/search/videos/<q>/?orientation=landscape`, collects `/video/<slug>-<id>/`, then fetches each video page and regex-reads its `videos.pexels.com/video-files/<id>/…mp4` renditions.
- **Choose the file:** most 4K clips also have a `…uhd_2560_1440_…fps.mp4` (or `2732x1440`), which is our exact output height, so download that.
- **Download** with `curl` straight from `videos.pexels.com` in the shell; `pexels.com/download/video/<id>/` also 302-redirects to the default file.
- **Review cheaply:** posters via `images.pexels.com/videos/<id>/…jpeg?w=480` on one contact sheet, then 6 frames per downloaded clip to pick the in-points.
- **Licence:** the Pexels licence (free for commercial use, no attribution required). Keep the IDs and in-points in the edit notes anyway.
- Prefer clips with Indian people for lines about Indian students, teachers or founders.

## Real photos, footage and documents for news videos *(AI Tech News ep 02 v2, 2026-10-16 — worked end to end)*
- **Order of preference:** primary source (the government page, the company's own post or report, the court filing) → public-domain official media (White House, DOJ/FBI, ODNI, NASA, NOAA, U.S. Space Force) → CC BY → CC BY-SA (credit all of them). Never use a deepfake, an AI image or a "photo illustration" as a real visual.
- **Wikimedia Commons API** (python urllib, a descriptive User-Agent, 1.5 s between calls, back off on HTTP 429): a person's lead photo = Wikipedia `prop=pageimages&piprop=name`, then Commons `prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=1600` for the licence (`LicenseShortName`), author (`Artist`) and date. Event photos: list a dated category (`Category:Donald Trump in September 2026`) and filter by the White House file-name date `P2026MMDD`. Commons also hosts White House *videos* (.webm, public domain) — the Sept 29 luncheon was there as 4 min of 1080p.
- **White House photos** are public domain; their videos carry a "TEXT POTUS…" banner in the bottom 15 %, so crop `1632:918:144:0` before scaling.
- **DOJ press releases** often include the FBI's evidence photos (ep 02: the recorder behind the TV, the device, the hidden-camera still) — public domain. justice.gov blocks curl; load the page in puppeteer and save every `<img>` with an in-page `fetch()` (`grab_imgs.js`).
- **Agency portraits** (ODNI, cabinet) are public domain on Commons; TechCrunch's Flickr is CC BY 2.0 for most tech executives; Bollywood/Tollywood stars usually have CC BY / BY-SA event photos.
- **Page captures** for documents: `capture2.js url "phrase1||phrase2||…" out.png` returns rects for every phrase after one scroll; `TOPY=n` puts the first phrase at y = n so the whole passage fits in the 900 px viewport; image px = CSS px × 2.
- **Faces for avatars:** square crops with head and a little shoulder (side ≈ 0.75–0.9 of the photo width for a portrait), checked on one sheet of circles before rendering (`faces.py`).
