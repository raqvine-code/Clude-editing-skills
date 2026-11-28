import os
P = os.path.dirname(os.path.abspath(__file__))
PANELS = [
 ("1.24", "0.0-1.4", "“Ee video ki andaru support…”", "light ‘Ee video ki’ / script ‘andaru’ + bold yellow ‘support’"),
 ("2.22", "1.4-2.4", "“…chestharu anukuntunnanu”", "italic ‘chestharu’ / bold ‘anukuntunnanu’"),
 ("3.67", "2.4-3.7", "“Guys, wait wait wait wait”", "script ‘Guys,’ + bold ‘wait’ / three bold ‘wait’ (last yellow); 4 punch-ins"),
 ("5.90", "3.7-7.1", "“nuvvu unnava poyava… kada?”", "UNNAVA ⇄ POYAVA switch + one light line"),
 ("11.62", "10.5-11.8", "“Nannu ippati varaku…”", "script ‘Nannu’ / light ‘ippati varaku’"),
 ("12.76", "11.8-12.9", "“…meeru support chesinanduku”", "light ‘meeru’ + bold ‘support’ / italic ‘chesinanduku’"),
 ("13.72", "12.9-13.9", "“thank you so much”", "bold ‘Thank’ / script ‘you’ + italic ‘so much!’"),
 ("20.90", "13.9-21.1", "“10K, 27K, 10K”", "your 3 cards, numbers count up on each word"),
 ("21.92", "21.1-22.0", "“Idantha kooda…”", "one light line on black"),
 ("22.74", "22.0-22.9", "“…mee valle vachindi”", "script ‘mee’ + bold ‘valle’ / italic ‘vachindi.’"),
 ("25.28", "24.1-25.5", "“Ivanni enduku cheptunnanu…”", "light ‘Ivanni’ + bold ‘enduku’ / italic ‘cheptunnanu’"),
 ("26.00", "25.5-26.1", "“…anukuntaru kada?”", "light ‘anukuntaru’ / script ‘kada?’"),
 ("27.45", "26.1-27.6", "“Yes, akkadike vasthunnanu”", "script ‘Yes,’ + bold ‘akkadike’ / light line; NEW: a straight yellow line fills to the cut (the ‘coming to that…’ chip is gone)"),
 ("31.50", "27.6-33.7", "“first facts… second challenge & entertainment”", "your two channel cards; the yellow arrow travels"),
 ("34.82", "33.7-35.0", "“ippudu malli facts…”", "light ‘Ippudu’ + script ‘malli’ / bold yellow ‘facts’"),
 ("35.86", "35.0-36.0", "“…channel ki vasthunnanu”", "light ‘channel ki’ / italic ‘vasthunnanu.’"),
 ("37.98", "36.0-38.2", "“So nannu ippati varaku support chesina…”", "light line / bold ‘support’ + italic ‘chesina’"),
 ("38.82", "38.2-39.0", "“…vallu evaraithe unnaro”", "script ‘vallu’ / light ‘evaraithe unnaro,’"),
 ("39.82", "39.0-40.0", "“ippudu kooda nannu…”", "one light line"),
 ("41.48", "40.0-41.7", "“…alage support chestharani”", "script ‘alage’ + bold ‘support’ / italic ‘chestharani’; hearts rise"),
 ("44.90", "41.7-45.1", "“meeru nannu support chestara leda?”", "community question card, the cursor taps YES"),
 ("46.22", "45.1-46.4", "“finally ga nenu cheppalanukunnadi…”", "script ‘finally ga’ / light ‘nenu’ + bold ‘cheppalanukunnadi’"),
 ("48.33", "46.4-48.5", "“enti ante, first follow chesukondi”", "italic ‘enti ante,’ + light ‘first’ / bold yellow ‘follow’ + script ‘chesukondi.’; follow card pressed"),
 ("49.70", "48.5-49.9", "“next video lo matladatham”", "script ‘Next’ + light ‘video lo’ / bold ‘matladatham.’"),
]
CSS = """<style>@font-face{font-family:A;src:url(../hc/fonts/Anton.ttf)}@font-face{font-family:D;src:url(../hc/fonts/DMSans.ttf);font-weight:100 1000}@font-face{font-family:M;src:url(../hc/fonts/Manrope.ttf);font-weight:200 800}
body{margin:0;background:#0b0b0c;color:#fff;font-family:D;width:2380px}.top{padding:34px 50px 10px;display:flex;align-items:baseline;gap:30px}.top h1{font:400 76px/1 A;margin:0;letter-spacing:.01em}.top h1 b{color:#FFD60A;font-weight:400}
.top span{font:500 26px/1.3 D;color:#bbb;letter-spacing:.06em}.g{display:grid;grid-template-columns:repeat(6,360px);gap:18px;padding:18px 50px 44px}
.p{background:#161618;border-radius:18px;overflow:hidden;box-shadow:0 0 0 1px #2a2a2e}.p img{width:360px;height:640px;display:block}.t{padding:12px 14px 16px}
.h{display:flex;justify-content:space-between;align-items:center}.h b{font:400 40px/1 A;color:#FFD60A}.h span{font:600 20px/1 D;color:#ccc}.s{font:600 21px/1.25 M;margin:8px 0 6px;color:#fff}
.v{font:400 19px/1.3 D;color:#cfcfd4}</style>"""
def panel(n, st, tr, said, vis):
    return f"""<div class="p"><img src="../stills_v4/s_{st}_B_v2.jpg"><div class="t"><div class="h"><b>{n}</b><span>{tr} s</span></div><div class="s">{said}</div><div class="v">{vis}</div></div></div>"""
for k in range(4):
    g = PANELS[k * 6:(k + 1) * 6]
    open(f"{P}/boards/v4_b{k + 1}.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8>{CSS}</head><body><div class=top><h1>BACK TO <b>FACTS</b></h1><span>TYPOGRAPHY v4 · {k + 1}/4 · two lines at most per phrase · always below your chin · frames {k * 6 + 1}-{k * 6 + len(g)}</span></div><div class=g>{''.join(panel(k * 6 + j + 1, *x) for j, x in enumerate(g))}</div></body></html>")
PAIRS = [("1.95", "v3", "1.24", "“Ee video ki andaru support chestharu…”"), ("38.80", "v3", "37.98", "“So nannu ippati varaku support chesina vallu…”"), ("46.60", "v3", "46.22", "“finally ga nenu cheppalanukunnadi enti ante”")]
cells = "".join(f"""<div style="display:flex;gap:18px;align-items:flex-start"><div class=p><img src="../stills_v3/s_{a}_B_v2.jpg"><div class=t><div class=h><b style="color:#888">BEFORE</b><span>3 lines</span></div><div class=s>{said}</div></div></div>
<div class=p><img src="../stills_v4/s_{c}_B_v2.jpg"><div class=t><div class=h><b>AFTER</b><span>2 lines</span></div><div class=s>split into two short phrases; no word lost</div></div></div></div>""" for a, _, c, said in PAIRS)
open(f"{P}/boards/v4_before_after.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8>{CSS}</head><body><div class=top><h1>3 LINES → <b>2 LINES</b></h1><span>your note: three lines looked like too many fonts · now every phrase is two lines at most</span></div><div style='display:flex;gap:28px;padding:18px 50px 44px'>{cells}</div></body></html>")
