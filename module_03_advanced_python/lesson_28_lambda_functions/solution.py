
# Lesson 28: Solution

multiply = lambda x, y: x * y
print("Result of multiply(5, 3):", multiply(5, 3))

to_upper = lambda s: s.upper()
print("'hello' in uppercase:", to_upper("hello"))

points = [(1, 5), (3, 2), (8, 1)]
points_sorted = sorted(points, key=lambda p: p[1])
print("Points sorted by the second element:", points_sorted)
