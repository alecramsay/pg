#!/usr/bin/env python3
#
# CALCULATE MOMENT OF INERTIA
#

from collections import defaultdict

from pg import *

xx: str = "NC"

### LOAD STATE DATA ###

preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
    [xx, cycle, "block", "data"], "_", "csv"
)
state: State = State()
state.load_features(preprocessed_path)

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
    plan: Plan = Plan()
    plan.state = state
    plan.load_assignments(plan_path)

    moi: float = plan.calc_moi()
    print(f"{label} plan has a moment of inertia of {moi:4.2f}.")

pass
