from Pages.SignUpPage import SignUpPage
import pytest
import time
from Config.config import TestData
from Tests.test_base import BaseTest

class Test_SignUpPage(BaseTest):

    #TC ID PS1-001
    def test_success_signUp(self):
        self.signUp = SignUpPage(self.driver)
        self.signUp.do_open_sign_up_page()
        self.signUp.do_send_message(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)

        #validasi alert
        time.sleep(2)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Sign up successful." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert

    #TC ID PS1-002
    def test_empty_username_and_password(self):
        self.signUp = SignUpPage(self.driver)
        self.signUp.do_open_sign_up_page()
        self.signUp.do_send_message(TestData.EMPTY, TestData.EMPTY)

        #validasi alert
        time.sleep(2)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Please fill out Username and Password." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert

    # #TC ID PS1-003
    def test_invalid_password_length_character(self):
        self.signUp = SignUpPage(self.driver)
        self.signUp.do_open_sign_up_page()
        self.signUp.do_send_message(TestData.VALID_USERNAME, TestData.INVALID_PASSWORD)
        
        #validasi alert
        time.sleep(2)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Invalid Password. Minimum Length 8" #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
    
    # #TC ID PS1-004
    def test_invalid_signUp_empty_username(self):
        self.signUp = SignUpPage(self.driver)
        self.signUp.do_open_sign_up_page()
        self.signUp.do_send_message(TestData.EMPTY, TestData.VALID_PASSWORD)
        
        #validasi alert
        time.sleep(2)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Please fill out Username and Password." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
        
    # #TC ID PS1-005
    def test_invalid_signUp_empty_password(self):
        self.signUp = SignUpPage(self.driver)
        self.signUp.do_open_sign_up_page()
        self.signUp.do_send_message(TestData.EMPTY, TestData.VALID_USERNAME)

        #validasi alert
        time.sleep(2)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "Please fill out Username and Password." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert
        
    # #TC ID PS1-006
    def test_invalid_signUp_existing_user(self):
        self.signUp = SignUpPage(self.driver)
        self.signUp.do_open_sign_up_page()
        self.signUp.do_send_message(TestData.EXISTING_USERNAME, TestData.EXISTING_PASSWORD)
        
        #validasi alert
        time.sleep(2)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = "This user already exist." #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept() #click alert