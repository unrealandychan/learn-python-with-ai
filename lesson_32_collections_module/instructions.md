# Lesson 32: The `collections` Module

Python's standard library is vast and powerful. The `collections` module is a part of it that provides specialized container datatypes, offering alternatives to Python's general-purpose built-in containers like `dict`, `list`, and `tuple`. These specialized containers can make your code more efficient, readable, and convenient for specific use cases.

## 1. `Counter`

A `Counter` is a `dict` subclass for counting hashable objects. It's an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. It's incredibly useful for frequency counting.

**Example:**

```python
from collections import Counter

# Counting characters in a string
text = "abracadabra"
char_counts = Counter(text)
print(char_counts) # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Counting words in a list
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)
print(word_counts) # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Accessing counts
print(char_counts['a']) # Output: 5
print(char_counts['z']) # Output: 0 (doesn't raise KeyError)

# Finding most common elements
print(word_counts.most_common(2)) # Output: [('apple', 3), ('banana', 2)]
```

## 2. `defaultdict`

A `defaultdict` is a subclass of `dict` that calls a factory function to supply missing values. When you try to access a key that doesn't exist, `defaultdict` automatically creates it and assigns a default value (determined by the factory function) instead of raising a `KeyError`.

**Example:**

```python
from collections import defaultdict

# Grouping items by category
# Using list as the default factory: if a key is missing, an empty list is created
category_items = defaultdict(list)

items = [('fruit', 'apple'), ('vegetable', 'carrot'), ('fruit', 'banana')]

for category, item in items:
    category_items[category].append(item)

print(category_items) # Output: defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']})

# Using int as the default factory: if a key is missing, 0 is created
word_counts = defaultdict(int)
sentence = "hello world hello"
for word in sentence.split():
    word_counts[word] += 1
print(word_counts) # Output: defaultdict(<class 'int'>, {'hello': 2, 'world': 1})
```

## 3. `namedtuple`

A `namedtuple` is a factory function for creating tuple subclasses with named fields. This means you can access elements of the tuple by name instead of by index, making your code more readable and self-documenting.

**Example:**

```python
from collections import namedtuple

# Define a Point namedtuple with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])

# Create instances of Point
p1 = Point(10, 20)
p2 = Point(x=30, y=40)

print(p1.x) # Access by name: Output: 10
print(p2.y) # Access by name: Output: 40

# Still behaves like a tuple (can access by index)
print(p1[0]) # Output: 10

# Namedtuples are immutable, like regular tuples
# p1.x = 50 # This would raise an AttributeError

# Define a Car namedtuple
Car = namedtuple('Car', 'make model year')
my_car = Car('Toyota', 'Camry', 2020)
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")
```

These specialized data structures from the `collections` module can significantly improve the clarity and efficiency of your Python code for specific tasks.

--- 

### Quiz

1.  **Which `collections` class would be best for counting the frequency of words in a text?**
    a) `defaultdict`
    b) `namedtuple`
    c) `Counter`

2.  **What is the advantage of `defaultdict` over a regular dictionary?**
    a) It is faster.
    b) It does not raise a `KeyError` if a key is not found.
    c) It is ordered.

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. b
</details>