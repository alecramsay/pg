#!/usr/bin/env python3

"""
Analyze the Official & Notable maps for a state vs. the Baseline map

For example:

$ scripts/analyze_state.py -s NC

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
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Log energies for all the maps generated for a state."""

    args: Namespace = parse_args()

    xx: str = args.state

    # NOTE - Make sure ratings have already been pulled for the baseline map.
    # ### PULL THE BASELINE RATINGS ###

    # print()
    # print("Pulling ratings for baseline map ...")
    # based_id: str = baseline_maps[xx]
    # os.system(f"scripts/pull_map_ratings.sh {xx} {plan_type} Baseline {based_id}")

    # TODO - Uncomment this
    # ### PLOT PAIRWISE RADAR DIAGRAMS ###

    # for label in [
    #     "Official",
    #     "Proportional",
    #     "Competitive",
    #     "Minority",
    #     "Compact",
    #     "Splitting",
    # ]:
    #     print("Plotting radar diagram for", label, "map ...")
    #     os.system(f"scripts/plot_radar_diagram.py {xx} {label} Baseline")

    # TODO - Uncomment this
    # ### WRITE THE RATINGS TO A CSV FILE ###

    # print("Writing ratings to CSV file ...")
    # os.system(f"scripts/write_ratings_table.py {xx}")

    ### FIND DISTRICT CORES ###

    print("Diffing plans ...")
    # os.system(f"scripts/diff_plans.py -s {xx}")

    # TODO - Compute population by district CSV
    # TODO - Import core "maps" into DRA
    # TODO - What else?

    print("Done!\n")

    pass


if __name__ == "__main__":
    main()

### END ###
