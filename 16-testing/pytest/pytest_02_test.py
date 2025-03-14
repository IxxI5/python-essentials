# API Testing with Pytest in Python
# Pytest is a popular testing framework for Python.

# Import dependencies
import pytest
import requests

# Dependency Installation:
# Ensure you have pytest installed by running:
# pip install pytest
# Additional dependencies:
# pip install requests

# VS Code: Command Palette > Python: Configure Tests > pytest

# Issue: AttributeError: module 'collections' has no attribute 'Callable'. 
# Cause: Compatibility issue with pyreadline and Python 3.11 or above
# Result: Test Explorer cannot discover or show tests for Python 3.11 or above
# Solution (VS Code Terminal):
# pip uninstall pyreadline
# pip install pypiwin32

# Fetching data from JSONPlaceholder API
class JSONPlaceholderService:
    def __init__(self, api_url):
        self.api_url = api_url                                          # Constructor: Replace with the actual API URL
    def get_post(self, post_id):
        response = requests.get(f"{self.api_url}/posts/{post_id}")      # Replace with the actual API endpoint
        if response.status_code != 200:
            raise ValueError("Failed to fetch post data")
        return response.json()

# Using pytest fixtures to setup common resources
@pytest.fixture
def jsonplaceholder_service():
    # Arrange: Setup JSONPlaceholderService instance with the API URL
    return JSONPlaceholderService("https://jsonplaceholder.typicode.com")

# Basic Test Case
def test_get_post_success(jsonplaceholder_service):
    # Act: Call the method with a real API request
    result = jsonplaceholder_service.get_post(1)

    # Assert: Validate the response contains expected keys
    assert isinstance(result, dict) # Check if the result is a dictionary
    assert "userId" in result       # Check if the "userId" key is present
    assert "id" in result           # Check if the "id" key is present
    assert "title" in result        # Check if the "title" key is present
    assert "body" in result         # Check if the "body" key is present

# Testing exception handling
def test_get_post_failure(jsonplaceholder_service):
    # Act & Assert: Expect an exception for an invalid post ID
    with pytest.raises(ValueError, match="Failed to fetch post data"):
        jsonplaceholder_service.get_post(999999)

# Parameterized Testing: Testing multiple cases efficiently
@pytest.mark.parametrize("post_id", [1, 2, 3])                      # Provide a list of valid post IDs
def test_get_post_multiple_cases(jsonplaceholder_service, post_id):
    # Act: Call the method
    result = jsonplaceholder_service.get_post(post_id)              # Pass the valid post ID over the fixture

    # Assert: Validate the response structure
    assert isinstance(result, dict)                                 # Check if the result is a dictionary
    assert result["id"] == post_id                                  # Check if the "id" key has the expected value

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