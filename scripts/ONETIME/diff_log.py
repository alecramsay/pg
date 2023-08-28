#!/usr/bin/env python3

"""
Diff two plans, renumbering the compare map ... logging diagnostics to a file.

For example:

$ scripts/ONETIME/diff_log.py
$ scripts/ONETIME/diff_log.py -s GA -b ../baseline/maps/GA/GA20C_baseline_100.csv -o ~/Downloads/

For documentation, type:

$ scripts/ONETIME/diff_log.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
import shutil
import datetime

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Diff two plans, renumbering the compare map ... logging diagnostics to a file."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="GA",
        help="The two-character state code (e.g., GA)",
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
    """Diff two plans, renumbering the compare map ... logging diagnostics to a file."""

    args: Namespace = parse_args()

    xx: str = args.state
    baseline: str = (
        os.path.expanduser(args.baseline)
        if args.baseline
        else f"../baseline/maps/{xx}/{xx}20C_baseline_100.csv"
    )
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    ### SETUP ###

    # Validate arguments & create the output directory

    base_path: str = FileSpec(baseline).abs_path
    if not os.path.isfile(base_path):
        print(f"ERROR - Baseline map not found: {base_path}")
        exit(1)

    output_root: str = FileSpec(output).abs_path
    if not os.path.isdir(output_root):
        print(f"ERROR - Root output directory not found: {output_root}")
        exit(1)

    subdir: str = f"{xx}_diffs"
    output_dir: str = os.path.join(output_root, subdir)
    if os.path.isdir(output_dir):
        print(f"ERROR - {subdir} subdirectory already exists. Please remove it first.")
        exit(1)
    else:
        os.mkdir(output_dir)

    # Build a list of comparison maps

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

    shutil.copy(base_path, output_dir)

    for label in comparisons:
        map_path: str = os.path.join(maps_dir, f"{xx}_2022_Congress_{label}.csv")
        if os.path.isfile(map_path):
            shutil.copy(map_path, output_dir)

    # Expand the baseline map to blocks

    base_csv: str = FileSpec(baseline).name + ".csv"
    command = (
        f"scripts/expand_precincts_to_blocks.py -s {xx} -o {output_dir} -f {base_csv}"
    )
    print(command)
    os.system(command)

    # Renumber & compare the maps to the baseline

    print()
    print("Diffing notable & official maps for {xx} against the baseline:")
    print()

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

    print()


if __name__ == "__main__":
    main()

### END ###
