# Lesson 23: OOP: Encapsulation (Public, Protected, Private)

**Encapsulation** is one of the core principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and the methods (functions) that operate on that data into a single unit, which is a class. It also involves restricting direct access to some of an object's components, preventing unintended interference and misuse.

In Python, encapsulation is achieved through naming conventions, as there are no strict access modifiers like `public`, `private`, or `protected` as found in some other languages (e.g., Java, C++).

## Access Modifiers in Python (by Convention)

Python uses a convention of prefixes to indicate the intended visibility of attributes and methods:

1.  **Public Members (No prefix):**
    *   Attributes and methods without any leading underscores are considered public.
    *   They can be accessed from anywhere, both inside and outside the class.
    *   **Example:** `self.attribute_name`, `self.method_name()`

    ```python
    class MyClass:
        def __init__(self):
            self.public_attribute = "I am public"

        def public_method(self):
            print("This is a public method.")

    obj = MyClass()
    print(obj.public_attribute) # Accessible
    obj.public_method()         # Accessible
    ```

2.  **Protected Members (Single leading underscore `_`):**
    *   Attributes and methods prefixed with a single underscore (e.g., `_protected_attribute`) are considered "protected."
    *   This is a **convention** to indicate that they are intended for internal use within the class or by its subclasses.
    *   Python does not strictly prevent access from outside the class, but it's a strong hint to developers not to access them directly.
    *   **Example:** `self._protected_attribute`, `self._protected_method()`

    ```python
    class MyClass:
        def __init__(self):
            self._protected_attribute = "I am protected"

        def _protected_method(self):
            print("This is a protected method.")

    obj = MyClass()
    print(obj._protected_attribute) # Accessible, but discouraged
    obj._protected_method()         # Accessible, but discouraged
    ```

3.  **Private Members (Double leading underscore `__`):**
    *   Attributes and methods prefixed with a double underscore (e.g., `__private_attribute`) are considered "private."
    *   Python performs **name mangling** on these members. This means the interpreter changes the name of the attribute/method to `_ClassName__private_attribute`.
    *   This makes them harder to access directly from outside the class, providing a stronger form of encapsulation.
    *   **Example:** `self.__private_attribute`, `self.__private_method()`

    ```python
    class MyClass:
        def __init__(self):
            self.__private_attribute = "I am private"

        def __private_method(self):
            print("This is a private method.")

        def public_access_private(self):
            print(f"Accessing private from public method: {self.__private_attribute}")
            self.__private_method()

    obj = MyClass()
    # print(obj.__private_attribute) # This would cause an AttributeError!
    # obj.__private_method()         # This would cause an AttributeError!

    obj.public_access_private() # Accessible through a public method
    # Output:
    # Accessing private from public method: I am private
    # This is a private method.

    # You can technically access it via name mangling, but it's highly discouraged:
    print(obj._MyClass__private_attribute) # Output: I am private
    ```

## Benefits of Encapsulation

*   **Data Hiding:** Prevents direct, unauthorized access to an object's internal state, reducing the risk of accidental modification.
*   **Control:** Allows you to control how data is accessed and modified through public methods (getters and setters), enabling validation or other logic.
*   **Flexibility:** You can change the internal implementation of a class without affecting the code that uses the class, as long as the public interface remains the same.
*   **Maintainability:** Makes code easier to maintain and debug by localizing changes and reducing dependencies.

Encapsulation is a key principle for building robust, maintainable, and scalable object-oriented applications.

--- 

### Quiz

1.  **How do you denote a private attribute in Python?**
    a) `private attribute_name`
    b) `__attribute_name`
    c) `_attribute_name`

2.  **What is the main purpose of encapsulation?**
    a) To make code faster.
    b) To bundle data and methods together and control access.
    c) To make attributes public.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>