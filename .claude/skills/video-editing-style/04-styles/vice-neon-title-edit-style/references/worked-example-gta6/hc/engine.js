// GTA 6 facts video compositor: every frame is a pure function of time (renderAt(t)).
// Style: P21 vice-neon titles (video-editing-style) + motion-graphics-craft M2 (numbers and counters drive the motion).
'use strict';
const $ = (tag, cls, parent, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; (parent || document.body).appendChild(e); return e; };
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x)), prog = (t, t0, d) => clamp((t - t0) / Math.max(1e-4, d));
const lerp = (a, b, p) => a + (b - a) * p, outCubic = p => 1 - Math.pow(1 - p, 3), inOut = p => p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
const outBack = (p, s = 1.4) => 1 + (s + 1) * Math.pow(p - 1, 3) + s * Math.pow(p - 1, 2);   // small overshoot
const inExpo = p => p <= 0 ? 0 : Math.pow(2, 10 * p - 10);
let TL, K, FPS, S = {}, comps = [], LAYOUT = 'B', CAPMODE = 'none', FRAME = [], CAPS = null;
const imgCache = {};
async function setImg(el, src) { if (el._src === src) return; el._src = src; el.src = src; try { await el.decode(); } catch (e) {} }
const frameMain = i => `frames/main/${String(Math.max(0, Math.min(TL.n - 1, i))).padStart(5, '0')}.jpg`;
const show = (el, on) => { el.style.display = on ? 'block' : 'none'; };
const sceneOf = id => TL.scenes.find(s => s.id === id);
const inScene = (t, id) => { const s = sceneOf(id); return t >= s.t0 && t < s.t1; };

// ---------------------------------------------------------------- speaker (full-bleed crop of the 1080x1368 picture, face follow)
const PUSH = { spk1: [1.00, 1.06], why: [1.20, 1.22], reason: [1.06, 1.12], hype: [1.02, 1.07], but: [1.24, 1.26], dev13: [1.03, 1.10], outro: [1.02, 1.08] };
async function drawSpeaker(t, i, sc) {
  const m = document.getElementById('main'); await setImg(m, frameMain(i));
  const f = TL.face, k = Math.min(f.cx.length - 1, i), cx = f.cx[k], cy = f.cy[k];
  const [p0, p1] = PUSH[sc.id] || [1, 1], p = lerp(p0, p1, inOut(prog(t, sc.t0, sc.t1 - sc.t0)));
  if (LAYOUT === 'B') {             // framed window: picture at native size between two bands
    const s = 1.0 * p, W = 1080 * s, H = 1368 * s; const x = clamp(540 - cx * s, 1080 - W, 0), y = 276 + clamp(560 - cy * s, 1368 - H, 0);
    m.style.transform = `translate(${x}px, ${y}px) scale(${s})`; document.getElementById('Lmain').style.clipPath = 'inset(276px 0 276px 0)'; return;
  }
  document.getElementById('Lmain').style.clipPath = 'none';
  const s = 1920 / 1368 * p, x = clamp(540 - cx * s, 1080 - 1080 * s, 0), y = clamp(700 - cy * s, 1920 - 1368 * s, 0);
  m.style.transform = `translate(${x}px, ${y}px) scale(${s})`;
}

// ---------------------------------------------------------------- shared moves
function flashSettle(el, t, t0, tOut, dOut = 0.37) {       // P21 move 3: one frame bright and soft, settles in 0.35 s
  const p = outCubic(prog(t, t0, 0.35)), e = prog(t, tOut, dOut);
  el.style.opacity = t < t0 ? 0 : 1 - e; el.style.filter = `blur(${lerp(7, 0, p)}px) brightness(${lerp(1.75, 1, p)})`;
}
function pop(el, t, t0, base = '', d = 0.32) {              // scale 1.25 -> 1 with a small overshoot, fades in over 3 frames
  const p = prog(t, t0, d); el.style.opacity = t < t0 ? 0 : clamp((t - t0) / 0.05); el.style.transform = `${base} scale(${lerp(1.25, 1, outBack(p, 1.2))})`;
}
function wipeIn(el, t, t0, d = 0.33) {                       // P21 move 6: diagonal soft wipe, top-left first
  const p = prog(t, t0, d), x = lerp(-30, 130, p); el.style.webkitMaskImage = p >= 1 ? 'none' : `linear-gradient(115deg, #000 ${x - 22}%, transparent ${x}%)`; el.style.opacity = p > 0 ? 1 : 0;
}
function cover(img, W, H, iw, ih, s = 1, ax = .5, ay = .5) { // object-fit: cover with a push and an anchor
  const k = Math.max(W / iw, H / ih) * s, w = iw * k, h = ih * k; img.style.width = w + 'px'; img.style.height = h + 'px';
  img.style.left = (W - w) * ax + 'px'; img.style.top = (H - h) * ay + 'px'; img.style.objectFit = 'fill';
}
function strike(parent, color = 'var(--hot)') { const d = $('div', 'abs', parent); d.style.cssText += `height:16px;border-radius:8px;background:${color};box-shadow:0 0 18px ${color};transform-origin:0 50%;`; return d; }

// ---------------------------------------------------------------- scenes
const C = {};
C.hook = sc => {                                            // official cover art (phone), slow push, light sweep, "out now" stamp on "release"
  const box = $('div', 'L', L.broll), im = $('img', 'full', box);
  const shade = $('div', 'L', box); shade.style.background = 'linear-gradient(180deg, transparent 52%, rgba(7,3,11,.82) 74%, rgba(7,3,11,.9) 100%)';
  const sweep = $('div', 'L', box); sweep.style.background = 'linear-gradient(115deg, transparent 40%, rgba(255,200,120,.55) 48%, rgba(255,120,210,.45) 53%, transparent 61%)'; sweep.style.mixBlendMode = 'screen';
  const stamp = $('div', 'abs', L.text); stamp.style.cssText = 'left:0;right:0;top:1600px;text-align:center';
  const pill = $('div', 'pill', stamp, 'OUT NOW'); pill.style.cssText += ';position:relative;display:inline-block;font:700 46px/1 Tight;letter-spacing:.18em;padding:14px 34px 16px;background:linear-gradient(90deg,#FA3BB1,#FDA53A);color:#fff';
  const date = $('div', 'track', stamp, 'NOV 19 · 2026'); date.style.cssText += ';margin-top:22px;font-size:44px';
  const src = $('div', 'src', L.text, 'Official media · Rockstar Games'); src.style.cssText += ';left:40px;top:1866px;font-size:22px';
  // source time of the official 30 fps animation: wordmark lands on "GTA 6", cover art on "release"
  const srcT = t => t < K.gta1 ? lerp(12.6, 14.2, t / K.gta1) : t < K.release - .05 ? lerp(14.2, 16.0, (t - K.gta1) / (K.release - .05 - K.gta1)) : Math.min(17.9, 16.0 + (t - K.release + .05) * .9);
  return async t => {
    show(box, 1); show(stamp, 1); show(src, 1);
    await setImg(im, `frames/cov/${String(Math.round(srcT(t) * 30)).padStart(5, '0')}.jpg`); im.style.transform = `scale(${lerp(1.0, 1.06, inOut(prog(t, K.release, 1.5)))})`; shade.style.opacity = prog(t, K.release, .3);
    const sw = prog(t, 0.15, 0.8); sweep.style.transform = `translateX(${lerp(-110, 110, sw)}%)`; sweep.style.opacity = sw > 0 && sw < 1 ? 1 : 0;
    pop(pill, t, K.release - 0.04, ''); flashSettle(date, t, K.release + 0.18, 99); src.style.opacity = prog(t, 0.3, 0.3);
  };
};
C.famous = sc => {                                           // four official character clips cut on syllables, "FAMOUS" on the word
  const names = [['jason_duval', 30], ['lucia_caminos', 45], ['raul_bautista', 45], ['real_dimez', 30]];
  const box = $('div', 'L', L.broll), im = $('img', 'full', box);
  const w = $('div', 'price', L.text, 'FAMOUS'); w.style.cssText += ';position:absolute;left:0;right:0;top:1160px;text-align:center;font-size:210px';
  return async t => {
    show(box, 1); show(w, 1); const seg = (sc.t1 - sc.t0) / 4, k = Math.min(3, Math.floor((t - sc.t0) / seg)), [n, nf] = names[k];
    const f = Math.min(nf - 1, Math.round((nf - 1) * 0.25 + (t - sc.t0 - k * seg) * 30));      // real motion, starting a quarter in
    await setImg(im, `frames/clip_${n}/${String(f).padStart(2, '0')}.jpg`); im.style.transform = `scale(${1.03 + .02 * prog(t, sc.t0, 1)})`;
    pop(w, t, K.famous, '');
  };
};
C.spk1 = sc => {
  const a = $('div', 'track cap', L.text, 'MOST PEOPLE<br>DON’T KNOW'); a.style.top = '1150px'; a.style.fontSize = '58px';
  return t => { show(a, 1); flashSettle(a, t, K.many, K.n13a - 1.05); captionOptions(t); };
};
C.n13 = sc => {                                              // P21 moves 4-6 compressed: neon edge draw, fill + bloom, "YEARS" wiped on, a handwritten "why?"
  const bg = $('div', 'L', L.bg); bg.style.background = 'radial-gradient(900px 760px at 50% 40%, #1b0b27 0%, #07030b 62%, #000 100%)';
  const svgNS = 'http://www.w3.org/2000/svg', box = $('div', 'L', L.mg);
  box.innerHTML = `<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0"><defs>
   <linearGradient id="fG" gradientUnits="userSpaceOnUse" x1="0" y1="330" x2="0" y2="900"><stop offset="0" stop-color="#3447B5"/><stop offset=".2" stop-color="#7C3CC4"/><stop offset=".4" stop-color="#C936B6"/><stop offset=".58" stop-color="#F0489C"/><stop offset=".78" stop-color="#F7706A"/><stop offset="1" stop-color="#FDA53A"/></linearGradient>
   <linearGradient id="eG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF62D6"/><stop offset=".5" stop-color="#FF7FB0"/><stop offset="1" stop-color="#FFB45E"/></linearGradient>
   <linearGradient id="wv" x1="0" y1="0" x2="0" y2="1"><stop id="wv0" offset="0" stop-color="#fff"/><stop id="wv1" offset="0" stop-color="#000"/></linearGradient>
   <linearGradient id="rv" x1="0" y1="1" x2="0" y2="0"><stop id="rv0" offset="0" stop-color="#fff"/><stop id="rv1" offset="0" stop-color="#000"/></linearGradient>
   <mask id="mE" maskUnits="userSpaceOnUse" x="0" y="250" width="1080" height="760"><rect x="0" y="250" width="1080" height="760" fill="url(#wv)"/></mask>
   <mask id="mF" maskUnits="userSpaceOnUse" x="0" y="250" width="1080" height="760"><rect x="0" y="250" width="1080" height="760" fill="url(#rv)"/></mask>
   <filter id="g1" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="16"/></filter><filter id="g2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5"/></filter></defs>
   <g id="n13" style="transform-origin:540px 640px">
    <g mask="url(#mF)"><text id="nF" x="540" y="900" text-anchor="middle" font-family="Tight" font-weight="900" font-size="760" letter-spacing="-30" fill="url(#fG)">13</text></g>
    <g mask="url(#mE)"><text id="nG1" x="540" y="900" text-anchor="middle" font-family="Tight" font-weight="900" font-size="760" letter-spacing="-30" fill="none" stroke="url(#eG)" stroke-width="16" filter="url(#g1)">13</text>
     <text id="nG2" x="540" y="900" text-anchor="middle" font-family="Tight" font-weight="900" font-size="760" letter-spacing="-30" fill="none" stroke="url(#eG)" stroke-width="9" filter="url(#g2)">13</text>
     <text x="540" y="900" text-anchor="middle" font-family="Tight" font-weight="900" font-size="760" letter-spacing="-30" fill="none" stroke="url(#eG)" stroke-width="5">13</text></g></g></svg>`;
  const yrs = $('div', 'price', L.text, 'YEARS'); yrs.style.cssText += ';position:absolute;left:0;right:0;top:960px;text-align:center;font-size:230px';
  const why = $('div', 'hand', L.text, 'why?'); why.style.cssText += ';position:absolute;left:330px;top:1190px;font-size:150px';
  const arr = $('div', 'abs', L.text, '<svg width="110" height="110" viewBox="0 0 90 90"><path d="M14 76 L72 18 M30 16 L74 16 L74 60" fill="none" stroke="#9EFE3C" stroke-width="13" stroke-linecap="square"/></svg>'); arr.style.cssText += ';left:210px;top:1220px';
  const g = id => box.querySelector('#' + id);
  return t => {
    [bg, box, yrs, why, arr].forEach(e => show(e, 1)); const t0 = sc.t0;
    const pe = prog(t, t0, 0.62); g('wv0').setAttribute('offset', clamp(pe * 1.25 - .22)); g('wv1').setAttribute('offset', clamp(pe * 1.25));
    const pf = inOut(prog(t, t0 + 0.45, 0.35)); g('rv0').setAttribute('offset', clamp(pf * 1.3 - .3)); g('rv1').setAttribute('offset', clamp(pf * 1.3));
    const bl = inOut(prog(t, t0 + 0.65, 1.1)); g('nF').style.filter = `brightness(${lerp(.34, 1, bl)}) saturate(${lerp(.75, 1.08, bl)})`;
    g('nG1').style.opacity = lerp(.95, 0, prog(t, t0 + 0.9, 1.0)); g('nG2').style.opacity = lerp(1, .35, prog(t, t0 + 0.9, 1.0));
    g('n13').style.transform = `scale(${lerp(1.13, 1, outCubic(prog(t, t0 + 0.4, 1.4)))})`;
    wipeIn(yrs, t, K.yearsA, 0.3); const h = outCubic(prog(t, K.whyA, 0.3)); why.style.opacity = h; why.style.transform = `scaleX(.92) rotate(-4deg) translateY(${lerp(30, 0, h)}px)`; arr.style.opacity = h;
    const ex = prog(t, sc.t1 - 0.25, 0.25); box.style.webkitMaskImage = ex > 0 ? `linear-gradient(115deg, transparent ${lerp(-30, 130, ex) - 22}%, #000 ${lerp(-30, 130, ex)}%)` : 'none';
  };
};
C.why = sc => { const w = $('div', 'price cap', L.text, 'WHY?'); w.style.cssText += ';top:1150px;font-size:220px'; return t => { show(w, 1); pop(w, t, K.whyB, ''); }; };
C.notlist = sc => {                                          // three crossed-off cards: story, maps, graphics; each struck on its "kaadu"
  const bg = $('div', 'L', L.bg); bg.style.background = 'radial-gradient(1100px 900px at 50% 30%, #2a0d33 0%, #0b0410 60%, #050207 100%)';
  const kick = $('div', 'track cap', L.text, 'IT’S NOT FOR THE'); kick.style.top = '70px'; kick.style.fontSize = '38px';
  const D = [['STORY', 'story_jl13.jpg', 3840, 2160, sc.t0 + .14, K.not1, .5, .45], ['MAPS', 'map_leonida.jpg', 1577, 2160, K.maps, K.not2, .5, .42], ['GRAPHICS', 'gfx_vc10.jpg', 3840, 2160, K.graphics, K.not3, .5, .5]];
  const cards = D.map(([lab, src, iw, ih, tin, tx, ax, ay], j) => {
    const c = $('div', 'card', L.mg); c.style.cssText += `;left:60px;top:${165 + j * 432}px;width:960px;height:400px`;
    const im = $('img', '', c); im.src = 'assets/' + src; const dim = $('div', 'L', c); dim.style.background = 'rgba(7,3,11,.62)';
    const sh = $('div', 'L', c); sh.style.background = 'linear-gradient(180deg, transparent 45%, rgba(10,3,16,.78))';
    const l = $('div', 'price', c, lab); l.style.cssText += ';position:absolute;left:44px;bottom:30px;font-size:132px';
    const s = strike(c); s.style.left = '30px'; s.style.width = (lab.length * 85 + 40) + 'px'; s.style.bottom = '74px';
    const x = $('div', 'price', c, '✕'); x.style.cssText += ';position:absolute;right:46px;bottom:40px;font-size:150px;color:#FA3BB1;-webkit-text-stroke:0;filter:drop-shadow(0 0 18px #FA3BB1)';
    return { c, im, dim, s, x, iw, ih, tin, tx, ax, ay };
  });
  return t => {
    show(bg, 1); show(kick, 1); flashSettle(kick, t, sc.t0 + 0.05, 99);
    cards.forEach(o => {
      show(o.c, 1); const p = outCubic(prog(t, o.tin - 0.14, 0.32)); o.c.style.opacity = prog(t, o.tin - 0.14, 0.08);
      o.c.style.transform = `translateX(${lerp(160, 0, p)}px)`; o.c.style.filter = `blur(${lerp(14, 0, p)}px)`;
      cover(o.im, 960, 400, o.iw, o.ih, lerp(1.12, 1.02, prog(t, o.tin, 3)), o.ax, o.ay);
      const q = prog(t, o.tx, 0.16); o.s.style.transform = `scaleX(${outCubic(q)})`; o.s.style.opacity = q > 0 ? 1 : 0; o.dim.style.opacity = .85 * q; o.x.style.opacity = q; o.x.style.transform = `scale(${lerp(1.6, 1, outBack(q))})`;
    });
    const shake = t > K.not3 && t < K.not3 + 0.25 ? Math.sin(t * 90) * 6 * (1 - prog(t, K.not3, .25)) : 0; L.mg.style.marginLeft = `${shake}px`;
  };
};
C.reason = sc => { const a = $('div', 'track cap', L.text, 'THE REAL REASON'); a.style.top = '1180px'; a.style.fontSize = '64px'; const d = $('div', 'L', L.broll); d.style.background = 'radial-gradient(800px 900px at 50% 40%, rgba(7,3,11,0) 0%, rgba(7,3,11,.62) 100%)';
  return t => { show(a, 1); show(d, 1); flashSettle(a, t, K.whatfor, 99); d.style.opacity = prog(t, sc.t0, .4); }; };
C.moneytime = sc => {                                        // split: MONEY (top) on the word, TIMING (bottom) with a sweeping dial
  const top = $('div', 'abs', L.broll); top.style.cssText += ';left:0;top:0;width:1080px;height:950px;overflow:hidden'; const ti = $('img', 'abs', top); ti.src = 'assets/money_jl02.jpg';
  const bot = $('div', 'abs', L.broll); bot.style.cssText += ';left:0;top:970px;width:1080px;height:950px;overflow:hidden'; const bi = $('img', 'abs', bot); bi.src = 'assets/night_vc27.jpg';
  const bdim = $('div', 'L', bot); bdim.style.background = 'rgba(7,3,11,.35)';
  const line = $('div', 'abs', L.mg); line.style.cssText += ';left:0;top:950px;width:1080px;height:20px;background:linear-gradient(90deg,#FA3BB1,#FDA53A)';
  const m = $('div', 'price', L.text, 'MONEY'); m.style.cssText += ';position:absolute;left:0;right:0;top:640px;text-align:center;font-size:220px';
  const dial = $('div', 'abs', L.mg, `<svg width="420" height="420" viewBox="0 0 420 420"><circle cx="210" cy="210" r="180" fill="rgba(7,3,11,.45)" stroke="#fff" stroke-opacity=".9" stroke-width="10"/>
    <circle id="arc" cx="210" cy="210" r="180" fill="none" stroke="#9EFE3C" stroke-width="14" stroke-dasharray="1131" stroke-dashoffset="1131" transform="rotate(-90 210 210)" stroke-linecap="round"/>
    <line id="hand" x1="210" y1="210" x2="210" y2="70" stroke="#fff" stroke-width="12" stroke-linecap="round"/><circle cx="210" cy="210" r="16" fill="#fff"/></svg>`); dial.style.cssText += ';left:410px;top:1160px;transform-origin:50% 50%'; dial.querySelector('svg').setAttribute('width', 260); dial.querySelector('svg').setAttribute('height', 260);
  const tm = $('div', 'price', L.text, 'TIMING'); tm.style.cssText += ';position:absolute;left:0;right:0;top:1000px;text-align:center;font-size:170px';
  return t => {
    [top, bot, line, m, dial, tm].forEach(e => show(e, 1));
    const pb = outCubic(prog(t, K.timing - 0.12, 0.3)), th = lerp(1920, 950, pb); top.style.height = th + 'px';
    cover(ti, 1080, th, 3840, 2160, lerp(1.06, 1.12, prog(t, sc.t0, 2)), .44, .3); cover(bi, 1080, 950, 3840, 2160, lerp(1.1, 1.16, prog(t, sc.t0, 2)), .5, .5);
    m.style.top = lerp(1150, 640, pb) + 'px'; pop(m, t, K.money, ''); bot.style.transform = `translateY(${lerp(950, 0, pb)}px)`; line.style.transform = `scaleX(${pb})`;
    pop(tm, t, K.timing + 0.04, ''); dial.style.opacity = pb; const sw = prog(t, K.timing, 1.0);
    dial.querySelector('#arc').setAttribute('stroke-dashoffset', 1131 * (1 - sw)); dial.querySelector('#hand').setAttribute('transform', `rotate(${360 * sw} 210 210)`);
  };
};
// one chart system for the "normal game" curve, then reused for GTA V (the governing idea: GTA V's line never fell)
let CHN = 0;
function chartSys(parent) {
  const W = 940, H = 760, X0 = 70, Y0 = 520, u_ = 'c' + (++CHN);
  const g = $('div', 'abs', parent); g.style.cssText += `;left:${X0}px;top:${Y0}px;width:${W}px;height:${H}px`;
  g.innerHTML = `<svg width="${W}" height="${H + 80}" viewBox="0 0 ${W} ${H + 80}" style="overflow:visible"><defs>
    <linearGradient id="lg${u_}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7C3CC4"/><stop offset=".45" stop-color="#F0489C"/><stop offset="1" stop-color="#FDA53A"/></linearGradient>
    <linearGradient id="ar${u_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F0489C" stop-opacity=".35"/><stop offset="1" stop-color="#F0489C" stop-opacity="0"/></linearGradient>
    <filter id="gl${u_}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="9"/></filter></defs>
    <g stroke="rgba(233,221,240,.16)" stroke-width="2">${[0, 1, 2, 3, 4].map(k => `<line x1="0" y1="${H - k * H / 4}" x2="${W}" y2="${H - k * H / 4}"/>`).join('')}</g>
    <line x1="0" y1="${H}" x2="${W}" y2="${H}" stroke="rgba(233,221,240,.6)" stroke-width="3"/>
    <path id="ghost" fill="none" stroke="rgba(233,221,240,.35)" stroke-width="6" stroke-dasharray="14 12"/>
    <path id="area" fill="url(#ar${u_})"/><path id="glow" fill="none" stroke="url(#lg${u_})" stroke-width="18" filter="url(#gl${u_})" opacity=".8"/><path id="line" fill="none" stroke="url(#lg${u_})" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="line2" fill="none" stroke="#9EFE3C" stroke-width="8" stroke-linecap="round"/><circle id="dot" r="16" fill="#fff"/><circle id="dot2" r="13" fill="#9EFE3C"/>
    <g id="xl" font-family="Tight" font-weight="600" font-size="28" fill="rgba(233,221,240,.75)" letter-spacing="2"></g></svg>`;
  const q = id => g.querySelector('#' + id);
  const curve = (fn, upto, n = 90) => { let d = ''; for (let k = 0; k <= n; k++) { const u = upto * k / n; d += (k ? 'L' : 'M') + (u * W).toFixed(1) + ' ' + (H - fn(u) * H).toFixed(1); } return d; };
  const normal = u => u < .32 ? .92 * Math.sin(u / .32 * Math.PI / 2) : .92 * Math.exp(-3.1 * (u - .32)) + .02;     // rise, then hype fades
  const gtav = u => clamp(.78 + .14 * Math.sin(u * 9) * .25 + .12 * u, 0, 1) * (u < .04 ? u / .04 : 1);                 // stays high for 13 years
  return { g, q, W, H, curve, normal, gtav, labels(arr) { q('xl').innerHTML = arr.map(([u, s]) => `<text x="${u * W}" y="${H + 50}" text-anchor="middle">${s}</text>`).join(''); } };
}
C.chart1 = sc => {
  const bg = $('div', 'L', L.bg); bg.style.background = 'linear-gradient(180deg, #120618 0%, #07030B 70%)';
  const ch = chartSys(L.mg); ch.labels([[0, 'YEAR 1'], [.25, 'YEAR 2'], [.5, 'YEAR 3'], [.75, 'YEAR 4'], [1, 'YEAR 5']]);
  const ttl = $('div', 'serif cap', L.text, 'A Normal Game'); ttl.style.cssText += ';top:190px;font-size:150px';
  const sub = $('div', 'label cap', L.text, 'SALES OVER TIME'); sub.style.top = '390px';
  const rel = $('div', 'pill', L.text, 'RELEASE'); rel.style.cssText += ';left:70px;top:1340px;font-size:36px;font-weight:700;letter-spacing:.14em';
  const cnt = $('div', 'price', L.text, 'SALES ↑'); cnt.style.cssText += ';position:absolute;left:430px;top:660px;font-size:92px';
  const cl = $('div', 'label', L.text, 'ILLUSTRATION'); cl.style.cssText += ';position:absolute;left:72px;top:1860px;font-size:22px;opacity:.6';
  return t => {
    [bg, ch.g, ttl, sub, rel, cnt, cl].forEach(e => show(e, 1)); flashSettle(ttl, t, sc.t0 + 0.02, 99); sub.style.opacity = prog(t, sc.t0 + .3, .3);
    pop(rel, t, K.release2 - .03); const u = .32 * inOut(prog(t, K.release2, K.sells + 0.55 - K.release2)) + .06 * prog(t, K.sells + .55, 1.2);
    const d = ch.curve(ch.normal, Math.max(.001, u)); ch.q('line').setAttribute('d', d); ch.q('glow').setAttribute('d', d); ch.q('area').setAttribute('d', d + `L${u * ch.W} ${ch.H} L0 ${ch.H} Z`);
    ch.q('dot').setAttribute('cx', u * ch.W); ch.q('dot').setAttribute('cy', ch.H - ch.normal(u) * ch.H); ch.q('line2').setAttribute('d', ''); ch.q('dot2').setAttribute('r', 0); ch.q('ghost').setAttribute('d', '');
    pop(cnt, t, K.sells - .05, ''); cl.style.opacity = .6 * prog(t, sc.t0, .3);
  };
};
C.hype = sc => {                                             // speaker + a HYPE meter that drains on "gradually decrease"
  const m = $('div', 'abs', L.mg); m.style.cssText += ';left:84px;top:560px;width:96px;height:720px;border-radius:48px;background:rgba(7,3,11,.55);box-shadow:inset 0 0 0 3px rgba(255,255,255,.75),0 0 30px rgba(240,72,156,.35);overflow:hidden';
  const fill = $('div', 'abs', m); fill.style.cssText += ';left:10px;right:10px;bottom:10px;border-radius:38px;background:linear-gradient(0deg,#FDA53A,#F0489C 55%,#7C3CC4)';
  const lab = $('div', 'price', L.text, 'HYPE'); lab.style.cssText += ';position:absolute;left:7px;top:430px;font-size:110px;width:250px;text-align:center';
  const pct = $('div', 'num', L.text, '96%'); pct.style.cssText += ';position:absolute;left:7px;top:1310px;width:250px;text-align:center;font-size:64px';
  const arr = $('div', 'abs', L.text, '<svg width="80" height="120" viewBox="0 0 80 120"><path d="M40 6 V100 M10 72 L40 104 L70 72" fill="none" stroke="#FA3BB1" stroke-width="12" stroke-linecap="square"/></svg>'); arr.style.cssText += ';left:196px;top:820px';
  return t => {
    [m, lab, pct, arr].forEach(e => show(e, 1)); const a = outCubic(prog(t, sc.t0 + .02, .3)); [m, lab, pct].forEach(e => { e.style.opacity = a; }); m.style.transform = `translateX(${lerp(-160, 0, a)}px)`;
    const lv = lerp(.96, .16, inOut(prog(t, K.gradually, K.decrease + .5 - K.gradually))); fill.style.height = (700 * lv) + 'px'; pct.style.display = 'none';
    arr.style.opacity = prog(t, K.decrease - .1, .2); arr.style.transform = `translateY(${lerp(-20, 10, prog(t, K.decrease, .6))}px)`;
  };
};
C.chart2 = sc => {
  const bg = $('div', 'L', L.bg); bg.style.background = 'linear-gradient(180deg, #120618 0%, #07030B 70%)';
  const ch = chartSys(L.mg); ch.labels([[0, 'YEAR 1'], [.25, 'YEAR 2'], [.5, 'YEAR 3'], [.75, 'YEAR 4'], [1, 'YEAR 5']]);
  const ttl = $('div', 'serif cap', L.text, 'A Normal Game'); ttl.style.cssText += ';top:190px;font-size:150px';
  const dev = $('div', 'hand', L.text, 'devs move on →'); dev.style.cssText += ';position:absolute;left:330px;top:1330px;font-size:92px';
  const nx = $('div', 'pill', L.text, 'NEXT GAME'); nx.style.cssText += ';left:700px;top:430px;font-size:36px;font-weight:700;letter-spacing:.14em;background:rgba(158,254,60,.18);box-shadow:inset 0 0 0 2px #9EFE3C';
  return t => {
    [bg, ch.g, ttl, dev, nx].forEach(e => show(e, 1));
    const u = .38 + .62 * inOut(prog(t, sc.t0, 1.4)); const d = ch.curve(ch.normal, u); ch.q('line').setAttribute('d', d); ch.q('glow').setAttribute('d', d); ch.q('area').setAttribute('d', d + `L${u * ch.W} ${ch.H} L0 ${ch.H} Z`);
    ch.q('dot').setAttribute('cx', u * ch.W); ch.q('dot').setAttribute('cy', ch.H - ch.normal(u) * ch.H);
    const v = prog(t, K.nextgame - .1, 1.2), nf = w => .85 * Math.sin(clamp((w - .62) / .38 * 1.1) * Math.PI / 2);
    let p2 = ''; for (let k = 0; k <= 40; k++) { const w = .62 + .38 * v * k / 40; p2 += (k ? 'L' : 'M') + (w * ch.W).toFixed(1) + ' ' + (ch.H - nf(w) * ch.H).toFixed(1); }
    ch.q('line2').setAttribute('d', v > 0 ? p2 : ''); ch.q('dot2').setAttribute('r', v > 0 ? 13 : 0); ch.q('dot2').setAttribute('cx', (.62 + .38 * v) * ch.W); ch.q('dot2').setAttribute('cy', ch.H - nf(.62 + .38 * v) * ch.H); ch.q('ghost').setAttribute('d', '');
    const h = outCubic(prog(t, K.devs, .3)); dev.style.opacity = h; dev.style.transform = `scaleX(.92) rotate(-3deg) translateY(${lerp(24, 0, h)}px)`; pop(nx, t, K.nextgame);
  };
};
C.but = sc => { const w = $('div', 'price cap', L.text, 'BUT...'); w.style.cssText += ';top:1150px;font-size:220px'; return t => { show(w, 1); pop(w, t, K.but, ''); }; };
C.vcover = sc => {                                           // the GTA V cover slams in; Guinness record on the year
  const bgi = $('img', 'full', L.bg); bgi.src = 'assets/cover_v.jpg'; bgi.style.filter = 'blur(40px) brightness(.45) saturate(1.2)'; bgi.style.transform = 'scale(1.2)';
  const c = $('div', 'card', L.mg); c.style.cssText += ';left:150px;top:200px;width:780px;height:780px;border-radius:28px;box-shadow:0 0 0 4px #FEB423,0 0 60px rgba(254,180,35,.45),0 40px 80px rgba(0,0,0,.6)'; const im = $('img', '', c); im.src = 'assets/cover_v.jpg';
  const yr = $('div', 'track cap', L.text, 'SEPT 17 · 2013'); yr.style.top = '1030px'; yr.style.fontSize = '46px';
  const g = $('div', 'abs', L.text); g.style.cssText += ';left:110px;top:1140px;width:860px;text-align:center';
  g.innerHTML = `<div class="price" style="font-size:150px;display:block">$1 BILLION</div><div class="price" style="font-size:96px;display:block;margin-top:26px">IN 3 DAYS</div>`;
  const src = $('div', 'src', L.text, 'Source: Guinness World Records'); src.style.cssText += ';left:0;right:0;text-align:center;top:1620px';
  return t => {
    [bgi, c, yr, g, src].forEach(e => show(e, 1)); const p = prog(t, sc.t0, .22);
    c.style.transform = `scale(${lerp(1.35, 1, outCubic(p))}) rotate(${lerp(-4, 0, outCubic(p))}deg)`; c.style.opacity = prog(t, sc.t0, .06); c.style.filter = `blur(${lerp(12, 0, p)}px)`;
    flashSettle(yr, t, K.gta5 + .45, 99); pop(g, t, K.gta5 + .95, ''); src.style.opacity = prog(t, K.gta5 + 1.0, .3);
  };
};
C.vline = sc => {                                            // GTA V's line never falls: 2013 -> 2026, counter to 230M, PC Gamer headline
  const bg = $('div', 'L', L.bg); bg.style.background = 'linear-gradient(180deg, #120618 0%, #07030B 70%)';
  const ch = chartSys(L.mg); ch.labels([[0, '2013'], [.25, '2016'], [.5, '2019'], [.75, '2022'], [1, '2026']]);
  const ttl = $('div', 'price cap', L.text, 'GTA V'); ttl.style.cssText += ';top:150px;font-size:170px';
  const cnt = $('div', 'num cap', L.text, '0'); cnt.style.cssText += ';top:360px;font-size:118px';
  const cl = $('div', 'label cap', L.text, 'COPIES SOLD SINCE 2013'); cl.style.top = '490px';
  const ev = $('div', 'ev', L.mg); ev.style.cssText += ';left:70px;top:800px;width:940px'; const ei = $('img', '', ev); ei.src = 'assets/ev_pcgamer_head.png';
  const hl = $('div', 'abs', ev); hl.style.cssText += ';left:4%;top:44%;width:92%;height:14%;background:rgba(254,180,35,.38);mix-blend-mode:multiply;transform-origin:0 50%';
  const src = $('div', 'src', L.text, 'PC Gamer, Nov 2025 · 230M: Take-Two via Outlook Respawn, Aug 2026'); src.style.cssText += ';left:70px;top:1620px;font-size:22px';
  return t => {
    [bg, ch.g, ttl, cnt, cl, ev, src].forEach(e => show(e, 1)); pop(ttl, t, sc.t0 + .02, '');
    const u = inOut(prog(t, sc.t0 + .1, 1.5)); ch.q('ghost').setAttribute('d', ch.curve(ch.normal, 1));
    const d = ch.curve(ch.gtav, Math.max(.001, u)); ch.q('line').setAttribute('d', d); ch.q('glow').setAttribute('d', d); ch.q('area').setAttribute('d', d + `L${u * ch.W} ${ch.H} L0 ${ch.H} Z`);
    ch.q('dot').setAttribute('cx', u * ch.W); ch.q('dot').setAttribute('cy', ch.H - ch.gtav(u) * ch.H); ch.q('line2').setAttribute('d', ''); ch.q('dot2').setAttribute('r', 0);
    cnt.textContent = Math.round(230e6 * outCubic(prog(t, K.didnt - .1, 1.4))).toLocaleString('en-US') + '+';
    const pe = outCubic(prog(t, sc.t1 - 1.0, .35)); ev.style.opacity = pe; ev.style.transform = `translateY(${lerp(120, 0, pe)}px) rotate(-1.5deg)`; hl.style.transform = `scaleX(${outCubic(prog(t, sc.t1 - .6, .35))})`;
    src.style.opacity = pe;
  };
};
C.scale = sc => {                                            // old game vs new game: the new bar must out-earn the old one
  const bg = $('div', 'L', L.bg); bg.style.background = 'var(--sky)';
  const sun = $('div', 'abs', L.bg); sun.style.cssText += ';left:190px;top:330px;width:700px;height:700px;border-radius:50%;background:linear-gradient(180deg,#FEB423,#F7706A 40%,#F0489C 65%,#C936B6);opacity:.55;-webkit-mask-image:linear-gradient(180deg,#000 0 55%,transparent 55% 58%,#000 58% 66%,transparent 66% 70%,#000 70% 78%,transparent 78% 83%,#000 83% 90%,transparent 90%)';
  const P = $('div', 'price cap', L.text, 'PROFIT'); P.style.cssText += ';top:150px;font-size:210px';
  const mk = (x, lab, img, iw) => { const col = $('div', 'abs', L.mg); col.style.cssText += `;left:${x}px;top:380px;width:400px;height:1010px`;
    const bar = $('div', 'abs', col); bar.style.cssText += ';left:70px;bottom:250px;width:260px;border-radius:24px 24px 6px 6px;background:linear-gradient(0deg,#FDA53A,#F0489C 50%,#7C3CC4);box-shadow:0 0 0 5px #31072C,0 20px 50px rgba(0,0,0,.35)';
    const th = $('div', 'card', col); th.style.cssText += ';left:110px;bottom:40px;width:180px;height:180px;border-radius:20px'; const ti = $('img', '', th); ti.src = 'assets/' + img;
    const l = $('div', 'label', col, lab); l.style.cssText += ';position:absolute;left:-40px;right:-40px;bottom:-30px;text-align:center;color:#fff;font-size:42px;text-shadow:0 2px 10px rgba(49,7,44,.8)'; return { col, bar }; };
  const A = mk(90, 'OLD GAME', 'cover_v.jpg'), B = mk(590, 'NEW GAME', 'cover_vi_square.jpg');
  const gt = $('div', 'price', L.text, '>'); gt.style.cssText += ';position:absolute;left:470px;top:760px;font-size:200px;width:140px;text-align:center';
  return t => {
    [bg, sun, P, A.col, B.col, gt].forEach(e => show(e, 1)); pop(P, t, K.profit - .03, '');
    A.col.style.opacity = prog(t, sc.t0, .15); A.bar.style.height = (600 * outCubic(prog(t, K.oldg - .1, .5))) + 'px';
    B.col.style.opacity = prog(t, K.newg - .05, .15); B.bar.style.height = (lerp(0, 380, outCubic(prog(t, K.newg, .5))) + lerp(0, 330, inOut(prog(t, K.more, K.brings + .3 - K.more)))) + 'px';
    const w = prog(t, K.brings + .2, .25); gt.style.opacity = w; gt.style.transform = `scale(${lerp(1.6, 1, outBack(w))}) rotate(180deg)`; B.bar.style.boxShadow = `0 0 0 5px #31072C, 0 0 ${60 * w}px #9EFE3C`;
  };
};
C.delays = sc => {                                           // timing evidence: two delay headlines, then the dates
  const bg = $('div', 'L', L.bg); bg.style.background = 'radial-gradient(1100px 1000px at 50% 30%, #2a0d33 0%, #0b0410 62%, #050207 100%)';
  const k = $('div', 'track cap', L.text, 'TIMING'); k.style.top = '110px'; k.style.fontSize = '46px';
  const e1 = $('div', 'ev', L.mg); e1.style.cssText += ';left:70px;top:220px;width:940px'; $('img', '', e1).src = 'assets/ev_gi_head.png';
  const e2 = $('div', 'ev', L.mg); e2.style.cssText += ';left:70px;top:410px;width:940px'; $('img', '', e2).src = 'assets/ev_engadget_head.png';
  const dates = $('div', 'abs', L.text); dates.style.cssText += ';left:70px;top:830px;width:940px';
  const rows = [['FALL 2025', 1], ['MAY 26 · 2026', 1], ['NOV 19 · 2026', 0]].map(([s, x], j) => { const r = $('div', 'abs', dates); r.style.cssText += `;left:0;top:${j * 150}px;width:940px;height:130px`;
    const tx = $('div', j === 2 ? 'price' : 'serif', r, s); tx.style.cssText += `;position:absolute;left:0;top:${j === 2 ? 10 : 0}px;font-size:${j === 2 ? 120 : 118}px;${j === 2 ? 'color:#fff' : 'color:rgba(255,255,255,.75)'}`;
    const st = x ? strike(r) : null; if (st) { st.style.left = '-10px'; st.style.top = '62px'; st.style.width = (s.length * 52) + 'px'; } return { r, st }; });
  const ok = $('div', 'hand', L.text, 'out now ✓'); ok.style.cssText += ';position:absolute;left:600px;top:1300px;font-size:90px;color:#9EFE3C;-webkit-text-stroke:2px #9EFE3C';
  return t => {
    [bg, k, e1, e2, dates, ok].forEach(e => show(e, 1)); flashSettle(k, t, sc.t0 + .02, 99);
    [[e1, sc.t0 + .05], [e2, K.release3 - .2]].forEach(([e, t0]) => { const p = outCubic(prog(t, t0, .35)); e.style.opacity = prog(t, t0, .08); e.style.transform = `translateY(${lerp(90, 0, p)}px) rotate(${e === e1 ? -1.2 : 1}deg)`; });
    rows.forEach((o, j) => { const t0 = K.release3 + .35 + j * .32; o.r.style.opacity = prog(t, t0, .1); o.r.style.transform = `translateX(${lerp(-40, 0, outCubic(prog(t, t0, .3)))}px)`;
      if (o.st) { const q = prog(t, t0 + .18, .14); o.st.style.transform = `scaleX(${q})`; o.st.style.opacity = q > 0 ? 1 : 0; } });
    const h = outCubic(prog(t, K.release3 + 1.3, .3)); ok.style.opacity = h; ok.style.transform = `scaleX(.92) rotate(-4deg) translateY(${lerp(20, 0, h)}px)`;
  };
};
C.dev13 = sc => {                                            // "13 years of development" appears on "develop", struck on "pattaledu"
  const box = $('div', 'abs', L.text); box.style.cssText += ';left:0;right:0;top:1110px;text-align:center';
  const a = $('div', 'price', box, '13 YEARS'); a.style.cssText += ';display:block;font-size:200px';
  const b = $('div', 'serif', box, 'of development'); b.style.cssText += ';display:block;font-size:120px;margin-top:30px';
  const st = strike(L.text); st.style.cssText += ';left:120px;top:1180px;width:840px;height:22px';
  const st2 = strike(L.text); st2.style.cssText += ';left:180px;top:1355px;width:720px;height:18px';
  return t => {
    [box, st, st2].forEach(e => show(e, 1)); pop(a, t, K.develop - .05, ''); b.style.opacity = prog(t, K.develop + .25, .2);
    const q = prog(t, K.didnttake, .16), q2 = prog(t, K.didnttake + .1, .16); st.style.transform = `scaleX(${q}) rotate(-4deg)`; st.style.opacity = q > 0 ? 1 : 0; st2.style.transform = `scaleX(${q2}) rotate(3deg)`; st2.style.opacity = q2 > 0 ? 1 : 0;
    box.style.opacity = 1 - .45 * q;
  };
};
C.vs = sc => {                                               // GTA V vs GTA VI covers, then the profit bars
  const bg = $('div', 'L', L.bg); bg.style.background = 'var(--sky)';
  const mk = (x, img, ty) => { const c = $('div', 'card', L.mg); c.style.cssText += `;left:${x}px;top:${ty}px;width:440px;height:440px;border-radius:24px;box-shadow:0 0 0 5px #31072C,0 0 0 9px #FA3BB1,0 30px 60px rgba(0,0,0,.4)`; $('img', '', c).src = 'assets/' + img; return c; };
  const a = mk(60, 'cover_v.jpg', 290), b = mk(580, 'cover_vi_square.jpg', 290);
  const vs = $('div', 'price', L.text, 'VS'); vs.style.cssText += ';position:absolute;left:440px;top:440px;width:200px;text-align:center;font-size:130px';
  const P = $('div', 'price cap', L.text, 'MORE PROFIT?'); P.style.cssText += ';top:810px;font-size:150px';
  const bars = $('div', 'abs', L.mg); bars.style.cssText += ';left:60px;top:1010px;width:960px;height:420px';
  const bar = (y, lab, col) => { const r = $('div', 'abs', bars); r.style.cssText += `;left:0;top:${y}px;height:150px;width:960px`; const l = $('div', 'label', r, lab); l.style.cssText += ';position:absolute;left:0;top:-14px;color:#fff;font-size:46px;text-shadow:0 2px 10px rgba(49,7,44,.8)';
    const f = $('div', 'abs', r); f.style.cssText += `;left:0;top:50px;height:92px;border-radius:46px;background:${col};box-shadow:0 0 0 5px #31072C`; return f; };
  const fa = bar(0, 'GTA V', 'linear-gradient(90deg,#7C3CC4,#C936B6)'), fb = bar(210, 'GTA VI', 'linear-gradient(90deg,#F0489C,#FDA53A)');
  return t => {
    [bg, a, b, vs, P, bars].forEach(e => show(e, 1)); pop(a, t, K.gta5c - .04, ''); pop(b, t, K.gta6c - .04, ''); vs.style.opacity = prog(t, K.gta6c - .2, .2);
    pop(P, t, K.profit2 - .5, ''); bars.style.opacity = prog(t, K.profit2 - .6, .2);
    fa.style.width = (680 * outCubic(prog(t, K.profit2 - .5, .5))) + 'px'; fb.style.width = (lerp(0, 600, outCubic(prog(t, K.profit2 - .4, .5))) + lerp(0, 360, inOut(prog(t, K.profit2 + .1, .6)))) + 'px';
  };
};
C.timeline = sc => {                                         // payoff: the year counter runs 2013 -> 2026, the neon 13 returns, "years of waiting"
  const bg = $('div', 'L', L.bg); bg.style.background = 'radial-gradient(900px 800px at 50% 38%, #1b0b27 0%, #07030b 62%, #000 100%)';
  const yr = $('div', 'num cap', L.text, '2013'); yr.style.cssText += ';top:90px;font-size:140px;color:#E9DDF0';
  const n = $('div', 'abs', L.mg); n.style.cssText += ';left:0;right:0;top:250px;text-align:center';
  n.innerHTML = `<span style="font:900 480px/1 Tight;letter-spacing:-20px;background:linear-gradient(180deg,#3447B5,#7C3CC4 20%,#C936B6 40%,#F0489C 58%,#F7706A 78%,#FDA53A);-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 0 30px rgba(240,72,156,.55)) drop-shadow(0 0 2px #FF7FB0)">13</span>`;
  const y = $('div', 'price cap', L.text, 'YEARS'); y.style.cssText += ';top:740px;font-size:190px';
  const w = $('div', 'hand', L.text, 'of waiting'); w.style.cssText += ';position:absolute;left:340px;top:915px;font-size:116px';
  const ms = $('div', 'abs', L.text); ms.style.cssText += ';left:120px;top:1090px;width:840px';
  const M = [['2013', 'GTA V launches'], ['2023', 'GTA VI Trailer 1'], ['2025', 'Trailer 2 · first delay'], ['2026', 'GTA VI is out']];
  const rows = M.map(([a, b], j) => { const r = $('div', 'abs', ms); r.style.cssText += `;left:0;top:${j * 84}px;width:840px;height:80px`;
    r.innerHTML = `<span style="position:absolute;left:0;top:30px;width:26px;height:26px;border-radius:50%;background:${j === 3 ? '#9EFE3C' : '#F0489C'};box-shadow:0 0 16px ${j === 3 ? '#9EFE3C' : '#F0489C'}"></span><span style="position:absolute;left:60px;top:12px;font:800 52px/1 Tight;color:#fff">${a}</span><span style="position:absolute;left:230px;top:18px;font:400 42px/1 Inter;color:rgba(233,221,240,.88)">${b}</span>`; return r; });
  return t => {
    [bg, yr, n, y, w, ms].forEach(e => show(e, 1)); const yp = inOut(prog(t, sc.t0, K.n13c - sc.t0 + .1)); yr.textContent = String(Math.round(2013 + 13 * yp));
    const pn = outCubic(prog(t, K.n13c - .05, .45)); n.style.opacity = prog(t, K.n13c - .05, .08); n.style.transform = `scale(${lerp(1.18, 1, pn)})`; n.style.filter = `brightness(${lerp(1.8, 1, pn)}) blur(${lerp(10, 0, pn)}px)`;
    wipeIn(y, t, K.n13c + .5, .3); const h = outCubic(prog(t, K.wait, .3)); w.style.opacity = h; w.style.transform = `scaleX(.92) rotate(-4deg) translateY(${lerp(24, 0, h)}px)`;
    rows.forEach((r, j) => { const t0 = sc.t0 + .1 + j * .2; r.style.opacity = prog(t, t0, .1); r.style.transform = `translateX(${lerp(-30, 0, outCubic(prog(t, t0, .3)))}px)`; });
  };
};
C.outro = sc => {                                            // "more important": subscribe card with a click (our own button, not YouTube's)
  const a = $('div', 'track cap', L.text, 'MORE IMPORTANT'); a.style.top = '1120px'; a.style.fontSize = '58px';
  const card = $('div', 'abs', L.mg); card.style.cssText += ';left:150px;top:1220px;width:780px;height:170px;border-radius:85px;background:linear-gradient(90deg,#FA3BB1,#FDA53A);box-shadow:0 0 0 6px #31072C,0 0 40px rgba(250,59,177,.55),0 30px 60px rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center';
  const tx = $('div', 'price', card, 'SUBSCRIBE'); tx.style.cssText += ';font-size:118px;-webkit-text-stroke:.11em #31072C;filter:none';
  const cur = $('div', 'abs', L.text, '<svg width="110" height="130" viewBox="0 0 44 52"><path d="M4 2 L40 30 L24 32 L32 48 L25 51 L17 35 L6 46 Z" fill="#fff" stroke="#1E0624" stroke-width="3" stroke-linejoin="round"/></svg>');
  return t => {
    [a, card, cur].forEach(e => show(e, 1)); flashSettle(a, t, K.moreimp, K.subscribe - .5, .3);
    pop(card, t, K.subscribe - .05, ''); const clk = prog(t, K.subscribe + .45, .12), done = t > K.subscribe + .55;
    card.style.background = done ? 'linear-gradient(90deg,#3a2a44,#2a1d33)' : 'linear-gradient(90deg,#FA3BB1,#FDA53A)'; tx.textContent = done ? 'SUBSCRIBED' : 'SUBSCRIBE'; tx.style.fontSize = done ? '96px' : '118px';
    card.style.transform += ` scale(${1 - .06 * Math.sin(Math.PI * clk)})`;
    const cp = outCubic(prog(t, K.subscribe + .05, .4)); cur.style.opacity = prog(t, K.subscribe + .05, .1); cur.style.left = lerp(1000, 700, cp) + 'px'; cur.style.top = lerp(1700, 1320, cp) + 'px';
  };
};
function drawCaps(t) {
  const c = TL.caps.find(c => t >= c.t0 - 0.02 && t < c.t1);
  if (!c) { CAPS.style.display = 'none'; return; }
  CAPS.style.display = 'flex';
  if (CAPS._c !== c) { CAPS._c = c; CAPS.innerHTML = ''; c.els = c.words.map(([tw, w]) => { const e = $('span', 'capw', CAPS, w); return [tw, e]; });
    const len = c.words.map(x => x[1]).join(' ').length; CAPS.style.fontSize = (len > 20 ? 52 : 58) + 'px'; }
  const p = prog(t, c.t0 - .02, .1); CAPS.style.opacity = p; CAPS.style.transform = `translateY(${lerp(10, 0, outCubic(p))}px)`;
  c.els.forEach(([tw, e], j) => { const nxt = j + 1 < c.els.length ? c.els[j + 1][0] : c.t1; const on = t >= tw - .02 && t < nxt; e.style.color = on ? '#FDA53A' : (t >= tw ? '#fff' : 'rgba(255,255,255,.92)'); });
}
// caption options for the storyboard only (the owner picks one)
let capEls = null;
function captionOptions(t) {
  if (!capEls) { capEls = { te: $('div', 'tel cap', L.text, 'అందరికీ తెలిసే ఉంటుంది'), tg: $('div', 'cap', L.text, 'andariki telise untundi') }; capEls.te.style.top = '1640px'; capEls.tg.style.cssText += ';top:1650px;font:600 50px/1.2 Tight;color:#fff;text-shadow:0 4px 16px rgba(0,0,0,.7)'; }
  show(capEls.te, CAPMODE === 'te'); show(capEls.tg, CAPMODE === 'tg');
}
// ---------------------------------------------------------------- frame
const L = {};
window.init = (tl, opts = {}) => {
  TL = tl; K = tl.K; FPS = tl.fps; LAYOUT = opts.layout || 'B'; CAPMODE = opts.cap || 'none';
  L.bg = document.getElementById('Lbg'); L.broll = document.getElementById('Lbroll'); L.mg = document.getElementById('Lmg'); L.text = document.getElementById('Ltext');
  for (const sc of tl.scenes) {
    const layers = ['bg', 'broll', 'mg', 'text'], before = layers.map(k => L[k].children.length);
    const draw = C[sc.id] ? C[sc.id](sc) : null;
    const els = layers.flatMap((k, j) => [...L[k].children].slice(before[j]));
    els.forEach(e => { e.style.display = 'none'; e._always = e.style.cssText; });
    comps.push({ sc, draw, els });
  }
  // layout B (owner's choice): the speaker sits in a 4:5 window between two neon lines; designed scenes break out to full screen
  const fr = $('div', 'L', L.text); const top = $('div', 'abs', fr); top.style.cssText += ';left:0;top:268px;width:1080px;height:8px;background:linear-gradient(90deg,#3447B5,#C936B6,#F0489C,#FDA53A);box-shadow:0 0 18px rgba(240,72,156,.55)';
  const bot = top.cloneNode(); bot.style.top = '1644px'; fr.appendChild(bot);
  const lab = $('div', 'track cap', fr, 'GTA VI · THE 13-YEAR WAIT'); lab.style.top = '128px'; lab.style.fontSize = '34px'; FRAME = [fr];
  // Tenglish captions (owner's choice): one line, Shorts-safe band centred at y 1500, the spoken word lights up
  CAPS = $('div', 'cap', document.getElementById('Lcap')); CAPS.style.cssText += ';top:1458px;height:90px;display:flex;justify-content:center;align-items:center;gap:0 18px;flex-wrap:nowrap';
  for (const c of tl.caps) c.els = null;
};
const SPEAKER = new Set(['spk1', 'why', 'reason', 'hype', 'but', 'dev13', 'outro']);
window.renderAt = async t => {
  const i = Math.min(TL.n - 1, Math.round(t * FPS));
  document.getElementById('turb').setAttribute('seed', 1 + (i >> 1) % 97);
  const cur = comps.find(c => t >= c.sc.t0 && t < c.sc.t1) || comps[comps.length - 1];
  L.mg.style.marginLeft = '0px';
  for (const c of comps) if (c !== cur) c.els.forEach(e => { e.style.display = 'none'; });
  const spk = SPEAKER.has(cur.sc.id); show(document.getElementById('Lmain'), spk); FRAME.forEach(e => show(e, spk && LAYOUT === 'B'));
  // scene-start punch (zoom-blur) on picture layers; scenes with their own entrance keep it
  const dt = t - cur.sc.t0, own = new Set(['hook', 'n13', 'notlist', 'vcover', 'famous']), pk = own.has(cur.sc.id) || cur.sc.t0 === 0 ? 1 : prog(dt, 0, 0.13);
  for (const id of ['Lbg', 'Lmain', 'Lbroll', 'Lmg']) { const e = document.getElementById(id); e.style.transform = pk < 1 ? `scale(${lerp(1.07, 1, outCubic(pk))})` : ''; e.style.filter = pk < 1 ? `blur(${lerp(10, 0, outCubic(pk))}px) brightness(${lerp(1.25, 1, pk)})` : ''; }
  drawCaps(t);
  if (SPEAKER.has(cur.sc.id)) await drawSpeaker(t, i, cur.sc);
  if (cur.draw) await cur.draw(t, i);
  await Promise.all([...document.images].filter(im => im.offsetParent !== null && !im.complete).map(im => im.decode().catch(() => {})));
};
