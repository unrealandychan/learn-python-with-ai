# Lesson 34: Working with JSON data (`json` module)

import json
import os

# --- Exercise 1: Python to JSON String (json.dumps()) ---
# 1. Create a Python dictionary representing a book.
#    It should have keys: "title", "author", "year", and "genres" (a list).
# 2. Convert this dictionary into a JSON formatted string.
# 3. Print the JSON string.
# 4. Convert the same dictionary into a pretty-printed JSON string with an indent of 2.
# 5. Print the pretty-printed JSON string.

print("--- Exercise 1: Python to JSON String ---")
book_data = {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "year": 1979,
    "genres": ["Science Fiction", "Comedy"]
}

# Your code for Exercise 1 here:
json_string_compact = json.dumps(book_data)
print("Compact JSON:", json_string_compact)

json_string_pretty = json.dumps(book_data, indent=2)
print("\nPretty JSON:\n", json_string_pretty)


# --- Exercise 2: JSON String to Python (json.loads()) ---
# 1. Take the following JSON string.
# 2. Convert it into a Python dictionary.
# 3. Access and print the "name" and "city" from the resulting dictionary.

print("\n--- Exercise 2: JSON String to Python ---")
json_person_string = '{"name": "Alice", "age": 30, "city": "New York", "isStudent": true}'

# Your code for Exercise 2 here:
person_dict = json.loads(json_person_string)
print("Name:", person_dict["name"])
print("City:", person_dict["city"])


# --- Exercise 3: Python to JSON File (json.dump()) ---
# 1. Create a Python list of dictionaries, where each dictionary represents a simple task
#    (e.g., {"id": 1, "description": "Buy groceries", "completed": false}).
# 2. Define a filename for your JSON file (e.g., "tasks.json").
# 3. Write the list of dictionaries to this file as JSON, with an indent of 4.
# 4. Print a confirmation message indicating the file was created.

print("\n--- Exercise 3: Python to JSON File ---")
tasks = [
    {"id": 1, "description": "Buy groceries", "completed": False},
    {"id": 2, "description": "Walk the dog", "completed": True},
    {"id": 3, "description": "Pay bills", "completed": False}
]
tasks_file = "tasks.json"

# Your code for Exercise 3 here:
with open(tasks_file, 'w') as f:
    json.dump(tasks, f, indent=4)
print(f"Tasks saved to {tasks_file}")


# --- Exercise 4: JSON File to Python (json.load()) ---
# 1. Assuming "tasks.json" was created in Exercise 3, read its content.
# 2. Convert the JSON content from the file back into a Python list of dictionaries.
# 3. Print the entire loaded list.
# 4. Print the description of the second task.
# 5. Clean up: Remove the "tasks.json" file after reading.

print("\n--- Exercise 4: JSON File to Python ---")

# Your code for Exercise 4 here:
try:
    with open(tasks_file, 'r') as f:
        loaded_tasks = json.load(f)
    print("Loaded tasks:", loaded_tasks)
    print("Description of second task:", loaded_tasks[1]["description"])
except FileNotFoundError:
    print(f"Error: {tasks_file} not found. Please run Exercise 3 first.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {tasks_file}. Check file content.")
finally:
    # Clean up the created file
    if os.path.exists(tasks_file):
        os.remove(tasks_file)
        print(f"Cleaned up {tasks_file}")