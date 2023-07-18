#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

from pg import *

"""Sum population by core district"""

### PARSE ARGS ###

xx: str = "NC"
n: int = districts_by_state[xx][plan_type.lower()]
verbose: bool = True

label: str = "Proportional"  # compare plan

### LOAD STATE DATA ###

preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
    [xx, cycle, "block", "data"], "_", "csv"
)
state: State = State()
state.load_features(preprocessed_path)

assert state.total_pop is not None
total_pop: int = state.total_pop
district_pop: int = total_pop // n

### LOAD THE COMPARISON PLAN ###

print(f"Comparing {xx} {yyyy} {plan_type} {label} plan with Baseline plan:")

compare_path: str = path_to_file([data_dir, xx]) + file_name(
    [xx, yyyy, plan_type, label, "cores_max"], "_", "csv"
)
compare_plan: Plan = Plan()
compare_plan.state = state
compare_plan.load_assignments(compare_path, geoid="GEOID", district="DISTRICT")

### SUM POPULATION BY CORE DISTRICT ###

assert compare_plan.state.features is not None
features: dict[str, Feature] = compare_plan.state.features

cores: list[int] = [0] * n  # Zero-indexed; maybe too many

for row in compare_plan.assignments():
    geoid: str = row.geoid
    core: int = row.district
    # print(f"GeoID: {geoid}, core: {core}, pop: {features[geoid].pop}")

    cores[core - 1] += features[geoid].pop

### WRITE DISTRICT CORE POPULATIONS TO A CSV FILE ###

cores_summary: list[dict] = list()

cumulative: int = 0

for i, pop in enumerate(cores):
    if pop == 0:
        break  # Fewer cores than districts

    cumulative += pop
    cores_summary.append(
        {
            "DISTRICT": i + 1,
            "POPULATION": pop,
            "DISTRICT%": round(pop / district_pop, 4),
            "CUMULATIVE%": round(cumulative / total_pop, 4),
        }
    )

cores_csv: str = path_to_file([site_data_dir]) + file_name(
    [xx, yyyy, plan_type, label, "cores_summary"], "_", "csv"
)

write_csv(
    cores_csv,
    cores_summary,
    [
        "DISTRICT",
        "POPULATION",
        "DISTRICT%",
        "CUMULATIVE%",
    ],
)

pass
