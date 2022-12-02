---
layout: page
title: Example
permalink: example/

xx: "NC"
small-radar-width: 300
big-radar-width: 500
map-width: 700
---

This is an annotated example of the analysis of a state's political geography, using North Carolina as an example.
There is a separate page for each state. 

At the top is a summary of what the various exhibits reveal. That is not shown here.

{% assign xx = page.xx %}

<!-- RADAR DIAGRAMS -->

<h3>Radar Diagrams</h3>

Then there are a set of pairwise radar diagrams. They compare six comparison maps -- the Official map and the five Notable Maps that maximizing proportionality, competitiveness, minority representation, compactness, and splitting -- to the baseline map for the state.

<table style="border:0px">
  <tr>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Official_radar.png" alt="{{ site.data.maps[0].label }}" title="{{ site.data.maps[0].label }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Proportional_radar.png" alt="{{ site.data.maps[1].qualified-label }}" title="{{ site.data.maps[1].qualified-label }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Competitive_radar.png" alt="{{ site.data.maps[2].qualified-label }}" title="{{ site.data.maps[2].qualified-label }}" width="{{ page.small-radar-width }}"/>
    </td>
  </tr>
  <tr>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Minority_radar.png" alt="{{ site.data.maps[3].qualified-label }}" title="{{ site.data.maps[3].qualified-label }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Compact_radar.png" alt="{{ site.data.maps[4].qualified-label }}" title="{{ site.data.maps[4].qualified-label }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Splitting_radar.png" alt="{{ site.data.maps[3].qualified-label }}" title="{{ site.data.maps[3].qualified-label }}" width="{{ page.small-radar-width }}"/>
    </td>
  </tr>
</table>

<!-- RATINGS -->

{% capture ratings-file %}
{{ xx }}_2022_Congress_ratings
{% endcapture %}
{% assign ratings-file = ratings-file | strip_newlines %}

{% assign ratings = site.data[ratings-file] %}

<h3>Ratings</h3>

Then the ratings are shown in tabular form for convenience.

<table>
  {% for row in ratings %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>

<!-- MAPS TABS -->

<h3>Maps</h3>

At the bottom are a set of tabs, one for each of the six comparison maps. For each map, there is: 

* a pairwise radar diagram
* the map with the baseline district lines overlaid on it, 
* a map of the regions formed by intersecting the district boundaries of the two maps, and
* a table showing data for each region

Note: The "BASELINE" and "OTHER" columns shows the districts that intersect to form the region.
The first is the district in the baseline map, and the second is the district in the comparison map.

<script src="{{ site.baseurl }}/assets/js/tabs.js"></script>

 <!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[0].label }}')" id="defaultOpen">{{ site.data.maps[0].qualified-label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[1].label }}')">{{ site.data.maps[1].qualified-label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[2].label }}')">{{ site.data.maps[2].qualified-label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[3].label }}')">{{ site.data.maps[3].qualified-label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[4].label }}')">{{ site.data.maps[4].qualified-label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[5].label }}')">{{ site.data.maps[5].qualified-label }}</button>
</div>

<!-- Tab content -->

<!-- Official -->
{% include detail.html index=0 %}

<!-- Most Proportional -->
{% include detail.html index=1 %}

<!-- Most Competitive -->
{% include detail.html index=2 %}

<!-- Best Minority -->
{% include detail.html index=3 %}

<!-- Most Compact -->
{% include detail.html index=4 %}

<!-- Least Splitting -->
{% include detail.html index=5 %}

<!-- Show the Official tab by default -->
<script>
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
</script> 