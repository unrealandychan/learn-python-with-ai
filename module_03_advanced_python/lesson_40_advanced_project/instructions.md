# Lesson 40: Advanced Project: Building a Multi-threaded Web Scraper

This lesson challenges you to integrate several key Python concepts into a single, functional project. You will build a multi-threaded web scraper that fetches data from a public API, processes it, and saves the results to a file. This project will reinforce your understanding of:

*   **Multithreading**: Using the `threading` module to perform tasks concurrently.
*   **HTTP Requests**: Making web requests to fetch data from an API using the `requests` library.
*   **JSON Handling**: Parsing and manipulating JSON data.
*   **File I/O**: Writing processed data to a file.
*   **Error Handling**: Gracefully managing potential issues during network requests or file operations.

---

### Project Goal

Your goal is to create a Python program that:
1.  **Fetches Data Concurrently**: Retrieves data for multiple posts from the JSONPlaceholder API (a free fake API for testing and prototyping).
2.  **Uses Multithreading**: Each data fetch operation should run in a separate thread to demonstrate concurrent execution.
3.  **Processes Data**: Extracts specific information (e.g., `title` and `body`) from the fetched JSON data.
4.  **Saves to File**: Stores all the processed data into a single JSON file.

### Key Concepts and Tools

#### 1. Making HTTP Requests with `requests`

The `requests` library is a popular and easy-to-use HTTP library for Python. If you haven't already, install it:

```bash
pip install requests
```

**Example Usage:**

```python
import requests

def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching post {post_id}: {e}")
        return None

# Example:
# post_data = get_post(1)
# if post_data:
#     print(post_data["title"])
```

#### 2. Multithreading with `threading`

The `threading` module allows you to run multiple parts of your program concurrently. This is particularly useful for I/O-bound tasks like network requests, as threads can perform other work while waiting for network responses.

**Basic Thread Usage:**

```python
import threading
import time

def task(name, duration):
    print(f"Thread {name}: Starting...")
    time.sleep(duration) # Simulate work
    print(f"Thread {name}: Finishing.")

# Create threads
thread1 = threading.Thread(target=task, args=("One", 2))
thread2 = threading.Thread(target=task, args=("Two", 1))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads finished.")
```

**Thread Safety and Locks:**
When multiple threads access and modify shared resources (like a list where you store fetched data), you need to ensure thread safety to prevent race conditions. A `threading.Lock` can be used to protect critical sections of code.

```python
import threading

shared_data = []
data_lock = threading.Lock()

def add_data(item):
    with data_lock: # Acquire lock before modifying shared_data
        shared_data.append(item)
    print(f"Added: {item}. Current data: {shared_data}")

# Example:
# thread3 = threading.Thread(target=add_data, args=("Item A",))
# thread4 = threading.Thread(target=add_data, args=("Item B",))
# thread3.start()
# thread4.start()
# thread3.join()
# thread4.join()
```

#### 3. JSON Handling with `json`

The `json` module allows you to work with JSON (JavaScript Object Notation) data, which is a common format for data exchange on the web.

**Example Usage:**

```python
import json

# Convert Python dictionary to JSON string
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data, indent=4)
print(json_string)

# Convert JSON string to Python dictionary
parsed_data = json.loads(json_string)
print(parsed_data["name"])

# Write Python dictionary to a JSON file
file_path = "output.json"
with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)
print(f"Data written to {file_path}")
```

#### 4. File I/O

You'll use basic file operations to save your processed data.

```python
# Example (already covered in JSON handling example above)
# with open("output.json", 'w') as f:
#     json.dump(data, f, indent=4)
```

---

### Project Structure and Implementation Hints

Consider organizing your code with the following functions:

*   `fetch_post_data(post_id, results_list, lock)`: This function will be executed by each thread. It should fetch data for a given `post_id`, process it, and append the processed data to a shared `results_list` using a `lock` for thread safety.
*   `process_data(raw_data)`: A helper function to extract `title` and `body` from the raw JSON response.
*   `save_data_to_json(data, filename)`: A function to write the final list of processed data to a JSON file.

Your main execution block will involve:
1.  Initializing an empty list to store results and a `threading.Lock`.
2.  Creating and starting multiple threads, each targeting `fetch_post_data` with a different `post_id`.
3.  Waiting for all threads to complete using `thread.join()`.
4.  Calling `save_data_to_json` with the collected results.

---

### Quiz

1.  **Why might you use multithreading for a web scraper?**
    a) To make the code more complex.
    b) To perform multiple network requests concurrently, speeding up the process.
    c) To bypass the GIL.

2.  **What is the purpose of `threading.Lock` in this project?**
    a) To prevent the program from crashing.
    b) To ensure that only one thread modifies shared data at a time, preventing race conditions.
    c) To lock the API endpoint to prevent other users from accessing it.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>