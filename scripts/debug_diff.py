#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

from pg import *

xx: str = "NC"
n: int = districts_by_state[xx][plan_type.lower()]
cycle: str = "2020"

### LOAD STATE DATA ###

preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
    [xx, cycle, "block", "data"], "_", "csv"
)
state: State = State()
state.load_features(preprocessed_path)

total_pop: int = state.total_pop
district_pop: int = total_pop // n


### LOAD THE BASELINE PLAN ###

baseline_path: str = path_to_file([data_dir, xx]) + file_name(
    [xx, cycle, plan_type, "Baseline"], "_", "csv"
)
baseline_plan: Plan = Plan()
baseline_plan.state = state
baseline_plan.load_assignments(baseline_path)


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
    compare_plan: Plan = Plan()
    compare_plan.state = state
    compare_plan.load_assignments(compare_path)

    if validate_plans([compare_plan.districts(), baseline_plan.districts()]):
        regions: list[Region] = diff_two_plans(compare_plan, baseline_plan)
        top_n_pct: float = sum([r.pop for r in regions[:n]]) / total_pop
        print(f"The top {n} common regions have {top_n_pct:4.2%} of the population.")
        print()

        # Prepare DictWriter output

        regions_summary: list[dict] = list()
        regions_by_block: list[dict] = list()

        i: int = 1
        cumulative: int = 0

        for region in regions:
            cumulative += region.pop
            regions_summary.append(
                {
                    "REGION": i,
                    "BASELINE": region.districts[0],
                    "OTHER": region.districts[1],
                    # "BLOCKS": region.n,
                    "POPULATION": region.pop,
                    "DISTRICT%": round(region.pop / district_pop, 4),
                    "CUMULATIVE%": round(cumulative / total_pop, 4),
                }
            )
            for geoid in region.geoids:
                regions_by_block.append(
                    {
                        "GEOID": geoid,
                        "REGION": i,
                    }
                )

            i += 1

        # Write a summary of regions to a CSV file

        # DELETED

    else:

        print("Plans have different # of blocks")

pass
