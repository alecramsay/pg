#!/usr/bin/env python3

"""
Update district colors.

For example:

$ scripts/update/district_colors.py
$ scripts/update/district_colors.py -s NC -o ~/Downloads/

For documentation, type:

$ scripts/update/district_colors.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update district colors."
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
        "-i",
        "--intersections",
        dest="intersections",
        action="store_true",
        help="Only do intersections",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Update district colors."""

    args: Namespace = parse_args()

    xx: str = args.state
    output: str = os.path.expanduser(args.output)
    only_intersections: bool = args.intersections

    verbose: bool = args.verbose

    print(f"Updating district_colors for {xx} ...")

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

    # Assign colors to districts for each map

    print(">>> Assigning district colors for each map ...")

    for label, guid in guids.items():  # NOTE - Missing maps are not enumerated
        if label in ["name", "ready"]:
            continue

        is_intersection: bool = True if label.endswith("-intersections") else False
        intersections_flag: str = "-i" if is_intersection else ""

        if only_intersections and not is_intersection:
            continue

        year: str = cycle if label.capitalize() == "Baseline" else yyyy
        map_type: str = ""
        if label == "official":
            map_type = label.capitalize()
        elif is_intersection:
            map_type = label.capitalize().replace("-", "_")
        else:
            map_type = f"{label.capitalize()}_canonical"

        assignments_csv: str = f"{xx}_{year}_Congress_{map_type}.csv"
        edits_json: str = f"{xx}_{year}_{plan_type}_{label.capitalize().replace('-', '_')}_display_settings.json"

        command = f"scripts/generate_map_settings.py -s {xx} -a {assignments_csv} -o {output_dir} -f {edits_json} {intersections_flag}"
        print(command)
        os.system(command)

    ###

    print("... done!\n")
    print()


if __name__ == "__main__":
    main()

### END ###
