# Lesson 41: `requests` - Making HTTP Requests

import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    """
    Task 1: Make a GET request to fetch a list of users.
    Endpoint: https://jsonplaceholder.typicode.com/users
    Print the status code and the JSON response (or a part of it).
    """
    print("\n--- Task 1: GET Request (Fetch Users) ---")
    url = f"{BASE_URL}/users"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for HTTP errors
        users = response.json()
        print(f"Status Code: {response.status_code}")
        print(f"Fetched {len(users)} users. First user: {users[0]['name']}")
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request: {e}")

def create_post():
    """
    Task 2: Make a POST request to create a new post.
    Endpoint: https://jsonplaceholder.typicode.com/posts
    Payload: title, body, userId
    Print the status code and the JSON response.
    """
    print("\n--- Task 2: POST Request (Create Post) ---")
    url = f"{BASE_URL}/posts"
    new_post_payload = {
        "title": "My New Awesome Post",
        "body": "This is the content of my brand new post.",
        "userId": 1
    }
    try:
        response = requests.post(url, json=new_post_payload)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print("New post created:")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")

def update_post():
    """
    Task 3: Make a PUT request to update an existing post.
    Endpoint: https://jsonplaceholder.typicode.com/posts/1
    Payload: id, title, body, userId (all fields are usually sent for PUT)
    Print the status code and the JSON response.
    """
    print("\n--- Task 3: PUT Request (Update Post) ---")
    url = f"{BASE_URL}/posts/1"
    updated_post_payload = {
        "id": 1,
        "title": "Updated Title for Post 1",
        "body": "This post has been updated with new content.",
        "userId": 1
    }
    try:
        response = requests.put(url, json=updated_post_payload)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print("Post updated:")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error during PUT request: {e}")

def delete_post():
    """
    Task 4: Make a DELETE request to delete an existing post.
    Endpoint: https://jsonplaceholder.typicode.com/posts/1
    Print the status code.
    """
    print("\n--- Task 4: DELETE Request (Delete Post) ---")
    url = f"{BASE_URL}/posts/1"
    try:
        response = requests.delete(url)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Post 1 successfully deleted.")
        else:
            print("Deletion might not have been successful or returned unexpected status.")
    except requests.exceptions.RequestException as e:
        print(f"Error during DELETE request: {e}")

if __name__ == "__main__":
    # Uncomment the functions below to run each task
    get_users()
    create_post()
    update_post()
    delete_post()