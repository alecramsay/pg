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

(4) Create a baseline map using the 'baseline' workflow

(5) Import the map, using the import_base_map.sh script

(6) Open the map in DRA:

* Set the Colors and Overlays -- 'Change Palette' to Plasma
* Copy the Share link guid to constants.py in both the 'baseline' and 'pg' repos
* Export the block-assignment file
* Rename it to XX_2020_Congress_Baseline.csv <<< NOTE - 2020 not 2022, and 'Baseline' not 'baseline'
* Move it to the data/XX/ folder

(x) Pull the ratings for it, using the pull_map_ratings.py script <<< This is done by analyze_state.py. Dup?

(8) For each duplicated Official and Notable map in DRA:

* Turn District Lines on
* Turn on the background map
* [Change Palette] to Plasma
* Add the baseline map as a Custom Overlay -- no fill, no labels, (line thickness = 1)
* Download the map image, using right-click in Chrome
* Rename it to XX_2022_Congress_<label>_map.png <<< NOTE - 2022 not 2020!
* Move it to the docs/assets/images/ folder

(9) Analyze the Official & Notable maps, using the analyze_state.py script
