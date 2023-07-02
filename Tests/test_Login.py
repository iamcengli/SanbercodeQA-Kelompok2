from Pages.LoginPage import LoginPage
import pytest
import time
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.BasePage import Alert

class Test_LoginPage(BaseTest):

    #TC ID PS1-001
    def test_success_Login(self):
        self.Login = LoginPage(self.driver)
        self.Login.do_open_login_page()
        self.Login.do_send_message(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        time.sleep(2)
        # Validasi Login 😪
        
    #TC ID PS1-002
    def test_failed_login_invalid_password(self):
        self.Login = LoginPage(self.driver)
        self.Login.do_open_login_page()
        self.Login.do_send_message(TestData.VALID_USERNAME, TestData.INVALID_PASSWORD)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Wrong password." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
    
    #TC ID PS1-003
    def test_failed_login_empty_username(self):
        self.Login = LoginPage(self.driver)
        self.Login.do_open_login_page()
        self.Login.do_send_message(TestData.EMPTY, TestData.VALID_PASSWORD)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Please fill out Username and Password." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
    
    #TC ID PS1-004
    def test_failed_login_empty_password(self):
        self.Login = LoginPage(self.driver)
        self.Login.do_open_login_page()
        self.Login.do_send_message(TestData.VALID_USERNAME, TestData.EMPTY)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Please fill out Username and Password." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
    
    #TC ID PS1-005
    def test_failed_login_blank_field(self):
        self.Login = LoginPage(self.driver)
        self.Login.do_open_login_page()
        self.Login.do_send_message(TestData.EMPTY, TestData.EMPTY)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Please fill out Username and Password." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
    
    #TC ID PS1-006
    def test_failed_login_invalid_username_and_password(self):
        self.Login = LoginPage(self.driver)
        self.Login.do_open_login_page()
        self.Login.do_send_message(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "User does not exist." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
    
    #TC ID PS1-007
    def test_failed_login_unregistered_user(self):
        self.Login = LoginPage(self.driver)
        self.Login.do_open_login_page()
        self.Login.do_send_message(TestData.UNEXISTING_USERNAME, TestData.UNEXISTING_PASSWORD)
        time.sleep(1.5)
        #validasi alert
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "User does not exist." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
