#!/usr/bin/env python3

"""
Restore a state's backed up artifacts for further processing.

For example:

$ scripts/RESTORE.py -s NC

For documentation, type:

$ scripts/RESTORE.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os
import shutil

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Restore a state's backed up artifacts for further processing."
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
    """Restore a state's backed up artifacts for further processing."""

    args: Namespace = parse_args()

    xx: str = args.state
    verbose: bool = args.verbose

    #

    backup_dir: str = os.path.expanduser("~/local/pg-backup")
    output_dir: str = os.path.expanduser("~/Downloads")

    backup_dir = os.path.join(FileSpec(backup_dir).abs_path, xx)
    if not os.path.isdir(FileSpec(backup_dir).abs_path):
        print(f"ERROR - Backup directory not found: {backup_dir}")
        exit(1)

    output_dir = FileSpec(output_dir).abs_path
    if not os.path.isdir(output_dir):
        print(f"ERROR - Root output directory not found: {output_dir}")
        exit(1)

    output_dir = os.path.join(output_dir, xx)
    if os.path.isdir(output_dir):
        print(
            f"ERROR - Output subdirectory {xx} already exists. Please remove it & re-run."
        )
        exit(1)

    #

    print(f"Restoring {xx} ...")

    shutil.copytree(backup_dir, output_dir)

    print("... done!\n")


if __name__ == "__main__":
    main()

### END ###
