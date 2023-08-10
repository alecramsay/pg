#!/usr/bin/env python3
#

"""
Generate display settings for a BAF that will be imported into a DRA map.

For example:

$ scripts/generate_map_settings.py -s NC -a ~/Downloads/NC/NC_2022_Congress_Official.csv -f ~/Downloads/NC/NC_2022_Congress_Official_display_settings.json

For documentation, type:

$ scripts/generate_map_settings.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

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
        "-a",
        "--assignments",
        default="~/Downloads/NC/NC_2022_Congress_Official.csv",
        help="Block-assignment file",
        type=str,
    )
    parser.add_argument(
        "-f",
        "--edits",
        default="~/Downloads/NC/NC_2022_Congress_Official_display_settings.json",
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
    assignments_csv: str = os.path.expanduser(args.assignments)
    settings_json: str = os.path.expanduser(args.edits)

    verbose: bool = args.verbose

    #

    # TODO - Assign better district colors (#49).

    n: int = districts_by_state[xx][plan_type.lower()]
    display_settings: str = generate_display_settings(n)

    with open(settings_json, "w") as text_file:
        text_file.write(display_settings)

    pass


if __name__ == "__main__":
    main()

### END ###
