#!/usr/bin/env python3

"""
Analyze the official & notable maps for a state compared to a given baseline map
(2 of 2 scripts)

For example:

$ scripts/analyze_state_part2.py
$ scripts/analyze_state_part2.py -s NC -b ../baseline/maps/NC/NC20C_baseline_100.csv -o ~/Downloads/

For documentation, type:

$ scripts/analyze_state_part2.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
import shutil

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Analyze the official & notable maps for a state compared to a given baseline map (2 of 2)"
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
    """Analyze the official & notable maps for a state compared to a given baseline map.

    Part 2 of 2:
    - First run analyze_state_part1.py
    - After the maps are imported into DRA, run this command

    """

    args: Namespace = parse_args()

    xx: str = args.state
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    print(f"Analyzing {xx} maps...")

    # Validate arguments & create the output directory

    print(f"Validating arguments ...")

    output_root: str = FileSpec(output).abs_path
    if not os.path.isdir(output_root):
        print(f"ERROR - Root output directory not found: {output_root}")
        exit(1)

    output_dir: str = os.path.join(output_root, xx)
    if not os.path.isdir(output_dir):
        print(f"ERROR - {xx} subdirectory not found.")
        exit(1)

    # Build a list of comparison maps

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
        map_path: str = os.path.join(output_dir, f"{xx}_2022_Congress_{label}.csv")
        if os.path.isfile(map_path):
            comparisons.append(label)

    # Load the map guids from Part 1

    print("Loading the map guids ...")

    guids_path: str = output_dir + "/" + "map_guids.json"
    guids: dict[str, Any] = read_json(guids_path)

    # Edit the display properties of each map

    print("TODO - Editing the display properties of each map ...")

    # Take a screenshot of each map

    print("TODO - Taking a screenshot of each map ...")

    # Pull the ratings for each map

    print("TODO - Pulling the ratings for each map ...")

    # Plot the pairwise radar diagrams

    print("TODO - Plotting the pairwise radar diagrams ...")

    # Write the ratings to a CSV

    print("TODO - Writing the ratings to a CSV ...")

    print("... done!\n")


if __name__ == "__main__":
    main()

### END ###
