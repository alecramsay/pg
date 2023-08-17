#!/usr/bin/env python3

"""
Update radar diagrams.

For example:

$ scripts/update/radar_diagrams.py
$ scripts/update/radar_diagrams.py -s NC -o ~/Downloads/

For documentation, type:

$ scripts/update/radar_diagrams.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update radar diagrams."
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
    """Update radar diagrams."""

    args: Namespace = parse_args()

    xx: str = args.state
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    print(f"Updating radar diagrams for {xx} ...")

    ### SETUP ###

    # Validate arguments & create the output directory

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

    guids_json: str = f"{xx}_{yyyy}_{plan_type}_map_guids.json"
    guids_path: str = os.path.join(output_dir, guids_json)
    guids: dict[str, Any] = read_json(guids_path)

    command: str = ""

    ### EXECUTION ###

    # Plot the pairwise radar diagrams

    print(">>> Plotting the pairwise radar diagrams ...")

    for label, guid in guids.items():
        if (
            label in ["name", "ready"]
            or label == "baseline"
            or label.endswith("-intersections")
        ):
            continue
        command = f"scripts/plot_radar_diagram.py -s {xx} -l {label.capitalize()} -b Baseline -o {output_dir}"
        print(command)
        os.system(command)

    ###

    print("... done!\n")
    print()


if __name__ == "__main__":
    main()

### END ###
