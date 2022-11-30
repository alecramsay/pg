#!/usr/bin/env python3
#
# STANDALONE GEOPROCESSING SCRIPT
#

import geopandas
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure, Axes
from typing import List

from pg import *


fips_map: dict[str, str] = make_state_codes()

xx: str = "NC"
fips: str = fips_map[xx]
label: str = "Official"

w: int = 8  # 6 inches is the default
h: int = 8  # 4 inches is the default
legend: bool = True
orientation: str = "vertical"
# orientation: str = "horizontal"

save: bool = False


### CONSTRUCT PATHS ###

regions_path: str = path_to_file([temp_dir]) + file_name(
    [xx, yyyy, plan_type, label, "regions"], "_", "geojson"
)
regions_plot_path: str = path_to_file([assets_dir]) + file_name(
    [xx, yyyy, plan_type, label, "regions"], "_", "png"
)


# LOAD THE REGIONS

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


### PLOT REGIONS ON A MAP ###

# Instead of simply this:
# regions_gdf.plot()
# the code below follows this example:
# https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac

dimension: str = "DISTRICT%"
colors: str = "Blues"
lines: float = 1.25
title: str = "% of District Population by Region"

fig: Figure
ax: List[Axes]

fig, ax = plt.subplots(1, figsize=(w, h))

ax.axis("off")
ax.set_title(title, fontdict={"fontsize": "14", "fontweight": "3"})

# A colorbar legend
if legend:
    vmin: int = 0
    vmax: int = 100
    # sm = plt.cm.ScalarMappable(cmap=colors, norm=plt.Normalize(hmin=vmin, hmax=vmax))
    sm = plt.cm.ScalarMappable(cmap=colors, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    fig.colorbar(sm, orientation=orientation, shrink=0.5)
    # fig.colorbar(sm, location="bottom", orientation="horizontal", shrink=0.5)
    # fig.colorbar(sm, location="right", orientation="vertical", shrink=0.5)

# Region labels
for idx, row in regions_gdf.iterrows():
    ax.annotate(
        "{}".format(row["REGION"]),
        xy=row["labelpos"].coords[0],
        ha="center",
        va="center",
        fontsize=8,
    )

regions_gdf.plot(column=dimension, cmap=colors, linewidth=lines, ax=ax, edgecolor="0.8")

if save:
    fig.savefig(regions_plot_path, dpi=300)

pass
