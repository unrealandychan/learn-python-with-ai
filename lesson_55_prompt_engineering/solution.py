"""
Lesson 55: Prompt Engineering in Code — Solutions
"""

import json


# ---- Mock client ----
class MockOpenAI:
    class _Completions:
        def create(self, model="gpt-4o-mini", messages=None, temperature=1, **kwargs):
            last_msg = next((m["content"] for m in reversed(messages or []) if m["role"] == "user"), "")
            system_msg = next((m["content"] for m in (messages or []) if m["role"] == "system"), "")

            if "POSITIVE" in last_msg or "NEGATIVE" in last_msg or "→" in last_msg:
                response = "POSITIVE"
            elif "JSON" in system_msg or "json" in system_msg.lower():
                response = '{"name": "Alice Chen", "email": "alice@techcorp.com", "company": "TechCorp", "role": "Senior Engineer"}'
            elif "step by step" in last_msg.lower():
                response = "Step 1: Sequential time = 1000 × 0.5s = 500 seconds.\nStep 2: With 10 workers, requests run in batches of 10.\nStep 3: 1000/10 = 100 batches × 0.5s = 50 seconds.\nFinal Answer: Sequential takes 500s; parallel takes ~50s (10x speedup)."
            elif "bullet" in last_msg.lower() or "•" in last_msg or "points" in last_msg.lower():
                response = "• Python 3.12 delivers a 5% performance improvement across the board.\n• Rewritten f-string parser enables multi-line expressions and quote reuse.\n• Improved asyncio performance benefits AI developers making concurrent API calls."
            else:
                response = f"[Response to: {last_msg[:50]}]"

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
# SOLUTION 1: Few-Shot Sentiment Classifier
# ===========================================================
def classify_sentiment(review: str) -> str:
    prompt = f"""Classify the sentiment of a review as POSITIVE, NEGATIVE, or NEUTRAL.

Examples:
Review: "Absolutely amazing, best purchase ever!" → POSITIVE
Review: "Complete garbage, do not buy." → NEGATIVE
Review: "It works as described, nothing more." → NEUTRAL

Now classify:
Review: "{review}" →"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()


print("=" * 50)
print("Exercise 1: Few-Shot Sentiment Classifier")
print("=" * 50)
for review in [
    "Absolutely love this product! Works perfectly.",
    "Waste of money. Broke after one day.",
    "It's fine, does the job."
]:
    result = classify_sentiment(review)
    print(f"Review: {review[:40]}...")
    print(f"Sentiment: {result}\n")


# ===========================================================
# SOLUTION 2: Dynamic Prompt Builder
# ===========================================================
SAMPLE_TEXT = """
Python 3.12 was released in October 2023 with significant performance improvements.
The new version includes a 5% overall speedup, better error messages with more context,
and a new type parameter syntax for generics. The f-string parser was also rewritten
to support multi-line expressions and reuse of quotes. For developers building AI systems,
the improved asyncio performance is particularly valuable for handling concurrent API calls.
"""

def build_summary_prompt(text: str, num_points: int, focus: str) -> str:
    return f"""Summarize the following text in exactly {num_points} bullet points.
Focus specifically on: {focus}
Start each bullet point with "• "

Text:
{text.strip()}"""


print("=" * 50)
print("Exercise 2: Dynamic Prompt Builder")
print("=" * 50)
prompt = build_summary_prompt(SAMPLE_TEXT, num_points=3, focus="developer benefits")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)
print(response.choices[0].message.content)


# ===========================================================
# SOLUTION 3: Information Extractor with JSON Output
# ===========================================================
def extract_contact_info(text: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Extract contact information from text. Always respond with valid JSON only, no other text. Use null for missing fields. Schema: {name, email, company, role}"
            },
            {"role": "user", "content": text}
        ],
        temperature=0
    )
    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw": response.choices[0].message.content}


print("\n" + "=" * 50)
print("Exercise 3: Information Extractor")
print("=" * 50)
text = "Hi, I'm Alice Chen, a Senior Engineer at TechCorp. Reach me at alice@techcorp.com"
info = extract_contact_info(text)
print("Extracted info:")
for key, value in info.items():
    print(f"  {key}: {value}")


# ===========================================================
# SOLUTION 4: Chain of Thought Prompting
# ===========================================================
def solve_with_reasoning(problem: str) -> str:
    prompt = f"""Solve this problem step by step, then state the final answer clearly.

Problem: {problem}

Let's think step by step:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content


print("\n" + "=" * 50)
print("Exercise 4: Chain of Thought")
print("=" * 50)
problem = "A Python script processes 1000 API requests. Each takes 0.5s sequentially. How long does it take? What if we use 10 concurrent workers?"
print(solve_with_reasoning(problem))


# ===========================================================
# SOLUTION 5: Prompt Template System
# ===========================================================
TEMPLATES = {
    "translate": "Translate the following text to {language}. Output only the translation.\n\nText: {text}",
    "explain_code": "Explain this {language} code in simple terms for a beginner:\n\n```{language}\n{code}\n```\n\nExplanation:",
    "write_tests": "Write {num_tests} pytest unit tests for this Python function:\n\n```python\n{code}\n```\n\nTests:",
    "summarize": "Summarize the following in {max_words} words or fewer:\n\n{text}",
    "classify": "Classify the following {item_type} into one of these categories: {categories}\n\nItem: {item}\n\nCategory:"
}

def apply_template(name: str, **kwargs) -> str:
    if name not in TEMPLATES:
        raise ValueError(f"Unknown template: {name}. Available: {list(TEMPLATES.keys())}")
    return TEMPLATES[name].format(**kwargs)


print("\n" + "=" * 50)
print("Exercise 5: Template System")
print("=" * 50)

# Test translate template
prompt = apply_template("translate", language="French", text="Hello, how are you?")
print(f"Translate template:\n{prompt}\n")

# Test explain_code template
code_prompt = apply_template("explain_code", language="python",
                              code="result = [x**2 for x in range(10) if x % 2 == 0]")
print(f"Explain code template:\n{code_prompt}\n")

print("All templates:", list(TEMPLATES.keys()))
