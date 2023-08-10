#!/usr/bin/env python3
#

"""
Import a BAF into a DRA map.

For example:

$ scripts/import_plan.py -s NC -f ~/Downloads/NC/NC_2020_Congress_Official.csv -l Official
$ scripts/import_plan.py -s NC -f ~/Downloads/NC/NC_2020_Congress_Proportional_canonical.csv -l Proportional
$ scripts/import_plan.py -s NC -f ~/Downloads/NC/NC_2020_Congress_Baseline_canonical.csv -l Baseline
$ scripts/import_plan.py -s NC -f ~/Downloads/NC/NC_2020_Congress_Official_intersections.csv -l Official -i

For documentation, type:

$ scripts/import_plan.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Import a BAF into a DRA map."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-f",
        "--file",
        default="~/Downloads/NC/NC_2020_Congress_Baseline_canonical.csv",
        help="Path to the plan CSV",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--label",
        default="Baseline",
        help="The type of map (e.g., Baseline)",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--intersections",
        dest="intersections",
        action="store_true",
        help="Intersections map",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Expand a precinct-assignment file into a block-assignment file."""

    args: Namespace = parse_args()

    xx: str = args.state
    plan: str = os.path.expanduser(args.file)
    label: str = args.label
    intersections: bool = args.intersections

    verbose: bool = args.verbose

    #

    year: str = cycle if label == "Baseline" else yyyy

    user: str = "alec@davesredistricting.org"

    name: str = f"{xx} {year} {plan_type.title()} - {label}"
    if intersections:
        name += " (intersections)"

    qualified_label: str = (
        f"Notable {label.lower()}" if label not in ["Baseline", "Official"] else label
    )
    description: str = (
        f"{label}-baseline district intersections"
        if intersections
        else f"{qualified_label} map"
    )

    tag: str = f"PG-{label.upper()}"
    if intersections:
        tag = "PG-CORES"
    elif label not in ["Baseline", "Official"]:
        tag = "PG-NOTABLE"

    #

    # TODO - Terry: Capture import breadcrumbs (#50).
    """
    On success, the importmap.js script echoes something like this:
    importmap: import succeeded: /Users/alecramsay/Downloads/NC/NC_2020_Congress_Baseline_canonical.csv (elapsed: 0:16)
    importmap: guid: e9fb3d3e-9e11-4e73-ad21-680b2feac04a
    importmap: shareguid: ff009f31-8017-4ae2-bc71-07a8f085f09e
    """

    command: str = f"../dra-cli/importmap.js -u {user} -f {plan} -T {plan_type.lower()} -N '{name}' -D '{description}' -L {tag}"
    print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
