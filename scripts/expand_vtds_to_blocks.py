#!/usr/bin/env python3
#

"""
Expand a precinct-assignment file into a block-assignment file

For example:

$ scripts/expand_vtds_to_blocks.py -s NC -o ~/Downloads/NC/ -f ~/Downloads/NC/NC20C_baseline_100.csv

For documentation, type:

$ scripts/expand_vtds_to_blocks.py -h

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
    output: str = os.path.expanduser(args.output)
    paf: str = args.file
    label: str = args.label

    verbose: bool = args.verbose

    #

    year: str = cycle if label == "Baseline" else yyyy

    output_root: str = FileSpec(output).abs_path
    output_dir: str = os.path.join(output_root, xx)
    output_path: str = os.path.join(
        output_dir, file_name([xx, year, "Congress", label], "_", "csv")
    )

    paf = os.path.join(output_dir, paf)

    # Unpickle blocks by vtd

    rel_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "vtd", "blocks"], "_", "pickle"
    )
    blocks_by_vtd: dict = read_pickle(rel_path)

    # Read the precinct-assignment file

    types: list = [str, int]
    vtd_assignments: list = read_csv(paf, types)  # A list of dicts

    # Map vtd assignments to block assignments

    block_assignments: list = list()
    for vtd_assignment in vtd_assignments:
        vtd: str = vtd_assignment["GEOID"]
        district: int = vtd_assignment["DISTRICT"]

        for block in blocks_by_vtd[vtd]:
            block_assignments.append({"GEOID": block, "DISTRICT": district})

    write_csv(output_path, block_assignments, ["GEOID", "DISTRICT"])

    pass


if __name__ == "__main__":
    main()

### END ###
