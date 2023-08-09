#!/usr/bin/env python3
#

"""
Take a screenshot of a DRA map.

For example:

$ scripts/save_map_image -s NC -l Official -i 532f03db-5243-4684-9863-166575c1ea1b 

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
        default="60ab513e-197b-40a3-970b-3d8e27354775",
        help="The map guid or sharing guid",
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

    verbose: bool = args.verbose

    #

    year: str = cycle if label == "Baseline" else yyyy

    print("TODO - Wrap a screenshot solution ...")

    pass


if __name__ == "__main__":
    main()

### END ###
