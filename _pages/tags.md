---
layout: page
title: Tags
permalink: /tags
---

# Browse by Tag

Click a tag to see all related notes.

{% assign all_tags = "" | split: "" %}
{% for note in site.notes %}
  {% if note.tags %}
    {% for tag in note.tags %}
      {% unless all_tags contains tag %}
        {% assign all_tags = all_tags | push: tag %}
      {% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign sorted_tags = all_tags | sort %}

<div class="tag-cloud">
{% for tag in sorted_tags %}
  {% assign tag_count = 0 %}
  {% for note in site.notes %}
    {% if note.tags contains tag %}
      {% assign tag_count = tag_count | plus: 1 %}
    {% endif %}
  {% endfor %}
  <a href="#{{ tag }}" class="tag-link">#{{ tag }} <span class="count">({{ tag_count }})</span></a>
{% endfor %}
</div>

---

{% for tag in sorted_tags %}

<div id="{{ tag }}" class="tag-section">

## #{{ tag }}

{% for note in site.notes %}{% if note.tags contains tag %}
- [{{ note.title }}]({{ note.url }})
{% endif %}{% endfor %}

</div>
{% endfor %}
