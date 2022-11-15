#!/usr/bin/env python3

"""
Plot radar diagram comparing two maps

For example:

$ scripts/plot_radar_diagram.py NC Official Baseline
$ scripts/plot_radar_diagram.py NC Proportional Baseline

For documentation, type:

$ scripts/plot_radar_diagram.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

# TODO - DELETE
# import chart_studio.plotly as py
# import plotly.graph_objs as go  # https://plotly.com/python-api-reference/plotly.graph_objects.html
# from typing import TypedDict

from pg import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(
    description="Plot a radar diagram comparing two maps"
)

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)
parser.add_argument("current", help="The current (top) map", type=str)
parser.add_argument("compare", help="The compare (bottom) map", type=str)

parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args: Namespace = parser.parse_args()

xx: str = args.state
current_subtype: str = args.current
compare_subtype: str = args.compare


### CONSTRUCT FILE NAMES ###

current_path: str = path_to_file([temp_dir]) + file_name(
    [xx + yy, type, current_subtype], "_", "json"
)
compare_path: str = path_to_file([temp_dir]) + file_name(
    [xx + yy, type, compare_subtype], "_", "json"
)

plot_path: str = path_to_file([content_dir]) + file_name(
    [xx, yy, type, current_subtype, "radar"], "_", "png"
)


### LOAD RATINGS ###


current_ratings: Ratings = cull_ratings(load_json(current_path))
compare_ratings: Ratings = cull_ratings(load_json(compare_path))


### PLOT RADAR DIAGRAM ###

current_name: str = f"{xx}{yy} {type} {current_subtype}"
compare_name: str = f"{xx}{yy} {type} {compare_subtype}"

current_plan: Plan = {
    "name": current_name,
    "nickname": current_subtype,
    "ratings": current_ratings,
}
compare_plan: Plan = {
    "name": compare_name,
    "nickname": compare_subtype,
    "ratings": compare_ratings,
}


plot_radar_diagram(current_plan, compare_plan, plot_path)

pass
