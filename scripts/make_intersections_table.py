#!/usr/bin/env python3

"""
Make the CSV for an intersections table.

For example:

$ scripts/make_intersections_table.py
$ scripts/make_intersections_table.py -s NC -i assignments.csv -o summary.csv

For documentation, type:

$ scripts/make_intersections_table.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os
from collections import defaultdict
import functools

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make the CSV for an intersections table."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., MD)",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--intersections",
        default="~/Downloads/NC/NC_2022_Congress_Proportional_intersections.csv",
        help="Path to a base x compare plan intersections CSV",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--summary",
        default="~/Downloads/NC/NC_2022_Congress_Proportional_intersections_summary.csv",
        help="Path to a base x compare plan intersections summary CSV",
        type=str,
    )
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def compare_compound_ids(x: dict, y: dict) -> int:
    """Order compound district IDs by first component, then second component."""

    x1, x2 = x["DISTRICT"].split("/")
    y1, y2 = y["DISTRICT"].split("/")

    if x1 == y1:
        return int(x2) - int(y2)
    else:
        return int(x1) - int(y1)


def main() -> None:
    """Make the CSV for an intersections table."""

    args: Namespace = parse_args()

    xx: str = args.state
    assignments_csv: str = os.path.expanduser(args.intersections)
    summary_csv: str = os.path.expanduser(args.summary)

    n: int = districts_by_state[xx][plan_type.lower()]

    verbose: bool = args.verbose

    # Load the population data

    preprocessed_path: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", "data"], "_", "csv"
    )
    state: State = State()
    state.load_features(preprocessed_path)

    assert state.total_pop is not None
    total_pop: int = state.total_pop
    district_pop: int = total_pop // n

    # Load the intersections CSV

    intersections_plan: Plan = Plan()
    intersections_plan.state = state
    intersections_plan.load_assignments(
        assignments_csv, geoid="GEOID", district="DISTRICT"
    )

    # Sum population by intersection district

    assert intersections_plan.state.features is not None
    features: dict[str, Feature] = intersections_plan.state.features

    intersections: defaultdict[str, int] = defaultdict(int)

    for row in intersections_plan.assignments():
        geoid: str = row.geoid
        intersection_id: str = str(row.district)

        intersections[intersection_id] += features[geoid].pop

    # Write the district intersection populations to a CSV file

    intersections_summary: list[dict] = list()

    for id, pop in intersections.items():
        intersections_summary.append(
            {
                "DISTRICT": id,
                "POPULATION": pop,
                "DISTRICT%": round(pop / district_pop, 4),
            }
        )

    intersections_summary = sorted(
        intersections_summary, key=functools.cmp_to_key(compare_compound_ids)
    )

    write_csv(
        summary_csv,
        intersections_summary,
        [
            "DISTRICT",
            "POPULATION",
            "DISTRICT%",
        ],
    )

    pass


if __name__ == "__main__":
    main()

### END ###
