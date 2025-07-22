# Lesson 40: Advanced Project: Building a Multi-threaded Web Scraper

import requests
import json
import threading
import os

# Base URL for JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

# List to store processed data from all threads
# This list will be shared among threads, so access to it must be synchronized.
all_posts_data = []

# A lock to ensure thread-safe access to `all_posts_data`
data_lock = threading.Lock()

def fetch_post_data(post_id):
    """
    Fetches a single post from the JSONPlaceholder API.
    """
    url = f"{BASE_URL}/posts/{post_id}"
    print(f"Thread for Post {post_id}: Fetching data...")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        post_data = response.json()
        print(f"Thread for Post {post_id}: Data fetched.")
        return post_data
    except requests.exceptions.RequestException as e:
        print(f"Thread for Post {post_id}: Error fetching data: {e}")
        return None

def process_post_data(raw_post_data):
    """
    Processes the raw post data to extract relevant information.
    """
    if raw_post_data:
        processed_data = {
            "id": raw_post_data.get("id"),
            "title": raw_post_data.get("title"),
            "body": raw_post_data.get("body")
        }
        return processed_data
    return None

def worker_function(post_id):
    """
    Worker function to be executed by each thread.
    Fetches, processes, and adds data to the shared list.
    """
    raw_data = fetch_post_data(post_id)
    processed_data = process_post_data(raw_data)

    if processed_data:
        with data_lock:
            all_posts_data.append(processed_data)
            print(f"Thread for Post {post_id}: Added processed data to shared list.")

def save_data_to_json(data, filename="posts_data.json"):
    """
    Saves the collected data to a JSON file.
    """
    output_path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {output_path}")
    except IOError as e:
        print(f"Error saving data to file {output_path}: {e}")

def main():
    print("Starting multi-threaded web scraper...")

    # Define the post IDs to fetch
    post_ids = range(1, 6)  # Fetch posts 1 through 5

    threads = []
    for post_id in post_ids:
        thread = threading.Thread(target=worker_function, args=(post_id,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All threads finished. Saving collected data...")
    save_data_to_json(all_posts_data)
    print("Scraping complete.")

if __name__ == "__main__":
    main()