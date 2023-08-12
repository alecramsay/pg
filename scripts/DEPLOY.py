#!/usr/bin/env python3

"""
Deploy a state's artifacts to the website.

For example:

$ scripts/DEPLOY.py -s NC

For documentation, type:

$ scripts/DEPLOY.py -h

"""


import argparse
from argparse import ArgumentParser, Namespace

import os
import fnmatch
import shutil

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Deploy a state's artifacts to the website."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Deploy a state's artifacts to the website.

    Copy all files in the output_dir to the 'intermediate' directory. Then:

    - Leave *.txt files in the 'intermediate' directory
    - Move all the *.png files to the 'images' directory
    - Leave all the *.json files in the 'intermediate' directory
    - Move the summary.csv files to the 'site_data' directory
    - Move the ratings.csv files to the 'site_data' directory
    - Copy the baseline BAF.csv file to the 'data' directory
    - Leave the remaining *.csv files in the 'intermediate' directory

    """

    args: Namespace = parse_args()

    xx: str = args.state
    verbose: bool = args.verbose

    #

    output_dir: str = os.path.expanduser("~/Downloads")
    output_dir = os.path.join(FileSpec(output_dir).abs_path, xx)
    if not os.path.isdir(output_dir):
        print(f"ERROR - Output directory not found: {output_dir}")
        exit(1)

    deploy_root: str = os.path.expanduser("~/iCloud/dev/pg")
    deploy_root = FileSpec(deploy_root).abs_path
    if not os.path.isdir(deploy_root):
        print(f"ERROR - Root deploy directory not found: {deploy_root}")
        exit(1)

    # Define individual deploy paths

    data: str = os.path.join(deploy_root, "data", xx)
    site_data: str = os.path.join(deploy_root, "docs", "_data")
    images: str = os.path.join(deploy_root, "docs", "assets", "images")
    intermediate: str = os.path.join(deploy_root, "intermediate", xx)

    print(f"Deploying {xx} ...")

    # Copy all files to the 'intermediate' directory
    shutil.copytree(output_dir, intermediate, dirs_exist_ok=True)

    # Then move (or copy) files to the appropriate directories
    for file in os.listdir(intermediate):
        source: str = os.path.join(intermediate, file)
        if fnmatch.fnmatch(file, "*.png"):
            shutil.move(source, images)
        elif fnmatch.fnmatch(file, "*_summary.csv"):
            shutil.move(source, site_data)
        elif fnmatch.fnmatch(file, "*_ratings.csv"):
            shutil.move(source, site_data)
        elif fnmatch.fnmatch(file, "*Baseline.csv"):
            shutil.copy(source, data)
        else:
            pass  # Leave the file in the intermediate directory

    print("... done!\n")
    print()
    print("REMEMBER: Copy & paste the YAML fragment into the state.yml file.\n")


if __name__ == "__main__":
    main()

### END ###
