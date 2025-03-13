# Inheritance is a way to create a new class (child class) that inherits from an existing class (parent class) 
# e.g. a child class Truck inherits from a parent class Vehicle

# import the parent class
from vehicle import Vehicle 

# Define a child class called "Truck" that inherits from "Vehicle"
class Truck(Vehicle):
    def __init__(self, brand, model, year, capacity):
        # Initialize attributes common to all trucks
        super().__init__(brand, model, year)  # Call parent class constructor
        self.capacity = capacity

    def load_cargo(self):
        # Method specific to trucks
        print("Cargo loaded.")