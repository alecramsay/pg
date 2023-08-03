# (Re)baseline State

TODO: Update and keep or delete this?

This note describes a command that we'd like to have that would generate all the artifacts necessary for the website without manual intervention. The results would be created in ~/Downloads from where they could be copied to the appropriate locations. 

We'd use this command to generate the artifacts for the website. Others could use the same command to generate analogous artifacts for other baselines which they could write up independently (e.g., in blog posts or papers).

## Context

Such a command (capability) assumes that a bunch of work has already been done (and doesn't have to be redone). For the state in question, for the official map and each of the five notable maps:

- The map has duplicated in Dave's Redistricting (DRA)
- The guid for the Share link has been captured in a file (for downstream use)
- The ratings for the five dimensions have been pulled
- The Overlays / Map, District Lines, and (District) Labels options are all on (checked), and everything else off (not checked)
- Map Settings / Color Palette / is set to Plasma
- An image of the map has been captured (currently using the Chrome hack), and 
- A block-assignment file has been exported for the map. 

This is all one-time work and doesn't have to be re-done. A non-trivial number of notable maps (close to 20) had to be replaced for one reason or another, so trying to further automate this part of the process and re-generate wouldn't make a lot of sense to me.

***Not true! The notable maps would be* not *be canonicalized. The actual context is just the block-assignment files for the (copies of the) official and notable maps. This is a much smaller / lower starting point.***

*The one exception that I could imagine is that if we generated map images for the baseline and district intersections ("cores") below starting with a .geojson file instead of automating the Chrome hack, to make the images for the above maps match the style of those images, we'd probably want to regenerate the images above. Alternatively, if we can automate the Chrome hack somehow, we could use that below too.*

## Command

For example, this command:

`scripts/rebaseline_state.py -s NC -b NC_assignments.csv`

would produce:

- Block-assignment files (BAF) for each map official, five notable, and baseline maps where the district ids have been canonicalized (probably on the official map's)
- Dave's Redistricting (DRA) maps imported from those BAF's where the metadata and visual properties for the maps have been set properly (details below)
- Share links for those maps
- Map images (.png) for those maps -- like produced today using the Chrome hack but possibly using another mechanism/process
- A CSV of the ratings for these seven maps

and some analogous artifacts for each pair of official or notable map and the baseline map:

- BAF's for the intersection of each pair of maps, where the district ids have been canonicalized and the intersections are labeled from/to
- DRA maps imported from these BAF's where the metadata and visual properties for the maps have been set properly
- Share links for these intersection maps
- Map images (.png) for these intersection maps
- CSV's of the population by intersecting region for these maps
 
## Processing Details

TODO

would process the baseline map:

- Import the baseline map into DRA
- Capture the guid the Share link (for downstream processing)

- Set Overlays / Map, District Lines, and (District) Labels options on (checked) and everything else off (not checked) <<< INV
- Set Map Settings / Color Palette / to Plasma <<< INV
- Generate an image of the map (either using the Chrome hack -or- by exporting a .geojson that a script ingests to produce the desired image) <<< INV
- Create a block-assignment file for the map <<< NOTE: if baseline maps  a) use precincts and b) don't split them, this could be done outside of DRA
- Pull the ratings for the map (using the guid)

and ...

- Add the baseline map as a Custom Overlay <<< ???
 
and then compare the official map and each of the five notable maps to it:
 
- Generate a radar diagram for the pair
- Find all cores (intersections), using block-assignment files as input and producing a mapping of district ids to canonical ids for the map -- to do this, would we a) first compare the official districts to the baseline districts and canonicalize the latter on the former and then use those as the canonical districts for each of the comparisons with the notable maps -or- b) compare the baseline and each of the notable maps with the official districts?
- [TODO: HERE]
- Import the intersections map into DRA
- Set the Overlays and Map Settings and generate an image for the intersection map, like with the baseline map above
- Generate a CSV of populations by from/to intersection for the "Districts vs. Baseline" table 

It would also write the ratings for the seven maps to a CSV file (once for the state) for the "Ratings vs. Baseline" table.

*This command for a baseline for one state could, of course, be wrapped in a shell script to do this for a set of baselines, e.g., a new set for each of the 42 states in our study.*
