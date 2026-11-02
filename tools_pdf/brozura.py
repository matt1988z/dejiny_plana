#!/usr/bin/env python3
"""Brožura „Fara v Plané“ (A4, PDF) z dat projektu.

Použití (z kořene projektu): python3 -I tools_pdf/brozura.py
  -> pracovni/pdf/brozura.html, pak node tools_pdf/tisk.js -> Fara_v_Plane.pdf
Čte data/domy.py, zaznamy.json, prepisy.json, svazky.json, mapy.json, pribeh_cp1.md – nic v datech nemění.
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "pracovni", "pdf")
os.makedirs(OUT, exist_ok=True)
FONTS = os.path.join(ROOT, "web", "node_modules", "@fontsource-variable")


def load(n):
    return json.load(open(os.path.join(D, n), encoding="utf-8"))


ns = {}
exec(open(os.path.join(D, "domy.py"), encoding="utf-8").read(), ns)
OBEC, DUM, ISSUES = ns["OBEC"], ns["D"]["1"], ns["ISSUES"]
zaz = {z["klic"]: z for z in load("zaznamy.json")}
pre = load("prepisy.json")
svz = load("svazky.json")
mapy = load("mapy.json")
e = html.escape


def img(key):
    return "file://" + os.path.join(ROOT, "vyrezy", key + ".jpg")


# pořadí zápisů v příloze = chronologicky
def rok(z):
    m = re.search(r"\d{4}", z.get("datum", ""))
    return int(m.group()) if m else 9999


poradi = sorted(zaz.values(), key=rok)
cislo = {z["klic"]: i + 1 for i, z in enumerate(poradi)}


def md_inline(t):
    t = e(t)
    t = re.sub(r"\[([^\]]+)\]\(/zdroj/([a-z0-9_]+)/\)",
               lambda m: f'<span class="ref">{m.group(1)}&nbsp;<sup>P{cislo.get(m.group(2), "?")}</sup></span>', t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    t = t.replace(" · ", " &nbsp;·&nbsp; ")
    return t


def pribeh():
    txt = open(os.path.join(D, "pribeh_cp1.md"), encoding="utf-8").read()
    txt = re.sub(r"^---.*?---\s*", "", txt, flags=re.S)
    out = []
    for blok in re.split(r"\n\s*\n", txt.strip()):
        b = blok.strip()
        m = re.match(r"!\[(.*?)\]\(/img/([a-z0-9_]+)\.jpg\)", b)
        if b.startswith("## "):
            out.append(f"<h2>{e(b[3:])}</h2>")
        elif m:
            out.append(f'<figure><img src="{img(m.group(2))}"><figcaption>{e(m.group(1))}</figcaption></figure>')
        else:
            out.append(f"<p>{md_inline(b)}</p>")
    # kapitola „Dnes“ až na konec, „Co ještě nevíme“ vynechat (je v samostatné kapitole)
    s = "\n".join(out)
    s = re.sub(r"<h2>Co ještě nevíme</h2>\s*<p>.*?</p>", "", s, flags=re.S)
    return s


def casova_osa():
    rows = []
    ud = [(u["rok"], u["text"], u.get("r", [])) for u in DUM["udalosti"]]
    ud += [(u["rok"], u["text"], u.get("r", [])) for u in OBEC_UDALOSTI if u["rok"] not in ("1839",)]
    ud.sort(key=lambda x: int(re.search(r"\d{4}", x[0]).group()))
    for r_, t, refs in ud:
        p = " ".join(f"<sup>P{cislo[k]}</sup>" for k in refs if k in cislo)
        rows.append(f'<tr><td class="yr">{e(r_)}</td><td>{e(t)} {p}</td></tr>')
    return "\n".join(rows)


OBEC_UDALOSTI = ns["OBEC_UDALOSTI"]


def lide():
    rows = []
    for o in DUM["obyvatele"]:
        p = " ".join(f"<sup>P{cislo[k]}</sup>" for k in o.get("r", []) if k in cislo)
        f = "; ".join(o.get("f", []))
        rows.append(f"<tr><td><strong>{e(o['n'])}</strong></td><td>{e(o['y'])}</td><td>{e(o['role'])}"
                    f"{'<br><span class=small>' + e(f) + '</span>' if f else ''} {p}</td></tr>")
    return "\n".join(rows)


def priloha():
    out = []
    for z in poradi:
        k = z["klic"]
        p = pre.get(k, {})
        sv = svz.get(z.get("svazek", ""), {})
        cit = []
        if sv:
            cit.append(f"{sv.get('archiv', '')}, {sv.get('svazek', '')}".strip(", "))
        if z.get("snimek") and z.get("druh") != "L":
            cit.append(f"snímek {z['snimek']}")
        if z.get("druh") == "L":
            cit.append(f"s. {z['snimek']}")
        orig = e(p.get("orig", "")).replace("\n", "<br>")
        out.append(f'''<section class="rec">
  <div class="rec-h"><span class="pn">P{cislo[k]}</span><div><h3>{e(z["nazev"])}</h3>
  <div class="meta">{e(z.get("datum", ""))} · {e(" · ".join(c for c in cit if c))}</div></div></div>
  <img src="{img(k)}">
  <div class="tr"><div><h4>Přepis originálu</h4><p class="orig">{orig}</p></div>
  <div><h4>Český překlad</h4><p>{e(p.get("cs", ""))}</p></div></div>
  <div class="url">{e(z.get("odkaz", ""))}</div>
</section>''')
    return "\n".join(out)


def mapy_html():
    out = []
    for m in mapy:
        out.append(f'''<figure class="map"><img src="{img(m["img"])}">
<figcaption><strong>{e(m["nazev"])}</strong> ({e(m["rok"])}). {e(m.get("popis", ""))}<br><span class="small">Zdroj: {e(m["zdroj"])}</span></figcaption></figure>''')
    return "\n".join(out)


def otazky():
    return "\n".join(f"<li><strong>{e(q)}</strong> {e(re.sub(r'^(Otevřené|Hypotéza): ', '', a))}</li>" for q, a in ISSUES)


css = f"""
@font-face {{ font-family: Fraunces; src: url(file://{FONTS}/fraunces/files/fraunces-latin-ext-wght-normal.woff2) format('woff2'); font-weight: 100 900; unicode-range: U+0100-024F, U+1E00-1EFF; }}
@font-face {{ font-family: Fraunces; src: url(file://{FONTS}/fraunces/files/fraunces-latin-wght-normal.woff2) format('woff2'); font-weight: 100 900; }}
@font-face {{ font-family: Fraunces; font-style: italic; src: url(file://{FONTS}/fraunces/files/fraunces-latin-ext-wght-italic.woff2) format('woff2'); font-weight: 100 900; unicode-range: U+0100-024F, U+1E00-1EFF; }}
@font-face {{ font-family: Fraunces; font-style: italic; src: url(file://{FONTS}/fraunces/files/fraunces-latin-wght-italic.woff2) format('woff2'); font-weight: 100 900; }}
@font-face {{ font-family: 'Source Sans 3'; src: url(file://{FONTS}/source-sans-3/files/source-sans-3-latin-ext-wght-normal.woff2) format('woff2'); font-weight: 200 900; unicode-range: U+0100-024F, U+1E00-1EFF; }}
@font-face {{ font-family: 'Source Sans 3'; src: url(file://{FONTS}/source-sans-3/files/source-sans-3-latin-wght-normal.woff2) format('woff2'); font-weight: 200 900; }}
@font-face {{ font-family: 'Source Sans 3'; font-style: italic; src: url(file://{FONTS}/source-sans-3/files/source-sans-3-latin-ext-wght-italic.woff2) format('woff2'); font-weight: 200 900; unicode-range: U+0100-024F, U+1E00-1EFF; }}
@font-face {{ font-family: 'Source Sans 3'; font-style: italic; src: url(file://{FONTS}/source-sans-3/files/source-sans-3-latin-wght-italic.woff2) format('woff2'); font-weight: 200 900; }}
@page {{ size: A4; margin: 20mm 20mm 22mm 22mm; }}
@page :first {{ margin: 0; }}
:root {{ --ink:#2e2419; --brown:#5a4330; --muted:#7a6a58; --line:#e0d4c2; --accent:#b4672e; --paper:#fbf8f2; }}
* {{ box-sizing: border-box; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ font-family: 'Source Sans 3', sans-serif; font-size: 10.6pt; line-height: 1.55; color: var(--ink); margin: 0; }}
h1, h2, h3 {{ font-family: Fraunces, serif; font-weight: 420; color: var(--brown); line-height: 1.15; }}
h2 {{ font-size: 19pt; margin: 18pt 0 6pt; break-after: avoid; }}
h3 {{ font-size: 12.5pt; margin: 0; }}
h4 {{ font-family: 'Source Sans 3'; font-size: 8pt; letter-spacing: .12em; text-transform: uppercase; color: var(--accent); margin: 0 0 3pt; }}
p {{ margin: 0 0 7pt; text-align: justify; hyphens: auto; }}
sup {{ font-size: 6.5pt; color: var(--accent); font-weight: 600; }}
.ref {{ color: var(--brown); }}
.small {{ font-size: 8.5pt; color: var(--muted); }}
figure {{ margin: 10pt 0 12pt; break-inside: avoid; }}
figure img {{ width: 100%; max-height: 92mm; object-fit: contain; border: 0.6pt solid var(--line); background: #fff; }}
figcaption {{ font-size: 8.8pt; color: var(--muted); margin-top: 4pt; font-style: italic; }}
.page {{ break-before: page; }}
.kicker {{ font-size: 8.5pt; letter-spacing: .16em; text-transform: uppercase; color: var(--accent); font-weight: 600; }}
/* obálka */
.cover {{ height: 297mm; width: 210mm; position: relative; overflow: hidden; background: #2e2419; }}
.cover img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: .92; }}
.cover .shade {{ position: absolute; inset: 0; background: linear-gradient(180deg, rgba(30,22,14,.0) 30%, rgba(30,22,14,.82) 72%, rgba(30,22,14,.95)); }}
.cover .t {{ position: absolute; left: 22mm; right: 22mm; bottom: 26mm; color: #fbf3e6; }}
.cover h1 {{ color: #fff; font-size: 54pt; margin: 4pt 0 8pt; font-weight: 380; }}
.cover .sub {{ font-size: 14pt; font-family: Fraunces; font-style: italic; color: #f1dfc6; }}
.cover .kicker {{ color: #f0b37a; }}
.cover .foot {{ margin-top: 16pt; font-size: 9pt; color: #d9c7ad; border-top: .6pt solid rgba(255,255,255,.35); padding-top: 8pt; }}
/* úvod */
.lead {{ font-family: Fraunces; font-size: 15pt; line-height: 1.4; color: var(--brown); font-weight: 350; margin: 6pt 0 14pt; text-align: left; }}
.facts {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; border: .6pt solid var(--line); border-radius: 4pt; margin: 12pt 0 16pt; background: var(--paper); }}
.facts div {{ padding: 9pt 10pt; border-right: .6pt solid var(--line); }}
.facts div:last-child {{ border-right: 0; }}
.facts b {{ display: block; font-family: Fraunces; font-size: 20pt; font-weight: 400; color: var(--brown); }}
.facts span {{ font-size: 8.5pt; color: var(--muted); }}
table {{ width: 100%; border-collapse: collapse; font-size: 9.6pt; }}
td {{ padding: 5pt 6pt; border-bottom: .5pt solid var(--line); vertical-align: top; }}
td.yr {{ white-space: nowrap; font-family: Fraunces; color: var(--accent); width: 26mm; }}
tr {{ break-inside: avoid; }}
.box {{ background: var(--paper); border-left: 2.5pt solid var(--accent); padding: 9pt 12pt; margin: 12pt 0; font-size: 9.6pt; break-inside: avoid; }}
.box p {{ text-align: left; margin: 0 0 4pt; }}
.story p:first-of-type::first-letter {{ font-family: Fraunces; float: left; font-size: 38pt; line-height: .9; padding: 3pt 5pt 0 0; color: var(--accent); }}
/* příloha */
.rec {{ break-inside: avoid; margin: 0 0 10pt; padding-bottom: 8pt; border-bottom: .6pt solid var(--line); }}
.rec-h {{ display: flex; gap: 9pt; align-items: flex-start; margin-bottom: 6pt; }}
.pn {{ font-family: Fraunces; font-size: 13pt; color: #fff; background: var(--accent); border-radius: 3pt; padding: 1pt 6pt; }}
.meta {{ font-size: 8.5pt; color: var(--muted); }}
.rec img {{ width: 100%; max-height: 62mm; object-fit: contain; background: #f4efe6; border: .6pt solid var(--line); }}
.tr {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12pt; margin-top: 7pt; }}
.tr p {{ font-size: 8.9pt; text-align: left; line-height: 1.45; }}
.orig {{ font-family: Fraunces; font-style: italic; color: #4a3b2c; }}
.url {{ font-size: 7.5pt; color: var(--muted); word-break: break-all; }}
.map img {{ max-height: 105mm; }}
ul.q li {{ margin-bottom: 6pt; }}
.toc li {{ margin: 3pt 0; }}
"""

pocet_zapisu = len(zaz)
html_doc = f"""<!doctype html><html lang="cs"><head><meta charset="utf-8"><title>Fara v Plané</title><style>{css}</style></head><body>

<section class="cover">
  <img src="{img('mapa_plana_1839_cisarsky_otisk')}">
  <div class="shade"></div>
  <div class="t">
    <div class="kicker">Planá u Hromnic · čp. 1</div>
    <h1>Fara v Plané</h1>
    <div class="sub">Dějiny domu u kostela z matrik, map a knih, 1409 – dnes</div>
    <div class="foot">Sestaveno z digitalizovaných pramenů Státního oblastního archivu v Plzni (Porta fontium),
    Archivu Zeměměřického úřadu (ČÚZK) a Národní knihovny ČR (Kramerius) · listopad 2026<br>
    Na obálce: náves v Plané na mapě stabilního katastru z roku 1839</div>
  </div>
</section>

<section class="page">
  <div class="kicker">Úvod</div>
  <h2 style="font-size:28pt;margin-top:4pt">Dům, kde žil skladatel</h2>
  <p class="lead">Bývalá fara čp. 1 stojí v Plané hned vedle gotického kostela. Přes 300 let tu žili faráři, kteří psali matriky pro celé okolí:
  mniši z kláštera v Plasích, barokní skladatel Jeroným Brixi, učenec z Prahy i farář zavražděný loupežníkem.</p>
  <div class="facts">
    <div><b>1409</b><span>nejstarší známý farář</span></div>
    <div><b>22 let</b><span>tu byl farářem skladatel Jeroným Brixi</span></div>
    <div><b>{len(DUM['obyvatele'])}</b><span>známých farářů a obyvatel fary</span></div>
    <div><b>{pocet_zapisu}</b><span>zápisů z pramenů v příloze</span></div>
  </div>
  <p>{e(OBEC['popis'])}</p>
  <p>Dnešní adresa: Planá 1, 330 11 Hromnice; pozemek st. 1/1 v katastrálním území Planá u Nynic, okres Plzeň-sever.
  Stejný pozemek číslo 1 má fara už na mapě z roku 1839 a jako dům číslo 1 ji vedou i matriky od roku 1784.</p>
  <div class="box"><p><strong>Jak číst tuto brožuru.</strong> Text vypráví příběh domu. Drobná čísla
  <sup>P1</sup>, <sup>P2</sup>… odkazují na <em>Přílohu</em>: tam je u každého údaje výřez původního zápisu, jeho přepis a český překlad
  a odkaz na snímek v digitálním archivu. Nejistá čtení jsou označena otazníkem.</p></div>
  <h4 style="margin-top:14pt">Obsah</h4>
  <ol class="toc"><li>Příběh fary</li><li>Časová osa</li><li>Lidé z fary</li><li>Staré mapy</li><li>Co ještě nevíme</li><li>Příloha: zápisy z pramenů</li><li>Prameny a literatura</li></ol>
</section>

<section class="page story">
  <div class="kicker">1 · Příběh fary</div>
  {pribeh()}
</section>

<section class="page">
  <div class="kicker">2 · Časová osa</div>
  <h2>Fara a farnost v čase</h2>
  <table>{casova_osa()}</table>
  <div class="kicker" style="margin-top:22pt">3 · Lidé z fary</div>
  <h2>Kdo na faře žil</h2>
  <table>{lide()}</table>
  <p class="small" style="margin-top:6pt">Faru vlastnilo farní obročí: do roku 1785 ji spravovali cisterciáci z Plas, potom farnost s faráři jmenovanými císařem.
  Posledním farářem byl Ludvík Vaníček (do 1950). Kdy fara přešla do soukromých rukou, zatím nevíme.</p>
</section>

<section class="page">
  <div class="kicker">4 · Staré mapy</div>
  <h2>Planá na starých mapách</h2>
  {mapy_html()}
</section>

<section class="page">
  <div class="kicker">5 · Co ještě nevíme</div>
  <h2>Otevřené otázky</h2>
  <ul class="q">{otazky()}</ul>
  <div class="box"><p><strong>Kde hledat dál.</strong> Pozdější matriky fary (1822–1949) na Porta fontium; sčítání lidu 1869–1921;
  pamětní kniha a spisy Farního úřadu Planá a patronátní spisy plaského velkostatku ve Státním oblastním archivu v Plzni;
  pozemková kniha k parcele st. 1/1 na katastrálním pracovišti Plzeň-sever.</p></div>
</section>

<section class="page">
  <div class="kicker">6 · Příloha</div>
  <h2>Zápisy z pramenů</h2>
  <p class="small">Řazeno podle data. Přepis zachovává původní pravopis; […] = nečitelné, (?) = nejisté čtení.</p>
  {priloha()}
</section>

<section class="page">
  <div class="kicker">7 · Prameny a literatura</div>
  <h2>Prameny a literatura</h2>
  <p><strong>Státní oblastní archiv v Plzni</strong>, Sbírka matrik západních Čech, fara Planá (Plzeň-sever):
  Planá (PS) 01 (N 1644–1708, O 1683–1708, Z 1685–1708); Planá (PS) 16 (N, O, Z pro ves Planá 1784–1821);
  Planá (PS) 21 (Z 1822–1868); Planá (PS) 32 (Z 1869–1911); Planá (PS) 36 (Z 1911–1949). Digitálně na portálu Porta fontium, www.portafontium.eu.</p>
  <p><strong>Zeměměřický úřad – Archiv ČÚZK</strong>, stabilní katastr: císařský otisk Planá 1839 (B2/a/6C 5802),
  originální mapa (B2/a/4C 5487, reambulace 1870); pozemkový katastr. ags.cuzk.gov.cz/archiv.</p>
  <p><strong>2. vojenské mapování</strong> (1836–1852), © ÚAZK / CENIA, gis.cenia.cz.</p>
  <p><strong>Antonín Podlaha</strong>, Posvátná místa království Českého, díl II (Vikariát plzeňský), Praha 1911, s. 310–313 (text i fotografie kostela).</p>
  <p><strong>Adresář církve katolické v republice Československé</strong>, 1928, s. 354.</p>
  <p><strong>Blahověst</strong>, katolický týdeník, 15. 4. 1852, s. 192 (zpráva o vraždě faráře).</p>
  <p><strong>Obec Hromnice</strong>, Historie (www.hromnice.cz); <strong>Římskokatolická farnost Dýšina</strong>, Kostel Nanebevzetí Panny Marie v Plané nade Mží (2011).</p>
  <p><strong>ČÚZK</strong>, Ortofoto ČR (letecký snímek).</p>
  <p><strong>Český slovník bohovědný</strong>, díl II, Praha 1916, s. 501, heslo Brixi. Národní knihovna ČR, Kramerius.</p>
  <p><strong>RÚIAN</strong> (Registr územní identifikace, adres a nemovitostí), ČÚZK – dnešní adresa a parcela.</p>
  <p class="small" style="margin-top:14pt">Brožura vznikla z otevřeného projektu dějin domu. Všechny údaje mají v projektu odkaz na konkrétní snímek pramene.
  Čtení rukopisů 18. a 19. století může obsahovat chyby – kde je to důležité, ověřte výřez v příloze.</p>
</section>
</body></html>"""

open(os.path.join(OUT, "brozura.html"), "w", encoding="utf-8").write(html_doc)
print(os.path.join(OUT, "brozura.html"))
