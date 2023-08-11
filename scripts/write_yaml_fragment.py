#!/usr/bin/env python3

"""
Generate a YAML fragment from the map guids JSON file.

For example:

$ scripts/write_yaml_fragment.py
$ scripts/write_yaml_fragment.py -s NC -o ~/Downloads/

For documentation, type:

$ scripts/write_yaml_fragment.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
from datetime import datetime

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate a YAML fragment from the map guids JSON file."
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
        default="~/Downloads/",
        help="Path to output directory",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Generate a YAML fragment from the map guids JSON file."""

    args: Namespace = parse_args()

    xx: str = args.state
    output: str = os.path.expanduser(args.output)

    verbose: bool = args.verbose

    #

    output_root: str = FileSpec(output).abs_path
    output_dir: str = os.path.join(output_root, xx)

    guids_json: str = f"{xx}_{yyyy}_{plan_type}_map_guids.json"
    guids_path: str = os.path.join(output_dir, guids_json)
    guids: dict[str, Any] = read_json(guids_path)

    # Translate the JSON into YAML

    guids_yaml: str = f"{xx}_{yyyy}_{plan_type}_map_guids.yaml"
    yaml_path: str = os.path.join(output_dir, guids_yaml)

    lines: list[str] = []
    lines.append("{:# Generated at %m/%d/%Y @ %H:%M}".format(datetime.now()))
    lines.append(f"- xx: {xx}")
    lines.append(f"  name: {STATE_NAMES[xx]}")
    lines.append(f"  official: {guids['official']}")
    for label in ["Proportional", "Competitive", "Minority", "Compact", "Splitting"]:
        if label.lower() in guids:
            lines.append(f"  {label.lower()}: {guids[label.lower()]}")
        else:
            lines.append(f"  {label.lower()}: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
    lines.append(f"  baseline: {guids['baseline']}")
    lines.append(f"  official-intersections: {guids['official-intersections']}")
    for label in ["Proportional", "Competitive", "Minority", "Compact", "Splitting"]:
        if label.lower() in guids:
            lines.append(
                f"  {label.lower()}-intersections: {guids[label.lower()]}-intersections"
            )
        else:
            lines.append(f"  {label.lower()}: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
    lines.append(f"  ready: true")

    with open(yaml_path, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()

### END ###
