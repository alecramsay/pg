#!/usr/bin/env python3

"""
Expand baseline precinct-assignment file to a block-assignment file.

For example:

$ scripts/baseline_BAF.py
$ scripts/baseline_BAF.py -s NC
$ scripts/baseline_BAF.py -s NC -b ../baseline/maps/NC/NC20C_baseline_100.csv -o ~/Downloads/

For documentation, type:

$ scripts/baseline_BAF.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Expand baseline precinct-assignment file to a block-assignment file."
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
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Expand baseline precinct-assignment file to a block-assignment file."""

    args: Namespace = parse_args()

    xx: str = args.state
    baseline: str = (
        os.path.expanduser(args.baseline)
        if args.baseline
        else f"../baseline/maps/{xx}/{xx}20C_baseline_100.csv"
    )
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    print(f"Updating baseline BAF for {xx} ...")

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

    # Expand the baseline map to blocks

    print(">>> Expanding the baseline CSV to a block-assignment file ...")

    base_csv: str = FileSpec(baseline).name + ".csv"
    command = f"scripts/expand_vtds_to_blocks.py -s {xx} -o {output_dir} -f {base_csv}"
    print(command)
    os.system(command)

    ###

    print("... done!\n")
    print()


if __name__ == "__main__":
    main()

### END ###
