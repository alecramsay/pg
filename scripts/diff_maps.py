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

FIPS = {"MD": 24}  # TODO: add more states
xx = FIPS[state]

### LOAD THE MAPS ###

maps_by_geoid = read_maps(state, year, map_type, verbose)
maps_by_district = invert_maps(maps_by_geoid)


### DIFF THE MAPS ###

areas = diff_maps(maps_by_district, verbose)
pop_by_geoid = read_census(state, xx, verbose)


### PREP THE OUTPUT ###

area_summary = dict()
areas_by_block = dict()

i = 1
for area in areas:
    n_blocks = len(area.geoids)
    n_pop = sum_area_pop(area, pop_by_geoid)

    if n_pop > 0:
        area_summary[i] = {
            "districts": area.districts,
            "blocks": n_blocks,
            "pop": n_pop,
        }
        for geoid in area.geoids:
            areas_by_block[geoid] = i

        i += 1


### WRITE OUTPUT FILES ###

areas_csv = "results/{}_areas.csv".format(state)

write_csv(
    areas_csv,
    [
        {
            "AREA": k,
            "DISTRICTS": stringify_districts(v["districts"]),
            "BLOCKS": v["blocks"],
            "POPULATION": v["pop"],
        }
        for k, v in area_summary.items()
    ],
    # rows,
    ["AREA", "DISTRICTS", "BLOCKS", "POPULATION"],
)

baf_csv = "results/{}_areas_by_block.csv".format(state)

write_csv(
    baf_csv,
    [{"GEOID": k, "AREA": v} for k, v in areas_by_block.items()],
    # rows,
    ["GEOID", "AREA"],
)
