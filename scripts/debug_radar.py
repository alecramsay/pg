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
    [xx, yyyy, plan_type, current_subtype, "ratings"], "_", "json"
)
compare_path: str = path_to_file([temp_dir]) + file_name(
    [xx, yyyy, plan_type, compare_subtype, "ratings"], "_", "json"
)

plot_path: str = path_to_file([assets_dir]) + file_name(
    [xx, yyyy, plan_type, current_subtype, "radar"], "_", "png"
)


### LOAD RATINGS ###


current_ratings: Ratings = cull_ratings(load_json(current_path))
compare_ratings: Ratings = cull_ratings(load_json(compare_path))


### PLOT RADAR DIAGRAM ###

current_name: str = f"{xx} {yyyy} {type} {current_subtype}"
compare_name: str = f"{xx} {yyyy} {type} {compare_subtype}"

current_plan: Plan = Plan()
current_plan.name = current_name
current_plan.nickname = current_subtype
current_plan.ratings = current_ratings

compare_plan: Plan = Plan()
compare_plan.name = compare_name
compare_plan.nickname = compare_subtype
compare_plan.ratings = compare_ratings

plot_radar_diagram(current_plan, compare_plan, plot_path)

pass
