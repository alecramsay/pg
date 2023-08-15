#!/usr/bin/env python3
#

"""
Update DRA maps, giving them xid's.

For example:

$ scripts/update/intersections_maps.py -s NC

For documentation, type:

$ scripts/update/intersections_maps.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Update DRA maps, giving them xid's."
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
        default="~/Downloads/NC/",
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
    """Update DRA maps, giving them xid's."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    comparisons: list[str] = [
        "Official",
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
    ]

    #

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

        command = f"scripts/import_plan.py -s {xx} -o {output_dir} -f {plan_csv} -l {label} -g {guids_txt}"
        print(command)
        os.system(command)

        ## Import the intersection maps
        if label != "Baseline":
            plan_csv = f"{xx}_{year}_Congress_{label}_intersections.csv"
            guids_txt: str = f"{xx}_{year}_Congress_{label}_intersections_guids.txt"

            command: str = f"scripts/import_plan.py -s {xx} -o {output_dir} -f {plan_csv} -l {label} -g {guids_txt} -i"
            print(command)
            os.system(command)

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

    pass


if __name__ == "__main__":
    main()

### END ###
