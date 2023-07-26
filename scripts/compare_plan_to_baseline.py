#!/usr/bin/env python3

"""
Compare the Official or a Notable plan with the Baseline plan.

For example:

$ scripts/compare_plan_to_baseline.py -s NC -l Proportional

For documentation, type:

$ scripts/compare_plan_to_baseline.py -h

"""

import os

import argparse
from argparse import ArgumentParser, Namespace

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Diff the Official or a Notable map with the the Baseline map."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., MD)",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--label",
        default="Proportional",
        help="The type of map (e.g., Proportional)",
        type=str,
    )
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def find_district_cores(
    *,
    assignments_csv: str,
    max_cores_csv: str,
    all_cores_csv: str,
    data_csv: str,
    debug: bool = False,
) -> None:
    """Find district "cores" for one map vs. the baseline.

    python3 ../dccvt/examples/redistricting/geoid.py cores \
    --assignments ~/iCloud/dev/pg/data/NC/NC_2020_Congress_Baseline.csv ~/iCloud/dev/pg/data/NC/NC_2022_Congress_Proportional.csv \
    --maxcores ~/iCloud/dev/pg/data/NC/NC_2022_Congress_Proportional_cores_max.csv \
    --diff ~/iCloud/dev/pg/data/NC/NC_2022_Congress_Proportional_cores_all.csv \
    --population ~/iCloud/dev/baseline/data/NC/NC_2020_block_data.csv
    """

    command: str = f"python3 {dccvt_py}/geoid.py cores --assignments {assignments_csv} --maxcores {max_cores_csv} --diff {all_cores_csv} --population {data_csv}"
    # print(command)
    os.system(command)


def main() -> None:
    """Compare the Official or a Notable map with the Baseline map."""

    args: Namespace = parse_args()

    xx: str = args.state
    label: str = args.label
    verbose: bool = args.verbose

    n: int = districts_by_state[xx][plan_type.lower()]

    ### FIND DISTRICT "CORES" FOR ONE MAP VS. THE BASELINE. ###

    assignments_csv: str = (
        path_to_file([data_dir, xx])
        + file_name([xx, cycle, plan_type, "Baseline"], "_", "csv")
        + " "
        + path_to_file([data_dir, xx])
        + file_name([xx, yyyy, plan_type, label], "_", "csv")
    )
    max_cores_csv: str = path_to_file([data_dir, xx]) + file_name(
        [xx, yyyy, plan_type, label, "cores_max"], "_", "csv"
    )
    all_cores_csv: str = path_to_file([data_dir, xx]) + file_name(
        [xx, yyyy, plan_type, label, "cores_all"], "_", "csv"
    )
    data_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", "data"], "_", "csv"
    )

    find_district_cores(
        assignments_csv=assignments_csv,
        max_cores_csv=max_cores_csv,
        all_cores_csv=all_cores_csv,
        data_csv=data_csv,
    )

    ### IMPORT THE DISTRICT CORES INTO A DRA MAP ###

    command: str = f"scripts/import_cores_map.sh {xx} {label}"
    os.system(command)

    ### SUM POPULATION BY CORE DISTRICT ###

    # Load the state data

    preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", "data"], "_", "csv"
    )
    state: State = State()
    state.load_features(preprocessed_path)

    assert state.total_pop is not None
    total_pop: int = state.total_pop
    district_pop: int = total_pop // n

    # Load the comparison plan

    compare_path: str = path_to_file([data_dir, xx]) + file_name(
        [xx, yyyy, plan_type, label, "cores_all"], "_", "csv"
    )
    compare_plan: Plan = Plan()
    compare_plan.state = state
    compare_plan.load_assignments(compare_path, geoid="GEOID", district="DISTRICT")

    # Sum population by core district

    assert compare_plan.state.features is not None
    features: dict[str, Feature] = compare_plan.state.features

    cores: list[int] = [0] * 100  # Zero-indexed. Might need more than 100 cores.

    for row in compare_plan.assignments():
        geoid: str = row.geoid
        core: int = row.district
        # print(f"GeoID: {geoid}, core: {core}, pop: {features[geoid].pop}")

        cores[core - 1] += features[geoid].pop

    # Write the district core populations to a CSV file

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


if __name__ == "__main__":
    main()

### END ###
