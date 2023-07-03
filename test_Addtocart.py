import pytest
from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest
import time
from selenium.webdriver.common.alert import Alert

class Test_Add_to_cart(BaseTest):

    #TC-001
    def test_open_product(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product()
        time.sleep(1.5)
    #TC-002
    def test_add_to_cart(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product()
        self.HomePage.add_to_cart()
        time.sleep(1.5)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = TestData.NOTIFIKASI_MESSAGE #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept()
    #TC-003
    def test_open_cart(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product()
        self.HomePage.open_cart()
        time.sleep(1.5)

    #productlaptop
    #TC-004
    def test_open_product_laptop(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product_laptop()
        time.sleep(2)
    #TC-005
    def test_add_to_cart_laptop(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product_laptop()
        self.HomePage.add_to_cart_laptop()
        time.sleep(2.5)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = TestData.NOTIFIKASI_MESSAGE #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept()

    #TC-006
    def test_open_cart_laptop(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product_laptop()
        self.HomePage.open_cart_laptop()
        time.sleep(2.5)

    #productmonitor
    #TC-007
    def test_open_product_detail_monitor(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product_monitor()
        self.HomePage.open_product_detail_monitor()
        time.sleep(2)
    def test_add_to_cart_monitor(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product_monitor()
        self.HomePage.open_product_detail_monitor()
        self.HomePage.add_to_cart_monitor()
        time.sleep(2.5)
        alert = Alert(self.driver)
        actual_alert_message=alert.text
        expected_alert_message = TestData.NOTIFIKASI_MESSAGE #pesan yang diharapkan
        self.assertEqual(expected_alert_message, actual_alert_message)
        assert actual_alert_message == expected_alert_message
        alert.accept()
    def test_open_cart_monitor(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.open_product_monitor()
        self.HomePage.open_cart_monitor()
        time.sleep(2.5)