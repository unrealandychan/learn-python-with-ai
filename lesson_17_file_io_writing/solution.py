
# Lesson 17: Solution

# Write initial items
with open('shopping_list.txt', 'w') as f:
    f.write("Milk\n")
    f.write("Bread\n")
    f.write("Eggs\n")

# Append more items
with open('shopping_list.txt', 'a') as f:
    f.write("Cheese\n")
    f.write("Apples\n")

# Read and print the final list
with open('shopping_list.txt', 'r') as f:
    print(f.read())

