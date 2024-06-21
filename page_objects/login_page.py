from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        """Open the login page using the URL specified."""
        self.open_url(self.__url)  # Call the method directly from BasePage

    def execute_login(self, username: str, password: str):
        """Log in using the provided username and password."""
        self._type(self.__username_field, username)
        self._type(self.__password_field, password)
        self._click(self.__submit_button)
