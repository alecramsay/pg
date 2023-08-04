#!/usr/bin/env python3

"""
Analyze the Official & Notable maps for a state compared to the Baseline map
- Optionally suppress the radar diagrams & pulling ratings, if they've already been done
- Optionally suppress analysis of individual Notable categories, if those maps don't exist

For example:

$ scripts/analyze_state.py -s NC
$ scripts/analyze_state.py -s NC -r

$ scripts/analyze_state.py -s WV -r -p

For documentation, type:

$ scripts/analyze_state.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace
import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Analyze the Official & Notable maps for a state vs. the Baseline map"
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-r",
        "--not_radar",
        dest="not_radar",
        action="store_true",
        help="Suppress radar diagrams & pulling ratings",
    )
    parser.add_argument(
        "-p",
        "--not_proportional",
        dest="not_proportional",
        action="store_true",
        help="Suppress proportional analysis",
    )
    parser.add_argument(
        "-c",
        "--not_competitive",
        dest="not_competitive",
        action="store_true",
        help="Suppress competitive analysis",
    )
    parser.add_argument(
        "-m",
        "--not_minority",
        dest="not_minority",
        action="store_true",
        help="Suppress minority analysis",
    )
    parser.add_argument(
        "-g",
        "--not_compact",
        dest="not_compact",
        action="store_true",
        help="Suppress compact analysis",
    )
    parser.add_argument(
        "-x",
        "--not_splitting",
        dest="not_splitting",
        action="store_true",
        help="Suppress splitting analysis",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Log energies for all the maps generated for a state."""

    args: Namespace = parse_args()

    xx: str = args.state

    radar: bool = not args.not_radar
    proportional: bool = not args.not_proportional
    competitive: bool = not args.not_competitive
    minority: bool = not args.not_minority
    compact: bool = not args.not_compact
    splitting: bool = not args.not_splitting

    verbose: bool = args.verbose

    # Prune the list of comparisons, if certain maps don't exist

    comparisons: list[str] = ["Official"]
    if proportional:
        comparisons.append("Proportional")
    if competitive:
        comparisons.append("Competitive")
    if minority:
        comparisons.append("Minority")
    if compact:
        comparisons.append("Compact")
    if splitting:
        comparisons.append("Splitting")

    ### PLOT PAIRWISE RADAR DIAGRAMS & WRITE THE RATINGS TO A CSV FILE ###

    if radar:
        print()
        print("Pulling ratings for baseline map ...")
        based_id: str = baseline_maps[xx]
        os.system(f"scripts/pull_map_ratings.sh {xx} {plan_type} Baseline {based_id}")

        for label in comparisons:
            print("Plotting radar diagram for", label, "map ...")
            os.system(f"scripts/plot_radar_diagram.py {xx} {label} Baseline")

        print("Writing ratings to CSV file ...")
        os.system(f"scripts/write_ratings_table.py {xx}")

    ### FIND DISTRICT CORES ###

    print("Comparing plans to the baseline ...")

    for label in comparisons:
        print("Comparing the", label, "map ...")
        os.system(f"scripts/compare_plan_to_baseline.py -s {xx} -l {label}")

    print("Done!\n")

    pass


if __name__ == "__main__":
    main()

### END ###
