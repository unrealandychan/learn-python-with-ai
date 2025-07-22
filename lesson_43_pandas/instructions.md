# Lesson 43: `pandas` - Data Analysis and Manipulation

`pandas` is an open-source Python library widely used for data manipulation and analysis. It provides powerful, flexible, and easy-to-use data structures, most notably the `DataFrame`, which is ideal for working with tabular data (like spreadsheets or SQL tables).

**Official Documentation:** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

---

### Installation

If you don't have `pandas` installed, you can do so using pip:

```bash
pip install pandas
```

### Core Data Structures

`pandas` introduces two primary data structures:

1.  **`Series`**: A one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). It's like a single column of a spreadsheet or a SQL table.

    ```python
    import pandas as pd

    s = pd.Series([1, 3, 5, 7, 9])
    # print(s)
    # Output:
    # 0    1
    # 1    3
    # 2    5
    # 3    7
    # 4    9
    # dtype: int64

    s_labeled = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    # print(s_labeled)
    # Output:
    # a    10
    # b    20
    # c    30
    # dtype: int64
    ```

2.  **`DataFrame`**: A two-dimensional labeled data structure with columns of potentially different types. It's like a spreadsheet, a SQL table, or a dictionary of Series objects. It is the most commonly used pandas object.

    ```python
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Paris']}
    df = pd.DataFrame(data)
    # print(df)
    # Output:
    #        Name  Age      City
    # 0     Alice   25  New York
    # 1       Bob   30    London
    # 2   Charlie   35     Paris
    ```

### Creating DataFrames

#### From a Dictionary (as shown above)

```python
# Already demonstrated above
```

#### From a List of Dictionaries

```python
list_of_dicts = [
    {'Name': 'David', 'Age': 22, 'City': 'Berlin'},
    {'Name': 'Eve', 'Age': 28, 'City': 'Rome'}
]
# df_from_list = pd.DataFrame(list_of_dicts)
# print(df_from_list)
```

#### Reading from CSV Files

One of the most common ways to get data into a DataFrame is by reading a CSV (Comma Separated Values) file using `pd.read_csv()`.

```python
# Assuming 'sample_data.csv' exists in the same directory
# df_csv = pd.read_csv('sample_data.csv')
# print(df_csv.head())
```

### Basic DataFrame Operations

#### Viewing Data

*   `df.head(n)`: Returns the first `n` rows (default 5).
*   `df.tail(n)`: Returns the last `n` rows (default 5).
*   `df.info()`: Provides a concise summary of a DataFrame, including data types and non-null values.
*   `df.describe()`: Generates descriptive statistics of numerical columns.
*   `df.shape`: Returns a tuple representing the dimensionality of the DataFrame (rows, columns).
*   `df.columns`: Returns the column labels of the DataFrame.

```python
# df = pd.read_csv('sample_data.csv')
# print(df.head(2))
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)
```

#### Selecting Columns

You can select one or more columns using square bracket notation.

```python
# df = pd.read_csv('sample_data.csv')
# print(df['Name']) # Select a single column (returns a Series)
# print(df[['Name', 'Age']]) # Select multiple columns (returns a DataFrame)
```

#### Indexing and Slicing (`.loc` and `.iloc`)

*   **`.loc`**: Label-based indexing. Used for selecting data by row and column labels.
*   **`.iloc`**: Integer-location based indexing. Used for selecting data by integer position.

```python
# df = pd.read_csv('sample_data.csv')
# print(df.loc[0]) # Select row with label 0
# print(df.loc[0:2, 'Name':'Age']) # Select rows 0 to 2, and columns from 'Name' to 'Age'

# print(df.iloc[0]) # Select row at integer position 0
# print(df.iloc[0:3, 0:2]) # Select rows 0 to 2, and columns 0 to 1
```

#### Filtering Data

You can filter DataFrames based on conditions.

```python
# df = pd.read_csv('sample_data.csv')
# young_people = df[df['Age'] < 30]
# print(young_people)

# Multiple conditions
# young_and_male = df[(df['Age'] < 30) & (df['Gender'] == 'Male')]
# print(young_and_male)
```

#### Handling Missing Data

*   `df.isnull()`: Returns a DataFrame of booleans indicating missing values.
*   `df.dropna()`: Removes rows or columns with missing values.
*   `df.fillna(value)`: Fills missing values with a specified value.

```python
# df_missing = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
# print(df_missing.isnull())
# print(df_missing.dropna())
# print(df_missing.fillna(0))
```

#### Adding/Modifying Columns

You can add new columns or modify existing ones easily.

```python
# df = pd.read_csv('sample_data.csv')
# df['Is_Adult'] = df['Age'] >= 18 # Add a new boolean column
# print(df.head())

# df['Age_in_Months'] = df['Age'] * 12 # Modify an existing column or create new
# print(df.head())
```

#### Grouping and Aggregation (`groupby`)

`groupby()` is used to group rows based on one or more columns and then apply an aggregation function (e.g., `sum`, `mean`, `count`).

```python
# df = pd.read_csv('sample_data.csv')
# avg_age_by_city = df.groupby('City')['Age'].mean()
# print(avg_age_by_city)

# Multiple aggregations
# city_stats = df.groupby('City').agg({'Age': 'mean', 'Salary': 'sum'})
# print(city_stats)
```

---

### Quiz

1.  **What is the primary data structure in `pandas` for tabular data?**
    a) `Series`
    b) `DataFrame`
    c) `Panel`

2.  **Which function is used to read a CSV file into a DataFrame?**
    a) `pd.load_csv()`
    b) `pd.read_csv()`
    c) `pd.import_csv()`

3.  **How would you select only the 'Name' and 'City' columns from a DataFrame named `df`?**
    a) `df['Name', 'City']`
    b) `df[['Name', 'City']]`
    c) `df.select('Name', 'City')`

4.  **To filter a DataFrame `df` to show only rows where the 'Age' column is greater than 25, which of the following is correct?**
    a) `df.filter(df['Age'] > 25)`
    b) `df[df['Age'] > 25]`
    c) `df.where(df['Age'] > 25)`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
  3. b
  4. b
</details>