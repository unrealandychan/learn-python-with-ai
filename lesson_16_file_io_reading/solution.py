
# Lesson 16: Solution

# Using the recommended 'with' statement
with open('haiku.txt', 'r') as f:
    content = f.read()
    print(content)

# Alternative without 'with'
# f = open('haiku.txt', 'r')
# content = f.read()
# print(content)
# f.close()
