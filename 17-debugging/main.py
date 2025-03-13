"""
Python Debugging Techniques
This script demonstrates various debugging techniques in Python,
including print statements, assertions, logging, pdb debugging, and exception handling.
"""

# Import necessary modules
import logging
import pdb

# 1. Using Print Statements
def add_numbers(a, b):
    print(f"Values received: a={a}, b={b}")         # Debug print: Values received: a=3, b=5
    return a + b

result = add_numbers(3, 5)
print(f"Result: {result}")                          # Debug print: Result: 8   

# 2. Using assert Statements
def divide(x, y):
    assert y != 0, "Denominator must not be zero"   # Ensuring y is not zero
    return x / y

print(divide(10, 2))                                # Works fine: 
# print(divide(10, 0))  # Uncommenting this line will raise an AssertionError

# 3. Using the logging module
logging.basicConfig(level=logging.DEBUG)            # Setting logging level to DEBUG
def multiply(x, y):
    logging.debug(f"Multiplying {x} and {y}")       # DEBUG:root:Multiplying 3 and 4
    return x * y

print(multiply(3, 4))                               # 12

# 4. Using pdb (Python Debugger)
def faulty_function(x):
    pdb.set_trace()                                 # Enters interactive debugging mode
    y = x + 10
    z = y / 2
    return z

# Uncomment to debug interactively
# faulty_function(5)

# 5. Using Exception Handling
try:
    num = int("abc")                                # This will cause a ValueError
except ValueError as e:
    print(f"Error occurred: {e}")                   # Error occurred: invalid literal for int() with base 10: 'abc'
