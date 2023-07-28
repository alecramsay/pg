---
layout: page
title: Canonicalizing District IDs
permalink: workflow_canonical_districts/
---

This note describes how we could canonicalize district ids.

### Existing Maps

Right now, we have created official maps, five notable maps, and baseline maps for each of 42 states.
For all except the baselines, we have a block-assignment file and a map in DRA.
For baseline maps, we also have a precinct-assignment file, the result of the baseline process.
The district ids in the assignment files are not canonicalized.

To preserve the work done so far but canonicalize the district ids on the ids in the official maps, we could do the following.
For the official map and each of the other maps:

- Run a script to produce a from/to map of district ids for the map -- Todd would need to write this script.
- Run a script to update the district ids in the DRA map -- Terry would need to write this script.
- Run a script to update the district ids in the block-assignment file -- I could write this script.

I could also write a meta script that would generate the script calls for each map and state, so this could all be done with a single command.

Note: This would *not* canonicalize the district ids in the input precinct-assignment files for the baseline maps.

- Then the revised analysis script (Step 8) could be run. It has to be run for each state regardless.

The resulting district intersections ("cores") assignment files would now have canonicalized district ids.

- Finally, the images for each of the updated maps could be re-generated (Step 7).

### New Baseline Map

The process for adopting a new baseline map for a state could be:

- Run the script to produce a from/to map of district ids for the map
- Run the script to update the district ids in the block-assignment file
- Import the block-assignment file into DRA (Step 5)
- Repeat the rest of the workflow as before (Steps 6-8)

Note: At the moment, there's no notion of versioning for the baseline maps.
So this would *replace* the artifacts for the previous baseline map.
Item #26 in GitHub is a tracking issue to remedy this.
