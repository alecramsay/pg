---
layout: default
---

This site introduces a new concept -- baseline districts -- and uses it to illustrate the tradeoffs inherent redistricting a state.[^1]

*Note: This web site is still a work in progress, but I've started to add preliminary results for some states.*

## Contents

- [Motivation](#motivation)
- [Concept](#concept)
- [Plan](#plan)
- [Scope](#scope)
- [Method](#method)
- [Example](#example)

## Motivation

[Dave's Redistricting](https://davesredistricting.org/) (DRA) has the notion of 
[Notable Maps](https://medium.com/dra-2020/notable-maps-66d744933a48): 
the maps that maximize the five rated dimensions: 
proportionality, competitiveness, minority representation, compactness, and county--district splitting.
The notable maps for the 2020 congressional redistricting cycle 
made clear to me that there were tradeoffs between the five dimensions:
that the most proportional map might be less compact than the
most compact map, and vice versa, for example.

Two hypotheses motivated this research:

1.  In contrast to the notable and official maps that use a broad spectrum of data,
    my first hypothesis was that
    there are well-defined "baseline districts" for a state that only
    depend on total census population -- While I introduced the concept
    several years ago,[^5] I had not developed an algorithm for
    generating them automatically.

2.  My second hypothesis was that 
    the districts for the notable maps for a state overlap significantly. 
    It seems obvious that – barring extremely serpentine districts – valid redistricting maps 
    for a state *must* share common core areas because of the underlying "population geography"
    characterized by the baseline districts.
    I wanted to show this empirically and visually, by comparing each map to the baseline map.[^6]

To the extent that the latter were true, it would formalize my intuition
that the essence of non-gerrymandering districting can be thought of as
the rubber band-like stretching of the boundaries of baseline districts
to achieve a mix of policy goals, e.g., more proportional, more competitive,
etc. In other words, the non-gerrymandering redistricting problem is
relatively constrained by the context of a state's political geography
and, even more fundamentally, by it's population geography. In effect,
one effectively must start with the baseline districts and modify them.

## Concept

The baseline districts for a state are the contigous, 'roughly equal' population districts
that are soley a function of total census population by precinct.
Consequently, they are the *least information* maps--all other maps incorporate more information 
into their district boundaries.
Conceptually, they are the districts in the [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram)
for a state, i.e., the districts that maximize population compactness.[^7]
In physics terms, baseline districts can be thought of as minimizing the moment of inertia or energy.
The resulting districts are convex and not oddly shaped like other simple geometric approaches.
Baseline districts characterize the "population geography" of a state, i.e., how many people live where.

Map drawers use lots of additional information -- demographic data, election results, municipal boundaries, etc. -- to, in effect,
stretch these baseline boundaries to achieve their desired mix of policy goals, e.g., more proportional, less county splitting, etc.
In other words, baseline districts are not only the implicit starting point for redistricting a state
-- *not* a blank canvas -- but
they can also illustrate the tradeoffs inherent in a redistricting a state.

## Plan

My plan mirrored my hypotheses:

1.  First, develop an automated method for generating baseline districts \--
    Justin Levitt keyed me into the idea that baseline districts are
    maximally population compact (vs. geometric compact), based on
    physics concept of moment of inertia. Some searching led me to
    Andrew Spann, Dan Gulotta, Daniel Kane\'s work on the latter. Daniel
    Gulotta wrote a C++ implementation of their heuristic approach to
    support their paper \"Electoral Redistricting with Moment of Inertia
    and Diminishing Halves Models\" at MCM 07. My plan was to
    reimplement it in Python.

2.  Then compare each notable & official map to the baseline map for the state -- Given the
    number of maps involved (222), I planned to develop a pipeline of
    tools to automate as much of the workflow as possible to produce the
    tabular and visual artifacts for this web site.

Of course, the latter depended on the former: without a well-defined,
defensible baseline map, there's no easy way to compare the notable maps
for a state.

## Scope

I chose to study the 37 states apportioned three or more congressional districts in the 2020 census.[^2]

This analysis uses maps drawn in Dave's Redistricting. 
Besides the official maps used for the 2022 congressional elections, 
it uses the five notable maps for each state that have the highest ratings for
proportionality, competitiveness, minority representation, compactness,
and county--district splitting.[^3] 

For [each state](./_pages/states.markdown), I compare these six maps to the baseline districts I generated.[^4]

## Method 

I tried to reimplement Gulotta's C++ moment of inertia code in Python with
only partial success. Fortunately, I shared what I was working on with
Todd Proebsting, he got intrigued, and then developed a solution based on 
[Balzer's work](Capacity-Constrained Voronoi Tessellations: Computation and Applications).
The evolution of our heuristic approach for finding the lowest energy assignment of precincts to districts 
is described [here](./_pages/method.markdown).

To generate the baseline maps presented here, we ran this process 100 times for each state
using random starting points.
Then we selected the map that met the following criteria:

1. The lowest energy
2. That was contiguous
3. That didn't split any precincts, and
4. Had a population deviation within +/– 1% of the target district population.

The specifics of our heuristic approach are not main contribution of this study.
Nor are the specific baseline maps we generated, though we think they are strong contenders for the lowest energy maps
and interesting in their own right.
The important contribution here is the *idea* of baseline districts and what they reveal about other maps, the tradeoffs inherent in a state\'s political geography.
If someone else can find a lower energy map for a state that meets the four criteria above, that's great. 
It should be considered the baseline instead.

## Example

You can see a representative example of the analysis that baseline districts enable 
on the [Example](./_pages/example.markdown) page.

---

## Footnotes

[^1]: The name of this site -- Redistricting Almanac -- is a hat tip to FiveThirtyEight's magisterial
    [Atlas of Redistricting](https://medium.com/dra-2020/atlas-of-redistricting-maps-14ea4d0874e5). 
    The [Notable Maps](https://medium.com/dra-2020/notable-maps-66d744933a48) in DRA were directly inspired by the Atlas.
    I use the term "almanac" instead, to suggest that this analysis could be updated periodically as new data are released,
    e.g., in 2030.

[^2]: I wrote the analytics portion of Dave\'s Redistricting (DRA). I
    would like to thank my DRA colleague Terry Crowley for the
    command-line tool support that made the scope of this project
    feasible, the DRA community for pushing the dimensional limits of
    congressional redistricting in each state with their Notable Maps,
    and Todd Proebsting for making baseline districts real by adapting
    Balzer's algorithm for generating capacity-constrained Vornonoi
    tessellations to redistricting.

[^3]: See "Notable Maps"
    \[https://medium.com/dra-2020/notable-maps-66d744933a48\].

[^4]: See GitHub \[https://github.com/proebsting/dccvt\].

[^5]: See "Baseline Congressional Districts: A Benchmark for Comparison"
    \[https://medium.com/redistricting-deep-dive/baseline-congressional-districts-a-benchmark-for-comparison-83b670608db3\].

[^6]: So, five comparisons instead of ten (5 choose 2).

[^7]: It turns out, one cannot simply run a Voronoi algorithm over the precincts. There are lots of practical issues 
    and real-world complications to deal with.
