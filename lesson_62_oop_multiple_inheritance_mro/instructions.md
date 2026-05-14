# Lesson 62: Multiple Inheritance & MRO

## Multiple Inheritance

Python allows inheriting from multiple parents:

```python
class D(B, C):
    pass
```

## Method Resolution Order (MRO)

Python uses **C3 Linearization** to determine which method to call:

```python
print(D.__mro__)
# (D, B, C, A, object)
```

**The diamond problem** — `A` is called exactly once:
```
    A
   / \
  B   C
   \ /
    D
```

```python
class A:
    def greet(self): print("A"); 

class B(A):
    def greet(self): print("B"); super().greet()

class C(A):
    def greet(self): print("C"); super().greet()

class D(B, C):
    def greet(self): print("D"); super().greet()

D().greet()  # D → B → C → A
```

## Mixins

Mixins are narrow-purpose classes that add behaviour via multiple inheritance:

```python
class LogMixin:
    def log(self, msg: str) -> None:
        print(f"[{self.__class__.__name__}] {msg}")

class JSONMixin:
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__)

class User(LogMixin, JSONMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

## Exercise

1. `Serializable` mixin — `to_dict() -> dict`
2. `Validatable` mixin — `validate()` raises `NotImplementedError`
3. `TimestampMixin` — adds `created_at` in `__init__`
4. `Product(TimestampMixin, Serializable, Validatable)` — `name`, `price`, `validate()` checks `price > 0`
5. Print `Product.__mro__`
