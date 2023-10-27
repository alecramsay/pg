#!/usr/bin/env python3

"""
Generate a state summaries.

For example:

$ scripts/generate_summaries.py

NOTE - Create an _includes directory in ~/Downloads, before running this.

"""

import os

from pg import *

states: list[str] = [
    xx
    for xx in sorted(study_states)  # if xx not in ["NC", "MD", "PA", "VA", "AZ", "CO"]
]

for xx in sorted(states):
    command: str = f"{xx}"
    command = f"scripts/generate_summary.py -s {xx}"

    print(command)
    os.system(command)

pass
