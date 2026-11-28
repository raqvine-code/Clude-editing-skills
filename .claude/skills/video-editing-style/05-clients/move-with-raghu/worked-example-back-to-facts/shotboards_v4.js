const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2380, height: 1200 } });
  for (const [k, out] of [['v4_b1', 'typography_v4_1'], ['v4_b2', 'typography_v4_2'], ['v4_b3', 'typography_v4_3'], ['v4_b4', 'typography_v4_4'], ['v4_before_after', 'two_lines_before_after']]) {
    await p.goto('file://' + path.resolve(`boards/${k}.html`)); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
    await p.screenshot({ path: `boards/${out}.jpg`, fullPage: true, type: 'jpeg', quality: 88 }); }
  await b.close(); })();
