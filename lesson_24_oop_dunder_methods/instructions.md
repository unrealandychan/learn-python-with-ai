# Lesson 24: OOP: Dunder (Magic) Methods

In Python, you'll often encounter methods that start and end with double underscores, like `__init__` or `__str__`. These are known as **dunder methods** (short for "double underscore methods") or **magic methods**.

Dunder methods allow you to define how objects of your class behave with built-in operations, functions, and syntax. They enable your objects to support features like arithmetic operations, comparisons, string representation, iteration, and more, making your custom classes behave like built-in types.

## Common Dunder Methods

Here are some of the most commonly used dunder methods:

1.  **`__init__(self, ...)`: The Constructor**
    *   We've already seen this one! It's called automatically when a new object is created. It initializes the object's attributes.
    ```python
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author
    ```

2.  **`__str__(self)`: String Representation for Users**
    *   Defines the "informal" string representation of an object. This is what you see when you use `print()` or `str()` on an object.
    *   It should be readable and provide a user-friendly description.
    ```python
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __str__(self):
            return f"'{self.title}' by {self.author}"

    my_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    print(my_book) # Output: 'The Great Gatsby' by F. Scott Fitzgerald
    ```

3.  **`__repr__(self)`: String Representation for Developers**
    *   Defines the "official" string representation of an object. This is what you see when you type an object's name in the Python interpreter or use `repr()`.
    *   It should be unambiguous and, if possible, look like a valid Python expression that could recreate the object.
    ```python
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __repr__(self):
            return f"Book(title='{self.title}', author='{self.author}')"

    my_book = Book("1984", "George Orwell")
    print(repr(my_book)) # Output: Book(title='1984', author='George Orwell')
    ```
    *   **Note:** If `__str__` is not defined, `__repr__` is used as a fallback for `str()`. It's good practice to define both.

4.  **`__len__(self)`: Length of the Object**
    *   Defines the behavior for the built-in `len()` function.
    *   It should return an integer representing the length of the object.
    ```python
    class MyList:
        def __init__(self, items):
            self.items = items

        def __len__(self):
            return len(self.items)

    my_list_obj = MyList([1, 2, 3, 4, 5])
    print(len(my_list_obj)) # Output: 5
    ```

5.  **`__getitem__(self, key)`: Accessing Items by Index/Key**
    *   Defines the behavior for accessing items using square brackets (e.g., `obj[key]`).
    ```python
    class MyContainer:
        def __init__(self, data):
            self.data = data

        def __getitem__(self, index):
            return self.data[index]

    container = MyContainer(["A", "B", "C"])
    print(container[0]) # Output: A
    ```

6.  **`__add__(self, other)`: Overloading the `+` Operator**
    *   Defines the behavior for the `+` operator when used with objects of your class.
    ```python
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __str__(self):
            return f"Vector({self.x}, {self.y})"

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(v3) # Output: Vector(4, 6)
    ```

There are many other dunder methods for various operations (e.g., `__eq__` for `==`, `__lt__` for `<`, `__call__` to make an object callable, etc.). By implementing these methods, you can make your custom classes behave just like Python's built-in types, leading to more intuitive and Pythonic code.

--- 

### Quiz

1.  **Which dunder method is called by the `str()` function?**
    a) `__repr__`
    b) `__string__`
    c) `__str__`

2.  **Which dunder method is used to overload the `+` operator?**
    a) `__plus__`
    b) `__add__`
    c) `__sum__`

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. b
</details>