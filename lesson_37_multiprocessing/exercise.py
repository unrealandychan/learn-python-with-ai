# Lesson 37: Multiprocessing (`multiprocessing` module)

import multiprocessing
import time
import os

# --- Exercise 1: Basic Process Creation and Execution ---
# 1. Define a function `perform_calculation(name, num_iterations)` that simulates
#    a CPU-bound task. It should print a message indicating it's starting,
#    perform a simple calculation (e.g., sum of numbers up to num_iterations),
#    and then print a message indicating it's finishing.
# 2. In the main block (`if __name__ == '__main__':`),
#    create two `multiprocessing.Process` objects, each running `perform_calculation`
#    with different names and iteration counts.
# 3. Start both processes.
# 4. Use `join()` on both processes to wait for them to complete.
# 5. Print a message in the main process after both child processes have finished.

print("--- Exercise 1: Basic Process Creation and Execution ---")

def perform_calculation(name, num_iterations):
    print(f"Process {name}: Starting calculation with {num_iterations} iterations...")
    total = 0
    for i in range(num_iterations):
        total += i * 2 # Simple CPU-bound operation
    print(f"Process {name}: Finished calculation. Result (partial): {total % 10000}")

if __name__ == '__main__':
    # Your code for Exercise 1 here:
    process1 = multiprocessing.Process(target=perform_calculation, args=("Calc_A", 5_000_000))
    process2 = multiprocessing.Process(target=perform_calculation, args=("Calc_B", 7_000_000))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Main process: All calculations are complete.")


# --- Exercise 2: Using `multiprocessing.Pool` for Parallel Processing ---
# 1. Define a function `cube(number)` that returns the cube of a number.
#    Add a small `time.sleep()` to simulate some work.
# 2. Create a list of numbers (e.g., `range(1, 11)`).
# 3. In the main block, use `multiprocessing.Pool` to apply the `cube` function
#    to all numbers in the list in parallel.
# 4. Print the original numbers and the cubed results.

print("\n--- Exercise 2: Using `multiprocessing.Pool` for Parallel Processing ---")

def cube(number):
    time.sleep(0.05) # Simulate some work
    return number ** 3

if __name__ == '__main__':
    # Your code for Exercise 2 here:
    numbers_to_cube = range(1, 11)
    print(f"Numbers to cube: {list(numbers_to_cube)}")

    # Use a Pool with a number of processes equal to CPU count or a fixed number
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        cubed_results = pool.map(cube, numbers_to_cube)

    print(f"Cubed results: {cubed_results}")
    print("Main process: Pool operations complete.")


# --- Exercise 3: Inter-Process Communication with `multiprocessing.Queue` ---
# 1. Define a `producer` function that puts a few messages (strings) into a `multiprocessing.Queue`.
#    Include a `None` sentinel value at the end to signal completion.
# 2. Define a `consumer` function that continuously gets messages from the `Queue`
#    until it receives the `None` sentinel. It should print each message it receives.
# 3. In the main block, create a `multiprocessing.Queue`.
# 4. Create a `producer` process and a `consumer` process, passing the queue to both.
# 5. Start both processes and `join()` them.

print("\n--- Exercise 3: Inter-Process Communication with `multiprocessing.Queue` ---")

def producer(q):
    messages = ["Hello", "from", "the", "producer", "process!"]
    for msg in messages:
        print(f"Producer: Sending '{msg}'")
        q.put(msg)
        time.sleep(0.1)
    q.put(None) # Sentinel to signal end
    print("Producer: Finished sending messages.")

def consumer(q):
    while True:
        msg = q.get()
        if msg is None:
            break
        print(f"Consumer: Received '{msg}'")
        time.sleep(0.2)
    print("Consumer: Finished receiving messages.")

if __name__ == '__main__':
    # Your code for Exercise 3 here:
    message_queue = multiprocessing.Queue()

    producer_process = multiprocessing.Process(target=producer, args=(message_queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(message_queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("Main process: Producer and Consumer communication complete.")