

# Lesson 20: Solution

todo_list = []

while True:
    command = input("Enter a command (add, show, quit): ")

    if command == "add":
        item = input("Enter a to-do item: ")
        todo_list.append(item)
        print("Item added.")
    elif command == "show":
        print("\n--- To-Do List ---")
        for item in todo_list:
            print(f"- {item}")
        print("------------------\n")
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid command.")

