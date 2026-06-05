class Car:
    def __init__(self, brand, model, battery_size):
        self.brand = brand
        self.model = model
        self.battery_size = battery_size
    
    def get__brand(self):
        return self.__brand
    def set__brand(self, brand):
        self.__brand = brand
my_car = Car("Tesla", "X", "300KW")
print(my_car.brand)  #accessing the private attribute using getter
print(my_car.model)
print(my_car.battery_size)
my_car.set__brand("Toyota")
print(my_car.get__brand())


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

