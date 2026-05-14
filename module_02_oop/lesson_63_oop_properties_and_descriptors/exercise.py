# Lesson 63: Exercise — @property

# TODO: Temperature class
#   __init__(self, celsius: float) — use the setter (self.celsius = celsius)
#
#   @property celsius → _celsius
#   @celsius.setter → validates >= -273.15
#
#   @property fahrenheit → celsius * 9/5 + 32
#   @fahrenheit.setter → convert F to C, store via celsius setter
#
#   @property kelvin → celsius + 273.15 (no setter)

# t = Temperature(100)
# print(t.celsius)     # 100
# print(t.fahrenheit)  # 212.0
# print(t.kelvin)      # 373.15
# t.fahrenheit = 32
# print(t.celsius)     # 0.0
# t.celsius = -300     # ValueError
