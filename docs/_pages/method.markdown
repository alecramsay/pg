---
layout: page
title: Method
permalink: method/
---

The method for generating baseline districts that [Todd Proebsting](http://proebsting.cs.arizona.edu/) & I 
developed evolved through an exploratory process:

-   I started trying to port Andrew Spann, Dan Gulotta, Daniel Kane's C code to Python. 
    But I could never quite get the solver to reliably work with multiple states.
-   When Todd got involved, he found and implemented Balzer's algorithm for computing Voronoi tessellations, 
    adapting it slightly to redistricting. With that in hand, we proceeded through a series of experiments.
-   First, we got Balzer to work with single pass, using various geographic granularities, e.g. blockgroups (BGs), blocks.
-   Then, to try to make the resulting maps stable -- invariant to specific starting points -- we generated maps by iterating on 
    BGs (100x), used those runs to find characteristic district centroids, and then did a final finish run using blocks. 
    Not surprisingly in retrospect, the block granularity resulted in a huge number of split precincts -- basically every precinct along every district boundary!
-   At that point, I realized that I was forgetting a redistricting fundamental -- that precincts (VTDs) are basically the atomic unit 
    of assignment, except when a few are split to achieve extreme population equality.
-   So I updated my scripts to iterate (100x) with precincts (instead of BGs) and then also used precincts in the finish run. 
    This resolved the split precincts problem, but introduced another one: stray precincts from one district were occassionally embedded within another adjacent district (near the shared boundary). IOW, the resulting districts for states were not always contiguous.
-   Another related issue was that, in a few cases -- notably LA and WA -- the shapes of states were significantly concave and
    districts spanned the concavity.
-   These issues prompted us modify the pure Balzer approach of randomly assigning the precincts to districts to assigning them 
    based on a real, contiguous map and then running Balzer on the precincts maintaining contiguity across all swaps. 
    Unfortunately, it seemed that this approach was very sensitive to the map chosen to establish the initial precinct-to-district assignments.
-   To regain the benefit of random seeds and multiple iterations, Todd created a multi-pass approach very similar to the one
    described below.
-   To generalize the approach to states with water-only precincts -- e.g., MD and MI -- I identified and removed them
    from the data and graphs. Todd's code did not have to change. That let us handle most other states.
-   However, we ultimately ran into issues with unpopulated land surrounding populated precincts, e.g., in KS, NV, and UT. 
    This prompted us to further revise the approach to zero population precincts which Todd's process had ignored. 
    Rather than remove them, we started assigning them infinitesimally small populations so they would be assigned to districts in the normal course of processing
    and connectivity would be maintained.
    
This is the method as it stands today (elliding I/O details) <<< TODO: flesh this out with Todd

-   Generate random district centroids ("sites", in Balzer terminology).
-   Assign each precinct to the nearest centroid. TODO - is this right? NOTE - The results may not be contiguous.
-   Run Balzer, to create an initial, population balanced, but not necessarily contiguous set of assignments with lowest energy.
-   Modify those assignments to make the districts contiguous but possibly not 'roughly equal' in population.
-   Run Balzer again, to create the lowest energy contiguous set of assignments, still possibly not 'roughly equal' in population.
-   Rebalance the assignments so that the districts remain contiguous and now are 'roughly equal' in population.
-   Run Balzer a third time, to create population balanced, contiguous, lowest energy assignments.
-   TODO: Consolidate -- What is the one-liner on what this does?
-   TODO: Complete -- Ditto

I used this solution in Step 4 of the overall workflow described [here](workflow.md).
