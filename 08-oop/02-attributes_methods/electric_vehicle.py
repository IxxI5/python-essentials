# Import the `Vehicle` class from the `vehicle` module
from vehicle import Vehicle

# Define a class called `ElectricVehicle` that inherits from `Vehicle`
class ElectricVehicle(Vehicle):
    # Initialize the `ElectricVehicle` class with attributes
    def __init__(self, make, model, year, color, battery_size):
        # Call the `__init__` method from the parent class named `Vehicle`
        super().__init__(make, model, year, color)
        self.battery_size = battery_size
        self.charge_level = 100

    # Method to display electric vehicle information
    def describe_electric_vehicle(self):
        # Call the `describe_vehicle` method from the parent class named `Vehicle` 
        super().describe_vehicle()
        print(f"This electric vehicle has a {self.battery_size} kWh battery and is currently {self.charge_level}% charged.")

    # Method to charge the electric vehicle
    def charge_vehicle(self, charge_amount):
        if charge_amount >= 0 and charge_amount <= 100:
            self.charge_level += charge_amount
            if self.charge_level > 100:
                self.charge_level = 100
        else:
            print("Invalid charge amount!")