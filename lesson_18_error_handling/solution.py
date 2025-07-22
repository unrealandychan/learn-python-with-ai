
# Lesson 18: Solution

try:
    num1_str = input("Enter a number: ")
    num1 = float(num1_str)

    num2_str = input("Enter another number: ")
    num2 = float(num2_str)

    result = num1 / num2
    print(f"The result of the division is: {result}")

except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
