# Lesson 07: List Methods & Operations

Lists are dynamic and come with a rich set of built-in **methods** that allow you to modify, query, and manipulate their contents efficiently. Understanding these methods is key to working effectively with lists.

## Common List Methods

Here are some of the most frequently used list methods:

1.  **`append(item)`:** Adds a single `item` to the end of the list.
    ```python
    fruits = ["apple", "banana"]
    fruits.append("cherry")
    print(fruits)  # Output: ['apple', 'banana', 'cherry']
    ```

2.  **`insert(index, item)`:** Inserts an `item` at a specified `index`.
    ```python
    fruits = ["apple", "cherry"]
    fruits.insert(1, "banana") # Insert 'banana' at index 1
    print(fruits)  # Output: ['apple', 'banana', 'cherry']
    ```

3.  **`remove(value)`:** Removes the first occurrence of the specified `value` from the list. If the value is not found, it raises a `ValueError`.
    ```python
    fruits = ["apple", "banana", "cherry", "banana"]
    fruits.remove("banana")
    print(fruits)  # Output: ['apple', 'cherry', 'banana']
    ```

4.  **`pop(index=-1)`:** Removes and returns the item at the given `index`. If no index is specified, it removes and returns the last item.
    ```python
    fruits = ["apple", "banana", "cherry"]
    removed_item = fruits.pop(1) # Remove item at index 1
    print(fruits)        # Output: ['apple', 'cherry']
    print(removed_item)  # Output: banana

    last_item = fruits.pop() # Remove the last item
    print(fruits)        # Output: ['apple']
    print(last_item)     # Output: cherry
    ```

5.  **`sort(key=None, reverse=False)`:** Sorts the items of the list in place (modifies the original list). By default, it sorts in ascending order. You can use `reverse=True` for descending order.
    ```python
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers.sort()
    print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

    words = ["banana", "apple", "cherry"]
    words.sort(reverse=True)
    print(words)    # Output: ['cherry', 'banana', 'apple']
    ```

6.  **`reverse()`:** Reverses the order of elements in the list in place.
    ```python
    numbers = [1, 2, 3, 4, 5]
    numbers.reverse()
    print(numbers)  # Output: [5, 4, 3, 2, 1]
    ```

7.  **`count(value)`:** Returns the number of times a specified `value` appears in the list.
    ```python
    numbers = [1, 2, 2, 3, 2, 4]
    count_of_2 = numbers.count(2)
    print(count_of_2) # Output: 3
    ```

8.  **`index(value, start=0, end=len(list))`:** Returns the index of the first occurrence of the specified `value`. Raises a `ValueError` if the value is not present.
    ```python
    fruits = ["apple", "banana", "cherry"]
    index_banana = fruits.index("banana")
    print(index_banana) # Output: 1
    ```

9.  **`clear()`:** Removes all items from the list, making it empty.
    ```python
    my_list = [1, 2, 3]
    my_list.clear()
    print(my_list) # Output: []
    ```

## Built-in Functions for Lists

Besides methods, there are also useful built-in Python functions that work with lists:

*   **`len(list)`:** Returns the number of items (length) in a list.
    ```python
    fruits = ["apple", "banana", "cherry"]
    length = len(fruits)
    print(length)  # Output: 3
    ```

*   **`min(list)` / `max(list)`:** Returns the smallest/largest item in a list.
    ```python
    numbers = [3, 1, 4, 2]
    print(min(numbers)) # Output: 1
    print(max(numbers)) # Output: 4
    ```

*   **`sum(list)`:** Returns the sum of all items in a list of numbers.
    ```python
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(total) # Output: 15
    ```

These methods and functions provide powerful tools for managing and manipulating data stored in lists, making them incredibly flexible for various programming tasks.

--- 

### Quiz

1.  **Which method adds an element to the very end of a list?**
    a) `insert()`
    b) `add()`
    c) `append()`

2.  **What is the difference between `remove()` and `pop()`?**
    a) `remove()` uses an index, `pop()` uses a value.
    b) `remove()` uses a value, `pop()` uses an index.
    c) They are the same.

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. b
</details>