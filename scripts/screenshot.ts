// Take a screenshot of map in DRA, using headless Chrome.
//
// Thanks to Steve Marx for working out the basics of how to do this!
//
// To build:
// tsc scripts/screenshot.ts
//
// To run:
// node scripts/screenshot.js https://davesredistricting.org/join/820378d9-43a4-43c5-aa31-999e6da2702a /Users/alecramsay/Downloads/screenshot.png
// node scripts/screenshot.js https://davesredistricting.org/join/820378d9-43a4-43c5-aa31-999e6da2702a

const puppeteer = require('puppeteer');

const [url, pathInput] = process.argv.slice(2);
if (url === undefined)
{
  throw new Error("Usage: node screenshot.js <url> [<screenshot PNG path>]");
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
    // await page.setViewport({width: 2381, height: 1481, deviceScaleFactor: 2});

    // Device Scale Factor:
    // https://cloudinary.com/glossary/device-pixel-ratio
    // https://github.com/puppeteer/puppeteer/issues/2372 <<<
    // await page._client.send('Emulation.clearDeviceMetricsOverride');
    // https://github.com/puppeteer/puppeteer/blob/v10.4.0/docs/api.md#class-cdpsession
    // const client = await page.target().createCDPSession();
    // await client.send('Emulation.clearDeviceMetricsOverride');

    // console.log("Loading the map. This can take 30 seconds or so... ");
    await page.goto(url, {waitUntil: ['load', 'domcontentloaded', 'networkidle0'], timeout: 0});

    await page.addStyleTag({
      content: '.MuiModal-backdrop, .MuiDialog-container, .MuiButtonBase-root, .MuiTypography-root, .mapboxgl-control-container { display: none; }'
    });

    const canvas = await page.$('canvas');

    // let dpr = await page.evaluate('window.devicePixelRatio');
    // console.log(`DPR = ${dpr}`);

    await canvas.screenshot({type: 'png', path: screenshotPath});

    console.log("Done!");

  } catch (e)
  {
    console.log(e)
  } finally
  {
    await browser.close();
  }
})();

// Resources:
// - https://developer.chrome.com/blog/headless-chrome/
// - https://developer.chrome.com/docs/puppeteer/
// - https://pptr.dev/
//
// - chrome://version/
