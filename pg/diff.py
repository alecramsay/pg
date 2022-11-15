#!/usr/bin/env python3

"""
TOOLS TO DIFF TWO PLANS (DISTRICT IDS BY FEATURE GEOID)
"""

from collections import defaultdict

from .types import *
from .io import *
from .helpers import *


def diff_two_plans(to_plan, from_plan) -> list[Region]:
    """
    Diff two inverted plans, a current/to plan and a from/compare plan.
    """

    features: dict[str, Feature] = from_plan.state.features
    regions: list[Region] = list()

    for from_id, from_district in from_plan.districts().items():
        from_geoids: set = from_district["geoids"]
        for to_id, to_district in to_plan.districts().items():
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


### HELPERS ###


def validate_plans(inverted_plans) -> bool:
    """
    Validate that all plans have the same number of blocks.
    """
    blocks_by_plan: list[int] = []

    for plan in inverted_plans:
        n: int = 0
        for k, v in plan.items():
            n += len(v["geoids"])
        blocks_by_plan.append(n)

    n = blocks_by_plan[0]
    all_same: bool = all(x == n for x in blocks_by_plan)

    return all_same


#
