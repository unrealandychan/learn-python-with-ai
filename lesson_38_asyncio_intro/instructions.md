
# Lesson 38: Introduction to Asynchronous Programming with `asyncio`

`asyncio` is a Python library used for writing concurrent code using the `async`/`await` syntax. It is a powerful framework for writing single-threaded concurrent code, particularly well-suited for I/O-bound and high-level structured network code. Unlike multithreading or multiprocessing, `asyncio` achieves concurrency through cooperative multitasking, where tasks voluntarily yield control.

## Key Concepts in `asyncio`

1.  **Coroutines (`async def`):
    *   Functions defined with `async def` are called coroutines. They are special functions that can be paused and resumed.
    *   They don't run immediately when called; instead, they return a coroutine object that needs to be scheduled to run on an event loop.

2.  **`await` Keyword:
    *   Used inside an `async def` function to pause the execution of the current coroutine until the `awaitable` (another coroutine, a Future, or a Task) it's waiting on completes.
    *   When a coroutine `awaits` something, it yields control back to the event loop, allowing the event loop to run other tasks while the awaited operation is pending (e.g., waiting for network data, a file to be read).

3.  **Event Loop:
    *   The heart of `asyncio`. It's responsible for running coroutines, performing I/O operations, and scheduling when coroutines should run.
    *   It continuously monitors for events (like data arriving on a socket) and dispatches them to the appropriate coroutines.

4.  **Tasks (`asyncio.create_task()`):
    *   Coroutines are wrapped into Tasks to be scheduled on the event loop. A Task is a Future-like object that runs a coroutine.
    *   `asyncio.create_task(coro)` schedules the coroutine `coro` to run as a Task.

5.  **`asyncio.run()`:
    *   The primary entry point for running `asyncio` applications. It takes a coroutine, runs it until it completes, and manages the event loop.
    *   It handles the creation and closing of the event loop automatically.

## Why `asyncio`?

*   **Concurrency without Threads:** Achieves concurrency in a single thread, avoiding the complexities of thread synchronization (like locks) and the GIL limitations for I/O-bound tasks.
*   **Efficiency:** Very efficient for handling a large number of concurrent I/O operations (e.g., thousands of network connections).
*   **Scalability:** Can scale to handle many concurrent operations with less overhead compared to traditional threading models.

## Examples

### Example 1: Basic `async`/`await` and `asyncio.run()`

This example demonstrates a simple asynchronous function and how to run it.

```python
import asyncio
import time

async def say_hello(delay, message):
    """A simple coroutine that waits and then prints a message."""
    print(f"[{time.strftime('%X')}] {message} (starting wait for {delay}s)")
    await asyncio.sleep(delay) # Pause this coroutine, allow others to run
    print(f"[{time.strftime('%X')}] {message} (finished wait)")

async def main():
    print(f"[{time.strftime('%X')}] Main coroutine started.")
    # Schedule coroutines to run concurrently as tasks
    task1 = asyncio.create_task(say_hello(2, "First hello"))
    task2 = asyncio.create_task(say_hello(1, "Second hello"))

    # Await the completion of the tasks
    await task1
    await task2
    print(f"[{time.strftime('%X')}] Main coroutine finished.")

if __name__ == "__main__":
    print("Running asyncio application...")
    asyncio.run(main())
    print("Asyncio application finished.")
```

**Explanation:**

*   `say_hello` is an `async def` function, making it a coroutine.
*   `await asyncio.sleep(delay)` is the key. When `say_hello` encounters this, it tells the event loop: "I'm going to wait for `delay` seconds. While I'm waiting, you can go run other things." The event loop then switches to another task.
*   `main()` is also a coroutine. It uses `asyncio.create_task()` to schedule `say_hello` coroutines to run concurrently. Without `create_task`, `await say_hello(...)` would run them sequentially.
*   `asyncio.run(main())` starts the event loop, runs the `main` coroutine, and closes the loop when `main` completes.

### Example 2: Simulating Concurrent Web Requests

This example shows how `asyncio` can be used to fetch multiple URLs concurrently, which is a common I/O-bound task.

```python
import asyncio
import time
import aiohttp # You might need to install this: pip install aiohttp

async def fetch_url(session, url):
    start_time = time.time()
    print(f"Fetching {url}...")
    async with session.get(url) as response:
        await response.text() # Simulate reading the response body
    end_time = time.time()
    print(f"Finished {url} in {end_time - start_time:.2f} seconds.")
    return url

async def main_web_fetch():
    urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(fetch_url(session, url)))
        
        # Wait for all tasks to complete
        results = await asyncio.gather(*tasks)
        print(f"\nAll URLs fetched: {results}")

if __name__ == "__main__":
    print("Simulating concurrent web fetches...")
    # Note: aiohttp is an external library. For this example to run, you need to install it.
    # If you don't want to install aiohttp, you can replace fetch_url with a simple
    # asyncio.sleep() to simulate I/O.
    try:
        asyncio.run(main_web_fetch())
    except ImportError:
        print("\n'aiohttp' not found. Please install it (`pip install aiohttp`) or run the simpler examples.")
    print("Web fetch simulation finished.")
```

**Explanation:**

*   `aiohttp` is an asynchronous HTTP client library. `asyncio` itself doesn't provide HTTP client functionality, but it provides the foundation for such libraries.
*   `async with aiohttp.ClientSession() as session:` creates an asynchronous context for HTTP requests.
*   `asyncio.gather(*tasks)` is a powerful function that runs multiple awaitable objects concurrently and waits for all of them to complete. It returns a list of results in the order the awaitables were passed.

---

### Quiz

1.  **Which keyword is used to define a coroutine function in Python?**
    a) `def`
    b) `coro def`
    c) `async def`
    d) `await def`

2.  **What is the purpose of the `await` keyword in an `async def` function?**
    a) To immediately execute the awaited function.
    b) To pause the current coroutine's execution and allow the event loop to run other tasks until the awaited operation completes.
    c) To convert a regular function into a coroutine.
    d) To define a new thread.

3.  **Which function is typically used as the entry point to run an `asyncio` application?**
    a) `asyncio.start()`
    b) `asyncio.run()`
    c) `asyncio.execute()`
    d) `asyncio.main()`

4.  **What does `asyncio.create_task(coro)` do?**
    a) It immediately executes the `coro` coroutine.
    b) It creates a new thread to run the `coro` coroutine.
    c) It wraps the `coro` coroutine into a Task and schedules it to run on the event loop.
    d) It converts `coro` into a regular function.

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. b
  3. b
  4. c
</details>
