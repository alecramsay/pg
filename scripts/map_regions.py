#!/usr/bin/env python3

"""
Make a shapefile (GeoJSON) for the intersection regions of the comparison maps wrto the baseline map.

For example:

$ scripts/map_regions.py -s NC

For documentation, type:

$ scripts/map_regions.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
import pandas as pd
import geopandas
from geopandas import GeoDataFrame

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Map the intersection regions of the comparison maps wrto the baseline map"
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., MD)",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Make a shapefile (GeoJSON) for the intersection regions of the comparison maps wrto the baseline mao"""

    args: Namespace = parse_args()
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
        regions_summary_path: str = path_to_file([site_data_dir]) + file_name(
            [xx, yyyy, plan_type, label, "regions", "summary"], "_", "csv"
        )
        regions_map_path: str = path_to_file([temp_dir]) + file_name(
            [xx, yyyy, plan_type, label, "regions"], "_", "geojson"
        )

        ### LOAD BLOCK SHAPES & BLOCK REGION ASSIGNMENTS ###

        blocks_gdf: GeoDataFrame = geopandas.read_file(block_shps_path)
        blocks_gdf = blocks_gdf[["geometry", "GEOID20"]]  # type: ignore

        regions_gdf: GeoDataFrame = geopandas.read_file(regions_baf_path)
        regions_gdf = regions_gdf[["GEOID", "REGION"]]  # type: ignore

        ### JOIN THE REGIONS TO THE BLOCK SHAPES ###

        blocks_gdf = blocks_gdf.merge(
            regions_gdf,
            how="left",
            left_on="GEOID20",
            right_on="GEOID",
        )  # type: ignore

        blocks_gdf = blocks_gdf[["geometry", "GEOID", "REGION"]]  # type: ignore
        del regions_gdf

        ### DISSOLVE BLOCKS BY REGION ###

        regions_gdf: GeoDataFrame = blocks_gdf.dissolve(by="REGION", as_index=False)  # type: ignore
        del blocks_gdf

        ### LOAD THE REGION SUMMARY DATA ###

        regions_summary_gdf: GeoDataFrame = geopandas.read_file(regions_summary_path)
        regions_summary_gdf = regions_summary_gdf[
            ["REGION", "BASELINE", "OTHER", "POPULATION", "DISTRICT%", "CUMULATIVE%"]
        ]  # type: ignore
        regions_gdf = regions_gdf.merge(
            regions_summary_gdf,
            on="REGION",
            how="left",
        )  # type: ignore
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
        ]  # type: ignore

        ### WRITE THE REGIONS TO A SHAPEFILE ###

        regions_gdf.to_file(regions_map_path, driver="GeoJSON")
        # regions_df.to_file(regions_map_path, driver="GeoJSON")

        pass

    print("Done.")


if __name__ == "__main__":
    main()

### END ###
