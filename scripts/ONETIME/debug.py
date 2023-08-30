#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

import os
from csv import DictReader

import networkx as nx

from pg import *


xx: str = "NC"
output_dir: str = os.path.expanduser("~/Downloads/NC/")
assignments_csv: str = os.path.join(output_dir, "NC_2022_Congress_Official.csv")

###


def pick_color(id: int) -> str:
    """Translate a 1-N color index to a color hex code.

    The DRA color grid is 13 x 12 (or 12 x 12, if you skip the partial first row).
    These are 6 colors in the Plasma colormap, repeated as necessary.

    1 - #f0f823 -  1 x  1 :  0 x  1
    2 - #0f0787 - 13 x 12 : 12 x 12
    3 - #fca735 -  3 x 12 :  2 x 12
    4 - #c5407e -  8 x  1 :  7 x  1
    5 - #f48948 -  5 x  1 :  4 x  1
    6 - #8b09a5 - 10 x  6 :  9 x  6

    """

    colors: list[str] = [
        "#f0f823",
        "#0f0787",
        "#fca735",
        "#c5407e",
        "#f48948",
        "#8b09a5",
    ]
    n_colors: int = len(colors)

    color: str = colors[(id - 1) % n_colors]

    return color


### ASSIGN DISTRICT COLORS, BASED ON ADJACENCY ###

## First, read the block-assignment file for the map to be colored.

district_by_block: list[dict] = read_csv(assignments_csv, [str, int])

## Then, construct a pseudo district graph, using the precinct graph.

# Read the precinct adjacencies

unit: str = "vtd"  # Extend for BG's

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

# Invert the districts by *precinct* and
# Create a precinct-to-districts mapping

precincts_by_district: dict[int, set[str]] = dict()
districts_by_precinct: dict[str, set[int]] = dict()

for row in district_by_block:
    block: str = row["GEOID20"]
    district: int = row["District"]

    precinct: str = precinct_by_block[block]

    if district not in precincts_by_district:
        precincts_by_district[district] = set()

    if precinct not in districts_by_precinct:
        districts_by_precinct[precinct] = set()

    precincts_by_district[district].add(precinct)
    districts_by_precinct[precinct].add(district)

# Construct an approximate district graph

district_graph: dict[int, set[int]] = dict()

for district in precincts_by_district:
    district_graph[district] = set()

    for precinct in precincts_by_district[district]:
        for neighbor in precinct_graph[precinct]:
            neighbor_districts: set[int] = districts_by_precinct[neighbor]

            for neighbor_district in neighbor_districts:
                if (
                    neighbor_district != district
                    and neighbor_district not in district_graph[district]
                ):
                    district_graph[district].add(neighbor_district)

## Convert the district graph to a networkx graph & assign colors to the districts

G: nx.Graph = nx.Graph()
elist: list[tuple[int, int]] = [
    (x, y) for x in district_graph for y in district_graph[x]
]
G.add_edges_from(elist)

d: dict[int, int] = nx.coloring.greedy_color(G)
# d = nx.coloring.greedy_color(G, strategy="largest_first")

district_colors: dict[int, str] = {k: pick_color(v) for k, v in d.items()}

pass
