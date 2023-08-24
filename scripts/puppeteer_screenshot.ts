// Take a screenshot of map in DRA, using puppeteer.
//
// Thanks to Steve Marx for working out the basics of how to do this!
//
// To build:
// tsc scripts/puppeteer_screenshot.ts
//
// To run:
// node scripts/puppeteer_screenshot.js https://davesredistricting.org/join/2d664fff-9375-4354-88d3-bde3a9bbca5a /Users/alecramsay/Downloads/screenshot.png
// node scripts/puppeteer_screenshot.js https://davesredistricting.org/join/2d664fff-9375-4354-88d3-bde3a9bbca5a

const puppeteer = require('puppeteer');

const [url, pathInput] = process.argv.slice(2);
if (url === undefined)
{
  throw new Error("Usage: node puppeteer_screenshot.js <url> [<screenshot PNG path>]");
}

const screenshotPath = pathInput ?? "screenshot.png";

(async () =>
{
  const browser = await puppeteer.launch({headless: "new"});

  try
  {
    const page = await browser.newPage();

    // Desired image size:
    // 1998,1382

    // Corresponding viewport:
    // 2381,1481

    await page.setViewport({width: 2381, height: 1481});

    await page.goto(url, {waitUntil: ['load', 'domcontentloaded', 'networkidle0'], timeout: 0});

    await page.addStyleTag({
      content: '.MuiModal-backdrop, .MuiDialog-container, .MuiButtonBase-root, .MuiTypography-root, .mapboxgl-control-container { display: none; }'
    });

    const canvas = await page.$('canvas');

    await canvas.screenshot({type: 'png', path: screenshotPath});

  } catch (e)
  {
    console.log(e)
  } finally
  {
    await browser.close();
  }
})();

