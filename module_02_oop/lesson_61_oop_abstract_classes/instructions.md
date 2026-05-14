# Lesson 61: Abstract Classes & ABCs

An **abstract class** cannot be instantiated directly — it defines a contract that subclasses must fulfil.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self) -> str:
        return f"Shape with area {self.area():.2f}"
```

- `Shape()` → TypeError (cannot instantiate)
- Any subclass MUST implement `area()` and `perimeter()`

## Abstract Properties

```python
class Animal(ABC):
    @property
    @abstractmethod
    def sound(self) -> str:
        pass

class Dog(Animal):
    @property
    def sound(self) -> str:
        return "Woof"
```

## Real-World Use: LLM Provider Interface

```python
class LLMProvider(ABC):
    @abstractmethod
    def complete(self, prompt: str) -> str:
        pass

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        pass

    def complete_with_log(self, prompt: str) -> str:
        result = self.complete(prompt)
        print(f"Tokens: {self.count_tokens(prompt)}")
        return result
```

All providers (OpenAI, Gemini, Anthropic) must implement `complete()` and `count_tokens()`.

## Exercise

Create `LLMProvider` ABC with:
- `complete(prompt: str) -> str` (abstract)
- `count_tokens(text: str) -> int` (abstract)
- `complete_with_log(prompt: str) -> str` (concrete — calls complete + prints tokens)

Implement `MockOpenAI` and `MockGemini`.
Verify `LLMProvider()` raises `TypeError`.
