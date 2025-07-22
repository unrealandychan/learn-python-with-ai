# Lesson 11: Tuples & Sets

In this lesson, you'll explore two more important built-in data structures in Python: **Tuples** and **Sets**. While they share some similarities with lists and dictionaries, they each have unique characteristics that make them suitable for different use cases.

## Tuples

A **tuple** is an ordered collection of items, similar to a list. However, the key difference is that tuples are **immutable**, meaning once a tuple is created, you cannot change, add, or remove its items.

**Characteristics of Tuples:**

*   **Ordered:** Items have a defined order that does not change.
*   **Immutable:** Cannot be changed after creation. This makes them useful for data that should not be modified, like coordinates or database records.
*   **Allow Duplicates:** Tuples can contain duplicate items.
*   **Heterogeneous:** Can contain items of different data types.

**Creating a Tuple:**

Tuples are created using round brackets `()`.

**Syntax:**

```python
my_tuple = (item1, item2, item3, ...)
```

**Examples:**

```python
# A tuple of numbers
coordinates = (10, 20, 30)
print(coordinates) # Output: (10, 20, 30)

# A tuple of strings
days_of_week = ("Monday", "Tuesday", "Wednesday")
print(days_of_week) # Output: ('Monday', 'Tuesday', 'Wednesday')

# A tuple with mixed data types
mixed_tuple = ("hello", 123, True)
print(mixed_tuple) # Output: ('hello', 123, True)

# A tuple with a single item (note the comma!)
single_item_tuple = ("apple",)
print(single_item_tuple) # Output: ('apple',)
print(type(single_item_tuple)) # Output: <class 'tuple'>

# Without the comma, it's just a string in parentheses
not_a_tuple = ("apple")
print(type(not_a_tuple)) # Output: <class 'str'>
```

**Accessing Tuple Items:**

Like lists, tuple items are accessed using indexing and slicing.

```python
my_tuple = ("apple", "banana", "cherry", "date")

print(my_tuple[0])   # Output: apple
print(my_tuple[-1])  # Output: date
print(my_tuple[1:3]) # Output: ('banana', 'cherry')
```

**Immutability Example:**

```python
my_tuple = (1, 2, 3)
# The following line would cause a TypeError because tuples are immutable:
# my_tuple[0] = 5
# print(my_tuple)
```

## Sets

A **set** is an unordered collection of **unique** items. This means that a set cannot have duplicate elements.

**Characteristics of Sets:**

*   **Unordered:** Items in a set do not have a defined order. You cannot access items by index.
*   **Unindexed:** You cannot refer to items by index or key.
*   **Mutable:** You can add and remove items after the set has been created.
*   **No Duplicates:** Sets automatically remove duplicate items.

**Creating a Set:**

Sets are created using curly braces `{}`. To create an empty set, you must use `set()` (because `{}` creates an empty dictionary).

**Syntax:**

```python
my_set = {item1, item2, item3, ...}
empty_set = set()
```

**Examples:**

```python
# A set of numbers (duplicates are automatically removed)
numbers_set = {1, 2, 3, 2, 1}
print(numbers_set) # Output: {1, 2, 3} (order might vary)

# A set of strings
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set) # Output: {'banana', 'cherry', 'apple'} (order might vary)

# Creating an empty set
empty_set = set()
print(empty_set) # Output: set()
```

**Adding and Removing Items from Sets:**

*   **`add(item)`:** Adds a single item to the set.
    ```python
    fruits_set = {"apple", "banana"}
    fruits_set.add("orange")
    print(fruits_set) # Output: {'banana', 'orange', 'apple'}
    fruits_set.add("banana") # Adding a duplicate has no effect
    print(fruits_set) # Output: {'banana', 'orange', 'apple'}
    ```

*   **`remove(item)`:** Removes the specified item. Raises a `KeyError` if the item is not found.
    ```python
    fruits_set = {"apple", "banana", "cherry"}
    fruits_set.remove("banana")
    print(fruits_set) # Output: {'cherry', 'apple'}
    ```

*   **`discard(item)`:** Removes the specified item if it is present. Does NOT raise an error if the item is not found.
    ```python
    fruits_set = {"apple", "cherry"}
    fruits_set.discard("banana") # No error, even if 'banana' is not there
    print(fruits_set) # Output: {'cherry', 'apple'}
    ```

*   **`pop()`:** Removes and returns an arbitrary item from the set (since sets are unordered, you don't know which item will be removed).
    ```python
    my_set = {1, 2, 3}
    popped_item = my_set.pop()
    print(my_set) # Output: {2, 3} (or {1, 3} etc.)
    print(popped_item) # Output: 1 (or 2 or 3)
    ```

## When to use Tuples vs. Lists vs. Sets

*   **Lists:** When you need an ordered, changeable collection that can contain duplicate items (e.g., a list of tasks, a sequence of numbers).
*   **Tuples:** When you need an ordered, unchangeable collection (e.g., coordinates, RGB color values, database records that shouldn't be altered).
*   **Sets:** When you need an unordered collection of unique items, and you want to perform mathematical set operations like union, intersection, difference (e.g., storing unique IDs, finding common elements between two groups).

--- 

### Quiz

1.  **What is the main difference between a list and a tuple?**
    a) Lists are ordered, tuples are not.
    b) Lists are mutable, tuples are immutable.
    c) Lists can store duplicates, tuples cannot.

2.  **What happens if you add a duplicate item to a set?**
    a) It raises an error.
    b) It stores both items.
    c) It is ignored.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
</details>