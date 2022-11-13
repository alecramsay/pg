#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

from pg import *


### PARSE ARGS ###

xx: str = "NC"
label: str = "Proportional"


### READ PLANS ###

compare_path: str = path_to_file([data_dir, xx]) + file_name(
    [xx, yyyy, plan_type, label], "_", "csv"
)
compare_plan: list[dict[str, int]] = from_baf(compare_path)

baseline_path: str = path_to_file([data_dir, xx]) + file_name(
    [xx, cycle, plan_type, "Baseline"], "_", "csv"
)
baseline_plan: list[dict[str, int]] = from_baf(baseline_path)


###

inverted_compare: dict[int, set[str]] = invert_plan(compare_plan)
inverted_baseline: dict[int, set[str]] = invert_plan(baseline_plan)

preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
    [xx, cycle, "block", "data"], "_", "csv"
)
features: defaultdict[Feature] = rehydrate_features(preprocessed_path)

n: int = districts_by_state[xx][plan_type.lower()]
total: int = 0
for geoid, feature in features.items():
    total += feature["pop"]

if validate_plans([inverted_compare, inverted_baseline]):
    regions: list[Region] = diff_two_plans(
        inverted_compare, inverted_baseline, features
    )

    top_n_pct: float = sum([r["pop"] for r in regions[:n]]) / total
    print(f"The top {n} common regions have {top_n_pct:4.2%} of the population.")

else:
    print("Plans have different # of blocks")

pass
