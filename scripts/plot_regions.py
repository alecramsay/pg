#!/usr/bin/env python3

"""
Plot the intersecting regions of a map wrto the baseline map on a map.

For example:

$ scripts/plot_regions.py -s NC
$ scripts/plot_regions.py -s NC -t
$ scripts/plot_regions.py -s NC -o vertical -t
$ scripts/plot_regions.py -s NC -H 6 -W 4 -t

For documentation, type:

$ scripts/plot_regions.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
import pandas as pd
import geopandas
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, Axes  # type: ignore
from typing import List

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Plot regions on a map"
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
        "--orientation",
        help="The orientation of the color bar",
        type=str,
        default="horizontal",
    )
    parser.add_argument(
        "-W", "--width", help="The width of the plot", type=int, default=8
    )
    parser.add_argument(
        "-H", "--height", help="The height of the plot", type=int, default=8
    )
    parser.add_argument(
        "-t", "--test", dest="test", action="store_true", help="Test mode"
    )  # Show one plot vs. write all plots

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )  # NOOP

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Plot the intersecting regions of a map wrto the baseline map on a map."""

    args: Namespace = parse_args()
    xx: str = args.state

    fips_map: dict[str, str] = STATE_FIPS
    fips: str = fips_map[xx]

    w: int = args.width  # 6 inches is the matplotlib default
    h: int = args.height  # 4 inches is the matplotlib default

    legend: bool = True

    if args.orientation in ["vertical", "horizontal"]:
        orientation: str = args.orientation
    else:
        raise ValueError("Orientation must be 'vertical' or 'horizontal'")

    test: bool = args.test
    verbose: bool = args.verbose  # Show the plot

    #

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

        regions_path: str = path_to_file([temp_dir]) + file_name(
            [xx, yyyy, plan_type, label, "regions"], "_", "geojson"
        )
        regions_plot_path: str = path_to_file([assets_dir]) + file_name(
            [xx, yyyy, plan_type, label, "regions"], "_", "png"
        )

        ### LOAD THE REGIONS ###

        regions_gdf: GeoDataFrame = geopandas.read_file(regions_path)
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
        # TYPE HINT
        # regions_df: pd.Series[Any] | pd.DataFrame | Any = regions_gdf[
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
        # assert isinstance(regions_df, pd.DataFrame)

        # Add points for label placement
        regions_gdf["labelpos"] = regions_gdf["geometry"].representative_point()
        # regions_df["labelpos"] = regions_df["geometry"].representative_point()

        ### PLOT THE REGIONS ON A MAP ###

        # Instead of simply this:
        # regions_gdf.plot()
        # the code below follows this example:
        # https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac

        dimension: str = "DISTRICT%"
        colors: str = "Blues"
        lines: float = 1.25
        title: str = "% of District Population by Region"
        title_font_size: int = 12
        label_font_size: int = 4

        #

        fig: Figure
        ax: List[Axes]

        fig, ax = plt.subplots(1, figsize=(w, h))

        # TYPE HINT
        ax.axis("off")
        ax.set_title(title, fontdict={"size": title_font_size, "weight": "normal"})
        # ax[0].axis("off")
        # ax[0].set_title(title, fontdict={"size": title_font_size, "weight": "normal"})

        # A colorbar legend
        if legend:
            vmin: int = 0
            vmax: int = 100
            sm: plt.cm.ScalarMappable = plt.cm.ScalarMappable(
                cmap=colors, norm=plt.Normalize(vmin=vmin, vmax=vmax)
            )
            # TYPE HINT
            # sm: plt.colorbar.ScalarMappable = plt.colorbar.cm.ScalarMappable(
            #     cmap=colors, norm=plt.colorbar.Normalize(vmin=vmin, vmax=vmax)
            # )
            sm._A = []
            fig.colorbar(sm, orientation=orientation, ax=ax, shrink=0.5)

        # Region labels
        for idx, row in regions_gdf.iterrows():
            ax.annotate(
                "{}".format(row["REGION"]),
                xy=row["labelpos"].coords[0],
                ha="center",
                va="center",
                fontsize=label_font_size,
            )
            # TYPE HINT
            # ax[0].annotate(
            #     "{}".format(row["REGION"]),
            #     xy=row["labelpos"].coords[0],
            #     ha="center",
            #     va="center",
            #     fontsize=label_font_size,
            # )

        regions_gdf.plot(
            column=dimension, cmap=colors, linewidth=lines, ax=ax, edgecolor="0.8"
        )
        # TYPE HINT
        # regions_gdf.plot(
        #     column=dimension, cmap=colors, linewidth=lines, ax=ax[0], edgecolor="0.8"
        # )

        if test:
            plt.show()
            break
        else:
            fig.savefig(regions_plot_path, dpi=300)


if __name__ == "__main__":
    main()

### END ###
