---
layout: page
title: States
permalink: /states
---

<!-- A placeholder state picker -->

<ul>
{% for state in site.data.states.states %}
  {% if state.ready == true %}
    <li><a href="{{ state.xx }}">{{ state.name }} ({{ state.xx }})</a></li>
  {% else %}
    <li>{{ state.name }} ({{ state.xx }}) -- not available yet</li>
  {% endif %}
{% endfor %}
</ul>