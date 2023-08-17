#!/usr/bin/env python3

"""
Update the DRA maps for a state.

For example:

$ scripts/DRA_maps.py
$ scripts/DRA_maps.py -s NC
$ scripts/DRA_maps.py -s NC -p 081623

For documentation, type:

$ scripts/DRA_maps.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update the DRA maps for a state."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-b",
        "--baseline",
        help="Path to the baseline map",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="~/Downloads/",
        help="Path to output directory",
        type=str,
    )
    # TODO - Figure this out
    parser.add_argument(
        "-p",
        "--prefix",
        default="081623",
        help="xid prefix (e.g., 081623)",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Update the DRA maps for a state."""

    args: Namespace = parse_args()

    xx: str = args.state
    baseline: str = (
        os.path.expanduser(args.baseline)
        if args.baseline
        else f"../baseline/maps/{xx}/{xx}20C_baseline_100.csv"
    )
    output: str = os.path.expanduser(args.output)
    prefix: str = args.prefix

    verbose: bool = args.verbose

    print(f"Updating the DRA maps for {xx} ...")

    ### SETUP ###

    # Arguments are assumed to be valid, so no error checking is done.

    base_path: str = FileSpec(baseline).abs_path
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

    # TODO - Figure this out

    # Import the BAFs into DRA maps

    print(">>> Importing the BAFs into DRA ...")

    ## Import the primary maps
    for label in comparisons + ["Baseline"]:
        year: str = cycle if label == "Baseline" else yyyy

        plan_csv: str = (
            f"{xx}_{year}_Congress_Official.csv"
            if label == "Official"
            else f"{xx}_{year}_Congress_{label}_canonical.csv"
        )
        guids_txt: str = f"{xx}_{year}_Congress_{label}_guids.txt"

        command = f"scripts/import_plan.py -s {xx} -o {output_dir} -f {plan_csv} -l {label} -g {guids_txt} -p {prefix}"
        print(command)
        os.system(command)

        ## Import the intersection maps
        if label != "Baseline":
            plan_csv = f"{xx}_{year}_Congress_{label}_intersections.csv"
            guids_txt: str = f"{xx}_{year}_Congress_{label}_intersections_guids.txt"

            command: str = f"scripts/import_plan.py -s {xx} -o {output_dir} -f {plan_csv} -l {label} -g {guids_txt} -i"
            print(command)
            os.system(command)

    ###

    print("... done!\n")
    print()


if __name__ == "__main__":
    main()

### END ###
