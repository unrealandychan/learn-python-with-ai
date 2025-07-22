
# Lesson 34: Working with JSON data (`json` module)

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for transmitting data in web applications (e.g., sending data from a server to a web page).

Python's built-in `json` module provides all the necessary tools for working with JSON data.

## Key Functions:

### 1. `json.dumps()`: Python to JSON String

*   **Purpose:** Encodes a Python object (like a dictionary or list) into a JSON formatted string. The "s" in `dumps` stands for "string".
*   **Common Use Case:** When you need to send Python data over a network, store it in a text file, or display it in a human-readable JSON format.

**Syntax:** `json.dumps(obj, indent=None, sort_keys=False, ...)`

*   `obj`: The Python object to be serialized (e.g., dictionary, list, string, int, float, boolean, None).
*   `indent`: (Optional) If provided, JSON output will be pretty-printed with the specified indentation level (e.g., `indent=4` for 4 spaces). This makes the JSON string more readable.
*   `sort_keys`: (Optional) If `True`, the output of dictionaries will be sorted by key.

**Example:**

```python
import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}

# Convert Python dictionary to JSON string
json_string = json.dumps(data)
print("JSON string (compact):")
print(json_string)
# Output: {"name": "Alice", "age": 30, "isStudent": false, "courses": ["Math", "Science"], "address": {"street": "123 Main St", "city": "Anytown"}}

# Convert Python dictionary to pretty-printed JSON string
json_pretty_string = json.dumps(data, indent=4)
print("\nJSON string (pretty-printed):")
print(json_pretty_string)
# Output:
# {
#     "name": "Alice",
#     "age": 30,
#     "isStudent": false,
#     "courses": [
#         "Math",
#         "Science"
#     ],
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown"
#     }
# }

# Example with a list
my_list = [1, 2, {"key": "value"}, 4]
json_list_string = json.dumps(my_list, indent=2)
print("\nJSON list string:")
print(json_list_string)
# Output:
# [
#   1,
#   2,
#   {
#     "key": "value"
#   },
#   4
# ]
```

### 2. `json.loads()`: JSON String to Python

*   **Purpose:** Decodes a JSON formatted string into a Python object (typically a dictionary or list). The "s" in `loads` also stands for "string".
*   **Common Use Case:** When you receive JSON data as a string (e.g., from a web API response, or read from a file) and need to work with it as Python objects.

**Syntax:** `json.loads(json_string)`

*   `json_string`: The JSON formatted string to be deserialized.

**Example:**

```python
import json

# JSON string
json_data_string = '{"product": "Laptop", "price": 1200.50, "inStock": true, "features": ["lightweight", "fast"]}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_data_string)
print("Python dictionary from JSON string:")
print(python_dict)
# Output: {'product': 'Laptop', 'price': 1200.5, 'inStock': True, 'features': ['lightweight', 'fast']}

print(f"Product name: {python_dict['product']}")
print(f"Is in stock: {python_dict['inStock']}")
print(f"First feature: {python_dict['features'][0]}")

# Example with a JSON array string
json_array_string = '[{"id": 1, "item": "apple"}, {"id": 2, "item": "banana"}]'
python_list = json.loads(json_array_string)
print("\nPython list from JSON array string:")
print(python_list)
# Output: [{'id': 1, 'item': 'apple'}, {'id': 2, 'item': 'banana'}]
print(f"First item: {python_list[0]['item']}")
```

### 3. `json.dump()`: Python to JSON File

*   **Purpose:** Encodes a Python object and writes it directly to a file-like object (e.g., a file opened in write mode) as a JSON formatted stream. This is useful for saving data to a file.
*   **Common Use Case:** Storing configuration, user data, or any structured data in a file in JSON format.

**Syntax:** `json.dump(obj, fp, indent=None, sort_keys=False, ...)`

*   `obj`: The Python object to be serialized.
*   `fp`: A file-like object with a `write()` method (e.g., `open('filename.json', 'w')`).
*   `indent`, `sort_keys`: Same as for `json.dumps()`.

**Example:**

```python
import json

data_to_save = {
    "city": "New York",
    "population": 8419000,
    "landmarks": ["Statue of Liberty", "Empire State Building"]
}

file_name = "city_data.json"

with open(file_name, 'w') as json_file:
    json.dump(data_to_save, json_file, indent=4)

print(f"Data saved to {file_name}")

# You can verify the content of city_data.json after running this code.
# It will contain:
# {
#     "city": "New York",
#     "population": 8419000,
#     "landmarks": [
#         "Statue of Liberty",
#         "Empire State Building"
#     ]
# }
```

### 4. `json.load()`: JSON File to Python

*   **Purpose:** Decodes a JSON document from a file-like object (e.g., a file opened in read mode) into a Python object.
*   **Common Use Case:** Reading configuration or data from a JSON file.

**Syntax:** `json.load(fp)`

*   `fp`: A file-like object with a `read()` method (e.g., `open('filename.json', 'r')`).

**Example:**

```python
import json

# Assuming 'city_data.json' was created by the json.dump() example above
file_name = "city_data.json"

try:
    with open(file_name, 'r') as json_file:
        loaded_data = json.load(json_file)
    
    print(f"Data loaded from {file_name}:")
    print(loaded_data)
    # Output: {'city': 'New York', 'population': 8419000, 'landmarks': ['Statue of Liberty', 'Empire State Building']}
    
    print(f"Loaded city: {loaded_data['city']}")
    print(f"First landmark: {loaded_data['landmarks'][0]}")

except FileNotFoundError:
    print(f"Error: {file_name} not found. Please run the json.dump() example first.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {file_name}. Check file content.")
```

---

### Quiz

1.  **Which function converts a Python dictionary to a JSON string?**
    a) `json.load()`
    b) `json.dumps()`
    c) `json.encode()`

2.  **Which function converts a JSON string to a Python dictionary?**
    a) `json.loads()`
    b) `json.dump()`
    c) `json.decode()`

3.  **To save a Python dictionary directly to a JSON file, which function would you use?**
    a) `json.loads()`
    b) `json.dump()`
    c) `json.dumps()`

4.  **To read JSON data from a file and convert it into a Python object, which function is appropriate?**
    a) `json.load()`
    b) `json.loads()`
    c) `json.read()`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
  3. b
  4. a
</details>
