
# Lesson 37: Solution

import multiprocessing

def sum_of_squares(n):
    return sum([i * i for i in range(n)])

if __name__ == "__main__":
    tasks = [1000000, 2000000, 3000000]

    with multiprocessing.Pool() as pool:
        results = pool.map(sum_of_squares, tasks)

    print("Results:", results)
