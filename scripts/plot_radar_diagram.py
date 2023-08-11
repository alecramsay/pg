#!/usr/bin/env python3

"""
Plot a radar diagram comparing two maps

For example:

$ scripts/plot_radar_diagram.py -s NC -l Official -o ~/Downloads/

For documentation, type:

$ scripts/plot_radar_diagram.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    """Plot a radar diagram comparing two maps"""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Plot a radar diagram comparing two maps"
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--current",
        default="Official",
        help="The current (top) map",
        type=str,
    )
    parser.add_argument(
        "-b",
        "--compare",
        default="Baseline",
        help="The compare (bottom) map",
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
    """Plot a radar diagram comparing two maps"""

    args: Namespace = parse_args()

    xx: str = args.state
    current_subtype: str = args.current
    compare_subtype: str = args.compare
    output: str = os.path.expanduser(args.output)

    # Construct file paths

    output_root: str = FileSpec(output).abs_path
    output_dir: str = os.path.join(output_root, xx)

    current_path: str = os.path.join(
        output_dir,
        file_name([xx, yyyy, plan_type, current_subtype, "ratings"], "_", "json"),
    )
    compare_path: str = os.path.join(
        output_dir,
        file_name([xx, yyyy, plan_type, compare_subtype, "ratings"], "_", "json"),
    )

    plot_path: str = os.path.join(
        output_dir,
        file_name([xx, yyyy, plan_type, current_subtype, "radar"], "_", "png"),
    )

    # Load ratings

    current_ratings: Ratings = cull_ratings(read_json(current_path))
    compare_ratings: Ratings = cull_ratings(read_json(compare_path))

    # Plot radar diagram

    current_name: str = f"{xx} {yyyy} {type} {current_subtype}"
    compare_name: str = f"{xx} {yyyy} {type} {compare_subtype}"

    current_plan: Plan = Plan()
    current_plan.name = current_name
    current_plan.nickname = current_subtype
    current_plan.ratings = current_ratings

    compare_plan: Plan = Plan()
    compare_plan.name = compare_name
    compare_plan.nickname = compare_subtype
    compare_plan.ratings = compare_ratings

    plot_radar_diagram(current_plan, compare_plan, plot_path)


if __name__ == "__main__":
    main()

### END ###
