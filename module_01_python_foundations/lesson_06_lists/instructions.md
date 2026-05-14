# Lesson 06: Lists: Creation, Indexing, and Slicing

In this lesson, you'll learn about **Lists**, which are one of the most versatile and widely used data structures in Python. Lists allow you to store multiple items in a single variable.

## What are Lists?

A list is an ordered, mutable (changeable) collection of items. This means:

*   **Ordered:** The items have a defined order, and that order will not change. New items are added to the end of the list.
*   **Mutable:** You can change, add, and remove items after the list has been created.
*   **Collection:** A list can hold items of different data types (e.g., integers, strings, floats, even other lists).

## Creating a List

Lists are created using square brackets `[]`, with items separated by commas.

**Syntax:**

```python
my_list = [item1, item2, item3, ...]
```

**Examples:**

```python
# A list of strings
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)

# A list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# A list with mixed data types
mixed_list = ["hello", 123, 3.14, True]
print(mixed_list)

# An empty list
empty_list = []
print(empty_list)
```

## Accessing Items (Indexing)

Each item in a list has an assigned index number, which represents its position. Python uses **zero-based indexing**, meaning the first item has an index of `0`, the second `1`, and so on.

You can access individual items by referring to their index number inside square brackets.

**Syntax:**

```python
list_name[index]
```

**Examples:**

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])  # Output: apple (the first item)
print(fruits[1])  # Output: banana (the second item)
print(fruits[3])  # Output: date (the fourth item)

# Negative indexing: Access items from the end of the list
print(fruits[-1]) # Output: date (the last item)
print(fruits[-2]) # Output: cherry (the second to last item)
```

## Slicing Lists

Slicing allows you to get a portion (a sub-list) of a list. You specify a `start` index and an `end` index, separated by a colon.

**Syntax:**

```python
list_name[start:end]  # Items from start up to (but not including) end
list_name[start:]     # Items from start to the end of the list
list_name[:end]       # Items from the beginning up to (but not including) end
list_name[:]          # A copy of the entire list
```

**Examples:**

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[1:4])   # Output: [20, 30, 40] (items at index 1, 2, 3)
print(numbers[3:])    # Output: [40, 50, 60, 70] (from index 3 to the end)
print(numbers[:5])    # Output: [10, 20, 30, 40, 50] (from beginning up to index 5)
print(numbers[::2])   # Output: [10, 30, 50, 70] (every second item)
print(numbers[::-1])  # Output: [70, 60, 50, 40, 30, 20, 10] (reverse the list)
```

Lists are incredibly powerful and form the basis for many data operations in Python. Mastering their creation, indexing, and slicing is a crucial step.

--- 

### Quiz

1.  **What is the index of the first element in a list?**
    a) 1
    b) 0
    c) -1

2.  **What would `my_list[1:3]` return for `my_list = [10, 20, 30, 40]`?**
    a) `[20, 30, 40]`
    b) `[10, 20]`
    c) `[20, 30]`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
</details>