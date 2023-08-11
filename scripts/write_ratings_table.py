#!/usr/bin/env python3

"""
Write Official map, Notable maps, and Baseline map ratings to a table in a CSV.

For example:

$ scripts/write_ratings_table.py -s NC -o ~/Downloads/NC/

For documentation, type:

$ scripts/write_ratings_table.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Analyze the Official & Notable maps for a state vs. the Baseline map"
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
        help="Path to output directory",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Write the ratings to a CSV file."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    ratings_table: list[dict] = list()

    for label in [
        "Official",
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
        "Baseline",
    ]:
        map_path: str = os.path.join(output_dir, f"{xx}_2022_Congress_{label}.csv")
        if os.path.isfile(map_path):
            ratings: Ratings = cull_ratings(
                read_json(
                    os.path.join(
                        output_dir,
                        file_name([xx, yyyy, plan_type, label, "ratings"], "_", "json"),
                    )
                )
            )

            row: dict = dict()
            row = {
                "Map": qualify_label(label),
                "Proportionality": ratings.proportionality,
                "Competitiveness": ratings.competitiveness,
                "Minority": ratings.minority_opportunity,
                "Compactness": ratings.compactness,
                "Splitting": ratings.splitting,
            }

            ratings_table.append(row)

    write_csv(
        os.path.join(
            output_dir, file_name([xx, yyyy, plan_type, "ratings"], "_", "csv")
        ),
        ratings_table,
        # rows,
        [
            "Map",
            "Proportionality",
            "Competitiveness",
            "Minority",
            "Compactness",
            "Splitting",
        ],
    )


if __name__ == "__main__":
    main()

### END ###
