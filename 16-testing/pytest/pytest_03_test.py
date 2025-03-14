# UI Testing with Selenium
# Selenium is a popular framework for automating web browsers.

# Import the pytest framework for testing
import pytest

# Dependency Installation:
# Ensure you have pytest installed by running:
# pip install pytest selenium webdriver-manager

# Import the Selenium WebDriver for browser automation
from selenium import webdriver

# Import the By class for specifying element location strategies
from selenium.webdriver.common.by import By

# Import the Keys class for simulating keyboard input
from selenium.webdriver.common.keys import Keys

# Import the ChromeDriverManager for managing ChromeDriver installations
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Define a pytest fixture for setting up and tearing down the browser
# A pytest fixture is a function that runs before and after each test
@pytest.fixture
def browser():
    # Initialize the Chrome WebDriver using the ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    options = Options()

    # prevent automation (driven by Selenium WebDriver) from being detected
    options.add_argument("--disable-blink-features=AutomationControlled"); # prevents Captcha from appearing
    
    # Create a ChromeDriver instance
    driver = webdriver.Chrome(service=service, options=options) 
    
    # Set an implicit wait of 5 seconds for elements to load
    driver.implicitly_wait(5)
    
    # Yield the driver to the test function
    yield driver
    
    # Close the browser after the test. It is done automatically by the pytest fixture
    # driver.quit()
    

# Define a test function for searching on Google
def test_google_search(browser):
    # Arrange: Open the Google homepage
    browser.get("https://www.google.com")

    # Maximize the browser window
    browser.maximize_window()

    # Press Accept on Google pop-up if present
    try:
        browser.find_element(By.ID, "L2AGLb").click()
    except:
        pass

    # Act: Find the search box, type a query, and press Enter
    # Use the By.NAME strategy to locate the search box element
    search_box = browser.find_element(By.NAME, "q")
    
    # Send the search query and press Enter using the Keys.RETURN key
    search_box.send_keys("pytest UI testing" + Keys.RETURN)

    # Remove Captcha if present
    try:
        browser.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
    except:
        pass

    # Assert: Check if the results page is loaded
    # Verify that the page title contains the search query
    assert "pytest UI testing" in browser.title

    # Verify that at least one search result with text "pytest UI testing" is present
    assert "pytest UI testing" in browser.page_source
    
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