
# Lesson 22: Solution

import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

shapes = [Rectangle(10, 5), Circle(7)]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.area():.2f}")
