#!/usr/bin/env python3

"""
TYPES
"""

from collections import namedtuple
from typing import NamedTuple, TypedDict


Region: NamedTuple = namedtuple("Region", ["districts", "geoids", "blocks", "pop"])
"""
* districts is a list of district numbers
* geoids is a set of geoids
* blocks is # of blocks
* pop is # of people 
"""

#
