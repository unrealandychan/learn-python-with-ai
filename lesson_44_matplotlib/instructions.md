# Lesson 44: `matplotlib` - Data Visualization

`matplotlib` is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is the foundational library for many other plotting libraries (like `seaborn`, which we'll cover next) and is widely used for generating publication-quality plots.

**Official Documentation:** [https://matplotlib.org/stable/index.html](https://matplotlib.org/stable/index.html)

---

### Installation

If you don't have `matplotlib` installed, you can do so using pip:

```bash
pip install matplotlib
```

### Basic Plotting with `pyplot`

The `matplotlib.pyplot` module provides a MATLAB-like interface for plotting. It's the most common way to use Matplotlib.

```python
import matplotlib.pyplot as plt

# Simple Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

plt.plot(x, y)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Plot")
plt.grid(True) # Add a grid
plt.show() # Display the plot
```

### Types of Plots

#### 1. Line Plots (`plt.plot()`)

Used to show trends over time or ordered categories.

```python
# Already shown above
```

#### 2. Scatter Plots (`plt.scatter()`)

Used to show the relationship between two numerical variables.

```python
import matplotlib.pyplot as plt

x_data = [10, 20, 30, 40, 50]
y_data = [5, 15, 25, 35, 45]

plt.scatter(x_data, y_data)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot Example")
plt.show()
```

#### 3. Bar Charts (`plt.bar()`)

Used to compare quantities of different categories.

```python
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 12]

plt.bar(categories, values, color='skyblue')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.show()
```

#### 4. Histograms (`plt.hist()`)

Used to show the distribution of a single numerical variable.

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000) # Generate 1000 random numbers from a normal distribution

plt.hist(data, bins=30, edgecolor='black') # bins define the number of bars
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.show()
```

### Customizing Plots

*   **Labels and Title**: `plt.xlabel()`, `plt.ylabel()`, `plt.title()`.
*   **Legend**: `plt.legend()` (requires `label` argument in `plot`/`scatter` calls).
*   **Colors, Markers, Linestyles**: Can be specified in plotting functions (e.g., `plt.plot(x, y, color='red', linestyle='--', marker='o')`).
*   **Grid**: `plt.grid(True)`.
*   **Figure Size**: `plt.figure(figsize=(width, height))`.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 5, 3]
y2 = [1, 3, 5, 2, 4]

plt.figure(figsize=(8, 5)) # Set figure size
plt.plot(x, y1, label='Data Series 1', color='blue', linestyle='-', marker='o')
plt.plot(x, y2, label='Data Series 2', color='red', linestyle='--', marker='x')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Customized Line Plot")
plt.legend() # Display legend
plt.grid(True)
plt.show()
```

### Subplots (`plt.subplot()` or `plt.subplots()`)

To create multiple plots within a single figure, you can use subplots.

```python
import matplotlib.pyplot as plt
import numpy as np

# Method 1: using plt.subplot()
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1) # (rows, columns, panel number)
plt.plot([0, 1], [0, 1])
plt.title("Subplot 1")

plt.subplot(1, 2, 2)
plt.plot([0, 1], [1, 0])
plt.title("Subplot 2")

plt.tight_layout() # Adjusts subplot params for a tight layout
plt.show()

# Method 2: using plt.subplots() (recommended for more control)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

axes[0].plot([0, 1], [0, 1])
axes[0].set_title("Subplot A")

axes[1].plot([0, 1], [1, 0])
axes[1].set_title("Subplot B")

plt.tight_layout()
plt.show()
```

### Saving Plots

You can save your plots to various file formats (e.g., PNG, JPG, PDF) using `plt.savefig()`.

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Plot to Save")
plt.savefig('my_plot.png') # Saves as PNG
# plt.savefig('my_plot.pdf') # Saves as PDF
print("Plot saved as my_plot.png")
```

---

### Quiz

1.  **Which function is used to display a plot in Matplotlib?**
    a) `plt.display()`
    b) `plt.show()`
    c) `plt.render()`

2.  **How do you add a title to your plot?**
    a) `plt.add_title("My Title")`
    b) `plt.set_title("My Title")`
    c) `plt.title("My Title")`

3.  **Which of the following is used to create multiple plots within a single figure?**
    a) `plt.multiple_plots()`
    b) `plt.subplots()`
    c) `plt.grid()`

4.  **What is the purpose of `plt.savefig('my_plot.png')`?**
    a) To display the plot in a web browser.
    b) To save the current plot to a file named `my_plot.png`.
    c) To clear the current plot.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
  3. b
  4. b
</details>