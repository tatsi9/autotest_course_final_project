import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# Importing Options classes with distinct names to avoid conflict
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Function to add command line options
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                 help="Choose language: en or ru")
    
    
# Fixture for initializing and quitting the browser
@pytest.fixture(scope="function")
def browser(request):
    # Getting the browser name from the command line option
    browser_name = request.config.getoption("browser_name")
    browser = None
    
    # Getting the user language from the command line option
    user_language = request.config.getoption("language")
    
    # Logic to initialize Chrome browser with specific options
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        # Setting language preference for Chrome
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    # Logic to initialize Firefox browser with specific options
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxOptions()
        # Setting language preference for Firefox
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        # Raising an error if the browser_name is neither chrome nor firefox
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()