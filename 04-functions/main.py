# Defining and Calling Functions
# Function Definition: It is a block of code that performs a specific task or set of tasks.
def greet(name):
    # This function takes a name as an argument and prints a greeting message
    print(f"Hello, {name}!")

# Call the greet function with a name
greet("John")  # Output: Hello, John!

# Function Arguments and Return Values
def add(a, b):
    # This function takes two numbers as arguments and returns their sum
    return a + b

# Call the add function with two numbers and store the result in a variable
result = add(2, 3)
print(result)  # Output: 5

# Lambda Functions
double = lambda x: x * 2  # Define a lambda function that doubles a number
print(double(5))  # Output: 10

# Variable Scope (Local vs Global)
x = 10  # Global variable

def local_scope():
    x = 20  # Local variable
    print("Local x:", x)

local_scope()  # Output: Local x: 20
print("Global x:", x)  # Output: Global x: 10

# Recursion
def factorial(n):
    # This function calculates the factorial of a number using recursion
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

# Recursive Sum
def recursive_sum(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: add the first element to the sum of the rest of the list
    else:
        return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print(result)  # Output: 15

# Example of a recursive function with a default argument value
def countdown(n=5):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n-1)

countdown()  # Output: 5, 4, 3, 2, 1, Blast off!