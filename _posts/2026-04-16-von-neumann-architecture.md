---
layout: single
title: "Von Neumann Architecture"
date: 2026-04-16 09:00:00 +0900
classes: wide
tags:
  - Zettelkasten
  - ComputerScience
categories:
  - Computer Science
excerpt: "프로그램을 구성하는 Instruction도 RAM 위에 올려놓는 구조."
---

<style>
.von-neumann-post {
  max-width: 760px;
  margin: 0 auto;
  padding: 1.25rem 1.4rem;
  border: 1px solid rgba(120, 120, 120, 0.18);
  border-radius: 18px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(248, 249, 252, 0.96));
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
}

.von-neumann-post p,
.von-neumann-post li {
  font-size: 1.02rem;
  line-height: 1.8;
}

.von-neumann-post p:first-of-type {
  margin-top: 0.8rem;
}

.von-neumann-post blockquote {
  margin: 1.2rem 0;
  padding: 1rem 1.1rem;
  border-left: 4px solid #5478f6;
  background: rgba(84, 120, 246, 0.06);
  border-radius: 10px;
  color: #24324a;
}

.von-neumann-post h2 {
  margin-top: 1.8rem;
  padding-top: 0.4rem;
  font-size: 1.15rem;
  letter-spacing: -0.02em;
}

.von-neumann-post ul {
  margin-left: 1.2rem;
}

.von-neumann-post hr {
  margin: 1.4rem 0;
  border: 0;
  border-top: 1px solid rgba(120, 120, 120, 0.18);
}

.von-neumann-post a {
  text-decoration-thickness: 2px;
  text-underline-offset: 0.18em;
}

@media (max-width: 768px) {
  .von-neumann-post {
    padding: 1rem;
    border-radius: 14px;
  }
}
</style>

<article class="von-neumann-post">
  <p>프로그램을 구성하는 Instruction도 RAM 위에 올려놓는 구조.</p>

  <p>즉 RAM에는 Instruction과 Data가 같이 저장된다. 또한 조건 분기가 무제한으로 허용된다. 임의 접근이 가능한 메모리 위에 Instruction이 올라와 있기 때문에 이것이 가능하다.</p>

  <hr>

  <h2>References</h2>
  <ul>
    <li>System Programming Course(4-1)</li>
  </ul>
</article>
