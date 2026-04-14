---
layout: single
title: "Unsupervised Learning"
date: 2026-04-14 09:00:00 +0900
classes: wide
tags:
  - Zettelkasten
  - AI
  - MachineLearning
excerpt: "컴퓨터에게 label 없이 데이터를 전달하고, 입력들의 그룹을 찾아내는 학습."
---

<style>
.unsupervised-post {
  max-width: 760px;
  margin: 0 auto;
  padding: 1.25rem 1.4rem;
  border: 1px solid rgba(120, 120, 120, 0.18);
  border-radius: 18px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(248, 249, 252, 0.96));
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
}

.unsupervised-post p,
.unsupervised-post li {
  font-size: 1.02rem;
  line-height: 1.8;
}

.unsupervised-post p:first-of-type {
  margin-top: 0.8rem;
}

.unsupervised-post blockquote {
  margin: 1.2rem 0;
  padding: 1rem 1.1rem;
  border-left: 4px solid #5478f6;
  background: rgba(84, 120, 246, 0.06);
  border-radius: 10px;
  color: #24324a;
}

.unsupervised-post h2 {
  margin-top: 1.8rem;
  padding-top: 0.4rem;
  font-size: 1.15rem;
  letter-spacing: -0.02em;
}

.unsupervised-post ul {
  margin-left: 1.2rem;
}

.unsupervised-post hr {
  margin: 1.4rem 0;
  border: 0;
  border-top: 1px solid rgba(120, 120, 120, 0.18);
}

.unsupervised-post a {
  text-decoration-thickness: 2px;
  text-underline-offset: 0.18em;
}

@media (max-width: 768px) {
  .unsupervised-post {
    padding: 1rem;
    border-radius: 14px;
  }
}
</style>

<article class="unsupervised-post">
  <p>Machine Learning의 일종.</p>

  <p>컴퓨터에게 그냥 데이터를 전달한다(Label 없이 전달한다는 뜻). 이후 컴퓨터가 Input들을 Clustering한다.</p>

  <p>간단히 말해, Input이 어떤 Output에 해당하는지 맞히는 것은 Unsupervised learning이 할 일이 아니다. 이 Input들이 어떤 그룹들로 나뉘는지를 알아내는 것이 Unsupervised learning이 할 일이다.</p>

  <hr>

  <h2>References</h2>
  <ul>
    <li><a href="https://youtu.be/gG_wI_uGfIE?si=MYdaFZU_-fLIrZkj" target="_blank" rel="noopener noreferrer">Machine Learning Specialization</a></li>
    <li><a href="https://youtu.be/gG_wI_uGfIE?si=0PVcHC4rJ--Xzr61" target="_blank" rel="noopener noreferrer">Machine Learning Specialization</a></li>
  </ul>
</article>
