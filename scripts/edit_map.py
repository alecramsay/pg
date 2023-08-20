#!/usr/bin/env python3
#

"""
Edit the properties of a DRA map.

For example:

$ scripts/edit_map.py -s NC -i 532f03db-5243-4684-9863-166575c1ea1b -o ~/Downloads/NC/ -f display_settings.json
$ scripts/edit_map.py -s NC -i 532f03db-5243-4684-9863-166575c1ea1b -o ~/Downloads/NC/ -f display_settings.json -n

For documentation, type:

$ scripts/edit_map.py -h

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
        "-i",
        "--guid",
        default="60ab513e-197b-40a3-970b-3d8e27354775",
        help="The map guid or sharing guid",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="~/Downloads/NC/",
        help="Path to output directory",
        type=str,
    )
    parser.add_argument(
        "-f",
        "--edits",
        default="display_settings.json",
        help="The display settings file",
        type=str,
    )
    parser.add_argument(
        "-n",
        "--nodeploy",
        dest="nodeploy",
        action="store_true",
        help="Do not save changes.",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Edit the properties of a DRA map."""

    args: Namespace = parse_args()

    xx: str = args.state
    guid: str = args.guid
    output_dir: str = os.path.expanduser(args.output)
    edits: str = os.path.join(output_dir, args.edits)
    user: str = "alec@davesredistricting.org"
    nodeploy: bool = args.nodeploy

    verbose: bool = args.verbose

    #

    command: str = f"../dra-cli/editmap.js -i {guid} -f {edits} -u {user} {'-n' if nodeploy else ''}"
    if verbose:
        print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
