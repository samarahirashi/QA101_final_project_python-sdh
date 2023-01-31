import unittest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from page_object_models.main_page import MainPage
from utilities.constants import user_name, password


class MasterKeyTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get('https://masterkey.enroutesystems.com/home')

    def test_name_in_profile_page(self):
        page = MainPage(self.driver)
        page.validate_log_in()
        page.log_in(username=user_name, password=password)
        page.go_to_profile()
        name = page.get_profile_first_name()
        print(name)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

