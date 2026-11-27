// node render.js stills OUTDIR t1,t2,...   |   node render.js video OUTDIR [from to]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [mode, out, arg1, arg2] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  const tl = JSON.parse(fs.readFileSync(path.join(__dirname, 'timeline.json')));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.error('PAGE ERROR', e.message)); p.on('console', m => { if (m.type() === 'error') console.error('console', m.text()); });
  await p.goto('file://' + path.join(__dirname, 'stage.html')); await p.evaluate(() => document.fonts.ready);
  await p.evaluate(t => window.init(t), tl);
  const times = mode === 'stills' ? arg1.split(',').map(Number) : null;
  const frames = times ? times.map(t => Math.round(t * tl.fps)) : [...Array(tl.n).keys()].filter(i => i >= Math.round((+arg1 || 0) * tl.fps) && i < Math.round((+arg2 || 1e9) * tl.fps));
  const t0 = Date.now();
  for (const i of frames) {
    await p.evaluate(async t => await window.renderAt(t), i / tl.fps);
    const name = times ? `s_${(i / tl.fps).toFixed(2)}.jpg` : `${String(i).padStart(6, '0')}.jpg`;
    await p.screenshot({ path: path.join(out, name), type: 'jpeg', quality: times ? 90 : 95 });
  }
  console.log('rendered', frames.length, 'frames in', ((Date.now() - t0) / 1000).toFixed(1), 's');
  await b.close();
})();
