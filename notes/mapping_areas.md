# Analysis

NOTE - These instructions are for manual processing using QGIS, and "areas" are now "regions."

* Open the census block shapes in QGIS <<< Where are these?
* Import the areas_by_block CSV <<< The "{XX}_2022_Congress_{label}_regions_BAF.csv" in temp/
* Join the areas data to the shapes (removing the auto prefix)
* Dissolve blocks by area
* Make the area shapes layer permanent
* Delete the block-level fields

* Import the areas CSV <<< The "{XX}_2022_Congress_{label}_regions_summary.csv" files in content/
* Join the areas CSV to the area shapes layer
* Make the joined layer permanent

--

* Open the census block shapes in QGIS <<< Where are these?
* Import the areas_by_block CSV <<< The "{XX}_2022_Congress_{label}_regions_BAF.csv" in temp/
* Join the areas data to the shapes (removing the auto prefix)
* Dissolve blocks by area
* Make the area shapes layer permanent
* Delete the block-level fields

* Import the areas CSV <<< The "{XX}_2022_Congress_{label}_regions_summary.csv" files in content/
* Join the areas CSV to the area shapes layer
* Make the joined layer permanent
