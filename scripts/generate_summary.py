#!/usr/bin/env python3

"""
Calculate the average overlap between the notable & baseline maps.

For example:

$ scripts/calc_overlaps.py
$ scripts/calc_overlaps.py -s NC

For documentation, type:

$ scripts/calc_overlaps.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
from operator import itemgetter

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Calculate the average overlap between the notable & baseline maps."
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
    """Calculate the average overlap between the notable & baseline maps."""

    args: Namespace = parse_args()

    xx: str = args.state
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    n: int = districts_by_state[xx][plan_type.lower()]

    summary_root: str = "docs/_data"
    summary_types: list = [str, int, float]

    overlaps: list[float] = list()

    notable_maps: list[str] = [
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
    ]

    print()
    print(f"Overlaps for {xx}:")

    for label in notable_maps:
        summary_path: str = os.path.join(
            summary_root, f"{xx}_2022_Congress_{label}_intersections_summary.csv"
        )
        if os.path.isfile(summary_path):
            summary: list[dict] = read_csv(summary_path, summary_types)
            summary = sorted(summary, key=itemgetter("DISTRICT%"), reverse=True)

            overlap: float = sum([x["DISTRICT%"] for x in summary][:n]) / n
            overlaps.append(overlap)
            # overlaps.append(sum([x["DISTRICT%"] for x in summary][:n]) / n)

            print(f"- {label} overlap: {overlap * 100:.1f}%")

        else:
            print(f"NOTE - {summary_path} not found.")

    average_overlap: float = sum(overlaps * 100) / len(overlaps)
    print(f"Average: {average_overlap:.1f}%")
    print()

    pass


if __name__ == "__main__":
    main()

### END ###
