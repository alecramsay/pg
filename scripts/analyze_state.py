#!/usr/bin/env python3

"""
Analyze the official & notable maps for a state compared to a given baseline map

For example:

$ scripts/analyze_state.py -s NC

For documentation, type:

$ scripts/analyze_state.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace
import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Analyze the official & notable maps for a state compared to a given baseline map"
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
        default="../baseline/maps/NC/NC20C_baseline_100.csv",
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
    """Analyze the official & notable maps for a state compared to a given baseline map."""

    args: Namespace = parse_args()

    xx: str = args.state
    baseline: str = args.baseline
    output: str = args.output

    verbose: bool = args.verbose

    # Echo arguments

    print(f"Analyzing {xx}:")
    print(f"- baseline = {baseline}")
    print(f"- output = {output}")

    # Prune the list of comparisons, if certain maps don't exist

    # TODO

    print("Done!\n")

    pass


if __name__ == "__main__":
    main()

### END ###
