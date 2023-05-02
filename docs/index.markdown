---
layout: default
---

This site introduces a new concept for understanding & evaluating redistricting maps: baseline districts.

*Note: This web site is still a work in progress, but I've started to add preliminary results for some states.*

## Contents

- [Baseline Districts](#baseline-districts)
- [Study](#study)
- [Hypotheses](#hypotheses)
- [Plan](#plan)

## Baseline Districts

The "baseline districts" for a state are generated only using total census population. 
They characterize the "population geography" of a state, i.e., how many people live where.
Broadly speaking, they are the "least information" maps that maximize population compactness.
In physics terms, they can be thought of as minimizing the moment of inertia or energy.
The resulting districts are convex and not oddly shaped like other simple geometric approaches.

Map drawers use additional information -- demographic data, election results, municipal boundaries, etc. -- to, in effect,
stretch these baseline boundaries to achieve their desired mix of policy goals, e.g., more proportional, less county splitting, etc.
In other words, baseline districts are not only the implicit starting point -- *not* a blank canvas -- for redistricting a state,
they also illustrate tradeoffs inherent in a redistricting a state.

## Study

This study covers the 37 states apportioned three or more congressional districts in the 2020 census.[^1]

To generate the baseline maps presented here, we developed a heuristic approach for finding the lowest energy assignment of precincts to districts, given random starting points, and we ran this process 100 times for each state.
Then we selected the map that met the following criteria:

1. The lowest energy
2. That was contiguous
3. That didn't split any precincts, and
4. Had a population deviation within +/– 1% of the target district population.

The specifics of our heuristic approach are not main contribution of this study.
Nor are the specific baseline maps we generated, though we think they are strong contenders for the lowest energy maps.
The important contribution here is the idea of baseline districts and what they reveal about other maps, the tradeoffs inherent in a state\'s political geography.
If others can find lower energy maps that meet the four criteria above, that's great. Those should be considered the baseline instead.

This analysis uses maps drawn in Dave's Redistricting. Besides the
official maps used for the 2022 congressional elections, it uses the
five "notable maps" for each state that have the highest ratings for
proportionality, competitiveness, minority representation, compactness,
and county--district splitting.[^2] 

For [each state](./_pages/states.markdown), we compare these six maps to the baseline districts we generated.[^3]

### Hypotheses

The notable maps in DRA during the 2020 redistricting
cycle made it clear to me that there were tradeoffs between the five dimensions:
for example, the most proportional map might be less compact than the
most compact map, and vice versa.

Hence, two hypotheses motivated this research:

1.  There are well-defined "baseline districts" for a state that only
    depend on total census population -- While I introduced the concept
    several years ago,[^4] I had not developed an algorithm for
    generating them automatically.

2.  The districts for the notable maps for a state overlap significantly
    -- It seems obvious that -- barring extremely serpentine districts
    -- valid redistricting maps for a state *must* share common core
    areas. I wanted to show this empirically and visually, by comparing
    each map to the baseline map.[^5]

To the extent that the latter were true, it would confirm my intuition
that the essence of non-gerrymandering districting can be thought of as
the rubber band-like stretching of the boundaries of baseline districts
to achieve a mix of goals, e.g., more proportional, more competitive,
etc. In other words, the non-gerrymandering redistricting problem is
relatively constrained by the context of a state's political geography
and, even more fundamentally, it's population geography. In effect,
one effectively starts with baseline districts and modifies them.

### Plan

My plan mirrored the hypotheses:

1.  Develop an automated solution generating baseline districts \--
    Justin Levitt keyed me into the idea that baseline districts are
    maximally population compact (vs. geometric compact), based on
    physics concept of moment of inertia. Some searching led me to
    Andrew Spann, Dan Gulotta, Daniel Kane\'s work on the latter. Daniel
    Gulotta wrote a C++ implementation of their heuristic approach to
    support their paper \"Electoral Redistricting with Moment of Inertia
    and Diminishing Halves Models\" at MCM 07. My plan was to
    reimplement it in Python.

2.  Then compare each notable map to the baseline map -- Given the
    number of maps involved (222), I planned to develop a pipeline of
    tools to automate as much of the workflow as possible to produce the
    tabular and visual artifacts for this web site.

Of course, the latter depended on the former: without a well-defined,
defensible baseline map, there's no easy way to compare the notable maps
for a state.

I tried to reimplement Gulotta's C++ moment of inertia code in Python with
only partial success. Fortunately, I shared what I was working on with
Todd Proebsting, he got intrigued, and developed a solution, based on Balzer's work. 

---

### Footnotes

[^1]: I wrote the analytics portion of Dave\'s Redistricting (DRA). I
    would like to thank my DRA colleague Terry Crowley for the
    command-line tool support that made the scope of this project
    feasible, the DRA community for pushing the dimensional limits of
    congressional redistricting in each state with their Notable Maps,
    and Todd Proebsting for making baseline districts real by adapting
    Balzer's algorithm for generating capacity-constrained Vornonoi
    tessellations to redistricting.

[^2]: See "Notable Maps"
    \[https://medium.com/dra-2020/notable-maps-66d744933a48\].

[^3]: See GitHub \[https://github.com/proebsting/dccvt\].

[^4]: See "Baseline Congressional Districts: A Benchmark for Comparison"
    \[https://medium.com/redistricting-deep-dive/baseline-congressional-districts-a-benchmark-for-comparison-83b670608db3\].

[^5]: So, five comparisons instead of ten (5 choose 2).
