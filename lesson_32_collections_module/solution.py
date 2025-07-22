
# Lesson 32: Solution

from collections import Counter, namedtuple, defaultdict

# 1. Counter
sentence = "this is a sample sentence for counting letters"
letter_counts = Counter(sentence)
print("3 most common letters:", letter_counts.most_common(3))

# 2. namedtuple
Card = namedtuple('Card', ['rank', 'suit'])
card1 = Card(rank='A', suit='Spades')
print("\nCard:", card1)
print("Card rank:", card1.rank)

# 3. defaultdict
students = [('A', 'Alice'), ('B', 'Bob'), ('A', 'Charlie')]
grade_dict = defaultdict(list)
for grade, name in students:
    grade_dict[grade].append(name)

print("\nStudents by grade:", grade_dict)

