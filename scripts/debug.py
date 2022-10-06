#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

# from collections import namedtuple

from pg import *


### ARGUMENTS ###

state = "MD"
year = 2022
map_type = "congressional"
verbose = True

FIPS = {"MD": 24}
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

print()
