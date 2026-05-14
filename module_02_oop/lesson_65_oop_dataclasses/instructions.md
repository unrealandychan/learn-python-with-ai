# Lesson 65: Dataclasses

`@dataclass` auto-generates boilerplate OOP code (`__init__`, `__repr__`, `__eq__`).

## Without @dataclass

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

## With @dataclass

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

Same behaviour — 3 lines instead of 12.

## Key Options

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)   # Immutable (hashable)
class Config:
    host: str = "localhost"
    port: int = 8080

@dataclass(order=True)    # Adds __lt__, __le__, __gt__, __ge__
class Score:
    value: int
    player: str = field(compare=False)  # Exclude from ordering
```

## Mutable Default Values

```python
# WRONG — raises TypeError
@dataclass
class Team:
    members: list = []

# CORRECT
@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)
```

## Post-Init Validation with __post_init__

```python
@dataclass
class Circle:
    radius: float

    def __post_init__(self):
        if self.radius < 0:
            raise ValueError(f"Radius cannot be negative: {self.radius}")
```

## Exercise

Create a dataclass-based AI message model:

1. `@dataclass(frozen=True) Role` with `value: str` and class constants `SYSTEM`, `USER`, `ASSISTANT`
2. `@dataclass Message` with `role: Role`, `content: str`, auto `timestamp` via `field(default_factory=...)`
3. `@dataclass ConversationWindow` — `max_tokens: int = 512`, `messages: list` (default empty), method `add(msg)` that trims oldest non-system messages when over token budget
