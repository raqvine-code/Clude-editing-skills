import json, os, subprocess
P = os.path.dirname(os.path.abspath(__file__))
PANELS = [  # n, still, time, said (meaning), visual, sound
 (1, "0.60", "0.00-0.72", "“Guys, GTA 6…”", "Rockstar’s official animated logo, retimed so the wordmark lands on “GTA 6”", "deep riser → impact on “GTA 6”"),
 (2, "2.20", "0.72-3.00", "“…has released”", "Official cover art; OUT NOW + NOV 19 · 2026 stamp pops on “release”", "whoosh, stamp thud"),
 (3, "3.50", "3.00-3.86", "“how famous it became”", "4 official character clips, one cut per syllable; FAMOUS (game-title font)", "4 shutter hits"),
 (4, "5.90", "3.86-7.42", "“everyone knows… most people don’t know”", "Speaker full screen, slow push 1.00→1.06; wide-spaced line flashes and settles", "soft swell into the next scene"),
 (5, "9.60", "7.42-10.28", "“…why it took 13 years”", "HERO: neon “13” drawn top-down, sunset fill + bloom, YEARS wiped on, handwritten “why?”", "riser peak → sub impact on “13”, whoosh, pen"),
 (6, "10.90", "10.28-11.68", "“Why?”", "Punch-in 1.20; WHY? pops", "pop"),
 (7, "15.70", "11.68-15.86", "“Not story, not maps, definitely not graphics”", "3 cards (official screenshot, official Leonida map, Vice City skyline), each struck on “kaadu”", "3 card whooshes, 3 marker strikes, stamp"),
 (8, "17.20", "15.86-18.04", "“Then what for?”", "Vignette closes in; THE REAL REASON flashes", "low reverse swell"),
 (9, "19.60", "18.04-19.92", "“Money. Timing.”", "Split: MONEY on the official heist shot; TIMING with a sweeping dial over Vice City at night", "cash recording, clock ticks"),
 (10, "24.90", "19.92-25.42", "“Normally a game sells well for a few years”", "Neon sales line rises (labelled ILLUSTRATION: no fake numbers)", "whoosh, rising tick"),
 (11, "27.90", "25.42-28.44", "“then its hype slowly drops”", "Speaker + HYPE meter draining on “decrease”", "power-down slide"),
 (12, "31.00", "28.44-31.43", "“developers move to the next game”", "Line falls; lime NEXT GAME curve starts; “devs move on →”", "marker squeak, pop"),
 (13, "31.80", "31.43-32.03", "“But…”", "Hard punch-in 1.24; BUT…", "brake/scratch hit"),
 (14, "33.70", "32.03-33.93", "“…GTA 5”", "Official GTA V cover slams in; SEPT 17 · 2013; $1 BILLION IN 3 DAYS (Guinness)", "impact, shutter, cash"),
 (15, "35.80", "33.93-35.93", "“that didn’t happen”", "GTA V line stays high 2013→2026 next to the dashed normal curve; counter to 230,000,000+; PC Gamer headline", "counter ticks, paper slide"),
 (16, "39.00", "35.93-39.31", "“only when a new game earns more than the old one”", "OLD GAME vs NEW GAME profit bars; the new bar overtakes on “brings”", "rising tone, chime"),
 (17, "42.00", "39.31-42.37", "“…that’s when they release it”", "TIMING proof: two delay headlines; FALL 2025 / MAY 26 struck, NOV 19 · 2026 out now", "paper slides, 2 strikes, check"),
 (18, "46.10", "42.37-46.23", "“It didn’t take 13 years to develop GTA 6”", "13 YEARS of development appears on “develop”, struck twice on “pattaledu”", "double strike, thud"),
 (19, "49.60", "46.23-49.79", "“until GTA 6 earns more than GTA 5”", "Official V and VI covers, VS; MORE PROFIT? bars", "whooshes, pops"),
 (20, "52.60", "49.79-53.23", "“they waited 13 years”", "PAYOFF: year counter 2013→2026, neon 13 returns, YEARS + “of waiting”, 4 real milestones", "tick roll, impact on 13, pen"),
 (21, "56.45", "53.23-57.70", "“More important: subscribe”", "Speaker; our own SUBSCRIBE button (not YouTube’s), cursor click → SUBSCRIBED", "pop, mouse click, bell"),
]
def panel(n, st, tr, said, vis, snd):
    return f"""<div class="p"><img src="../stills/s_{st}.jpg"><div class="t"><div class="h"><b>{n}</b><span>{tr} s</span></div>
    <div class="s">{said}</div><div class="v">{vis}</div><div class="a">♪ {snd}</div></div></div>"""
CSS = """<style>@font-face{font-family:T;src:url(../hc/fonts/InterTight.ttf);font-weight:100 900}@font-face{font-family:P;src:url(../hc/fonts/PricedownBl.otf)}
body{margin:0;background:#0b0610;color:#fff;font-family:T;width:2380px}.top{padding:34px 50px 10px;display:flex;align-items:baseline;gap:30px}.top h1{font:400 76px/1 P;margin:0;-webkit-text-stroke:6px #31072C;paint-order:stroke fill}
.top span{font:600 26px/1.3 T;color:#E9DDF0;letter-spacing:.08em}.g{display:grid;grid-template-columns:repeat(6,360px);gap:18px;padding:18px 50px 44px}
.p{background:#160c1c;border-radius:18px;overflow:hidden;box-shadow:0 0 0 1px #2b1a33}.p img{width:360px;height:640px;display:block}.t{padding:12px 14px 16px}
.h{display:flex;justify-content:space-between;align-items:center}.h b{font:800 38px/1 T;color:#FDA53A}.h span{font:600 20px/1 T;color:#E9DDF0}.s{font:600 21px/1.25 T;margin:8px 0 6px;color:#fff}
.v{font:400 19px/1.3 T;color:#d9cfe0}.a{font:500 18px/1.3 T;color:#9EFE3C;margin-top:8px}</style>"""
groups = [PANELS[0:6], PANELS[6:12], PANELS[12:18], PANELS[18:21]]
for k, g in enumerate(groups):
    html = f"<!doctype html><html><head><meta charset=utf-8>{CSS}</head><body><div class=top><h1>GTA 6 · 13 YEARS</h1><span>STORYBOARD {k + 1}/5 · scenes {g[0][0]}-{g[-1][0]} · real frames from the compositor on your footage</span></div><div class=g>{''.join(panel(*x) for x in g)}</div></body></html>"
    open(f"{P}/boards/b{k + 1}.html", "w").write(html)
opt = f"""<!doctype html><html><head><meta charset=utf-8>{CSS}<style>.o{{width:360px}}.o img{{width:360px;height:640px;display:block;border-radius:14px}}.o p{{font:600 22px/1.3 T;margin:10px 0 0}}.o small{{font:400 18px/1.3 T;color:#d9cfe0}}</style></head><body>
<div class=top><h1>2 CHOICES FOR YOU</h1><span>STORYBOARD 5/5 · pick one in each row</span></div>
<div class=g style="grid-template-columns:repeat(5,360px);gap:40px">
<div class=o><img src="../stills/s_5.90.jpg"><p>A · Full screen (recommended)</p><small>Picture scaled 1.40× to fill 9:16, face kept centred. Most immersive.</small></div>
<div class=o><img src="../stills/s_5.90_B.jpg"><p>B · Framed window</p><small>Your 4:5 picture at full sharpness between two neon lines; title band on top.</small></div>
<div style="width:40px"></div>
<div class=o><img src="../stills/s_4.30_te.jpg"><p>Captions + Telugu line</p><small>Keyword titles + a Telugu subtitle line (you check the spelling).</small></div>
<div class=o><img src="../stills/s_4.30_tg.jpg"><p>Captions + Tenglish line</p><small>Keyword titles + Telugu in English letters. Third option: keyword titles only (as on boards 1-4).</small></div>
</div></body></html>"""
open(f"{P}/boards/b5.html", "w").write(opt)
