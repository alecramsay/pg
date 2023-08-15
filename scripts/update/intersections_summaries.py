#!/usr/bin/env python3
#

"""
Update intersections.csv and intersections_summary.csv.

For example:

$ scripts/update/intersections_summaries.py -s NC

For documentation, type:

$ scripts/update/intersections_summaries.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update intersections.csv and intersections_summary.csv."
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
    """Update intersections.csv and intersections_summary.csv."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    comparisons: list[str] = [
        "Official",
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
    ]

    for label in comparisons:
        assignments_csv: str = f"{xx}_{yyyy}_Congress_{label}_intersections.csv"
        summary_csv: str = f"{xx}_{yyyy}_Congress_{label}_intersections_summary.csv"

        command = f"scripts/make_intersections_table.py -s {xx} -o {output_dir} -i {assignments_csv} -t {summary_csv}"
        print(command)
        os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
