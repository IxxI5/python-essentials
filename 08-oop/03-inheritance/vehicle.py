# Define a parent class called "Vehicle"
class Vehicle:
    def __init__(self, brand, model, year):
        # Initialize attributes common to all vehicles
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        # Method to increase mileage
        self.mileage += miles

    def describe_vehicle(self):
        # Method to print out vehicle details
        print(f"This vehicle is a {self.year} {self.brand} {self.model} with {self.mileage} miles.")