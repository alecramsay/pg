---
layout: page
title: Overall Workflow
permalink: workflow_detailed/
---

This note describes the detailed workflow that Alec used for creating the maps for this study:

(1) Copied the Official maps

    - Grabbed the guids for the Official maps from DRA using a script; used this create a var in pg/constants.py
    - Duplicated the Official maps, using the duplicate_official_maps.py script 

    Then, for each new map in DRA <<< This stuff can't be done at the CLI right now

    - Set the Colors and Overlays
    - Copied the guid of the duplicate into pg/constants.py
    - Exported it

(2) Copied the Notable Maps

    - Copied the guids for the Notable Maps in DRA into pg/constants.py by hand
    - Inspected each map to make sure there were no problems; replaced bad maps (~20 / 210)
    - Duplicated the Notable Maps, using the duplicate_notable_maps.py script 

    For each new map in DRA <<< This stuff can't be done at the CLI right now

    - Set the Colors and Overlays
    - Copied the guid of the duplicate into pg/constants.py
    - Exported it

(3) Pulled the ratings for these maps

    - Using the pull_ratings.py script (which uses guids in pg/constants.py)


Then, for each state:

(4) Created a baseline map using [the 'baseline' workflow](baseline_workflow.md) 

(5) Imported it into DRA

    - Using the import_base_map.sh script 

(6) Opened the map in DRA & tweaked a few settings <<< This stuff can't be done at the CLI right now

    - Set the Colors and Overlays -- 'Change Palette' to Plasma
    - Copied the guid into pg/constants.py
    - Exported the block-assignment file (the baseline is imported as a precinct-assignment file)

    - Renamed the resulting CSV to XX_2020_Congress_Baseline.csv <<< NOTE - 2020 not 2022, and 'Baseline' not 'baseline'
    - Moved it to the data/XX/ folder

(7) Tweaked each duplicated Official and Notable map in DRA <<< This stuff can't be done at the CLI right now

    - Added the baseline map as a Custom Overlay -- no fill, no labels, (line thickness = 1) <<< TODO: Do we still want to do this?
    - Saved the images

        XX_2022_Congress_Compact_map.png
		XX_2022_Congress_Competitive_map.png
		XX_2022_Congress_Minority_map.png
		XX_2022_Congress_Official_map.png
		XX_2022_Congress_Proportional_map.png
		XX_2022_Congress_Splitting_map.png

    - Moved them to the docs/assets/images/ folder

(8) Analyzed the Official & Notable maps relative to the baseline map

    - scripts/analyze_state.py -s XX ...

    - Tweaked each district cores map in DRA (same settings as above) <<< This stuff can't be done at the CLI right now
    - Saved the images
	
        XX_2022_Congress_Compact_district_cores.png
		XX_2022_Congress_Competitive_district_cores.png
		XX_2022_Congress_Minority_district_cores.png
		XX_2022_Congress_Official_district_cores.png
		XX_2022_Congress_Proportional_district_cores.png
		XX_2022_Congress_Splitting_district_cores.png

	- Moved them to the docs/assets/images/ folder

(9) Added population deviation & runtimes to the abstract spreadsheet

    - cat intermediate/XX/XX20C_log_100.txt | awk 'END{print}'
	
(10) Turned the state on in the website

    - Added the Share link guid to states.yml and 
    - Flipped the 'ready' property for the state to 'true' <<< TODO: Is this necessary? I don't see where it's used.
    - On the state's page in docs/_pages/pages/XX.markdown, changed the layout to 'state' and removed the NYI one-liner.
