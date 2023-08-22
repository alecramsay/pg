#!/usr/bin/env python3

"""
Analyze the official & notable maps for a state compared to a given baseline map
(2 of 2 scripts)

For example:

$ scripts/analyze_state_part2.py
$ scripts/analyze_state_part2.py -s NC -o ~/Downloads/

For documentation, type:

$ scripts/analyze_state_part2.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os

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
    # xx = "CO"  # NOTE - To run a specific state in the debugger
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    print(f"Analyzing {xx} maps...")

    ### SETUP ###

    # Validate arguments & create the output directory

    print(">>> Validating arguments ...")

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

    print(">>> Loading the map guids ...")

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

        intersections: bool = True if label.endswith("-intersections") else False
        intersections_flag: str = "-i" if intersections else ""

        year: str = cycle if label.capitalize() == "Baseline" else yyyy
        map_type: str = ""
        if label == "official":
            map_type = label.capitalize()
        elif intersections:
            map_type = label.capitalize().replace("-", "_")
        else:
            map_type = f"{label.capitalize()}_canonical"

        assignments_csv: str = f"{xx}_{year}_Congress_{map_type}.csv"
        edits_json: str = f"{xx}_{year}_{plan_type}_{label.capitalize().replace('-', '_')}_display_settings.json"

        command = f"scripts/generate_map_settings.py -s {xx} -a {assignments_csv} -o {output_dir} -f {edits_json} {intersections_flag}"
        print(command)
        os.system(command)

    # Edit the display properties of each map

    print(">>> Editing the display properties of each map ...")

    for label, guid in guids.items():  # NOTE - Missing maps are not enumerated
        if label in ["name", "ready"]:
            continue

        year: str = cycle if label.capitalize() == "Baseline" else yyyy
        edits_json: str = f"{xx}_{year}_{plan_type}_{label.capitalize().replace('-', '_')}_display_settings.json"

        command = (
            f"scripts/edit_map.py -s {xx} -i {guid} -o {output_dir} -f {edits_json}"
        )
        print(command)
        os.system(command)

    # Take a screenshot of each map

    print(">>> Taking a screenshot of each map ...")

    for label, guid in guids.items():
        if label in ["name", "ready"]:
            continue
        command = f"scripts/save_map_image.py -s {xx} -l {label.capitalize().replace('-', '_')} -i {guid}  -o {output_dir}"
        print(command)
        os.system(command)

    # Pull the ratings for each map & write the ratings to a CSV

    print(">>> Pulling the ratings for each map ...")

    for label, guid in guids.items():
        if label in ["name", "ready"] or label.endswith("-intersections"):
            continue
        command = f"scripts/pull_map_ratings.py -s {xx} -l {label.capitalize()} -i {guid} -o {output_dir}"
        print(command)
        os.system(command)

    print(">>> Writing the ratings to a CSV file ...")

    command = f"scripts/write_ratings_table.py -s {xx} -o {output_dir}"
    print(command)
    os.system(command)

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
    print("Now you can deploy the state's artifacts to the website.")
    print()


if __name__ == "__main__":
    main()

### END ###
