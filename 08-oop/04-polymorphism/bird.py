# Polymorphism is achieved through the use of inheritance and method overriding.

# import the parent class
from animal import Animal

# Define a child class called "Bird" that inherits from Animal
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    # Override the make_sound method to make a bird-specific sound
    def make_sound(self):
        print("The bird chirps.")

    # Override the eat method to eat bird-specific food
    def eat(self):
        print("The bird eats seeds.")

    # Add a new method specific to birds
    def fly(self):
        print("The bird flies away.")