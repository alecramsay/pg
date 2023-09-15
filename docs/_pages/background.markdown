---
layout: page
title: Background
permalink: background/
---

This page explains what we did and why we did it.

## Contents

- [Motivation](#motivation)
- [Concept](#concept)
- [Plan](#plan)
- [Scope](#scope)
- [Method](#method)
- [Data](#data)
- [Code](#code)

## Motivation

The [notable maps](https://medium.com/dra-2020/notable-maps-66d744933a48) in 
[Dave's Redistricting](https://davesredistricting.org/) (DRA)
are the published maps that maximize five rated dimensions: 
proportionality, competitiveness, minority representation, compactness, and county--district splitting.
For the 2020 congressional redistricting cycle, these maps demonstrated that there were tradeoffs between these objectives.
For example, the most proportional map for a state might be less compact than the
most compact map one, and vice versa.

This led to the two hypotheses that motivated this research:

1.  In contrast to the notable and official maps that use a broad spectrum of data,
    Alec's first hypothesis was that
    there are well-defined "baseline districts" for a state that only
    depend on total census population &#8212; While he had introduced the concept
    several years ago,[^1] he had not written code to generate them automatically.

2.  Alec's second hypothesis was that
    the districts for the notable maps for a state overlap significantly. 
    It seems obvious that &#8212; barring extremely serpentine districts &#8212; valid redistricting maps 
    for a state *must* share common core areas because of the underlying "population geography" for a state,
    i.e., how many people live where.
    This is precisely what is characterized by our baseline districts.
    Alec wanted to show this empirically and visually, by comparing each map to the baseline map.[^2]

To the extent that the latter were true, it would formalize Alec's intuition
that the essence of redistricting can be thought of as
the rubber band-like stretching of the boundaries of baseline districts
to achieve a mix of policy goals, e.g., partisan fairness, competitiveness, etc.
In other words, redistricting is relatively constrained by the context of a state's population geography.
Perhaps implicitly, one effectively has to start with the baseline districts and modify their boundaries.

## Concept

We define the baseline map for a state to be contigous, 'roughly equal' population districts
that are soley a function of total census population by precinct.
Moreover, they are the *least information* maps &#8212; all other maps incorporate more information 
into their district boundaries.
Conceptually, baseline districts are the [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram)
for a state.[^3]
In physics terms, baseline districts can be thought of as minimizing the moment of inertia or energy, or
more informally, the districts that maximize "population compactness."
The resulting districts are convex and not oddly shaped like other simple geometric approaches.
Baseline districts characterize the "population geography" of a state, i.e., how many people live where.

Map drawers use lots of additional information &#8212; demographic data, election results, 
municipal boundaries, etc. &#8212; to, in effect,
stretch these baseline boundaries to achieve their desired mix of policy goals, e.g., more 
proportional, less county splitting, etc.
Consequently, baseline districts are not only the implicit starting point for redistricting a state
&#8212; redistricting does *not* start with a blank canvas! &#8212; but
baseline districts can also be used to illustrate the tradeoffs inherent in redistricting a state.

## Plan

Alec's plan mirrored his hypotheses:

1.  First, develop an automated method for generating baseline districts &#8212;
    Justin Levitt had keyed him into the idea that baseline districts are
    maximally population compact (vs. geometrically compact), based on
    physics concept of moment of inertia. Some searching led Alec to
    Andrew Spann, Dan Gulotta, Daniel Kane\'s work on the latter. Daniel
    Gulotta wrote a C++ implementation of their heuristic approach to
    support their paper \"Electoral Redistricting with Moment of Inertia
    and Diminishing Halves Models\" at MCM 07. Alec's plan was to simply
    reimplement it in Python.

2.  Then compare each notable & official map to the baseline map for the state &#8212; Given the
    number of maps involved (252 = 42 x 6), Alec planned to develop a pipeline of
    tools to automate as much of the workflow as possible to produce the artifacts for this web site.

Of course, the latter depended on the former: without a well-defined,
defensible baseline map, there would be no easy way to compare the notable maps for a state.

## Scope

Alec chose to study the states apportioned two or more congressional districts in the 2020 census.
Hawaii and Maine had to be skipped due to data issues, leaving 42 states in the study.

This analysis uses maps drawn in Dave's Redistricting. 
Besides the official maps used for the 2022 congressional elections, 
it uses the five notable maps for each state that have the highest ratings for
proportionality, competitiveness, minority representation, compactness,
and county--district splitting.
While these are not definitively the *best* on their respective dimensions (i.e., globally optimal),
DRA users work hard to find maps that optimize these dimensions and have their
map be selected as the notable map, so they are good proxies for maps that
maximize these dimensions.
As such, they serve to illustrate the tradeoffs between these dimensions in a state.

For each state, we compare these six maps to the baseline districts we generated.

## Method 

At first Alec tried to reimplement Gulotta's C++ moment of inertia code in Python 
but met with only partial success. Fortunately, he shared what he was working on with his friend,
Todd Proebsting, he got intrigued, and then Todd developed a solution based on 
Balzer's [Capacity-Constrained Voronoi Tessellations: Computation and Applications](TODO).
The evolution of our heuristic approach for finding the lowest energy assignment of precincts to districts 
is described [here](./method.markdown).

To generate the baseline maps presented here, we ran this process 100 times for each state
using random starting points and the 2020 Census VTD shapes and population data.[^4]
Then we selected the lowest energy map that met four constraints:

1. Complete -- all precincts assigned to districts
2. Contiguous
3. Didn't split any precincts, and
4. Had a population deviation of 2% or less.

The specifics of our heuristic approach are *not* main contribution of this study.
Nor are the specific baseline maps we generated, though we think they are strong contenders for the lowest energy maps
and interesting in their own right.
The important contribution here is the *idea* of baseline districts and what they reveal about other maps, 
the tradeoffs inherent in a state\'s political geography.

## Data

The data used came from two sources.

DRA data:

-   The block-assignment files for the official and notable maps were exported from DRA on 10/06/22. 
    A few of the maps violated basic requirements (like contiguity) and were replaced by the next best maps that didn't.
-   Block, blockgroup, and tract-level census data were downloaded from the dra2020/dra-data repository on 10/06/22.
-   VTD-level census data came from https://github.com/dra2020/vtd_data on 10/06/22.

Census data:

- The block shapes were downloaded from [https://www2.census.gov/geo/tiger/TIGER2020/TABBLOCK20/](https://www2.census.gov/geo/tiger/TIGER2020/TABBLOCK20/) on 10/06/22.
- The VTD shapefiles come from [https://www2.census.gov/geo/tiger/TIGER2020PL/LAYER/VTD/2020/](https://www2.census.gov/geo/tiger/TIGER2020PL/LAYER/VTD/2020/).
- The precint (VTD) to block mapping files come from [https://www.census.gov/geographies/reference-files/time-series/geo/block-assignment-files.html](https://www.census.gov/geographies/reference-files/time-series/geo/block-assignment-files.html).
- The Name Lookup tables for friendly precinct (VTD) names are from [https://www.census.gov/geographies/reference-files/time-series/geo/name-lookup-tables.html](https://www.census.gov/geographies/reference-files/time-series/geo/name-lookup-tables.html)

Due to the size of these files, none are stored in a GitHub repository, except the block-assignment files.

## Code 

This site was developed using the code in three GitHub repositories:

-   Alec's [pg repository](https://github.com/alecramsay/pg)
-   Alec's [baseline repository](https://github.com/alecramsay/baseline), and
-   Todd's [dccvt repository](https://github.com/proebsting/dccvt)

The site is homed in the first.
The code in that repository uses the code in the other two to generate baseline maps, and
analyze the official and notable maps relative to them.

---

## Footnotes

[^1]: See "Baseline Congressional Districts: A Benchmark for Comparison"
    \[https://medium.com/redistricting-deep-dive/baseline-congressional-districts-a-benchmark-for-comparison-83b670608db3\].

[^2]: So, five comparisons instead of ten (5 choose 2).

[^3]: It turns out, one cannot simply run a Voronoi algorithm over the precincts. There are lots of practical issues 
    and real-world complications to deal with. See GitHub \[https://github.com/proebsting/dccvt\].

[^4]: CA, OR, and WV don't have VTDs, so we used blockgroups instead like DRA. Also, the official Florida data is pretty messed up, so we used DRA's GeoJSON file of corrected Florida VTDs.
