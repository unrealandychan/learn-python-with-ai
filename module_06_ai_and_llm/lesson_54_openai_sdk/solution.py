"""
Lesson 54: The OpenAI SDK — Solutions
"""

import json

# ---- Mock client (same as exercise.py) ----
class MockMessage:
    def __init__(self, content):
        self.content = content
        self.tool_calls = None

class MockChoice:
    def __init__(self, content, finish_reason="stop"):
        self.message = MockMessage(content)
        self.finish_reason = finish_reason

class MockResponse:
    def __init__(self, content):
        self.choices = [MockChoice(content)]

class MockStreamChunk:
    class MockDelta:
        def __init__(self, content):
            self.content = content
    class MockChoice:
        def __init__(self, content):
            self.delta = MockStreamChunk.MockDelta(content)
    def __init__(self, content):
        self.choices = [self.MockChoice(content)]

class MockOpenAI:
    class _Completions:
        def create(self, model="gpt-4o-mini", messages=None, stream=False,
                   response_format=None, tools=None, **kwargs):
            last_user_msg = ""
            for m in reversed(messages or []):
                if m["role"] == "user":
                    last_user_msg = m["content"]
                    break

            if response_format and response_format.get("type") == "json_object":
                return MockResponse('{"name": "James", "city": "London", "country": "UK"}')

            content = f"[AI Response to: {last_user_msg[:40]}] Python is a versatile, readable language perfect for AI development."
            if stream:
                words = content.split()
                return [MockStreamChunk(w + " ") for w in words]
            return MockResponse(content)

    def __init__(self, api_key=None):
        self.chat = type('obj', (object,), {
            'completions': self._Completions()
        })()

client = MockOpenAI()

# ===========================================================
# SOLUTION 1: Basic Chat Completion
# ===========================================================
print("=" * 50)
print("Exercise 1: Basic Chat Completion")
print("=" * 50)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "What is Python in one sentence?"}
    ]
)
print(response.choices[0].message.content)

# ===========================================================
# SOLUTION 2: System Prompt
# ===========================================================
print("\n" + "=" * 50)
print("Exercise 2: System Prompt")
print("=" * 50)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a pirate who loves Python programming. Speak like a pirate but give accurate Python advice."},
        {"role": "user", "content": "How do I use a for loop?"}
    ]
)
print(response.choices[0].message.content)

# ===========================================================
# SOLUTION 3: Multi-Turn Conversation
# ===========================================================
print("\n" + "=" * 50)
print("Exercise 3: Multi-Turn Conversation")
print("=" * 50)

conversation = [
    {"role": "system", "content": "You are a concise Python tutor."}
]

questions = [
    "What is a list in Python?",
    "How do I add items to it?",
    "What about removing items?"
]

for question in questions:
    conversation.append({"role": "user", "content": question})
    response = client.chat.completions.create(model="gpt-4o-mini", messages=conversation)
    reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})
    print(f"User: {question}")
    print(f"AI: {reply}\n")

# ===========================================================
# SOLUTION 4: JSON Structured Output
# ===========================================================
print("=" * 50)
print("Exercise 4: JSON Structured Output")
print("=" * 50)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Extract information from text. Always respond with valid JSON."},
        {"role": "user", "content": "My name is James and I live in London, UK."}
    ],
    response_format={"type": "json_object"}
)

data = json.loads(response.choices[0].message.content)
for key, value in data.items():
    print(f"  {key}: {value}")

# ===========================================================
# SOLUTION 5: Streaming Response
# ===========================================================
print("\n" + "=" * 50)
print("Exercise 5: Streaming Response")
print("=" * 50)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Write a Python function that reverses a string"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
