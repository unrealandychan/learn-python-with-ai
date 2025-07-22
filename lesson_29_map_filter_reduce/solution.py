
# Lesson 29: Solution

from functools import reduce

str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print("Strings to integers:", int_numbers)

numbers = [5, 10, 15, 20, 25]
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print("Numbers greater than 10:", greater_than_10)

product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)
