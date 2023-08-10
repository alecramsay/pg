#!/usr/bin/env python3

"""
Analyze the official & notable maps for a state compared to a given baseline map
(1 of 2 scripts)

For example:

$ scripts/analyze_state_part1.py
$ scripts/analyze_state_part1.py -s NC
$ scripts/analyze_state_part1.py -s NC -b ../baseline/maps/NC/NC20C_baseline_100.csv -o ~/Downloads/

For documentation, type:

$ scripts/analyze_state_part1.py -h

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
        # default="../baseline/maps/NC/NC20C_baseline_100.csv",
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
        "-x",
        "--execute",
        dest="execute",
        action="store_true",
        help="Execute the commands",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Analyze the official & notable maps for a state compared to a given baseline map.

    Part 1 of 2:
    - Run this command, and after the maps are imported into DRA
    - Run analyze_state_part2.py

    """

    args: Namespace = parse_args()

    xx: str = args.state
    baseline: str = (
        os.path.expanduser(args.baseline)
        if args.baseline
        else f"../baseline/maps/{xx}/{xx}20C_baseline_100.csv"
    )
    output: str = os.path.expanduser(args.output)
    execute: bool = args.execute

    verbose: bool = args.verbose

    print(f"Analyzing {xx} maps...")

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
        if execute:
            os.mkdir(output_dir)

    # Copy CSVs for the official, notable, and baseline maps to the output directory,
    # building a list of comparison maps. Save it for Part 2.

    print(f"Copying CSVs for the official, notable, and baseline maps ...")

    if execute:
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
            if execute:
                shutil.copy(map_path, output_dir)
            comparisons.append(label)

    command: str = ""

    # Expand the baseline map to blocks

    print("Expanding the baseline CSV to a block-assignment file ...")

    command = f"scripts/expand_vtds_to_blocks.py -s {xx} -o {output_dir} -f {base_path}"
    if execute:
        os.system(command)
    else:
        print(command)

    # Renumber & compare the maps to the baseline

    print(
        "Comparing maps to the baseline & canonicalizing districts to the official ids ..."
    )

    for label in comparisons:
        base_csv: str = (
            output_dir
            + "/"
            + (
                f"{xx}_{yyyy}_Congress_Official.csv"
                if label == "Official"
                else f"{xx}_{cycle}_Congress_Baseline_canonical.csv"
            )
        )
        compare_csv: str = (
            output_dir
            + "/"
            + (
                f"{xx}_{cycle}_Congress_Baseline.csv"
                if label == "Official"
                else f"{xx}_{yyyy}_Congress_{label}.csv"
            )
        )
        intersections_csv: str = (
            output_dir + "/" + f"{xx}_{yyyy}_Congress_{label}_intersections.csv"
        )

        renumbered_csv: str = (
            output_dir
            + "/"
            + (
                f"{xx}_{cycle}_Congress_Baseline_canonical.csv"
                if label == "Official"
                else f"{xx}_{yyyy}_Congress_{label}_canonical.csv"
            )
        )

        if verbose:
            print()
            print(f"label: {label}")
            print(f"base_csv: {base_csv}")
            print(f"compare_csv: {compare_csv}")
            print(f"intersections: {intersections_csv}")
            print(f"renumbered_csv: {renumbered_csv}")

        command = f"scripts/diff_two_plans.py -s {xx} -b {base_csv} -c {compare_csv}  -i {intersections_csv} -r {renumbered_csv}"
        if execute:
            os.system(command)
        else:
            print(command)

    # Import the BAFs into DRA maps

    print(f"Importing the BAFs into DRA ...")

    for label in comparisons + ["Baseline"]:
        year: str = cycle if label == "Baseline" else yyyy

        plan: str = (
            f"{xx}_{year}_Congress_Official.csv"
            if label == "Official"
            else f"{xx}_{year}_Congress_{label}_canonical.csv"
        )

        # TODO - Capture the output of the import command & save it for Part 2
        command = (
            f"scripts/import_plan.py -s {xx} -f {output_dir + '/' + plan} -l {label}"
        )
        if execute:
            os.system(command)
        else:
            print(command)

        if label != "Baseline":
            plan = f"{xx}_{year}_Congress_{label}_intersections.csv"

            command: str = f"scripts/import_plan.py -s {xx} -f {output_dir + '/' + plan} -l {label} -i"
            if execute:
                os.system(command)
            else:
                print(command)

    # Create & save a dict of maps & guids

    print("TODO - Creating & saving a dict of maps & guids ...")

    # Generate a YAML fragment

    print(f"Generating a YAML fragment ...")

    command = f"scripts/write_yaml_fragment.py -s {xx} -o {output_dir}"
    if execute:
        os.system(command)
    else:
        print(command)

    # Generate intersection tables

    print(f"Generating intersection tables ...")

    for label in comparisons:
        assignments_csv: str = (
            output_dir + f"{xx}_{yyyy}_Congress_{label}_intersections.csv"
        )
        summary_csv: str = (
            output_dir + f"{xx}_{yyyy}_Congress_{label}_intersections_summary.csv"
        )

        command = f"scripts/make_intersections_table.py -s {xx} -i {assignments_csv} -o {summary_csv}"
        if execute:
            os.system(command)
        else:
            print(command)

    print("... done!\n")


if __name__ == "__main__":
    main()

### END ###
