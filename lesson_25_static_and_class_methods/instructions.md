# Lesson 25: Static and Class Methods

In Python, methods within a class can behave differently based on how they are defined. Beyond the regular **instance methods** (which take `self` as their first argument and operate on an instance of the class), Python offers **class methods** and **static methods**.

## 1. Instance Methods

These are the most common type of methods. They operate on an instance of the class and can access or modify the instance's attributes. They always take `self` as their first parameter, which refers to the instance itself.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print(f"Instance method called. Value: {self.value}")

obj = MyClass(10)
obj.instance_method() # Output: Instance method called. Value: 10
```

## 2. Class Methods (`@classmethod`)

Class methods operate on the class itself, rather than on an instance of the class. They are defined using the `@classmethod` decorator and take `cls` (conventionally, short for class) as their first parameter.

**Use Cases:**

*   **Alternative Constructors:** To create instances of the class in different ways.
*   **Accessing Class-level Data:** To modify or access class attributes (attributes shared by all instances).

**Example:**

```python
class Car:
    wheels = 4 # Class attribute

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def get_wheels_count(cls):
        # cls refers to the Car class itself
        print(f"All cars have {cls.wheels} wheels.")

    @classmethod
    def from_string(cls, car_string):
        # An alternative constructor
        brand, model = car_string.split('-')
        # cls() is equivalent to Car()
        return cls(brand + " " + model) # Creates a new Car instance

Car.get_wheels_count() # Output: All cars have 4 wheels.

my_car = Car.from_string("Toyota-Camry")
print(my_car.brand) # Output: Toyota Camry
```

## 3. Static Methods (`@staticmethod`)

Static methods are defined using the `@staticmethod` decorator. They do not take `self` or `cls` as their first parameter. They are essentially regular functions that happen to be defined within a class's namespace. They cannot access or modify instance-specific data or class-specific data.

**Use Cases:**

*   **Utility Functions:** When a function logically belongs to a class but doesn't need to operate on an instance or the class itself.
*   **No `self` or `cls` access:** If your method doesn't use `self` or `cls`, it can often be a static method.

**Example:**

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Call static methods directly on the class
print(MathOperations.add(5, 3))     # Output: 8
print(MathOperations.multiply(4, 2)) # Output: 8

# You can also call them on an instance, but it's less common
math_obj = MathOperations()
print(math_obj.add(1, 1)) # Output: 2
```

## Summary of Method Types

| Method Type     | First Argument | Can Access Instance Data? | Can Access Class Data? | Common Use Cases                               |
| :-------------- | :------------- | :------------------------ | :--------------------- | :--------------------------------------------- |
| **Instance**    | `self`         | Yes                       | Yes                    | Operate on object-specific data                |
| **Class**       | `cls`          | No (directly)             | Yes                    | Alternative constructors, class-level operations |
| **Static**      | None           | No                        | No                     | Utility functions, logical grouping            |

Choosing the right method type helps in designing cleaner, more organized, and more efficient object-oriented code.

--- 

### Quiz

1.  **Which decorator is used to define a class method?**
    a) `@staticmethod`
    b) `@classmethod`
    c) `@instancemethod`

2.  **What is the first argument of a static method?**
    a) `self`
    b) `cls`
    c) It has no special first argument.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
</details>