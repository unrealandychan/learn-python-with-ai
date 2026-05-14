# Lesson 62: Exercise — Multiple Inheritance & MRO
from datetime import datetime

# TODO: Serializable mixin — to_dict() returns self.__dict__.copy()

# TODO: Validatable mixin — validate() raises NotImplementedError

# TODO: TimestampMixin — adds self.created_at in __init__ via super().__init__()

# TODO: Product(TimestampMixin, Serializable, Validatable)
#   __init__(self, name: str, price: float)
#   validate() — raise ValueError if price <= 0

# p = Product("Widget", 9.99)
# p.validate()
# print(p.to_dict())
# print([c.__name__ for c in Product.__mro__])
