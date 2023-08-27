#!/usr/bin/env python3

"""
Analyze the official & notable maps for a state compared to a given baseline map
(1 of 2 scripts)

For example:

$ scripts/analyze_state_part1.py
$ scripts/analyze_state_part1.py -s NC
$ scripts/analyze_state_part1.py -s NC -p 081623
$ scripts/analyze_state_part1.py -s NC -b ../baseline/maps/NC/NC20C_baseline_100.csv -o ~/Downloads/

For documentation, type:

$ scripts/analyze_state_part1.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
import shutil
import datetime

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
        "-p",
        "--prefix",
        help="xid prefix (e.g., 081623)",
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
    """Analyze the official & notable maps for a state compared to a given baseline map.

    Part 1 of 2:
    - Run this command, and after the maps are imported into DRA
    - Run analyze_state_part2.py

    """

    args: Namespace = parse_args()

    xx: str = args.state
    # xx = "GA"  # NOTE - To run a specific state in the debugger
    baseline: str = (
        os.path.expanduser(args.baseline)
        if args.baseline
        else f"../baseline/maps/{xx}/{xx}20C_baseline_100.csv"
    )
    output: str = os.path.expanduser(args.output)
    prefix: str = (
        args.prefix
        if args.prefix is not None
        else f'{datetime.datetime.now().strftime("%m%d%y")}'
    )

    verbose: bool = args.verbose

    print(f"Analyzing {xx} maps...")

    ### SETUP ###

    # Validate arguments & create the output directory

    print(">>> Validating arguments & creating the output directory ...")

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

    # Log the map prefix

    xid_path: str = os.path.join(output_dir, f"{xx}_{yyyy}_{plan_type}_xid_prefix.txt")

    with open(xid_path, "w") as f:
        f.write(f"Map prefix: {prefix}")

    # Build a list of comparison maps

    print(">>> Building a list of comparison maps ...")

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

    # Expand the baseline map to blocks

    print(">>> Expanding the baseline CSV to a block-assignment file ...")

    base_csv: str = FileSpec(baseline).name + ".csv"
    command = (
        f"scripts/expand_precincts_to_blocks.py -s {xx} -o {output_dir} -f {base_csv}"
    )
    print(command)
    os.system(command)

    # Renumber & compare the maps to the baseline

    print(
        ">>> Comparing maps to the baseline & canonicalizing districts to the official ids ..."
    )

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

        # Quote the compound district ids
        intersections_csv = os.path.join(output_dir, intersections_csv)
        command = f"scripts/quote_compound_district_ids.py -f {intersections_csv}"
        print(command)
        os.system(command)

        # Generate intersection tables

    print(">>> Generating intersection tables ...")

    for label in comparisons:
        assignments_csv: str = f"{xx}_{yyyy}_Congress_{label}_intersections.csv"
        summary_csv: str = f"{xx}_{yyyy}_Congress_{label}_intersections_summary.csv"

        command = f"scripts/make_intersections_table.py -s {xx} -o {output_dir} -i {assignments_csv} -t {summary_csv}"
        print(command)
        os.system(command)

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
    print("Confirm that the maps have been imported into DRA, and then run Part 2.")
    print()


if __name__ == "__main__":
    main()

### END ###
