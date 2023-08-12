# Post-Baseline Workflow

TODO - DELETE: I've implemented this.

This note describes the workflow (and ultimately a command) 
to generate all the artifacts necessary for the website or a side-by-side analysis,
given a baseline map for a state.
Actually updating the website with these artifacts is a separate step, 
so alternative baselines can be explored without affecting the website.

I'll wrap all this up in a single command that will take:

- the state abbreviation (e.g., XX)
- a precinct-assignment file (PAF) for the baseline map, and
- an output directory (e.g., ~/Downloads)

and will create all the artifacts in the output directory.
From there, they can be copied to the appropriate locations. 

I'll use this command to generate the artifacts for the website, instead of my current much more manual process. 
Others will be able use the same command to generate analogous artifacts for other baseline maps
which they could write up independently (e.g., in blog posts or papers).

## Context

This commmand/workflow assumes that the following files already exist for the state in data/XX/:

- A block-assignment file (BAF) for the official map (e.g., XX_2022_Congress_Official.csv)
- A BAF for each of the five notable maps (e.g., XX_2022_Congress_{label}.csv, 
  where {label} is one of Proportional, Competitive, Minority, Compact, and Splitting)

The baseline map hasn't been converted from precinct to block assignments.
The district ids in the assignment files have not been canonicalized.
No DRA maps have been created yet.

TODO: Once this is working, I'll want to 
delete the existing maps in DRA,
rationalize what's in constants.py (Issue #43), and 
delete the obsolete regions artifacts (Issue #28).

The rest of this note describes the sequential steps.

## Workflow / Command

I'll develop and test this workflow as a series of standalone scripts, and 
then I'll wrap them up into the single uber command imagined above.

### Copy the baseline & other maps to the output directory

This step will copy the input baseline assignment file and the BAFs for the official & notable maps 
to the output directory so it contains the inputs and outputs.

### Convert the baseline assignments from precincts to blocks

TODO: I should pull out of individual scripts which states uses blockgroups (BGs) instead of precincts (VTDs), and
consolidate that metadata into a reusable file (like constants.py).
This step needs to know whether to use BGs or VTDs.

TODO: Also need to ensure that the VTD- or BG-to-block mappings have been created.
They weren't in the most recent series of extract_data.py runs.

TODO: Then I need to write a script to do this, but it's straightforward.

Once this is done, there are BAFs for the official map, the five notable maps, and the baseline map.
The district ids in the BAFs are not canonicalized though.
That is the starting point for the main process below.

### Find the district cores & canonicalize the district ids

This step canonicalizes district ids on the official districts, and 
interects the districts for each pair of maps.

Using Todd's renumbering command:

```bash
python3 renumber.py --basemap baseline.csv --comparatormap proportional.csv --renumbered new_proportional.csv --cores baseline_proportional_cores.csv
```

this step would:

- first renumber the districts in the baseline map based on its cores with the official maps, and 
- then renumber the districts in each of the notable maps based on their cores with the *renumbered* baseline districts

The results will be:

- Seven BAFs with canonical district ids with names of the form 
  XX_2022_Congress_{label}_canonical.csv, where {label} is one of Official, Proportional, Competitive, Minority, Compact, Splitting, and Baseline
- Six BAFs with canonical district ids for the intersections ("cores") of the official and notable maps with the baseline map 
  with names of the form XX_2022_Congress_{label}_cores.csv

### Import the canonicalized BAFs into DRA

This step will import the seven BAFs into DRA, generating the seven maps.
It will also capture the guids for the seven maps (output of the import command) in files of the form 
XX_2022_Congress_{label}_map_guid.txt.

TODO: Formally ask Terry to echo the guid on successful CLI import.

### Update the maps' display properties

This step will use the map GUIDs captured above to:

- Set Overlays / Map, District Lines, and (District) Labels options on (checked) and everything else off (not checked), and
- Set Map Settings / Color Palette / to Plasma

for all seven maps.

TODO: Formally ask Terry to enable these at the command line.

### Generate images of the maps

This step will generate an image for each of the seven maps
with names of the form XX_2022_Congress_{label}_map.png.

TODO: Figure out whether we can automate Chrome or 
whether we'll export a .geojson and write a script to generate an image from it.

Note: I'm assuming that we *won't* add the baseline map as a Custom Overlay to the other six maps.
I think the visual is too cluttered, especially since we'll have the intersection map, and 
we can't do this at the command line.

### Pull ratings for the maps

Then we'll pull the ratings for the maps from DRA, using the GUIDs captured above.
The results will be named XX_2022_Congress_{label}_ratings.json.

### Compare the ratings for the official & notable maps to the baseline's

This step will compare the ratings for the six non-baseline maps to those for the baseline map.
It will generate a radar diagram for each pair, and
write the ratings for all seven maps to a CSV file for the "Ratings vs. Baseline" table.

### Compare the districts for the official & notable maps to the baseline's

This step will do the analogous comparison for the districts for the "Districts vs. Baseline" section.
The interections ("cores") have already been computed above.
This step will generate a CSV of populations by from/to intersection for the table.
Note: I've already written this script. 

### Generate a fragment for state.yml

This last step will produce the appropriate entry for the state to be used in state.yml.
It's an enumeration of maps (including the core maps) and their associated GUIDs in DRA.

TODO: Need to write this script.

## Integrate the results into the website

This step will move the resulting artifacts to the appropriate website directories:

- The canonicalized BAFs, the cores BAFs, the ratings JSONs, and the GUID text files will all go in data/XX/
- The map images will go in docs/assets/images/
- The CSVs for the tables (grids) will go in docs/_data/
- The YML entry will be pasted into docs/_data/state.yml
