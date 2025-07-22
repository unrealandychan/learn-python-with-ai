# Lesson 35: Interacting with the Operating System (`os` and `sys` modules)

import os
import sys

# --- Exercise 1: Basic `os` Module Operations ---
# 1. Get and print the current working directory.
# 2. Create a new directory named "my_temp_dir" in the current working directory.
#    Ensure it doesn't already exist before creating it.
# 3. List all files and directories in the current working directory and print them.

print("--- Exercise 1: Basic `os` Module Operations ---")

# Your code for Exercise 1 here:
current_working_directory = os.getcwd()
print(f"1. Current Working Directory: {current_working_directory}")

new_directory_name = "my_temp_dir"
if not os.path.exists(new_directory_name):
    os.mkdir(new_directory_name)
    print(f"2. Created directory: {new_directory_name}")
else:
    print(f"2. Directory '{new_directory_name}' already exists.")

print("3. Contents of current directory:")
for item in os.listdir():
    print(f"   - {item}")


# --- Exercise 2: Path Manipulation and File Operations ---
# 1. Inside "my_temp_dir", create a new text file named "my_file.txt".
#    Write the text "Hello, OS module!" into this file.
# 2. Construct the full path to "my_file.txt" using `os.path.join()`.
# 3. Verify that "my_file.txt" exists using `os.path.exists()`.
# 4. Remove "my_file.txt".
# 5. Remove the "my_temp_dir" directory.
#    Ensure both removals are conditional on their existence.

print("\n--- Exercise 2: Path Manipulation and File Operations ---")

# Your code for Exercise 2 here:
file_to_create = os.path.join(new_directory_name, "my_file.txt")

with open(file_to_create, 'w') as f:
    f.write("Hello, OS module!")
print(f"1. Created file: {file_to_create}")

print(f"2. Full path to my_file.txt: {file_to_create}")

if os.path.exists(file_to_create):
    print(f"3. Verified: {file_to_create} exists.")
    os.remove(file_to_create)
    print(f"4. Removed file: {file_to_create}")
else:
    print(f"3. Error: {file_to_create} does not exist.")

if os.path.exists(new_directory_name):
    if not os.listdir(new_directory_name): # Check if directory is empty before removing
        os.rmdir(new_directory_name)
        print(f"5. Removed directory: {new_directory_name}")
    else:
        print(f"5. Directory '{new_directory_name}' is not empty, cannot remove.")


# --- Exercise 3: `sys` Module Information ---
# 1. Print the Python version being used.
# 2. Print the operating system platform.
# 3. Simulate command-line arguments and print them using `sys.argv`.
#    (Note: To truly test `sys.argv`, you'd run this script from the command line like:
#    `python your_script_name.py arg1 arg2`)

print("\n--- Exercise 3: `sys` Module Information ---")

# Your code for Exercise 3 here:
print(f"1. Python Version: {sys.version.split('\n')[0]}")
print(f"2. Operating System Platform: {sys.platform}")

print(f"3. Command-line arguments (sys.argv): {sys.argv}")
if len(sys.argv) > 1:
    print(f"   (First argument after script name: {sys.argv[1]})")
else:
    print("   (No additional command-line arguments provided. Try running: python exercise.py hello world)")