// node render.js stills OUT t1,t2,..  |  node render.js video OUT DUR
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const [mode, out, arg] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(__dirname, 'vice_neon_titles.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  const times = mode === 'stills' ? arg.split(',').map(Number) : [...Array(Math.round(+arg * 30)).keys()].map(i => i / 30);
  let k = 0; for (const t of times) { await p.evaluate(t => window.renderAt(t), t); await p.screenshot({ path: path.join(out, mode === 'stills' ? `s_${t.toFixed(2)}.jpg` : String(k++).padStart(5, '0') + '.jpg'), type: 'jpeg', quality: 93 }); }
  await b.close(); console.log('rendered', times.length); })();
