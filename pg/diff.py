#!/usr/bin/env python3

"""
TOOLS TO DIFF TWO PLANS (DISTRICT IDS BY FEATURE GEOID)
"""

from .data import *
from .datatypes import *
from .readwrite import *
from .helpers import *


def diff_two_plans(
    to_districts: dict[int, District],
    from_districts: dict[int, District],
    features: dict[str, Feature],
) -> list[Region]:
    """Diff two inverted plans (sets of districts), a current/to plan and a from/compare plan."""

    regions: list[Region] = list()

    for from_id, from_district in from_districts.items():
        from_geoids: set = from_district["geoids"]
        for to_id, to_district in to_districts.items():
            to_geoids: set = to_district["geoids"]
            intersection: set[str] = from_geoids.intersection(to_geoids)
            if intersection:
                districts: list[int] = [from_id, to_id]
                n: int = len(intersection)
                pop: int = 0
                for geoid in intersection:
                    n += 1
                    pop += features[geoid].pop
                region: Region = Region(
                    districts=districts,
                    geoids=intersection,
                    n=n,
                    pop=pop,
                )
                regions.append(region)

    regions.sort(key=lambda region: region.pop, reverse=True)

    return regions


def compare_compound_ids(x_id: str, y_id: str) -> int:
    """Order compound district IDs by first component, then second component."""

    x1, x2 = x_id.split("/")
    y1, y2 = y_id.split("/")

    if x1 == y1:
        return int(x2) - int(y2)
    else:
        return int(x1) - int(y1)


### END ###
