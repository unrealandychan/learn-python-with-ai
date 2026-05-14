# Lesson 39: Using `async` and `await` for Asynchronous I/O

Asynchronous programming is a paradigm that allows a program to start a potentially long-running task and then continue with other tasks without waiting for the long-running task to complete. When the long-running task finishes, the program is notified and can then process its result. This is particularly useful for I/O-bound operations (like network requests, file operations, or database queries) where the program spends a lot of time waiting for external resources.

In Python, the `asyncio` library provides a framework for writing concurrent code using the `async`/`await` syntax.

---

### The `async` and `await` Keywords

*   **`async def`**: This keyword is used to define a *coroutine*. A coroutine is a special type of function that can be paused and resumed. When you call an `async def` function, it doesn't execute immediately; instead, it returns a coroutine object.

    ```python
    async def my_coroutine():
        print("Hello from coroutine!")
    ```

*   **`await`**: This keyword can only be used inside an `async def` function. It's used to pause the execution of the current coroutine until the `await`-ed task is complete. While the current coroutine is paused, the `asyncio` event loop can switch to and execute other coroutines.

    ```python
    import asyncio

    async def fetch_data():
        print("Fetching data...")
        await asyncio.sleep(2)  # Simulate a 2-second I/O operation
        print("Data fetched!")
        return {"data": "Some important data"}

    async def main():
        print("Starting main...")
        data = await fetch_data()
        print(f"Received: {data}")
        print("Main finished.")

    # To run the main coroutine
    # asyncio.run(main())
    ```

### The `asyncio` Event Loop

At the heart of `asyncio` is the event loop. The event loop is responsible for:
1.  Running coroutines.
2.  Managing tasks (scheduled coroutines).
3.  Handling I/O operations.
4.  Switching between coroutines when one is paused by an `await` expression.

### Running Coroutines

To run a top-level coroutine, you use `asyncio.run()`. This function takes a coroutine object and runs it until it completes. It also manages the `asyncio` event loop.

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1) # Simulate some work
    print(f"Hello, {name}!")

async def main_single():
    print("Running single coroutine...")
    await greet("Alice")
    print("Single coroutine finished.")

# asyncio.run(main_single())
```

### Concurrent Execution with `asyncio.gather()`

One of the most powerful features of `asyncio` is the ability to run multiple coroutines concurrently. `asyncio.gather()` is used to run multiple awaitable objects (like coroutines) concurrently and wait for all of them to complete. It returns a list of results in the order the awaitables were passed to it.

```python
import asyncio
import time

async def task(name, delay):
    print(f"Task {name}: Starting (delay={delay}s)")
    await asyncio.sleep(delay)
    print(f"Task {name}: Finished")
    return f"Result from {name}"

async def main_concurrent():
    print("Running concurrent tasks...")
    start_time = time.time()

    # Run tasks concurrently
    results = await asyncio.gather(
        task("A", 3),
        task("B", 1),
        task("C", 2)
    )

    end_time = time.time()
    print(f"All tasks finished in {end_time - start_time:.2f} seconds.")
    print(f"Results: {results}")

# asyncio.run(main_concurrent())
```
In the example above, even though Task A takes 3 seconds, Task B takes 1 second, and Task C takes 2 seconds, they run concurrently. The total execution time will be approximately 3 seconds (the duration of the longest task), not 6 seconds (the sum of all delays).

### Real-world Example: Asynchronous HTTP Requests with `aiohttp`

For real-world asynchronous I/O, you often need external libraries. For HTTP requests, `aiohttp` is a popular choice.

First, you need to install it:
`pip install aiohttp`

Here's an example of how to use `aiohttp` to make asynchronous HTTP GET requests:

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main_http_example():
    async with aiohttp.ClientSession() as session:
        data1 = await fetch_url(session, 'https://jsonplaceholder.typicode.com/posts/1')
        data2 = await fetch_url(session, 'https://jsonplaceholder.typicode.com/comments/1')
        print("--- Data from Post 1 ---")
        print(data1)
        print("
--- Data from Comment 1 ---")
        print(data2)

# To run this example:
# asyncio.run(main_http_example())
```

---

### Quiz

1.  **Is `asyncio` a good choice for CPU-bound tasks?**
    a) Yes
    b) No, it is single-threaded and will be blocked by CPU-bound work.

2.  **What does `asyncio.gather()` do?**
    a) Runs coroutines sequentially.
    b) Runs coroutines concurrently and waits for all to complete.
    c) Gathers results from a queue.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>