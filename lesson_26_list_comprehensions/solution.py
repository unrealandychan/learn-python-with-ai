
# Lesson 26: Solution

even_numbers = [x * 2 for x in range(10)]
print("First 10 even numbers:", even_numbers)

sentence = "The quick brown fox jumps over the lazy dog"
long_words = [word for word in sentence.split() if len(word) > 4]
print("Words with more than 4 letters:", long_words)

word_lengths = [len(word) for word in sentence.split()]
print("Lengths of words:", word_lengths)
