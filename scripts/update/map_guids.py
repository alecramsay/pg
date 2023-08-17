#!/usr/bin/env python3

"""
Update the DRA map guids and YAML fragment for a state.

For example:

$ scripts/map_guids.py
$ scripts/map_guids.py -s NC

For documentation, type:

$ scripts/map_guids.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update the DRA map guids and YAML fragment for a state."
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


def get_map_guid(file: str) -> str:
    """Get the sharing GUID from importmap.js output"""

    with open(file, "r") as f:
        f.readline()
        f.readline()
        line: str = f.readline().strip()
        guid: str = line.split(" ")[-1]

        return guid


def main() -> None:
    """Update the DRA map guids and YAML fragment for a state."""

    args: Namespace = parse_args()

    xx: str = args.state
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    print(f"Analyzing {xx} maps...")

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

    # Create & save a dict of maps & guids

    print(">>> Creating & saving a dict of maps & guids ...")

    guids: dict[str, str] = {}

    for label in comparisons + ["Baseline"]:
        year: str = cycle if label == "Baseline" else yyyy

        primary_txt: str = os.path.join(
            output_dir, f"{xx}_{year}_Congress_{label}_guids.txt"
        )
        intersections_txt: str = os.path.join(
            output_dir, f"{xx}_{year}_Congress_{label}_intersections_guids.txt"
        )

        guid: str = get_map_guid(primary_txt)
        guids[label.lower()] = guid

        if label != "Baseline":
            guid: str = get_map_guid(intersections_txt)
            guids[f"{label.lower()}-intersections"] = guid

    guids_json: str = f"{xx}_{yyyy}_{plan_type}_map_guids.json"
    guids_path: str = os.path.join(output_dir, guids_json)

    write_json(guids_path, guids)

    # Generate a YAML fragment

    print(">>> Generating a YAML fragment ...")

    command = f"scripts/write_yaml_fragment.py -s {xx} -o {output_dir}"
    print(command)
    os.system(command)

    ###

    print("... done!\n")
    print()


if __name__ == "__main__":
    main()

### END ###
