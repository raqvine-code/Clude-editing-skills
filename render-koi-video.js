// Renders koi-pond-watercolour.html (#video mode) frame by frame and encodes an MP4.
// Usage: node render-koi-video.js [output.mp4] [framesDir] [workers]
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const html = path.resolve(__dirname, 'koi-pond-watercolour.html');
const out = path.resolve(process.argv[2] || 'koi-pond-watercolour.mp4');
const dir = path.resolve(process.argv[3] || 'koi-frames');
const workers = Number(process.argv[4] || 4);

(async () => {
  fs.mkdirSync(dir, { recursive: true });
  const t0 = Date.now();
  let meta = null, done = 0;
  await Promise.all(Array.from({ length: workers }, async (_, w) => {
    const browser = await chromium.launch();
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
    page.on('pageerror', e => { console.error('page error:', e.message); process.exit(1); });
    await page.goto('file://' + html + '#video');
    await page.waitForFunction(() => document.body.dataset.done === '1', null, { timeout: 180000 });
    meta = await page.evaluate(() => ({ fps: window.koiVideo.fps, frames: window.koiVideo.frames }));
    for (let i = w; i < meta.frames; i += workers) {
      const file = path.join(dir, `f_${String(i).padStart(4, '0')}.png`);
      if (fs.existsSync(file)) { done++; continue; }
      await page.evaluate(n => window.koiVideo.render(n), i);
      await page.screenshot({ path: file + '.tmp.png', type: 'png', clip: { x: 0, y: 0, width: 1080, height: 1920 } });
      fs.renameSync(file + '.tmp.png', file);
      if (++done % 40 === 0) console.log(`${done}/${meta.frames} frames, ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    }
    await browser.close();
  }));
  console.log('encoding', out);
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(meta.fps), '-i', path.join(dir, 'f_%04d.png'),
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '19', '-pix_fmt', 'yuv420p', '-profile:v', 'high',
    '-movflags', '+faststart', out], { stdio: 'inherit' });
  console.log('done in', ((Date.now() - t0) / 1000).toFixed(0), 's');
})();
