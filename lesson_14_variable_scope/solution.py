
# Lesson 14: Solution

user_name = "Alice"

def print_user():
    print(f"Current user: {user_name}")

def change_user(new_name):
    global user_name
    user_name = new_name
    print(f"User changed to: {user_name}")

print_user()
change_user("Bob")
print_user()
