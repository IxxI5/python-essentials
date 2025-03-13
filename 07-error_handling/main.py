# Error Handling is a process of handling exceptions that may occur during the execution of a program.

# Example 1: Syntax Error
# The following line will raise a SyntaxError because of the missing colon
# def greet(name)  # Uncomment this line to see the SyntaxError

# Example 2: Exception (TypeError)
def divide_numbers(a, b):
    """Divide two numbers"""
    # Try to divide a and b
    try:
        result = a / b
        print(f"{a} divided by {b} is {result}")
    # Catch specific exceptions
    except TypeError:
        print("Error: Both inputs must be numbers")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

# Test the function
divide_numbers(10, 2)  # Output: 10 divided by 2 is 5.0
divide_numbers(10, "two")  # Output: Error: Both inputs must be numbers
divide_numbers(10, 0)  # Output: Error: Cannot divide by zero

# Example 3: Try-Except-Finally Block
def read_file(filename):
    """Read a file and print its contents"""
    # Try to open and read the file
    try:
        with open(filename, "r") as file:
            contents = file.read()
            print(contents)
    # Catch specific exceptions        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File operation completed")

# Test the function
read_file("example.txt")  # Output: File 'example.txt' not found (if the file doesn't exist)

# Example 4: Raising Exceptions
def validate_age(age):
    """Validate a person's age"""
    if age < 18:
        raise ValueError("Age must be 18 or older")
    print(f"Age {age} is valid")

# Test the function
try:
    validate_age(15)  # Output: ValueError: Age must be 18 or older
except ValueError as e:
    print(e)

# Example 5: Custom Exceptions
class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance"""
    pass

def withdraw_money(balance, amount):
    """Withdraw money from an account"""
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    print(f"Withdrew ${amount} from account")

# Test the function
try:
    withdraw_money(100, 150)  # Output: InsufficientBalanceError: Insufficient balance
except InsufficientBalanceError as e:
    print(e)