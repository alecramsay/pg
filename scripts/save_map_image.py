#!/usr/bin/env python3
#

"""
Take a screenshot of a DRA map.

For example:

$ scripts/save_map_image -s NC -l Official -i 532f03db-5243-4684-9863-166575c1ea1b -o ~/Downloads/NC/

For documentation, type:

$ scripts/save_map_image.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Take a screenshot of a map."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--label",
        default="Baseline",
        help="The type of map (e.g., Baseline)",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--guid",
        default="820378d9-43a4-43c5-aa31-999e6da2702a",
        help="The map guid or sharing guid",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="~/Downloads/NC/",
        help="Path to output directory",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Take a screenshot of a map."""

    args: Namespace = parse_args()

    xx: str = args.state
    label: str = args.label
    guid: str = args.guid
    output_dir: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    year: str = cycle if label == "Baseline" else yyyy

    url: str = f"https://davesredistricting.org/join/{guid}"

    image_png: str = f"{xx}_{yyyy}_{plan_type}_{label}_map.png"
    image_path: str = os.path.join(output_dir, image_png)

    # TODO - Take the screenshot, using some solution.

    print(f"Screenshot of {xx} / {label} / {guid} ...")

    command: str = f"node scripts/screenshot.js {url} {image_path}"
    # print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
