#!/usr/bin/env python3

"""
Make a shapefile (GeoJSON) for the intersection regions of the comparison maps wrto the baseline mao

For example:

$ scripts/map_regions.py NC

For documentation, type:

$ scripts/map_regions.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
import geopandas
from geopandas import GeoDataFrame

from pg import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(
    description="Map the intersection regions of the comparison maps wrto the baseline map"
)

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)

parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args: Namespace = parser.parse_args()

xx: str = args.state
fips_map: dict[str, str] = make_state_codes()

fips: str = fips_map[xx]


### MAKE A SHAPEFILE FOR EACH COMPARISON MAP ###

for label in [
    "Official",
    "Proportional",
    "Competitive",
    "Minority",
    "Compact",
    "Splitting",
]:
    print("Making shapefile for the", label, "map ...")

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
    regions_map_path: str = path_to_file(["content"]) + file_name(
        [xx, yyyy, plan_type, label, "regions"], "_", "geojson"
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

    regions_gdf.to_file(regions_map_path, driver="GeoJSON")

    pass

print("Done.")

pass
