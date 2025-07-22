
# Lesson 37: Multiprocessing (`multiprocessing` module)

Multiprocessing is a technique that allows a program to run multiple processes concurrently. Unlike threads, each process has its own independent memory space and Python interpreter. This is particularly beneficial for CPU-bound tasks in Python because it bypasses the Global Interpreter Lock (GIL), enabling true parallel execution on multi-core processors.

## Understanding Processes

*   **Process:** An independent execution unit that has its own memory space, resources, and Python interpreter. Processes are heavier than threads but offer true parallelism for CPU-bound tasks.
*   **GIL (Global Interpreter Lock) Bypass:** Since each process has its own Python interpreter, the GIL is not an issue for multiprocessing. Each process runs its own GIL, allowing multiple processes to execute Python bytecode simultaneously on different CPU cores.

## The `multiprocessing` Module

Python's `multiprocessing` module provides an API similar to the `threading` module, making it relatively easy to use for parallel programming.

### Key Concepts and Functions:

1.  **Creating a Process:**
    *   **Subclassing `multiprocessing.Process`:** Define a new class that inherits from `multiprocessing.Process` and override its `run()` method.
    *   **Passing a Target Function:** Pass a function as the `target` argument to the `multiprocessing.Process` constructor. Arguments can be passed using `args` and `kwargs`.

2.  **Starting a Process:**
    *   `process_object.start()`: This method starts the process's activity. It calls the `run()` method internally.

3.  **Waiting for a Process to Finish:**
    *   `process_object.join()`: This method blocks the calling process (e.g., the main process) until the process whose `join()` method is called terminates.

4.  **Inter-Process Communication (IPC):**
    *   **Queues (`multiprocessing.Queue`):** A FIFO (First-In, First-Out) data structure that allows processes to safely exchange messages.
    *   **Pipes (`multiprocessing.Pipe`):** A two-way communication channel between two processes.
    *   **Shared Memory (`multiprocessing.Value`, `multiprocessing.Array`):** Allows processes to share data directly in memory, but requires careful synchronization.

5.  **Process Pools (`multiprocessing.Pool`):**
    *   Provides a convenient way to manage a pool of worker processes. It can distribute tasks among these processes and collect results.
    *   `pool.map(func, iterable)`: Applies `func` to each item in `iterable` in parallel.
    *   `pool.apply_async(func, args)`: A variant of `apply()` which returns a result object. The result is available via `get()` method of the result object.

### Example 1: Basic Process Creation with a Target Function

```python
import multiprocessing
import time

def cpu_bound_task(name, iterations):
    """A CPU-bound task to demonstrate multiprocessing."""
    print(f"Process {name}: Starting CPU-bound task...")
    result = 0
    for i in range(iterations):
        result += i * i # Simulate heavy computation
    print(f"Process {name}: Finished. Result (partial): {result % 1000}")

if __name__ == '__main__': # Essential for multiprocessing on Windows/macOS
    print("Main process: Starting child processes.")

    # Create process objects
    p1 = multiprocessing.Process(target=cpu_bound_task, args=("One", 10**7))
    p2 = multiprocessing.Process(target=cpu_bound_task, args=("Two", 10**7))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    print("Main process: All child processes finished.")
```

**Explanation:**

*   The `if __name__ == '__main__':` block is crucial for multiprocessing, especially on Windows and macOS, to prevent child processes from recursively importing the main script and creating infinite processes.
*   `cpu_bound_task` performs a heavy computation, making it suitable for multiprocessing.
*   `p1.start()` and `p2.start()` launch the tasks in separate processes, allowing them to run in parallel on multi-core systems.
*   `p1.join()` and `p2.join()` ensure the main process waits for the child processes to complete.

### Example 2: Using `multiprocessing.Pool` for Parallel Execution

`Pool` objects manage a pool of worker processes. They are ideal for parallelizing the execution of a function across a range of inputs.

```python
import multiprocessing
import time

def square(number):
    """A simple function to square a number, simulating some work."""
    time.sleep(0.1) # Simulate some computation time
    return number * number

if __name__ == '__main__':
    print("Main process: Using a Pool to square numbers.")

    numbers = range(10)

    # Create a Pool with a specified number of processes (e.g., 4)
    # If no number is specified, it defaults to os.cpu_count()
    with multiprocessing.Pool(processes=4) as pool:
        # Map the square function to each number in the list
        # This distributes the work across the processes in the pool
        results = pool.map(square, numbers)

    print(f"Original numbers: {list(numbers)}")
    print(f"Squared results: {results}")
    print("Main process: Pool operations complete.")
```

**Explanation:**

*   `multiprocessing.Pool(processes=4)` creates a pool of 4 worker processes.
*   `pool.map(square, numbers)` applies the `square` function to each number in the `numbers` iterable. The `Pool` automatically distributes these tasks among its worker processes.
*   The `with` statement ensures that the pool is properly closed and terminated after the tasks are done.

### Example 3: Inter-Process Communication with `multiprocessing.Queue`

Queues are useful for passing messages or data between processes.

```python
import multiprocessing
import time

def producer(queue, items):
    """Puts items into the queue."""
    for item in items:
        print(f"Producer: Putting {item} into queue.")
        queue.put(item)
        time.sleep(0.5)
    queue.put(None) # Sentinel value to signal end of production

def consumer(queue):
    """Gets items from the queue and processes them."""
    while True:
        item = queue.get()
        if item is None: # Check for sentinel value
            break
        print(f"Consumer: Got {item} from queue. Processing...")
        time.sleep(0.7)
    print("Consumer: Finished.")

if __name__ == '__main__':
    print("Main process: Setting up producer-consumer with Queue.")

    q = multiprocessing.Queue()
    data_items = ["data1", "data2", "data3", "data4"]

    p_producer = multiprocessing.Process(target=producer, args=(q, data_items))
    p_consumer = multiprocessing.Process(target=consumer, args=(q,))

    p_producer.start()
    p_consumer.start()

    p_producer.join()
    p_consumer.join()

    print("Main process: Producer and Consumer processes finished.")
```

**Explanation:**

*   `multiprocessing.Queue()` creates a queue that can be safely shared between processes.
*   The `producer` process puts items into the queue, and the `consumer` process gets items from it.
*   A `None` sentinel value is used to signal the consumer that no more items will be produced.

---

### Quiz

1.  **What is the primary advantage of using `multiprocessing` over `threading` for CPU-bound tasks in Python?**
    a) Processes are lighter-weight than threads.
    b) Multiprocessing allows for true parallel execution by bypassing the GIL.
    c) Processes share memory more efficiently.
    d) It's simpler to implement.

2.  **Which of the following is essential for `multiprocessing` to work correctly on Windows and macOS?**
    a) Using `threading.Lock`.
    b) Enclosing the main logic within `if __name__ == '__main__':`.
    c) Importing `sys` module.
    d) Running the script with `python -m`.

3.  **Which `multiprocessing` class is best suited for distributing a function across a collection of inputs to a pool of worker processes?**
    a) `multiprocessing.Queue`
    b) `multiprocessing.Process`
    c) `multiprocessing.Pool`
    d) `multiprocessing.Pipe`

4.  **How can two independent processes safely exchange data in `multiprocessing`?**
    a) Directly accessing global variables.
    b) Using `multiprocessing.Queue` or `multiprocessing.Pipe`.
    c) Passing data via function return values.
    d) Through shared file descriptors only.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
  3. c
  4. b
</details>
