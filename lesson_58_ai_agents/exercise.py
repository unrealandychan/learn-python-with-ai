"""
Lesson 58: Building AI Agents — Exercise File

Build a working (simulated) AI agent with a tool registry.
No API key required — uses a mock LLM that follows the ReAct pattern.
"""

import json
import io
import contextlib
import math
from datetime import datetime


# ============================================================
# MOCK LLM — Simulates an LLM that follows ReAct pattern
# ============================================================

class MockReActLLM:
    """Simulates an LLM that reasons and acts using ReAct format."""
    
    def __init__(self):
        self.step_count = {}
    
    def complete(self, messages: list, session_id: str = "default") -> str:
        """Generate next ReAct step based on conversation history."""
        self.step_count[session_id] = self.step_count.get(session_id, 0) + 1
        step = self.step_count[session_id]
        
        # Extract the original goal
        goal = next((m["content"] for m in messages if m["role"] == "user"), "")
        
        # Check if there are tool results in history
        tool_results = [m["content"] for m in messages if m.get("role") == "user" and "Tool result:" in m.get("content", "")]
        
        # Simple decision logic based on goal keywords
        if "calculate" in goal.lower() or "math" in goal.lower() or "=" in goal:
            if step == 1:
                return """THOUGHT: I need to calculate a mathematical expression.
ACTION: calculate
ARGS: {"expression": "2 ** 10 + 15 * 3"}"""
            else:
                result = tool_results[-1].replace("Tool result: ", "") if tool_results else "1069"
                return f"FINAL ANSWER: The calculation result is {result}"
        
        elif "time" in goal.lower() or "date" in goal.lower():
            if step == 1:
                return """THOUGHT: I need to get the current time.
ACTION: get_time
ARGS: {}"""
            else:
                result = tool_results[-1].replace("Tool result: ", "") if tool_results else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return f"FINAL ANSWER: The current date and time is {result}"
        
        elif "word" in goal.lower() or "count" in goal.lower():
            if step == 1:
                return """THOUGHT: I need to count words in the text provided.
ACTION: count_words
ARGS: {"text": "The quick brown fox jumps over the lazy dog"}"""
            elif step == 2:
                return """THOUGHT: Now I'll check if any words are longer than 4 characters.
ACTION: filter_long_words
ARGS: {"text": "The quick brown fox jumps over the lazy dog", "min_length": 4}"""
            else:
                return "FINAL ANSWER: The sentence 'The quick brown fox jumps over the lazy dog' has 9 words."
        
        elif "save" in goal.lower() or "file" in goal.lower() or "write" in goal.lower():
            if step == 1:
                return """THOUGHT: I need to save a report to a file.
ACTION: save_to_file
ARGS: {"filename": "agent_report.txt", "content": "# Agent Report\\n\\nThis report was created by an AI agent.\\nDate: 2024-01-01\\n"}"""
            else:
                return "FINAL ANSWER: Successfully saved the report to 'agent_report.txt'."
        
        else:
            # Multi-step: first calculate, then get time, then finish
            if step == 1:
                return """THOUGHT: Let me start by computing the square root of 144.
ACTION: calculate
ARGS: {"expression": "math.sqrt(144)"}"""
            elif step == 2:
                return """THOUGHT: Now let me get the current time for the report.
ACTION: get_time
ARGS: {}"""
            elif step == 3:
                calc_result = "12.0"
                time_result = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return f"FINAL ANSWER: The square root of 144 is 12. Retrieved at {time_result}."
            else:
                return "FINAL ANSWER: Task completed successfully."


# ============================================================
# EXERCISE 1: Build the Tool Registry
# ============================================================
# TODO: Implement the ToolRegistry class with:
# - register(func): decorator to register a function as a tool
# - execute(name, **kwargs): execute a tool by name, return string result
# - list_tools(): return list of registered tool names
# - get_descriptions(): return formatted string of tool names + docstrings

print("=" * 50)
print("Exercise 1: Tool Registry")
print("=" * 50)

class ToolRegistry:
    """Registry for agent tools."""
    
    def __init__(self):
        self._tools = {}
    
    def register(self, func):
        """Register a function as a tool."""
        # YOUR CODE HERE
        pass
    
    def execute(self, name: str, **kwargs) -> str:
        """Execute a named tool with keyword arguments."""
        # YOUR CODE HERE
        # Handle unknown tool names gracefully
        # Handle exceptions gracefully
        pass
    
    def list_tools(self) -> list:
        """Return list of registered tool names."""
        # YOUR CODE HERE
        pass
    
    def get_descriptions(self) -> str:
        """Return formatted descriptions of all tools."""
        # YOUR CODE HERE
        pass


# ===========================================================
# EXERCISE 2: Register These Tools
# ===========================================================
# TODO: Create a ToolRegistry instance and register these 4 tools using
# the @registry.register decorator:

registry = ToolRegistry()

# Tool 1: calculate(expression: str) -> str
# Safely evaluate a math expression using eval with limited globals
# Include math functions: allow {"sqrt": math.sqrt, "pi": math.pi, etc.}
# Return the result as string, or error message if it fails

# Tool 2: count_words(text: str) -> str
# Count the number of words in text
# Return as a string like "9 words"

# Tool 3: get_time() -> str
# Return the current date and time as a formatted string

# Tool 4: save_to_file(filename: str, content: str) -> str
# Save content to a file, return success message

# Tool 5 (BONUS): filter_long_words(text: str, min_length: int) -> str
# Return words from text that are >= min_length characters, comma-separated

# YOUR CODE HERE:


# Test the registry:
print(f"Registered tools: {registry.list_tools()}")
print(f"\nTool descriptions:\n{registry.get_descriptions()}")

# Test execute:
print(f"\nTest calculate: {registry.execute('calculate', expression='2**10')}")
print(f"Test count_words: {registry.execute('count_words', text='Hello world from Python')}")
print(f"Test get_time: {registry.execute('get_time')}")


# ===========================================================
# EXERCISE 3: Parse ReAct Responses
# ===========================================================
# TODO: Implement parse_react_response(response: str) -> dict
# 
# For a FINAL ANSWER response, return:
#   {"type": "answer", "content": "the answer text"}
#
# For an action response, return:
#   {"type": "action", "thought": "...", "action": "tool_name", "args": {...}}
#
# ARGS line contains a JSON string — parse it with json.loads()
# Handle malformed JSON gracefully (return {} for args)

def parse_react_response(response: str) -> dict:
    """Parse a ReAct format response into a structured dict."""
    # YOUR CODE HERE
    pass


print("\n" + "=" * 50)
print("Exercise 3: Parse ReAct Responses")
print("=" * 50)

sample_action = """THOUGHT: I need to calculate 2 to the power of 10.
ACTION: calculate
ARGS: {"expression": "2 ** 10"}"""

sample_answer = "FINAL ANSWER: The result is 1024."

action_parsed = parse_react_response(sample_action)
answer_parsed = parse_react_response(sample_answer)

print(f"Action parsed: {action_parsed}")
print(f"Answer parsed: {answer_parsed}")


# ===========================================================
# EXERCISE 4: The Agent Loop
# ===========================================================
# TODO: Implement the run_agent(goal, llm, registry, max_steps) function.
# 
# It should:
# 1. Print the goal
# 2. Set up an initial messages list with system + user messages
# 3. Loop up to max_steps:
#    a. Get LLM response (llm.complete(messages))
#    b. Parse it with parse_react_response()
#    c. If type == "answer": print it and return it
#    d. If type == "action": 
#       - Print the thought and action
#       - Execute the tool
#       - Print the result
#       - Add assistant message + tool result to messages
# 4. If max_steps reached, return an error message

SYSTEM_PROMPT = """You are a helpful AI agent. Use the ReAct pattern.
Available tools:
{tools}

Response format:
THOUGHT: [reasoning]
ACTION: tool_name
ARGS: {{"key": "value"}}

Or for final answer:
FINAL ANSWER: [answer]"""

def run_agent(goal: str, llm, registry: ToolRegistry, max_steps: int = 10) -> str:
    """Run an AI agent to achieve the given goal."""
    # YOUR CODE HERE
    pass


print("\n" + "=" * 50)
print("Exercise 4: Agent Loop")
print("=" * 50)

if registry.list_tools():
    llm = MockReActLLM()
    
    # Test 1: Math calculation
    result = run_agent(
        goal="Calculate 2 to the power of 10, plus 15 times 3",
        llm=llm,
        registry=registry
    )
    
    print("\n" + "-" * 30)
    
    # Test 2: Multi-step task
    result = run_agent(
        goal="Get the current time and compute square root",
        llm=llm,
        registry=registry
    )
