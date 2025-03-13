# Import the `Vehicle`, `ElectricVehicle`, and `Person` classes from their respective modules
from vehicle import Vehicle
from electric_vehicle import ElectricVehicle
from person import Person

# Create instances of the classes
my_vehicle = Vehicle("Toyota", "Corolla", 2015, "Silver")
my_electric_vehicle = ElectricVehicle("Tesla", "Model S", 2020, "Red", 75)
my_person = Person("John", "Doe", "1990-02-12")

# Call methods on the instances
my_vehicle.describe_vehicle()
my_vehicle.update_mileage(30000)
my_vehicle.increment_mileage(5000)
my_vehicle.describe_vehicle()

my_electric_vehicle.describe_electric_vehicle()
my_electric_vehicle.charge_vehicle(20)
my_electric_vehicle.describe_electric_vehicle()

my_person.describe_person()
print(f"{my_person.first_name} is {my_person.calculate_age()} years old.")

# Output:
# This vehicle is a 2015 Silver Toyota Corolla with 0 miles.
# This vehicle is a 2015 Silver Toyota Corolla with 35000 miles.
# This vehicle is a 2020 Red Tesla Model S with 0 miles.
# This electric vehicle has a 75 kWh battery and is currently 100% charged.
# This vehicle is a 2020 Red Tesla Model S with 0 miles.
# This electric vehicle has a 75 kWh battery and is currently 100% charged.
# John Doe was born on February 12, 1990
# John is 35 years old.