---
layout: default

xx: "NC"
small-radar-width: 300
big-radar-width: 500
map-width: 700
---

<h2>Population Geography &amp; Redistricting Trade-offs</h2>

We explore two ideas here:

-   The population geography of a state characterized as a set of
    > districts is the natural starting point of redistricting -- all
    > redistricting plans for a state are informed by it; and

-   Comparing redistricting plans to it highlights the mix of policy
    > choices (trade-offs) that the mapmakers made.

where by population geography we mean how many people live where in a state.

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
Figure 1: The root congressional districts for North Carolina

Specifically:

1.  We introduce the concept of a **root plan** or **root map** that
    > characterizes a state's unique **population geography** as a set
    > of districts. They are solely a function of total census
    > population by geographic unit (**block** or **precinct**). We
    > don't incorporate other criteria, such as preserving city or
    > county boundaries, because the point is to abstract away any
    > political considerations.\
    > \
    > **Bolded** terms are defined on the
    > \[Definitions](./\_pages/definitions.markdown) page.

2.  We hypothesize that maximizing **population compactness** is a good
    > heuristic for generating a proximal root map. Roughly speaking,
    > the resulting districts form a
    > \[Voronoi diagram\](https://en.wikipedia.org/wiki/Voronoi_diagram).

> We impose three additional constraints on our approximation:

-   Each district is contiguous

-   No precincts are split, and

-   Population deviation is 2% or less

> From an initial, random districting, our algorithm greedily searches
> for the most population-compact districting. Because this algorithm is
> not guaranteed to find the best districting, we run it 100 times and
> take the best qualifying map.
>
> By this definition, each state has exactly one root map.

3.  We generate root maps for 42 states apportioned two or more
    > congressional districts in the 2020 census. We exclude Hawaii and
    > Maine, due to data issues.

4.  We compare these root maps to the five \[**notable maps**\](https://medium.com/dra-2020/notable-maps-66d744933a48)
    > from Dave's Redistricting (DRA)
    > for each state that individually optimize for proportionality,
    > competitiveness, minority representation, compactness, and
    > county-district splitting.

5.  Despite optimizing on these different dimensions, these maps share
    > substantial **district cores** with the root map, an average of
    > nearly two thirds of the population-weighted assignments (65.9%).
    > This reinforces our hypothesis that maximizing the overall
    > population compactness of districts is a good way to characterize
    > population geography.

6.  Then we compare the DRA
    > \[**ratings**\](https://medium.com/dra-2020/ratings-deep-dive-c03290659b7)
    > for these divergent maps to those for the root map showing some
    > major quantifiable policy trade-offs inherent in congressional
    > redistricting for each state. These contrasts put policy choices
    > framed by the underlying population geography in sharp relief.\
    > \
    > Our root maps are not normative, not what we think redistricting
    > plans *should* be. By definition, they are the natural starting
    > point of redistricting. All redistricting plans for a state are
    > unavoidably informed by them, so they provide a good baseline
    > against which to evaluate and compare plans.

7.  Finally, we compare the official map for each state to the root
    > districts showing the mix of policy choices (trade-offs) that each
    > state made.

You can see a representative example of this analysis on the
\[Example\](./\_pages/example.markdown) page. You can choose a specific
state to look at, on the \[States\](./\_pages/states.markdown) page.

**Next Steps**

Going forward, we want to test two further hypotheses:

1.  Root maps are relatively robust and relatively invariant to the
    > specific approach used to generating approximations -- We have
    > used Balzer's capacity-constrained Voronoi tessellations. We want
    > to a) explore alternate distance functions for our Balzer's
    > Voronoi algorithm and b) explore rectangular tilings.

2.  Our population compactness heuristic and its variants (from #1) are
    > among the maps with the largest district cores with respect to
    > other maps in a large ensemble of randomly generated maps for a
    > state.

**Acknowledgements**

We would like to thank Dave\'s Redistricting for the input data
and the wonderful platform for sharing our maps and the DRA user
community for pushing the dimensional limits of congressional
redistricting in each state with their notable maps. We would like to
especially thank Terry Crowley for making the large scope of this
project feasible.