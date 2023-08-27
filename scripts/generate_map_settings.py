#!/usr/bin/env python3
#

"""
Generate display settings for a BAF that will be imported into a DRA map.

For example:

$ scripts/generate_map_settings.py -s NC -o ~/Downloads/NC/ -a NC_2022_Congress_Official.csv -f NC_2022_Congress_Official_display_settings.json
$ scripts/generate_map_settings.py -s NC -o ~/Downloads/NC/ -a NC_2022_Congress_Official_intersections.csv -f NC_2022_Congress_Official_intersections_display_settings.json -i

For documentation, type:

$ scripts/generate_map_settings.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os
from csv import DictReader
import networkx as nx
import functools

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate display settings for a BAF that will be imported into a DRA map."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="~/Downloads/NC/",
        help="Path to output directory",
        type=str,
    )
    parser.add_argument(
        "-a",
        "--assignments",
        default="NC_2022_Congress_Official.csv",
        help="Block-assignment file",
        type=str,
    )
    parser.add_argument(
        "-f",
        "--edits",
        default="NC_2022_Congress_Official_display_settings.json",
        help="The display settings file",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--intersections",
        dest="intersections",
        action="store_true",
        help="Intersections map",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


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


def assign_district_colors(xx: str, assignments: list[dict]) -> dict[int | str, str]:
    """Assign colors to districts, based on adjacency."""

    ## First, read the block-assignment file for the map to be colored.

    district_by_block: list[dict] = assignments
    # district_by_block: list[dict] = read_csv(assignments_csv, [str, int])

    ## Then, construct a pseudo district graph, using the precinct graph.

    # Read the precinct adjacencies

    unit: str = study_unit(xx)

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
        block: str = row["GEOID"] if "GEOID" in row else row["GEOID20"]
        district: int = row["DISTRICT"] if "DISTRICT" in row else row["District"]

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
                if neighbor not in districts_by_precinct:
                    print(f"Warning: {neighbor} not in districts_by_precinct!")
                    continue

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

    district_colors: dict[int | str, str] = dict()
    for i in range(1, len(d) + 1):
        district_colors[i] = pick_color(d[i])

    return district_colors


def canonicalize_for_sorting(compound_id: str) -> str:
    """
    The DRA district id canonicalization function to match:

    // Normalize any numeric part to have four digits with padded leading zeros
    // so alphabetic sorting will result in correct numeric sort for mixed alphanumber
    // district labels.
    export function canonicalSortingDistrictID(districtID: string): string
    {
    let a = reNumeric.exec(districtID);
    if (a && a.length == 4)
    {
        let s = a[2];
        if (s.length > 0)
        {
        switch (s.length)
        {
            case 1: s = `000${s}`;  break;
            case 2: s = `00${s}`;  break;
            case 3: s = `0${s}`;  break;
        }
        a[2] = s;
        }
        districtID = `${a[1]}${a[2]}${a[3]}`;
    }
    return districtID;
    }
    """

    canonical_id: str = compound_id[0].zfill(4) + compound_id[1:]

    return canonical_id


def compare_canonical_ids(x_id: str, y_id: str) -> int:
    """Put compound district IDs in canonical DRA sort order."""

    x: str = canonicalize_for_sorting(x_id)
    y: str = canonicalize_for_sorting(y_id)

    if x < y:
        return -1
    elif y > x:
        return 1
    else:
        return 0


def generate_display_settings(ids: list, orders: list, colors: list) -> str:
    """Generate the display settings for a DRA map, given a number of districts."""

    # n: int = len(district_colors)
    meta: str = "{\n" '\t"meta": {\n' '\t\t"palette": "plasma_r"\n' "\t},\n"

    owner: str = (
        '\t"owner": {\n'
        '\t\t"UserID": "owner",\n'
        '\t\t"bShowMap": true,\n'
        '\t\t"bShowVotingDistricts": true,\n'
        '\t\t"bShowDistrictLines": false,\n'
        '\t\t"bShowNewDistrictLines": true,\n'
        '\t\t"bShowDistrictLabels": true,\n'
        '\t\t"bShowLandmarks": false\n'
        "\t}\n"
        "}"
    )

    district_header: str = (
        '\t"districtprops": [\n'
        "\t\t{\n"
        '\t\t\t"lat": 0,\n'
        '\t\t\t"lon": 0,\n'
        '\t\t\t"fontsize": -1,\n'
        '\t\t\t"label": "",\n'
        '\t\t\t"color": "",\n'
        '\t\t\t"target": 0,\n'
        '\t\t\t"order": 0\n'
        "\t\t}"
    )
    district_footer: str = "\n\t],\n"

    districts: list[str] = []
    districts.append(district_header)

    # for i, id in enumerate(district_colors):
    for id, order, color in zip(ids, orders, colors):
        # j: int = i + 1
        # color: str = district_colors[id]

        district: str = (
            "\t\t{\n"
            '\t\t\t"lat": 0,\n'
            '\t\t\t"lon": 0,\n'
            '\t\t\t"fontsize": -1,\n'
            f'\t\t\t"label": "{id}",\n'
            f'\t\t\t"color": "{color}",\n'
            '\t\t\t"target": 0,\n'
            f'\t\t\t"order": {order}\n'
            "\t\t}"
        )

        districts.append(district)

    district_props: str = ",\n".join(districts)
    district_props += district_footer

    return meta + district_props + owner


def main() -> None:
    """Generate display settings for a BAF that will be imported into a DRA map."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)
    assignments_csv: str = os.path.join(output_dir, args.assignments)
    settings_json: str = os.path.join(output_dir, args.edits)
    intersections: bool = args.intersections

    verbose: bool = args.verbose

    # Debug

    # xx = "IL"
    # output_dir: str = os.path.expanduser("~/Downloads/IL/")
    # assignments_csv: str = os.path.join(output_dir, "IL_2022_Congress_Official.csv")
    # settings_json: str = os.path.join(
    #     output_dir, "IL_2022_Congress_Official_display_settings.json"
    # )

    #

    n: int = districts_by_state[xx][plan_type.lower()]

    # Read the block-assignment file

    field_types: list = [str, str] if intersections else [str, int]
    district_by_block: list[dict] = read_csv(assignments_csv, field_types)

    assignments: list[dict] = list() if intersections else district_by_block

    # Map compound district ids to int's 1-N, so colors can be assigned

    scan_order: dict[str, int] = dict()
    reverse_scan_order: dict[int, str] = dict()
    district_ids: list[str] = list()

    if intersections:
        i: int = 1
        for row in district_by_block:
            block: str = row["GEOID"] if "GEOID" in row else row["GEOID20"]
            district: str = row["DISTRICT"] if "DISTRICT" in row else row["District"]

            if district not in scan_order:
                scan_order[district] = i
                reverse_scan_order[i] = district
                district_ids.append(district)
                i += 1

            mapped: dict = {
                "DISTRICT": scan_order[district],
                "GEOID": block,
            }
            assignments.append(mapped)

    # Assign colors to districts

    district_colors: dict[int | str, str] = assign_district_colors(xx, assignments)

    if intersections:
        temp: dict[int | str, str] = dict()
        for k, v in reverse_scan_order.items():
            temp[v] = district_colors[k]

        district_colors = temp

    # Generate display settings for a DRA map

    sort_order: list = (
        list(range(1, n + 1))
        if not intersections
        else sorted(list(district_ids), key=functools.cmp_to_key(compare_canonical_ids))
    )
    ui_order: list = (
        list(range(1, n + 1))
        if not intersections
        else [
            dict(
                zip(
                    sorted(
                        list(district_ids),
                        key=functools.cmp_to_key(compare_compound_ids),
                    ),
                    range(1, len(district_ids) + 1),
                )
            )[x]
            for x in sort_order
        ]
    )
    colors: list[str] = [district_colors[i] for i in sort_order]

    display_settings: str = generate_display_settings(sort_order, ui_order, colors)

    # Write the display settings file

    with open(settings_json, "w") as text_file:
        text_file.write(display_settings)

    pass


if __name__ == "__main__":
    main()

### END ###
