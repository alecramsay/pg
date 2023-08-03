#! /usr/bin/env python
#
# Take screenshot of a URL.
#
# https://developer.chrome.com/blog/headless-chrome/
# https://pypi.org/project/pyppeteer/ | https://pyppeteer.github.io/pyppeteer/
#
# For example:
#
# scripts/screenshot.py
#

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(options={'defaultViewport': None})
    page = await browser.newPage()
    # https://stackoverflow.com/questions/53236692/how-to-use-chrome-profile-in-puppeteer
    # https://stackoverflow.com/questions/57623828/in-puppeteer-how-to-switch-to-chrome-window-from-default-profile-to-desired-prof/57662769#57662769
    await page.goto('https://davesredistricting.org/maps#viewmap::bbd90d8a-b4c3-4875-8ffe-4f931e141211')
    # await page.goto('https://davesredistricting.org/maps#viewmap::bbd90d8a-b4c3-4875-8ffe-4f931e141211')
    # await page.goto('https://alec:pw@davesredistricting.org/maps#viewmap::bbd90d8a-b4c3-4875-8ffe-4f931e141211')
    # await page.goto('https://davesredistricting.org/join/bbd90d8a-b4c3-4875-8ffe-4f931e141211')
    await asyncio.sleep(20)
    # await page.waitForSelector('#map')
    # await page.setViewport({'width': viewport_width, 'height': viewport_height})
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

# https://intoli.com/blog/saving-images/
# https://peter.sh/experiments/chromium-command-line-switches/
#
# https://stackoverflow.com/questions/73073064/find-specific-divs-on-page-and-remove-before-taking-screenshot-with-puppeteer
# - open Chrome full screen
# https://stackoverflow.com/questions/60548332/how-can-i-take-a-screenshot-of-a-table-using-puppeteer
# - waituntil networkidle0
#
# This opens a map from the command line in a new window:
# open -na "Google Chrome" --args --new-window https://davesredistricting.org/join/bbd90d8a-b4c3-4875-8ffe-4f931e141211
# open -na "Google Chrome" --args --new-window --screenshot https://davesredistricting.org/join/bbd90d8a-b4c3-4875-8ffe-4f931e141211
