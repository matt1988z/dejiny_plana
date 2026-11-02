# Stav projektu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## O čem to je
- Obec a hlavní dům: Planá čp. 1 (bývalá fara), 330 11 Hromnice; parcela st. 1/1, k. ú. Planá u Nynic (708402)
- Kdo s Claudem pracuje: dnešní majitel fary; chce profesionální, obsahově zajímavý výstup s obrázky a příběhy; komunikace česky
- Farnost: Planá (PS) – sama sídlo fary; matriky SOA Plzeň, Porta fontium, knihy plana-ps-01 až 37 (1644–1949). Panství: Plasy (klášter cisterciáků, zrušen 1785). Stabilní katastr 1839 (cio B2/a/6C 5802, om B2/a/4C 5487).

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/domy.py` | Obec (`OBEC`, `OBEC_UDALOSTI`), domy podle čp. (`D`: události, držitelé, obyvatelé), otevřené otázky. |
| `data/zaznamy.json` | Každý použitý zápis z pramene (klíč = název obrázku). |
| `data/svazky.json` | Svazky a fondy (matriky, gruntovní knihy, sčítání, katastry) – archiv, signatura, odkaz. |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/mapy.json` | Historické mapy a letecké snímky (rok, zdroj) – stránka „Staré mapy“ s porovnáním. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/pametnici.md` | Co řekli majitelé a pamětníci, domovní dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu / na katastru. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Okolní místa na mapě, fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů a map pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Materiály od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `domy.py`, `zaznamy.json` a `research_log.md` (číslo domu, jméno, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Literatura je `lit`, ne `doc`.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím. Číslo domu ověřuji proti přečíslování.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Hotovo (2026-11): úmrtí čp. 1 1784–1821 (plana-ps-16) kompletně; 1822–1868 (plana-ps-21, sn. 415–437) jen zběžně – dočíst čp. 1 (1837, 1840 a sn. 425–437).
- Další: křty/sňatky čp. 1 (kuchařky, čeleď), úmrtí 1869–1911 (plana-ps-32) a 1911–1949 (plana-ps-36) – faráři; sčítání lidu 1869–1921 (fara, kdo tu bydlel).
- Wikipedia / Commons vrátily 429 – zkusit znovu (článek Planá (Hromnice), fotky kostela a fary).
- Příběh pribeh_cp1.md napsán jako koncept – čeká na schválení majitelem.
- web.json: přihlašovací otázku a odpověď musí zvolit majitel před zveřejněním.
