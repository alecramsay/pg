#!/usr/bin/env python3

"""
Update intersections and canonicalized BAFs for a state.

For example:

$ scripts/update/diffs.py
$ scripts/update/diffs.py -s NC

For documentation, type:

$ scripts/update/diffs.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update intersections and canonicalized BAFs for a state."
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
    """Update intersections and canonicalized BAFs for a state."""

    args: Namespace = parse_args()

    xx: str = args.state
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    print(f"Updating intersections & canonicalized BAFs for {xx} ...")

    ### SETUP ###

    # Arguments are assumed to be valid, so no error checking is done.

    output_root: str = FileSpec(output).abs_path
    output_dir: str = os.path.join(output_root, xx)

    # Build a list of comparison maps.

    maps_root: str = FileSpec(os.path.expanduser("data")).abs_path
    maps_dir: str = os.path.join(maps_root, xx)

    potential_comparisons: list[str] = [
        "Official",
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
    ]
    comparisons: list[str] = []

    for label in potential_comparisons:
        map_path: str = os.path.join(maps_dir, f"{xx}_2022_Congress_{label}.csv")
        if os.path.isfile(map_path):
            comparisons.append(label)

    command: str = ""

    ### EXECUTION ###

    # Renumber & compare the maps to the baseline

    print(
        ">>> Comparing maps to the baseline & canonicalizing districts to the official ids ..."
    )

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

        # Quote the compound district ids
        intersections_csv = os.path.join(output_dir, intersections_csv)
        command = f"scripts/quote_compound_district_ids.py -f {intersections_csv}"
        print(command)
        os.system(command)

        # Generate intersection tables

    print(">>> Generating intersection tables ...")

    for label in comparisons:
        assignments_csv: str = f"{xx}_{yyyy}_Congress_{label}_intersections.csv"
        summary_csv: str = f"{xx}_{yyyy}_Congress_{label}_intersections_summary.csv"

        command = f"scripts/make_intersections_table.py -s {xx} -o {output_dir} -i {assignments_csv} -t {summary_csv}"
        print(command)
        os.system(command)

    ###

    print("... done!\n")
    print()


if __name__ == "__main__":
    main()

### END ###
