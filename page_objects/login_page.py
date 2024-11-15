from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    # URL for the login page
    __url = "https://practicetestautomation.com/practice-test-login/"

    # Locators for elements on the page
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        # Initialize the page with the browser driver
        super().__init__(driver)

    def open(self):
        # Open the login page
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        # Enter username, password, and click submit button
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_message(self) -> str:
        # Retrieve the error message text
        return super()._get_text(self.__error_message, time=3)

