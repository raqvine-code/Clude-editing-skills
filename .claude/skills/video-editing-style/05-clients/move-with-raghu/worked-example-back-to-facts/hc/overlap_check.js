// for every 0.1 s in the speaker scenes: is any text box above the chin line (+ margin)?  prints the worst cases
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const tl = JSON.parse(fs.readFileSync(path.join(__dirname, 'timeline.json'))); const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'stage.html')); await p.evaluate(() => document.fonts.ready); await p.evaluate(([tl]) => window.init(tl, { layout: 'B', cap: 'v2' }), [tl]);
  const bad = []; let n = 0;
  for (let t = 0; t < tl.dur; t += 0.1) {
    const r = await p.evaluate(async t => { await window.renderAt(t); const sc = TL.scenes.find(x => t >= x.t0 && t < x.t1); if (!SPEAKER.has(sc.id)) return null;
      const c = camAt(t, sc), i = Math.min(TL.n - 1, Math.round(t * FPS)), f = TL.face, k = Math.min(f.cx.length - 1, i);
      const fx0 = c.x + (f.cx[k] - .62 * f.fw[k]) * c.s, fx1 = c.x + (f.cx[k] + .62 * f.fw[k]) * c.s, fy0 = c.y + (f.cy[k] - .9 * f.fw[k]) * c.s, fy1 = c.chin;   // face box incl. hair, to the chin
      const hits = [];
      document.querySelectorAll('#Ltext *, #Lcap .lkw, #Lmg > div').forEach(e => { if (e.offsetParent === null) return; if (+getComputedStyle(e).opacity < .05) return;
        const bb = e.getBoundingClientRect(); if (bb.width < 4 || bb.height < 4 || e.classList.contains('L') || bb.width * bb.height > 0.5 * 1080 * 1920) return;
        if (bb.left < fx1 && bb.right > fx0 && bb.top < fy1 && bb.bottom > fy0) hits.push((e.className || e.tagName) + '@' + Math.round(bb.left) + ',' + Math.round(bb.top)); });
      return { sc: sc.id, hits }; }, t);
    if (!r) continue; n++; if (r.hits.length) bad.push([+t.toFixed(1), r.sc, r.hits.slice(0, 2).join(' ')]);
  }
  console.log('checked', n, 'speaker frames; text boxes overlapping the face box in', bad.length, bad.slice(0, 12)); await b.close(); })();
