# Lesson 53: Python for MCP and Skills

As AI-assisted development grows, two concepts appear frequently:

1.  **MCP (Model Context Protocol):** A standard way for an AI model to call tools and exchange structured messages.
2.  **Skills:** Reusable capabilities (small, focused units of behavior) that solve specific tasks.

In this lesson, you will build a small Python program that mimics an MCP-style tool router and uses skill functions to complete requests.

## Learning Goals

By the end of this lesson, you will be able to:

*   Model a request/response format similar to MCP messages.
*   Register Python functions as tools.
*   Dispatch requests by method name.
*   Return structured success and error responses.
*   Separate reusable business logic into skills.

## MCP-Like Message Shape

For this lesson, we use a simplified request format:

```json
{
  "id": "req-1",
  "method": "tool.add",
  "params": {"a": 2, "b": 3}
}
```

And a response format:

```json
{
  "id": "req-1",
  "ok": true,
  "result": 5
}
```

If something fails:

```json
{
  "id": "req-1",
  "ok": false,
  "error": "Unknown method: tool.multiply"
}
```

## Skills in Python

A skill can simply be a function with a focused purpose. Examples:

*   `add_numbers(a, b)`
*   `word_count(text)`
*   `summarize_title(text)`

These skills become tools when they are exposed through a method registry.

## Core Pattern

1.  Build tool functions (skills).
2.  Register them in a dictionary (`method_name -> function`).
3.  Parse incoming request dictionaries.
4.  Validate method and params.
5.  Execute safely and return structured responses.

## Why This Matters

This pattern is the foundation for:

*   Local agent tools.
*   Plugin/tool-calling systems.
*   MCP-compatible server design.
*   Clean separation between orchestration logic and capability logic.

## Next Steps

After this lesson, you can extend your router by adding:

*   Type validation for parameters.
*   Async tool support with `async def`.
*   Logging and tracing.
*   Tool metadata (`description`, `input_schema`).
*   Network transport (HTTP, stdio, websockets).
