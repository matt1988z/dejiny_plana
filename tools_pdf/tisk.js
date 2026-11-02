// HTML brožury -> PDF (Chromium z Playwright). Použití: node tools_pdf/tisk.js <vstup.html> <vystup.pdf>
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(src), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:7.5pt;color:#7a6a58;font-family:sans-serif;padding:0 20mm 0 22mm;display:flex;justify-content:space-between"><span>Fara v Plané · dějiny domu čp. 1</span><span class="pageNumber"></span></div>',
  });
  // obálka bez zápatí: vytiskne se zvlášť a nahradí 1. stranu (tools_pdf/sloucit.py)
  await p.pdf({ path: out.replace(/\.pdf$/, '_obalka.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true, pageRanges: '1' });
  await b.close();
})();
