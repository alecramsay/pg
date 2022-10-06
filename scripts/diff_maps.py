#!/usr/bin/env python3
#

"""
Diff the notable maps for a state & year.

For example:

$ scripts/diff_maps.py MD 2022 congressional

For documentation, type:

$ scripts/diff_maps.py -h

"""

import argparse
from collections import namedtuple

from pg import *


### PARSE ARGUMENTS ###

parser = argparse.ArgumentParser(
    description="Add MM2 list seats to base congressional apportionment."
)

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)
parser.add_argument("year", help="The map year (e.g., 2022)", type=int)
parser.add_argument("type", help="The type of map (e.g., congressional)", type=str)

parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args = parser.parse_args()

state = args.state
year = args.year
map_type = args.type
verbose = args.verbose


### LOAD THE MAPS ###

maps_by_geoid = read_maps(state, year, map_type, verbose)
maps_by_district = invert_maps(maps_by_geoid)


### DIFF THE MAPS ###

areas = diff_maps(maps_by_district)

### PRINT THE RESULTS ###

total_blocks = 0
for district, geoids in maps_by_district[0].items():
    total_blocks += len(geoids)

print()
common_blocks = 0
for area in areas:
    n_blocks = len(area.geoids)
    common_blocks += n_blocks
    print(area.districts, "|", n_blocks)

print()
print("Areas:", len(areas))
print("Missing:", total_blocks - common_blocks)
print()
