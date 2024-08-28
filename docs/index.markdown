---
layout: default

xx: "NC"
small-radar-width: 300
big-radar-width: 500
map-width: 700
---

<h2>Redistricting Trade-offs Illuminated</h2>

*Note: This site has been superceded by [Trade-offs in Redistricting](https://rdatools.github.io/tradeoffs/).*

Redistricting involves trade-offs between various policy objectives. 
The trade-offs that a state made in drawing their official 2022 congressional map are 
revealed by comparing it to the natural starting point for redistricting in that state. 
The range of alternatives that the mapmakers had are similarly highlighted using maps that optimize for 
proportionality, competitiveness, minority representation, compactness, and county-district splitting. 

{% assign xx = page.xx %}

<table style="border:0px">
    <tr>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Official_radar.png"
                alt="{{ site.data.maps[0].label }}" title="{{ site.data.maps[0].label }}"
                width="{{ page.small-radar-width }}" />
        </td>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Proportional_radar.png"
                alt="There is no most proportional map." title="{{ site.data.maps[1].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Competitive_radar.png"
                alt="There is no most competitive map." title="{{ site.data.maps[2].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
    </tr>
    <tr>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Minority_radar.png"
                alt="There is no best minority map." title="{{ site.data.maps[3].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Compact_radar.png"
                alt="There is no most compact map." title="{{ site.data.maps[4].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Splitting_radar.png"
                alt="There is no least splitting map." title="{{ site.data.maps[3].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
    </tr>
</table>

<p style="text-align: left"><small>Figure 1: The official and five notable maps for North Carolina compared to the root map</small></p>

That natural starting point for redistricting is a map where 
people who live near each other tend to be in the same district. 
For simplicity, we call this the **root map** or **root plan**.

You can see an example of this analysis on the [Example](./_pages/example.markdown) page, and 
you can pick a state to look at on the [States](./_pages/states.markdown) page.

A detailed description of and the rationale for our method is on the [How It Works](./_pages/details.markdown) page. 
Key terms are bolded and defined on the [Glossary](./_pages/glossary.markdown) page.