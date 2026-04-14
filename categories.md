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

{% assign machine_learning_posts = site.categories["Machine Learning"] | sort: "date" | reverse %}

<div class="category-tree">
  <section class="category-tree__group" id="computer-science">
    <h2>Computer Science</h2>
    <p>현재는 Machine Learning 하위 분류를 사용합니다.</p>

    <div class="category-tree__child" id="machine-learning">
      <h3>Machine Learning</h3>
      {% if machine_learning_posts.size > 0 %}
        <ul class="category-tree__list">
          {% for post in machine_learning_posts %}
            <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
          {% endfor %}
        </ul>
      {% else %}
        <p>아직 이 분류에 글이 없습니다.</p>
      {% endif %}
    </div>
  </section>
</div>
