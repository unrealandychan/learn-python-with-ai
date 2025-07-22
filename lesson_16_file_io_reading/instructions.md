# Lesson 16: File I/O: Reading from Files

In this lesson, you'll learn how to interact with files on your computer's file system. This is a crucial skill for many applications, allowing your programs to read data from external sources or save information for later use.

## What is File I/O?

**File I/O** stands for File Input/Output. It refers to the process of reading data from a file (input) or writing data to a file (output).

## Opening a File for Reading

Before you can read from a file, you need to **open** it. The `open()` function is used for this purpose. It takes at least two arguments:

1.  **`file_path`**: The path to the file you want to open (e.g., `"my_document.txt"`, `"data/report.csv"`).
2.  **`mode`**: A string indicating how the file should be opened. For reading, we use `"r"`.

**Syntax:**

```python
file_object = open("file_path", "mode")
```

**Example:**

```python
# Open a file named 'my_text_file.txt' in read mode
# (Assuming 'my_text_file.txt' exists in the same directory)
file = open("my_text_file.txt", "r")
```

## Reading File Content

Once a file is open, you can use various methods to read its content:

1.  **`read()`**: Reads the entire content of the file as a single string.
    ```python
    file = open("my_text_file.txt", "r")
    content = file.read()
    print(content)
    file.close() # Always close the file!
    ```

2.  **`readline()`**: Reads one line from the file at a time. Each call to `readline()` reads the next line.
    ```python
    file = open("my_text_file.txt", "r")
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)
    file.close()
    ```

3.  **`readlines()`**: Reads all lines from the file and returns them as a list of strings, where each string is a line.
    ```python
    file = open("my_text_file.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line.strip()) # .strip() removes leading/trailing whitespace, including newline characters
    file.close()
    ```

4.  **Iterating directly over the file object (most common and Pythonic):**
    You can loop directly over the file object, and it will read one line at a time efficiently.
    ```python
    file = open("my_text_file.txt", "r")
    for line in file:
        print(line.strip())
    file.close()
    ```

## Closing the File

It is **crucial** to close a file after you are done with it using the `close()` method. This releases the file from your program's control, frees up system resources, and ensures that any buffered writes are actually saved to disk.

If you forget to close a file, it can lead to data corruption, resource leaks, or errors when other programs try to access the same file.

## The `with` Statement (Recommended Approach)

Manually calling `close()` can be error-prone (e.g., if an error occurs before `close()` is called). Python's `with` statement provides a much safer and more convenient way to handle file operations. It ensures that the file is automatically closed, even if errors occur.

**Syntax:**

```python
with open("file_path", "mode") as file_object:
    # Perform file operations here
    # The file is automatically closed when exiting this block
```

**Example with `with` statement:**

```python
# Create a dummy file for demonstration
with open("example_read.txt", "w") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: World\n")

# Read the file using the with statement
with open("example_read.txt", "r") as file:
    content = file.read()
    print(content)
# The file is automatically closed here
```

Using the `with` statement is the recommended and most Pythonic way to handle file I/O.

--- 

### Quiz

1.  **What does the `"r"` mode stand for when opening a file?**
    a) `run`
    b) `read`
    c) `remove`

2.  **Why is using a `with` statement recommended?**
    a) It makes the code faster.
    b) It automatically closes the file.
    c) It automatically reads the file.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>