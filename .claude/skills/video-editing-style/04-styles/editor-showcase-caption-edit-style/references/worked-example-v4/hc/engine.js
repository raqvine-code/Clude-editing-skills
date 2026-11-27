// v4 compositor: footage + captions + 12 designed components, rendered by the browser frame by frame.
// window.init(TL) builds the DOM; await window.renderAt(t) draws time t.
(() => {
const $ = (tag, cls, parent, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; (parent || document.getElementById('stage')).appendChild(e); return e; };
const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
const lerp = (a, b, p) => a + (b - a) * p;
const prog = (t, a, d) => clamp((t - a) / d);
const outCubic = p => 1 - Math.pow(1 - p, 3);
const outExpo = p => p >= 1 ? 1 : 1 - Math.pow(2, -10 * p);
const inOut = p => 0.5 - 0.5 * Math.cos(Math.PI * p);
const pad = n => String(n).padStart(5, '0');
let TL, FPS, stage, L = {}, items = [], comps = [];
const imgCache = {};
async function setImg(el, src) { if (el.dataset.src === src) return; el.dataset.src = src; el.src = src; try { await el.decode(); } catch (e) {} }
const frameMain = i => `frames/main/${pad(TL.src_frame[Math.max(0, Math.min(TL.n - 1, i))] + 1)}.jpg`;
const frameB = (k, j) => `frames/${k}/${pad(Math.max(1, Math.min(TL.broll[k], j + 1)))}.jpg`;

// ---------- text helpers
function wspan(parent, w, cls) { const s = $('span', 'w ' + cls, parent, w[1]); s.dataset.t = w[0]; return s; }
function fitFont(el, maxW, base) { el.style.fontSize = base + 'px'; const w = el.getBoundingClientRect().width; if (w > maxW) el.style.fontSize = (base * maxW / w) + 'px'; }
function arrive(el, t, tw, kind) {
  const p = prog(t, tw, kind === 'small' ? 0.10 : 0.15), q = outCubic(p);
  if (t < tw) { el.style.opacity = 0; return; }
  const blur = kind === 'small' ? 6 * (1 - q) : 12 * (1 - q);
  el.style.opacity = q; el.style.filter = blur > 0.05 ? `blur(${blur}px)` : 'none';
  el.style.transform = kind === 'small' ? 'none' : `scale(${lerp(1.06, 1, q)})`;
}
function writeOn(el, t, tw, dur) {
  if (dur == null) dur = Math.max(0.24, Math.min(0.45, 0.03 * (el.textContent || '').length));                       // R8: the script line uncovers left to right through a soft edge
  const p = t < tw ? 0 : outCubic(prog(t, tw, dur)), x = lerp(-16, 108, p);
  const m = `linear-gradient(90deg, #000 ${x - 14}%, rgba(0,0,0,.35) ${x - 4}%, transparent ${x}%)`;
  el.style.webkitMaskImage = m; el.style.maskImage = m; el.style.opacity = p > 0 ? 1 : 0;
  el.style.filter = p < 1 ? `blur(${2.5 * (1 - p)}px)` : 'none';
}
function exitFx(el, t, t1, d = 0.12) {                          // R7: the block drops 2 % and blurs out on the cut
  const p = prog(t, t1 - d, d);
  el.style.opacity = 1 - p; el.style.transform = `translateY(${38 * p}px)`; el.style.filter = p > 0 ? `blur(${8 * p}px)` : 'none';
}
const lastWord = it => it.groups[it.groups.length - 1].slice(-1)[0][0];
const endOf = (it, hold = 0.55) => Math.min(it.t1, it.t1 - lastWord(it) > 0.75 ? lastWord(it) + hold : it.t1);

// ---------- caption treatments (fonts: Great Vibes + Arimo, as R8; placement: chin + 17 %, as R7/R6)
function buildCaption(it, group, parent, onpaper) {
  const cap = $('div', 'cap' + (onpaper ? ' onpaper' : ''), parent); const blk = $('div', '', cap); blk.style.display = 'inline-block';
  const words = group, kind = it.kind; const spans = [];
  if (kind === 'r8' || (kind === 'C5' && words.some(w => w[2] === '~'))) {
    const pre = words.slice(0, words.findIndex(w => w[2] === '~')), scr = words.filter(w => w[2] === '~'), post = words.slice(words.findIndex(w => w[2] === '~') + scr.length);
    if (pre.length) { const l = $('div', 'line', blk); l.style.textAlign = 'left'; l.style.marginBottom = '-26px'; l.style.paddingLeft = '18px'; pre.forEach(w => { spans.push([wspan(l, w, 'small'), w, 'small']); l.append(' '); }); }
    const ls = $('div', 'line', blk); const sc = $('span', 'w script', ls, scr.map(w => w[1]).join(' ')); spans.push([sc, scr[0], 'script']); cap._script = sc;
    if (post.length) { const l = $('div', 'line', blk); l.style.textAlign = 'right'; l.style.marginTop = '-30px'; l.style.paddingRight = '18px'; post.forEach(w => { l.append(' '); spans.push([wspan(l, w, 'small'), w, 'small']); }); }
  } else if (kind === 'r8bold') {
    const l = $('div', 'line', blk); words.forEach(w => { spans.push([wspan(l, w, 'bold'), w, 'bold']); l.append(' '); });
  } else {
    const ki = words.findIndex(w => w[2] === '*' || w[2] === '^');
    if (ki < 0) {                                                      // small words only: one or two balanced lines
      let a = [], b = [], len = words.map(w => w[1].length + 1).reduce((x, y) => x + y, 0), acc = 0;
      words.forEach(w => { (acc < len / 2 || len < 24 ? a : b).push(w); acc += w[1].length + 1; });
      [a, b].filter(x => x.length).forEach(arr => { const l = $('div', 'line', blk); arr.forEach(w => { spans.push([wspan(l, w, 'small'), w, 'small']); l.append(' '); }); });
    } else {
      const k1 = words.slice(ki).findIndex(w => !(w[2] === '*' || w[2] === '^')), kend = k1 < 0 ? words.length : ki + k1;
      const pre = words.slice(0, ki), keys = words.slice(ki, kend), post = words.slice(kend);
      if (pre.length) { const l = $('div', 'line', blk); pre.forEach(w => { spans.push([wspan(l, w, 'small'), w, 'small']); l.append(' '); }); }
      const lk = $('div', 'line', blk); lk.style.margin = '6px 0 4px';
      keys.forEach((w, j) => { const cls = w[2] === '^' ? 'white' : 'key'; spans.push([wspan(lk, w, cls), w, cls]); if (j < keys.length - 1) lk.append(' '); });
      if (post.length) { const l = $('div', 'line', blk); post.forEach(w => { spans.push([wspan(l, w, 'small'), w, 'small']); l.append(' '); }); }
    }
  }
  cap._spans = spans; cap._blk = blk; return cap;
}
function layoutCap(cap, y, maxScript = 700) {
  cap.style.display = 'block';
  if (cap._script) fitFont(cap._script, maxScript, 170);
  cap.querySelectorAll('.key').forEach(k => { if (k.getBoundingClientRect().width > 880) fitFont(k, 880, 124); });
  const h = cap.getBoundingClientRect().height; cap.style.top = (y - h / 2) + 'px'; cap.style.display = 'none';
}
function drawCap(cap, t, t0, t1) {
  if (t < t0 || t >= t1) { cap.style.display = 'none'; return; }
  cap.style.display = 'block';
  for (const [el, w, kind] of cap._spans) { const tw = Math.max(w[0], t0); kind === 'script' ? writeOn(el, t, tw) : arrive(el, t, tw, kind); }
  exitFx(cap._blk, t, t1);
}

// ---------- small inline icons (drawn, not stock)
const ICON = {
  person: '<svg viewBox="0 0 48 48" width="34" height="34" style="position:absolute;left:12px;top:12px"><circle cx="24" cy="17" r="8" fill="#E9B86F"/><path d="M9 41c2-9 8-13 15-13s13 4 15 13z" fill="#E9B86F"/></svg>',
  pair: '<svg viewBox="0 0 48 48" width="34" height="34" style="position:absolute;left:12px;top:12px"><circle cx="17" cy="18" r="6.5" fill="#E9B86F"/><circle cx="32" cy="18" r="6.5" fill="#E9B86F" opacity=".7"/><path d="M4 40c1.5-7 6.5-10 13-10s11.5 3 13 10z" fill="#E9B86F"/><path d="M22 40c1.4-6 5.6-9 10-9 5.6 0 10.6 3 12 9z" fill="#E9B86F" opacity=".7"/></svg>',
  case: '<svg viewBox="0 0 48 48" width="34" height="34" style="position:absolute;left:12px;top:12px"><rect x="6" y="15" width="36" height="25" rx="5" fill="#E9B86F"/><path d="M18 15v-4a3 3 0 0 1 3-3h6a3 3 0 0 1 3 3v4" stroke="#E9B86F" stroke-width="3.5" fill="none"/><rect x="6" y="24" width="36" height="3" fill="#15201C" opacity=".5"/></svg>',
  bubble: (w = 170) => `<svg viewBox="0 0 170 140" width="${w}" height="${w * 140 / 170}"><defs><linearGradient id="gl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset="1" stop-color="#F3EADB" stop-opacity=".62"/></linearGradient></defs>
    <path d="M28 8h114a22 22 0 0 1 22 22v52a22 22 0 0 1-22 22H70l-30 26 6-26H28A22 22 0 0 1 6 82V30A22 22 0 0 1 28 8z" fill="url(#gl)" stroke="#fff" stroke-opacity=".85" stroke-width="2"/>
    <path d="M30 18h70" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".7"/>
    <circle cx="60" cy="58" r="8" fill="#E9B86F"/><circle cx="85" cy="58" r="8" fill="#E9B86F" opacity=".8"/><circle cx="110" cy="58" r="8" fill="#E9B86F" opacity=".6"/></svg>`,
  talk: `<svg viewBox="0 0 300 230" width="300" height="230"><defs><linearGradient id="g2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset=".55" stop-color="#cfd6d2" stop-opacity=".7"/><stop offset="1" stop-color="#8E9A94" stop-opacity=".55"/></linearGradient><linearGradient id="g3" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7DDB0" stop-opacity=".95"/><stop offset="1" stop-color="#E9B86F" stop-opacity=".7"/></linearGradient></defs>
    <path d="M24 14h130a20 20 0 0 1 20 20v54a20 20 0 0 1-20 20H78l-28 24 5-24H24A20 20 0 0 1 4 88V34A20 20 0 0 1 24 14z" fill="url(#g2)" stroke="#fff" stroke-opacity=".8" stroke-width="2"/>
    <path d="M146 92h130a20 20 0 0 1 20 20v54a20 20 0 0 1-20 20h-31l5 24-28-24H146a20 20 0 0 1-20-20v-54a20 20 0 0 1 20-20z" fill="url(#g3)" stroke="#fff" stroke-opacity=".75" stroke-width="2"/>
    <path d="M26 26h70" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".75"/><path d="M150 104h60" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".6"/></svg>`,
};

// ---------- footage as full frame or as a card (cards close in round the speaker: R7 device board, R5 phone)
function placeMain(i, rect, t) {
  const [s, x0, y0] = TL.cam[Math.max(0, Math.min(TL.n - 1, i))];
  const r = rect || { x: 0, y: 0, w: 1080, h: 1920, r: 0 };
  const k = Math.max(r.w / 1080, r.h / 1920), full = !rect;
  const ox = full ? 0 : r.w / 2 - 540 * k, oy = full ? 0 : r.h * 0.42 - 820 * k;
  const cw = L.cardwrap; cw.style.left = r.x + 'px'; cw.style.top = r.y + 'px'; cw.style.width = r.w + 'px'; cw.style.height = r.h + 'px'; cw.style.borderRadius = r.r + 'px';
  cw.style.boxShadow = full ? 'none' : '0 34px 70px rgba(0,0,0,.35), 0 8px 18px rgba(0,0,0,.25)';
  L.main.style.transform = `translate(${ox}px,${oy}px) scale(${k}) translate(${-x0 * s}px,${-y0 * s}px) scale(${s})`;
  let blur = 0;
  for (const f of TL.focus) if (t >= f && t < f + 0.30) blur = Math.max(blur, 16 * (1 - outCubic(prog(t, f, 0.30))));
  for (const f of TL.punch) if (t >= f && t < f + 0.14) blur = Math.max(blur, 7 * (1 - prog(t, f, 0.14)));
  cw.style.filter = blur > 0.05 ? `blur(${blur}px)` : 'none';
}
const lerpRect = (a, b, p) => ({ x: lerp(a.x, b.x, p), y: lerp(a.y, b.y, p), w: lerp(a.w, b.w, p), h: lerp(a.h, b.h, p), r: lerp(a.r, b.r, p) });
const FULL = { x: 0, y: 0, w: 1080, h: 1920, r: 0 };
function brollCard(el, wrap, rect) {                              // the B-roll image cover-fitted into a rounded card
  wrap.style.left = rect.x + 'px'; wrap.style.top = rect.y + 'px'; wrap.style.width = rect.w + 'px'; wrap.style.height = rect.h + 'px'; wrap.style.borderRadius = rect.r + 'px';
  const k = Math.max(rect.w / 1080, rect.h / 1920); el.style.width = 1080 * k + 'px'; el.style.height = 1920 * k + 'px';
  el.style.left = (rect.w - 1080 * k) / 2 + 'px'; el.style.top = (rect.h - 1920 * k) / 2 + 'px';
}

// ---------- the 12 components
const C = {};
const W = (it, gi = 0) => it.groups[gi];
const find = (it, word, n = 0) => { const all = it.groups.flat().filter(w => w[1].toLowerCase() === word); return all[n]; };

C.converge = it => {                                               // R6: two halves converge from the frame edges
  const box = $('div', 'cap', L.text); box.style.top = (it.y - 120) + 'px';
  const tiny = $('div', 'line small', box, W(it)[0][1]); tiny.style.marginBottom = '6px';
  const big = $('div', 'abs', box); big.style.top = '62px'; big.style.left = '0';
  const a = $('span', 'w key', big, 'SELF-'), b = $('span', 'w key', big, 'CREATING');
  [a, b].forEach(e => { e.style.position = 'absolute'; e.style.color = '#fff'; e.style.fontSize = '106px'; e.style.textShadow = '0 0 28px rgba(233,184,111,.55), 0 6px 16px rgba(0,0,0,.5)'; });
  box.style.display = 'block'; const wa = a.getBoundingClientRect().width, wb = b.getBoundingClientRect().width; box.style.display = 'none';
  const x0 = 540 - (wa + wb + 8) / 2;
  return t => {
    if (t < it.t0 || t >= it.t1) { box.style.display = 'none'; return; } box.style.display = 'block';
    arrive(tiny, t, W(it)[0][0], 'small');
    [[a, W(it)[1][0], -wa - 60, x0], [b, W(it)[2][0], 1140, x0 + wa + 8]].forEach(([e, tw, from, to]) => {
      const p = outExpo(prog(t, tw, 0.32)); e.style.left = lerp(from, to, p) + 'px'; e.style.opacity = t < tw ? 0 : 1; e.style.filter = p < 1 ? `blur(${16 * (1 - p)}px)` : 'none'; });
    exitFx(box, t, it.t1);
  };
};

C.C3 = it => {                                                     // R6: B-roll whips in, then shrinks into a camera card on his wall colour
  const g = W(it), [wAttr, wGood, wThings] = g, pillWords = g.slice(3);
  const board = $('div', 'plate', L.broll); board.style.background = 'radial-gradient(120% 80% at 50% 35%, #2A3C35, #17231F 70%)';
  const wrap = $('div', 'card', L.broll); const img = $('img', '', wrap);
  const ui = $('div', 'abs', L.broll); ui.innerHTML = `<div style="position:absolute;left:30px;top:26px;display:flex;gap:12px">${'<i style="display:block;width:16px;height:16px;border-radius:50%;background:rgba(255,255,255,.85)"></i>'.repeat(3)}</div>
    <div style="position:absolute;left:0;right:0;bottom:34px;text-align:center;font:700 22px AR;letter-spacing:3px;color:rgba(255,255,255,.8)">VIDEO &nbsp;&nbsp; <span style="color:#E9B86F">PHOTO</span> &nbsp;&nbsp; PORTRAIT</div>
    <div style="position:absolute;left:50%;bottom:82px;width:84px;height:84px;margin-left:-42px;border-radius:50%;border:6px solid #fff;box-shadow:0 0 0 4px rgba(0,0,0,.25)"></div>`;
  const shade = $('div', 'shade', L.broll);
  const cap = $('div', 'cap', L.text); const ta = $('div', 'line small', cap, wAttr[1]);
  const big = $('div', 'line', cap); const sg = $('span', 'w key', big, 'GOOD'), st = $('span', 'w key', big, 'THINGS');
  [sg, st].forEach(e => { e.style.color = '#F3EADB'; e.style.fontSize = '112px'; e.style.textShadow = '0 0 26px rgba(233,184,111,.5), 0 6px 18px rgba(0,0,0,.5)'; });
  const pill = $('div', 'pill', L.text); pill.innerHTML = '<div class="glow"></div><div class="ic">' + ICON.person + '</div><div class="tx">' + pillWords.map(w => w[1]).join(' ').toUpperCase() + '</div>';
  const card = { x: 150, y: 210, w: 780, h: 800, r: 44 };
  cap.style.display = 'block'; const ch = cap.getBoundingClientRect().height; cap.style.top = (it.y - ch / 2) + 'px'; cap.style.display = 'none';
  pill.style.display = 'flex'; const pw = pill.getBoundingClientRect().width; pill.style.left = (540 - pw / 2) + 'px'; pill.style.top = (it.y + 92) + 'px'; pill.style.display = 'none';
  const tB = wGood[0], tS = tB + 0.55;
  return async t => {
    const on = t >= it.t0 && t < it.t1; [board, wrap, ui, shade].forEach(e => e.style.display = on && t >= tB ? 'block' : 'none');
    cap.style.display = on ? 'block' : 'none'; pill.style.display = on && t >= pillWords[0][0] ? 'flex' : 'none';
    if (!on) return;
    arrive(ta, t, Math.max(wAttr[0], it.show0 || 0), 'small'); arrive(sg, t, wGood[0], 'key'); arrive(st, t, wThings[0], 'key');
    if (t >= tB) {
      await setImg(img, frameB('sunset', Math.round((t - tB) * TL.fps) + 6));
      const ps = inOut(prog(t, tS, 0.30)), r = lerpRect(FULL, card, ps); brollCard(img, wrap, r);
      const pe = outCubic(prog(t, tB, 0.20)); wrap.style.transform = `translateX(${(1 - pe) * 34}%)`; wrap.style.filter = pe < 1 ? `blur(${20 * (1 - pe)}px)` : 'none';
      board.style.opacity = ps; shade.style.opacity = 1 - ps; ui.style.left = card.x + 'px'; ui.style.top = card.y + 'px'; ui.style.width = card.w + 'px'; ui.style.height = card.h + 'px'; ui.style.opacity = prog(t, tS + 0.22, 0.15);
    }
    const pp = outCubic(prog(t, pillWords[0][0], 0.22)); pill.style.clipPath = `inset(0 ${100 - pp * 100}% 0 0 round 46px)`;
    pill.querySelector('.tx').style.opacity = 1;
    [cap, pill].forEach(e => { const q = prog(t, it.t1 - 0.12, 0.12); e.style.opacity = 1 - q; });
  };
};

C.C4 = it => {                                                     // R7: the "middle box" frame snaps round him on "luck frame"
  const box = { x: 100, y: 210, w: 880, h: 1130 };
  const tint = $('div', 'abs', L.fx); tint.style.cssText += `;left:${box.x}px;top:${box.y}px;width:${box.w}px;height:${box.h}px;border-radius:38px;box-shadow:0 0 0 2400px rgba(23,35,31,.74);display:none`;
  const corners = [[0, 0, 'top', 'left'], [1, 0, 'top', 'right'], [0, 1, 'bottom', 'left'], [1, 1, 'bottom', 'right']].map(([cx, cy, v, h]) => {
    const c = $('div', 'abs', tint); c.style.cssText += `;width:74px;height:74px;${v}:-6px;${h}:-6px;border-${v}:7px solid #E9B86F;border-${h}:7px solid #E9B86F;border-${v}-${h}-radius:40px`; return c; });
  const label = $('div', 'abs', tint, 'LUCK FRAME'); label.style.cssText += ';left:30px;top:26px;font:700 26px AR;letter-spacing:5px;color:#E9B86F';
  const flash = $('div', 'plate', L.fx); flash.style.background = '#E9B86F';
  const cap = buildCaption({ kind: 'r8' }, it.groups[0].map((w, j) => j >= 2 ? [w[0], w[1], '~'] : w), L.text); layoutCap(cap, it.y);
  const tSnap = it.groups[0][1][0] - 0.04;
  return t => {
    const on = t >= it.t0 && t < it.t1; tint.style.display = on && t >= tSnap ? 'block' : 'none';
    const p = outCubic(prog(t, tSnap, 0.10)); tint.style.transform = `scale(${lerp(1.04, 1, p)})`; tint.style.opacity = p;
    flash.style.display = on && t >= it.t1 - 1.5 / TL.fps ? 'block' : 'none'; flash.style.opacity = .45;
    drawCap(cap, t, it.show0 || it.t0, it.t1);
  };
};

C.C5 = it => {                                                     // R7: the speaker shrinks into a card on a paper board; "research" brings a second card
  const board = $('div', 'plate', L.bg); board.style.background = 'radial-gradient(100% 70% at 50% 40%, #F6EEE0, #E6DAC6 75%)';
  const wrap = $('div', 'card', L.broll); const img = $('img', '', wrap);
  const caps = it.groups.map(g => { const c = buildCaption({ kind: g.some(w => w[2] === '~') ? 'r8' : 'r7' }, g, L.text, true); layoutCap(c, 1215, 640); return c; });
  const A = { x: 96, y: 250, w: 520, h: 760, r: 40 }, B = { x: 640, y: 380, w: 350, h: 520, r: 30 };
  const wRes = find(it, 'research'), tB = wRes[0] - 0.18;
  return async (t, i) => {
    const on = t >= it.t0 && t < it.t1; board.style.display = on ? 'block' : 'none'; wrap.style.display = on && t >= tB ? 'block' : 'none';
    it.groups.forEach((g, gi) => drawCap(caps[gi], t, gi ? g[0][0] : (it.show0 || g[0][0]), gi + 1 < it.groups.length ? Math.max(it.groups[gi + 1][0][0], g[g.length - 1][0] + 0.34) : it.t1));
    if (!on) return null;
    if (t >= tB) {
      await setImg(img, frameB('book', Math.round((t - tB) * TL.fps) + 4));
      const p = outExpo(prog(t, tB, 0.40)); brollCard(img, wrap, B); wrap.style.transform = `translateX(${(1 - p) * 520}px) rotate(${(1 - p) * 6}deg)`;
    }
    return lerpRect(FULL, A, inOut(prog(t, it.t0, 0.30)));
  };
};

C.C6 = it => {                                                     // R5: type cards with a hard colour inversion on the stressed word; frames as film frames
  const g = it.groups[0]; const idx = w => g.findIndex(x => x[1].toLowerCase() === w);
  const iFacts = idx('facts'), iIts = idx("it's"), iFrames = idx('frames');
  const plate = $('div', 'plate', L.plate);
  const mk = (words, cls, y, align) => { const d = $('div', 'cap', L.text); d.style.top = y + 'px'; const l = $('div', 'line', d); l.style.textAlign = align || 'center'; l.style.padding = '0 120px';
    const sp = words.map(w => { const s = wspan(l, w, cls); l.append(' '); return [s, w]; }); return [d, sp]; };
  const [dA, sA] = mk(g.slice(0, iFacts), 'small', 700, 'left');
  const hero = $('div', 'cap', L.text); const hs = $('span', 'w', hero, 'FACTS'); hs.style.font = '700 250px/1 AR'; hs.style.letterSpacing = '-8px';
  hero.style.display = 'block'; fitFont(hs, 860, 250); hero.style.top = '770px'; hero.style.display = 'none';
  const [dB, sB] = mk(g.slice(iFacts + 1, iIts), 'small', 1040, 'right');
  const [dC, sC] = mk(g.slice(iIts, iFrames), 'small', 640, 'left');
  const fr = $('div', 'cap', L.text); const fs = $('span', 'w script', fr, 'frames'); fs.style.fontSize = '300px'; fs.style.color = '#1E2B26'; fs.style.textShadow = 'none';
  fr.style.display = 'block'; fitFont(fs, 760, 300); fr.style.top = '690px'; fr.style.display = 'none';
  const [dD, sD] = mk(g.slice(iFrames + 1), 'small', 1010, 'right');
  const film = $('div', 'film', L.text); const shots = [60, 330, 720, 905];
  shots.forEach(f => { const d = $('div', 'fr', film); $('div', 'holes', d).style.top = '10px'; const h2 = $('div', 'holes', d); h2.style.bottom = '10px'; const im = $('img', '', d); im.src = `frames/main/${pad(f)}.jpg`; });
  const tFacts = g[iFacts][0], tIts = g[iIts][0], tInv = g[iFrames][0];
  return t => {
    const on = t >= it.t0 && t < it.t1; const inv = t >= tInv;
    plate.style.display = on ? 'block' : 'none'; plate.style.background = inv ? '#F3EADB' : 'radial-gradient(110% 80% at 50% 40%, #24342E, #17231F 75%)';
    const ink = inv ? '#1E2B26' : '#F3EADB';
    [dA, hero, dB, dC, fr, dD, film].forEach(e => e.style.display = on ? 'block' : 'none'); if (!on) return;
    film.style.display = inv ? 'flex' : 'none';
    for (const [s, w] of [...sA, ...sB, ...sC, ...sD]) { arrive(s, t, w[0], 'small'); s.style.color = ink; s.style.textShadow = 'none'; }
    const dim = 1 - 0.82 * outCubic(prog(t, tIts, 0.2));
    [dA, dB].forEach(e => { e.style.opacity = inv ? 0 : dim; e.style.transform = `translateY(${-30 * (1 - dim)}px)`; });
    const ph = outCubic(prog(t, tFacts, 0.18)); hs.style.color = '#F3EADB'; hs.style.opacity = t < tFacts ? 0 : (inv ? 0 : lerp(.35, 1, ph) * dim);
    hero.style.transform = `translateY(${10 * (1 - ph) - 30 * (1 - dim)}px)`;
    dC.style.opacity = t < tIts ? 0 : 1; writeOn(fs, t, tInv);
    const pf = outCubic(prog(t, tInv, 0.35)); film.style.left = (60 - 46 * (t - tInv)) + 'px'; film.style.top = '1110px'; film.style.opacity = pf;
  };
};

function pillEl(text, icon) { const p = $('div', 'pill', L.text); p.innerHTML = `<div class="glow"></div><div class="ic">${ICON[icon]}</div><div class="tx">${text}</div>`; p.style.display = 'flex'; const w = p.getBoundingClientRect().width; p.style.left = (540 - w / 2) + 'px'; p.style.display = 'none'; return p; }
function drawPill(p, t, t0, t1, y) { if (t < t0 || t >= t1) { p.style.display = 'none'; return; } p.style.display = 'flex'; p.style.top = y + 'px';
  const q = outCubic(prog(t, t0, 0.22)); p.style.clipPath = `inset(0 ${100 - q * 100}% 0 0 round 46px)`; p.style.opacity = 1 - prog(t, t1 - 0.12, 0.12); }

C.C7a = it => { const p = pillEl('HOW AM I?', 'person'); return t => drawPill(p, t, it.groups[0][0][0], it.t1, it.y - 46); };

C.C7b = it => {                                                    // R6: the questions stack as pills over the B-roll they name
  const g = it.groups[0]; const tPartner = g[0][0], tColl = g[4][0];
  const wrap = $('div', 'card', L.broll); const img = $('img', '', wrap); wrap.style.borderRadius = '0'; const shade = $('div', 'shade', L.broll);
  const p1 = pillEl('HOW AM I?', 'person'), p2 = pillEl('HOW IS MY PARTNER?', 'pair'), p3 = pillEl('HOW IS MY COLLEAGUE?', 'case');
  return async t => {
    const on = t >= it.t0 && t < it.t1; [wrap, shade].forEach(e => e.style.display = on ? 'block' : 'none');
    drawPill(p1, t, on ? it.t0 - 1 : 1e9, it.t1, 1040); drawPill(p2, t, tPartner, it.t1, 1150); drawPill(p3, t, tColl, it.t1, 1260);
    if (on) p1.style.clipPath = 'none';
    if (!on) return;
    const coll = t >= tColl, k = coll ? 'coworkers' : 'couple', t0 = coll ? tColl : tPartner;
    await setImg(img, frameB(k, Math.round((t - t0) * TL.fps) + 2)); brollCard(img, wrap, FULL);
    const pe = outCubic(prog(t, t0, 0.18)); wrap.style.transform = `translateX(${(coll ? -1 : 1) * (1 - pe) * 30}%)`; wrap.style.filter = pe < 1 ? `blur(${18 * (1 - pe)}px)` : 'none';
  };
};

C.C8 = it => {                                                     // MC: "PATTERNS" pinned while seven real sources flash behind it; then dominoes repeat
  const g = it.groups[0]; const tRep = g[3][0], tEnd = it.t1;
  const plate = $('div', 'plate', L.plate); const fl = $('img', 'full', plate); fl.style.objectFit = 'cover'; const dk = $('div', 'plate', plate); dk.style.display = 'block'; dk.style.background = 'rgba(10,15,13,.32)';
  const pin = $('div', 'cap', L.text); const ps = $('span', 'w', pin, 'PATTERNS'); ps.style.font = '700 200px/1 AR'; ps.style.letterSpacing = '-5px'; ps.style.color = '#F3EADB'; ps.style.textShadow = '0 10px 30px rgba(0,0,0,.6)';
  pin.style.display = 'block'; fitFont(ps, 880, 200); pin.style.top = '850px'; pin.style.display = 'none';
  const tiny = $('div', 'cap', L.text); tiny.style.top = '1070px'; const tl = $('div', 'line', tiny); const tw = [g[1], g[2]].map(w => { const s = wspan(tl, w, 'small'); tl.append(' '); return [s, w]; });
  const src = [['couple', 18], ['coworkers', 24], ['sunset', 40], ['book', 30], ['eye', 34], ['dominoes', 8], ['main', 640]];
  const bw = $('div', 'card', L.broll); const bimg = $('img', '', bw); bw.style.borderRadius = '0'; const sh = $('div', 'shade', L.broll);
  const rep = $('div', 'cap', L.text); rep.style.top = (1000) + 'px'; const rl = $('div', 'line', rep); const rs = wspan(rl, g[3], 'key');
  const echo = $('div', 'cap', L.text); echo.style.top = '1150px'; const el = $('div', 'line', echo);
  const o1 = wspan(el, g[4], 'white'); el.append(' '); const an = wspan(el, g[5], 'small'); el.append(' '); const o2 = wspan(el, g[6], 'white');
  const ghosts = [o1, o2].map(o => [1, 2, 3].map(k => { const c = o.cloneNode(true); c.style.position = 'absolute'; c.style.left = '0'; c.style.top = '0'; c.style.pointerEvents = 'none'; o.style.position = 'relative'; o.appendChild(c); return c; }));
  const ag = $('div', 'cap', L.text); ag.style.top = '1370px'; const al = $('div', 'line', ag); const ags = wspan(al, g[7], 'white'); ags.style.color = '#E9B86F';
  return async t => {
    const mc = t >= it.t0 && t < tRep - 0.02, on = t >= it.t0 && t < tEnd;
    plate.style.display = mc ? 'block' : 'none'; pin.style.display = mc ? 'block' : 'none'; tiny.style.display = mc ? 'block' : 'none';
    [bw, sh, rep, echo, ag].forEach(e => e.style.display = on && !mc ? 'block' : 'none');
    if (mc) { const j = Math.floor((t - it.t0) * TL.fps / 4) % src.length, [k, f] = src[j];
      await setImg(fl, k === 'main' ? `frames/main/${pad(f)}.jpg` : frameB(k, f)); tw.forEach(([s, w]) => arrive(s, t, w[0], 'small')); return; }
    if (!on) return;
    await setImg(bimg, frameB('dominoes', Math.round((t - tRep) * TL.fps) + 14)); brollCard(bimg, bw, FULL);
    arrive(rs, t, g[3][0], 'key'); [o1, an, o2].forEach((s, j) => arrive(s, t, [g[4], g[5], g[6]][j][0], j === 1 ? 'small' : 'white'));
    ghosts.forEach((gs, j) => { const tw0 = [g[4], g[6]][j][0]; gs.forEach((c, k) => { const p = outCubic(prog(t, tw0 + 0.04 * k, 0.35));
      c.style.opacity = t < tw0 || k > 1 ? 0 : [0.38, 0.16][k] * p; c.style.transform = `translateY(${(k + 1) * 60 * p}px)`; c.style.filter = `blur(${0.8 + k * 1.6}px)`; }); });
    arrive(ags, t, g[7][0], 'white'); [rep, echo, ag].forEach(e => exitFx(e, t, tEnd));
  };
};

C.C9 = it => {                                                     // R8: "seeing" written over the eye B-roll
  const g = it.groups[0]; const iS = g.findIndex(w => w[1].toLowerCase() === 'seeing');
  const pre = buildCaption({ kind: 'r7' }, g.slice(0, iS), L.text); layoutCap(pre, it.y);
  const cap = buildCaption({ kind: 'r8' }, g.slice(iS).map((w, j) => j === 0 ? [w[0], w[1], '~'] : w), L.text); layoutCap(cap, 1230, 620);
  const wrap = $('div', 'card', L.broll); const img = $('img', '', wrap); wrap.style.borderRadius = '0';
  const tE = g[iS][0] - 0.07;
  return async t => {
    drawCap(pre, t, it.t0, tE); drawCap(cap, t, tE, it.t1);
    const on = t >= tE && t < it.t1; wrap.style.display = on ? 'block' : 'none'; if (!on) return;
    await setImg(img, frameB('eye', Math.round((t - tE) * TL.fps) + 18)); brollCard(img, wrap, FULL);
    const p = outCubic(prog(t, tE, 0.26)); wrap.style.transform = `scale(${lerp(1.22, 1, p)})`; wrap.style.filter = p < 1 ? `blur(${18 * (1 - p)}px)` : 'none';
  };
};

C.C10 = it => {                                                    // R6 dark card with a glass icon; HL: the highlight wipes under "self-conversation" as he says it
  const g = it.groups[0]; const tSelf = g[1][0], tConv = g[2][0];
  const plate = $('div', 'plate', L.plate); plate.style.background = 'radial-gradient(70% 45% at 12% 88%, rgba(233,184,111,.42), rgba(233,184,111,0) 70%), radial-gradient(120% 90% at 60% 30%, #1E2B26, #0E1512 75%)';
  const icon = $('div', 'abs', L.text, ICON.talk); icon.style.left = '640px'; icon.style.top = '330px'; icon.style.filter = 'drop-shadow(0 18px 30px rgba(0,0,0,.45))';
  const tiny = $('div', 'cap', L.text); tiny.style.top = '960px'; const tl = $('div', 'line', tiny); tl.style.textAlign = 'left'; tl.style.paddingLeft = '120px';
  const ts = [g[0]].map(w => { const s = wspan(tl, w, 'small'); return [s, w]; });
  const mkLine = (txt, y) => { const d = $('div', 'abs', L.text); d.style.left = '120px'; d.style.top = y + 'px';
    const hl = $('div', 'abs', d); hl.style.cssText += ';left:-14px;top:12px;bottom:4px;background:#E9B86F;border-radius:12px';
    const s = $('span', 'w', d, txt); s.style.position = 'relative'; s.style.font = '700 118px/1.05 AR'; s.style.letterSpacing = '-3px'; s.style.color = '#F3EADB'; return [d, hl, s]; };
  const [d1, h1, s1] = mkLine('self-', 1030), [d2, h2, s2] = mkLine('conversation', 1155);
  return t => {
    const on = t >= it.t0 && t < it.t1; [plate, icon, tiny, d1, d2].forEach(e => e.style.display = on ? 'block' : 'none'); if (!on) return;
    const pi = outCubic(prog(t, it.t0, 0.25)); icon.style.opacity = pi; icon.style.transform = `translateY(${(1 - pi) * 30}px) translateY(${Math.sin(t * 2.2) * 6}px)`;
    ts.forEach(([s, w]) => arrive(s, t, Math.max(w[0], it.show0 || 0), 'small'));
    [[s1, h1, d1, tSelf, 0.22], [s2, h2, d2, tConv - 0.05, 0.36]].forEach(([s, h, d, tw, dur]) => {
      arrive(s, t, tw, 'key'); const p = outCubic(prog(t, tw + 0.05, dur)); h.style.width = `calc(${p * 100}% + 28px)`; h.style.opacity = t < tw + 0.05 ? 0 : 1;
      s.style.color = p > 0.6 ? '#17231F' : '#F3EADB'; d.style.width = s.getBoundingClientRect().width + 'px'; });
    [tiny, d1, d2, icon].forEach(e => { e.style.opacity = (e === icon ? pi : 1) * (1 - prog(t, it.t1 - 0.12, 0.12)); });
  };
};

C.C12 = it => {                                                    // R5: the live video shrinks into a phone; a share sheet slides up; R8 boxed lines
  const g = it.groups[0]; const tSheet = g[2][0], tWho = g[4][0];
  const board = $('div', 'plate', L.bg); board.style.background = 'radial-gradient(110% 70% at 50% 35%, #2A3C35, #121B17 72%)';
  const phone = { x: 318, y: 170, w: 444, h: 950, r: 58 };
  const bez = $('div', 'abs', L.fx); bez.style.cssText += `;left:${phone.x - 14}px;top:${phone.y - 14}px;width:${phone.w + 28}px;height:${phone.h + 28}px;border-radius:72px;border:14px solid #0A100D;box-sizing:border-box;box-shadow:0 40px 80px rgba(0,0,0,.5);display:none`;
  const notch = $('div', 'abs', bez); notch.style.cssText += ';left:50%;top:16px;width:120px;height:30px;margin-left:-60px;border-radius:16px;background:#0A100D';
  const sheet = $('div', 'abs', L.fx); sheet.style.cssText += `;left:${phone.x}px;width:${phone.w}px;height:340px;border-radius:30px 30px ${phone.r}px ${phone.r}px;background:#F3EADB;overflow:hidden;display:none`;
  sheet.innerHTML = `<div style="margin:14px auto 0;width:64px;height:6px;border-radius:3px;background:rgba(30,43,38,.25)"></div>
    <div style="font:700 30px AR;color:#1E2B26;margin:18px 0 0 30px">Share</div>
    <div style="display:flex;gap:22px;margin:24px 0 0 30px">${['#E9B86F', '#6E8C7E', '#C98A5A', '#3E5A50'].map(c => `<div style="width:76px;height:76px;border-radius:50%;background:radial-gradient(circle at 35% 30%, #fff8, ${c} 60%)"></div>`).join('')}</div>
    <div style="margin:30px 30px 0;height:74px;border-radius:37px;background:#E9B86F;font:700 30px/74px AR;color:#17231F;text-align:center;letter-spacing:1px">Send</div>`;
  const mkBox = (words, y) => { const b = $('div', 'box', L.text); b.style.top = y + 'px'; const sp = words.map(w => { const s = wspan(b, w, ''); b.append(' '); return [s, w]; });
    b.style.display = 'block'; const w = b.getBoundingClientRect().width; b.style.left = (540 - w / 2) + 'px'; b.style.display = 'none'; return [b, sp]; };
  const [b1, sp1] = mkBox(g.slice(0, 4), 1190), [b2, sp2] = mkBox(g.slice(4), 1290);
  return t => {
    const on = t >= it.t0 && t < it.t1; board.style.display = bez.style.display = on ? 'block' : 'none';
    sheet.style.display = on && t >= tSheet ? 'block' : 'none'; b1.style.display = on ? 'block' : 'none'; b2.style.display = on && t >= tWho ? 'block' : 'none';
    if (!on) return null;
    const p = inOut(prog(t, it.t0, 0.33)); bez.style.opacity = prog(t, it.t0 + 0.18, 0.15);
    const ps = outExpo(prog(t, tSheet, 0.35)); sheet.style.top = (phone.y + phone.h - 340 * ps) + 'px';
    for (const [s, w] of [...sp1, ...sp2]) arrive(s, t, Math.max(w[0], it.show0 || 0), 'small');
    [b1, b2].forEach((b, j) => { const tb = j ? tWho : Math.max(g[0][0], it.show0 || 0); const q = outCubic(prog(t, tb, 0.18)); b.style.opacity = q; b.style.transform = `translateY(${(1 - q) * 14}px)`; });
    return lerpRect(FULL, phone, p);
  };
};

// hook accent: a glass speech bubble (the story you tell yourself), with a small callback on "talking to yourself"
function bubble(t0, t1, x, y, w) { const b = $('div', 'abs', L.text, ICON.bubble(w)); b.style.left = x + 'px'; b.style.top = y + 'px'; b.style.filter = 'drop-shadow(0 14px 22px rgba(0,0,0,.4))';
  return t => { if (t < t0 || t >= t1) { b.style.display = 'none'; return; } b.style.display = 'block'; const p = outExpo(prog(t, t0, 0.35));
    b.style.opacity = p * (1 - prog(t, t1 - 0.15, 0.15)); b.style.transform = `scale(${lerp(.6, 1, p)}) translateY(${Math.sin(t * 2.4) * 6}px)`; }; }

window.init = tl => {
  TL = tl; FPS = tl.fps; stage = document.getElementById('stage');
  L.cardwrap = document.getElementById('cardwrap'); L.main = document.getElementById('main');
  L.bg = $('div', 'full'); stage.insertBefore(L.bg, L.cardwrap);
  ['broll', 'plate', 'fx', 'text'].forEach(k => { L[k] = $('div', 'full'); });
  for (const it of tl.items) {
    if (C[it.kind]) comps.push([it, C[it.kind](it)]);
    else { const cap = buildCaption(it, it.groups[0], L.text); layoutCap(cap, it.y); items.push([it, cap]); }
  }
  const hook = tl.items[0], tb = tl.items.find(x => x.kind === 'r8bold');
  comps.push([null, bubble(0.15, tl.items[2].t0, 806, 286, 170)]);
  comps.push([null, bubble(tb.t0 + 0.2, tb.t1, 860, tb.y - 230, 120)]);
};
window.renderAt = async t => {
  const i = Math.min(TL.n - 1, Math.round(t * FPS));
  let rect = null;
  for (const [it, f] of comps) { const r = await f(t, i); if (r && typeof r === 'object' && 'w' in r) rect = r; }
  for (const [it, cap] of items) drawCap(cap, t, it.show0 || it.t0, endOf(it));
  await setImg(L.main, frameMain(i)); placeMain(i, rect, t);
};
})();
