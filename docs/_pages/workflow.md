---
layout: page
title: Overall Workflow
permalink: workflow/
---

This note describes the workflow that Alec used for creating the artifacts for this website:

(1) Exported block-assignment files for the official &amp; notable maps in DRA

Then, for each state:

(2) Created a baseline map using [the 'baseline' workflow](./baseline_workflow.markdown) 

(3) Analyzed the official & notable maps relative to the baseline map

    - scripts/analyze_state_part1.py -s XX
    - scripts/analyze_state_part2.py -s XX

(4) Deployed the artifacts

    - scripts/DEPLOY.py -s XX

(5) Turned the state on in the website

    - Copy & pasted the YAML fragment into the state.yml file
    - Changed the state.md layout from 'page' to 'state'
    - Added qualitative analysis

