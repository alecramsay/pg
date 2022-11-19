#!/usr/bin/env python3

"""
Replace problematic Notable maps with new versions.

For example:

$ scripts/replace_maps.py

For documentation, type:

$ scripts/replace_maps.py -h

"""

import os

from pg import *

"""
Notable Maps search:

state:xx and
districts:# and
cycle:2020 and
planType:congress
(complete: true and contiguous: true and freeofholes: true and equalpopulation: true) and
(proportionality: >= 20 and competitiveness: >= 10 and compactness: >= 20 and splitting: >= 20)
"""

replacement_maps: dict[str, dict] = {
    "CO": {
        "compact": "e9e9c486-bb80-4ce5-9666-4466947f7ab0",  # copy of "7d34443b-3e8c-4108-9074-2e565805b89d"
        #       "compact": "5970deaa-8306-4728-8933-3a74d1f2f298",
        "splitting": "d639dbaf-cf30-4998-b794-7cfba3312a0b",  # copy of "fe586498-24d8-4c7c-a6db-8437ed0b9ca6"
        #       "splitting": "896e564c-ddfa-4596-9c3d-a6dbd9b6e886",
    },
    "KS": {
        "proportional": "177278c7-822b-414c-a6e4-47c49e6d8e31",  # copy of "5e0fe356-4f7f-49eb-b36b-693b1a156845"
        #       "proportional": "659e9adf-713c-4375-9528-f384d043f1b0",
        "competitive": "cadda27c-9616-45b6-a872-2d5a6e60c6a1",  # copy of dfabfef9-429c-4b81-a893-da79e7e26214
        #       "competitive": "e2021c4b-281c-451a-ad9e-49fef9c2f57b",
    },
    "MO": {
        "competitive": "f07502f1-f94d-47c6-b083-f41aadb0f7ee",  # copy of "127dfd4d-094a-4cdc-ac9e-e98829a664dc"
        #       "competitive": "a110a70b-d083-4934-905c-2ba0dae7256f",
    },
    "OK": {
        "competitive": "ca3b3e26-9a73-422f-a40c-cd7b240e053d",  # copy of "2de2dd82-508d-4c6d-a626-b41373f1a9b7"
        #       "competitive": "b8794457-352e-4412-9908-027f95cc9b1d",
        "compact": "fbec07f7-2c67-4928-aedc-956f551aee08",  # copy of "10e4bc47-38a4-4b0d-9329-81b40bc039f4"
        #       "compact": "5d052539-7560-4200-9e96-c920cda86b4f",
    },
    "AZ": {
        "splitting": "7ff7eec5-1b01-422b-bb34-d78da0f8fcb8",  # copy of "2dff53e3-4c0a-499b-b3c9-26e409318e83"
        #       "splitting": "01aecc9a-2a4b-4d43-9ca7-96385c0d1daa",
    },
    "NM": {
        "proportional": "2051bf23-0195-4d89-aceb-252d78c32dc4",  # copy of "3cab7943-cc5d-4c56-a460-307ca987324a"
        #       "proportional": "1739a3fd-0a61-40b4-affe-2d9943568477",
        "competitive": "57893e66-fd7d-464a-8e6f-c39b69609b73",  # copy of "0852f3ca-438e-43be-858c-72e6fd797f98"
        #       "competitive": "2e487b62-e26b-4c96-92de-0ffd20feade6",
        "minority": "46afff6c-1f2c-43bb-bfeb-1c69f75fa403",  # copy of "3cab7943-cc5d-4c56-a460-307ca987324a"
        #       "minority": "5dcbf4ee-ad06-4fb2-9d30-45b7b1496a3f",
        "compact": "769b245f-4c5d-4a93-98a5-6cd2e66420a2",  # copy of "e7ac5c2a-ce36-4780-ab04-0fc82faac874"
        #       "compact": "a569b54b-eebb-42c7-af2a-373d13142d05",
    },
}


def make_command(xx: str, subtype: str, id: str) -> str:
    return f"scripts/pull_map_ratings.sh {xx} Congress {subtype} {id}"


for xx, maps in replacement_maps.items():
    for dim, id in maps.items():
        print(f"Pulling ratings for {xx} Notable {dim.capitalize()} map ...")
        os.system(make_command(xx, dim.capitalize(), id))

#
