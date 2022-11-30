---
layout: page
title: Example
permalink: example/

xx: "NC"
small-radar-width: 300
big-radar-width: 500
map-width: 700
---

A sample page for {{ page.xx }}.

{% assign xx = page.xx %}

<!-- RADAR DIAGRAMS -->

<h3>Radar Diagrams</h3>

<table style="border:0px">
  <tr>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Official_radar.png" alt="{{ site.data.maps[0].id }}" title="{{ site.data.maps[0].id }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Proportional_radar.png" alt="{{ site.data.maps[1].label }}" title="{{ site.data.maps[1].label }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Competitive_radar.png" alt="{{ site.data.maps[2].label }}" title="{{ site.data.maps[2].label }}" width="{{ page.small-radar-width }}"/>
    </td>
  </tr>
  <tr>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Minority_radar.png" alt="{{ site.data.maps[3].label }}" title="{{ site.data.maps[3].label }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Compact_radar.png" alt="{{ site.data.maps[4].label }}" title="{{ site.data.maps[4].label }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Splitting_radar.png" alt="{{ site.data.maps[3].label }}" title="{{ site.data.maps[3].label }}" width="{{ page.small-radar-width }}"/>
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

<script src="{{ site.baseurl }}/assets/js/tabs.js"></script>

 <!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[0].id }}')" id="defaultOpen">{{ site.data.maps[0].label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[1].id }}')">{{ site.data.maps[1].label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[2].id }}')">{{ site.data.maps[2].label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[3].id }}')">{{ site.data.maps[3].label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[4].id }}')">{{ site.data.maps[4].label }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[5].id }}')">{{ site.data.maps[5].label }}</button>
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