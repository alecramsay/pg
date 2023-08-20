#!/usr/bin/env python3
#

"""
Pull the ratings for a DRA map.

For example:

$ scripts/pull_map_ratings -s NC -l Official -i 6e8268a4-3b9b-4140-8f99-e3544a2f0816 -o ~/Downloads/NC/

For documentation, type:

$ scripts/pull_map_ratings.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Pull the ratings for a DRA map."
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
        default="Official",
        help="The type of map (e.g., Official)",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--guid",
        default="6e8268a4-3b9b-4140-8f99-e3544a2f0816",
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
    """Pull the ratings for a DRA map."""

    args: Namespace = parse_args()

    xx: str = args.state
    label: str = args.label
    guid: str = args.guid
    output_dir: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    year: str = cycle if label == "Baseline" else yyyy

    command: str = f"scripts/pull_map_ratings.sh {xx} {year} {plan_type} {label} {guid} {output_dir}"
    if verbose:
        print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
