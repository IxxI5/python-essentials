# Define a parent class called "Animal"
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display animal information
    def describe_animal(self):
        print(f"This animal is named {self.name} and is {self.age} years old.")

    # Method to make a sound (this will be overridden by child classes)
    def make_sound(self):
        print("The animal makes a generic sound.")

    # Method to eat (this will be overridden by child classes)
    def eat(self):
        print("The animal eats generic food.")