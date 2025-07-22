# Lesson 38: Introduction to Asynchronous Programming with `asyncio`

import asyncio
import time
import random

# --- Exercise 1: Basic Coroutine and `asyncio.run()` ---
# 1. Define an `async` function `greet(name, delay)` that prints "Hello, [name]!" after `delay` seconds.
# 2. Use `asyncio.run()` to execute the `greet` coroutine with a name and a short delay (e.g., 1 second).

print("--- Exercise 1: Basic Coroutine and `asyncio.run()` ---")

async def greet(name, delay):
    print(f"Greeting {name} in {delay} seconds...")
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # Your code for Exercise 1 here:
    asyncio.run(greet("Alice", 1))


# --- Exercise 2: Running Multiple Coroutines Concurrently with `asyncio.create_task()` ---
# 1. Define an `async` function `simulate_download(file_name, duration)` that prints
#    "Starting download of [file_name]...", waits for `duration` seconds,
#    and then prints "Finished download of [file_name]."
# 2. In an `async` main function (`main_downloads`), create multiple tasks using
#    `asyncio.create_task()` for different files and durations.
# 3. `await` each task to ensure they all complete.
# 4. Run `main_downloads` using `asyncio.run()`.

print("\n--- Exercise 2: Running Multiple Coroutines Concurrently ---")

async def simulate_download(file_name, duration):
    print(f"Starting download of {file_name} (estimated {duration}s)...")
    await asyncio.sleep(duration)
    print(f"Finished download of {file_name}.")

async def main_downloads():
    # Your code for Exercise 2 here:
    task1 = asyncio.create_task(simulate_download("report.pdf", 3))
    task2 = asyncio.create_task(simulate_download("image.jpg", 2))
    task3 = asyncio.create_task(simulate_download("data.zip", 4))

    await task1
    await task2
    await task3
    print("All downloads completed.")

if __name__ == "__main__":
    asyncio.run(main_downloads())


# --- Exercise 3: Using `asyncio.gather()` for Concurrent Execution and Results ---
# 1. Define an `async` function `fetch_data(item_id)` that simulates fetching data.
#    It should print "Fetching data for [item_id]...", wait a random time (0.5 to 2 seconds),
#    and then return a string like "Data for [item_id] fetched."
# 2. In an `async` main function (`main_fetch`), create a list of item IDs.
# 3. Use a list comprehension to create a list of coroutine objects by calling `fetch_data` for each item ID.
# 4. Use `asyncio.gather()` to run all these coroutines concurrently and collect their results.
# 5. Print all the collected results.

print("\n--- Exercise 3: Using `asyncio.gather()` ---")

async def fetch_data(item_id):
    delay = random.uniform(0.5, 2.0)
    print(f"Fetching data for {item_id} (will take {delay:.2f}s)...")
    await asyncio.sleep(delay)
    return f"Data for {item_id} fetched."

async def main_fetch():
    item_ids = ["A1", "B2", "C3", "D4", "E5"]

    # Your code for Exercise 3 here:
    fetch_tasks = [fetch_data(item_id) for item_id in item_ids]
    results = await asyncio.gather(*fetch_tasks)

    print("\n--- All Fetch Results ---")
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main_fetch())