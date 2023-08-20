---
layout: page
title: Overall Workflow
permalink: workflow_detailed/
---

This note describes the detailed workflow that Alec used for creating the maps for this study:

(1) Copied the Official maps from DRA

    - Grabbed the guids for the Official maps from DRA using a script; used this create a var in pg/constants.py
    - Duplicated the Official maps, using the duplicate_official_maps.py script 

    Then, for each new map in DRA <<< This stuff can't be done at the CLI right now

    - Set the Colors and Overlays
    - Copied the guid of the duplicate into pg/constants.py
    - Exported it

    In the re-work, I simply started with these block-assignment files.
    I chucked everything else.

(2) Copied the Notable Maps from DRA

    - Copied the guids for the Notable Maps in DRA into pg/constants.py by hand
    - Inspected each map to make sure there were no problems; replaced bad maps (~20 / 210)
    - Duplicated the Notable Maps, using the duplicate_notable_maps.py script 

    For each new map in DRA <<< This stuff can't be done at the CLI right now

    - Set the Colors and Overlays
    - Copied the guid of the duplicate into pg/constants.py
    - Exported it

    In the re-work, I simply started with these block-assignment files.
    I chucked everything else.

(x) This step was pulling the ratings for these maps. In the re-work, that is integrated into the analyze_state scripts below.

Then, for each state:

(3) Created a baseline map using [the 'baseline' workflow](baseline_workflow.markdown) 

    Added population deviation & runtimes to the abstract spreadsheet

    - cat intermediate/XX/XX20C_log_100.txt | awk 'END{print}'

(4) Analyzed the official & notable maps relative to the baseline map

    - scripts/analyze_state_part1.py -s XX
    - scripts/analyze_state_part2.py -s XX

(5) Deployed the artifacts

    - scripts/DEPLOY.py -s XX

(6) Turned the state on in the website

    - Copy & pasted the YAML fragment into the state.yml file. 
    - Changed the state.md layout from 'page' to 'state.
    - Added qualitative analysis.

--------
