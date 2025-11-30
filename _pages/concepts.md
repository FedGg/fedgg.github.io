---
layout: page
title: Key Concepts
permalink: /concepts
---

{::nomarkdown}
<div class="concepts-page">

<h1>Key Concepts</h1>

<p class="concepts-intro">Foundational ideas that connect throughout this digital garden.</p>

{% assign concept_notes = "" | split: "" %}
{% for note in site.notes %}
  {% if note.category == "Concepts" or note.category == "concepts" %}
    {% assign concept_notes = concept_notes | push: note %}
  {% elsif note.tags contains "concepts" %}
    {% assign concept_notes = concept_notes | push: note %}
  {% endif %}
{% endfor %}

{% assign sorted_concepts = concept_notes | sort: "title" %}

{% if sorted_concepts.size > 0 %}
<ul class="concepts-list">
{% for note in sorted_concepts %}
  <li><a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a></li>
{% endfor %}
</ul>
{% else %}
<p class="no-concepts"><em>No concept notes found yet. Add notes with <code>category: Concepts</code> or <code>tags: [concepts]</code> in the YAML front matter.</em></p>
{% endif %}

</div>
{:/nomarkdown}
