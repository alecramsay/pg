#!/usr/bin/env python3

"""
Diff two plans, adding the district cores.

For example:

$ scripts/revise/add_cores.py
$ scripts/revise/add_cores.py -s NC -o ~/Downloads/NC/ -b base.csv -c compare.csv -r new_compare.csv -i intersections.csv

For documentation, type:

$ scripts/revise/add_cores.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Diff two plans, adding the district cores."
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
        default="NC_2020_Congress_Baseline_canonical.csv",
        help="Base plan (with the canonical district numbers)",
        type=str,
    )
    parser.add_argument(
        "-c",
        "--compareplan",
        default="NC_2022_Congress_Official.csv",
        help="Plan to compare to the base plan",
        type=str,
    )
    # parser.add_argument(
    #     "-r",
    #     "--renumbered",
    #     default="NC_2020_Congress_Baseline_canonical.csv",
    #     help="Path to the renumbered compare plan",
    #     type=str,
    # )
    # parser.add_argument(
    #     "-i",
    #     "--intersections",
    #     default="NC_2020_Congress_Baseline_intersections.csv",
    #     help="Resulting intersections",
    #     type=str,
    # )
    parser.add_argument(
        "-m",
        "--maxcores",
        default="NC_2020_Congress_Official_cores.csv",
        help="Resulting district cores",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Diff two plans, adding the district cores."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)
    base_csv: str = os.path.join(output_dir, args.baseplan)
    compare_csv: str = os.path.join(output_dir, args.compareplan)
    # intersections_csv: str = os.path.join(output_dir, args.intersections)
    # renumbered_csv: str = os.path.join(output_dir, args.renumbered)
    cores_csv: str = os.path.join(output_dir, args.maxcores)

    verbose: bool = args.verbose

    #

    assignments_csv: str = base_csv + " " + compare_csv
    data_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", "data"], "_", "csv"
    )

    # Third pass, assuming first two passes are done
    command: str = f"python3 {dccvt_py}/geoid.py cores \
        --assignments {assignments_csv} \
        --population {data_csv} \
        --maxcores {cores_csv} \
        --renumber {os.path.expanduser(f'~/Downloads/{xx}/ignore.csv')}"
    if verbose:
        print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
