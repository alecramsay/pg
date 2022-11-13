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

if validate_plans([inverted_compare, inverted_baseline]):
    # Plans have the same # of blocks

    regions: list[Region] = diff_two_plans(inverted_compare, inverted_baseline)

    preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", "data"], "_", "csv"
    )
    by_geoid: dict[str, dict] = from_preprocessed(preprocessed_path)
    regions = agg_regions(regions, by_geoid)

    sort_regions_by_pop(regions, by_geoid)

pass
