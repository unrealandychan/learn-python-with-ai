# Lesson 22: OOP: Polymorphism & Method Overriding

In Object-Oriented Programming, **Polymorphism** is a powerful concept that means "many forms." In Python, it allows objects of different classes to be treated as objects of a common type. This is often achieved through **method overriding**.

## Polymorphism

Polymorphism allows you to write code that can work with objects of various classes, as long as those classes share a common interface (i.e., they have methods with the same names).

**Example:**

Consider different types of animals that all make a sound. Even though the sound is different, the action is the same (`make_sound`).

```python
class Animal:
    def make_sound(self):
        pass # Placeholder for a generic sound

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

# A function that can take any Animal object
def animal_sound(animal):
    animal.make_sound()

# Create instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Call the same function with different animal objects
animal_sound(dog) # Output: Woof!
animal_sound(cat) # Output: Meow!
animal_sound(cow) # Output: Moo!
```

In this example, the `animal_sound` function doesn't care what specific type of `Animal` it receives, as long as that animal has a `make_sound` method. This is polymorphism in action.

## Method Overriding

**Method overriding** occurs when a child class provides its own specific implementation of a method that is already defined in its parent class. When you call that method on an object of the child class, the child's version of the method is executed instead of the parent's.

**How it works:**

1.  A method is defined in the parent class.
2.  A method with the exact same name is defined in the child class.
3.  When an object of the child class calls that method, the child's version takes precedence.

**Example:**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is driving.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    # Method Overriding: Car provides its own drive method
    def drive(self):
        print(f"{self.brand} {self.model} is driving on the road.")

class Boat(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    # Method Overriding: Boat provides its own drive method
    def drive(self):
        print(f"{self.brand} {self.type} is sailing on the water.")

# Create instances
vehicle = Vehicle("Generic")
car = Car("Toyota", "Camry")
boat = Boat("Yamaha", "Yacht")

# Demonstrate method overriding
vehicle.drive() # Output: Generic is driving.
car.drive()     # Output: Toyota Camry is driving on the road.
boat.drive()    # Output: Yamaha Yacht is sailing on the water.

# Demonstrate polymorphism with a list of vehicles
vehicles = [vehicle, car, boat]

print("\n--- Demonstrating Polymorphism ---")
for v in vehicles:
    v.drive() # The correct drive method is called based on the object's type
# Output:
# Generic is driving.
# Toyota Camry is driving on the road.
# Yamaha Yacht is sailing on the water.
```

Polymorphism and method overriding are powerful tools that make your code more flexible, extensible, and easier to manage, especially in large and complex object-oriented systems.

--- 

### Quiz

1.  **What is method overriding?**
    a) Creating a new method in a child class.
    b) Deleting a method from the parent class.
    c) Providing a specific implementation of a method in a child class that is already defined in its parent class.

2.  **What does the `super()` function do?**
    a) It calls a method from the child class.
    b) It calls a method from the parent class.
    c) It creates a superclass.

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. b
</details>