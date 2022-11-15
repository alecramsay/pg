#!/usr/bin/env python3

"""
Duplicate Notable maps.

For example:

$ scripts/duplicate_notable_maps.py

For documentation, type:

$ scripts/duplicate_notable_maps.py -h

Using the draclient.js command-line script:

$ ./draclient.js --help
Usage: -p [parallel clients] -f [script file] -u [url] -v [verbosity level] -n
[username] -x [password]

Options:
  --help             Show help                                         [boolean]
  --version          Show version number                               [boolean]
  -v, --verbosity    Verbose output.                       [number] [default: 0]
  -f, --file         File with load test scripts.
  -p, --parallel     How many clients to run at a time in parallel on the
                     script.                               [number] [default: 1]
  -h, --host         Host to operate against. [default: "http://localhost:3000"]
  -u, --user         User name to use to connect.
  -x, --password     Password to use when connecting.
  -i, --id           ID of map to operate against.
  -d, --duplicate    Duplicate the current map and update the current map to be
                     the new one.
  -N, --name         Set name of specified map.
  -D, --description  Set description of specified map.
  -L, --labels       Set labels of map. Use leading + to indicate adding, -
                     indicate removing, none indicates replace.          [array]
  -P, --print        Print meta data of the given map, use all for entire meta
                     data, otherwise list of fields to print.            [array]

Examples:
  draclient.js -p 10  Load test with 10 clients.

"""

import os

from pg import *

group: str = "Notable"
label: str = "PG-" + group.upper()


def make_command(group: str, label: str, xx: str, id: str) -> str:
    # scripts/duplicate_map.sh NC Congress 2022 Proportional PG-NOTABLE 7cfcec86-b8bf-41fa-a6c2-0be9b3799747
    return f"scripts/duplicate_map.sh {xx} {plan_type} {yyyy} {group} {label} {id}"


for xx, maps in notables_copy.items():
    for dim, id in maps.items():
        os.system(make_command(dim.capitalize(), label, xx, id))
        pass

#
