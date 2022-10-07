#!/usr/bin/env python3

"""
TYPES
"""

from collections import namedtuple


Area = namedtuple("Area", ["districts", "geoids"])
# districts is a list of district numbers
# geoids is a set of geoids

AreaExtended = namedtuple(
    "AreaExtended", ["districts", "geoids", "blocks", "population"]
)
