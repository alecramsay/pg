#!/usr/bin/env python3

"""
Duplicate Official & Notable maps.

For example:

$ scripts/duplicate_maps.py

For documentation, type:

$ scripts/duplicate_maps.py -h

"""

import os

from pg import *

yyyy: str = 2022
plan_type: str = "Congress"
units: str = "blocks"


def make_command(group: str, label: str, xx: str, id: str) -> str:
    name: str = (
        '"'
        + (
            f"{xx} {yyyy} {plan_type} ({label})"
            if len(label) > 0
            else f"{xx} {yyyy} {plan_type} ({group})"
        )
        + '"'
    )
    description: str = (
        '"'
        + (f"{group}/{label}/{units}" if len(label) > 0 else f"{group}/{units}")
        + '"'
    )
    return f"echo scripts/dupmap.js -i {id} -u alec@davesredistricting.org -N {name} -D {description} -L PG-{group}"


for xx, id in officials_copy.items():
    os.system(make_command("Official", "", xx, id))

for xx, maps in notables_copy.items():
    for dim, id in maps.items():
        os.system(make_command("Notables", dim.capitalize(), xx, id))

#
