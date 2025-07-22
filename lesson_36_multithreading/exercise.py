# Lesson 36: Multithreading (`threading` module)

import threading
import time
import random

# --- Exercise 1: Basic Thread Creation and Execution ---
# 1. Define a function `worker_task(name, duration)` that prints a message
#    indicating it's starting, sleeps for `duration` seconds, and then prints
#    a message indicating it's finishing.
# 2. Create two threads, each running `worker_task` with different names and durations.
# 3. Start both threads.
# 4. Observe the interleaved output, demonstrating concurrency.

print("--- Exercise 1: Basic Thread Creation and Execution ---")

def worker_task(name, duration):
    print(f"Thread {name}: Starting work for {duration} seconds...")
    time.sleep(duration)
    print(f"Thread {name}: Finished work.")

# Your code for Exercise 1 here:
thread_a = threading.Thread(target=worker_task, args=("A", 3))
thread_b = threading.Thread(target=worker_task, args=("B", 2))

thread_a.start()
thread_b.start()

# Note: We are not using .join() here to demonstrate interleaved output.
# The main program might finish before threads if they are long-running.


# --- Exercise 2: Waiting for Threads with `join()` ---
# 1. Define a function `download_file(filename, delay)` that simulates downloading
#    a file. It should print messages for starting and finishing download,
#    and sleep for `delay` seconds.
# 2. Define a function `process_data(data_size, delay)` that simulates processing
#    data. It should print messages for starting and finishing processing,
#    and sleep for `delay` seconds.
# 3. Create two threads: one for `download_file` and one for `process_data`.
# 4. Start both threads.
# 5. Use `join()` on both threads to ensure the main program waits for them to complete.
# 6. Print a message in the main thread only after both threads have finished.

print("\n--- Exercise 2: Waiting for Threads with `join()` ---")

def download_file(filename, delay):
    print(f"Downloading '{filename}' (estimated {delay}s)...")
    time.sleep(delay)
    print(f"Finished downloading '{filename}'.")

def process_data(data_size, delay):
    print(f"Processing {data_size}MB of data (estimated {delay}s)...")
    time.sleep(delay)
    print(f"Finished processing {data_size}MB of data.")

# Your code for Exercise 2 here:
download_thread = threading.Thread(target=download_file, args=("report.pdf", 4))
process_thread = threading.Thread(target=process_data, args=(100, 3))

download_thread.start()
process_thread.start()

download_thread.join()
process_thread.join()

print("Main thread: All download and processing tasks are complete.")


# --- Exercise 3: Thread Synchronization with `threading.Lock` ---
# 1. Initialize a global variable `bank_balance = 1000`.
# 2. Create a `threading.Lock` object.
# 3. Define a function `deposit(amount)` that simulates depositing money.
#    It should acquire the lock, update `bank_balance`, print the new balance,
#    and then release the lock. Simulate a small delay.
# 4. Define a function `withdraw(amount)` that simulates withdrawing money.
#    It should acquire the lock, update `bank_balance`, print the new balance,
#    and then release the lock. Simulate a small delay.
# 5. Create multiple threads (e.g., 5-10 threads), some calling `deposit` and some `withdraw`.
# 6. Start all threads and `join()` them.
# 7. Print the final `bank_balance`.
#    Observe how the lock ensures correct balance updates, preventing race conditions.

print("\n--- Exercise 3: Thread Synchronization with `threading.Lock` ---")

bank_balance = 1000
balance_lock = threading.Lock()

def deposit(amount):
    global bank_balance
    print(f"Attempting to deposit {amount}...")
    balance_lock.acquire()
    try:
        time.sleep(random.uniform(0.01, 0.1)) # Simulate network delay
        bank_balance += amount
        print(f"Deposited {amount}. New balance: {bank_balance}")
    finally:
        balance_lock.release()

def withdraw(amount):
    global bank_balance
    print(f"Attempting to withdraw {amount}...")
    balance_lock.acquire()
    try:
        time.sleep(random.uniform(0.01, 0.1)) # Simulate network delay
        if bank_balance >= amount:
            bank_balance -= amount
            print(f"Withdrew {amount}. New balance: {bank_balance}")
        else:
            print(f"Insufficient funds to withdraw {amount}. Current balance: {bank_balance}")
    finally:
        balance_lock.release()

# Your code for Exercise 3 here:
threads = []
threads.append(threading.Thread(target=deposit, args=(100,)))
threads.append(threading.Thread(target=withdraw, args=(50,)))
threads.append(threading.Thread(target=deposit, args=(200,)))
threads.append(threading.Thread(target=withdraw, args=(150,)))
threads.append(threading.Thread(target=deposit, args=(50,)))
threads.append(threading.Thread(target=withdraw, args=(1000,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"\nFinal Bank Balance: {bank_balance}")