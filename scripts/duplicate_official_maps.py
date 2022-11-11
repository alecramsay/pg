#!/usr/bin/env python3

"""
Duplicate Official maps.

For example:

$ scripts/duplicate_official_maps.py

For documentation, type:

$ scripts/duplicate_official_maps.py -h

"""

import os

from pg import *

yyyy: str = 2022
plan_type: str = "Congress"
group: str = "Official"
label: str = "PG-" + group.upper()


def make_command(group: str, label: str, xx: str, id: str) -> str:
    # scripts/duplicate_map.sh NC Congress 2022 Official PG-OFFICIAL c62fa27b-1f4b-40ba-bcd7-9e2ca6f9df87
    return f"scripts/duplicate_map.sh {xx} {plan_type} {yyyy} {group} {label} {id}"


for xx, id in officials_copy.items():
    os.system(make_command(group, label, xx, id))
    pass

#
