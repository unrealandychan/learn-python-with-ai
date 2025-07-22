# Lesson 21: OOP: Inheritance

In Object-Oriented Programming (OOP), **Inheritance** is a fundamental concept that allows a new class to be based on an existing class. This means the new class (called the **child class** or **subclass**) inherits all the attributes and methods of the existing class (called the **parent class** or **superclass**).

## Why Use Inheritance?

Inheritance promotes **code reusability** and helps establish a clear **"is-a" relationship** between classes. For example, a `Dog` *is a* `Animal`, and a `Car` *is a* `Vehicle`.

*   **Code Reusability:** You don't have to write the same code multiple times. Common attributes and behaviors can be defined in a parent class and reused by multiple child classes.
*   **Maintainability:** Changes to the parent class automatically propagate to all child classes, reducing the effort needed for updates.
*   **Extensibility:** New features can be added to child classes without modifying the parent class.
*   **Polymorphism:** (We'll cover this in the next lesson) Allows objects of different classes to be treated as objects of a common type.

## Defining a Parent Class and a Child Class

To create a child class that inherits from a parent class, you include the parent class name in parentheses after the child class name in its definition.

**Syntax:**

```python
class ParentClass:
    # Parent class attributes and methods
    pass

class ChildClass(ParentClass):
    # Child class attributes and methods
    # It inherits everything from ParentClass
    pass
```

**Example: `Animal` (Parent) and `Dog` (Child)**

Let's define a general `Animal` class and then a more specific `Dog` class that inherits from `Animal`.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic animal sound")

    def describe(self):
        print(f"{self.name} is a {self.species}.")

# Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class's __init__ method
        # This ensures that name and species (which is fixed for Dog) are initialized
        super().__init__(name, species="Dog")
        self.breed = breed

    # Dog can override the make_sound method from Animal
    def make_sound(self):
        print("Woof! Woof!")

    # Dog can have its own new methods
    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# Create instances
my_animal = Animal("Leo", "Lion")
my_dog = Dog("Buddy", "Golden Retriever")

# Access inherited attributes and methods
my_animal.describe() # Output: Leo is a Lion.
my_animal.make_sound() # Output: Generic animal sound

my_dog.describe()    # Output: Buddy is a Dog. (Inherited from Animal)
my_dog.make_sound()  # Output: Woof! Woof! (Overridden in Dog)
my_dog.fetch()       # Output: Buddy is fetching the ball. (Specific to Dog)

print(f"Buddy's breed: {my_dog.breed}") # Accessing Dog's own attribute
```

### The `super()` Function

The `super()` function is a special function that allows you to call methods from the parent class. It's most commonly used in the `__init__` method of the child class to ensure that the parent class's attributes are properly initialized.

```python
class Parent:
    def __init__(self, value):
        self.value = value

class Child(Parent):
    def __init__(self, value, extra_value):
        super().__init__(value) # Calls Parent.__init__(self, value)
        self.extra_value = extra_value

c = Child(10, 20)
print(c.value)       # Output: 10
print(c.extra_value) # Output: 20
```

Inheritance is a cornerstone of OOP, enabling you to build hierarchical relationships between classes and create more organized and efficient codebases.

--- 

### Quiz

1.  **What is the class that is being inherited from called?**
    a) Child class
    b) Superclass (or Parent class)
    c) Subclass

2.  **How do you specify that a class should inherit from another class?**
    a) `class Child(Parent):`
    b) `class Child inherits Parent:`
    c) `class Child extends Parent:`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>