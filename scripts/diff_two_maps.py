#!/usr/bin/env python3

"""
Diff the Official or a Notable map with the Baseline map.

For example:

$ scripts/diff_two_maps.py NC Official -v
$ scripts/diff_two_maps.py NC Proportional -v

For documentation, type:

$ scripts/diff_two_maps.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from pg import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(
    description="Diff the Official or a Notable map with the Baseline map."
)

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)
parser.add_argument(
    "label", help="The type of map (e.g., Official, Proportional)", type=str
)

parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args: Namespace = parser.parse_args()
# fips_map: dict[str, str] = make_state_codes()

xx: str = args.state
# fips: str = fips_map[xx]

verbose: bool = args.verbose


### DIFF THE TWO MAPS ###

if verbose:
    print(f"Diffing {xx} {args.label} map with Baseline map...")


### OUTPUT THE DIFFS ###


#
