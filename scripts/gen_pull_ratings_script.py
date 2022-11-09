#!/usr/bin/env python3
#
# Generate a script to pull ratings for official, notable, and baseline maps.
#
# For example:
#
# $ scripts/gen_pull_ratings_script.py
# $ scripts/gen_pull_ratings_script.py > ~/Downloads/pull_ratings.sh
#

import json

from pg import *


def print_command(xx: str, subtype: str, id: str):
    print(f"scripts/pull_map_ratings.sh {xx} Congress {subtype} {id}")


for xx, id in officials_copy.items():
    print_command(xx, "Official", id)

for xx, maps in notables_copy.items():
    for dim, id in maps.items():
        print_command(xx, dim.capitalize(), id)

for xx, id in baseline_maps.items():
    print_command(xx, "Baseline", id)
