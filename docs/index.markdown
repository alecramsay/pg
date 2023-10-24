---
layout: default

xx: "NC"
small-radar-width: 300
big-radar-width: 500
map-width: 700
---

<h2>Trade-offs in Redistricting</h2>

Redistricting involves trade-offs between various policy objectives. 
The population geography of a state &#8212; how many people live where &#8212; frames these trade-offs. 
A mapmaker’s choices are revealed by comparing their map to the natural starting point for redistricting in that state.

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
        <img src="{{ baseline-png }}" alt="Root districts" title="Click to view the map in Dave's Redistricting"
            width="{{ page.map-width }}" />
    </a>
</p>
<p style="text-align: left"><small>Figure 1: The root congressional districts for North Carolina</small></p>


That natural starting point for redistricting is a map that is maximally population compact 
&#8212; people who live near each other tend to be in the same district. 
We call this a root map.

Other maps for a state can be described as deltas from it, 
like the points in a coordinate system are described relative to the origin. 
Root maps aren’t normative. 
The potential plans for a state are unavoidably informed by the root map 
which makes it a good baseline against which to compare them.

For each state, we compare the five [notable maps](https://medium.com/dra-2020/notable-maps-66d744933a48) 
in [Dave's Redistricting](https://davesredistricting.org/) (DRA) 
&#8212; which optimize for proportionality, competitiveness, minority representation, compactness, and county-district splitting &#8212; to the root map using 
the DRA [ratings](https://medium.com/dra-2020/ratings-deep-dive-c03290659b7)
that use a scale of [0--100] where bigger is always better. 
We do the same for the official map. 
These comparisons show some major quantifiable trade-offs inherent in congressional redistricting for a state.

You can see an example of this analysis on the [Example](./\_pages/example.markdown) page. 
You can choose a specific state to look at, on the [States](./\_pages/states.markdown) page.
A detailed description of and the rationale for our method is on the [Details](./\_pages/details.markdown) page. 
Key terms are defined on the [Glossary](./\_pages/glossary.markdown) page.

### Acknowledgements

We would like to thank DRA for the input data and the wonderful platform for sharing our maps, 
their user community for pushing the limits of congressional redistricting with their notable maps, 
the [VEST](https://dataverse.harvard.edu/dataverse/electionscience) team
for the election data making the partisan ratings possible, and 
Terry Crowley for making the large scope of this project feasible.