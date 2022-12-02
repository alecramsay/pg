---
layout: page
title: States
permalink: states/
---

<!-- A placeholder state picker -->

<ul>
{% for state in site.data.states %}
  {% if state.ready == true %}
    <li><a href="{{ site.baseurl }}/states/{{ state.xx }}">{{ state.name }} ({{ state.xx }})</a></li>
  {% else %}
    <li>{{ state.name }} ({{ state.xx }}) -- TBD</li>
  {% endif %}
{% endfor %}
</ul>