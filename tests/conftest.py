import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture()
def driver(request):
    # Get the browser option from the command line
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")

    # Set up the browser driver based on the chosen option
    if browser == "chrome":
        service = ChromeService(executable_path='/usr/local/bin/chromedriver')
        my_driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(executable_path='/usr/local/bin/geckodriver')
        my_driver = webdriver.Firefox(service=service)
    else:
        # Raise an error if the browser option is not supported
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")

    # Set implicit wait for finding elements
    my_driver.implicitly_wait(10)

    # Provide the driver instance to the test, and close it afterward
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    # Add a command-line option for selecting the browser
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )




