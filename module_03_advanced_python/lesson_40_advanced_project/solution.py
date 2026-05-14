
# Lesson 40: Solution

import threading
import requests
import json

results = []
lock = threading.Lock()

def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    data = response.json()

    processed_data = {
        "id": data["id"],
        "title": data["title"],
        "body": data["body"]
    }

    with lock:
        results.append(processed_data)

threads = []
for i in range(1, 6):
    thread = threading.Thread(target=fetch_post, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

with open("posts.json", "w") as f:
    json.dump(results, f, indent=4)

print("Successfully fetched and saved 5 posts to posts.json")
