# Lesson 45: `seaborn` - Statistical Data Visualization

`seaborn` is a Python data visualization library based on `matplotlib`. It provides a high-level interface for drawing attractive and informative statistical graphics. While `matplotlib` is the foundation, `seaborn` simplifies the creation of complex plots and often produces more aesthetically pleasing results with less code.

**Official Documentation:** [https://seaborn.pydata.org/](https://seaborn.pydata.org/)

---

### Installation

If you don't have `seaborn` installed, you can do so using pip:

```bash
pip install seaborn
```

### Relationship with Matplotlib

It's crucial to understand that `seaborn` is built on top of `matplotlib`. This means you can use `matplotlib`'s functions (like `plt.title()`, `plt.xlabel()`, `plt.show()`) to further customize `seaborn` plots.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Example: Using a built-in dataset
tips = sns.load_dataset("tips")

sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Total Bill vs. Tip") # Matplotlib function
plt.xlabel("Total Bill ($)") # Matplotlib function
plt.ylabel("Tip ($)") # Matplotlib function
plt.show()
```

### Key Features and Plot Types

Seaborn categorizes its plotting functions into several groups:

#### 1. Relational Plots (e.g., `scatterplot`, `lineplot`)

These plots visualize the statistical relationship between two or more variables.

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Scatter Plot
sns.scatterplot(x="total_bill", y="tip", hue="time", style="smoker", data=tips)
plt.title("Total Bill vs. Tip by Time and Smoker")
plt.show()

# Line Plot (often for time series or ordered data)
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot_table(index='year', columns='month', values='passengers')
sns.lineplot(data=flights_pivot['Jan'])
plt.title("January Passengers Over Years")
plt.show()
```

#### 2. Distribution Plots (e.g., `histplot`, `kdeplot`, `boxplot`, `violinplot`, `displot`)

These plots show the distribution of a single variable or the relationship between a numerical and a categorical variable.

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Histogram
sns.histplot(data=tips, x="total_bill", kde=True)
plt.title("Distribution of Total Bill")
plt.show()

# Box Plot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Total Bill by Day")
plt.show()

# Violin Plot (combines box plot with kernel density estimation)
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Total Bill Distribution by Day (Violin Plot)")
plt.show()

# Displot (flexible function for various distributions)
sns.displot(data=tips, x="total_bill", col="time", row="smoker", kind="kde")
plt.suptitle("KDE of Total Bill by Time and Smoker", y=1.02) # Adjust suptitle position
plt.show()
```

#### 3. Categorical Plots (e.g., `barplot`, `countplot`)

These plots show the relationship between a numerical and one or more categorical variables.

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Bar Plot (shows mean and confidence interval)
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Average Total Bill by Day")
plt.show()

# Count Plot (shows counts of observations in each category)
sns.countplot(x="day", data=tips)
plt.title("Number of Observations per Day")
plt.show()
```

#### 4. Regression Plots (e.g., `regplot`, `lmplot`)

These plots visualize linear relationships between variables.

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Regplot (single plot)
sns.regplot(x="total_bill", y="tip", data=tips)
plt.title("Regression Plot: Total Bill vs. Tip")
plt.show()

# Lmplot (can create multi-panel plots based on categorical variables)
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)
plt.suptitle("Regression Plot by Smoker Status", y=1.02)
plt.show()
```

#### 5. Matrix Plots (e.g., `heatmap`, `clustermap`)

These plots visualize data that is organized in a matrix form.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Heatmap of correlations
iris = sns.load_dataset("iris")
correlation_matrix = iris.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix of Iris Dataset")
plt.show()
```

#### 6. Multi-plot Grids (e.g., `pairplot`)

These functions allow you to draw multiple plots on a single figure, often showing relationships across many variables.

```python
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.pairplot(iris, hue="species")
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()
```

---

### Quiz

1.  **Is `seaborn` a replacement for `matplotlib`?**
    a) Yes
    b) No, it is built on top of `matplotlib` and extends its capabilities.

2.  **Which `seaborn` function is best suited for visualizing the distribution of a single numerical variable with a histogram and KDE?**
    a) `sns.scatterplot()`
    b) `sns.boxplot()`
    c) `sns.histplot()`
    d) `sns.lineplot()`

3.  **What is the purpose of `sns.pairplot()`?**
    a) To create a single plot showing the relationship between two variables.
    b) To plot pairwise relationships in a dataset.
    c) To compare two different datasets.

4.  **How do you typically load a built-in dataset in Seaborn?**
    a) `sns.load_data("dataset_name")`
    b) `sns.get_dataset("dataset_name")`
    c) `sns.load_dataset("dataset_name")`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
  3. b
  4. c
</details>