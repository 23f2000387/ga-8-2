# Marimo Interactive Notebook
# Author Email: 23f2000387@ds.study.iitm.ac.in
# This file demonstrates variable dependencies, interactivity, and dynamic markdown.

import marimo as mo

# -------------------------------------------------------------
# CELL 1: Load or create dataset
# This cell defines `x` and `y`, which downstream cells depend on.
# -------------------------------------------------------------
x = list(range(1, 101))
y = [i * 2 for i in x]   # simple linear relation
mo.md("### Dataset Loaded\nA simple dataset with a linear relationship was created.")

# -------------------------------------------------------------
# CELL 2: Slider widget controls number of points shown
# This slider value will be used by dependent cells.
# -------------------------------------------------------------
slider = mo.ui.slider(start=5, stop=100, value=20, label="Number of Points to Display")

mo.md(f"### Selected value: **{slider.value}** data points")

# -------------------------------------------------------------
# CELL 3: Dependent computation
# Depends on both the dataset (x, y) and the slider value.
# -------------------------------------------------------------
subset_x = x[: slider.value]
subset_y = y[: slider.value]

mo.md(
    f"""
### Data Preview (First {slider.value} points)

- Minimum X: **{min(subset_x)}**
- Maximum X: **{max(subset_x)}**
- Minimum Y: **{min(subset_y)}**
- Maximum Y: **{max(subset_y)}**

Relationship remains linear:  
`y = 2x`
"""
)

# -------------------------------------------------------------
# CELL 4: Dynamic visualization
# Automatically updates when slider changes.
# -------------------------------------------------------------
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(subset_x, subset_y)
ax.set_title(f"Interactive Plot for First {slider.value} Points")
ax.set_xlabel("X")
ax.set_ylabel("Y")

fig
