# Lesson 19: Introduction to Object-Oriented Programming (Classes & Objects)

Up until now, you've been writing procedural code, where instructions are executed step-by-step. In this lesson, you'll be introduced to **Object-Oriented Programming (OOP)**, a powerful paradigm that helps organize code into reusable, modular components.

## What is Object-Oriented Programming (OOP)?

OOP is a programming paradigm based on the concept of "objects", which can contain data (attributes or properties) and code (methods or functions) that operate on that data. The goal of OOP is to model real-world entities as software objects.

**Key Concepts in OOP:**

*   **Class:** A blueprint or a template for creating objects. It defines the attributes (data) and methods (functions) that all objects of that class will have.
*   **Object (Instance):** A specific instance of a class. When you create an object, you're creating a concrete item based on the class's blueprint.
*   **Attribute:** A variable associated with a class or an object. It represents the data or properties of the object.
*   **Method:** A function that belongs to a class or an object. Methods define the behaviors or actions that objects of the class can perform.

## Defining a Class

In Python, you define a class using the `class` keyword, followed by the class name and a colon. Class names typically follow the `CamelCase` convention.

**Syntax:**

```python
class ClassName:
    # Class attributes (optional)
    # Methods (functions within the class)
    pass # Placeholder if the class body is empty
```

**Example: A simple `Dog` class**

```python
class Dog:
    # Class attribute (shared by all instances of Dog)
    species = "Canis familiaris"

    # Method: a function that belongs to the class
    def bark(self):
        print("Woof! Woof!")

    def describe(self):
        print("This is a dog.")
```

## Creating Objects (Instances)

To create an object (or instance) of a class, you call the class name as if it were a function.

**Syntax:**

```python
object_name = ClassName()
```

**Example:**

```python
my_dog = Dog() # Create an object named my_dog from the Dog class
your_dog = Dog() # Create another object named your_dog

# Accessing methods using the object
my_dog.bark()   # Output: Woof! Woof!
your_dog.describe() # Output: This is a dog.
```

## The `__init__()` Method (Constructor)

The `__init__()` method is a special method in Python classes. It's often called the **constructor** because it's automatically called whenever a new object of the class is created. It's used to initialize the object's attributes.

*   The first parameter of any method in a class, including `__init__()`, is always `self`. `self` refers to the instance of the class itself. It allows you to access the attributes and methods of that specific object.

**Syntax:**

```python
class ClassName:
    def __init__(self, param1, param2, ...):
        self.attribute1 = param1
        self.attribute2 = param2
        # ...
```

**Example: `Dog` class with `__init__` and attributes**

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Initialize instance attributes
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")

    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.species}."

# Create Dog objects, passing arguments to the __init__ method
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Access attributes
print(f"{dog1.name} is {dog1.age} years old.") # Output: Buddy is 3 years old.
print(f"{dog2.name} is {dog2.age} years old.") # Output: Lucy is 5 years old.

# Call methods
dog1.bark() # Output: Woof! Woof!
print(dog2.get_info()) # Output: Lucy is a 5-year-old Canis familiaris.
```

OOP is a fundamental concept in modern software development. It helps in creating modular, reusable, and maintainable code by modeling real-world entities and their interactions.

--- 

### Quiz

1.  **What is a class?**
    a) An instance of an object.
    b) A blueprint for creating objects.
    c) A function.

2.  **What is the `__init__()` method used for?**
    a) To destroy an object.
    b) To initialize an object's attributes.
    c) To print an object.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>