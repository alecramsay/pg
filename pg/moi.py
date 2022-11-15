#!/usr/bin/env python3

"""
POPULATION COMPACTNESS aka MOMENT OF INERTIA (MOI)
"""

import math

from .types import Coordinate, Feature
from .diff import invert_plan


def calc_moi(
    inverted_plan: dict[int, set[str]],
    centroids: dict[int, Coordinate],
    fc: dict[str, Feature],
) -> float:

    n: int = len(inverted_plan)
    moi: float = 0.0

    for district_id, geoids in inverted_plan.items():
        moi += calc_district_moi(geoids, centroids[district_id], fc)

    moi /= n

    return moi


def calc_district_moi(
    geoids: set[str], centroid: Coordinate, fc: dict[str, Feature]
) -> float:

    moi: float = 0.0
    total: int = 0

    for geoid in geoids:
        feature: Feature = fc[geoid]
        xy: Coordinate = feature.xy
        pop: int = feature.pop

        moi += pop * distance_squared(xy, centroid)
        total += pop

    moi /= total

    return moi


### HELPERS ###


def distance_squared(pt1: Coordinate, pt2: Coordinate) -> float:
    """
    Compute a *squared* distance between two points, using a Cartesian (flat earth) not
    geodesic (curved earth) model.
    """

    dx: float = pt1.x - pt2.x
    dy: float = pt1.y - pt2.y

    d: float = dx**2 + dy**2

    return d


def district_centroid(geoids: set[str], fc: dict[str, Feature]) -> Coordinate:
    xsum: float = 0
    ysum: float = 0
    total: int = 0
    for geoid in geoids:
        feature: Feature = fc[geoid]
        # pop: int = feature["pop"]
        total += feature.pop
        xsum += feature.xy.x * feature.pop
        ysum += feature.xy.y * feature.pop

    return Coordinate(xsum / total, ysum / total)


#
