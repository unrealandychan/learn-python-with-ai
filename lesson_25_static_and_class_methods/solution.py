
# Lesson 25: Solution

import math

class MathHelper:
    @staticmethod
    def pi():
        return math.pi

    @staticmethod
    def circle_area(radius):
        return math.pi * radius**2

    @classmethod
    def info(cls):
        return f"This is the {cls.__name__} class."


print("Value of Pi:", MathHelper.pi())
print("Area of a circle with radius 5:", MathHelper.circle_area(5))
print(MathHelper.info())
