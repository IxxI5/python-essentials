# Unittest
# Unittest is a built-in module in Python that provides a framework for writing and running tests.

# VS Code: Command Palette > Python: Configure Tests > pytest

# Issue: AttributeError: module 'collections' has no attribute 'Callable'. 
# Cause: Compatibility issue with pyreadline and Python 3.11 or above
# Result: Test Explorer cannot discover or show tests for Python 3.11 or above
# Solution (VS Code Terminal):
# pip uninstall pyreadline
# pip install pypiwin32

# Import the unittest module to create and run tests
import unittest

# Simple Example 1: Function to add two numbers
def add_numbers(a, b):
    return a + b  # Returns the sum of two numbers

# Test case class for add_numbers function
class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        # Arrange: (Setup test data) - No setup needed here
        
        # Act & Assert: Call function and check expected result
        self.assertEqual(add_numbers(2, 3), 5)  # 2 + 3 should be 5
        self.assertEqual(add_numbers(-1, 1), 0)  # -1 + 1 should be 0
        self.assertEqual(add_numbers(-1, -1), -2)  # -1 + -1 should be -2

# Simple Example 2: Function to check if a number is even
def is_even(n):
    return n % 2 == 0  # Returns True if number is even, otherwise False

# Test case class for is_even function
class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        # Arrange: (Setup test data) - No setup needed here
        
        # Act & Assert: Call function and check expected result
        self.assertTrue(is_even(2))  # 2 is even, so should return True
        self.assertTrue(is_even(4))  # 4 is even, so should return True
        self.assertFalse(is_even(3))  # 3 is odd, so should return False
        self.assertFalse(is_even(1))  # 1 is odd, so should return False

# Advanced Example 1: BankAccount class with deposit and withdraw methods
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  # Initialize account with given balance

    def deposit(self, amount):
        self.balance += amount  # Add amount to the balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")  # Raise error if withdrawal exceeds balance
        self.balance -= amount  # Deduct amount from the balance

# Test case class for BankAccount
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Arrange: Create a BankAccount instance before each test
        self.account = BankAccount(100)  # Start with a balance of 100
    
    def tearDown(self):
        # Cleanup after each test
        del self.account

    def test_deposit(self):
        # Act: Perform deposit operation
        self.account.deposit(50)  # Deposit 50 into account
        
        # Assert: Check if balance is updated correctly
        self.assertEqual(self.account.balance, 150)  # Balance should be 150
    
    def test_withdraw(self):
        # Act: Perform withdraw operation
        self.account.withdraw(20)  # Withdraw 20 from account
        
        # Assert: Check if balance is updated correctly
        self.assertEqual(self.account.balance, 80)  # Balance should be 80
    
    def test_insufficient_funds(self):
        # Act & Assert: Expecting an exception when withdrawing more than balance
        with self.assertRaises(ValueError):
            self.account.withdraw(200)  # Trying to withdraw 200 should raise ValueError


# Arrange, Act, Assert

# Advanced Example 2: Testing a function that uses a mock object
# import unittest.mock

# def get_user_data(user_id):
#     # Simulate a database query
#     return {"name": "John Doe", "email": "johndoe@example.com"}


# Key unittest Assertions:

# assertEqual(a, b): Checks if a and b are equal.
# assertNotEqual(a, b): Checks if a and b are not equal.
# assertTrue(x): Checks if x is true.
# assertFalse(x): Checks if x is false.
# assertIs(a, b): Checks if a and b are the same object.
# assertIsNot(a, b): Checks if a and b are not the same object.
# assertIsNone(x): Checks if x is None.
# assertIsNotNone(x): Checks if x is not None.
# assertRaises(exception, callable, *args, **kwargs): Checks if a specific exception is raised.