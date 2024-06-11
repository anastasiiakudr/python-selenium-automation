import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


# @pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        service = ChromeService(executable_path='/usr/local/bin/chromedriver')
        my_driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(executable_path='/usr/local/bin/geckodriver')
        my_driver = webdriver.Firefox(service=service)
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )



