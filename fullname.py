class Car:
    def __init__(self, brand, model, battery_size):
        self.brand = brand
        self.model = model
        self.battery_size = battery_size
    
    def full_name(self):
        return f"{self.brand}{self.model}"

my_car = Car("Tesala", "X", "300KW")
print(my_car.brand)
print(my_car.model)
print(my_car.battery_size)
print(my_car)
print(my_car.full_name())

#Ihertiance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size, color):
        super().__init__(brand, model, battery_size,)
        self.color = color
    def __str__(self):
        return f"{self.color} {self.brand} {self.model} ({self.battery_size})"
my_electric_car = ElectricCar("Tesala", "model X", "300kw", "Black")
print(my_electric_car.full_name())
print(my_electric_car.battery_size)
print(my_electric_car.model)
print(my_electric_car.brand)
print(my_electric_car)