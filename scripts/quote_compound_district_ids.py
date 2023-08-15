#!/usr/bin/env python3
#

"""
Quote fields in a CSV file.

For example:

$ scripts/quote_compound_district_ids.py -f ~/Downloads/sample.csv

For documentation, type:

$ scripts/quote_compound_district_ids.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Quote fields in a CSV file."
    )

    parser.add_argument(
        "-f",
        "--file",
        default="~/Downloads/NC/NC_2022_Congress_Official_intersections.csv",
        help="Path to file to quote in place",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Quote fields in a CSV file in place."""

    args: Namespace = parse_args()

    file_path: str = os.path.expanduser(args.file)

    verbose: bool = args.verbose

    #

    quoted_lines: list[str] = list()

    with open(file_path, "r") as f:
        line: str = f.readline()
        while line:
            fields: list[str] = line.strip().split(",")
            if fields[0][0] == "\ufeff":
                fields[0] = fields[0][1:]

            geoid: str = fields[0]
            district: str = '"' + fields[1] + '"'

            quoted_line: str = geoid + "," + district + "\n"

            # print(quoted_line)
            quoted_lines.append(quoted_line)
            line = f.readline()

    with open(file_path, "w") as f:
        for line in quoted_lines:
            f.write(line)


if __name__ == "__main__":
    main()

### END ###
