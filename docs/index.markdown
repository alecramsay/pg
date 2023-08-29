---
layout: default

xx: "NC"
small-radar-width: 300
big-radar-width: 500
map-width: 700
---

This site characterizes policy tradeoffs inherent in congressional redistricting state by state.[^1]
In contrast to the *Compare* feature in [Dave's Redistricting](https://davesredistricting.org/) (DRA) 
&#8212; which compares a given map to maps that optimize for 
proportionality, competitiveness, opportunity for minority representation, compactness, and county-district splitting &#8212; 
we compare these five policy-maximizing maps and the official map to a common baseline set of districts
to illustrate some major quantifiable policy tradeoffs for congressional redistricting in each state.

By our definition (elaborated below), each state has exactly one baseline plan. 
These are the baseline districts for North Carolina.

{% assign xx = page.xx %}

{% capture baseline-png %}
{{ site.baseurl }}/assets/images/{{ xx }}_2020_Congress_Baseline_map.png
{% endcapture %}
{% assign baseline-png = baseline-png | strip_newlines %}

{% assign state = site.data.states | where:"xx", xx | first %}

{% capture baseline-link %}
https://davesredistricting.org/join/{{ state["baseline"] }}
{% endcapture %}
{% assign baseline-link = baseline-link | strip_newlines %}

<p style="text-align: left">
    <a href="{{ baseline-link }}">
        <img src="{{ baseline-png }}" alt="Baseline districts" title="Click to view the map in Dave's Redistricting"
            width="{{ page.map-width }}" />
    </a>
</p>

Our analysis is built on a set of ideas:

1.  We call the distribution and concentration of where people live in a state its "population geography" and claim that 
    a state's unique population geography can be characterized in a well-defined set of districts that satisfy basic legal constraints, 
    i.e., districts are contiguous and have 'roughly equal' populations.
    We call these "baseline districts." 
    Since they only depend on population, baseline maps are the "least information" redistricting plans for states.[^2] 
2.  Because valid redistricting plans must have 'roughly equal' populations, they are, to a large degree, constrained by this underlying population geography. 
    The boundaries of baseline districts can only be distorted so much before they become visibly engineered towards specific, typically partisan and/or racial, ends. 
    Hence, even when a plan optimizes on one policy dimension, such as proportionality, 
    it tends to share many of the same precinct assignments as the baseline map producing identifiable "district cores."
3.  Conversely, because mapmakers use considerable data &#8212; e.g., voting age population, demographics, past election results, etc. &#8212; to draw districts that 
    reflect their preferred mixes of policy objectives, the boundaries in such a "high information" plans reflect that data and those decisions.
4.  Moreover, due to the complex *blend* of demographic, economic, cultural, and political attributes determined by a state's underlying population geography, 
    redistricting often involves *tradeoffs* between various policy objectives, 
    such as proportionality, competitiveness, opportunity for minority representation, compactness, and county-district splitting, among others. 
    Sometimes two macro goals can be pursued in tandem, but often they are in tension with each other. 
    For example, a plan that maximizes proportionality might not be very compact, or vice versa.
5.  Finally, because the tradeoffs ultimately depend on states' population geographies &#8212;
    which are established definitively for a decade by the decennial census &#8212; 
    these tradeoffs can be characterized *a priori*.

We characterize some major quantifiable policy tradeoffs for congressional redistricting 
for 42 states apportioned two or more congressional districts in the 2020 census.[^3]

## Summary

We introduce a new concept &#8212; baseline districts &#8212; which are solely a function of total census population by precinct.
Roughly speaking, the baseline districts for a state form a [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram),
the districts that maximize "population compactness" (as opposed to geometric compactness).
Baseline districts characterize the underlying "population geography" of a state &#8212; i.e., how many people live where &#8212;
which constrains every other valid map to some degree. 

To illustrate the inherent redistricting tradeoffs for states, we compared the
the five [notable maps](https://medium.com/dra-2020/notable-maps-66d744933a48) for each state from DRA
&#8212; these optimize proportionality, competitiveness, minority representation, compactness, and county--district splitting &#8212; 
as well as the official map for each state to the baseline districts.
These contrasts put policy choices in bold relief.

You can see a representative example of this analysis on the [Example](./_pages/example.markdown) page.
You can choose a specific state to look at, on the [States](./_pages/states.markdown) page.

*Note: This site is still a work in progress, but you can see this analysis applied to NC, VA, and CO.*

We encourage two overarching takeaways:

1. The baseline districts for a state should be the districts that maximize population compactness (minimize energy),[^4] and
2. Redistricting a state involves inherent tradeoffs that can be *a priori* revealed by comparing policy-maximizing maps to these baseline districts.

The specifics of our heuristic approach to generating baseline districts are *not* the main contribution of this study.
Neither are the specific baseline maps we generated, though we think they are good proxies for the lowest energy maps for states and interesting in their own right.
If someone else can find a lower energy map for a state that meets the definitional constraints of a baseline map, great:
it should be considered the baseline instead.[^5]

You can find more details about our approach in the [Background](./_pages/background.markdown) page.

## Future Research

We imagine many potential areas of future research, including:

-   Finding lower energy baselines using our approach 
-   Varying some aspect of our approach 
    &#8212; one can imagine many [variations](./_pages/variations.markdown) 
-   Exploring baseline districts as the seed maps for generating large ensembles of maps
-   Using the same technique to analyze state legislative redistricting

## Acknowledgements

Alec would like to thank his DRA colleague Terry Crowley for making the large scope of this project feasible and
the DRA user community for pushing the dimensional limits of congressional redistricting in each state with their notable maps.

---

## Footnotes

[^1]: The name of this site &#8212; Redistricting Almanac &#8212; is a nod to FiveThirtyEight's magisterial
    [Atlas of Redistricting](https://medium.com/dra-2020/atlas-of-redistricting-maps-14ea4d0874e5). 
    The [notable maps](https://medium.com/dra-2020/notable-maps-66d744933a48) in DRA were directly inspired by the Atlas.
    We use the term "almanac" here instead, to suggest that this analysis could be updated periodically as new data are released,
    e.g., in 2030.

[^2]: We use the terms "map" and "plan" interchangeably.

[^3]: We excluded Hawaii and Maine, due to data issues.

[^4]: Here "energy" means energy as Balzer defined it in formula 2.13 in "Capacity-Constrained Voronoi Tessellations: Computation and Applications." TODO: provide a link to the paper? a one-line summary of the formula?

[^5]: You can even imagine a contest with prize money for finding the lowest energy map for a state.
