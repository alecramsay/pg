#!/usr/bin/env python3
#

"""
Update intersections DRA maps in place.

For example:

$ scripts/update/intersections_maps.py -s NC

For documentation, type:

$ scripts/update/intersections_maps.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update intersections DRA maps in place."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
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
    """Update intersections DRA maps in place."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    user: str = "alec@davesredistricting.org"

    guids_json: str = f"{xx}_{yyyy}_{plan_type}_map_guids.json"
    guids_path: str = os.path.join(output_dir, guids_json)
    guids: dict[str, Any] = read_json(guids_path)

    comparisons: list[str] = [
        "Official",
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
    ]

    for label in comparisons:
        year: str = cycle if label == "Baseline" else yyyy

        plan_csv = f"{xx}_{year}_Congress_{label}_intersections.csv"
        guid: str = guids[label.lower()]

        command: str = f"../dra-cli/importmap.js -u {user} -f {os.path.join(output_dir, plan_csv)} -x {guid}"
        print(command)
        os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
