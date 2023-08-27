#!/usr/bin/env python3
#

"""
Expand a precinct-assignment file into a block-assignment file

For example:

$ scripts/expand_precincts_to_blocks.py -s NC -o ~/Downloads/NC/ -f NC20C_baseline_100.csv

For documentation, type:

$ scripts/expand_precincts_to_blocks.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Expand a precinct-assignment file to a block-assignment file."
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
        help="Path to the output root",
        type=str,
    )
    parser.add_argument(
        "-f",
        "--file",
        default="NC20C_baseline_100.csv",
        help="Precinct-assignment file to expand",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--label",
        default="Baseline",
        help="The type of map (e.g., Baseline)",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Expand a precinct-assignment file into a block-assignment file."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)
    paf: str = os.path.join(output_dir, args.file)
    label: str = args.label

    verbose: bool = args.verbose

    # Debug

    # xx = "FL"
    # output_dir = os.path.expanduser("~/Downloads/FL/")
    # paf = os.path.join(output_dir, "FL20C_baseline_100.csv")

    #

    unit: str = study_unit(xx)
    year: str = cycle if label == "Baseline" else yyyy
    expanded_path: str = os.path.join(
        output_dir, file_name([xx, year, plan_type, label], "_", "csv")
    )

    # Unpickle blocks by vtd or bg

    rel_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, unit, "blocks"], "_", "pickle"
    )
    blocks_by_precinct: dict = read_pickle(rel_path)

    # Read the precinct-assignment file

    types: list = [str, int]
    precinct_assignments: list = read_csv(paf, types)  # A list of dicts

    # Map vtd assignments to block assignments

    block_assignments: list = list()
    for assignment in precinct_assignments:
        precinct: str = assignment["GEOID"]
        district: int = assignment["DISTRICT"]

        if precinct not in blocks_by_precinct:
            print(f"Warning: {precinct} not in blocks_by_precinct!")
            continue

        for block in blocks_by_precinct[precinct]:
            block_assignments.append({"GEOID": block, "DISTRICT": district})

    write_csv(expanded_path, block_assignments, ["GEOID", "DISTRICT"])

    pass


if __name__ == "__main__":
    main()

### END ###
