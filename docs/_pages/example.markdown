---
layout: page
title: Example
permalink: /example/

xx: "NC"
width: 400
---

State: {{ page.xx }}

---|---|---
<img src="../assets/images/{{ page.xx }}_2022_Congress_Official_radar.png" alt="Official" title="Official" width="{{ page.width }}"/> | <img src="../assets/images/{{ page.xx }}_2022_Congress_Proportional_radar.png" alt="Most Proportional" title="Most Proportional" width="{{ page.width }}"/> | <img src="../assets/images/{{ page.xx }}_2022_Congress_Competitive_radar.png" alt="Most Competitive" title="Most Competitive" width="{{ page.width }}"/>
<img src="../assets/images/{{ page.xx }}_2022_Congress_Minority_radar.png" alt="Best Minority" title="Best Minority" width="{{ page.width }}"/> | <img src="../assets/images/{{ page.xx }}_2022_Congress_Compact_radar.png" alt="Most Compact" title="Most Compact" width="{{ page.width }}"/> | <img src="../assets/images/{{ page.xx }}_2022_Congress_Splitting_radar.png" alt="Least Splitting" title="Least Splitting" width="{{ page.width }}"/>

<!-- Pure Markdown:
---|---|---
![Official](../assets/images/{{ page.xx }}_2022_Congress_Official_radar.png "Official") | ![Most Proportional](../assets/images/{{ page.xx }}_2022_Congress_Proportional_radar.png "Most Proportional") | ![Most Competitive](../assets/images/{{ page.xx }}_2022_Congress_Competitive_radar.png "Most Competitive")
![Best Minority](../assets/images/{{ page.xx }}_2022_Congress_Minority_radar.png "Best Minority") | ![Most Compact](../assets/images/{{ page.xx }}_2022_Congress_Compact_radar.png "Most Compact") | ![Least Splitting](../assets/images/{{ page.xx }}_2022_Congress_Splitting_radar.png "Least Splitting") -->

