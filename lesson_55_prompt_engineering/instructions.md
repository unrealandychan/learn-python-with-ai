# Lesson 55: Prompt Engineering in Code

Prompt engineering is the art of crafting instructions that get the best results from LLMs. As a Python developer, you'll write prompts programmatically — constructing them dynamically based on data, user input, and context.

## Why This Matters for Developers

Unlike using ChatGPT manually, in code you need to:
- Build prompts dynamically from variables and data
- Test prompt variations systematically
- Structure outputs reliably for downstream processing
- Handle edge cases and failure modes

## Core Techniques

### 1. Zero-Shot Prompting

Ask the model to do something without examples:

```python
prompt = "Classify the sentiment of this review as POSITIVE, NEGATIVE, or NEUTRAL:\n\n'The product arrived on time but the quality was disappointing.'"
```

### 2. Few-Shot Prompting

Give 2-5 examples to teach the model the format you want:

```python
def build_sentiment_prompt(review: str) -> str:
    return f"""Classify sentiment as POSITIVE, NEGATIVE, or NEUTRAL.

Examples:
Review: "Amazing product, works perfectly!" → POSITIVE
Review: "Terrible experience, broken on arrival." → NEGATIVE  
Review: "It's okay, nothing special." → NEUTRAL

Now classify:
Review: "{review}" →"""
```

### 3. Chain of Thought (CoT)

Ask the model to reason step-by-step before answering:

```python
def build_cot_prompt(problem: str) -> str:
    return f"""Solve this problem step by step, then give the final answer.

Problem: {problem}

Let's think through this step by step:"""
```

### 4. System Prompt Templates

Store system prompts as reusable templates:

```python
SYSTEM_PROMPTS = {
    "analyst": """You are a senior data analyst. 
You provide concise, data-driven insights.
Always cite specific numbers when available.
Format your responses with clear headings.""",
    
    "tutor": """You are a patient Python tutor for beginners.
Use simple language and relatable analogies.
Always include a short code example.
Never make the student feel dumb.""",
    
    "extractor": """You are an information extraction system.
Always respond with valid JSON.
If information is not present, use null for that field.
Do not add commentary outside the JSON."""
}
```

### 5. Dynamic Prompt Construction

Build prompts from data:

```python
def build_analysis_prompt(data: dict) -> str:
    lines = []
    for key, value in data.items():
        lines.append(f"- {key}: {value}")
    data_str = "\n".join(lines)
    
    return f"""Analyze the following metrics and identify the top 3 insights:

{data_str}

Provide your analysis as a numbered list."""
```

### 6. Prompt Templates with f-strings

```python
CLASSIFY_TEMPLATE = """
Task: {task}
Categories: {categories}
Input: {input_text}

Respond with only the category name, nothing else.
""".strip()

def classify(task, categories, input_text):
    return CLASSIFY_TEMPLATE.format(
        task=task,
        categories=", ".join(categories),
        input_text=input_text
    )

# Usage:
prompt = classify(
    task="Classify the programming language",
    categories=["Python", "JavaScript", "Java", "Other"],
    input_text="def fibonacci(n): return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)"
)
```

### 7. Output Formatting Instructions

Always specify exactly how you want the output formatted:

```python
# Vague (bad):
"Summarize this article."

# Specific (good):
"""Summarize this article in exactly 3 bullet points.
Each bullet point should be one sentence.
Focus on the most important information.
Start each bullet with "• "."""
```

### 8. Handling Uncertainty

Tell the model what to do when it doesn't know:

```python
SAFE_ANSWER_SYSTEM = """Answer questions accurately and concisely.
If you are not sure about something, say "I'm not certain, but..." 
If the question is outside your knowledge, say "I don't have information about that."
Never make up facts or statistics."""
```

## Prompt Testing Pattern

Test prompts systematically:

```python
def test_prompt(client, prompt_builder, test_cases: list[dict]) -> list[dict]:
    """
    Test a prompt function against multiple test cases.
    
    Args:
        client: OpenAI client
        prompt_builder: Function that takes test case dict and returns prompt string
        test_cases: List of {'input': ..., 'expected': ...} dicts
    
    Returns:
        List of results with pass/fail
    """
    results = []
    for case in test_cases:
        prompt = prompt_builder(case["input"])
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0  # deterministic for testing
        )
        output = response.choices[0].message.content.strip()
        passed = case["expected"].lower() in output.lower()
        results.append({
            "input": case["input"],
            "expected": case["expected"],
            "got": output,
            "passed": passed
        })
    return results
```

## Temperature Guide

| Temperature | Use Case | Behavior |
|-------------|----------|----------|
| 0.0 | Classification, extraction | Deterministic, consistent |
| 0.3 | Analysis, summarization | Mostly consistent with minor variation |
| 0.7 | General chat, explanation | Balanced |
| 1.0 | Creative writing | More varied |
| 1.5+ | Brainstorming | Very creative, less reliable |

## Common Mistakes

❌ **Too vague**: `"Analyze this"`  
✅ **Specific**: `"List 3 strengths and 3 weaknesses of this business plan"`

❌ **No output format**: `"Extract the data"`  
✅ **Format specified**: `"Extract as JSON: {'name': str, 'date': str, 'amount': float}"`

❌ **No examples for edge cases**: The model will guess  
✅ **Handle edge cases**: `"If no date is mentioned, use null for the date field"`

---

### Quiz

1. **What is few-shot prompting and when should you use it?**
2. **Why set `temperature=0` when testing prompts?**
3. **Why is specifying output format important in code?**

<details>
  <summary><b>Answer Key</b></summary>
  1. Few-shot prompting provides 2-5 examples in the prompt to show the model the exact format/style you want. Use it when zero-shot gives inconsistent results.
  2. temperature=0 makes the model deterministic (same input → same output), which is needed for reproducible tests.
  3. Your code needs to reliably parse the response. If format is unspecified, the model may respond in many different ways, breaking your parsing logic.
</details>
