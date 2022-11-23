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


### CONSTRUCT PATHS ###

regions_path: str = path_to_file(["content"]) + file_name(
    [xx, yyyy, plan_type, label, "regions"], "_", "geojson"
)

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

regions_plot_path: str = path_to_file(["content"]) + file_name(
    [xx, yyyy, plan_type, label, "regions"], "_", "png"
)

# regions_gdf.plot()

# Following this example -- https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac

gradient: str = "DISTRICT%"
colors: str = "Blues"
lines: float = 1.25
title: str = "% of District Population by Region"

fig: Figure
ax: List[Axes]
fig, ax = plt.subplots(1, figsize=(10, 6))  # TODO: figsize

ax.axis("off")
ax.set_title(title, fontdict={"fontsize": "14", "fontweight": "3"})

# colorbar as a legend
vmin: int = 0
vmax: int = 100
sm = plt.cm.ScalarMappable(cmap=colors, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
fig.colorbar(sm)

# TODO: label regions

regions_gdf.plot(column=gradient, cmap=colors, linewidth=lines, ax=ax, edgecolor="0.8")

# saving our map as .png file.
# fig.savefig(regions_plot_path, dpi=300)

pass
