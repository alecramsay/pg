// Take a screenshot of map in DRA, using headless Chrome.
//
// To build:
// tsc scripts/screenshot.ts
//
// To run:
// node scripts/screenshot.js

const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  // const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox'], headless: true, ignoreHTTPSErrors:true});
  
  const page = await browser.newPage();

  const VWIDTH = 1382;
  const VHEIGHT = 790;
  const VIEWPORT = { width: VWIDTH, height: VHEIGHT }; 
  await page.setViewport(VIEWPORT);

  // const url = 'https://www.nakedcapitalism.com/';
  const url = 'https://davesredistricting.org/';
  // const url = 'https://davesredistricting.org/maps#viewmap::bbd90d8a-b4c3-4875-8ffe-4f931e141211';

  const image = '/Users/alecramsay/Downloads/screenshot.png';

  try {
    await page.goto(url, {
      waitUntil: 'domcontentloaded'
      // waitUntil: 'networkidle0'
      // waitUntil: 'networkidle2'
      // timeout: 10000
    });

    const body = await page.$("body");
    // await page.waitForSelector('#root', {timeout: 10000});

  } catch (err) {
    console.error(err);
    throw new Error('Loading page timed out.');
  }
  
  await page.screenshot({ path: image });

  await browser.close();
})();

// Resources:
// - https://code.visualstudio.com/docs/typescript/typescript-tutorial
// - https://developer.chrome.com/blog/headless-chrome/
// - https://developer.chrome.com/docs/puppeteer/get-started/
//
// - https://stackoverflow.com/questions/71656606/getting-blank-screenshot-from-puppeteer
// - https://github.com/puppeteer/puppeteer/issues/2423
//
// - https://stackoverflow.com/questions/52497252/puppeteer-wait-until-page-is-completely-loaded
// - https://medium.com/@jaredpotter1/connecting-puppeteer-to-existing-chrome-window-8a10828149e0
// - https://github.com/puppeteer/puppeteer/issues/3543
// - https://stackoverflow.com/questions/48218584/tell-puppeteer-to-open-chrome-tab-instead-of-window
// - https://stackoverflow.com/questions/62852714/pyppeteer-wait-until-all-elements-of-page-is-loaded
//
// - https://stackoverflow.com/questions/53236692/how-to-use-chrome-profile-in-puppeteer
// - https://stackoverflow.com/questions/57623828/in-puppeteer-how-to-switch-to-chrome-window-from-default-profile-to-desired-prof/57662769#57662769