// Move with Raghu "back to facts" update: every frame is a pure function of time (renderAt(t)).
// Type: Anton (headlines), Mont SemiBold (captions), DM Sans Medium (supporting text). One accent: yellow.
// Motion: motion-graphics-craft M6 (one object, the yellow marker, travels through UI states: toggle, comments, stat cards, channels, poll, follow).
'use strict';
const $ = (tag, cls, parent, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; (parent || document.body).appendChild(e); return e; };
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x)), prog = (t, t0, d) => clamp((t - t0) / Math.max(1e-4, d));
const lerp = (a, b, p) => a + (b - a) * p, outCubic = p => 1 - Math.pow(1 - p, 3), inOut = p => p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
const outBack = (p, s = 1.5) => 1 + (s + 1) * Math.pow(p - 1, 3) + s * Math.pow(p - 1, 2);
let TL, K, FPS, comps = [], LAYOUT = 'B', CAPMODE = 'tg', CAPS = null, FRAME = [];
const L = {};
async function setImg(el, src) { if (el._src === src) return; el._src = src; el.src = src; try { await el.decode(); } catch (e) {} }
const frameMain = i => `frames/main/${String(Math.max(0, Math.min(TL.n - 1, i))).padStart(5, '0')}.jpg`;
const show = (el, on) => { el.style.display = on ? 'block' : 'none'; };
const WY = 317, WH = 1286;                                   // the 1080x1286 picture window (layout B)
function pop(el, t, t0, base = '', d = 0.3, from = 1.3) { const p = prog(t, t0, d); el.style.opacity = t < t0 ? 0 : clamp((t - t0) / 0.05); el.style.transform = `${base} scale(${lerp(from, 1, outBack(p, 1.3))})`; }
function rise(el, t, t0, d = 0.28, dy = 40) { const p = outCubic(prog(t, t0, d)); el.style.opacity = t < t0 ? 0 : p; el.style.transform = `translateY(${lerp(dy, 0, p)}px)`; el.style.filter = p < 1 ? `blur(${lerp(8, 0, p)}px)` : 'none'; }
function marker(el, t, t0, d = 0.16) { const p = outCubic(prog(t, t0, d)); el.style.clipPath = `inset(0 ${100 - 100 * p}% 0 0 round .16em)`; }

// ---------------------------------------------------------------- speaker (framed window B, or full screen A), face follow, punches on key words
const PUSH = { hook: [1.00, 1.05], toggle: [1.02, 1.06], thanks: [1.03, 1.08], why: [1.00, 1.05], support: [1.02, 1.07], finally: [1.05, 1.08], follow: [1.0, 1.04] };
const STEPS = () => [K.guys, K.kada, K.thank, K.enduku, K.yes, K.support3, K.support4, K.finallyw, K.follow];
function camAt(t, sc) {                                     // scale and offset of the speaker picture at time t (same maths for picture and text)
  const i = Math.min(TL.n - 1, Math.round(t * FPS)), f = TL.face, k = Math.min(f.cx.length - 1, i), cx = f.cx[k], cy = f.cy[k], fw = f.fw[k];
  const [p0, p1] = PUSH[sc.id] || [1, 1]; let p = lerp(p0, p1, inOut(prog(t, sc.t0, sc.t1 - sc.t0)));
  if (sc.id === 'wait') { const n = [K.wait1, K.wait2, K.wait3, K.wait4].filter(x => t >= x - .03).length; p = 1 + 0.07 * n; }       // "wait wait wait wait": four hard punches
  const st = STEPS().filter(x => x >= sc.t0 && x < sc.t1); let z = 0;
  for (let j = 0; j < st.length; j++) { if (t < st[j] - .06) break; const q = inOut(prog(t, st[j] - .06, .18)); z = j % 2 === 0 ? q : 1 - q; }
  p *= 1 + 0.05 * z;
  let s, x, y;
  if (LAYOUT === 'B') { s = p; x = clamp(540 - cx * s, 1080 - 1080 * s, 0); y = WY + clamp(560 - cy * s, WH - WH * s, 0); }
  else { s = 1920 / WH * p; x = clamp(540 - cx * s, 1080 - 1080 * s, 0); y = clamp(700 - cy * s, 1920 - WH * s, 0); }
  return { s, x, y, chin: y + (cy + 0.62 * fw) * s };       // chin = bottom of the face box in screen pixels
}
async function drawSpeaker(t, i, sc) {
  const m = document.getElementById('main'); await setImg(m, frameMain(i));
  const c = camAt(t, sc); m.style.transform = `translate(${c.x}px, ${c.y}px) scale(${c.s})`;
  document.getElementById('Lmain').style.clipPath = LAYOUT === 'B' ? `inset(${WY}px 0 ${1920 - WY - WH}px 0)` : 'none';
}
// owner 2026-11-28: text never sits on his face. Lowest chin over the phrase (punches included) + a margin = the highest the text may start.
const FACE_GAP = 46, TEXT_FLOOR = 1588;
function chinMax(t0, t1, sc) { let m = 0; for (let t = t0; t <= t1; t += 1 / 30) { const s2 = TL.scenes.find(x => t >= x.t0 && t < x.t1) || sc; if (SPEAKER.has(s2.id)) m = Math.max(m, camAt(t, s2).chin); } return m; }   // a phrase may cross a cut: use each moment's own scene

// ---------------------------------------------------------------- captions: Mont SemiBold, words build in as spoken, yellow marker on key words
function drawCaps(t, hide) {
  const c = TL.caps.find(c => t >= c.t0 - 0.03 && t < c.t1);
  if (!c || hide || CAPMODE === 'none') { CAPS.style.display = 'none'; return; }
  CAPS.style.display = 'flex';
  if (CAPMODE === 'en') { const en = (TL.caps_en || []).find(x => t >= x[0] && t < x[1]); CAPS.innerHTML = en ? en[2].split(' ').map(w => `<span class="cw${w.startsWith('*') ? ' hl' : ''}">${w.replace('*', '')}</span>`).join('') : ''; CAPS._c = null; return; }
  if (CAPS._c !== c) { CAPS._c = c; CAPS.innerHTML = ''; c.els = c.words.map(([tw, w, h]) => [tw, $('span', 'cw' + (h ? ' hl' : ''), CAPS, w), h]); }
  c.els.forEach(([tw, e, h]) => { const p = outCubic(prog(t, tw - .04, .16)); e.style.opacity = t < tw - .04 ? 0 : p; e.style.transform = `translateY(${lerp(18, 0, p)}px) scale(${lerp(.92, 1, p)})`; if (h) marker(e, t, tw - .02, .18); });
}

// ---------------------------------------------------------------- typography v2: phrase lockups built word by word as spoken
let LKEL = null;
function drawLockups(t, allow) {
  const L0 = allow ? (TL.lockups || []).find(x => t >= x.t0 - .03 && t < x.t1) : null;
  if (!L0) { LKEL.style.display = 'none'; return; }
  LKEL.style.display = 'block';
  if (LKEL._l !== L0) { LKEL._l = L0; LKEL.innerHTML = ''; const n = L0.lines.length, dx = n === 3 ? [-46, 10, 64] : n === 2 ? [-34, 44] : [0];
    L0.els = []; L0.lines.forEach((ln, j) => { const row = $('div', 'lkl', LKEL); row.style.marginLeft = (2 * dx[j]) + 'px';
      const prevScriptOnly = j && L0.lines[j - 1].every(w => w[2].startsWith('s')); if (j) row.style.marginTop = prevScriptOnly ? '6px' : '-14px';      // a script-only line needs room for its tails
      ln.forEach(([tw, w, role]) => { const r = role.replace('*', ''), e = $('span', 'lkw ' + r + (role.includes('*') ? ' y' : ''), row, w); L0.els.push([tw, e, r]); }); });
    const sc = TL.scenes.find(x => L0.t0 >= x.t0 - .01 && L0.t0 < x.t1), spk = sc && SPEAKER.has(sc.id);
    LKEL.style.transform = 'none'; LKEL.style.top = '0px'; const h0 = LKEL.getBoundingClientRect().height;
    const w0 = Math.max(...[...LKEL.querySelectorAll('.lkl')].map(r => { const a = [...r.children].map(e => e.getBoundingClientRect()); return a.length ? Math.max(...a.map(b => b.right)) - Math.min(...a.map(b => b.left)) + Math.abs(parseFloat(r.style.marginLeft) || 0) : 0; }));
    let k = Math.min(L0.scale, 1000 / w0), top;          // owner 2026-11-28: two lines at most, so a line can run long; keep it inside a 1000 px column
    if (spk) { const lim = chinMax(L0.t0, L0.t1, sc) + FACE_GAP; top = Math.max(lim, 1170); if (top + h0 * k > TEXT_FLOOR) k = Math.max(.72, (TEXT_FLOOR - top) / h0); L0._chin = lim; }
    else top = L0.y - h0 * k / 2;
    LKEL.style.transformOrigin = '50% 0'; LKEL.style.transform = `scale(${k})`; LKEL.style.top = top + 'px'; }
  const lw = Math.max(...L0.lines.flat().map(w => w[0])), xs = Math.min(L0.t1 - .02, Math.max(L0.t1 - .12, lw + .1)), ex = prog(t, xs, L0.t1 - xs);   // the last word always gets 0.1 s before the fade LKEL.style.opacity = 1 - ex; LKEL.style.filter = ex > 0 ? `blur(${8 * ex}px)` : 'none';
  L0.els.forEach(([tw, e, r]) => { const t0 = tw - .04;
    if (r === 's') { const p = outCubic(prog(t, t0, .38)), x = lerp(-16, 124, p), m = p >= 1 ? 'none' : `linear-gradient(90deg, #000 ${x - 14}%, rgba(0,0,0,.35) ${x - 4}%, transparent ${x}%)`;
      e.style.webkitMaskImage = m; e.style.opacity = t < t0 ? 0 : 1; }
    else if (r === 'B' || r === 'b') { const p = prog(t, t0, .24); e.style.opacity = t < t0 ? 0 : clamp((t - t0) / .05); e.style.transform = `scale(${lerp(1.16, 1, outBack(p, 1.2))})`; }
    else if (r === 'i') { const p = outCubic(prog(t, t0, .26)); e.style.opacity = t < t0 ? 0 : p; e.style.transform = `translateX(${lerp(-26, 0, p)}px)`; }
    else { const p = outCubic(prog(t, t0, .2)); e.style.opacity = t < t0 ? 0 : p; e.style.transform = `translateY(${lerp(16, 0, p)}px)`; e.style.filter = p < 1 ? `blur(${lerp(6, 0, p)}px)` : 'none'; } });
}
// ---------------------------------------------------------------- scenes
const C = {};
C.hook_v1 = sc => { const w = $('div', 'anton', L.text, '<span class="y">SUPPORT</span>'); w.style.cssText += ';position:absolute;left:0;right:0;top:1120px;text-align:center;font-size:210px';
  const ul = $('div', 'abs', L.text); ul.style.cssText += ';left:250px;top:1330px;width:580px;height:14px;border-radius:7px;background:#FFD60A;transform-origin:0 50%';
  return t => { show(w, 1); show(ul, 1); pop(w, t, K.support1 - .04); ul.style.transform = `scaleX(${outCubic(prog(t, K.support1 + .12, .3))})`; ul.style.opacity = t > K.support1 ? 1 : 0; }; };
C.wait = sc => {                                             // four WAIT stamps stacking up the frame, one per "wait"
  const ws = [0, 1, 2, 3].map(j => { const e = $('div', 'anton', L.text, j % 2 ? '<span class="y">WAIT</span>' : 'WAIT'); e.style.cssText += `;position:absolute;left:0;right:0;top:1150px;text-align:center;font-size:190px;transform-origin:50% 60%`; return e; });
  const pz = $('div', 'abs', L.text, '<span style="position:absolute;left:0;top:0;width:26px;height:84px;border-radius:8px;background:#fff"></span><span style="position:absolute;left:44px;top:0;width:26px;height:84px;border-radius:8px;background:#fff"></span>'); pz.style.cssText += ';left:960px;top:360px;width:70px;height:84px';
  const WT = () => [K.wait1, K.wait2, K.wait3, K.wait4];          // each WAIT replaces the last on the chest, a little bigger, with the punch
  return t => { ws.forEach(e => show(e, 0)); show(pz, 1); pop(pz, t, K.guys, '', .2); };
};
C.toggle = sc => {                                           // UNNAVA <-> POYAVA switch: the knob jumps on each word, a ? on "kada"
  const tg = $('div', 'abs', L.mg); tg.style.cssText += ';left:120px;top:1140px;width:840px;height:160px;border-radius:80px;background:rgba(22,22,24,.86);box-shadow:inset 0 0 0 2px rgba(255,255,255,.14),0 24px 60px rgba(0,0,0,.55);backdrop-filter:blur(8px)';
  const knob = $('div', 'abs', tg); knob.style.cssText += ';left:12px;top:12px;width:408px;height:136px;border-radius:68px;background:#FFD60A;box-shadow:0 10px 30px rgba(255,214,10,.35)';
  const a = $('div', 'anton', tg, 'UNNAVA'), b = $('div', 'anton', tg, 'POYAVA'); [a, b].forEach((e, j) => { e.style.cssText += `;position:absolute;top:42px;left:${j ? 420 : 12}px;width:408px;text-align:center;font-size:66px;text-shadow:none`; });
  const q = $('div', 'abs', L.text); q.style.cssText += ';left:0;width:1080px;top:1330px;text-align:center';
  q.innerHTML = '<span class="lkw l" style="font-size:58px">cheppu ani alochistharu</span><span class="lkw s" style="font-size:150px">kada?</span>'; const [q1, q2] = q.children;
  const top0 = Math.max(1150, chinMax(sc.t0, sc.t1, sc) + FACE_GAP); tg.style.top = top0 + 'px'; q.style.top = (top0 + 186) + 'px';
  return t => { [tg, q].forEach(e => show(e, 1)); rise(tg, t, sc.t0 + .02, .3); const kx = outBack(prog(t, K.poyava - .05, .28), 1.2);
    knob.style.left = (t < K.unnava - .05 ? 12 : lerp(12, 420, t < K.poyava - .05 ? 0 : kx)) + 'px'; knob.style.opacity = t < K.unnava - .05 ? 0 : 1;
    a.style.color = t >= K.unnava - .05 && t < K.poyava - .05 ? '#111' : '#fff'; b.style.color = t >= K.poyava - .05 ? '#111' : '#fff'; q.style.display = 'block'; rise(q1, t, 5.24, .25, 16); const p2 = outCubic(prog(t, K.kada - .04, .38)), x2 = lerp(-16, 124, p2); q2.style.webkitMaskImage = p2 >= 1 ? 'none' : `linear-gradient(90deg, #000 ${x2 - 14}%, rgba(0,0,0,.35) ${x2 - 4}%, transparent ${x2}%)`; q2.style.opacity = t < K.kada - .04 ? 0 : 1; };
};
C.comments = sc => {                                         // YouTube-style comment list (PLACEHOLDER rows until the owner sends real screenshots)
  const bg = $('div', 'L', L.bg); bg.style.background = '#0F0F0F';
  const hd = $('div', 'abs', L.mg, '<span class="dmw" style="font-size:54px;font-weight:700">Comments</span>'); hd.style.cssText += ';left:70px;top:330px';
  // owner 2026-11-28: "all comments are same ... add like real": four different wordings of the question he says viewers asked; names and photos stay blurred
  const T = ['Bro <b>unnava poyava?</b> cheppu', 'Anna <b>ekkada unnav?</b> 🤔', 'Bro <b>unnava?</b> video ledu', '<b>Poyava</b> bro? reply ivvu 😅'];
  const AV = ['#6b5a4a,#2e2620', '#4a5a6b,#20262e', '#5a4a6b,#26202e', '#4a6b55,#202e24'];
  const rows = T.map((tx, j) => { const r = $('div', 'abs', L.mg); r.style.cssText += `;left:70px;top:${450 + j * 250}px;width:940px;height:220px`;
    r.innerHTML = `<div class="av blur" style="left:0;top:10px;width:96px;height:96px;background:linear-gradient(135deg,${AV[j]})"></div>
      <div class="blur" style="position:absolute;left:126px;top:18px;width:${210 + 40 * (j % 3)}px;height:26px;border-radius:13px;background:#55555b"></div>
      <div style="position:absolute;left:126px;top:58px;font:600 52px/1.25 Mont;color:#F1F1F1;white-space:nowrap">${tx.replace(/<b>(.*?)<\/b>/, '<span class="hlw" style="position:relative;display:inline-block;padding:0 .18em;color:#111"><i style="position:absolute;inset:0;border-radius:.14em;background:#FFD60A;z-index:-1"></i>$1</span>')}</div>
      <div class="dm" style="position:absolute;left:126px;top:142px;font-size:30px">👍&nbsp;&nbsp;👎&nbsp;&nbsp;&nbsp;Reply</div>`; return r; });
  return t => { [bg, hd, ...rows].forEach(e => show(e, 1)); rise(hd, t, sc.t0, .25, 20);
    rows.forEach((r, j) => { const t0 = j === 0 ? K.comments : K.chaala + (j - 1) * .16; rise(r, t, t0, .3, 70); const hl = r.querySelector('.hlw i'); if (hl) hl.style.clipPath = `inset(0 ${100 - 100 * outCubic(prog(t, (j === 0 ? K.bro : t0 + .2), .2))}% 0 0)`; }); };
};
C.thanks_v1 = sc => { const a = $('div', 'anton', L.text, 'THANK <span class="y">YOU</span>'); a.style.cssText += ';position:absolute;left:0;right:0;top:1130px;text-align:center;font-size:200px';
  return t => { show(a, 1); pop(a, t, K.thank - .04, '', .3, 1.4); }; };
C.stats = sc => {                                            // three real numbers from the owner's screenshots, counted up as he says them
  const bg = $('div', 'L', L.bg); bg.style.background = 'radial-gradient(1200px 900px at 50% 30%, #1d1d20 0%, #0A0A0B 70%)';
  const kick = $('div', 'dm', L.text, 'APPROXIMATELY'); kick.style.cssText += ';position:absolute;left:0;right:0;top:250px;text-align:center;font-size:36px;letter-spacing:.32em;text-indent:.32em';
  const D = [['avatar_move_with_raghu.png', 'move with raghu', 'Instagram', 10000, 'followers', K.insta, K.k10a, '10K'], ['avatar_raqvine.png', 'Raqvine', 'YouTube · first channel', 27296, 'subscribers', K.first, K.k27],
             ['avatar_move_with_raghu.png', 'Move with raghu', 'YouTube · second channel', 10106, 'subscribers', K.second, K.k10b]];
  const cards = D.map(([av, nm, sub, num, unit, tin, tn, short], j) => { const c = $('div', 'card', L.mg); c.style.cssText += `;left:60px;top:${340 + j * 400}px;width:960px;height:360px`;
    c.innerHTML = `<div class="av" style="left:44px;top:44px;width:150px;height:150px"><img src="assets/${av}"></div>
      <div class="dmw" style="position:absolute;left:224px;top:62px;font-size:50px;font-weight:700">${nm}</div><div class="dm" style="position:absolute;left:224px;top:126px;font-size:36px">${sub}</div>
      <div class="num anton" style="position:absolute;left:44px;top:222px;font-size:100px;text-shadow:none">0</div><div class="dm" style="position:absolute;left:560px;top:262px;font-size:40px">${unit}</div>`;
    return { c, num: c.querySelector('.num'), n: num, tin, tn, short, unitEl: c.querySelectorAll('.dm')[1] }; });
  return t => { [bg, kick, ...cards.map(o => o.c)].forEach(e => show(e, 1)); rise(kick, t, sc.t0 + .3, .3, 16);
    cards.forEach((o, j) => { rise(o.c, t, o.tin - .1, .32, 80); const q = outCubic(prog(t, o.tn - .05, .6)); const v = Math.round(o.n * q);
      o.num.textContent = o.short ? (q >= 1 ? o.short : Math.round(10 * q) + 'K') : v.toLocaleString('en-US'); o.num.style.color = t >= o.tn - .05 ? '#FFD60A' : '#fff';
      o.unitEl.style.left = (o.num.getBoundingClientRect().width + 74) + 'px';
      o.c.style.boxShadow = t >= o.tn - .05 && (j === 2 || t < cards[j + 1].tin - .1) ? '0 30px 80px rgba(0,0,0,.55), inset 0 0 0 4px #FFD60A' : '0 30px 80px rgba(0,0,0,.55), inset 0 0 0 1.5px rgba(255,255,255,.10)'; }); };
};
C.you = sc => { const bg = $('div', 'L', L.bg); bg.style.background = '#0A0A0B';
  const a = $('div', 'anton', L.text, 'ALL OF THIS'), b = $('div', 'anton', L.text, 'BECAUSE OF'), c = $('div', 'anton', L.text, '<span class="y">YOU</span>');
  [[a, 560, 150], [b, 720, 150], [c, 890, 420]].forEach(([e, y, s]) => { e.style.cssText += `;position:absolute;left:0;right:0;top:${y}px;text-align:center;font-size:${s}px`; });
  return t => { show(bg, 1); [a, b, c].forEach(e => show(e, 0)); }; };
C.why = sc => { const w = $('div', 'anton', L.text, 'WHY?'); w.style.cssText += ';position:absolute;left:0;right:0;top:1150px;text-align:center;font-size:200px';
  // owner 2026-11-28 (two lines max, less text): the "coming to that…" chip repeated his own words and hit the lockup; now one straight yellow line under the phrase fills up to the cut
  const tr = $('div', 'abs', L.mg), bar = $('div', 'abs', L.mg);
  tr.style.cssText += ';left:330px;width:420px;height:6px;border-radius:3px;background:rgba(255,255,255,.18)';
  bar.style.cssText += ';left:330px;width:420px;height:6px;border-radius:3px;background:#FFD60A;transform-origin:0 50%;box-shadow:0 0 18px rgba(255,214,10,.35)';
  WHYBAR = t => { const row = [...LKEL.querySelectorAll('.lkl')].pop(), on = LKEL.style.display !== 'none' && row && t >= K.yes;
    if (!on) { tr.style.opacity = bar.style.opacity = 0; return; }
    const y = Math.max(...[...row.children].map(e => e.getBoundingClientRect().bottom)) + 30, a = outCubic(prog(t, K.yes, .25));
    tr.style.top = bar.style.top = y + 'px'; tr.style.opacity = a * (+LKEL.style.opacity || 1); bar.style.opacity = tr.style.opacity;
    tr.style.transform = `scaleX(${a})`; bar.style.transform = `scaleX(${prog(t, K.akkadike, sc.t1 - K.akkadike)})`; };
  return t => { show(w, 0); show(tr, 1); show(bar, 1); }; };
let WHYBAR = null;
function channelTiles(parent) {
  const bg = $('div', 'L', L.bg); bg.style.background = 'radial-gradient(1200px 900px at 50% 40%, #1d1d20 0%, #0A0A0B 70%)';
  const kick = $('div', 'dm', L.text, 'MY CHANNELS'); kick.style.cssText += ';position:absolute;left:0;right:0;top:250px;text-align:center;font-size:36px;letter-spacing:.32em;text-indent:.32em';
  const mk = (y, av, name, big, size) => { const c = $('div', 'card', L.mg); c.style.cssText += `;left:60px;top:${y}px;width:960px;height:440px`;
    c.innerHTML = `<div class="av" style="left:44px;top:44px;width:130px;height:130px"><img src="assets/${av}"></div><div class="dmw" style="position:absolute;left:200px;top:66px;font-size:46px;font-weight:700">${name}</div>
      <div class="anton big" style="position:absolute;left:44px;top:210px;font-size:${size}px;text-shadow:none">${big}</div>`; return c; };
  const a = mk(340, 'avatar_raqvine.png', 'Raqvine · 1st channel', 'FACTS', 150), b = mk(840, 'avatar_move_with_raghu.png', 'Move with raghu · 2nd channel', 'CHALLENGE &amp; ENTERTAINMENT', 70);
  b.querySelector('.big').style.whiteSpace = 'normal'; b.querySelector('.big').style.width = '880px';
  const arr = $('div', 'abs', L.text, '<svg width="160" height="560" viewBox="0 0 160 560" style="overflow:visible"><path id="ar" d="M 80 20 C 190 160, 190 400, 80 540" fill="none" stroke="#FFD60A" stroke-width="12" stroke-linecap="round"/><path id="ah" d="M 52 508 L 80 540 L 112 512" fill="none" stroke="#FFD60A" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>');
  arr.style.cssText += ';left:880px;top:560px;transform-origin:50% 50%';
  return { bg, kick, a, b, arr };
}
C.channels = sc => { const o = channelTiles(); const ar = o.arr.querySelector('#ar'); let len = 0;
  return t => { [o.bg, o.kick, o.a, o.b].forEach(e => show(e, 1)); rise(o.kick, t, sc.t0, .25, 16); rise(o.a, t, K.facts1 - .3, .3, 80); rise(o.b, t, K.second2 - .1, .3, 80);
    o.a.style.boxShadow = t >= K.facts1 && t < K.second2 ? '0 30px 80px rgba(0,0,0,.55), inset 0 0 0 4px #FFD60A' : ''; o.b.style.boxShadow = t >= K.challenge ? '0 30px 80px rgba(0,0,0,.55), inset 0 0 0 4px #FFD60A' : '';
    o.a.querySelector('.big').style.color = t >= K.facts1 && t < K.second2 ? '#FFD60A' : '#fff'; o.b.querySelector('.big').style.color = t >= K.challenge ? '#FFD60A' : '#fff';
    show(o.arr, 1); if (!len) { len = ar.getTotalLength(); ar.style.strokeDasharray = len; } const q = outCubic(prog(t, K.second2 - .2, .4)); ar.style.strokeDashoffset = len * (1 - q); o.arr.querySelector('#ah').style.opacity = q > .9 ? 1 : 0; o.arr.style.opacity = q > 0 ? 1 : 0; }; };
C.back = sc => { const o = channelTiles(); const ar = o.arr.querySelector('#ar'); let len = 0; o.arr.style.transform = 'scaleY(-1)';
  const st = $('div', 'anton', L.text, 'BACK TO <span class="y">FACTS</span>'); st.style.cssText += ';position:absolute;left:0;right:0;top:1340px;text-align:center;font-size:150px';
  return t => { [o.bg, o.kick, o.a, o.b, o.arr, st].forEach(e => show(e, 1));
    const back = t >= K.facts2 - .05; o.a.style.boxShadow = back ? '0 30px 80px rgba(0,0,0,.55), inset 0 0 0 4px #FFD60A' : ''; o.a.querySelector('.big').style.color = back ? '#FFD60A' : '#fff';
    o.b.style.opacity = lerp(1, .45, prog(t, K.ippudu, .3)); if (!len) { len = ar.getTotalLength(); ar.style.strokeDasharray = len; } const q = outCubic(prog(t, K.ippudu, .45)); ar.style.strokeDashoffset = len * (1 - q); o.arr.querySelector('#ah').style.opacity = q > .9 ? 1 : 0;
    show(st, 0); }; };
C.support = sc => { const hs = [0, 1, 2, 3, 4, 5].map(j => { const h = $('div', 'abs', L.text, `<svg width="70" height="64" viewBox="0 0 70 64"><path d="M35 60 C 10 42, 2 28, 2 18 A 16 16 0 0 1 35 12 A 16 16 0 0 1 68 18 C 68 28, 60 42, 35 60 Z" fill="${j % 2 ? '#FFD60A' : '#FF3B5C'}"/></svg>`); h.style.cssText += `;left:${905 + (j % 2) * 70}px;top:1520px`; return h; });
  return t => { hs.forEach((h, j) => { show(h, 1); const t0 = K.support4 + j * .09, p = prog(t, t0, 1.1); h.style.opacity = p > 0 && p < 1 ? Math.min(1, (1 - p) * 2) : 0; h.style.transform = `translate(${Math.sin(p * 6 + j) * 14}px, ${-430 * outCubic(p)}px) scale(${lerp(.6, 1, p)})`; }); }; };
C.poll = sc => {                                             // community-post-style question; the cursor taps "Yes" on "support" (no fake percentages)
  const bg = $('div', 'L', L.bg); bg.style.background = '#0F0F0F';
  const c = $('div', 'card', L.mg); c.style.cssText += ';left:70px;top:520px;width:940px;height:760px';
  c.innerHTML = `<div class="av" style="left:44px;top:44px;width:100px;height:100px"><img src="assets/avatar_raqvine.png"></div><div class="dmw" style="position:absolute;left:170px;top:52px;font-size:40px;font-weight:700">Raqvine</div><div class="dm" style="position:absolute;left:170px;top:102px;font-size:30px">community question</div>
    <div style="position:absolute;left:44px;top:190px;font:700 66px/1.18 Mont;color:#fff">Nannu support<br>chestara? 🙏</div>
    <div class="opt" style="position:absolute;left:44px;top:420px;width:852px;height:120px;border-radius:60px;box-shadow:inset 0 0 0 3px rgba(255,255,255,.25);overflow:hidden"><div class="fill" style="position:absolute;inset:0;background:#FFD60A;transform-origin:0 50%;transform:scaleX(0)"></div><div class="lab" style="position:absolute;left:48px;top:30px;font:700 52px/1 Mont;color:#fff">Yes, support! 💛</div><div class="chk anton" style="position:absolute;right:44px;top:22px;font-size:70px;color:#111;opacity:0">✓</div></div>
    <div style="position:absolute;left:44px;top:570px;width:852px;height:120px;border-radius:60px;box-shadow:inset 0 0 0 3px rgba(255,255,255,.25)"><div style="position:absolute;left:48px;top:30px;font:700 52px/1 Mont;color:#fff">No</div></div>`;
  const cur = $('div', 'abs', L.text, '<svg width="96" height="114" viewBox="0 0 44 52"><path d="M4 2 L40 30 L24 32 L32 48 L25 51 L17 35 L6 46 Z" fill="#fff" stroke="#111" stroke-width="3" stroke-linejoin="round"/></svg>');
  return t => { [bg, c, cur].forEach(e => show(e, 1)); rise(c, t, sc.t0 + .02, .32, 90);
    const cp = outCubic(prog(t, K.support5 - .45, .45)); cur.style.left = lerp(980, 640, cp) + 'px'; cur.style.top = lerp(1700, 1010, cp) + 'px'; cur.style.opacity = prog(t, K.support5 - .45, .1);
    const tap = prog(t, K.support5 + .5, .3); c.querySelector('.fill').style.transform = `scaleX(${outCubic(tap)})`; c.querySelector('.lab').style.color = tap > .5 ? '#111' : '#fff'; c.querySelector('.chk').style.opacity = tap >= 1 ? 1 : 0;
    cur.style.transform = `scale(${1 - .12 * Math.sin(Math.PI * prog(t, K.support5 + .42, .16))})`; }; };
C.finally_v1 = sc => { const w = $('div', 'anton', L.text, 'FINALLY'); w.style.cssText += ';position:absolute;left:0;right:0;top:1150px;text-align:center;font-size:200px';
  return t => { show(w, 1); const p = outCubic(prog(t, K.finallyw - .04, .4)); w.style.opacity = t < K.finallyw - .04 ? 0 : p; w.style.letterSpacing = lerp(.3, .005, p) + 'em'; w.style.filter = p < 1 ? `blur(${lerp(10, 0, p)}px)` : 'none'; }; };
C.follow = sc => {                                           // follow card with his avatar; the button is pressed on "follow"
  const c = $('div', 'abs', L.mg); c.style.cssText += ';left:70px;top:1410px;width:940px;height:170px;border-radius:85px;background:rgba(22,22,24,.92);box-shadow:inset 0 0 0 2px rgba(255,255,255,.14),0 24px 60px rgba(0,0,0,.55)';
  c.innerHTML = `<div class="av" style="left:20px;top:20px;width:150px;height:150px"><img src="assets/avatar_move_with_raghu.png"></div><div class="dmw" style="position:absolute;left:196px;top:46px;font-size:46px;font-weight:700">move with raghu</div><div class="dm" style="position:absolute;left:196px;top:104px;font-size:32px">10K followers</div>
    <div class="btn" style="position:absolute;right:26px;top:45px;width:250px;height:100px;border-radius:50px;background:#FFD60A;color:#111;font:800 44px/100px Mont;text-align:center">Follow</div>`;
  const cur = $('div', 'abs', L.text, '<svg width="90" height="106" viewBox="0 0 44 52"><path d="M4 2 L40 30 L24 32 L32 48 L25 51 L17 35 L6 46 Z" fill="#fff" stroke="#111" stroke-width="3" stroke-linejoin="round"/></svg>');
  return t => { show(c, 1); show(cur, 1); rise(c, t, K.follow - .55, .3, 50); const btn = c.querySelector('.btn'), done = t >= K.follow + .32;
    btn.textContent = done ? 'Following ✓' : 'Follow'; btn.style.background = done ? '#3a3a3e' : '#FFD60A'; btn.style.color = done ? '#fff' : '#111'; btn.style.width = done ? '300px' : '250px'; btn.style.fontSize = done ? '40px' : '44px';
    const cp = outCubic(prog(t, K.follow - .3, .32)); cur.style.left = lerp(1010, 958, cp) + 'px'; cur.style.top = lerp(1700, 1525, cp) + 'px'; cur.style.opacity = prog(t, K.follow - .3, .08);
    btn.style.transform = `scale(${1 - .08 * Math.sin(Math.PI * prog(t, K.follow + .2, .16))})`; }; };

// ---------------------------------------------------------------- frame
const SPEAKER = new Set(['hook', 'wait', 'toggle', 'thanks', 'why', 'support', 'finally', 'follow']);
const NOCAP = new Set(['wait', 'comments', 'stats', 'you', 'channels', 'back', 'poll']);       // the design already carries those words
window.init = (tl, opts = {}) => {
  TL = tl; K = tl.K; FPS = tl.fps; LAYOUT = opts.layout || 'B'; CAPMODE = opts.cap || 'tg';
  for (const id of ['bg', 'mg', 'text']) L[id] = document.getElementById('L' + id);
  for (const sc of tl.scenes) {
    const layers = ['bg', 'mg', 'text'], before = layers.map(k => L[k].children.length);
    const draw = C[sc.id] ? C[sc.id](sc) : null;
    const els = layers.flatMap((k, j) => [...L[k].children].slice(before[j])); els.forEach(e => { e.style.display = 'none'; });
    comps.push({ sc, draw, els });
  }
  const fr = $('div', 'L', L.text); FRAME = [fr];
  if (LAYOUT === 'B') [WY - 3, WY + WH].forEach(y => { const l = $('div', 'abs', fr); l.style.cssText += `;left:0;top:${y}px;width:1080px;height:3px;background:rgba(255,255,255,.22)`; });
  CAPS = $('div', 'cap', document.getElementById('Lcap')); CAPS.style.top = '1420px'; CAPS.style.height = '90px'; CAPS.style.display = 'none';
  LKEL = $('div', 'lk', document.getElementById('Lcap'));
};
window.renderAt = async t => {
  const i = Math.min(TL.n - 1, Math.round(t * FPS));
  document.getElementById('turb').setAttribute('seed', 1 + (i >> 1) % 97);
  const cur = comps.find(c => t >= c.sc.t0 && t < c.sc.t1) || comps[comps.length - 1];
  for (const c of comps) if (c !== cur) c.els.forEach(e => { e.style.display = 'none'; });
  const spk = SPEAKER.has(cur.sc.id); show(document.getElementById('Lmain'), spk); FRAME.forEach(e => show(e, spk));
  const dt = t - cur.sc.t0, pk = cur.sc.t0 === 0 || cur.sc.id === 'wait' ? 1 : prog(dt, 0, 0.13);      // scene-start zoom-blur punch
  for (const id of ['Lbg', 'Lmain', 'Lmg']) { const e = document.getElementById(id); e.style.transform = pk < 1 ? `scale(${lerp(1.06, 1, outCubic(pk))})` : ''; e.style.filter = pk < 1 ? `blur(${lerp(10, 0, outCubic(pk))}px)` : ''; }
  if (spk) await drawSpeaker(t, i, cur.sc);
  if (cur.draw) await cur.draw(t, i);
  if (CAPMODE === 'en' || CAPMODE === 'v1') drawCaps(t, NOCAP.has(cur.sc.id)); else CAPS.style.display = 'none';
  drawLockups(t, !['comments', 'stats', 'channels', 'poll', 'toggle'].includes(cur.sc.id));
  if (cur.sc.id === 'why' && WHYBAR) WHYBAR(t);
  await Promise.all([...document.images].filter(im => im.offsetParent !== null && !im.complete).map(im => im.decode().catch(() => {})));
};
