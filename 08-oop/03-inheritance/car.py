# Inheritance is a way to create a new class (child class) that inherits from an existing class (parent class) 
# e.g. a child class Car inherits from a parent class Vehicle


# import the parent class
from vehicle import Vehicle

# Define a child class called "Car" that inherits from "Vehicle"
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        # Initialize attributes common to all cars
        super().__init__(brand, model, year)  # Call parent class constructor
        self.doors = doors

    def lock_doors(self):
        # Method specific to cars
        print("Doors locked.")