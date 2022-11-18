#!/usr/bin/env python3

"""
Print all Notable map ratings

For example:

$ scripts/print_ratings.py

For documentation, type:

$ scripts/print_ratings.py -h

"""

from pg import *


print("Map,Plan,Proportional,Competitive,Minority,Compact,Splitting")
for xx, maps in notable_maps.items():
    for dim, id in maps.items():
        ratings: Ratings = cull_ratings(
            load_json(
                path_to_file([data_dir, xx])
                + file_name(
                    [xx, yyyy, plan_type, dim.capitalize(), "ratings"], "_", "json"
                )
            )
        )
        print(
            f"{xx},{qualify_label(dim.capitalize())},{ratings.proportionality},{ratings.competitiveness},{ratings.minority_opportunity},{ratings.compactness},{ratings.splitting}"
        )

pass
