#!/usr/bin/env python3

"""
Analyze the Official & Notable maps for a state vs. the Baseline map

For example:

$ scripts/analyze_state.py NC

For documentation, type:

$ scripts/analyze_state.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace
import os

from pg import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(
    description="Analyze the Official & Notable maps for a state vs. the Baseline map"
)

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)
parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args: Namespace = parser.parse_args()

xx: str = args.state
plan_type: str = "Congress"


### PULL THE BASELINE RATINGS ###

print()
print("Pulling ratings for baseline map...")
based_id: str = baseline_maps[xx]
os.system(f"scripts/pull_map_ratings.sh {xx} {plan_type} Baseline {based_id}")


### PLOT PAIRWISE RADAR DIAGRAMS ###

for label in [
    "Official",
    "Proportional",
    "Competitive",
    "Minority",
    "Compact",
    "Splitting",
]:
    print("Plotting radar diagram for", label, "map...")
    os.system(f"scripts/plot_radar_diagram.py {xx} {label} Baseline")

print("Done.")

pass
