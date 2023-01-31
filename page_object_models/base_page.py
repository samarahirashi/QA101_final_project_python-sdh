from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, in_browser):
        self.browser = in_browser
        self.wait_short = WebDriverWait(self.browser, 20)
        self.wait_long = WebDriverWait(self.browser, 45)

    def get_element(self, element, wait=45):
        """
        Generic method to get multiple elements
        """
        ec_clickable = EC.element_to_be_clickable(element)
        clickable = None
        if isinstance(wait, int) or isinstance(wait, float):
            clickable = WebDriverWait(self.browser, wait).until(ec_clickable)
        return clickable

    def press_enter(self):
        action = ActionChains(self.browser)
        action.send_keys(Keys.ENTER).perform()

    def wait_for_element_to_be_visible(self, locator):
        self.wait_long.until(EC.visibility_of_element_located(locator))

    def click_element(self, element_locator, wait=45):
        clickable = self.get_element(element_locator, wait)
        clickable.click()

    def input_to_element(self, element_locator, input_text, wait=30):
        """
        Input text to an element
        """
        clickable = self.get_element(element_locator, wait=30)
        clickable.clear()
        clickable.send_keys(input_text)

    def wait_until_isDisplayed(self, element_locator, wait=30):
        element = self.wait_short.until(EC.element_to_be_clickable(element_locator))
        element.is_displayed()

    def wait_until_clickable_then_click(self, element_locator, wait=30):
        element = self.wait_short.until(EC.element_to_be_clickable(element_locator))
        if element and element.is_enabled():
            element.click()
