# Variables and Data Types
# Variables are used to store and manipulate data in a program.
# Data types determine the type of value a variable can hold.

name = "John Doe"  # string variable
age = 30  # integer variable
height = 1.75  # float variable
is_adult = True  # boolean variable
colors = ["red", "green", "blue"]  # list variable
person = {"name": "John", "age": 30}  # dictionary variable
numbers = (1, 2, 3)  # tuple variable
empty_list = []  # empty list
empty_dict = {}  # empty dictionary

# Print the variables
# This section prints the variables to the console for verification.
# It is used to test that the variables have been assigned correctly.
print("Name:", name)                # Output: Name: John Doe
print("Age:", age)                  # Output: Age: 30
print("Height:", height)            # Output: Height: 1.75
print("Is Adult:", is_adult)        # Output: Is Adult: True
print("Colors:", colors)            # Output: Colors: ['red', 'green', 'blue']
print("Person:", person)            # Output: Person: {'name': 'John', 'age': 30}
print("Numbers:", numbers)          # Output: Numbers: (1, 2, 3)
print("Empty List:", empty_list)    # Output: Empty List: []
print("Empty Dict:", empty_dict)    # Output: Empty Dict: {}

# Input and Output
# Input and output operations allow the program to interact with the user.
user_name = input("What is your name? ")
print("Hello, " + user_name + "!")

# Basic Operations
# Basic operations include arithmetic, comparison, and logical operations.
x = 5
y = 3

# Arithmetic Operators
# Arithmetic operators perform mathematical operations on numbers.
print("x + y =", x + y)             # Output: x + y = 8
print("x - y =", x - y)             # Output: x - y = 2
print("x * y =", x * y)             # Output: x * y = 15
print("x / y =", x / y)             # Output: x / y = 1.6666666666666667

# modulus (remainder)
print("x % y =", x % y)             # Output: x % y = 2

# exponentiation
print("x ** y =", x ** y)           # Output: x ** y = 125

# Comparison Operators
# Comparison operators compare values and return a boolean result.
print("x == y", x == y)             # Output: x == y False
print("x != y", x != y)             # Output: x != y True
print("x > y", x > y)               # Output: x > y False
print("x < y", x < y)               # Output: x < y True
print("x >= y", x >= y)             # Output: x >= y False
print("x <= y", x <= y)             # Output: x <= y True

# Logical Operators
# Logical operators combine multiple conditions and return a boolean result.
print("x > 2 and x < 10", x > 2 and x < 10)     # Output: x > 2 and x < 10 False
print("x > 2 or x < 10", x > 2 or x < 10)       # Output: x > 2 or x < 10 True
print("not x > 2", not x > 2)                   # Output: not x > 2 False

# List Operations
# Lists are ordered collections of values that can be modified.
# indexing
print("colors[0]", colors[0])                   # Output: colors[0] red
# slicing
print("colors[1:3]", colors[1:3])               # Output: colors[1:3] ['green', 'blue']

colors.append("yellow")
print("colors", colors)                         # Output: colors ['red', 'green', 'blue', 'yellow']

colors.insert(1, "orange") 
print("colors", colors)                         # Output: colors ['red', 'orange', 'green', 'blue', 'yellow']

colors.remove("green") 
print("colors", colors)                         # Output: colors ['red', 'orange', 'blue', 'yellow']

# Dictionary Operations
# Dictionaries are unordered collections of key-value pairs that can be modified.
# indexing
print("person['name']", person["name"])         # Output: person['name'] John

# assignment
person["age"] = 31  
print("person", person)                         # Output: person {'name': 'John', 'age': 31}

# add new key-value pair
person[" occupation"] = "Developer"  
print("person", person)                         # Output: person {'name': 'John', 'age': 31, ' occupation': 'Developer'}

# delete key-value pair
del person["age"]  
print("person", person)                         # Output: person {'name': 'John', ' occupation': 'Developer'}

# Tuple Operations
# Tuples are ordered, immutable collections of values.
# indexing
print("numbers[0]", numbers[0])                 # Output: numbers[0] 1

# slicing
print("numbers[1:3]", numbers[1:3])             # Output: numbers[1:3] (2, 3)

# String Operations
# Strings are sequences of characters that can be manipulated.
greeting = "Hello, " + user_name + "!"
print("greeting", greeting)                     # Output: greeting Hello, Alice!

greeting = "Hello, {}!".format(user_name)
print("greeting", greeting)                     # Output: greeting Hello, Alice!

greeting = f"Hello, {user_name}!"
print("greeting", greeting)                     # Output: greeting Hello, Alice!

# Function: greet(name)
# This function prints a personalized greeting message to the console.
# In Python, the triple-quoted string """...""" is used to create a docstring. 
# It is used to document the code and provide a description of what the code does.
def greet(name):
    """
    Prints a personalized greeting message.

    Args:
        name (str): The person's name.

    Returns:
        None
    """
    print("Hello, " + name + "!")

# Call the greet function with the name "Alice"
greet("Alice")                                  # Output: Hello, Alice!  

# Output: Hello, Alice!

# Type Casting
# Type casting is the process of converting a value from one data type to another.

# Integer to float
num_int = 10
num_float = float(num_int)
print(num_float)                    # Output: 10.0

# Float to integer
num_float = 10.8
num_int = int(num_float)
print(num_int)                      # Output: 10

# String to integer
num_str = "20"
num_int = int(num_str)
print(num_int)                      # Output: 20

# Integer to string
num = 30
num_str = str(num)
print(num_str)                      # Output: "30"

# List to tuple
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print(tuple_data)                   # Output: (1, 2, 3)

# Tuple to list
tuple_data = (4, 5, 6)
list_data = list(tuple_data)
print(list_data)                    # Output: [4, 5, 6]

# Dictionary to list
dict_data = {"a": 1, "b": 2, "c": 3}
list_data = list(dict_data.items())
print(list_data)                    # Output: [('a', 1), ('b', 2), ('c', 3)]

# List to dictionary
list_data = [("a", 1), ("b", 2), ("c", 3)]
dict_data = dict(list_data)
print(dict_data)                    # Output: {'a': 1, 'b': 2, 'c': 3}