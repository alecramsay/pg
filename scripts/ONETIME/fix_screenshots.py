#!/usr/bin/env python3
"""
Retake some screenshots that were bad.

For example:

$ scripts/fix_screenshots.py

"""

import os

from pg import *

maps: list[dict[str, str]] = [
    {"xx": "AR", "label": "Official_intersections"},
    {"xx": "IA", "label": "Proportional"},
    {"xx": "KY", "label": "Official"},
    {"xx": "LA", "label": "Minority"},
    {"xx": "MA", "label": "Official"},
    {"xx": "MS", "label": "Compact"},
    {"xx": "NJ", "label": "Official_intersections"},
    {"xx": "NM", "label": "Minority"},
    {"xx": "WA", "label": "Proportional_intersections"},
    {"xx": "WA", "label": "Competitive"},
    {"xx": "WA", "label": "Competitive_intersections"},
    {"xx": "CT", "label": "Compact"},
    {"xx": "IL", "label": "Minority"},
    {"xx": "KS", "label": "Proportional"},
    {"xx": "NY", "label": "Compact"},
    {"xx": "NY", "label": "Splitting_intersections"},
    {"xx": "UT", "label": "Official"},
    {"xx": "UT", "label": "Compact_intersections"},
    {"xx": "WI", "label": "Official_intersections"},
]

for m in maps:
    xx: str = m["xx"]
    label: str = m["label"]

    backup_dir: str = os.path.expanduser("~/local/pg-backup")
    guids_dir: str = os.path.join(backup_dir, xx)
    guids_json: str = f"{xx}_{yyyy}_{plan_type}_map_guids.json"
    guids_path: str = os.path.join(guids_dir, guids_json)
    guids: dict[str, Any] = read_json(guids_path)

    guid: str = guids[label.lower().replace("_", "-")]

    command: str = (
        f"scripts/save_map_image.py -s {xx} -l {label} -i {guid} -o ~/Downloads/"
    )
    print(command)
    os.system(command)

pass
