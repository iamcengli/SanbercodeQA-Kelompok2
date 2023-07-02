import pytest
from Config.config import TestData
from Pages.ContactMenuPage import ContactMenuPage
from Tests.test_base import BaseTest
import time
from selenium.webdriver.common.alert import Alert


class Test_Contact_Menu(BaseTest):
    
    # TC6-001
    def test_send_message(self):
        self.contactMenu = ContactMenuPage(self.driver)
        self.contactMenu.do_open_contact_menu()
        self.contactMenu.do_send_message(TestData.CM_EMAIL_VALID, TestData.CM_NAME, TestData.CM_MESSAGE)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = TestData.CM_RESPONSE_MESSAGE #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
        # self.contactMenu.is_alert_message_equal(TestData.CM_MESSAGE)
        self.contactMenu.close()
        
    # TC6-002 
    def test_failed_send_message1(self):
        self.contactMenu = ContactMenuPage(self.driver)
        self.contactMenu.do_open_contact_menu()
        self.contactMenu.do_send_message(TestData.CM_EMAIL_INVALID, TestData.CM_NAME, TestData.CM_MESSAGE)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = TestData.CM_RESPONSE_INVALID_EMAIL #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
        # self.contactMenu.is_alert_message_equal(TestData.CM_MESSAGE)
        self.contactMenu.close()
        
    # TC6-003 
    def test_failed_send_message2(self):
        self.contactMenu = ContactMenuPage(self.driver)
        self.contactMenu.do_open_contact_menu()
        self.contactMenu.do_send_message(TestData.CM_EMAIL_INVALID, TestData.EMPTY, TestData.CM_MESSAGE)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = TestData.CM_RESPONSE_FAILED_MESSAGE #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
        # self.contactMenu.is_alert_message_equal(TestData.CM_MESSAGE)
        self.contactMenu.close()
        
    # TC6-004 
    def test_failed_send_message3(self):
        self.contactMenu = ContactMenuPage(self.driver)
        self.contactMenu.do_open_contact_menu()
        self.contactMenu.do_send_message(TestData.CM_EMAIL_INVALID, TestData.CM_NAME, TestData.EMPTY)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = TestData.CM_RESPONSE_FAILED_MESSAGE #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
        # self.contactMenu.is_alert_message_equal(TestData.CM_MESSAGE)
        self.contactMenu.close()
       
    # TC6-005 
    def test_cancel_send_message1(self):
        self.contactMenu = ContactMenuPage(self.driver)
        self.contactMenu.do_open_contact_menu()
        self.contactMenu.do_close_form_close_button()        
    
    # TC6-006
    def test_cancel_send_message2(self):
        self.contactMenu = ContactMenuPage(self.driver)
        self.contactMenu.do_open_contact_menu()
        self.contactMenu.do_close_form_x_button()        