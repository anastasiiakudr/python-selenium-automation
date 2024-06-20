from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfully:
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self._driver.expected_url

    @property
    def header(self) -> str:
        return self.driver.find_element(By.TAG_NAME, "h1").text

    def is_log_out_button_displayed(self) -> bool:
        return self._driver.find_element(self.__log_out_button_locator).is_displayed()





