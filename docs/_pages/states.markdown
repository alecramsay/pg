---
layout: page
title: States
permalink: /States/
---

<ul>
{% for state in site.data.states.states %}
  {% if state.ready == true %}
    <li><a href="TODO">{{ state.name }} ({{ state.xx }})</a></li>
  {% else %}
    <li>{{ state.name }} ({{ state.xx }}) -- not available yet</li>
  {% endif %}
{% endfor %}
</ul>