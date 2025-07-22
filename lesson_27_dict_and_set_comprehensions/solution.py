
# Lesson 27: Solution

squares_dict = {x: x**2 for x in range(1, 6)}
print("Numbers and their squares:", squares_dict)

my_string = "hello world"
unique_chars = {char for char in my_string}
print("Unique characters:", unique_chars)

words = ["apple", "banana", "cherry"]
word_lengths_dict = {word: len(word) for word in words}
print("Words and their lengths:", word_lengths_dict)
