# Import the `datetime` module to work with dates and times
import datetime

# Define a class called `Person` with attributes and methods
class Person:
    # Initialize the `Person` class with attributes
    def __init__(self, first_name, last_name, birthdate):
        # Attributes
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

    # Method to display person information
    def describe_person(self):
        print(f"{self.first_name} {self.last_name} was born on {self.birthdate.strftime('%B %d, %Y')}")

    # Method to calculate person's age
    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age