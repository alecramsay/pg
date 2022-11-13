#!/usr/bin/env python3

"""
Diff the Official & Notable plans with the Baseline plan.

For example:

$ scripts/diff_plans.py NC

For documentation, type:

$ scripts/diff_plans.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from pg import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(
    description="Diff the Official or a Notable map with the the Baseline map."
)

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)
parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args: Namespace = parser.parse_args()

xx: str = args.state
verbose: bool = args.verbose


### LOAD THE BASELINE PLAN ###

baseline_path: str = path_to_file([data_dir, xx]) + file_name(
    [xx, cycle, plan_type, "Baseline"], "_", "csv"
)
baseline_plan: list[dict[str, int]] = from_baf(baseline_path)
inverted_baseline: dict[int, set[str]] = invert_plan(baseline_plan)


### LOAD STATE DATA ###

preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
    [xx, cycle, "block", "data"], "_", "csv"
)
features: defaultdict[Feature] = rehydrate_features(preprocessed_path)

n: int = districts_by_state[xx][plan_type.lower()]
total: int = 0
for geoid, feature in features.items():
    total += feature["pop"]


### DIFF EACH PLAN AGAINST THE BASELINE ###

for label in [
    "Official",
    "Proportional",
    "Competitive",
    "Minority",
    "Compact",
    "Splitting",
]:
    print(f"Diffing {xx}{yy} {plan_type} {label} plan with Baseline plan:")

    compare_path: str = path_to_file([data_dir, xx]) + file_name(
        [xx, yyyy, plan_type, label], "_", "csv"
    )
    compare_plan: list[dict[str, int]] = from_baf(compare_path)
    inverted_compare: dict[int, set[str]] = invert_plan(compare_plan)

    if validate_plans([inverted_compare, inverted_baseline]):
        regions: list[Region] = diff_two_plans(
            inverted_compare, inverted_baseline, features
        )
        top_n_pct: float = sum([r["pop"] for r in regions[:n]]) / total
        print(f"The top {n} common regions have {top_n_pct:4.2%} of the population.")
        print()
    else:
        print("Plans have different # of blocks")

    # TODO - Write output to a file

#
