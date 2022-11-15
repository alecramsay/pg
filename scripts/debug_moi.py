#!/usr/bin/env python3
#
# CALCULATE MOMENT OF INERTIA
#

import math
from collections import defaultdict

from pg import *

xx: str = "NC"

### LOAD STATE DATA ###

preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
    [xx, cycle, "block", "data"], "_", "csv"
)
fc: dict[str, Feature] = rehydrate_features(preprocessed_path)

n: int = districts_by_state[xx][plan_type.lower()]


### CALCULATE POPULATION COMPACTNESS (MOMENT OF INERTIA) ###

for label in [
    "Baseline",
    "Official",
    "Proportional",
    "Competitive",
    "Minority",
    "Compact",
    "Splitting",
]:
    year: str = yyyy if not label == "Baseline" else cycle
    plan_path: str = path_to_file([data_dir, xx]) + file_name(
        [xx, year, plan_type, label], "_", "csv"
    )
    plan: list[dict[str, int]] = from_baf(plan_path)
    inverted_plan: dict[int, set[str]] = invert_plan(plan)

    centroids: dict[int, Coordinate] = defaultdict(Coordinate)
    for district_id, geoids in inverted_plan.items():
        centroids[district_id] = district_centroid(geoids, fc)

    moi: float = calc_moi(inverted_plan, centroids, fc)
    print(f"{label} plan has a moment of inertia of {moi:4.2f}.")

pass
