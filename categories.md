---
title: "Categories"
layout: archive
permalink: /categories/
author_profile: true
classes: wide
---

<style>
.category-tree {
  display: grid;
  gap: 1.25rem;
  margin-top: 1rem;
}

.category-tree__group {
  padding: 1.1rem 1.2rem;
  border: 1px solid rgba(120, 120, 120, 0.16);
  border-radius: 16px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.95), rgba(248, 249, 252, 0.96));
  box-shadow: 0 14px 32px rgba(15, 23, 42, 0.06);
}

.category-tree__group h2,
.category-tree__child h3 {
  margin-top: 0;
  margin-bottom: 0.6rem;
  letter-spacing: -0.02em;
}

.category-tree__child {
  margin-top: 0.9rem;
  margin-left: 1rem;
  padding-left: 1rem;
  border-left: 3px solid rgba(84, 120, 246, 0.35);
}

.category-tree__list {
  margin: 0.4rem 0 0;
  padding-left: 1.1rem;
}

.category-tree__list li {
  margin: 0.35rem 0;
  line-height: 1.6;
}

.category-tree__list a {
  text-decoration-thickness: 2px;
  text-underline-offset: 0.18em;
}
</style>

{% assign sorted_posts = site.posts | sort: "date" | reverse %}
{% assign preferred_kbo_children = "일간 기록|주간 기록|월간 기록|연간 기록" | split: "|" %}
{% assign top_categories = '' | split: '' %}
{% for post in sorted_posts %}
  {% assign top_category = post.categories | first %}
  {% if top_category and top_category != "" %}
    {% unless top_categories contains top_category %}
      {% assign top_categories = top_categories | push: top_category %}
    {% endunless %}
  {% endif %}
{% endfor %}

<div class="category-tree">
  {% for top_category in top_categories %}
    {% assign top_level_posts = '' | split: '' %}
    {% assign child_categories = '' | split: '' %}
    {% for post in sorted_posts %}
      {% if post.categories[0] == top_category %}
        {% if post.categories.size == 1 %}
          {% assign top_level_posts = top_level_posts | push: post %}
        {% elsif post.categories[1] %}
          {% unless child_categories contains post.categories[1] %}
            {% assign child_categories = child_categories | push: post.categories[1] %}
          {% endunless %}
        {% endif %}
      {% endif %}
    {% endfor %}

    <section class="category-tree__group" id="{{ top_category | slugify }}">
      <h2>{{ top_category }}</h2>
      {% if top_level_posts.size > 0 %}
        <ul class="category-tree__list">
          {% for post in top_level_posts %}
            <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
          {% endfor %}
        </ul>
      {% elsif child_categories.size == 0 %}
        <p>아직 이 분류에 글이 없습니다.</p>
      {% endif %}

      {% if top_category == "KBO Data" %}
        {% for child_category in preferred_kbo_children %}
          {% if child_categories contains child_category %}
            {% assign child_posts = '' | split: '' %}
            {% for post in sorted_posts %}
              {% if post.categories[0] == top_category and post.categories[1] == child_category %}
                {% assign child_posts = child_posts | push: post %}
              {% endif %}
            {% endfor %}

            <div class="category-tree__child" id="{{ top_category | slugify }}-{{ child_category | slugify }}">
              <h3>{{ child_category }}</h3>
              {% if child_posts.size > 0 %}
                <ul class="category-tree__list">
                  {% for post in child_posts %}
                    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
                  {% endfor %}
                </ul>
              {% endif %}
            </div>
          {% endif %}
        {% endfor %}

        {% for child_category in child_categories %}
          {% unless preferred_kbo_children contains child_category %}
            {% assign child_posts = '' | split: '' %}
            {% for post in sorted_posts %}
              {% if post.categories[0] == top_category and post.categories[1] == child_category %}
                {% assign child_posts = child_posts | push: post %}
              {% endif %}
            {% endfor %}

            <div class="category-tree__child" id="{{ top_category | slugify }}-{{ child_category | slugify }}">
              <h3>{{ child_category }}</h3>
              {% if child_posts.size > 0 %}
                <ul class="category-tree__list">
                  {% for post in child_posts %}
                    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
                  {% endfor %}
                </ul>
              {% endif %}
            </div>
          {% endunless %}
        {% endfor %}
      {% else %}
      {% for child_category in child_categories %}
        {% assign child_posts = '' | split: '' %}
        {% for post in sorted_posts %}
          {% if post.categories[0] == top_category and post.categories[1] == child_category %}
            {% assign child_posts = child_posts | push: post %}
          {% endif %}
        {% endfor %}

        <div class="category-tree__child" id="{{ top_category | slugify }}-{{ child_category | slugify }}">
          <h3>{{ child_category }}</h3>
          {% if child_posts.size > 0 %}
            <ul class="category-tree__list">
              {% for post in child_posts %}
                <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
              {% endfor %}
            </ul>
          {% else %}
            <p>아직 이 분류에 글이 없습니다.</p>
          {% endif %}
        </div>
      {% endfor %}
      {% endif %}
    </section>
  {% endfor %}
</div>
