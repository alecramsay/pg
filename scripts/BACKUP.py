#!/usr/bin/env python3

"""
Backup a state's artifacts for safekeeping.

For example:

$ scripts/BACKUP.py -s NC

For documentation, type:

$ scripts/BACKUP.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os
import shutil

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Backup a state's artifacts for safekeeping."
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
    """Backup a state's artifacts for safekeeping."""

    args: Namespace = parse_args()

    xx: str = args.state
    verbose: bool = args.verbose

    #

    output_dir: str = os.path.expanduser("~/Downloads")
    backup_dir: str = os.path.expanduser("~/local/pg-backup")

    output_dir = os.path.join(FileSpec(output_dir).abs_path, xx)
    if not os.path.isdir(output_dir):
        print(f"ERROR - Output directory not found: {output_dir}")
        exit(1)

    backup_dir = FileSpec(backup_dir).abs_path
    if not os.path.isdir(backup_dir):
        print(f"ERROR - Root backup directory not found: {backup_dir}")
        exit(1)

    backup_dir = os.path.join(backup_dir, xx)
    if os.path.isdir(backup_dir):
        print(
            f"ERROR - Backup subdirectory {xx} already exists. Please remove it & re-run."
        )
        exit(1)

    #

    print(f"Backing up {xx} ...")

    shutil.copytree(output_dir, backup_dir)

    print("... done!\n")
    print()


if __name__ == "__main__":
    main()

### END ###
