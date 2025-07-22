
# Lesson 35: Solution

import os
import sys

cwd = os.getcwd()
print(f"Current working directory: {cwd}")

try:
    os.mkdir("test_dir")
    print("Directory 'test_dir' created.")
except FileExistsError:
    print("Directory 'test_dir' already exists.")

print("\nContents of current directory:")
print(os.listdir('.'))

print(f"\nPython version: {sys.version}")
