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
