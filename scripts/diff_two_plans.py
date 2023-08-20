#!/usr/bin/env python3

"""
Diff two plans, renumbering the compare map.

For example:

$ scripts/diff_two_plans.py
$ scripts/diff_two_plans.py -s NC -o ~/Downloads/NC/ -b base.csv -c compare.csv -r new_compare.csv -i intersections.csv

For documentation, type:

$ scripts/diff_two_plans.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Diff two plans, renumbering the compare plan."
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
        "-b",
        "--baseplan",
        default="NC_2022_Congress_Official.csv",
        help="Base plan (with the canonical district numbers)",
        type=str,
    )
    parser.add_argument(
        "-c",
        "--compareplan",
        default="NC_2020_Congress_Baseline.csv",
        help="Plan to compare to the base plan",
        type=str,
    )
    parser.add_argument(
        "-r",
        "--renumbered",
        default="NC_2020_Congress_Baseline_canonical.csv",
        help="Path to the renumbered compare plan",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--intersections",
        default="NC_2020_Congress_Baseline_intersections.csv",
        help="Resulting intersections",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Diff two plans, renumbering the compare map.

    python3 ../dccvt/examples/redistricting/geoid.py cores \
    --assignments basemap.csv comparemap.csv \
    --population population.csv
    --diff intersections.csv \
    --renumber new_comparemap.csv
    """

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)
    base_csv: str = os.path.join(output_dir, args.baseplan)
    compare_csv: str = os.path.join(output_dir, args.compareplan)
    intersections_csv: str = os.path.join(output_dir, args.intersections)
    renumbered_csv: str = os.path.join(output_dir, args.renumbered)

    verbose: bool = args.verbose

    #

    assignments_csv: str = base_csv + " " + compare_csv
    data_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", "data"], "_", "csv"
    )

    # TODO - Todd: Fix the 'cores' command (#51)

    # First pass
    command: str = f"python3 {dccvt_py}/geoid.py cores \
        --assignments {assignments_csv} \
        --population {data_csv} \
        --maxcores {os.path.expanduser(f'~/Downloads/{xx}/ignore.csv')} \
        --renumber {renumbered_csv}"
    if verbose:
        print(command)
    os.system(command)

    # Second pass
    assignments_csv = base_csv + " " + renumbered_csv
    command: str = f"python3 {dccvt_py}/geoid.py cores \
        --assignments {assignments_csv} \
        --diff {intersections_csv}"
    if verbose:
        print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
