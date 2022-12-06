---
layout: default
---

This project characterizes the redistricting tradeoffs inherent in a
state\'s political geography, using the 37 states apportioned three or
more congressional districts in the 2020 census.[^1]

*Note: This web site is all fleshed out and ready to go, but I'm waiting on baseline maps.
Check back in January--I hope to be able to start generating them then.*

### Background

This analysis uses maps drawn in Dave's Redistricting. Besides the
official maps used for the 2022 congressional elections, it uses the
five "notable maps" for each state that have the highest ratings for
proportionality, competitiveness, minority representation, compactness,
and county--district splitting.[^2]

It compares them to "baseline districts" which are algorithmically drawn
only using total census population.[^3] These are "least information"
maps that maximize population compactness. The resulting districts are
convex and not oddly shaped like other simple geometric approaches. Maps
that maximize one of notable dimensions, such as partisan
proportionality or opportunity for minority representation, necessarily
include more data, such as past elections or race & ethnicity,
respectively.

### Hypotheses

Comparing other maps to the notable maps during the 2020 redistricting
cycle made clear that there were tradeoffs between the five dimensions:
for example, the most proportional map might be less compact than the
most compact map, and vice versa.

Two hypotheses motivated this research:

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
and, even more fundamentally, it's population geography.

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
Todd Proebsting, he got intrigued, and developed a theoretically sound
solution, based on Balzer's work. 

### Results

TBD: More ...

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

[^3]: See GitHub \[https://github.com/proebsting/balzer\].

[^4]: See "Baseline Congressional Districts: A Benchmark for Comparison"
    \[https://medium.com/redistricting-deep-dive/baseline-congressional-districts-a-benchmark-for-comparison-83b670608db3\].

[^5]: So, five comparisons instead ten (5 choose 2).
