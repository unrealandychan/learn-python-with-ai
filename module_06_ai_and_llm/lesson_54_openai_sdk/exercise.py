"""
Lesson 54: The OpenAI SDK — Calling LLMs from Python
Exercise File

This exercise uses a MOCK OpenAI client so it works without an API key.
The mock has the exact same interface as the real OpenAI SDK.
When you're ready to use the real API, just replace MockOpenAI with OpenAI.
"""

import json
import os

# ============================================================
# MOCK OPENAI CLIENT
# (Same interface as the real SDK — swap for real when ready)
# ============================================================

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
    """Drop-in mock for openai.OpenAI() — works without an API key."""

    class _Completions:
        RESPONSES = {
            "gpt-4o-mini": "I'm GPT-4o Mini, a fast and efficient AI assistant.",
        }

        def create(self, model="gpt-4o-mini", messages=None, stream=False,
                   response_format=None, tools=None, temperature=1, max_tokens=None):
            # Find the last user message
            last_user_msg = ""
            for m in reversed(messages or []):
                if m["role"] == "user":
                    last_user_msg = m["content"].lower()
                    break

            # Generate contextual mock responses
            if tools:
                # Simulate a tool call response
                class ToolCall:
                    class Function:
                        name = "get_weather"
                        arguments = '{"city": "Tokyo", "unit": "celsius"}'
                    function = Function()
                    id = "call_mock_001"

                mock_msg = MockMessage(None)
                mock_msg.tool_calls = [ToolCall()]
                choice = MockChoice(None, finish_reason="tool_calls")
                choice.message = mock_msg
                resp = MockResponse(None)
                resp.choices = [choice]
                return resp

            if response_format and response_format.get("type") == "json_object":
                # Simulate JSON extraction
                content = '{"name": "Maria", "city": "Barcelona", "extracted": true}'
                return MockResponse(content)

            # Build a contextual response
            if "explain" in last_user_msg or "what is" in last_user_msg:
                content = "Great question! In Python, this concept helps you write cleaner, more efficient code. The key idea is to break complex problems into smaller, reusable pieces."
            elif "write" in last_user_msg or "create" in last_user_msg or "function" in last_user_msg:
                content = "```python\ndef example_function(items):\n    \"\"\"A well-structured Python function.\"\"\"\n    return [item for item in items if item is not None]\n```"
            elif "hello" in last_user_msg or "hi" in last_user_msg:
                content = "Hello! I'm your AI assistant. How can I help you learn Python today?"
            else:
                content = f"I understand you're asking about: '{last_user_msg[:50]}...'. This is a fascinating topic in AI development. Let me explain..."

            if stream:
                words = content.split()
                return [MockStreamChunk(w + " ") for w in words]

            return MockResponse(content)

    def __init__(self, api_key=None):
        self.chat = type('obj', (object,), {
            'completions': self._Completions()
        })()

# ============================================================
# To use the REAL OpenAI API instead:
#
# from openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()
# client = OpenAI()  # reads OPENAI_API_KEY from environment
# ============================================================

client = MockOpenAI()


# ===========================================================
# EXERCISE 1: Basic Chat Completion
# ===========================================================
# TODO: Send a message to the AI asking it to explain what
# Python is in one sentence. Print the response.
#
# Hint: Use client.chat.completions.create() with:
#   - model="gpt-4o-mini"
#   - messages=[{"role": "user", "content": "...your question..."}]

print("=" * 50)
print("Exercise 1: Basic Chat Completion")
print("=" * 50)

# YOUR CODE HERE:


# ===========================================================
# EXERCISE 2: System Prompt — Setting AI Persona
# ===========================================================
# TODO: Create a response with:
#   - A system message making the AI act as a "pirate who loves Python"
#   - A user message asking: "How do I use a for loop?"
# Print the response.

print("\n" + "=" * 50)
print("Exercise 2: System Prompt")
print("=" * 50)

# YOUR CODE HERE:


# ===========================================================
# EXERCISE 3: Multi-Turn Conversation
# ===========================================================
# TODO: Build a 3-turn conversation:
#   Turn 1 (user): "What is a list in Python?"
#   Turn 2 (user): "How do I add items to it?"
#   Turn 3 (user): "What about removing items?"
#
# After each turn, add the assistant's reply to the messages list
# so the AI has context. Print each response.

print("\n" + "=" * 50)
print("Exercise 3: Multi-Turn Conversation")
print("=" * 50)

# YOUR CODE HERE:


# ===========================================================
# EXERCISE 4: JSON Structured Output
# ===========================================================
# TODO: Ask the AI to extract information from this text:
#   "My name is James and I live in London, UK."
# Use response_format={"type": "json_object"} to get JSON back.
# Parse the JSON and print each key-value pair.

print("\n" + "=" * 50)
print("Exercise 4: JSON Structured Output")
print("=" * 50)

# YOUR CODE HERE:


# ===========================================================
# EXERCISE 5: Streaming Response
# ===========================================================
# TODO: Ask the AI to "Write a Python function that reverses a string"
# Use stream=True and print each chunk as it arrives (no newline between chunks).
# Add a newline at the end.

print("\n" + "=" * 50)
print("Exercise 5: Streaming Response")
print("=" * 50)

# YOUR CODE HERE:


print("\n✅ All exercises complete! When ready, swap MockOpenAI for OpenAI and use a real API key.")
