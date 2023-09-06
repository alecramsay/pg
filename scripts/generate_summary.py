#!/usr/bin/env python3

"""
Generate a state summary.

For example:

$ scripts/generate_summary.py
$ scripts/generate_summary -s NC

For documentation, type:

$ scripts/generate_summary.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
from operator import itemgetter
import copy

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate a state summary."
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
    """Generate a state summary."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    data_root: str = "docs/_data"

    # Gather the overlaps info

    n: int = districts_by_state[xx][plan_type.lower()]

    summary_types: list = [str, int, float]

    overlaps: dict[str, float] = dict()
    total: float = 0.0

    notable_maps: list[str] = [
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
    ]

    for label in notable_maps:
        summary_path: str = os.path.join(
            data_root, f"{xx}_2022_Congress_{label}_intersections_summary.csv"
        )
        if os.path.isfile(summary_path):
            summary: list[dict] = read_csv(summary_path, summary_types)
            summary = sorted(summary, key=itemgetter("DISTRICT%"), reverse=True)

            overlap: float = sum([x["DISTRICT%"] for x in summary][:n]) / n
            total += overlap
            overlaps[label] = overlap

        else:
            print(f"NOTE - {summary_path} not found.")
            exit(1)

    average_overlap: float = total / len(overlaps)
    overlaps["Average"] = average_overlap

    # Gather ratings info

    ratings_path: str = os.path.join(
        data_root, file_name([xx, yyyy, plan_type, "ratings"], "_", "csv")
    )
    ratings_table: list[dict] = read_csv(ratings_path, [str, int, int, int, int, int])

    baseline_ratings: dict = dict(ratings_table[-1])
    baseline_ratings.pop("Map")
    ratings_table = ratings_table[:-1]

    ratings_dict: dict[str, dict] = dict()
    for row in ratings_table:
        ratings_dict[row["Map"]] = dict(row)
        ratings_dict[row["Map"]].pop("Map")

    deltas: dict[str, dict] = copy.deepcopy(ratings_dict)
    for label, ratings in deltas.items():
        for metric in ratings:
            deltas[label][metric] -= baseline_ratings[metric]

    # TODO - Write the summary

    pass


if __name__ == "__main__":
    main()

### END ###
