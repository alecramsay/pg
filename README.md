# pg
Exploring redistricting tradeoffs inherent in a state's political geography

## Processing Steps

* Export BAF's for the notable maps for a state
* Move them to the appropriate state folder in the data/ directory
* Run the diff_maps script for the state
* Download the block shapes for the states
* Open them in QGIS
* Import the areas CSV
* Join the areas data to the shapes (removing the auto prefix)
* Dissolve blocks by area
* Make the areas layer permanent
* Delete the block-level fields
* Turn on area labels

## TODO

* Sort areas by population instead of # blocks
* Add block-count validations
* Diff all states
* Figure out how to visualize the diffs