
# Lesson 36: Solution

import threading
import time

def download_file(filename):
    print(f"Downloading {filename}...")
    time.sleep(2)
    print(f"Finished downloading {filename}.")

def process_file(filename):
    print(f"Processing {filename}...")
    time.sleep(3)
    print(f"Finished processing {filename}.")

file_to_process = "data.csv"

t1 = threading.Thread(target=download_file, args=(file_to_process,))
t2 = threading.Thread(target=process_file, args=(file_to_process,))

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks finished.")
