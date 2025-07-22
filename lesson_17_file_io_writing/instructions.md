# Lesson 17: File I/O: Writing to Files

In the previous lesson, you learned how to read data from files. Now, you'll learn how to **write** data to files, allowing your programs to save information, generate reports, or create new files.

## Opening a File for Writing

To write to a file, you use the `open()` function, but with different modes:

1.  `"w"` (Write Mode):
    *   Opens a file for writing.
    *   **If the file exists, its contents will be completely overwritten.**
    *   If the file does not exist, a new file will be created.

2.  `"a"` (Append Mode):
    *   Opens a file for appending.
    *   **If the file exists, new data will be written to the end of the file, preserving existing content.**
    *   If the file does not exist, a new file will be created.

**Syntax:**

```python
file_object = open("file_path", "mode")
```

**Example:**

```python
# Open a file in write mode (will overwrite if it exists)
file_w = open("my_output.txt", "w")
file_w.write("Hello, this is the first line.\n")
file_w.write("This is the second line.\n")
file_w.close()

# Open the same file in append mode
file_a = open("my_output.txt", "a")
file_a.write("This line is appended.\n")
file_a.close()

# Now, let's read the file to see the content
with open("my_output.txt", "r") as f:
    print(f.read())
# Expected Output:
# Hello, this is the first line.
# This is the second line.
# This line is appended.
```

## Writing Content to a File

Once a file is opened in write (`"w"`) or append (`"a"`) mode, you can use the `write()` method to add content.

*   **`write(string)`**: Writes the specified `string` to the file. It does not automatically add a newline character, so you need to include `\n` if you want content on separate lines.

**Example:**

```python
# Writing multiple lines
with open("my_report.txt", "w") as f:
    f.write("Daily Report\n")
    f.write("--------------\n")
    f.write("Sales: $1500\n")
    f.write("Expenses: $500\n")
    f.write("Profit: $1000\n")

# Appending to an existing file
with open("my_report.txt", "a") as f:
    f.write("\n-- End of Report --\n")

# Read to verify
with open("my_report.txt", "r") as f:
    print(f.read())
```

## The `with` Statement (Again!)

Just like with reading, it is highly recommended to use the `with` statement when writing to files. It ensures that the file is properly closed even if an error occurs during the write operation, preventing data loss or corruption.

```python
# Using with statement for writing
with open("log.txt", "w") as log_file:
    log_file.write("Application started.\n")
    log_file.write("User logged in.\n")

# Using with statement for appending
with open("log.txt", "a") as log_file:
    log_file.write("Data processed.\n")
    log_file.write("Application shut down.\n")
```

Mastering file I/O is essential for any program that needs to persist data or interact with external files.

---

### Quiz

1.  **Which mode will overwrite the contents of a file if it already exists?**
    a) `a`
    b) `w`
    c) `r`

2.  **Which mode should you use to add content to the end of an existing file?**
    a) `a`
    b) `w`
    c) `r+`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>