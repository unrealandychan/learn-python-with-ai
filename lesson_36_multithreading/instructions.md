
# Lesson 36: Multithreading (`threading` module)

Multithreading is a programming concept that allows a program to execute multiple parts of its code concurrently. In Python, this is achieved using the `threading` module. While threads can give the *appearance* of parallel execution, it's important to understand Python's Global Interpreter Lock (GIL) and its implications for CPU-bound tasks.

## Understanding Threads

*   **Thread:** A lightweight unit of execution within a process. Multiple threads can exist within the same process and share its resources (memory, files).
*   **Concurrency vs. Parallelism:**
    *   **Concurrency:** Deals with many things at once (managing multiple tasks that can make progress independently).
    *   **Parallelism:** Doing many things at once (simultaneously executing multiple tasks).
*   **Global Interpreter Lock (GIL):** A mutex (or a lock) that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. This means that even on multi-core processors, a single Python process can only execute one thread at a time for CPU-bound tasks. The GIL is released during I/O operations, making multithreading beneficial for I/O-bound tasks (e.g., network requests, file operations).

## The `threading` Module

Python's `threading` module provides a high-level way to work with threads.

### Key Concepts and Functions:

1.  **Creating a Thread:**
    *   **Subclassing `threading.Thread`:** Define a new class that inherits from `threading.Thread` and override its `run()` method. The code to be executed in the new thread goes inside `run()`.
    *   **Passing a Target Function:** Pass a function as the `target` argument to the `threading.Thread` constructor. You can also pass arguments to this function using `args` (for positional arguments) and `kwargs` (for keyword arguments).

2.  **Starting a Thread:**
    *   `thread_object.start()`: This method starts the thread's activity. It calls the `run()` method internally. You should call `start()` only once per thread object.

3.  **Waiting for a Thread to Finish:**
    *   `thread_object.join()`: This method blocks the calling thread (e.g., the main thread) until the thread whose `join()` method is called terminates. This is crucial when the main thread needs results from other threads or needs to ensure all threads complete before proceeding.

### Example 1: Basic Thread Creation with a Target Function

```python
import threading
import time

def task(name, duration):
    """A simple function to be run in a thread."""
    print(f"Thread {name}: Starting...")
    time.sleep(duration) # Simulate some work
    print(f"Thread {name}: Finished.")

print("Main thread: Starting threads.")

# Create thread objects
thread1 = threading.Thread(target=task, args=("One", 2))
thread2 = threading.Thread(target=task, args=("Two", 1))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Main thread: All threads finished.")
```

**Explanation:**

*   The `task` function simulates work using `time.sleep()`. This is an I/O-bound operation (waiting), so the GIL is released, allowing other threads to run concurrently.
*   `thread1.start()` and `thread2.start()` initiate the execution of `task` in separate threads.
*   `thread1.join()` and `thread2.join()` ensure that the main program waits for `thread1` and `thread2` to complete their execution before printing "Main thread: All threads finished."

### Example 2: Subclassing `threading.Thread`

```python
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        self.count = count

    def run(self):
        print(f"Thread {self.name}: Starting count.")
        for i in range(self.count):
            time.sleep(0.5)
            print(f"Thread {self.name}: Count {i+1}")
        print(f"Thread {self.name}: Finished count.")

print("Main thread: Creating custom threads.")

thread_a = MyThread("A", 3)
thread_b = MyThread("B", 2)

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()

print("Main thread: All custom threads finished.")
```

**Explanation:**

*   `MyThread` inherits from `threading.Thread`.
*   The `__init__` method calls the parent class's `__init__` to properly initialize the thread.
*   The `run` method contains the code that will be executed when the thread starts.

### Example 3: Using Locks for Thread Synchronization

When multiple threads try to access and modify shared resources (like a global variable), it can lead to race conditions and incorrect results. A `Lock` is a synchronization primitive that prevents multiple threads from simultaneously accessing a shared resource.

*   `threading.Lock()`: Creates a new lock.
*   `lock.acquire()`: Acquires the lock. If the lock is already acquired by another thread, this call blocks until the lock is released.
*   `lock.release()`: Releases the lock. It should only be called by the thread that acquired the lock.

```python
import threading
import time

shared_counter = 0
counter_lock = threading.Lock()

def increment_counter(iterations):
    global shared_counter
    for _ in range(iterations):
        # Acquire the lock before modifying shared_counter
        counter_lock.acquire()
        try:
            shared_counter += 1
        finally:
            # Ensure the lock is released even if an error occurs
            counter_lock.release()
        time.sleep(0.001) # Simulate some work

threads = []
for i in range(5):
    thread = threading.Thread(target=increment_counter, args=(1000,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"\nFinal shared counter value: {shared_counter}")
# Without locks, this value would likely be less than 5000 due to race conditions.
```

**Explanation:**

*   `shared_counter` is a global variable accessed by multiple threads.
*   `counter_lock` is used to protect `shared_counter`.
*   `counter_lock.acquire()` ensures that only one thread can increment `shared_counter` at a time.
*   The `try...finally` block ensures that `counter_lock.release()` is always called, even if an exception occurs during the increment operation.

---

### Quiz

1.  **What is the primary reason multithreading in Python is *not* ideal for CPU-bound tasks?**
    a) It's too complex to implement.
    b) The Global Interpreter Lock (GIL) allows only one thread to execute Python bytecode at a time.
    c) Threads consume too much memory.
    d) Python threads are slower than processes.

2.  **Which method is used to start a thread's execution?**
    a) `run()`
    b) `execute()`
    c) `start()`
    d) `begin()`

3.  **If you want the main program to wait until a specific thread finishes its execution, which method would you call on that thread object?**
    a) `wait()`
    b) `pause()`
    c) `join()`
    d) `finish()`

4.  **What is the purpose of a `threading.Lock`?**
    a) To speed up thread execution.
    b) To prevent multiple threads from simultaneously accessing and modifying shared resources.
    c) To terminate a thread.
    d) To create new threads.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
  3. c
  4. b
</details>
