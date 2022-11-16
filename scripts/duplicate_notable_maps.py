#!/usr/bin/env python3

"""
Duplicate Notable maps.

For example:

$ scripts/duplicate_notable_maps.py

For documentation, type:

$ scripts/duplicate_notable_maps.py -h

"""

import os

from pg import *

group: str = "Notable"
label: str = "PG-" + group.upper()


def make_command(group: str, label: str, xx: str, id: str) -> str:
    # scripts/duplicate_map.sh NC Congress 2022 Proportional PG-NOTABLE 7cfcec86-b8bf-41fa-a6c2-0be9b3799747
    return f"scripts/duplicate_map.sh {xx} {plan_type} {yyyy} {group} {label} {id}"


for xx, maps in notable_maps.items():
    for dim, id in maps.items():
        os.system(make_command(dim.capitalize(), label, xx, id))
        pass

#
