# Lesson 41: `requests` - Making HTTP Requests

The `requests` library is the de facto standard for making HTTP requests in Python. It simplifies the process of sending HTTP requests and handling responses, making web interactions much easier than using Python's built-in `urllib` module.

**Official Documentation:** [https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)

---

### Installation

If you don't have `requests` installed, you can do so using pip:

```bash
pip install requests
```

### Basic Usage: GET Requests

GET requests are used to retrieve data from a specified resource. This is the most common type of HTTP request.

```python
import requests

# Making a simple GET request
response = requests.get('https://www.google.com')

# Checking the status code
print(f"Status Code: {response.status_code}")

# Accessing the response content (HTML in this case)
# print(response.text)

# For JSON responses, use .json()
# response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
# if response.status_code == 200:
#     todo_item = response.json()
#     print(f"Todo Title: {todo_item['title']}")
```

#### Passing Parameters in GET Requests

You can pass parameters (query strings) to a GET request using the `params` argument, which takes a dictionary.

```python
import requests

params = {'q': 'Python requests', 'limit': 1}
response = requests.get('https://api.github.com/search/repositories', params=params)

if response.status_code == 200:
    data = response.json()
    # print(data['items'][0]['full_name'])
```

### POST Requests

POST requests are used to send data to a server to create a new resource.

```python
import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'

# Data to be sent in the request body
# For JSON data, use the 'json' argument
payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}

response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}")
if response.status_code == 201: # 201 Created
    print("Post created successfully:")
    print(response.json())
```

### PUT Requests

PUT requests are used to update an existing resource on the server.

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1' # Updating post with ID 1

payload = {
    'id': 1,
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1,
}

response = requests.put(url, json=payload)

print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    print("Post updated successfully:")
    print(response.json())
```

### DELETE Requests

DELETE requests are used to delete a specified resource.

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1' # Deleting post with ID 1

response = requests.delete(url)

print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    print("Post deleted successfully.")
```

### Handling Responses

*   **`response.status_code`**: The HTTP status code (e.g., 200 OK, 404 Not Found, 500 Internal Server Error).
*   **`response.ok`**: A boolean indicating if the status code is less than 400.
*   **`response.text`**: The content of the response in Unicode.
*   **`response.json()`**: If the response contains JSON data, this method parses it into a Python dictionary or list.
*   **`response.headers`**: A dictionary of response headers.
*   **`response.raise_for_status()`**: Raises an `HTTPError` for bad responses (4xx or 5xx client or server error responses). This is a convenient way to check for errors.

```python
import requests

try:
    response = requests.get('https://httpbin.org/status/404')
    response.raise_for_status() # This will raise an HTTPError for 404
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
except requests.exceptions.Timeout as e:
    print(f"Timeout Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"An unexpected error occurred: {e}")
```

### Timeouts

It's good practice to set a timeout for your requests to avoid waiting indefinitely for a response.

```python
import requests

try:
    response = requests.get('https://httpbin.org/delay/5', timeout=3) # Wait for 3 seconds
    print(response.text)
except requests.exceptions.Timeout:
    print("The request timed out.")
```

---

### Quiz

1.  **Which `requests` method is used for a GET request?**
    a) `requests.get()`
    b) `requests.fetch()`
    c) `requests.post()`

2.  **How do you check if a request was successful (status code < 400)?**
    a) `response.success == True`
    b) `response.status_code == 200`
    c) `response.ok`

3.  **What is the purpose of the `json` argument in `requests.post()`?**
    a) To specify the expected response format.
    b) To send data as a JSON payload in the request body.
    c) To authenticate the request.

<details>
  <summary><b>Answer Key</b></summary>
  1. a
  2. c
  3. b
</details>