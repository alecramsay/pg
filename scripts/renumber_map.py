#!/usr/bin/env python3

"""
Renumber the districts in a CSV map.

For example:

$ scripts/renumber_map.py -s NC -l Proportional

For documentation, type:

$ scripts/renumber_map.py -h

"""

import os

import argparse
from argparse import ArgumentParser, Namespace

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Diff the Official or a Notable map with the the Baseline map."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., MD)",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--label",
        default="Proportional",
        help="The type of map (e.g., Proportional)",
        type=str,
    )
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Renumber the districts in a CSV map."""

    args: Namespace = parse_args()

    xx: str = args.state
    label: str = args.label
    verbose: bool = args.verbose

    # Load the original assignments and district mapping CSV files

    original_csv: str = path_to_file([data_dir, xx]) + file_name(
        [xx, yyyy, plan_type, label], "_", "csv"
    )
    mapping_csv: str = path_to_file([data_dir, xx]) + file_name(
        [xx, yyyy, plan_type, label, "district_ids"], "_", "csv"
    )

    original: list[dict[str, int]] = read_csv(original_csv, [str, int])
    mapping: dict[int, int] = {
        m["FROM"]: m["TO"] for m in read_csv(mapping_csv, [int, int])
    }

    # Map the original assignments to the new assignments

    renumbered: list[dict] = []
    for assignment in original:
        mapped: dict = dict(assignment)
        mapped["District"] = mapping[assignment["District"]]
        renumbered.append(mapped)

    # Write the canonicalized assignments to a CSV file

    canonicalized_csv: str = path_to_file([data_dir, xx]) + file_name(
        [xx, yyyy, plan_type, label, "canonicalized"], "_", "csv"
    )

    write_csv(
        canonicalized_csv,
        renumbered,
        [
            "GEOID20",
            "District",
        ],
    )

    pass


if __name__ == "__main__":
    main()

### END ###
