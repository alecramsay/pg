#!/usr/bin/env python3

"""
Generate a state summary.

For example:

$ scripts/generate_summary.py
$ scripts/generate_summary.py -s NC

For documentation, type:

$ scripts/generate_summary.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
from operator import itemgetter
import copy

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate a state summary."
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
        default="~/Downloads/",
        help="Path to output directory",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def qualify_label(label: str) -> str:
    """Add the adjective to the notable label."""

    if label in ["Proportional", "Competitive", "Compact"]:
        return f"Most {label}"
    elif label == "Minority":
        return "Best Minority"
    elif label == "Splitting":
        return "Least Splitting"
    else:
        return label


def main() -> None:
    """Generate a state summary."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    # Build a list of comparison maps

    maps_root: str = FileSpec(os.path.expanduser("data")).abs_path
    maps_dir: str = os.path.join(maps_root, xx)

    potential_notables: list[str] = [
        "Proportional",
        "Competitive",
        "Minority",
        "Compact",
        "Splitting",
    ]
    notable_maps: list[str] = []

    for label in potential_notables:
        map_path: str = os.path.join(maps_dir, f"{xx}_2022_Congress_{label}.csv")
        if os.path.isfile(map_path):
            notable_maps.append(label)

    # Gather the overlaps info

    n: int = districts_by_state[xx][plan_type.lower()]

    summary_types: list = [str, int, float]

    overlaps: dict[str, float] = dict()
    total: float = 0.0

    data_root: str = "docs/_data"

    for label in notable_maps:
        summary_path: str = os.path.join(
            data_root, f"{xx}_2022_Congress_{label}_intersections_summary.csv"
        )
        if os.path.isfile(summary_path):
            summary: list[dict] = read_csv(summary_path, summary_types)
            summary = sorted(summary, key=itemgetter("DISTRICT%"), reverse=True)

            overlap: float = sum([x["DISTRICT%"] for x in summary][:n]) / n
            total += overlap
            overlaps[label] = overlap

        else:
            print(f"NOTE - {summary_path} not found.")
            exit(1)

    average_overlap: float = total / len(overlaps)
    overlaps["Average"] = average_overlap

    # Gather ratings info

    ratings_path: str = os.path.join(
        data_root, file_name([xx, yyyy, plan_type, "ratings"], "_", "csv")
    )
    ratings_table: list[dict] = read_csv(ratings_path, [str, int, int, int, int, int])

    baseline_ratings: dict = dict(ratings_table[-1])
    baseline_ratings.pop("Map")
    ratings_table = ratings_table[:-1]

    ratings_dict: dict[str, dict] = dict()
    for row in ratings_table:
        ratings_dict[row["Map"]] = dict(row)
        ratings_dict[row["Map"]].pop("Map")

    deltas: dict[str, dict] = copy.deepcopy(ratings_dict)
    for label, ratings in deltas.items():
        for metric in ratings:
            deltas[label][metric] -= baseline_ratings[metric]

    # Write the summary

    lines: list[str] = list()
    line: str = ""

    line = f"An average of {average_overlap * 100:.0f}% of population-weighted precinct assignments are shared between the comparison notable maps and the Baseline map:"
    lines.append(line)

    lines.append("<ul>")
    for label, overlap in overlaps.items():
        if label == "Average":
            continue
        line = f"  <li>{qualify_label(label)}: {overlap * 100:.1f}%</li>"
        lines.append(line)
    lines.append("</ul>")

    line = f"The overlaps are described in detail below in the “Overlaps: Districts vs. Baseline” section."
    lines.append(line)

    lines.append("<br><br>")

    line = "Relative to the Baseline ratings &#8212; proportionality: {0}, competitiveness: {1}, minority: {2}, compactness: {3}, splitting: {4} &#8212; the notable maps illustrate some major quantifiable policy trade-offs:".format(
        baseline_ratings["Proportionality"],
        baseline_ratings["Competitiveness"],
        baseline_ratings["Minority"],
        baseline_ratings["Compactness"],
        baseline_ratings["Splitting"],
    )
    lines.append(line)

    lines.append("<ul>")
    for label, ratings in ratings_dict.items():
        if label in ["Official", "Baseline"]:
            continue
        relative: list[int] = [deltas[label][metric] for metric in deltas[label]]
        absolute: list[int] = [ratings[metric] for metric in ratings]
        line = f"  <li>{qualify_label(label)}: {relative} &rarr; {absolute}</li>"
        lines.append(line)
    lines.append("</ul>")

    official_relative: list[int] = [
        deltas["Official"][metric] for metric in deltas["Official"]
    ]
    official_absolute: list[int] = [
        ratings_dict["Official"][metric] for metric in ratings_dict["Official"]
    ]
    line = f"The Official map trades-off {official_relative} for {official_absolute} ratings."
    lines.append(line)

    lines.append("<br><br>")

    line = f"The trade-offs are described in more detail below in the “Trade-offs: Ratings vs. Baseline” section."
    lines.append(line)

    html_path: str = os.path.join(output_dir, f"{xx}_summary.html")

    with open(html_path, "w") as f:
        for line in lines:
            f.write(line + "\n")

    pass


if __name__ == "__main__":
    main()

### END ###
