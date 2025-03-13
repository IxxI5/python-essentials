# import the classes Car, Truck, and ElectricCar
from car import Car
from truck import Truck
from electric_car import ElectricCar

# Create instances of each class
my_car = Car("Toyota", "Corolla", 2015, 4)
my_truck = Truck("Ford", "F-150", 2010, 2.5)
my_electric_car = ElectricCar("Tesla", "Model S", 2020, 4, 75)


# Demonstrate inheritance and polymorphism
print("My car:")
my_car.describe_vehicle()
my_car.lock_doors()

# Output:
# My car:
# This vehicle is a 2015 Toyota Corolla with 0 miles.
# Doors locked.

print("\nMy truck:")
my_truck.describe_vehicle()

# Output:
# My truck:
# This vehicle is a 2010 Ford F-150 with 0 miles.

print("\nMy electric car:")
my_electric_car.describe_vehicle()
my_electric_car.lock_doors()
my_electric_car.charge_battery()

# Output:
# My electric car:
# This vehicle is a 2020 Tesla Model S with 0 miles.
# Doors locked.
# Battery charged. 