---
layout: page
title: Baseline Workflow
permalink: baseline-workflow/
---

This page describes the workflow for generating a baseline map for a state, using the code
in Alec's [baseline repository](https://github.com/alecramsay/baseline) which in turn uses the
code in Todd's [dccvt repository](https://github.com/proebsting/dccvt).

## Summary

-   Download files
-   Create output directories
-   Extract precinct data
-   Extract a graph of precincts
-   Generate candidate baselines
-   Compare the candidate maps, and
-   Choose a baseline

## Download files


The data for VTDs (precincts) came from these sources:

-   The VTD census data came from https://github.com/dra2020/vtd_data.
-   The VTD shapefiles come from https://www2.census.gov/geo/tiger/TIGER2020PL/LAYER/VTD/2020/.
-   The precint (VTD) to block mapping files come from https://www.census.gov/geographies/reference-files/time-series/geo/block-assignment-files.html.
-   The Name Lookup tables for friendly precinct (VTD) names are from https://www.census.gov/geographies/reference-files/time-series/geo/name-lookup-tables.html

[//]: # (Block assignments -- https://www.census.gov/geographies/reference-files/time-series/geo/block-assignment-files.html)

## Create output directories

-   baseline/data/XX
-   baseline/intermediate/XX
-   baseline/maps/XX

## Extract & format data

Extract the population & coordinates of precincts and put it into the format that Todd's dccvt package expects.

```
scripts/extract_data.py -s XX
```

## Extract a graph of precincts

Similarly, extract a graph of the precincts and put them into the format that Todd's dccvt package expects.

```
scripts/extract_graph.py -s XX
```

## Generate candidate baselines

Use the baseline_state.py script to generate 100 baseline candidates.

```
scripts/baseline_state.py -s XX -i 100 -v > intermediate/XX/XX20C_log_100.txt
```

## Compare the candidate maps

Use the compare_maps.py script to compare them.

```
scripts/compare_maps.py -s XX -i 100 -v
```

-   Copy any missing maps output to maps/XX/XX20C_missing.txt.
-   Import XX20C_candidates.csv into a spreadheet, and verify that the results are OK.

## Choose a baseline

Designate the lowest energy contiguous candidate with population deviation <= 2% (+/– 1%) as the baseline.

-   Copy it to the maps/XX directory as XX20C_baseline_100.csv.


The specific workflow for each state -- along with command arguments -- are in the workflows/ directory of Alec's baseline repository.
