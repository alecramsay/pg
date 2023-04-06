# Workflow

(1) Copy Official maps
* Snapshot Official map ids in pg/constants.py -- DONE
* Copy the Official maps, using the duplicate_official_maps.py script -- DONE

  For each new map in DRA -- DONE

* Set the Colors and Overlays
* Collect the id into pg/constants.py
* Export it

(2) Copy Notable Maps
* Snapshot Notable map ids in pg/constants.py -- DONE
* Copy Notable maps, using the duplicate_notable_maps.py script -- DONE

  For each new map in DRA -- DONE

* Set the Colors and Overlays
* Collect the id into pg/constants.py
* Export it

(3) Pull the ratings for the duplicated Official and Notable maps, using the pull_ratings.py script -- DONE

---

For each state:

(4) Create a baseline map using the tools in the 'baseline' repo

(5) Import the map, using the import_base_map.sh script

(6) Add the Share guid to constants.py

(7) In DRA:

* Set the Colors and Overlays -- 'Change Palette' to Plasma
* Collect the id into pg/constants.py
* Export the block-assignment file
* Rename it to XX_2020_Congress_Baseline.csv <<< NOTE - 2020 not 2022, and 'Baseline' not 'baseline'
* Move it to the data/XX/ folder

(8) Pull the ratings for it, using the pull_map_ratings.py script

(9) For each duplicated Official and Notable map in DRA:

* Turn District Lines on
* Turn on the background map
* [Change Palette] to Plasma
* Add the baseline map as a Custom Overlay -- no fill, no labels, line thickness = 2
* Download the map image, using right-click in Chrome
* Rename it to XX_2022_Congress_<label>_map.png <<< NOTE - 2022 not 2020!
* Move it to the docs/assets/images/ folder

(10) Analyze the Official & Notable maps, using the analyze_state.py script

(11) Finally, map the regions identified above: <<< TODO: Fix these scripts

* First run the map_regions.py script to create maps (.geojson) of the regions for the various maps
* Then use the plot_regions.py script to generate plots for those maps -- experiment with the height & width that work best for the state's shape; cut the resulting image down to the right size