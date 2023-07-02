import pytest
from selenium import webdriver

from Config.config import TestData

# @pytest.mark.usefixtures("init_driver")
class BaseTest:
    # pass
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def assertEqual(self, expected_alert_message, actual_alert_message):
        pass