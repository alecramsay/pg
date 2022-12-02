#!/usr/bin/env python3
#

"""
HOW MANY UNIQUE NOTABLE MAPS WERE THERE?

# of states: 37
# of states with unique notables: 26 (70.27%)
# of unique notables: 171 (92.43%)

"""

from pg import *

n: int = len(notable_maps)
k: int = 0  # number of states with unique notables
total: int = 0  # number of unique notables overall

for xx, maps in notable_maps.items():
    list_set: set = set(maps.values())
    notables: int = len(list(list_set))

    total += notables
    if notables == 5:
        k += 1

print()
print(f"# of states: {n}")
print(f"# of states with unique notables: {k} ({k/n:.2%})")
print(f"# of unique notables: {total} ({total/(n * 5):.2%})")
print()

pass
