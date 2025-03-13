# Importing Modules
# ================
# Import the entire math module
import math

# Use a function from the math module
print(math.pi)

# Import a specific function from the math module
from math import sin

# Use the imported function
print(sin(math.pi / 2))

# Standard Library Modules
# =======================
# Import the datetime module
import datetime

# Use a class from the datetime module
now = datetime.datetime.now()
print(now)

# Creating Custom Modules
# =======================
# Create a custom module called 'greetings.py' with the following content:
#   def hello(name):
#       return f"Hello, {name}!"

# Import the custom module
import greetings

# Use a function from the custom module
print(greetings.hello("Alice"))

# Using Packages
# ==============
# Create a package called 'utils' with the following structure:
#   utils/
#       __init__.py
#       string_utils.py
#       math_utils.py

#   string_utils.py:
#       def reverse(s):
#           return s[::-1]

#   math_utils.py:
#       def add(a, b):
#           return a + b

# Import a module from the package
from utils.string_utils import reverse

# Use a function from the imported module
print(reverse("hello"))

# pip
# ===
# Install a package using pip and using VS Code Terminal
# pip install requests

# Import the installed package
import requests

# Use a function from the imported package
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(f"Status code: {response.status_code}") 
# Output: Status code: 200

print(f"Response content: {response.content}") 
# Output: b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'