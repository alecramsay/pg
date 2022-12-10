#!/usr/bin/env python3

"""
POPULATION COMPACTNESS aka MOMENT OF INERTIA (MOI)
"""

from .pgtypes import Coordinate, Feature


def calc_moi(
    geoids: set[str], centroid: Coordinate, features: dict[str, Feature]
) -> float:

    moi: float = 0.0
    total: int = 0

    for geoid in geoids:
        feature: Feature = features[geoid]
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


# LIMIT WHAT GETS EXPORTED.


__all__: list[str] = ["calc_moi"]
