#!/usr/bin/env python3
#
# STANDALONE GEOPROCESSING SCRIPT
#

import geopandas
from geopandas import GeoDataFrame

from pg import *

### Make a shapefile for the regions of the {label} map wrto the baseline mao

### PARSE ARGS ###

fips_map: dict[str, str] = make_state_codes()

xx: str = "NC"
fips: str = fips_map[xx]
label: str = "Official"


### CONSTRUCT PATHS ###

block_shps_path: str = path_to_file([rawdata_dir, xx]) + file_name(
    ["tl", cycle, fips, "tabblock20"], "_"
)
regions_baf_path: str = path_to_file([temp_dir]) + file_name(
    [xx, yyyy, plan_type, label, "regions", "BAF"], "_", "csv"
)
regions_summary_path: str = path_to_file(["content"]) + file_name(
    [xx, yyyy, plan_type, label, "regions", "summary"], "_", "csv"
)


### LOAD BLOCK SHAPES & BLOCK REGION ASSIGNMENTS ###

blocks_gdf: GeoDataFrame = geopandas.read_file(block_shps_path)
blocks_gdf = blocks_gdf[["geometry", "GEOID20"]]

regions_gdf: GeoDataFrame = geopandas.read_file(regions_baf_path)
regions_gdf = regions_gdf[["GEOID", "REGION"]]


### JOIN THE REGIONS TO THE BLOCK SHAPES ###

blocks_gdf = blocks_gdf.merge(
    regions_gdf,
    how="left",
    left_on="GEOID20",
    right_on="GEOID",
)
blocks_gdf = blocks_gdf[["geometry", "GEOID", "REGION"]]
del regions_gdf


### DISSOLVE BLOCKS BY REGION ###

regions_gdf: GeoDataFrame = blocks_gdf.dissolve(by="REGION", as_index=False)
del blocks_gdf


### LOAD THE REGION SUMMARY DATA ###

regions_summary: GeoDataFrame = geopandas.read_file(regions_summary_path)
regions_summary = regions_summary[
    ["REGION", "BASELINE", "OTHER", "POPULATION", "DISTRICT%", "CUMULATIVE%"]
]
regions_gdf = regions_gdf.merge(
    regions_summary,
    on="REGION",
    how="left",
)
regions_gdf = regions_gdf[
    [
        "geometry",
        "REGION",
        "BASELINE",
        "OTHER",
        "POPULATION",
        "DISTRICT%",
        "CUMULATIVE%",
    ]
]


### WRITE THE REGIONS TO A SHAPEFILE ###

# TODO

pass
