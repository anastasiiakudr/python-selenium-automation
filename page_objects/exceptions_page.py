from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    # URL for the exceptions page
    __url = "https://practicetestautomation.com/practice-test-exceptions/"

    # Element locators
    __add_button_locator = (By.ID, "add_btn")
    __row_1_input_element = (By.XPATH, "//div[@id='row1']/input")
    __row_2_input_element = (By.XPATH, "//div[@id='row2']/input")
    __row_1_save_button = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row_2_save_button = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __row_1_edit_button = (By.ID, "edit_btn")
    __confirmation_element = (By.ID, "confirmation")
    __instructions_element = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        # Initialize with driver
        super().__init__(driver)

    def open(self):
        # Open the exceptions page
        super()._open_url(self.__url)

    def add_second_row(self):
        # Click "Add" button to show second row
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row_2_input_element)

    def is_row2_displayed(self) -> bool:
        # Check if second row is displayed
        return super()._is_displayed(self.__row_2_input_element)

    def add_second_food(self, food: str):
        # Enter text in second row and save
        super()._type(self.__row_2_input_element, food)
        super()._click(self.__row_2_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def get_confirmation_message(self) -> str:
        # Get text of confirmation message
        return super()._get_text(self.__confirmation_element, time=3)

    def modify_row_1_input(self, food: str):
        # Edit, clear, type text in first row, and save
        super()._click(self.__row_1_edit_button)
        super()._wait_until_element_is_clickable(self.__row_1_input_element)
        super()._clear(self.__row_1_input_element)
        super()._type(self.__row_1_input_element, food)
        super()._click(self.__row_1_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def are_instructions_displayed(self) -> bool:
        # Check if instructions are displayed
        return super()._is_displayed(self.__instructions_element)
