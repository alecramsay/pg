---
layout: page
title: Example
permalink: /example/

xx: "NC"
small-radar-width: 300
big-radar-width: 500
map-width: 700
---

An example for {{ page.xx }}.

<h3>Radar Diagrams</h3>

<table style="border:0px">
  <tr>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Official_radar.png" alt="{{ site.data.maps[0]["id"] }}" title="{{ site.data.maps[0]["id"] }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Proportional_radar.png" alt="{{ site.data.maps[1]["id"]["label"] }}" title="{{ site.data.maps[1]["id"]["label"] }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Competitive_radar.png" alt="{{ site.data.maps[2]["id"]["label"] }}" title="{{ site.data.maps[2]["id"]["label"] }}" width="{{ page.small-radar-width }}"/>
    </td>
  </tr>
  <tr>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Minority_radar.png" alt="{{ site.data.maps[3]["id"]["label"] }}" title="{{ site.data.maps[3]["id"]["label"] }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Compact_radar.png" alt="{{ site.data.maps[4]["id"]["label"] }}" title="{{ site.data.maps[4]["id"]["label"] }}" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Splitting_radar.png" alt="{{ site.data.maps[3]["id"]["label"] }}" title="{{ site.data.maps[3]["id"]["label"] }}" width="{{ page.small-radar-width }}"/>
    </td>
  </tr>
</table>

<h3>Ratings</h3>

<table>
  {% for row in site.data.NC_2022_Congress_ratings %}
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

<h3>Maps</h3>

<script src="../assets/js/tabs.js"></script>

 <!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[0]["id"] }}')" id="defaultOpen">{{ site.data.maps[0]["label"] }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[1]["id"] }}')">{{ site.data.maps[1]["label"] }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[2]["id"] }}')">{{ site.data.maps[2]["label"] }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[3]["id"] }}')">{{ site.data.maps[3]["label"] }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[4]["id"] }}')">{{ site.data.maps[4]["label"] }}</button>
  <button class="tablinks" onclick="openCity(event, '{{ site.data.maps[5]["id"] }}')">{{ site.data.maps[5]["label"] }}</button>
</div>

<!-- Tab content -->
<div id="{{ site.data.maps[0]["id"] }}" class="tabcontent">
  
  <h4>Ratings Compared to Baseline</h4>
  <p style="text-align: center">
    <img src="../assets/images/{{ page.xx }}_2022_Congress_{{ site.data.maps[0]["id"] }}_radar.png" alt="Radar diagram" title="Radar Diagram" width="{{ page.big-radar-width }}"/>
  </p>

  <h4>Map With Baseline Overlay</h4>
  <p style="text-align: center">
    <img src="../assets/images/{{ page.xx }}_2022_Congress_{{ site.data.maps[0]["id"] }}_map.png" alt="Map" title="Map with baseline overlay" width="{{ page.map-width }}"/>
  </p>

  <h4>Regions Intersecting With Baseline</h4>
  <p style="text-align: center">
    <img src="../assets/images/{{ page.xx }}_2022_Congress_{{ site.data.maps[0]["id"] }}_regions.png" alt="Regions" title="Intersecting regions" width="{{ page.map-width }}"/>
  </p>

  <h4>Regions Data</h4>
  <table>
    {% for row in site.data.NC_2022_Congress_Official_regions %}
      {% if forloop.first %}
      <tr>
        {% for pair in row %}
          <th>{{ pair[0] }}</th>
        {% endfor %}
      </tr>
      {% endif %}

      {% tablerow pair in row %}
        {% if pair[0] == "DISTRICT%" or pair[0] == "CUMULATIVE%"%}
          {{ pair[1] | times: 100 | round: 2 }}
        {% elsif pair[0] == "POPULATION" %}
          {{ pair[1] | intcomma }}
        {% else %}
          {{ pair[1] }}
        {% endif %}
      {% endtablerow %}
    {% endfor %}
  </table>
</div>

<div id="Proportional" class="tabcontent">
  <h4>Most Proportional</h4>
  <p>Most proportional maps ...</p>
</div>

<div id="Competitive" class="tabcontent">
  <h4>Most Competitive</h4>
  <p>Most competitive map ...</p>
</div> 

<div id="Minority" class="tabcontent">
  <h4>Best Minority</h4>
  <p>Best minority map ...</p>
</div> 

<div id="Compact" class="tabcontent">
  <h4>Most Compact</h4>
  <p>Most compact map ...</p>
</div> 

<div id="Splitting" class="tabcontent">
  <h4>Least Splitting</h4>
  <p>Least splitting map ...</p>
</div> 

<!-- Show the Official tab by default -->
<script>
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
</script> 