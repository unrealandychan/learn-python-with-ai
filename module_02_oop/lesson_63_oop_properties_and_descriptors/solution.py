# Lesson 63: Solution


class Temperature:
    def __init__(self, celsius: float = 0.0):
        self.celsius = celsius  # Triggers setter validation

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError(f"{value}°C is below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self.celsius = (value - 32) * 5 / 9  # Delegate to celsius setter

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15


t = Temperature(100)
print(t.celsius)      # 100
print(t.fahrenheit)   # 212.0
print(t.kelvin)       # 373.15
t.fahrenheit = 32
print(t.celsius)      # 0.0
try:
    t.celsius = -300
except ValueError as e:
    print(f"Error: {e}")
