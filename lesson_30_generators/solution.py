
# Lesson 30: Solution

def countdown(n):
    while n > 0:
        yield n
        n -= 1

def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

print("Countdown from 5:")
for num in countdown(5):
    print(num)

print("\nEven numbers up to 10:")
for num in even_numbers(10):
    print(num)

