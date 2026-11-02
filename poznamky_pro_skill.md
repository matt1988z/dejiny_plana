# Poznámky pro správce skillu „dejiny-domu“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné osobní údaje. Nic se neposílá automaticky.

- Kramerius: polohu článku na skenu stránky lze zjistit z proudu ALTO (`…/item/uuid:<pid>/streams/ALTO`, TextBlock HPOS/VPOS/WIDTH/HEIGHT vůči Page WIDTH/HEIGHT) – výřez novinového článku bez ručního hledání. Hodilo by se jako nástroj `kramerius.py vyrez <pid> "<slovo>"`.
- Kramerius: filtr `datum_begin` u novin 1852 vyřadil všechna relevantní čísla; hledání bez data a s německými tvary („Pfarrer“, „Plana“, „ermordet“) našlo vše.
- Wikimedia Commons opakovaně vrací 429 i na první dotaz z cloudového prostředí.
