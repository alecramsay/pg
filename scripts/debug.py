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

### LOAD THE MAPS & DATA ###

maps_by_geoid = read_maps(state, year, map_type, verbose)
maps_by_district = invert_maps(maps_by_geoid)
pop_by_geoid = read_census(state, xx, verbose)


### DIFF THE MAPS & SORT AREAS BY POPULATION ###

areas = diff_maps(maps_by_district, verbose)
sorted_areas = sort_areas_by_pop(areas, pop_by_geoid)

print()
