from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        # Initialize the class with the browser driver
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        # Find and return the element based on the given locator
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        # Wait until the element is visible, then type text into it
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple, time: int = 10):
        # Wait until the element is visible, then clear its contents
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _click(self, locator: tuple, time: int = 10):
        # Wait until the element is visible, then click on it
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        # Wait until the element becomes visible on the page
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        # Wait until the element is clickable (ready for interaction)
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    @property
    def current_url(self) -> str:
        # Return the current URL of the browser
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        # Check if the element is displayed on the page
        # Returns False if the element is not found
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        # Open the specified URL in the browser
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        # Wait until the element is visible, then get its text content
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

