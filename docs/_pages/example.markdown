---
layout: page
title: Example
permalink: /example/

xx: "NC"
width: 400
---

An example for {{ page.xx }}.

### Radar Diagrams

<table style="border:0px">
  <tr>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Official_radar.png" alt="Official" title="Official" width="{{ page.width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Proportional_radar.png" alt="Most Proportional" title="Most Proportional" width="{{ page.width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Competitive_radar.png" alt="Most Competitive" title="Most Competitive" width="{{ page.width }}"/>
    </td>
  </tr>
  <tr>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Minority_radar.png" alt="Best Minority" title="Best Minority" width="{{ page.width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Compact_radar.png" alt="Most Compact" title="Most Compact" width="{{ page.width }}"/>
    </td>
    <td style="border:0px">
      <img src="../assets/images/{{ page.xx }}_2022_Congress_Splitting_radar.png" alt="Least Splitting" title="Least Splitting" width="{{ page.width }}"/>
    </td>
  </tr>
</table>

### Ratings

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

### Maps

<script src="../assets/js/tabs.js"></script>

 <!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'London')" id="defaultOpen">London</button>
  <button class="tablinks" onclick="openCity(event, 'Paris')">Paris</button>
  <button class="tablinks" onclick="openCity(event, 'Tokyo')">Tokyo</button>
</div>

<!-- Tab content -->
<div id="London" class="tabcontent">
  <h3>London</h3>
  <p>London is the capital city of England.</p>
</div>

<div id="Paris" class="tabcontent">
  <h3>Paris</h3>
  <p>Paris is the capital of France.</p>
</div>

<div id="Tokyo" class="tabcontent">
  <h3>Tokyo</h3>
  <p>Tokyo is the capital of Japan.</p>
</div> 

<!-- Show a tab by default -->
<script>
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
</script> 