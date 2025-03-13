# Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated 
# as instances of a common superclass.
# In Python, polymorphism is achieved through the use of inheritance and method overriding.

# Import the classes
from animal import Animal
from dog import Dog
from cat import Cat
from bird import Bird

# Create a list of animals
animals = [
    Dog("Fido", 3, "Golden Retriever"),
    Cat("Whiskers", 2, "Grey"),
    Bird("Tweety", 1, "Canary"),
    Animal("Unknown", 0)  # This is just a generic animal
]

# Iterate over the list of animals and call the make_sound and eat methods
for animal in animals:
    animal.describe_animal()
    animal.make_sound()
    animal.eat()
    if isinstance(animal, Dog):
        animal.fetch()
    elif isinstance(animal, Cat):
        animal.scratch()
    elif isinstance(animal, Bird):
        animal.fly()
    print()

# Output:
# This animal is named Fido and is 3 years old.
# The dog barks.
# The dog eats dog food.
# The dog fetches a ball.

# This animal is named Whiskers and is 2 years old.
# The cat meows.
# The cat eats catnip.
# The cat scratches the furniture.

# This animal is named Tweety and is 1 years old.
# The bird chirps.
# The bird eats seeds.
# The bird flies away.

# This animal is named Unknown and is 0 years old.
# The animal makes a generic sound.
# The animal eats generic food.