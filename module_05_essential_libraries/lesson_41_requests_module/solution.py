
# Lesson 41: Solution

import requests

# GET request
get_response = requests.get("https://jsonplaceholder.typicode.com/users")
print("GET Response:", get_response.status_code, get_response.json()[0])

# POST request
new_post = {"title": "foo", "body": "bar", "userId": 1}
post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print("\nPOST Response:", post_response.status_code, post_response.json())

# PUT request
updated_post = {"id": 1, "title": "foo", "body": "bar", "userId": 1}
put_response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)
print("\nPUT Response:", put_response.status_code, put_response.json())

