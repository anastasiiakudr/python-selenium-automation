import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Initialize login page and open it
        login_page = LoginPage(driver)
        login_page.open()

        # Perform login with valid credentials
        login_page.execute_login("student", "Password123")

        # Initialize page for logged-in state
        logged_in_page = LoggedInSuccessfullyPage(driver)

        # Verify the current URL matches the expected URL
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"

        # Verify the header text is as expected
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"

        # Verify the logout button is displayed
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"

