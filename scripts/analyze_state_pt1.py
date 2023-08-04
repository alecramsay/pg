#!/usr/bin/env python3

"""
Analyze the official & notable maps for a state compared to a given baseline map
(1 of 2 scripts)

For example:

$ scripts/analyze_state_pt1.py -s NC -b ../baseline/maps/NC/NC20C_baseline_100.csv -o ~/Downloads/ -y

For documentation, type:

$ scripts/analyze_state_pt1.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
import shutil

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Analyze the official & notable maps for a state compared to a given baseline map (1 of 2)"
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
        default="../baseline/maps/NC/NC20C_baseline_100.csv",
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
    """Analyze the official & notable maps for a state compared to a given baseline map."""

    args: Namespace = parse_args()

    xx: str = args.state
    baseline: str = os.path.expanduser(args.baseline)
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    # Validate arguments & create the output directory

    print(f"Validating arguments & creating the output directory ...")

    base_path: str = FileSpec(baseline).abs_path
    if not os.path.isfile(base_path):
        print(f"ERROR - Baseline map not found: {base_path}")
        exit(1)

    output_root: str = FileSpec(output).abs_path
    if not os.path.isdir(output_root):
        print(f"ERROR - Root output directory not found: {output_root}")
        exit(1)

    output_dir: str = os.path.join(output_root, xx)
    if os.path.isdir(output_dir):
        print(f"ERROR - {xx} subdirectory already exists. Please remove it first.")
        exit(1)
    else:
        os.mkdir(output_dir)

    # Copy CSVs for the official, notable, and baseline maps to the output directory,
    # building a list of comparison maps

    print(f"Copying CSVs for the official, notable, and baseline maps ...")
    shutil.copy(base_path, output_dir)

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
            shutil.copy(map_path, output_dir)
            comparisons.append(label)

    # Expand the baseline map to blocks

    print(f"TODO - Expanding the baseline CSV to a block-assignment file ...")

    # Renumber & compare the maps to the baseline

    print(f"TODO - Renumbering & comparing the maps to the baseline ...")

    # Import the BAFs into DRA maps

    print(f"TODO - Importing the BAFs into DRA ...")

    # Create & save a dict of maps & guids

    print(f"TODO - Creating & saving a dict of maps & guids ...")

    # Generate a YAML fragment

    print(f"TODO - Generating a YAML fragment ...")

    print("... done!\n")


if __name__ == "__main__":
    main()

### END ###
