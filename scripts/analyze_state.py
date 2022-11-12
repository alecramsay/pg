#!/usr/bin/env python3

"""
Analyze the Official & Notable maps for a state vs. the Baseline map

For example:

$ scripts/analyze_state.py NC

For documentation, type:

$ scripts/analyze_state.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace
import os

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


### PULL THE BASELINE RATINGS ###

print()
print("Pulling ratings for baseline map ...")
based_id: str = baseline_maps[xx]
os.system(f"scripts/pull_map_ratings.sh {xx} {plan_type} Baseline {based_id}")


### PLOT PAIRWISE RADAR DIAGRAMS ###

for label in [
    "Official",
    "Proportional",
    "Competitive",
    "Minority",
    "Compact",
    "Splitting",
]:
    print("Plotting radar diagram for", label, "map ...")
    os.system(f"scripts/plot_radar_diagram.py {xx} {label} Baseline")


### WRITE THE RATINGS TO A CSV FILE ###

print("Writing ratings to CSV file ...")

in_dir: str = path_to_file(["temp"])

out_dir: str = path_to_file(["content"])
csv_file: str = file_name([xx + yy, plan_type, "ratings"], "_", "csv")


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
    file: str = file_name([xx + yy, plan_type, label], "_", "json")
    ratings: Ratings = cull_ratings(load_json(in_dir + file))

    row: dict = dict()
    row["Map"] = label
    # Prettify the dict keys for column names
    row["Most Proportional"] = ratings["proportionality"]
    row["Most Competitive"] = ratings["competitiveness"]
    row["Best Minority"] = ratings["minority_opportunity"]
    row["Most Compact"] = ratings["compactness"]
    row["Least Splitting"] = ratings["splitting"]

    ratings_table.append(row)

write_csv(
    out_dir + csv_file,
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


print("Done.")

pass
