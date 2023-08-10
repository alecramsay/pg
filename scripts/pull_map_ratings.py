#!/usr/bin/env python3
#

"""
Pull the ratings for a DRA map.

For example:

$ scripts/pull_map_ratings -s NC -l Official -i 6e8268a4-3b9b-4140-8f99-e3544a2f0816 

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
        default="~/Downloads/",
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
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    year: str = cycle if label == "Baseline" else yyyy

    output_root: str = FileSpec(output).abs_path
    output_dir: str = os.path.join(output_root, xx)

    url: str = f"https://davesredistricting.org/join/{guid}"

    ratings_json: str = f"{xx}_{year}_{plan_type}_{label}_ratings.json"
    ratings_path: str = output_dir + "/" + ratings_json

    command: str = f"../dra-cli/getmap.js -m -i {guid} | grep score_ >> {ratings_path}"
    # print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
