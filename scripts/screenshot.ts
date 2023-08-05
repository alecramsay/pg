// Take a screenshot of map in DRA, using headless Chrome.
//
// Thanks to Steve Marx for working out how to do this!
//
// To build:
// tsc scripts/screenshot.ts
//
// To run:
// node scripts/screenshot.js

const puppeteer = require('puppeteer');

// TODO - add command line args:
// - map guid 
// - image path

// const [url, pathInput] = process.argv.slice(2);
// if (url === undefined) {
//   console.log("Usage: node mapscreenshot.js <url> [<screenshot PNG path>]");
// }

const url = 'https://davesredistricting.org/maps#viewmap::bbd90d8a-b4c3-4875-8ffe-4f931e141211';
// const url = 'https://www.nakedcapitalism.com/';
// const url = 'https://davesredistricting.org/';

const screenshotPath = "/Users/alecramsay/Downloads/screenshot.png";
// const screenshotPath = pathInput ?? "screenshot.png";

(async () =>
{
  const browser = await puppeteer.launch({headless: "new"});

  try
  {
    const page = await browser.newPage();

    // Desired output:
    // 1998,1382

    // Viewport:
    // 2381,1481

    await page.setViewport({width: 2381, height: 1481});
    // await page.setViewport({width: 1280, height: 1024});

    // await page.setViewport({width: 2560, height: 1600});
    // await page.setViewport({width: 1998, height: 1394});

    console.log("Loading the page. This can take 30 seconds or so... ");
    await page.goto(url, {waitUntil: ['load', 'domcontentloaded', 'networkidle0'], timeout: 0});

    await page.addStyleTag({
      content: '.MuiModal-backdrop, .MuiDialog-container, .MuiButtonBase-root, .MuiTypography-root, .mapboxgl-control-container { display: none; }'
    });

    const canvas = await page.$('canvas');

    console.log(`Saving PNG to ${screenshotPath}...`);
    await canvas.screenshot({type: 'png', path: screenshotPath});

    console.log("Done!");

  } catch (e)
  {
    console.log(e)
  } finally
  {
    await browser.close();
  }

  // await page.screenshot({path: screenshotPath});

  // await browser.close();
})();

// Resources:
// - https://developer.chrome.com/blog/headless-chrome/
// - https://developer.chrome.com/docs/puppeteer/
// - https://pptr.dev/
