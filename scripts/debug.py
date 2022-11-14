#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

# from qgis.core import *

from pg import *


### PARSE ARGS ###

xx: str = "NC"
label: str = "Official"

fips_map: dict[str, str] = make_state_codes()
fips: str = fips_map[xx]


### CONSTRUCT FILENAMES & PATHS ###

regions_baf: str = path_to_file([temp_dir]) + file_name(
    [xx + yy, plan_type, label, "regions_BAF"], "_", "csv"
)

blocks_path: str = path_to_file([rawdata_dir, xx]) + file_name(
    ["tl_2020" + fips + "tabblock20"], "_"
)
# feature_shps: tuple[dict, dict[str, Any]] = load_shapes(blocks_path, unit_id("block"))


### QGIS ###


pass
