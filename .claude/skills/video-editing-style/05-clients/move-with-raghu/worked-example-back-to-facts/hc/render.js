// node render.js stills OUT t1,t2,... [layout] [cap]   |   node render.js video OUT [from to]
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const [mode, out, a1, a2, a3] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  const tl = JSON.parse(fs.readFileSync(path.join(__dirname, 'timeline.json')));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('console', m => { if (m.type() === 'error') console.log('page:', m.text()); }); p.on('pageerror', e => console.log('pageerror:', e.message));
  await p.goto('file://' + path.join(__dirname, 'stage.html')); await p.evaluate(() => document.fonts.ready);
  const opts = mode === 'stills' ? { layout: a2 || 'B', cap: a3 || 'tg' } : {};
  await p.evaluate(([tl, o]) => window.init(tl, o), [tl, opts]); await p.waitForTimeout(500);
  const times = mode === 'stills' ? a1.split(',').map(Number) : [...Array(tl.n).keys()].filter(i => i >= Math.round((+a1 || 0) * tl.fps) && i < Math.round((+a2 || 1e9) * tl.fps)).map(i => i / tl.fps);
  const t0 = Date.now(); let k = 0;
  for (const t of times) {
    await p.evaluate(t => window.renderAt(t), t);
    const name = mode === 'stills' ? `s_${t.toFixed(2)}${opts.layout === 'B' ? '_B' : ''}${opts.cap !== 'none' ? '_' + opts.cap : ''}.jpg` : String(Math.round(t * tl.fps)).padStart(6, '0') + '.jpg';
    await p.screenshot({ path: path.join(out, name), type: 'jpeg', quality: 92 }); k++;
  }
  console.log('rendered', k, 'frames in', ((Date.now() - t0) / 1000).toFixed(1), 's'); await b.close();
})();
