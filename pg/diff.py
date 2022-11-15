#!/usr/bin/env python3

"""
TOOLS TO DIFF TWO PLANS (DISTRICT IDS BY FEATURE GEOID)
"""

from collections import defaultdict

from .types import *
from .io import *
from .helpers import *


def from_baf(rel_path) -> list:
    """
    Read a plan from a block-assignment file (BAF).
    Return a list of dicts with keys "GEOID20" (str) and "District" (int).
    """

    types: list = [str, int]
    districts_by_geoid: list[dict[str, int]] = read_typed_csv(rel_path, types)

    return districts_by_geoid


def rehydrate_features(rel_path, id="GEOID") -> dict[str, Feature]:
    """
    Re-hydrate a dict of Features serialized to a CSV.
    """
    features: defaultdict[str, Feature] = defaultdict(Feature)

    types: list = [str, int, float, float]
    rows: list[dict[str, int, float, float]] = read_typed_csv(rel_path, types)

    for row in rows:
        geoid: str = row[id]
        pop: int = row["POP"]
        x: float = row["X"]
        y: float = row["Y"]

        feature: Feature = {"xy": Coordinate(x, y), "pop": pop}
        features[geoid] = feature

    return features


def is_water_only(geoid) -> bool:
    """
    Return True if the block geoid has a water-only signature, False otherwise.
    """
    return geoid[5:7] == "99"


# TODO - Move this to a Plan class
def invert_plan(plan) -> dict:
    """
    Invert a plan by GEOID to sets of GEOIDs by District ID.
    """

    inverted: defaultdict[int, set] = defaultdict(set)

    for row in plan:  # type: dict[str, int]
        geoid: str = row["GEOID20"]
        if is_water_only(geoid):
            continue

        # HACK: These two unpopulated blocks are missing from the NY Most Compact plan.
        if geoid in ["360610001001001", "360610001001000"]:
            continue

        district: int = row["District"]
        # if district not in inverted:
        #     inverted[district] = set()

        inverted[district].add(geoid)

    return inverted


def validate_plans(inverted_plans) -> bool:
    """
    Validate that all plans have the same number of blocks.
    """
    blocks_by_plan: list[int] = []

    for plan in inverted_plans:
        n: int = 0
        for k, v in plan.items():
            n += len(v)
        blocks_by_plan.append(n)

    n = blocks_by_plan[0]
    all_same: bool = all(x == n for x in blocks_by_plan)

    return all_same


def diff_two_plans(to_plan, from_plan, features) -> list[Region]:
    """
    Diff two inverted plans, a current/to plan and a from/compare plan.
    """

    regions: list[Region] = list()

    for from_district, from_geoids in from_plan.items():
        for to_district, to_geoids in to_plan.items():
            intersection: set[str] = from_geoids.intersection(to_geoids)
            if intersection:
                districts: list[int] = [from_district, to_district]
                n: int = len(intersection)
                pop: int = 0
                for geoid in intersection:
                    n += 1
                    pop += features[geoid]["pop"]
                region: Region = {
                    "districts": districts,
                    "geoids": intersection,
                    "n": n,
                    "pop": pop,
                }
                regions.append(region)

    regions.sort(key=lambda region: region["pop"], reverse=True)

    return regions


#
