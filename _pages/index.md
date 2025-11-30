---
layout: home
title: Home
id: home
permalink: /
---

<div class="home-container">
<div class="home-main" markdown="1">

# Federico's Notes

This is a selection of my interconnected notes. It is an experiment and a work in progress, a space for developing ideas through writing and connecting concepts across different domains.

---

## Knowledge Graph

Explore the connections between notes below. Click any node to navigate, or drag nodes to rearrange the view.

</div>

<div class="graph-container" markdown="0">

{% include notes_graph.html %}

</div>

<aside class="home-sidebar" markdown="0">

<h3>Recently Updated</h3>

<ul class="recent-notes-list">
{% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
{% for note in recent_notes limit: 10 %}
<li><a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a></li>
{% endfor %}
</ul>

</aside>
</div>
