# Lesson 54: The OpenAI SDK — Calling LLMs from Python

This lesson is where Python meets AI. You'll learn to call Large Language Models (LLMs) programmatically using the official OpenAI Python SDK — the same patterns used in production AI applications.

## Why This Matters

Every modern AI application — from chatbots to document analyzers to autonomous agents — is built on the pattern you'll learn here:

1. Construct a structured message payload
2. Send it to a model via API
3. Parse the structured response
4. Use the result in your program

Once you understand this pattern, you can build anything.

## Installation

```bash
pip install openai python-dotenv
```

## Setting Up Your API Key

**Never hardcode API keys in source code.** Use environment variables:

```bash
# Create a .env file in your project root:
OPENAI_API_KEY=sk-...your-key-here...
```

Then load it in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

## The Chat Completions API

The most important API in the OpenAI SDK. You send a list of messages, and the model replies.

```python
from openai import OpenAI

client = OpenAI()  # Reads OPENAI_API_KEY from environment automatically

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful Python tutor."},
        {"role": "user", "content": "Explain list comprehensions in one sentence."}
    ]
)

# Extract the text from the response
answer = response.choices[0].message.content
print(answer)
```

## Message Roles

| Role | Purpose |
|------|---------|
| `system` | Sets the AI's personality, persona, and constraints |
| `user` | What the human says |
| `assistant` | What the AI said (used for multi-turn conversations) |

## Multi-Turn Conversations

Build a conversation by accumulating messages:

```python
from openai import OpenAI

client = OpenAI()

conversation = [
    {"role": "system", "content": "You are a concise Python expert."}
]

# Turn 1
conversation.append({"role": "user", "content": "What is a decorator?"})
response = client.chat.completions.create(model="gpt-4o-mini", messages=conversation)
assistant_reply = response.choices[0].message.content
conversation.append({"role": "assistant", "content": assistant_reply})
print(f"AI: {assistant_reply}")

# Turn 2
conversation.append({"role": "user", "content": "Give me a simple example."})
response = client.chat.completions.create(model="gpt-4o-mini", messages=conversation)
print(f"AI: {response.choices[0].message.content}")
```

## Streaming Responses

For long responses, streaming lets you display text as it generates (like ChatGPT):

```python
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Write a Python function that sorts a list."}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()  # newline at end
```

## Structured Output with JSON Mode

Get structured data back from the model:

```python
from openai import OpenAI
import json

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You extract information from text. Always respond with valid JSON."
        },
        {
            "role": "user",
            "content": "Extract the name and city from: 'Hi, I'm Maria from Barcelona'"
        }
    ],
    response_format={"type": "json_object"}
)

data = json.loads(response.choices[0].message.content)
print(data)  # {'name': 'Maria', 'city': 'Barcelona'}
```

## Function Calling (Tool Use)

Tell the model about functions it can call, and it will return structured arguments:

```python
from openai import OpenAI
import json

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "The city name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["city"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools
)

# If the model wants to call a tool:
if response.choices[0].finish_reason == "tool_calls":
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    print(f"Model wants to call: {function_name}({arguments})")
    # Output: Model wants to call: get_weather({'city': 'Tokyo'})
```

## Key Parameters

| Parameter | What It Does |
|-----------|-------------|
| `model` | Which model to use (`gpt-4o`, `gpt-4o-mini`, etc.) |
| `temperature` | Randomness: 0 = deterministic, 2 = very random (default: 1) |
| `max_tokens` | Maximum length of the response |
| `top_p` | Alternative to temperature for controlling randomness |

## Running Without an API Key (Mock Mode)

The exercise file uses a mock client so you can learn the patterns without spending credits:

```python
# Mock response that mimics the real OpenAI response structure
class MockChoice:
    class MockMessage:
        content = "This is a simulated AI response."
    message = MockMessage()

class MockResponse:
    choices = [MockChoice()]

# This has the same interface as the real response!
response = MockResponse()
print(response.choices[0].message.content)
```

---

### Quiz

1. **What are the three message roles in the Chat Completions API?**
2. **Why should you never hardcode your API key in source code?**
3. **What does `stream=True` enable?**

<details>
  <summary><b>Answer Key</b></summary>
  1. system, user, assistant
  2. Security risk — anyone who sees your code gets free access to your account
  3. Streaming lets you receive and display the response token-by-token as it generates, instead of waiting for the full response
</details>
