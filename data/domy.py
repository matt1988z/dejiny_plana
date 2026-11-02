# Dějiny obce a jejích domů. Každý údaj má stav doložení `st`:
#   doc  = přečteno přímo v prameni (snímek matriky, gruntovní knihy, katastru, sčítání…)
#   lit  = z literatury (vlastivěda, kronika v knižním vydání, článek) – uvést kde v `note`/`zdroj`
#   prob = pravděpodobné (shoda údajů, ne přímý doklad) – v `note` proč
#   fam  = od majitele / pamětníka / rodiny (ústní podání, rodinné dokumenty)
#   unk  = neznámé (jen místo v přehledu)
# `r` = klíče zápisů z data/zaznamy.json, které údaj dokládají.

# Obec – vstupní stránka webu „Obec“
OBEC = dict(
    nazev="Planá",
    jine_nazvy="Plana, Plania (latinsky Planensis)",
    obec="Hromnice, okres Plzeň-sever; katastrální území Planá u Nynic",
    farnost="Planá (sídlo fary, v 19. století i děkanství); filiální kostely Kostelec a Čívice",
    panstvi="Plasy (cisterciácký klášter, po jeho zrušení 1785 státní náboženský fond); okres Plasy",
    popis="Malá ves nad řekou Mží severně od Plzně. Byla ale sídlem fary pro celé okolí: do plánského kostela "
          "chodili lidé z Hromnic, Nynic, Žichlic, Kaceřova, Jarova a dalších vsí. Faru dlouho spravovali cisterciáci "
          "z nedalekých Plas, po zrušení kláštera kněží jmenovaní císařem.",
    lat=49.8562, lon=13.5172,
)

# Časová osa obce
OBEC_UDALOSTI = [
    dict(rok="asi 1370", text="Na jižní straně návsi vzniká gotický kostel Nanebevzetí Panny Marie. Farář Petr je zmiňován roku 1409, "
         "zvon ve věži nese letopočet 1491.", st="lit", zdroj="A. Podlaha, Posvátná místa II (1911), s. 310–313; web obce Hromnice",
         r=["plana_lit_podlaha_1911"]),
    dict(rok="asi 1560", text="Pánem Plané je luterán Florian Gryspek z Kaceřova. Farář Adler, kněz ženatý, zpívá při mši evangelium německy.",
         st="lit", zdroj="A. Podlaha, Posvátná místa II (1911), s. 311", r=["plana_lit_podlaha_1911"]),
    dict(rok="1623", text="Gryspekům je panství zabaveno a vráceno plaskému klášteru. Od té doby jsou faráři v Plané cisterciáci.",
         st="lit", zdroj="A. Podlaha, Posvátná místa II (1911), s. 312", r=["plana_lit_podlaha_1911"]),
    dict(rok="1644", text="Plaský cisterciák P. Matyáš Valecius, původem řeholník z Velehradu, zakládá matriku plánské fary.",
         st="doc", r=["plana_matrika_titul_1644"]),
    dict(rok="1752–1753", text="Kostel je rozšířen a dostane věž. Do starého se podle faráře vešla sotva polovina farníků. "
         "Stavba trvala 24 týdnů.", st="doc", r=["plana_poznamka_kostel_1753"]),
    dict(rok="1753", text="Od plánské fary se oddělují Olešná a Liblín. Dohodl se na tom plaský opat Silvestr s pánem na Liblíně.",
         st="doc", r=["plana_poznamka_kostel_1753"]),
    dict(rok="1785", text="Císař Josef II. ruší plaský klášter. Faráře do Plané od té doby jmenuje císař.",
         st="lit", zdroj="dějiny kláštera Plasy; jmenování faráře císařem dokládá zápis z 1815",
         r=["plana_nastroje_1815"]),
    dict(rok="1815", text="Mlynáři z okolí platí stavbu kůru v kostele. Farář Nahlowsky daruje pražské housle, violy a violoncello, "
         "farníci se skládají na trubky, lesní rohy a tympány.", st="doc", r=["plana_kur_1815", "plana_nastroje_1815"]),
    dict(rok="1839", text="Zeměměřiči kreslí mapu stabilního katastru. Ves má asi dvacet domů kolem návsi s kostelem, většinou dřevěných.",
         st="doc", r=["plana_katastr_cp1_1839"]),
    dict(rok="1826", text="Plaské panství kupuje kníže Klement Metternich, rakouský kancléř. Stává se patronem kostela a fary.",
         st="lit", zdroj="A. Podlaha, Posvátná místa II (1911), s. 312", r=["plana_lit_podlaha_1911"]),
    dict(rok="1928", text="Farnost má 1504 katolíků v patnácti vsích. Kaplanské místo už není obsazené.", st="lit",
         zdroj="Adresář církve katolické (1928), s. 354", r=["plana_lit_adresar_1928"]),
    dict(rok="1949", text="Požár poškodí vybavení kostela. Opravy proběhly v letech 1953–1955.", st="lit",
         zdroj="ŘKF Dýšina, článek o kostele v Plané (2011)", r=[]),
    dict(rok="1950–1951", text="V presbytáři kostela jsou objeveny gotické nástěnné malby z konce 14. století. Restauroval je F. Fišer.",
         st="lit", zdroj="ŘKF Dýšina, článek o kostele v Plané (2011)", r=[]),
    dict(rok="1986", text="Planá se stává součástí obce Hromnice.", st="lit", zdroj="web obce Hromnice, Historie", r=[]),
    dict(rok="2026", text="Kostel spravuje římskokatolická farnost Dýšina. Je ve špatném stavu, sbírka na opravu začala v roce 2005.",
         st="lit", zdroj="ŘKF Dýšina (2011); webové vyhledávání", r=[]),
]

D = {
    "1": dict(
        nazev="Fara",
        druh="fara",
        st="doc",
        popis="Bývalá fara stojí hned vedle kostela Nanebevzetí Panny Marie. Přes 300 let v ní žili faráři a děkani, kaplani, "
              "kuchařky a čeleď, mezi nimi barokní skladatel Jeroným Brixi. Už v roce 1839 byla zděná, "
              "když většina domů ve vsi byla ještě dřevěná.",
        lat=49.85653, lon=13.51631,
        cisla=[("1839", "pozemek č. 1 u kostela"), ("asi 1900–1950", "pozemek č. 1"),
               ("dnes", "čp. 1, parcela st. 1/1, k. ú. Planá u Nynic")],
        udalosti=[
            dict(rok="1781", text="Farářem se stává cisterciák a hudebník P. Jeroným Brixi, dosud ředitel kůru v Plasích.",
                 st="lit", zdroj="Český slovník bohovědný II (1916), s. 501",
                 r=["plana_lit_brixi_slovnik_1916", "plana_umrti_cp1_brixi_1803"]),
            dict(rok="1784", text="Farář Brixi zakládá novou matriku pro ves Planá, už s čísly domů.", st="doc",
                 r=["plana_matrika_titul_1784"]),
            dict(rok="27. 1. 1793", text="Na faře umírá malíř Eugen, bratr farní kuchařky, 61 let.", st="doc",
                 r=["plana_umrti_cp1_eugen_1793"]),
            dict(rok="16. 4. 1803", text="V noci umírá na mrtvici farář Jeroným Brixi. Pohřbil ho bývalý plaský opat Celestin Werner.",
                 st="doc", r=["plana_umrti_cp1_brixi_1803"]),
            dict(rok="1803", text="Faru přebírá Jan Nepomuk Nahlowsky z Prahy, dosud ředitel vzorové školy ve Zbirohu.",
                 st="doc", r=["plana_kur_1815", "plana_nastroje_1815"]),
            dict(rok="29. 9. 1815", text="Farář Nahlowsky umírá na faře, 53 let. Léčil ho ranhojič i lékař z Plzně.", st="doc",
                 r=["plana_umrti_cp1_nahlowsky_1815"]),
            dict(rok="12. 6. 1819", text="Náhle umírá děkan Tomáš Mikovec, 60 let.", st="doc", r=["plana_umrti_cp1_mikovec_1819"]),
            dict(rok="1825–1845", text="Faru vede Bernard Hutter, nejdřív jako farář, začátkem 40. let už jako děkan.", st="doc",
                 r=["plana_podpis_hutter_dekan_1843"]),
            dict(rok="22. 10. 1848", text="Na faře umírá farář a děkan Bernard Hutter, 65 let.", st="doc",
                 r=["plana_umrti_cp1_hutter_1848"]),
            dict(rok="2. 4. 1852", text="Večer na faře zavraždí loupežný vrah faráře Karla Nekolu. Bylo mu 65 let.", st="doc",
                 r=["plana_umrti_cp1_nekola_1852", "plana_lit_podlaha_1911"]),
            dict(rok="1852–1856", text="Farářem je František Vosmík. Umírá v roce 1856.", st="doc",
                 r=["plana_podpis_vosmik_1854", "plana_lit_podlaha_1911"]),
            dict(rok="1856–1876", text="Faru vede Karel Kummer, vyhlášený kazatel. Ze sbírek dvakrát opravil vnitřek kostela.", st="doc",
                 r=["plana_podpis_kummer_1856", "plana_lit_podlaha_1911"]),
            dict(rok="1876–1885", text="Farářem je František Eška, předtím farář v Michli.", st="lit", zdroj="Podlaha 1911, s. 313",
                 r=["plana_lit_podlaha_1911"]),
            dict(rok="1885–1902", text="Farářem je Karel Appel, vzdělaný kněz a autor dějin poutního kostela v Tejnici. Umírá v roce 1902.",
                 st="lit", zdroj="Podlaha 1911, s. 313", r=["plana_lit_podlaha_1911"]),
            dict(rok="1902–asi 1917", text="Farářem je Jan Uhlíř. V roce 1913 s ním na faře působí kaplan.", st="doc",
                 r=["plana_podpis_uhlir_1913", "plana_lit_podlaha_1911"]),
            dict(rok="1918–1950", text="Faru vede Ludvík Vaníček (nar. 1883). Kaplana už nemá. Na počátku roku 1950 uzavírá matriky, "
                 "které převzal stát.", st="doc", r=["plana_lit_adresar_1928", "plana_podpis_vanicek_1950"]),
            dict(rok="po 1950", text="Planá ztrácí vlastního faráře. Farnost a kostel spravuje později farnost Dýšina, "
                 "fara přestává sloužit svému účelu.", st="prob", r=[],
                 note="Kdy přesně odešel poslední farář, nevíme; Dýšina spravuje kostel nejpozději v roce 2011."),
            dict(rok="2026", text="Bývalá fara je soukromý dům.", st="fam", r=[]),
            dict(rok="1839", text="Mapa stabilního katastru ukazuje faru jako zděnou budovu na pozemku č. 1 západně od kostela.",
                 st="doc", r=["plana_katastr_cp1_1839"]),
        ],
        drzitele=[
            dict(od="1644", do="1785", n="Fara spravovaná cisterciáky z Plas", jak="",
                 st="prob", r=["plana_matrika_titul_1644", "plana_poznamka_kostel_1753", "plana_matrika_titul_1784"],
                 note="Fara jako budova patřila farnímu obročí. Plaskou správu dokládají faráři-cisterciáci v matrikách."),
            dict(od="1785", do="20. století", n="Římskokatolická farnost Planá (patron náboženský fond, od 1826 kníže Metternich)", jak="",
                 st="prob", r=["plana_nastroje_1815", "plana_lit_podlaha_1911"], note="Faráře jmenoval císař (1815), pak patron. Majitele ve 20. století dohledáme v pozemkové knize."),
            dict(od="?", do="dnes", n="Dnešní majitel", jak="koupě", st="fam", r=[]),
        ],
        obyvatele=[
            dict(n="P. Matyáš Valecius", y="1644", role="farář, cisterciák z Velehradu", f=["založil matriku 1644"], st="doc",
                 r=["plana_matrika_titul_1644"]),
            dict(n="P. Silvan Czarda", y="1747–1753", role="farář, cisterciák z Plas", f=["rozšířil kostel 1752–1753"], st="doc",
                 r=["plana_poznamka_kostel_1753"]),
            dict(n="P. Jeroným (Václav) Brixi", y="1738–1803", role="farář 1781–1803, cisterciák z Plas, skladatel",
                 f=["* 1738 Manětín", "† 16. 4. 1803 Planá čp. 1"], st="doc",
                 r=["plana_umrti_cp1_brixi_1803", "plana_lit_brixi_slovnik_1916"]),
            dict(n="Eugen Molisar (?)", y="asi 1732–1793", role="malíř, nejspíš z Krakova, bratr farní kuchařky",
                 f=["† 27. 1. 1793 Planá čp. 1"], st="doc", r=["plana_umrti_cp1_eugen_1793"]),
            dict(n="Jan Nepomuk Nahlowsky", y="asi 1762–1815", role="farář 1803–1815",
                 f=["z Prahy, magistr filozofie", "† 29. 9. 1815 Planá čp. 1"], st="doc",
                 r=["plana_umrti_cp1_nahlowsky_1815", "plana_kur_1815"]),
            dict(n="P. Jakub Lang", y="1815", role="kaplan, po smrti faráře správce fary", f=["z Plzně"], st="doc",
                 r=["plana_kur_1815", "plana_umrti_cp1_nahlowsky_1815"]),
            dict(n="P. Tomáš Mikovec", y="asi 1759–1819", role="děkan", f=["† 12. 6. 1819 Planá čp. 1"], st="doc",
                 r=["plana_umrti_cp1_mikovec_1819"]),
            dict(n="P. Damián Koller", y="1819", role="kaplan, po smrti děkana správce fary", f=[], st="doc",
                 r=["plana_umrti_cp1_mikovec_1819"]),
            dict(n="Bernard Hutter", y="asi 1783–1848", role="farář 1819–1848, děkan", f=["† 22. 10. 1848 Planá čp. 1"], st="doc",
                 r=["plana_podpis_hutter_dekan_1843", "plana_umrti_cp1_hutter_1848"]),
            dict(n="Karel Nekola", y="asi 1787–1852", role="farář 1848–1852", f=["dříve farář v Liblíně 1820–1827", "† 2. 4. 1852 Planá čp. 1, zavražděn"],
                 st="doc", r=["plana_umrti_cp1_nekola_1852", "plana_lit_podlaha_1911"]),
            dict(n="František Vosmík", y="1852–1856", role="farář", f=["† 1856"], st="doc", r=["plana_podpis_vosmik_1854"]),
            dict(n="Karel Kummer", y="1856–1876", role="farář, kazatel", f=[], st="doc", r=["plana_podpis_kummer_1856"]),
            dict(n="P. Josef Pracner", y="1856", role="kooperátor (kaplan)", f=[], st="doc", r=["plana_podpis_kummer_1856"]),
            dict(n="František Eška", y="1876–1885", role="farář", f=[], st="lit", r=["plana_lit_podlaha_1911"]),
            dict(n="Karel Appel", y="1885–1902", role="farář, spisovatel", f=["† 1902"], st="lit", r=["plana_lit_podlaha_1911"]),
            dict(n="Jan Uhlíř", y="1902–asi 1917", role="farář", f=[], st="doc", r=["plana_podpis_uhlir_1913"]),
            dict(n="Ludvík Vaníček", y="1883–?", role="farář asi 1918–1950", f=["* 1883", "vysvěcen 1906"], st="doc",
                 r=["plana_lit_adresar_1928", "plana_podpis_vanicek_1950"]),
        ],
        note="Fara je v matrikách od 1784 vždy čp. 1 a v katastru 1839 i dnes pozemek č. 1 – číslo se neměnilo.",
    ),
}

# Rozpory a otevřené otázky (na web do „Co hledáme“)
ISSUES = [
    ("Kdy byla postavena dnešní budova fary?", "Otevřené: v roce 1839 už stála zděná. Víc by mohl říct stavebně-historický "
     "průzkum nebo spisy fary a plaského velkostatku ve Státním oblastním archivu v Plzni."),
    ("Kdo zavraždil faráře Nekolu v roce 1852?", "Otevřené: matrika píše jen „vražda“ a soudní ohledání 4. dubna. "
     "Soudní spisy nebo noviny z jara 1852 by mohly prozradit, zda byl vrah dopaden."),
    ("Kdy odešel z Plané poslední farář?", "Otevřené: Ludvík Vaníček tu byl ještě na začátku roku 1950. Pak faru převzala správa z okolních far."),
    ("Jak se jmenoval malíř Eugen, bratr farní kuchařky?", "Otevřené: příjmení je v matrice špatně čitelné (Molisar?), přišel nejspíš z Krakova. "
     "Nevíme ani, co maloval. Možná obrazy pro kostel?"),
    ("Hrály se v Plané Brixiho skladby?", "Hypotéza: farář-skladatel tu žil 22 let a roku 1815 dostal kostel celou sadu nástrojů. "
     "Noty z farního kůru mohou být v archivu nebo v Národním muzeu."),
    ("Kdy fara přešla do soukromých rukou?", "Otevřené: pozemková kniha a katastr nemovitostí."),
]
