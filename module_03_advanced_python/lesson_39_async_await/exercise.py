# Lesson 39: Using `async` and `await` for Asynchronous I/O

import asyncio
import aiohttp

# --- Exercise 1: Basic Async/Await with asyncio.sleep() ---
# Task: Create an asynchronous function `greet_after_delay` that takes a name and a delay.
# It should wait for the specified delay and then print a greeting message.
# Call this function for two different names and delays concurrently using `asyncio.gather()`.

async def greet_after_delay(name, delay):
    # Your code here
    pass

async def exercise_1():
    print("\n--- Exercise 1: Basic Async/Await ---")
    # Call greet_after_delay for "Alice" with 2 seconds delay and "Bob" with 1 second delay
    # Your code here
    pass

# --- Exercise 2: Asynchronous HTTP Requests with aiohttp ---
# Task: Create an asynchronous function `fetch_json` that takes a URL.
# It should use `aiohttp` to make a GET request to the URL and return the JSON response.
# Then, in `exercise_2`, fetch data from two different JSONPlaceholder API endpoints concurrently:
# 1. https://jsonplaceholder.typicode.com/posts/1
# 2. https://jsonplaceholder.typicode.com/users/1
# Print the title of the post and the name of the user.

async def fetch_json(session, url):
    # Your code here
    pass

async def exercise_2():
    print("\n--- Exercise 2: Asynchronous HTTP Requests ---")
    async with aiohttp.ClientSession() as session:
        # Fetch data from both URLs concurrently
        # Your code here
        pass

# --- Main execution --- 
async def main():
    await exercise_1()
    await exercise_2()

if __name__ == "__main__":
    # To run the exercises, uncomment the line below:
    # asyncio.run(main())
    print("Uncomment `asyncio.run(main())` to run the exercises.")