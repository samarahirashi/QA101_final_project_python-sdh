from selenium.common import WebDriverException, TimeoutException, NoSuchElementException
from page_object_models.base_page import BasePage
from locators.locators import Locators as loc


class MainPage(BasePage):
    def __init__(self, in_browser):
        super().__init__(in_browser)
    

    def validate_log_in(self):
        # Validates Login Page is displayed
        self.wait_until_isDisplayed(loc.LOG_IN_BUTTON)
        self.wait_until_isDisplayed(loc.WELCOME_HEADER)


    def log_in(self, username, password):
        # click on log in button
        self.wait_until_clickable_then_click(loc.LOG_IN_BUTTON)
        # input text to username box
        self.input_to_element(loc.EMAIL_FIELD, username)
        # press next
        self.press_enter()
        # input text to username password
        self.input_to_element(loc.PASSWORD_FIELD, password)
        # press next
        self.press_enter()
        # click on No on Stay signed in prompt
        self.wait_until_clickable_then_click(loc.STAY_SIGNED_IN_PROMPT_NO)
        # validate log in successful
        try:
            self.wait_for_element_to_be_visible(loc.ENROUTE_HEADER_LOGO)
        except (WebDriverException, TimeoutException, NoSuchElementException):
            raise "Log in not successful"

    def go_to_profile(self):
        # click on sidebar menu
        self.wait_until_clickable_then_click(loc.SIDEBAR_MENU_TOGGLE_BUTTON)
        # click on profile
        self.wait_until_clickable_then_click(
            # We use a Dynamic parameter to create a single locator.
            loc.Dynamic.get_menu_item("Profile")
        )
        # validate profile is shown
        self.wait_for_element_to_be_visible(loc.PROFILE_NAMES)

    def get_profile_first_name(self):
        # get name text
        name_element = self.get_element(loc.PROFILE_NAMES)
        return name_element.text

    def get_pmf_points(self):
        # get PMF points
        pass
