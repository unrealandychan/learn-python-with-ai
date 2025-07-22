
# Lesson 38: Solution

import asyncio
import time

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def main():
    start_time = time.time()
    await asyncio.gather(task1(), task2())
    end_time = time.time()
    print(f"All tasks finished in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
