# Lesson 63: @property — Pythonic Getters & Setters

`@property` turns a method into a read-only attribute. Add `@x.setter` for write access.

```python
class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius ** 2  # Computed on access
```

## Why @property over Getters/Setters?

| Java | Python |
|---|---|
| `obj.setRadius(5)` | `obj.radius = 5` |
| `obj.getRadius()` | `obj.radius` |

Clean API + validation/computation power.

## @property.deleter

```python
@name.deleter
def name(self):
    del self._name
```

## Exercise

`Temperature` class:
- Stores internally as Celsius (`_celsius`)
- `celsius` property with validation (>= -273.15)
- `fahrenheit` property — computed; setter converts to Celsius
- `kelvin` property — read-only (celsius + 273.15)
