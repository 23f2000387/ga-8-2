---
marp: true
title: Product Technical Documentation
author: Kalppana S
theme: default
paginate: true
---

<!-- _class: lead -->

# Product Technical Documentation
### Using Marp
**Email:** 23f2000387@ds.study.iitm.ac.in

---

<!-- Custom Theme -->
<style>
section {
  background: #f7f9fc;
  color: #222;
  font-family: "Segoe UI", sans-serif;
}
h1, h2 {
  color: #005bbb;
}
blockquote {
  border-left: 4px solid #005bbb;
  padding-left: 10px;
  font-style: italic;
}
</style>

# Introduction
This documentation demonstrates:
- Custom themes
- Background images
- Code blocks
- Math equations
- Directives
- Page numbering
- Maintainable structure

---

<!-- Background image slide -->
<!-- _backgroundImage: url('images/bg1.jpg') -->
<!-- _backgroundSize: cover -->

# Background Image Slide
This slide uses a **full background image** using Marp directives.
Make sure the image exists at: `images/bg1.jpg`

---

# Algorithmic Complexity

Marp supports **KaTeX** for math:

### Inline Math
$O(n \log n)$

### Block Equation
$$
T(n) = 2T\left(\frac{n}{2}\right) + n
$$

Master theorem gives:
$$
T(n) = O(n \log n)
$$

---

# Code Sample

```python
def compute():
    for i in range(1000):
        print(i)

compute()
