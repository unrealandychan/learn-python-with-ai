# Lesson 01: Intro to Python — Your Gateway to the AI Era

Welcome to your very first Python lesson. You're not just learning a programming language — you're learning the language of AI.

## Why Python for AI?

Python is the #1 language for AI and machine learning. Here's the proof:
- **OpenAI, Google DeepMind, Meta AI** — all use Python as their primary language
- **Every major AI library** (TensorFlow, PyTorch, LangChain, Hugging Face) has Python as its first-class interface
- **ChatGPT, Gemini, Claude** — you call all of them from Python with just a few lines of code

Python was created by Guido van Rossum and first released in 1991. Its design philosophy prioritizes **readability** — code that humans can understand easily. This turned out to be perfect for AI, where you need to express complex ideas clearly.

## Your First Python Program

The `print()` function displays output to the terminal. It's your main tool for seeing what's happening in your code.

```python
# This is a comment — Python ignores it
# Comments explain what your code does

print("Hello, World!")          # Classic first program
print("Hello, AI era!")         # AI-focused greeting
print("Python + AI = 🚀")       # f-strings and emojis work too
```

## What You'll Build in This Course

By the end of 60 lessons, you'll write code like this:

```python
# This is what REAL AI code looks like — you'll understand all of it soon!
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain Python in one sentence."}
    ]
)

print(response.choices[0].message.content)
# Output: "Python is a versatile, readable programming language widely used in AI and data science."
```

Every concept you learn — variables, loops, functions, classes — exists to help you write code like this, but better.

## How to Run Python Code

1. Open `exercise.py` in your code editor (VS Code recommended)
2. Write your code
3. Open your terminal and run:
   ```bash
   python exercise.py
   # or on macOS/Linux:
   python3 exercise.py
   ```

## The Python Interpreter

Python is **interpreted** — it runs your code line by line. This makes development fast: write code, run it instantly, see the result.

```python
print("Line 1 runs first")
print("Line 2 runs second")
print("Line 3 runs third")
```

If there's an error on line 2, Python runs line 1, then stops at line 2 and shows you exactly what went wrong.

## Comments: Your Future Self Will Thank You

```python
# Single-line comment: explain what the next line does

"""
Multi-line comment (docstring):
Used to explain a whole block of code.
In AI development, always document what your prompts do
and why you chose specific parameters.
"""

print("Comments make code readable — and AI code can get complex!")
```

---

### Quiz

1. **Why is Python the dominant language for AI?**
   a) It's the fastest language
   b) It has the most readable syntax and the richest AI library ecosystem
   c) It was designed specifically for AI

2. **What does the `print()` function do?**
   a) Creates a variable
   b) Displays output to the terminal
   c) Sends data to a printer

3. **What does "interpreted" mean?**
   a) Python translates your code to another language first
   b) Python runs your code line by line
   c) Python requires compilation before running

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
  3. b
</details>
