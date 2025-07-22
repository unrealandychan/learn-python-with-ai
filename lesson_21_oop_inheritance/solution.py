
# Lesson 21: Solution

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.number_of_doors}")

class ElectricCar(Car):
    def __init__(self, make, model, number_of_doors, battery_capacity):
        super().__init__(make, model, number_of_doors)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery: {self.battery_capacity} kWh")

my_car = Car("Toyota", "Camry", 4)
my_electric_car = ElectricCar("Tesla", "Model S", 4, 100)

my_car.display_info()
print("---")
my_electric_car.display_info()
