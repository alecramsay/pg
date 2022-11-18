#!/usr/bin/env python3

"""
Write Official map, Notable maps, and Baseline map ratings to a table in a CSV.

For example:

$ scripts/write_ratings_table.py NC

For documentation, type:

$ scripts/write_ratings_table.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

from pg import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(
    description="Analyze the Official & Notable maps for a state vs. the Baseline map"
)

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)
parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args: Namespace = parser.parse_args()

xx: str = args.state


### WRITE THE RATINGS TO A CSV FILE ###

ratings_table: list[dict] = list()

for label in [
    "Proportional",
    "Competitive",
    "Minority",
    "Compact",
    "Splitting",
    "Official",
    "Baseline",
]:
    ratings: Ratings = cull_ratings(
        load_json(
            path_to_file([data_dir, xx])
            + file_name([xx, yyyy, plan_type, label, "ratings"], "_", "json")
        )
    )

    # TODO
    row: dict = dict()
    row["Map"] = label
    # Prettify the dict keys for column names
    row["Most Proportional"] = ratings.proportionality
    row["Most Competitive"] = ratings.competitiveness
    row["Best Minority"] = ratings.minority_opportunity
    row["Most Compact"] = ratings.compactness
    row["Least Splitting"] = ratings.splitting

    ratings_table.append(row)

write_csv(
    path_to_file([content_dir])
    + file_name([xx, yyyy, plan_type, "ratings"], "_", "csv"),
    ratings_table,
    # rows,
    [
        "Map",
        "Most Proportional",
        "Most Competitive",
        "Best Minority",
        "Most Compact",
        "Least Splitting",
    ],
)

pass
