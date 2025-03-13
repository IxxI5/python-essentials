# Polymorphism is achieved through the use of inheritance and method overriding.

# import the parent class
from animal import Animal

# Define a child class called "Cat" that inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # Override the make_sound method to make a cat-specific sound
    def make_sound(self):
        print("The cat meows.")

    # Override the eat method to eat cat-specific food
    def eat(self):
        print("The cat eats catnip.")

    # Add a new method specific to cats
    def scratch(self):
        print("The cat scratches the furniture.")