#!/usr/bin/env python3

"""
Plot the intersecting regions of a map wrto the baseline map on a map.

For example:

$ scripts/plot_regions.py NC Official
$ scripts/plot_regions.py NC Official -H 6 -W 4 -v

For documentation, type:

$ scripts/plot_regions.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
import geopandas
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, Axes
from typing import List

from pg import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(description="Plot regions on a map")

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)
parser.add_argument("label", help="The map the regions belong to", type=str)

parser.add_argument("-W", "--width", help="The width of the plot", type=int, default=8)
parser.add_argument(
    "-H", "--height", help="The height of the plot", type=int, default=8
)
parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)  # Shows the plot

args: Namespace = parser.parse_args()
fips_map: dict[str, str] = make_state_codes()

xx: str = args.state
fips: str = fips_map[xx]
label: str = args.label

w: int = args.width  # 6 inches is the matplotlib default
h: int = args.height  # 4 inches is the matplotlib default
# No need to repeat the colorbar on every plot
legend: bool = False
orientation: str = "vertical"  # "horizontal"

save: bool = True  # No interactive mode for scripts

verbose: bool = args.verbose

### CONSTRUCT PATHS ###

regions_path: str = path_to_file(["content"]) + file_name(
    [xx, yyyy, plan_type, label, "regions"], "_", "geojson"
)
regions_plot_path: str = path_to_file(["content"]) + file_name(
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
# Add points for label placement
regions_gdf["labelpos"] = regions_gdf["geometry"].representative_point()


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

ax.axis("off")
ax.set_title(title, fontdict={"size": title_font_size, "weight": "normal"})

# A colorbar legend
if legend:
    vmin: int = 0
    vmax: int = 100
    sm = plt.cm.ScalarMappable(cmap=colors, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    fig.colorbar(sm, orientation=orientation, shrink=0.5)

# Region labels
for idx, row in regions_gdf.iterrows():
    ax.annotate(
        "{}".format(row["REGION"]),
        xy=row["labelpos"].coords[0],
        ha="center",
        va="center",
        fontsize=label_font_size,
    )

regions_gdf.plot(column=dimension, cmap=colors, linewidth=lines, ax=ax, edgecolor="0.8")

if save:
    fig.savefig(regions_plot_path, dpi=300)

if verbose:
    plt.show()

#
