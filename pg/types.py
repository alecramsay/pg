#!/usr/bin/env python3

"""
TYPES
"""

from typing import NamedTuple, TypedDict


### TUPLES -- IMMUTABLE ###


class Coordinate(NamedTuple):
    x: int
    y: int

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Feature(NamedTuple):
    xy: Coordinate
    pop: int

    def __repr__(self) -> str:
        return f"xy={self.xy}, pop={self.pop}"


class Ratings(NamedTuple):
    proportionality: int
    competitiveness: int
    minority_opportunity: int
    compactness: int
    splitting: int

    def __repr__(self) -> str:
        return f"[{self.proportionality}, {self.competitiveness}, {self.minority_opportunity}, {self.compactness}, {self.splitting}]"


class Region(NamedTuple):
    districts: list[int]
    geoids: set[str]
    n: int  # number of features (blocks)
    pop: int  # total population


### DICTIONARIES -- MUTABLE ###


### TODO - LEGACY ###


class SimplePlan(TypedDict):
    name: str
    nickname: str
    ratings: Ratings


#
