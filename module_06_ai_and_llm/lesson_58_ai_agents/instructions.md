# Lesson 58: Building AI Agents — Autonomous Python Programs

An AI agent is a program that perceives its environment, decides what actions to take (using an LLM as its brain), executes those actions, and observes the results — in a loop until a goal is achieved.

This lesson teaches you to build agents from scratch in Python.

## The Agent Loop

```
User Goal → [LLM: What should I do?] → Tool Call → [Observe Result] → [LLM: Done or more steps?] → ...
```

```python
def agent_loop(goal: str, tools: dict, max_steps: int = 10):
    """Core agent loop."""
    messages = [
        {"role": "system", "content": AGENT_SYSTEM_PROMPT},
        {"role": "user", "content": goal}
    ]
    
    for step in range(max_steps):
        response = llm.complete(messages, tools=tools)
        
        if response.is_done:
            return response.final_answer
        
        # Execute the tool the LLM chose
        tool_result = tools[response.tool_name](**response.tool_args)
        
        # Feed result back to LLM
        messages.append({"role": "assistant", "content": response.reasoning})
        messages.append({"role": "tool", "content": str(tool_result)})
    
    return "Max steps reached without completing goal."
```

## Building Tools

Tools are just Python functions with clear documentation:

```python
import json
from datetime import datetime

def search_web(query: str) -> str:
    """Search the web for information. Use for current events or unknown facts."""
    # In production: call a search API
    return f"Search results for '{query}': [relevant article content...]"

def run_python(code: str) -> str:
    """Execute Python code and return the output. Use for calculations."""
    try:
        import io, contextlib
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(code, {})
        return output.getvalue() or "Code executed successfully (no output)"
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_file(filename: str, content: str) -> str:
    """Save content to a file."""
    with open(filename, "w") as f:
        f.write(content)
    return f"Saved {len(content)} characters to {filename}"
```

## Tool Registry Pattern

```python
class ToolRegistry:
    """Manages a collection of tools an agent can use."""
    
    def __init__(self):
        self._tools = {}
    
    def register(self, func):
        """Register a function as a tool (works as a decorator)."""
        self._tools[func.__name__] = func
        return func
    
    def execute(self, name: str, **kwargs) -> str:
        """Execute a tool by name."""
        if name not in self._tools:
            return f"Error: Unknown tool '{name}'. Available: {list(self._tools.keys())}"
        try:
            result = self._tools[name](**kwargs)
            return str(result)
        except Exception as e:
            return f"Error executing {name}: {type(e).__name__}: {e}"
    
    def get_descriptions(self) -> str:
        """Get tool descriptions for the system prompt."""
        descriptions = []
        for name, func in self._tools.items():
            doc = func.__doc__ or "No description"
            descriptions.append(f"- {name}: {doc.strip()}")
        return "\n".join(descriptions)


# Usage:
registry = ToolRegistry()

@registry.register
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression. Example: '2 + 2 * 10'"""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

@registry.register
def count_words(text: str) -> str:
    """Count the number of words in a text."""
    return str(len(text.split()))
```

## ReAct Pattern (Reasoning + Acting)

The ReAct pattern makes agents explain their reasoning before acting:

```python
REACT_SYSTEM_PROMPT = """You are a helpful AI agent. You work by:
1. THINKING: Reason step-by-step about what to do
2. ACTING: Call a tool with specific arguments
3. OBSERVING: Process the tool result
4. Repeat until you have the final answer.

Available tools:
{tools}

Response format:
THOUGHT: [your reasoning]
ACTION: tool_name
ARGS: {{"param1": "value1", "param2": "value2"}}
---
OR if you have the final answer:
FINAL ANSWER: [your answer]"""

def parse_react_response(response: str) -> dict:
    """Parse a ReAct-format response."""
    if "FINAL ANSWER:" in response:
        answer = response.split("FINAL ANSWER:")[1].strip()
        return {"type": "answer", "content": answer}
    
    thought = ""
    action = ""
    args = {}
    
    for line in response.split("\n"):
        if line.startswith("THOUGHT:"):
            thought = line.replace("THOUGHT:", "").strip()
        elif line.startswith("ACTION:"):
            action = line.replace("ACTION:", "").strip()
        elif line.startswith("ARGS:"):
            try:
                args = json.loads(line.replace("ARGS:", "").strip())
            except json.JSONDecodeError:
                args = {}
    
    return {"type": "action", "thought": thought, "action": action, "args": args}
```

## Complete Simple Agent

```python
class SimpleAgent:
    """A simple LLM-powered agent with tools."""
    
    def __init__(self, llm, tools: ToolRegistry):
        self.llm = llm
        self.tools = tools
        self.max_steps = 10
    
    def run(self, goal: str) -> str:
        """Run the agent to achieve a goal."""
        print(f"\n🤖 Agent Goal: {goal}")
        print("=" * 50)
        
        system_prompt = REACT_SYSTEM_PROMPT.format(
            tools=self.tools.get_descriptions()
        )
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": goal}
        ]
        
        for step in range(self.max_steps):
            print(f"\n[Step {step + 1}]")
            
            # Ask LLM what to do
            response = self.llm.complete(messages)
            print(response)
            
            # Parse the response
            parsed = parse_react_response(response)
            
            if parsed["type"] == "answer":
                print(f"\n✅ Final Answer: {parsed['content']}")
                return parsed["content"]
            
            # Execute the tool
            tool_result = self.tools.execute(parsed["action"], **parsed["args"])
            print(f"Tool Result: {tool_result}")
            
            # Add to conversation history
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": f"Tool result: {tool_result}"})
        
        return "Goal not achieved within step limit."
```

## When to Use Agents

| Use Case | Agent? |
|----------|--------|
| Simple Q&A | ❌ Just use chat completion |
| Multi-step research | ✅ Agent with search tools |
| Data analysis pipeline | ✅ Agent with code execution |
| Form filling / extraction | ❌ Structured prompting |
| Autonomous coding assistant | ✅ Agent with file tools |

## Safety Considerations

1. **Sandbox code execution** — never run agent-generated code on your main system
2. **Rate limit tool calls** — prevent infinite loops costing money
3. **Validate tool inputs** — agents can pass unexpected arguments
4. **Log everything** — always record what tools were called with what args
5. **Human-in-the-loop** — for high-stakes actions, require human approval

---

### Quiz

1. **What is the core loop of an AI agent?**
2. **What is the ReAct pattern?**
3. **Why should you sandbox code execution in agents?**

<details>
  <summary><b>Answer Key</b></summary>
  1. Perceive goal → LLM decides action → Execute tool → Observe result → Repeat until done
  2. ReAct = Reasoning + Acting. The agent first writes its THOUGHT (reasoning), then specifies an ACTION and ARGS. This makes agent behavior transparent and debuggable.
  3. An LLM might generate malicious or buggy code that could delete files, exfiltrate data, or crash systems. Sandboxing limits what the code can do.
</details>
