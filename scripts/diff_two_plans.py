#!/usr/bin/env python3

"""
Diff two plans, renumbering the compare map.

For example:

$ scripts/diff_two_plans.py
$ scripts/diff_two_plans.py -s NC -b base.csv -c compare.csv -r new_compare.csv -i intersections.csv

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
        "-b",
        "--baseplan",
        default="~/Downloads/NC/NC_2022_Congress_Official.csv",
        help="Path to the base plan (with the canonical district numbers)",
        type=str,
    )
    parser.add_argument(
        "-c",
        "--compareplan",
        default="~/Downloads/NC/NC_2022_Congress_Baseline.csv",
        help="Path to the plan to compare to the base plan",
        type=str,
    )
    parser.add_argument(
        "-r",
        "--renumbered",
        default="~/Downloads/NC/NC_2022_Congress_Baseline_canonical.csv",
        help="Path to the renumbered compare plan",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--intersections",
        default="~/Downloads/NC/NC_2022_Congress_Baseline_intersections.csv",
        help="Path to the base x compare plan intersections",
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
    base_csv: str = os.path.expanduser(args.baseplan)
    compare_csv: str = os.path.expanduser(args.compareplan)
    intersections_csv: str = os.path.expanduser(args.intersections)
    renumbered_csv: str = os.path.expanduser(args.renumbered)

    verbose: bool = args.verbose

    #

    assignments_csv: str = base_csv + " " + compare_csv
    data_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", "data"], "_", "csv"
    )

    # TODO - Remove --maxcores option

    command: str = f"python3 {dccvt_py}/geoid.py cores \
        --assignments {assignments_csv} \
        --population {data_csv} \
        --diff {intersections_csv} \
        --maxcores {os.path.expanduser('~/Downloads/NC/ignore.csv')} \
        --renumber {renumbered_csv}"
    # print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
