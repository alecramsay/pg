---
layout: default
---

This site illustrates three things:[^1]

1. Redistricting maps are constrained by a state's underlying "population geography," i.e., how many people live where. 
2. When you draw a redistricting map, you, in effect, distort the boundaries of the districts in this underlying political geography making tradeoffs between various policy objectives. Because of the underlying constraint, most maps share many of the same precinct assignments.
3. The underlying political geography can be used to characterize the tradeoffs for redistricting a state.

We show the tradeoffs inherent in congressional redistricting state by state,
for 42 states apportioned two or more congressional districts in the 2020 census.
Hawaii and Maine are excluded due to data issues.

We introduce a new concept &#8212; baseline districts &#8212; which are solely a function of total census population by precinct.
If you squint, the baseline districts for a state are a [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram),
the districts that maximize "population compactness" (as opposed to geometric compactness).
As such, baseline districts characterize the underlying "population geography" of a state
&#8212; i.e., how many people live where &#8212;
which constrain every other map to some degree. 

To understand the redistricting tradeoffs for a state, we compared the
the five [notable maps](https://medium.com/dra-2020/notable-maps-66d744933a48) 
from [Dave's Redistricting](https://davesredistricting.org/) (DRA) &#8212;
these maximize proportionality, competitiveness, minority representation, compactness, and county--district splitting 
&#8212; as well as the official map for each state to the baseline districts.
The contrasts put policy choices in bold relief.

You can see a representative example of this analysis on the [Example](./_pages/example.markdown) page.
You can choose a specific state to look at, on the [States](./_pages/states.markdown) page.
*Note: This is still a work in progress, but we've added the results for AZ, MD, NC, PA, and VA.*

The important results here are twofold:

1. The baseline districts for a state are the districts that maximize population compactness (minimize energy).[^3]
2. Redistricting a state involves inherent tradeoffs that can be *a priori* revealed by comparing policy-maximizing maps to the baseline districts.

The specifics of our heuristic approach to generating baseline districts are *not* the main contribution of this study.
Neither are the specific baseline maps we generated, though we think they are good proxies for the lowest energy maps for states and interesting in their own right.
If someone else can find a lower energy map for a state that meets the definitional constraints of a baseline map, great:
it should be considered the baseline instead.[^4]

One could use the same technique to analyze state legislative redistricting, though we haven't done that yet.

## Acknowledgements

Alec would like to thank his DRA colleague Terry Crowley for the
command-line tool support that made the large scope of this project feasible, 
the DRA user community for pushing the dimensional limits of
congressional redistricting in each state with their notable maps, 
and
Todd Proebsting for realizing the concept of baseline districts in code &#8212;
patiently persisting in the adaptation of Balzer's algorithm to redistricting with all its real world, 
complicating issues.

---

## Footnotes

[^1]: The name of this site &#8212; Redistricting Almanac &#8212; is a nod to FiveThirtyEight's magisterial
    [Atlas of Redistricting](https://medium.com/dra-2020/atlas-of-redistricting-maps-14ea4d0874e5). 
    The [Notable Maps](https://medium.com/dra-2020/notable-maps-66d744933a48) in DRA were directly inspired by the Atlas.
    We use the term "almanac" here instead, to suggest that this analysis could be updated periodically as new data are released,
    e.g., in 2030.

[^2]: Here "energy" means energy as Balzer defined it in formula 2.13 in "Capacity-Constrained Voronoi Tessellations: Computation and Applications." TODO: provide a link to the paper? a one-line summary of the formula?

[^3]: Baseline maps are the lowest energy maps that meet four constraints: complete, contiguous, doesn't split any precincts, and has a population deviation of 2% or less.

[^4]: You can even imagine a contest with prize money for finding the lowest energy map for a state.