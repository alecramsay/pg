#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

import os
from csv import DictReader

from pg import *


xx: str = "NC"
output_dir: str = os.path.expanduser("~/Downloads/NC/")
assignments_csv: str = os.path.join(output_dir, "NC_2022_Congress_Official.csv")

### ASSIGN DISTRICT COLORS, BASED ON ADJACENCY ###

## First, read the block-assignment file for the map to be colored.

district_by_block: list[dict] = read_csv(assignments_csv, [str, int])

## Then, construct a pseudo district graph, using the precinct graph.

# Read the precinct adjacencies

unit: str = "vtd"  # TODO: extend for BG's

adjacencies_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
    [xx, cycle, unit, "adjacencies"], "_", "csv"
)

precinct_adjacencies: list[dict] = list()
fieldnames: list[str] = ["one", "two"]
with open(adjacencies_csv, "r", encoding="utf-8-sig") as file:
    reader: DictReader = DictReader(
        file, fieldnames=fieldnames, restkey=None, restval=None, dialect="excel"
    )
    for row in reader:
        precinct_adjacencies.append(row)

# Convert the adjacency pairs to a graph

precinct_graph: dict[str, list[str]] = dict()
for row in precinct_adjacencies:
    if row["one"] not in precinct_graph:
        precinct_graph[row["one"]] = []
    if row["two"] not in precinct_graph:
        precinct_graph[row["two"]] = []
    precinct_graph[row["one"]].append(row["two"])
    precinct_graph[row["two"]].append(row["one"])

# Read the block-to-precinct mapping

types: list = [str, str]
block_precinct_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
    [xx, cycle, "block", unit], "_", "csv"
)
block_precinct: list[dict] = read_csv(block_precinct_csv, types)
precinct_by_block: dict[str, str] = {
    row["BLOCK"]: row["PRECINCT"] for row in block_precinct
}

# Condense unique block assignments to non-unique precinct assignments

district_by_precinct: dict[str, set[int]] = dict()

for row in district_by_block:
    block: str = row["GEOID20"]
    district: int = row["District"]

    precinct: str = precinct_by_block[block]

    if precinct not in district_by_precinct:
        district_by_precinct[precinct] = set()

    district_by_precinct[precinct].add(district)


# Invert precincts by district, handling split precincts

precinct_by_district: dict[int, set[str]] = dict()

for precinct in district_by_precinct:
    for district in district_by_precinct[precinct]:
        if district not in precinct_by_district:
            precinct_by_district[district] = set()
        precinct_by_district[district].add(precinct)

# Construct a pseudo district graph

district_graph: dict[str, list[str]] = dict()

# For each precinct in a district
# - Find the neighboring precincts
# - Find the districts of all the neighboring precincts
# - ...
# Handle split precincts case

pass
