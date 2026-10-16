const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch());
  const p = await b.newPage({ viewport: { width: +process.env.W||1280, height: +process.env.H||720 } });
  for (const n of process.argv.slice(2)) {
    await p.goto('file://' + __dirname + '/' + n + '.html'); await p.waitForTimeout(400);
    await p.screenshot({ path: n + '.png', omitBackground: true });
  }
  await b.close();
})();
