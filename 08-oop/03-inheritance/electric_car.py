# Inheritance is a way to create a new class (child class) that inherits from an existing class (parent class) 
# e.g. a child class ElectricCar inherits from a parent class Car

# import the parent class
from car import Car
 
# Define a child class called "ElectricCar" that inherits from "Car"
class ElectricCar(Car):
    def __init__(self, brand, model, year, doors, battery_size):
        # Initialize attributes common to all electric cars
        super().__init__(brand, model, year, doors)  # Call parent class constructor
        self.battery_size = battery_size

    def charge_battery(self):
        # Method specific to electric cars
        print("Battery charged.")