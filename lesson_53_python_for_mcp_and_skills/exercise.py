# Lesson 53: Python for MCP and Skills - Exercise

from typing import Any


def skill_add(params: dict[str, Any]) -> int:
    """Return a + b from params = {"a": int, "b": int}."""
    # TODO: Read a and b from params and return their sum.
    raise NotImplementedError("Implement skill_add")


def skill_word_count(params: dict[str, Any]) -> int:
    """Return the number of words in params["text"]."""
    # TODO: Read text from params and return the number of words.
    # Tip: text.split() gives a list of words.
    raise NotImplementedError("Implement skill_word_count")


TOOLS: dict[str, Any] = {
    "tool.add": skill_add,
    "tool.word_count": skill_word_count,
}


def handle_request(request: dict[str, Any]) -> dict[str, Any]:
    """
    Handle a simplified MCP-like request.

    Request shape:
    {
      "id": "req-1",
      "method": "tool.add",
      "params": {"a": 2, "b": 3}
    }
    """
    request_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    # TODO: Return an error if method is missing from TOOLS.
    # Example:
    # return {"id": request_id, "ok": False, "error": f"Unknown method: {method}"}

    # TODO: Call the matched tool and return success response:
    # {"id": request_id, "ok": True, "result": result}

    # TODO: Wrap execution in try/except and return structured errors.
    raise NotImplementedError("Implement handle_request")


def run_demo() -> None:
    requests = [
        {"id": "req-1", "method": "tool.add", "params": {"a": 10, "b": 5}},
        {
            "id": "req-2",
            "method": "tool.word_count",
            "params": {"text": "MCP tools make AI workflows practical"},
        },
        {"id": "req-3", "method": "tool.missing", "params": {}},
    ]

    for request in requests:
        response = handle_request(request)
        print(response)


if __name__ == "__main__":
    run_demo()
