
# Lesson 4: Solution

name = input("What is your name? ")
age_str = input("What is your age? ")
favorite_number_str = input("What is your favorite number? ")

age = int(age_str)
favorite_number = float(favorite_number_str)

age_in_5_years = age + 5

print(f"Hello, {name}!")
print(f"In 5 years, you will be {age_in_5_years} years old.")
print(f"Your favorite number is {favorite_number}.")
