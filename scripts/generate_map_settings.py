#!/usr/bin/env python3
#

"""
Generate display settings for a BAF that will be imported into a DRA map.

For example:

$ scripts/generate_map_settings.py -s NC -o ~/Downloads/NC/ -a NC_2022_Congress_Official.csv -f NC_2022_Congress_Official_display_settings.json

For documentation, type:

$ scripts/generate_map_settings.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os
from csv import DictReader

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
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def color_district(id: int) -> str:
    """Translate a 1-N district id to a color hex code.

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


def generate_display_settings(n: int) -> str:
    """Generate the display settings for a DRA map, given a number of districts."""

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

    for id in range(1, n + 1):
        color: str = color_district(id)

        district: str = (
            "\t\t{\n"
            '\t\t\t"lat": 0,\n'
            '\t\t\t"lon": 0,\n'
            '\t\t\t"fontsize": -1,\n'
            f'\t\t\t"label": "{id}",\n'
            f'\t\t\t"color": "{color}",\n'
            '\t\t\t"target": 0,\n'
            f'\t\t\t"order": {id}\n'
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

    verbose: bool = args.verbose

    # TODO - HACK the district colors

    n: int = districts_by_state[xx][plan_type.lower()]
    display_settings: str = generate_display_settings(n)

    # TODO - Assign better district colors (#49).

    ## Read the precinct adjacencies & convert them a graph
    adjacencies_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "vtd", "adjacencies"], "_", "csv"
    )
    vtd_adjacencies: list[dict] = list()
    fieldnames: list[str] = ["one", "two"]
    with open(adjacencies_csv, "r", encoding="utf-8-sig") as file:
        reader: DictReader[str] = DictReader(
            file, fieldnames=fieldnames, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            vtd_adjacencies.append(row)

    vtd_graph: dict[str, list[str]] = dict()
    for row in vtd_adjacencies:
        if row["one"] not in vtd_graph:
            vtd_graph[row["one"]] = []
        if row["two"] not in vtd_graph:
            vtd_graph[row["two"]] = []
        vtd_graph[row["one"]].append(row["two"])
        vtd_graph[row["two"]].append(row["one"])

    ## Read the block-to-vtd mapping
    types: list = [str, str]
    block_vtd_csv: str = path_to_file([preprocessed_data_dir, xx]) + file_name(
        [xx, cycle, "block", "vtd"], "_", "csv"
    )
    block_vtd: list[dict] = read_csv(block_vtd_csv, types)

    ## Condense block assignments to non-unique precinct assignments

    ## Invert precincts by district

    ## Construct a pseudo district graph

    # Write the display settings file

    with open(settings_json, "w") as text_file:
        text_file.write(display_settings)

    pass


if __name__ == "__main__":
    main()

### END ###
