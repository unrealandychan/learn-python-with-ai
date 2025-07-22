
# Lesson 50: Solution

# Command-line steps:
# mkdir my-uv-project
# cd my-uv-project
# uv venv
# source .venv/bin/activate
# uv pip install requests pandas

# Python script (e.g., main.py):
import requests
import pandas as pd

print("requests version:", requests.__version__)
print("pandas version:", pd.__version__)
