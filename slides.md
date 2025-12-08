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

<!-- Custom Theme (CSS override) -->
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
- Maintainability for version control  

---

<!-- Background Image Slide -->
<!-- _backgroundImage: url('bg1.jpg') -->
<!-- _backgroundSize: cover -->
<!-- _backgroundPosition: center -->

# Background Image Slide

This slide uses a **full background image**.

Make sure the image exists at:  
`images/bg1.jpg`

**Email:** 23f2000387@ds.study.iitm.ac.in

---

# Algorithmic Complexity (Math Support)

Marp supports **KaTeX** for rendering math:

### Time Complexity  
Inline: $O(n \log n)$  

### Full Equation  
$$
T(n) = 2T\left(\frac{n}{2}\right) + n
$$

Using the Master theorem:  
$$
T(n) = O(n \log n)
$$

---

# Code Sample

```python
def compute():
    for i in range(1000):
        print(i)
