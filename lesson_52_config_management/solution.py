
# Lesson 52: Solution

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access and print the variables
app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")

print(f"Application Name: {app_name}")
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")
