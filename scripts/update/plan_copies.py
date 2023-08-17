#!/usr/bin/env python3

"""
Update official, notable, and baseline plan copies.

For example:

$ scripts/plan_copies.py
$ scripts/plan_copies.py -s NC
$ scripts/plan_copies.py -s NC -b ../baseline/maps/NC/NC20C_baseline_100.csv -o ~/Downloads/

For documentation, type:

$ scripts/plan_copies.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
import shutil

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update official, notable, and baseline plan copies."
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

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Update official, notable, and baseline plan copies."""

    args: Namespace = parse_args()

    xx: str = args.state
    baseline: str = (
        os.path.expanduser(args.baseline)
        if args.baseline
        else f"../baseline/maps/{xx}/{xx}20C_baseline_100.csv"
    )
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    print(f"Updating plan copies for {xx} ...")

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

    # Copy CSVs for the official, notable, and baseline maps to the output directory.

    print(">>> Copying CSVs for the official, notable, and baseline maps ...")

    shutil.copy(base_path, output_dir)

    for label in comparisons:
        map_path: str = os.path.join(maps_dir, f"{xx}_2022_Congress_{label}.csv")
        if os.path.isfile(map_path):
            shutil.copy(map_path, output_dir)

    ###

    print("... done!\n")
    print()


if __name__ == "__main__":
    main()

### END ###
