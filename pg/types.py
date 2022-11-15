#!/usr/bin/env python3

"""
TYPES
"""

from typing import NamedTuple, TypedDict


class Region(NamedTuple):
    districts: list[int]
    geoids: set[str]
    n: int  # number of features (blocks)
    pop: int  # total population


# Modified versions of types in the 'baseline' repo


class Coordinate(NamedTuple):
    x: int
    y: int

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Feature(TypedDict):
    xy: Coordinate
    pop: int


class Ratings(TypedDict):
    proportionality: int
    competitiveness: int
    minority_opportunity: int
    compactness: int
    splitting: int


class Plan(TypedDict):
    name: str
    nickname: str
    ratings: Ratings


#
