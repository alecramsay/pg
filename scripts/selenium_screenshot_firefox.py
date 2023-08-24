#!/usr/bin/env python3
#

"""
Take a screenshot of map in DRA, using Python Selenium (using Firefox).

For example:

$ scripts/selenium_screenshot_firefox.py
$ scripts/selenium_screenshot_firefox.py https://davesredistricting.org/join/2d664fff-9375-4354-88d3-bde3a9bbca5a /Users/alecramsay/Downloads/screenshot.png

For documentation, type:

$ scripts/selenium_screenshot_firefox.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os
import sys
import contextlib
import time

# import datetime

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Take a screenshot of map in DRA, using Python Selenium."
    )

    parser.add_argument(
        "-u",
        "--url",
        default="https://davesredistricting.org/join/2d664fff-9375-4354-88d3-bde3a9bbca5a",
        help="URL of the DRA map to to take a screenshot of",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--image",
        default="~/Downloads/screenshot.png",
        help="Path to resulting screenshot image",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()


def main() -> None:
    """Take a screenshot of map in DRA, using Python Selenium.

    Status:
    - As is, this code produces the right size & resolution screenshot,
      but the background map and labels don't match the manual screenshot.
    - The hard wait is a hack, but it works.
    """

    args: Namespace = parse_args()

    url = args.url
    screenshot_path = os.path.expanduser(args.image)

    options = FirefoxOptions()
    options.add_argument("--headless")

    with quitting(webdriver.Firefox(options=options)) as browser:
        browser.set_window_size(2381, 1481)

        # The app & map loads behind the ToS for an unauthenticated user.
        # So, load the page, wait, and then take a screenshot of the 'canvas' element.

        browser.get(url)

        # HACK: Wait for the map to load.
        time.sleep(10)

        # Hide the occludng elements.
        style_script = """
            var style = document.createElement('style');
            style.textContent = '.MuiModal-backdrop, .MuiDialog-container, .MuiButtonBase-root, .MuiTypography-root, .mapboxgl-control-container { display: none; }';
            document.head.appendChild(style);
        """
        browser.execute_script(style_script)

        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "canvas"))
        )

        canvas = browser.find_element(By.TAG_NAME, "canvas")

        screenshot = canvas.screenshot_as_png
        with open(screenshot_path, "wb") as f:
            f.write(screenshot)

    pass


if __name__ == "__main__":
    main()

### END ###
