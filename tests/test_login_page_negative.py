import pytest
from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Initialize login page and open it
        login_page = LoginPage(driver)
        login_page.open()

        # Attempt to log in with invalid credentials
        login_page.execute_login(username, password)

        # Verify that the error message matches the expected message
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"

