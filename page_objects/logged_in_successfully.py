from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    # URL for the successful login page
    _url = "https://practicetestautomation.com/logged-in-successfully/"

    # Locators for page elements
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        # Initialize with driver
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        # Return the expected URL for this page
        return self._url

    @property
    def header(self) -> str:
        # Get the header text
        return super()._get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:
        # Check if the logout button is displayed
        return super()._is_displayed(self.__log_out_button_locator)






