# Lesson 53: Solution

from typing import Any, Callable


def skill_add(params: dict[str, Any]) -> int:
    a = int(params["a"])
    b = int(params["b"])
    return a + b


def skill_word_count(params: dict[str, Any]) -> int:
    text = str(params.get("text", "")).strip()
    if not text:
        return 0
    return len(text.split())


TOOLS: dict[str, Callable[[dict[str, Any]], Any]] = {
    "tool.add": skill_add,
    "tool.word_count": skill_word_count,
}


def handle_request(request: dict[str, Any]) -> dict[str, Any]:
    request_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method not in TOOLS:
        return {
            "id": request_id,
            "ok": False,
            "error": f"Unknown method: {method}",
        }

    tool = TOOLS[method]
    try:
        result = tool(params)
        return {"id": request_id, "ok": True, "result": result}
    except Exception as exc:
        return {
            "id": request_id,
            "ok": False,
            "error": f"Tool execution failed: {exc}",
        }


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
