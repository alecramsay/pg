#!/usr/bin/env python3

"""
TYPES
"""

from typing import NamedTuple, TypedDict


### TUPLES -- IMMUTABLE ###


class Coordinate(NamedTuple):
    x: float
    y: float

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Feature(NamedTuple):
    xy: Coordinate
    pop: int

    def __repr__(self) -> str:
        return f"xy={self.xy}, pop={self.pop}"


class Assignment(NamedTuple):
    geoid: str
    district: int

    def __repr__(self) -> str:
        return f"{self.geoid} => {self.district}"


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


class District(TypedDict):
    geoids: set[str]
    xy: Coordinate
    pop: int


# DON'T LIMIT WHAT GETS EXPORTED.

### END ###
