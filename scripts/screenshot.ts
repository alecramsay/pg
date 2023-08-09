// Take a screenshot of map in DRA, using headless Chrome.
//
// Thanks to Steve Marx for working out how to do this!
//
// To build:
// tsc scripts/screenshot.ts
//
// To run:
// node scripts/screenshot.js

// TODO - Parameterize this

const puppeteer = require('puppeteer');

// TODO - add command line args:
// - map guid 
// - image path

// const [url, pathInput] = process.argv.slice(2);
// if (url === undefined) {
//   console.log("Usage: node mapscreenshot.js <url> [<screenshot PNG path>]");
// }

const url = 'https://davesredistricting.org/maps#viewmap::bbd90d8a-b4c3-4875-8ffe-4f931e141211';

const screenshotPath = "/Users/alecramsay/Downloads/screenshot.png";
// const screenshotPath = pathInput ?? "screenshot.png";

(async () =>
{
  const browser = await puppeteer.launch({headless: "new"});
  // const browser = await puppeteer.launch({
  //   headless: "new", args: [
  //     '--user-data-dir=/Users/alecramsay/Library/Application Support/Google/Chrome/Profile 1']
  // });

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

    console.log("Loading the page. This can take 30 seconds or so... ");
    await page.goto(url, {waitUntil: ['load', 'domcontentloaded', 'networkidle0'], timeout: 0});

    await page.addStyleTag({
      content: '.MuiModal-backdrop, .MuiDialog-container, .MuiButtonBase-root, .MuiTypography-root, .mapboxgl-control-container { display: none; }'
    });

    const canvas = await page.$('canvas');

    // await page.waitFor(10000);

    let dpr = await page.evaluate('window.devicePixelRatio');
    console.log(`DPR = ${dpr}`);

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
})();

// Resources:
// - https://developer.chrome.com/blog/headless-chrome/
// - https://developer.chrome.com/docs/puppeteer/
// - https://pptr.dev/
//
// - chrome://version/
// - Profile path: /Users/alecramsay/Library/Application Support/Google/Chrome/Profile 1
//
// - https://stackoverflow.com/questions/53236692/how-to-use-chrome-profile-in-puppeteer
// - https://stackoverflow.com/questions/57623828/in-puppeteer-how-to-switch-to-chrome-window-from-default-profile-to-desired-prof/57662769#57662769
