---
layout: page
title: DRA CLI
permalink: dra-cli/
---

This page describes the DRA capabilities that I (Alec) took advantage of in developing the content for this site.

### Metadata

- Enumerate GUIDs for official maps by state and type of map -- from data/state_plans.json; I copied this structure.
- Enumerate GUIDs for notable maps by state and type of map -- ditto
- Enumerate # of districts by state and type of map -- from dra-types/lib/stateinfo.ts; I copied this structure.

### CLI Commands

- Duplicate a map by GUID -- I duplicated all of the official & notable maps *en masse* [(1 + 5) x 42 => 252].
- Export the block-assignment file for a map by GUID -- after inspecting each notable map and confirming that it didn't have any problems, I exported a block-assignment file for it in the UI; we could have generated these at the command-line using a little known feature [(1 + 5 + 1) x 42 => 294].
- Import a CSV, setting many map properties, getting the resulting map & access GUIDs -- I generated baseline maps for 42 states and imported them at the CLI.
- Edit map settings by GUID -- I set core display properties for each map at the CLI [(7 + 6) x 42 => 546].
- Save a map image -- this is the right-click Chrome hack. This capability is *not* currently exposed at the DRA CLI, but we figured out how to replicate the feature at the command line.
- Pull ratings for a map by GUID -- I pulled ratings for each map at the CLI [(7 + 6) x 42 => 546].

Altogether, I generate 85 artifacts per state or 3,570 in total, 
of which 1,092 are visible (the rest intermediate/restart files).