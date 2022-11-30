---
layout: page
title: About
permalink: about/
---

This analysis covers the 37 states apportioned three or more congressional districts in the 2020 census.
States with only two congressional districts were excluded, because the baseline districts aren't interesting.

## Data

The data used came from several sources:
- The block-assignment files for Notable Maps were exported from DRA on 10/06/22. A few of the maps violated basic requirements (like contiguity) and were replaced by the next best maps that didn't.
- The district shapes for Notable Maps were also exported from DRA on 10/06/22.
- Census data were downloaded from the dra2020/dra-data repository on 10/06/22.
- The block shapes were downloaded from [census.gov](https://www2.census.gov/geo/tiger/TIGER2020/TABBLOCK20/) on 10/06/22.

## Workflow

Given the number of maps involved -- 37 states x 7 Official, Notable, and baselines maps = 259 maps -- the analysis was highly automated:

1. Copied the Official maps from DRA:
  - Snapshoted the Official map ids in pg/constants.py
  - Copied the Official maps, using the duplicate_official_maps.py script -- then in DRA, for each new map:
  - Set the Colors and Overlays
  - Collected the id into pg/constants.py
  - Exported it

2. Copied the Notable Maps from DRA
  - Snapshoted Notable map ids in pg/constants.py
  - Copied the Notable maps, using the duplicate_notable_maps.py script -- then in DRA, for each new map:
  - Set the Colors and Overlays
  - Collected the id into pg/constants.py
  - Exported it

3. Pulled the ratings for the duplicated Official and Notable maps, using the pull_ratings.py script

4. Created a baseline map for a state, using the tools in the 'baseline' repo

5. For each baseline map:
  - Imported the map, using the import_base_map.sh script -- then in DRA:
  - Set the Colors and Overlays -- 'Change Palette' to Plasma
  - Collected the id into pg/constants.py
  - Exported it

6. For each duplicated Official and Notable map in DRA:
  - Turned District Lines on
  - Turned on the background map
  - Change the color palette to Plasma
  - Added the baseline map as a Custom Overlay -- no fill, line thickness = 2
  - Downloaded the map image, using right-click in Chrome

7. Analyzed the Official & Notable maps, using the analyze_state.py script

8. Finally, mapped the regions identified above:
  - First ran the map_regions.py script to create maps (.geojson) of the regions for the various maps
  - Then used the plot_regions.py script to generate plots for those maps