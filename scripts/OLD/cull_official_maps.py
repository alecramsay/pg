#!/usr/bin/env python3

"""
Extract ids for official congressional maps with 3 or more districts,
from state_plans.json.
"""


from pg import *

states: dict[str, Any] = read_json(
    path_to_file([data_dir]) + file_name(["state", "plans"], "_", "json")
)

official: list = list()
for state, data in states.items():
    for plan in data["plans"]:
        if (
            plan["year"] == 2022
            and plan["planType"] == "congress"
            and plan["nDistricts"] >= 2
        ):
            official.append([state, "congress", plan["id"]])
            x: str = '"{}": "{}"'.format(state, plan["id"])
            print(x, ",")

pass
