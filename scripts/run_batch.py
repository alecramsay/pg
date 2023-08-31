#!/usr/bin/env python3
"""
Run a batch of commands.

For example:

$ scripts/run_batch.py

"""

import os

# from baseline import *

states: list[str] = ["MD", "PA", "VA", "AZ", "CO"]

for xx in sorted(states):
    command: str = ""

    # command = f"scripts/update/district_colors.py -s {xx} -i"
    # command = f"scripts/update/map_settings.py -s {xx} -i"
    # command = f"scripts/update/screenshots.py -s {xx} -i"
    # command = f"scripts/BACKUP.py -s {xx}"
    # NOTE - Hand deploy the updated files!

    print(command)
    os.system(command)

pass
