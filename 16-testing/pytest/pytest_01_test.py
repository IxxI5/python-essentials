# Mock API Testing with Pytest in Python
# Pytest is a popular testing framework for Python.

# Import dependencies
import pytest
from unittest.mock import MagicMock
import requests

# Dependency Installation:
# Ensure you have pytest installed by running:
# pip install pytest
# Additional dependencies:
# pip install pytest-mock requests

# VS Code: Command Palette > Python: Configure Tests > pytest

# Issue: AttributeError: module 'collections' has no attribute 'Callable'. 
# Cause: Compatibility issue with pyreadline and Python 3.11 or above
# Result: Test Explorer cannot discover or show tests for Python 3.11 or above
# Solution (VS Code Terminal):
# pip uninstall pyreadline
# pip install pypiwin32

# Fetching data from a mock API. Mocking is a technique to simulate responses from an API.
class WeatherService:
    def __init__(self, api_url):
        self.api_url = api_url                                                  # Constructor: Replace with the actual API URL

    def get_weather(self, city):
        response = requests.get(f"{self.api_url}/weather?city={city}")          # Replace with the actual API endpoint
        if response.status_code != 200:
            raise ValueError("Failed to fetch weather data")                    # Raise an exception with the actual error message
        return response.json()

# Using pytest fixtures to setup common resources
@pytest.fixture
def weather_service():
    # Arrange: Setup WeatherService instance with a mock API URL
    return WeatherService("https://api.example.com")

# Basic Test Case
def test_get_weather_success(mocker, weather_service):
    # Arrange: Mock the requests.get call
    mock_response = MagicMock()                                                     # Mocking the requests.get function                     
    mock_response.status_code = 200                                                 # Mocking the status code
    mock_response.json.return_value = {"temperature": 22, "condition": "Sunny"}     # Mocking the JSON response
    mocker.patch("requests.get", return_value=mock_response)                        # Patching the requests.get function, 
                                                                                    # meaning it will return the mocked response
    # Act: Call the method
    result = weather_service.get_weather("London")

    # Assert: Validate the expected outcome
    assert result == {"temperature": 22, "condition": "Sunny"}

# Testing exception handling
def test_get_weather_failure(mocker, weather_service):
    # Arrange: Mock the requests.get call to return a failure response
    mock_response = MagicMock()                                                     # Mocking the requests.get function
    mock_response.status_code = 500                                                 # Mocking the status code
    mocker.patch("requests.get", return_value=mock_response)                        # Patching the requests.get function, 
                                                                                    # meaning it will return the mocked response

    # Act & Assert: Expect an exception
    with pytest.raises(ValueError, match="Failed to fetch weather data"):           # Using pytest.raises to expect an exception
        weather_service.get_weather("New York")

# Parameterized Testing: Testing multiple cases efficiently
@pytest.mark.parametrize(
    "city, expected_response",
    [
        ("Paris", {"temperature": 18, "condition": "Cloudy"}), 
        ("Tokyo", {"temperature": 25, "condition": "Rainy"}),
    ]
)
def test_get_weather_multiple_cases(mocker, weather_service, city, expected_response):
    # Arrange: Mock the requests.get call
    mock_response = MagicMock()                                                     # Mocking the requests.get function
    mock_response.status_code = 200                                                 # Mocking the status code
    mock_response.json.return_value = expected_response                             # Mocking the JSON response
    mocker.patch("requests.get", return_value=mock_response)                        # Patching the requests.get function, 
                                                                                    # meaning it will return the mocked response

    # Act: Call the method
    result = weather_service.get_weather(city)

    # Assert
    assert result == expected_response

# Mocking Example: Mocking an external API call
@pytest.fixture
def mock_requests_get(mocker):
    # Arrange: Mocking the requests.get function globally
    return mocker.patch("requests.get", autospec=True)                               # Patching the requests.get function, 
                                                                                     # meaning it will return the mocked response

def test_mocking_example(mock_requests_get, weather_service):
    # Arrange: Set up mock response
    mock_response = MagicMock()                                                      # Mocking the requests.get function
    mock_response.status_code = 200                                                  # Mocking the status code
    mock_response.json.return_value = {"temperature": 30, "condition": "Hot"}        # Mocking the JSON response
    mock_requests_get.return_value = mock_response                                   # Patching the requests.get function, 
                                                                                     # meaning it will return the mocked response

    # Act: Call the method
    result = weather_service.get_weather("Dubai")

    # Assert: Ensure the function was called once with expected arguments
    mock_requests_get.assert_called_once_with("https://api.example.com/weather?city=Dubai") 
    assert result == {"temperature": 30, "condition": "Hot"}                         # Check if the result matches the expected response

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