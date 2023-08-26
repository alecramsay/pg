#!/usr/bin/env python3

"""
Calculate the edit distance between a map & the baseline map.

For example:

$ scripts/calc_edit_distances.py
$ scripts/calc_edit_distances.py -s NC -o ~/Downloads/NC/
$ scripts/calc_edit_distances.py -s NC -o ~/Downloads/NC/ -c
$ scripts/calc_edit_distances.py -s NC -o ~/Downloads/NC/ -c > intermediate/NC/NC_2022_Congress_edit_distances.txt

For documentation, type:

$ scripts/calc_edit_distance.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
from operator import itemgetter

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Calculate the edit distance between a map & the baseline map."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="~/Downloads/NC/",
        help="Path to the output root",
        type=str,
    )
    parser.add_argument(
        "-c", "--header", dest="header", action="store_true", help="Generate a header"
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Calculate the edit distance between a map & the baseline map."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)
    header: bool = args.header

    verbose: bool = args.verbose

    # Read the canonicalized baseline map

    baseline_csv: str = f"{xx}_{cycle}_{plan_type}_Baseline_canonical.csv"
    baseline_path: str = os.path.join(output_dir, baseline_csv)
    baseline_blocks: list[dict] = read_csv(baseline_path, [str, int])

    # Read the block-to-precinct mapping

    unit: str = study_unit(xx)

    block_precinct_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", unit], "_", "csv"
    )
    block_precinct: list[dict] = read_csv(block_precinct_csv, [str, str])
    precinct_by_block: dict[str, str] = {
        row["BLOCK"]: row["PRECINCT"] for row in block_precinct
    }

    # Map block assignments to precinct assignments

    baseline_assignments: dict[str, set[int]] = dict()

    for row in baseline_blocks:
        block: str = row["GEOID"] if "GEOID" in row else row["GEOID20"]
        district: int = row["DISTRICT"] if "DISTRICT" in row else row["District"]

        precinct: str = precinct_by_block[block]

        if precinct not in baseline_assignments:
            baseline_assignments[precinct] = set()

        baseline_assignments[precinct].add(district)

    #

    compare_maps: list[str] = [
        "Official",
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
    ]

    edits: dict[str, int] = dict()
    splits: dict[str, int] = dict()

    for label in compare_maps:
        # Read the canonicalized comparison map

        compare_csv: str = (
            f"{xx}_{yyyy}_{plan_type}_{label}_canonical.csv"
            if label != "Official"
            else f"{xx}_{yyyy}_{plan_type}_Official.csv"
        )
        compare_path: str = os.path.join(output_dir, compare_csv)
        compare_blocks: list[dict] = read_csv(compare_path, [str, int])

        # Map block assignments to precinct assignments

        compare_assignments: dict[str, set[int]] = dict()

        for row in compare_blocks:
            block: str = row["GEOID"] if "GEOID" in row else row["GEOID20"]
            district: int = row["DISTRICT"] if "DISTRICT" in row else row["District"]

            precinct: str = precinct_by_block[block]

            if precinct not in compare_assignments:
                compare_assignments[precinct] = set()

            compare_assignments[precinct].add(district)

        # Compare precinct assignments

        nedits: int = 0
        nsplits: int = 0

        for k, v in baseline_assignments.items():
            if k not in compare_assignments:
                print(f"Precinct {k} not in {label}")
                continue

            baseline_district: int = next(iter(v))  # No split precincts in baseline
            nsplits += 1 if len(compare_assignments[k]) > 1 else 0
            compare_assignments[k].discard(baseline_district)
            nedits += len(compare_assignments[k])

        edits[label] = nedits
        splits[label] = nsplits

    pass

    # Print the results

    if header:
        print(
            "{0:^12}".format("XX/precincts"),
            "{0:^12}".format("Official"),
            "{0:^12}".format("Proportional"),
            "{0:^12}".format("Competitive"),
            "{0:^12}".format("Minority"),
            "{0:^12}".format("Compact"),
            "{0:^12}".format("Splitting"),
        )
        print(
            "{0:12}".format("------------"),
            "{0:12}".format("------------"),
            "{0:12}".format("------------"),
            "{0:12}".format("------------"),
            "{0:12}".format("------------"),
            "{0:12}".format("------------"),
            "{0:12}".format("------------"),
        )

    print(
        "{0:>12}".format(xx),
        "{0:>12,}".format(edits["Official"]),
        "{0:>12,}".format(edits["Proportional"]),
        "{0:>12,}".format(edits["Competitive"]),
        "{0:>12,}".format(edits["Minority"]),
        "{0:>12,}".format(edits["Compact"]),
        "{0:>12,}".format(edits["Splitting"]),
        "edits",
    )
    print(
        "{0:>12,}".format(len(baseline_assignments)),
        "{0:>12,}".format(splits["Official"]),
        "{0:>12,}".format(splits["Proportional"]),
        "{0:>12,}".format(splits["Competitive"]),
        "{0:>12,}".format(splits["Minority"]),
        "{0:>12,}".format(splits["Compact"]),
        "{0:>12,}".format(splits["Splitting"]),
        "splits",
    )


if __name__ == "__main__":
    main()

### END ###
