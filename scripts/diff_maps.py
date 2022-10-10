#!/usr/bin/env python3
#

"""
Diff the notable maps for a state & year.

For example:

$ scripts/diff_maps.py MD 2022 congressional 8
$ scripts/diff_maps.py NY 2022 congressional 26

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
parser.add_argument("districts", help="The # of districts", type=int)

parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args = parser.parse_args()

state = args.state
year = args.year
map_type = args.type
districts = args.districts
verbose = args.verbose

xx = FIPS[state]

print("Diffing {} {} maps for {}/{} ...".format(year, map_type, state, xx))


### LOAD THE MAPS & DATA ###

maps_by_geoid = read_maps(state, year, map_type, verbose)
maps_by_district = invert_maps(maps_by_geoid)
validate_maps(maps_by_district)
pop_by_geoid = read_census(state, xx, verbose)

total_pop = sum(pop_by_geoid.values())
district_pop = round(total_pop / districts)


### DIFF THE MAPS & SORT AREAS BY POPULATION ###

diffs = diff_map_pairs(maps_by_district, verbose)
sorted_diffs = list()
for areas in diffs:
    sorted_diffs.append(sort_areas_by_pop(areas, pop_by_geoid))

# areas = diff_all_maps(maps_by_district, verbose)
# sorted_areas = sort_areas_by_pop(areas, pop_by_geoid)


### OUTPUT THE DIFFS ###

for map, sorted_areas in enumerate(sorted_diffs):
    area_summary = dict()
    areas_by_block = dict()

    label = NOTABLE_MAPS[map]
    i = 1
    cumulative = 0

    for area in sorted_areas:
        cumulative += area.population
        area_summary[i] = {
            "PROPORTIONAL": area.districts[0],
            label: area.districts[1],
            # "COMPETITIVE": area.districts[1],
            # "MINORITY": area.districts[2],
            # "COMPACT": area.districts[3],
            # "SPLITTING": area.districts[4],
            "BLOCKS": area.blocks,
            "POPULATION": area.population,
            "DISTRICT%": round(area.population / district_pop, 4),
            "CUMULATIVE%": round(cumulative / total_pop, 4),
        }
        for geoid in area.geoids:
            areas_by_block[geoid] = i

        i += 1

    areas_csv = "results/{}/{}_{}_areas.csv".format(state, state, label)

    write_csv(
        areas_csv,
        [
            {
                "AREA": k,
                "PROPORTIONAL": v["PROPORTIONAL"],
                label: v[label],
                # "COMPETITIVE": v["COMPETITIVE"],
                # "MINORITY": v["MINORITY"],
                # "COMPACT": v["COMPACT"],
                # "SPLITTING": v["SPLITTING"],
                # "BLOCKS": v["BLOCKS"],
                "POPULATION": v["POPULATION"],
                "DISTRICT%": v["DISTRICT%"],
                "CUMULATIVE%": v["CUMULATIVE%"],
            }
            for k, v in area_summary.items()
        ],
        # rows,
        [
            "AREA",
            "PROPORTIONAL",
            label,
            # "COMPETITIVE",
            # "MINORITY",
            # "COMPACT",
            # "SPLITTING",
            # "BLOCKS",
            "POPULATION",
            "DISTRICT%",
            "CUMULATIVE%",
        ],
    )

    baf_csv = "results/{}/{}_{}_areas_by_block.csv".format(state, state, label)

    write_csv(
        baf_csv,
        [{"GEOID": k, "AREA": v} for k, v in areas_by_block.items()],
        # rows,
        ["GEOID", "AREA"],
    )
