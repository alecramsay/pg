#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

from pg import *

xx: str = "NC"
n: int = districts_by_state[xx][plan_type.lower()]
cycle: str = "2020"

current_subtype: str = "Official"
compare_subtype: str = "Baseline"


### CONSTRUCT FILE NAMES ###

current_path: str = path_to_file([temp_dir]) + file_name(
    [xx + yy, plan_type, current_subtype], "_", "json"
)
compare_path: str = path_to_file([temp_dir]) + file_name(
    [xx + yy, plan_type, compare_subtype], "_", "json"
)

plot_path: str = path_to_file([content_dir]) + file_name(
    [xx, yy, plan_type, current_subtype, "radar"], "_", "png"
)


### LOAD RATINGS ###


current_ratings: Ratings = cull_ratings(load_json(current_path))
compare_ratings: Ratings = cull_ratings(load_json(compare_path))


### PLOT RADAR DIAGRAM ###

current_name: str = f"{xx}{yy} {type} {current_subtype}"
compare_name: str = f"{xx}{yy} {type} {compare_subtype}"

current_plan: SimplePlan = {
    "name": current_name,
    "nickname": current_subtype,
    "ratings": current_ratings,
}
compare_plan: SimplePlan = {
    "name": compare_name,
    "nickname": compare_subtype,
    "ratings": compare_ratings,
}


plot_radar_diagram(current_plan, compare_plan, plot_path)

pass
