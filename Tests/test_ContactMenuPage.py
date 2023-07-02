import pytest
from Config.config import TestData
from Pages.ContactMenuPage import ContactMenuPage
from Tests.test_base import BaseTest
import time
from selenium.webdriver.common.alert import Alert


class Test_Contact_Menu(BaseTest):
        
    def test_send_message(self):
        self.contactMenu = ContactMenuPage(self.driver)
        self.contactMenu.do_open_contact_menu()
        self.contactMenu.do_send_message(TestData.CM_EMAIL_INVALID, TestData.CM_NAME, TestData.CM_MESSAGE)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Thanks for the message!!" #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
        # self.contactMenu.is_alert_message_equal(TestData.CM_MESSAGE)
        self.contactMenu.close()
        
    # def test_check_message(self):
    #     contact_page = ContactMenuPage(self.driver)
        