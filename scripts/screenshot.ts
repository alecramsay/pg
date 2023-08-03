// Take a screenshot of map in DRA, using headless Chrome.
//
// To build:
// tsc scripts/screenshot.ts
//
// To run:
// node scripts/screenshot.js

const puppeteer = require('puppeteer');

console.log("Taking a screenshot...");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({ path: 'example.png' });

  await browser.close();
})();

console.log("... done.");


// Resources:
// - https://code.visualstudio.com/docs/typescript/typescript-tutorial
// - https://developer.chrome.com/docs/puppeteer/get-started/