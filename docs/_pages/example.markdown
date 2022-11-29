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
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Official_radar.png" alt="Official" title="Official" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Proportional_radar.png" alt="Most Proportional" title="Most Proportional" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Competitive_radar.png" alt="Most Competitive" title="Most Competitive" width="{{ page.small-radar-width }}"/>
    </td>
  </tr>
  <tr>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Minority_radar.png" alt="Best Minority" title="Best Minority" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Compact_radar.png" alt="Most Compact" title="Most Compact" width="{{ page.small-radar-width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Splitting_radar.png" alt="Least Splitting" title="Least Splitting" width="{{ page.small-radar-width }}"/>
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
  <button class="tablinks" onclick="openCity(event, 'Official')" id="defaultOpen">Official</button>
  <button class="tablinks" onclick="openCity(event, 'Proportional')">Most Proportional</button>
  <button class="tablinks" onclick="openCity(event, 'Competitive')">Most Competitive</button>
  <button class="tablinks" onclick="openCity(event, 'Minority')">Best Minority</button>
  <button class="tablinks" onclick="openCity(event, 'Compact')">Most Compact</button>
  <button class="tablinks" onclick="openCity(event, 'Splitting')">Least Splitting</button>
</div>

<!-- Tab content -->
<div id="Official" class="tabcontent">
  
  <h4>Ratings Compared to Baseline</h4>
  <p style="text-align: center">
    <img src="../assets/images/{{ page.xx }}_2022_Congress_Official_radar.png" alt="Radar diagram" title="Radar Diagram" width="{{ page.big-radar-width }}"/>
  </p>

  <h4>Map With Baseline Overlay</h4>
  <p style="text-align: center">
    <img src="../assets/images/{{ page.xx }}_2022_Congress_Official_map.png" alt="Map" title="Map with baseline overlay" width="{{ page.map-width }}"/>
  </p>

  <h4>Regions Intersecting With Baseline</h4>
  <p style="text-align: center">
    <img src="../assets/images/{{ page.xx }}_2022_Congress_Official_regions.png" alt="Regions" title="Intersecting regions" width="{{ page.map-width }}"/>
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