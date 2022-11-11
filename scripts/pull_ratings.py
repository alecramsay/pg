#!/usr/bin/env python3

"""
Pull ratings for Official & Notable maps.

For example:

$ scripts/pull_ratings.py

For documentation, type:

$ scripts/gen_pull_ratings.py -h

"""

import os

from pg import *


def make_command(xx: str, subtype: str, id: str) -> str:
    return f"scripts/pull_map_ratings.sh {xx} Congress {subtype} {id}"


for xx, id in officials_copy.items():
    os.system(make_command(xx, "Official", id))

for xx, maps in notables_copy.items():
    for dim, id in maps.items():
        os.system(make_command(xx, dim.capitalize(), id))

#
