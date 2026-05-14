# Lesson 10: Dictionaries

In this lesson, you'll learn about **Dictionaries**, another fundamental and highly useful data structure in Python. Unlike lists, which are ordered collections accessed by numerical indices, dictionaries are unordered collections of **key-value pairs**.

## What are Dictionaries?

A dictionary is a collection which is:

*   **Unordered** (as of Python 3.7, they are insertion-ordered, meaning the order in which items are added is preserved, but they are not sorted by key).
*   **Changeable** (mutable): You can add, remove, and modify key-value pairs after creation.
*   **Indexed** by keys: You access items using unique keys, not numerical indices.
*   **Key-Value Pairs:** Each item in a dictionary consists of a `key` and its associated `value`. Keys must be unique and immutable (e.g., strings, numbers, tuples). Values can be of any data type.

Think of a dictionary like a real-world dictionary or a phone book: you look up a word (the key) to find its definition (the value), or a person's name (the key) to find their phone number (the value).

## Creating a Dictionary

Dictionaries are created using curly braces `{}`. Each key-value pair is separated by a colon (`:`), and pairs are separated by commas.

**Syntax:**

```python
my_dict = {
    key1: value1,
    key2: value2,
    # ...
}
```

**Examples:**

```python
# A dictionary representing a person's information
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# A dictionary storing product prices
prices = {
    "apple": 1.00,
    "banana": 0.50,
    "orange": 0.75
}
print(prices)

# An empty dictionary
empty_dict = {}
print(empty_dict)
```

## Accessing Items

You access the values in a dictionary by referring to their associated key, inside square brackets `[]`.

**Syntax:**

```python
value = dictionary_name[key]
```

**Examples:**

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30

# If you try to access a key that doesn't exist, it will raise a KeyError
# print(person["country"]) # This would cause an error!

# Using the .get() method (safer way to access)
# The .get() method returns None if the key does not exist, or a default value if specified.
print(person.get("city"))    # Output: New York
print(person.get("country")) # Output: None
print(person.get("country", "Unknown")) # Output: Unknown
```

## Adding and Modifying Items

Dictionaries are mutable, so you can add new key-value pairs or change the values of existing keys.

**Adding a new item:**

```python
person = {"name": "Alice", "age": 30}
person["city"] = "New York" # Add a new key-value pair
print(person) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

**Modifying an existing item:**

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
person["age"] = 31 # Change the value associated with the 'age' key
print(person) # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
```

## Removing Items

*   **`del` keyword:** Removes a key-value pair.
    ```python
    person = {"name": "Alice", "age": 30, "city": "New York"}
    del person["city"]
    print(person) # Output: {'name': 'Alice', 'age': 30}
    ```

*   **`.pop(key)` method:** Removes the item with the specified key and returns its value.
    ```python
    person = {"name": "Alice", "age": 30, "city": "New York"}
    removed_city = person.pop("city")
    print(person)      # Output: {'name': 'Alice', 'age': 30}
    print(removed_city) # Output: New York
    ```

*   **`.clear()` method:** Removes all items from the dictionary.
    ```python
    person = {"name": "Alice", "age": 30}
    person.clear()
    print(person) # Output: {}
    ```

## Looping Through a Dictionary

You can iterate over dictionaries in several ways using `for` loops:

```python
student = {
    "name": "Bob",
    "grade": "A",
    "major": "Computer Science"
}

print("\nLooping through keys:")
for key in student:
    print(key) # Prints: name, grade, major

print("\nLooping through values:")
for value in student.values():
    print(value) # Prints: Bob, A, Computer Science

print("\nLooping through key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")
# Prints:
# name: Bob
# grade: A
# major: Computer Science
```

Dictionaries are incredibly powerful for organizing and retrieving data using meaningful keys.

---

### Quiz

1.  **How do you access the value associated with a key in a dictionary?**
    a) `my_dict(key)`
    b) `my_dict[key]`
    c) `my_dict.get_key(key)`

2.  **Are dictionaries ordered?**
    a) Yes, always.
    b) No, never.
    c) As of Python 3.7, they are insertion ordered.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
</details>