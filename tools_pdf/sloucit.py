import sys
from pypdf import PdfReader, PdfWriter
hl, ob, out = sys.argv[1:4]
r, c = PdfReader(hl), PdfReader(ob)
w = PdfWriter()
w.add_page(c.pages[0])
for pg in r.pages[1:]:
    w.add_page(pg)
w.add_metadata({"/Title": "Fara v Plané – dějiny domu čp. 1", "/Subject": "Planá u Hromnic, 1644–dnes", "/Language": "cs"})
w.write(out)
