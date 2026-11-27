// Browser reference capture (written 2026-11-25, used for the mustard-red and P16 Instagram / YouTube studies).
// Study other creators' reels WITHOUT downloading them: run inside the built-in browser pane
// (mcp__Claude_Browser__javascript_tool), view only. Never like, follow, comment, save or change the account.
// Rule 1.6: reference reels are study only; nothing captured here goes into a delivered edit.
//
// Paste this whole file once per page (javascript_tool), then call the helpers:
//   await RC.post("DcgwecURmrE")            -> {account, likes, comments, date, caption} from the post's og:description
//   await RC.search("aesthetic subtitles")  -> post codes on the keyword search page currently open
//   await RC.grid([0.5, 1, 2, 3, 4, 5])     -> overlays a 216x384 tile grid of the reel at those times; then
//                                              resize_window 1320x830 and take ONE screenshot (800 px wide is enough)
//   await RC.grid(RC.every(0, 30, 1.0))     -> one tile per second
//   await RC.cuts(0, 30)                     -> {cuts:[t...], perSec} from frame differences at 4 fps
//   RC.clear()                               -> removes the overlay; then resize_window preset "desktop"
// Split-screen reel (speaker in one half): RC.grid(times, {crop: [555, 450, 450, 800]}) crops sx, sy, sw, sh of the 1080x1920 source.
// YouTube Shorts: open https://www.youtube.com/shorts/<id>; the same RC.grid / RC.cuts work on its <video>.
//   Quick look with no page at all: https://i.ytimg.com/vi/<id>/hq1.jpg, hq2.jpg, hq3.jpg = frames at 25 / 50 / 75 %.
(() => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  // The reel that is playing. On /reels/ the first <video> is the one opened from /reel/<code>/.
  function video(i = 0) {
    const v = document.querySelectorAll("video")[i];
    if (!v) throw new Error("no <video> on this page yet - wait for the reel to load");
    return v;
  }

  async function seek(v, t) {
    v.pause();
    if (Math.abs(v.currentTime - t) < 0.01) return;
    await new Promise((res) => {
      const done = () => { v.removeEventListener("seeked", done); res(); };
      v.addEventListener("seeked", done);
      v.currentTime = t;
      setTimeout(done, 3000); // MSE buffers can stall; never hang the tool call
    });
    await sleep(60);
  }

  const every = (t0, t1, step) => {
    const out = [];
    for (let t = t0; t <= t1 + 1e-6; t += step) out.push(Math.round(t * 100) / 100);
    return out;
  };

  // Likes, comments, account, date and caption from the post HTML (no API: the /api/v1 search endpoints return 404 / HTML).
  async function post(code) {
    const html = await (await fetch(`/p/${code}/`, { credentials: "include" })).text();
    const doc = new DOMParser().parseFromString(html, "text/html");
    const og = doc.querySelector('meta[property="og:description"]')?.content || "";
    // og:description reads like: "12K likes, 85 comments - account on November 3, 2026: \"caption...\""
    const m = og.match(/^([\d.,KMk]+) likes?, ([\d.,KMk]+) comments? - ([^ ]+) on ([^:]+): ([\s\S]*)$/);
    return m ? { code, likes: m[1], comments: m[2], account: m[3], date: m[4], caption: m[5].slice(0, 400) } : { code, raw: og.slice(0, 400) };
  }

  // Post codes on the open keyword search page: https://www.instagram.com/explore/search/keyword/?q=<words>
  // Only about 3 results load while the browser pane is hidden (often 21 when it is shown): run several queries.
  async function search(q) {
    if (q && !location.href.includes(encodeURIComponent(q))) {
      location.href = `/explore/search/keyword/?q=${encodeURIComponent(q)}`;
      return "navigating - call RC.search() again (re-paste this file) once the page has loaded";
    }
    await sleep(1500);
    const codes = [...document.querySelectorAll('a[href*="/p/"], a[href*="/reel/"]')]
      .map((a) => (a.getAttribute("href").match(/\/(?:p|reel)\/([^/]+)/) || [])[1])
      .filter(Boolean);
    return [...new Set(codes)];
  }

  // Tile grid overlay. The MSE blob is 1080x1920 and the canvas is not tainted, so drawImage works.
  async function grid(times, opt = {}) {
    const v = video(opt.index || 0);
    const W = opt.w || 216, H = opt.h || 384, cols = opt.cols || 6;
    const rows = Math.ceil(times.length / cols);
    clear();
    const c = document.createElement("canvas");
    c.id = "__rc_grid"; c.width = cols * W; c.height = rows * H;
    Object.assign(c.style, { position: "fixed", left: "0", top: "0", zIndex: 2147483647, background: "#111", maxWidth: "100vw", maxHeight: "100vh" });
    document.body.appendChild(c);
    const g = c.getContext("2d");
    g.font = "bold 18px monospace"; g.textBaseline = "top";
    for (let i = 0; i < times.length; i++) {
      await seek(v, times[i]);
      const x = (i % cols) * W, y = Math.floor(i / cols) * H;
      if (opt.crop) g.drawImage(v, ...opt.crop, x, y, W, H); else g.drawImage(v, x, y, W, H);
      g.fillStyle = "rgba(0,0,0,.65)"; g.fillRect(x, y, 70, 24);
      g.fillStyle = "#ffd34d"; g.fillText(times[i].toFixed(2), x + 4, y + 3);
      if (opt.guides !== false) { // safe-zone guides: caption band y 1150-1330 and the bottom 300 px
        g.strokeStyle = "rgba(255,80,80,.55)"; g.lineWidth = 1;
        [1150, 1330, 1620].forEach((py) => { const yy = y + (py / 1920) * H; g.beginPath(); g.moveTo(x, yy); g.lineTo(x + W, yy); g.stroke(); });
      }
    }
    return { tiles: times.length, size: [c.width, c.height], duration: v.duration, src: [v.videoWidth, v.videoHeight] };
  }

  // Cut detector: 48x86 thumbnails at 4 fps, mean absolute difference > thr (38 found the hard cuts on 11 reels).
  async function cuts(t0 = 0, t1 = null, opt = {}) {
    const v = video(opt.index || 0);
    const fps = opt.fps || 4, thr = opt.thr || 38;
    t1 = Math.min(t1 ?? v.duration, v.duration - 0.05);
    const c = document.createElement("canvas"); c.width = 48; c.height = 86;
    const g = c.getContext("2d", { willReadFrequently: true });
    let prev = null; const out = [], diffs = [];
    for (let t = t0; t <= t1; t += 1 / fps) {
      await seek(v, t);
      g.drawImage(v, 0, 0, 48, 86);
      const d = g.getImageData(0, 0, 48, 86).data;
      if (prev) {
        let s = 0;
        for (let k = 0; k < d.length; k += 4) s += Math.abs(d[k] - prev[k]) + Math.abs(d[k + 1] - prev[k + 1]) + Math.abs(d[k + 2] - prev[k + 2]);
        const m = s / (48 * 86 * 3);
        diffs.push(Math.round(m));
        if (m > thr) out.push(Math.round(t * 100) / 100);
      }
      prev = d;
    }
    const span = t1 - t0;
    return { cuts: out, count: out.length, perSec: +(out.length / span).toFixed(2), avgShot: out.length ? +(span / (out.length + 1)).toFixed(2) : span, diffs };
  }

  function clear() { document.getElementById("__rc_grid")?.remove(); }

  window.RC = { video, seek, every, post, search, grid, cuts, clear };
  return "RC ready: post, search, grid, cuts, every, clear";
})();
