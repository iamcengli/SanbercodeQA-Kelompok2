from Pages.LogOut import LogOut
import pytest
import time
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.BasePage import Alert

class Test_LogOut(BaseTest):

    #TC ID PS1-001
    def test_success_log_out(self):
        self.logOut = LogOut(self.driver)
        self.logOut.do_open_login_page()
        self.logOut.do_send_message(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        time.sleep(2)
        self.logOut.do_click_log_out()
        time.sleep(2)

        # Validasi Logout 😪😪😪😪😪😪😪😪😪
        