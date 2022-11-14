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
total_pop: int = 0
for geoid, feature in features.items():
    total_pop += feature["pop"]
district_pop: int = total_pop // n

if validate_plans([inverted_compare, inverted_baseline]):
    regions: list[Region] = diff_two_plans(
        inverted_compare, inverted_baseline, features
    )

    ###

    regions_summary: dict = dict()
    regions_by_block: dict = dict()

    i: int = 1
    cumulative: int = 0

    for region in regions:
        cumulative += region["pop"]
        regions_summary[i] = {
            "BASELINE": region["districts"][0],
            "OTHER": region["districts"][1],
            "BLOCKS": region["n"],
            "POPULATION": region["pop"],
            "DISTRICT%": round(region["pop"] / district_pop, 4),
            "CUMULATIVE%": round(cumulative / total_pop, 4),
        }
        for geoid in region["geoids"]:
            regions_by_block[geoid] = i

        i += 1

    regions_csv: str = path_to_file([content_dir]) + file_name(
        [xx + yy, label, "regions"], "_", "csv"
    )

    write_csv(
        regions_csv,
        [
            {
                "REGION": k,
                "BASELINE": v["BASELINE"],
                "OTHER": v["OTHER"],
                "POPULATION": v["POPULATION"],
                "DISTRICT%": v["DISTRICT%"],
                "CUMULATIVE%": v["CUMULATIVE%"],
            }
            for k, v in regions_summary.items()
        ],
        # rows,
        [
            "REGION",
            "BASELINE",
            "OTHER",
            "POPULATION",
            "DISTRICT%",
            "CUMULATIVE%",
        ],
    )

    baf_csv: str = path_to_file([temp_dir]) + file_name(
        [xx, label, "regions_by_block"], "_", "csv"
    )

    write_csv(
        baf_csv,
        [{"GEOID": k, "REGION": v} for k, v in regions_by_block.items()],
        # rows,
        ["GEOID", "REGION"],
    )

    ###

else:
    print("Plans have different # of blocks")

pass
