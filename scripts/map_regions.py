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
import pandas as pd
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
fips_map: dict[str, str] = STATE_FIPS

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
    regions_summary_path: str = path_to_file([assets_dir]) + file_name(
        [xx, yyyy, plan_type, label, "regions"], "_", "csv"
    )
    regions_map_path: str = path_to_file([temp_dir]) + file_name(
        [xx, yyyy, plan_type, label, "regions"], "_", "geojson"
    )

    ### LOAD BLOCK SHAPES & BLOCK REGION ASSIGNMENTS ###

    # TYPE HINT
    blocks_gdf: GeoDataFrame = geopandas.read_file(block_shps_path)
    blocks_df: pd.Series[Any] | pd.DataFrame | Any = blocks_gdf[["geometry", "GEOID20"]]
    assert isinstance(blocks_df, pd.DataFrame)
    # blocks_gdf = blocks_gdf[["geometry", "GEOID20"]]

    # TYPE HINT
    regions_gdf: GeoDataFrame = geopandas.read_file(regions_baf_path)
    regions_df: pd.Series[Any] | pd.DataFrame | Any = regions_gdf[["GEOID", "REGION"]]
    assert isinstance(regions_df, pd.DataFrame)
    # regions_gdf = regions_gdf[["GEOID", "REGION"]]

    ### JOIN THE REGIONS TO THE BLOCK SHAPES ###

    # TYPE HINT
    blocks_df = blocks_df.merge(
        regions_df,
        how="left",
        left_on="GEOID20",
        right_on="GEOID",
    )
    # blocks_gdf = blocks_gdf.merge(
    #     regions_gdf,
    #     how="left",
    #     left_on="GEOID20",
    #     right_on="GEOID",
    # )
    blocks_df = blocks_df[["geometry", "GEOID", "REGION"]]
    # blocks_gdf = blocks_gdf[["geometry", "GEOID", "REGION"]]
    del regions_gdf
    del regions_df

    ### DISSOLVE BLOCKS BY REGION ###

    # TYPE HINT
    regions_df = blocks_df.dissolve(by="REGION", as_index=False)
    # regions_gdf: GeoDataFrame = blocks_gdf.dissolve(by="REGION", as_index=False)
    del blocks_gdf
    del blocks_df

    ### LOAD THE REGION SUMMARY DATA ###

    # TYPE HINT
    regions_summary_gdf: GeoDataFrame = geopandas.read_file(regions_summary_path)
    regions_summary_df: pd.Series[Any] | pd.DataFrame | Any = regions_summary_gdf[
        ["REGION", "BASELINE", "OTHER", "POPULATION", "DISTRICT%", "CUMULATIVE%"]
    ]
    # regions_summar_gdf = regions_summary_gdf[
    #     ["REGION", "BASELINE", "OTHER", "POPULATION", "DISTRICT%", "CUMULATIVE%"]
    # ]
    regions_df = regions_df.merge(
        regions_summary_df,
        on="REGION",
        how="left",
    )
    # regions_gdf = regions_gdf.merge(
    #     regions_summary_gdf,
    #     on="REGION",
    #     how="left",
    # )
    regions_df = regions_df[
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
    # regions_gdf = regions_gdf[
    #     [
    #         "geometry",
    #         "REGION",
    #         "BASELINE",
    #         "OTHER",
    #         "POPULATION",
    #         "DISTRICT%",
    #         "CUMULATIVE%",
    #     ]
    # ]

    ### WRITE THE REGIONS TO A SHAPEFILE ###

    regions_df.to_file(regions_map_path, driver="GeoJSON")
    # regions_gdf.to_file(regions_map_path, driver="GeoJSON")

    pass

print("Done.")

pass

### END ###
