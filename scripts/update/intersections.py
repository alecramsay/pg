#!/usr/bin/env python3
#

"""
Update intersections.csv.

For example:

$ scripts/update/intersections.py -s NC

For documentation, type:

$ scripts/update/intersections.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update intersections.csv."
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
    """Update intersections.csv."""

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

    for label in comparisons:  # Does not include "Baseline"
        base_csv: str = (
            f"{xx}_{yyyy}_Congress_Official.csv"
            if label == "Official"
            else f"{xx}_{cycle}_Congress_Baseline_canonical.csv"
        )
        compare_csv: str = (
            f"{xx}_{cycle}_Congress_Baseline.csv"
            if label == "Official"
            else f"{xx}_{yyyy}_Congress_{label}.csv"
        )
        intersections_csv: str = f"{xx}_{yyyy}_Congress_{label}_intersections.csv"
        renumbered_csv: str = (
            f"{xx}_{cycle}_Congress_Baseline_canonical.csv"
            if label == "Official"
            else f"{xx}_{yyyy}_Congress_{label}_canonical.csv"
        )

        command = f"scripts/diff_two_plans.py -s {xx} -o {output_dir} -b {base_csv} -c {compare_csv}  -i {intersections_csv} -r {renumbered_csv}"
        print(command)
        os.system(command)

        intersections_csv = output_dir + intersections_csv
        command = f"scripts/quote_compound_district_ids.py -f {intersections_csv}"
        print(command)
        os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
