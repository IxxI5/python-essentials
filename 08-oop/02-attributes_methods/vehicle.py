# Import the `datetime` module to work with dates and times
import datetime

# Define a class called `Vehicle` with attributes and methods
class Vehicle:
    # Initialize the `Vehicle` class with attributes
    def __init__(self, make, model, year, color):
        # Attributes
        # Attribute is a variable that belongs to a class and is shared by all instances of the class
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0

    # Method to display vehicle information
    #Method is a function that belongs to a class and is shared by all instances of the class
    def describe_vehicle(self):
        print(f"This vehicle is a {self.year} {self.color} {self.make} {self.model} with {self.mileage} miles.")

    # Method to update vehicle mileage
    def update_mileage(self, miles):
        if miles >= self.mileage:
            self.mileage = miles
        else:
            print("You can't roll back the odometer!")

    # Method to increment vehicle mileage
    def increment_mileage(self, miles):
        self.mileage += miles