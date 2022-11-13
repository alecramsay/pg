# Workflow

(1) Copy Official maps
* Snapshot Official map ids in pg/constants.py -- DONE
* Copy the Official maps, using the duplicate_official_maps.py script
* Set the Colors and Overlays (in DRA)
* Collect the ids for the new maps in pg/constants.py
* Export the new maps, using the {TBD} script

(2) Copy Notable Maps
* Snapshot Notable map ids in pg/constants.py -- DONE
* Copy Notable maps, using the duplicate_notable_maps.py script
* Set the Colors and Overlays (in DRA)
* Collect the ids for the new maps in pg/constants.py
* Export the new maps, using the {TBD} script

(3) Pull the ratings for the Official and Notable maps, using the pull_ratings.py script

(4) Create a baseline map for a state, using the tools in the 'baseline' repo

(5) For each baseline map:
* Import the map, using the import_base_map.sh script
* Set the Colors and Overlays (in DRA)
* Collect the id for the new map in pg/constants.py
* Export the map, using the {TBD} script

(6) Analyze the Official & Notable maps, using the analyze_state.py script
* This pulls the ratings for the baseline map, and
* Plot radar diagrams for each map vs. the baseline map
* And TBD ...

(7) For each Official and Notable map (in DRA)
* Add the baseline map as a Custom Overlay
* Download the map image, using right-click in Chrome