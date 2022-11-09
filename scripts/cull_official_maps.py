#!/usr/bin/env python3
#
# Extract ids for official congressional maps with 3 or more districts,
# from state_plans.json.
#

import json

from pg import *

states: dict[str, Any] = load_json("data/state_plans.json")

official: list = list()
for state, data in states.items():
    for plan in data["plans"]:
        if (
            plan["year"] == 2022
            and plan["planType"] == "congress"
            and plan["nDistricts"] > 2
        ):
            official.append([state, "congress", plan["id"]])
            x: str = '"{}": "{}"'.format(state, plan["id"])
            print(x, ",")

pass
