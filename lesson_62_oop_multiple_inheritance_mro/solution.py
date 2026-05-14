# Lesson 62: Solution
from datetime import datetime


class Serializable:
    def to_dict(self) -> dict:
        return self.__dict__.copy()


class Validatable:
    def validate(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement validate()")


class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now().isoformat()


class Product(TimestampMixin, Serializable, Validatable):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        super().__init__()

    def validate(self):
        if self.price <= 0:
            raise ValueError(f"Price must be positive, got {self.price}")


p = Product("Widget", 9.99)
p.validate()
print(p.to_dict())
print([c.__name__ for c in Product.__mro__])

try:
    bad = Product("Free", -1.0)
    bad.validate()
except ValueError as e:
    print(f"Validation error: {e}")
