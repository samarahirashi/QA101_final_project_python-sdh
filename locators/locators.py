from selenium.webdriver.common.by import By


class Locators:
    """
    Space for creating static locators
    In this house we use holy Xpaths
    """
    # Log In Page
    WELCOME_HEADER = (By.CSS_SELECTOR, ".css-1h808s5")
    LOG_IN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    STAY_SIGNED_IN_PROMPT_NO = (By.XPATH, "//input[@type='button' and @value='No']")

    ENROUTE_HEADER_LOGO = (By.XPATH, "//a[@href='/home']")
    SIDEBAR_MENU_TOGGLE_BUTTON = (By.XPATH, "//a[@href='#open-sidebar']")
    # PROFILE PAGE
    PROFILE_NAMES = (By.XPATH, "//div[@class='css-16rnk79']")
    ENROUTE_PROFILE_POSITION = (By.XPATH, "//div[@class='css-1d93mh8']")
    PMF_POINTS = (By.XPATH, "//div[@class='css-lgaul']")

    # MY POSITION
    MY_POSITION_CARD_DATA = (By.XPATH, "//div[@class='css-1la031y']/p")

    class Dynamic:
        """
        Use the methods here to create locators that change based on parameters
        """

        _SIDEBAR_MENU_ITEM = "//div[contains(@class, 'SideBar')]//li/a[text()='{item}']"

        @classmethod
        def get_menu_item(cls, menu_item_name):
            """
            Get the selector for an item on the sidebar menu. Pass the menu item name as parameter (case sensitive)
            """
            return By.XPATH, cls._SIDEBAR_MENU_ITEM.replace('{item}', menu_item_name)


