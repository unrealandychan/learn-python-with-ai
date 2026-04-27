"""
Lesson 58: Building AI Agents — Solutions
"""

import json
import math
from datetime import datetime


# ---- Mock LLM (same as exercise) ----
class MockReActLLM:
    def __init__(self):
        self.step_count = {}
    
    def complete(self, messages: list, session_id: str = "default") -> str:
        self.step_count[session_id] = self.step_count.get(session_id, 0) + 1
        step = self.step_count[session_id]
        goal = next((m["content"] for m in messages if m["role"] == "user"), "")
        tool_results = [m["content"] for m in messages if m.get("role") == "user" and "Tool result:" in m.get("content", "")]
        
        if "calculate" in goal.lower() or "math" in goal.lower():
            if step == 1:
                return """THOUGHT: I need to calculate the expression.\nACTION: calculate\nARGS: {"expression": "2 ** 10 + 15 * 3"}"""
            return f"FINAL ANSWER: The result is {tool_results[-1].replace('Tool result: ', '') if tool_results else '1069'}"
        elif "time" in goal.lower() or "square root" in goal.lower():
            if step == 1:
                return """THOUGHT: Let me compute the square root first.\nACTION: calculate\nARGS: {"expression": "math.sqrt(144)"}"""
            elif step == 2:
                return """THOUGHT: Now get the time.\nACTION: get_time\nARGS: {}"""
            return f"FINAL ANSWER: sqrt(144)=12, retrieved at {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        return "FINAL ANSWER: Task complete."


# ===========================================================
# SOLUTION 1 & 2: Tool Registry with Tools
# ===========================================================
class ToolRegistry:
    def __init__(self):
        self._tools = {}
    
    def register(self, func):
        self._tools[func.__name__] = func
        return func
    
    def execute(self, name: str, **kwargs) -> str:
        if name not in self._tools:
            return f"Error: Unknown tool '{name}'. Available: {list(self._tools.keys())}"
        try:
            result = self._tools[name](**kwargs)
            return str(result)
        except Exception as e:
            return f"Error in {name}: {type(e).__name__}: {e}"
    
    def list_tools(self) -> list:
        return list(self._tools.keys())
    
    def get_descriptions(self) -> str:
        lines = []
        for name, func in self._tools.items():
            doc = (func.__doc__ or "No description").strip().split("\n")[0]
            lines.append(f"- {name}: {doc}")
        return "\n".join(lines)


registry = ToolRegistry()


@registry.register
def calculate(expression: str) -> str:
    """Safely evaluate a mathematical expression."""
    safe_globals = {
        "__builtins__": {},
        "math": math,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "abs": abs,
        "round": round,
    }
    try:
        result = eval(expression, safe_globals)
        return str(result)
    except Exception as e:
        return f"Math error: {e}"


@registry.register
def count_words(text: str) -> str:
    """Count the number of words in text."""
    count = len(text.split())
    return f"{count} words"


@registry.register
def get_time() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@registry.register
def save_to_file(filename: str, content: str) -> str:
    """Save content to a file."""
    with open(filename, "w") as f:
        f.write(content)
    return f"Saved {len(content)} characters to '{filename}'"


@registry.register
def filter_long_words(text: str, min_length: int = 5) -> str:
    """Return words from text that are at least min_length characters long."""
    words = [w for w in text.split() if len(w) >= min_length]
    return ", ".join(words) if words else "No words found"


print("=" * 50)
print("Tool Registry")
print("=" * 50)
print(f"Registered tools: {registry.list_tools()}")
print(f"\nDescriptions:\n{registry.get_descriptions()}")
print(f"\nTest calculate: {registry.execute('calculate', expression='2**10')}")
print(f"Test count_words: {registry.execute('count_words', text='Hello world from Python')}")
print(f"Test get_time: {registry.execute('get_time')}")


# ===========================================================
# SOLUTION 3: Parse ReAct Responses
# ===========================================================
def parse_react_response(response: str) -> dict:
    if "FINAL ANSWER:" in response:
        content = response.split("FINAL ANSWER:")[1].strip()
        return {"type": "answer", "content": content}
    
    thought = ""
    action = ""
    args = {}
    
    for line in response.strip().split("\n"):
        if line.startswith("THOUGHT:"):
            thought = line[len("THOUGHT:"):].strip()
        elif line.startswith("ACTION:"):
            action = line[len("ACTION:"):].strip()
        elif line.startswith("ARGS:"):
            args_str = line[len("ARGS:"):].strip()
            try:
                args = json.loads(args_str)
            except json.JSONDecodeError:
                args = {}
    
    return {"type": "action", "thought": thought, "action": action, "args": args}


print("\n" + "=" * 50)
print("ReAct Parser")
print("=" * 50)
sample = """THOUGHT: I need to calculate 2 to the power of 10.
ACTION: calculate
ARGS: {"expression": "2 ** 10"}"""
print(f"Action: {parse_react_response(sample)}")
print(f"Answer: {parse_react_response('FINAL ANSWER: The result is 1024.')}")


# ===========================================================
# SOLUTION 4: Agent Loop
# ===========================================================
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
    print(f"\n🤖 Goal: {goal}")
    print("=" * 50)
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT.format(tools=registry.get_descriptions())},
        {"role": "user", "content": goal}
    ]
    
    for step in range(1, max_steps + 1):
        print(f"\n[Step {step}]")
        response = llm.complete(messages)
        parsed = parse_react_response(response)
        
        if parsed["type"] == "answer":
            print(f"✅ {parsed['content']}")
            return parsed["content"]
        
        print(f"💭 Thought: {parsed['thought']}")
        print(f"🔧 Action: {parsed['action']}({parsed['args']})")
        
        tool_result = registry.execute(parsed["action"], **parsed["args"])
        print(f"📊 Result: {tool_result}")
        
        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": f"Tool result: {tool_result}"})
    
    return "❌ Max steps reached without completing goal."


print("\n" + "=" * 50)
print("Agent in Action")
print("=" * 50)

llm = MockReActLLM()
run_agent("Calculate 2 to the power of 10, plus 15 times 3", llm, registry)
print("\n" + "-" * 30)
run_agent("Get the current time and compute square root", llm, registry)
