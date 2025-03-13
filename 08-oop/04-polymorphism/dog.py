# Polymorphism is achieved through the use of inheritance and method overriding.

# import the parent class
from animal import Animal

# Define a child class called "Dog" that inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    # Override the make_sound method to make a dog-specific sound
    def make_sound(self):
        print("The dog barks.")

    # Override the eat method to eat dog-specific food
    def eat(self):
        print("The dog eats dog food.")

    # Add a new method specific to dogs
    def fetch(self):
        print("The dog fetches a ball.")