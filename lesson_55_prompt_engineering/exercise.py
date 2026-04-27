"""
Lesson 55: Prompt Engineering in Code
Exercise File

Practice building prompts programmatically using Python.
This file works without an API key using the MockOpenAI client.
"""


# ---- Simple mock client ----
class MockOpenAI:
    class _Completions:
        def create(self, model="gpt-4o-mini", messages=None, temperature=1, **kwargs):
            last_msg = next((m["content"] for m in reversed(messages or []) if m["role"] == "user"), "")
            system_msg = next((m["content"] for m in (messages or []) if m["role"] == "system"), "")

            # Simulate different behaviors based on prompts
            if "POSITIVE" in last_msg or "NEGATIVE" in last_msg or "sentiment" in last_msg.lower():
                response = "POSITIVE"
            elif "JSON" in system_msg or "json" in last_msg.lower():
                response = '{"name": "Alice", "role": "Engineer", "company": "TechCorp"}'
            elif "step by step" in last_msg.lower():
                response = "Step 1: Identify the variables.\nStep 2: Apply the formula.\nStep 3: The answer is 42."
            elif "bullet" in last_msg.lower() or "•" in last_msg:
                response = "• AI is transforming software development.\n• Python is the dominant AI language.\n• Prompt engineering is a key skill."
            else:
                response = f"[Simulated response to prompt about: {last_msg[:60]}]"

            class Msg:
                content = response
            class Ch:
                message = Msg()
            class Resp:
                choices = [Ch()]
            return Resp()

    def __init__(self, api_key=None):
        self.chat = type('obj', (object,), {'completions': self._Completions()})()


client = MockOpenAI()


# ===========================================================
# EXERCISE 1: Few-Shot Sentiment Classifier
# ===========================================================
# TODO: Write a function `classify_sentiment(review: str) -> str`
# that uses a few-shot prompt with 3 examples (POSITIVE, NEGATIVE, NEUTRAL)
# to classify the sentiment of a given review.
# Return just the classification string.

def classify_sentiment(review: str) -> str:
    """Classify review sentiment using few-shot prompting."""
    # YOUR CODE HERE: Build a few-shot prompt and call client.chat.completions.create()
    pass


# Test it:
print("=" * 50)
print("Exercise 1: Few-Shot Sentiment Classifier")
print("=" * 50)
test_reviews = [
    "Absolutely love this product! Works perfectly.",
    "Waste of money. Broke after one day.",
    "It's fine, does the job."
]
for review in test_reviews:
    result = classify_sentiment(review)
    print(f"Review: {review[:40]}...")
    print(f"Sentiment: {result}\n")


# ===========================================================
# EXERCISE 2: Dynamic Prompt Builder
# ===========================================================
# TODO: Write a function `build_summary_prompt(text: str, num_points: int, focus: str) -> str`
# that builds a prompt asking the AI to summarize `text` in `num_points` bullet points
# focusing on `focus` (e.g., "technical details", "business impact").
# Then use it to summarize the sample text below.

SAMPLE_TEXT = """
Python 3.12 was released in October 2023 with significant performance improvements.
The new version includes a 5% overall speedup, better error messages with more context,
and a new type parameter syntax for generics. The f-string parser was also rewritten
to support multi-line expressions and reuse of quotes. For developers building AI systems,
the improved asyncio performance is particularly valuable for handling concurrent API calls.
"""

def build_summary_prompt(text: str, num_points: int, focus: str) -> str:
    """Build a dynamic summary prompt."""
    # YOUR CODE HERE
    pass


print("=" * 50)
print("Exercise 2: Dynamic Prompt Builder")
print("=" * 50)
prompt = build_summary_prompt(SAMPLE_TEXT, num_points=3, focus="developer benefits")
if prompt:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)


# ===========================================================
# EXERCISE 3: Information Extractor with JSON Output
# ===========================================================
# TODO: Write a function `extract_contact_info(text: str) -> dict`
# that prompts the AI to extract name, email, company, and role from text.
# Use a system prompt that instructs JSON-only output.
# Parse and return the result as a Python dict.
# If a field is missing, it should be None.

import json

def extract_contact_info(text: str) -> dict:
    """Extract structured contact info from unstructured text."""
    # YOUR CODE HERE
    pass


print("\n" + "=" * 50)
print("Exercise 3: Information Extractor")
print("=" * 50)
text = "Hi, I'm Alice Chen, a Senior Engineer at TechCorp. Reach me at alice@techcorp.com"
info = extract_contact_info(text)
if info:
    print("Extracted info:")
    for key, value in info.items():
        print(f"  {key}: {value}")


# ===========================================================
# EXERCISE 4: Chain of Thought Prompting
# ===========================================================
# TODO: Write a function `solve_with_reasoning(problem: str) -> str`
# that uses a chain-of-thought prompt ("Let's think step by step...")
# to solve a problem. Return the full response.

def solve_with_reasoning(problem: str) -> str:
    """Use chain-of-thought prompting to solve a problem."""
    # YOUR CODE HERE
    pass


print("\n" + "=" * 50)
print("Exercise 4: Chain of Thought")
print("=" * 50)
problem = "A Python script processes 1000 API requests. Each takes 0.5s sequentially. How long does it take? What if we use 10 concurrent workers?"
result = solve_with_reasoning(problem)
if result:
    print(result)


# ===========================================================
# EXERCISE 5: Prompt Template System
# ===========================================================
# TODO: Create a dictionary TEMPLATES with at least 3 prompt templates
# (e.g., "translate", "explain_code", "write_tests").
# Each template should be a string with {placeholders}.
# Write a function `apply_template(name: str, **kwargs) -> str`
# that formats and returns the template.

TEMPLATES = {
    # YOUR CODE HERE: Add at least 3 templates
}

def apply_template(name: str, **kwargs) -> str:
    """Apply a named prompt template with the given variables."""
    # YOUR CODE HERE
    pass


print("\n" + "=" * 50)
print("Exercise 5: Template System")
print("=" * 50)
if TEMPLATES:
    # Test your templates here
    for template_name in TEMPLATES:
        print(f"Template available: {template_name}")
