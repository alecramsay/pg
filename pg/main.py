#!/usr/bin/env python3

"""
MAIN ROUTINES
"""

from .types import *
from .io import *
from .utils import *


def read_maps(state, year, map_type, verbose=False):
    """
    Read the maps for a state and year.
    """

    notables = ["proportional", "competitive", "minority", "compact", "splitting"]
    file_names = list()

    for notable in notables:
        file_names.append(
            "data/{}/{}_{}_{}_{}.csv".format(state, state, year, map_type, notable)
        )

    types = [str, int]
    maps_by_geoid = list()
    for csv in file_names:
        rows = read_typed_csv(csv, types)
        maps_by_geoid.append(rows)

    return maps_by_geoid


def invert_maps(maps_by_geoid):
    maps_by_district = list()

    for map_by_geoid in maps_by_geoid:
        inverted = dict()
        for row in map_by_geoid:
            geoid = row["GEOID20"]
            if is_water_only(geoid):
                continue

            district = row["District"]
            if district not in inverted:
                inverted[district] = set()

            inverted[district].add(geoid)

        maps_by_district.append(inverted)

    return maps_by_district


def diff_maps(maps_by_district):
    areas = list()

    # Add the first map's districts as the initial areas
    for district, geoids in maps_by_district[0].items():
        areas.append(Area([district], geoids))

    # Diff each successive map in succession
    for map_by_district in maps_by_district[1:]:
        new_areas = list()

        for district, geoids in map_by_district.items():
            for area in areas:
                intersection = area.geoids.intersection(geoids)
                if intersection:
                    districts = area.districts + [district]
                    new_areas.append(Area(districts, intersection))

        areas = new_areas

    areas.sort(key=lambda area: len(area.geoids), reverse=True)

    return areas
