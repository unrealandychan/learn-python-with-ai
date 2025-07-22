
# Lesson 11: Solution

point = (10, 20, 30)
print("Point coordinates:", point)

# The following line will raise a TypeError because tuples are immutable
# point[0] = 15

colors = {"red", "green", "blue"}
print("Initial set of colors:", colors)

colors.add("yellow")
print("After adding yellow:", colors)

colors.add("red")
print("After adding red again:", colors)
