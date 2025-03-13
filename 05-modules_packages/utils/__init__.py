# This __init__.py file serves several purposes:
# 1. It indicates that the directory containing it should be treated as a Python package.
# 2. It allows relative imports within the package.
# 3. It can be used to initialize the package or perform setup tasks.
# For example, if you have a directory structure like this:
# my_package/
#     __init__.py
#     module1.py
#     module2.py

# You can import module1 and module2 like this:
# from my_package import module1
# from my_package import module2

# When this package is imported, the code in this file will be executed.
# This can be useful for setting up package-level variables or performing initialization tasks.

# Here's an example of what the __init__.py file might contain:
# my_package/__init__.py
# print("Initializing my package")

# Set up package-level variables
# package_variable = "Hello, world!"

# In this case, when you import my_package, the message "Initializing my package" will be printed, and the package_variable will be set.

