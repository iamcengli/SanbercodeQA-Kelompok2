from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage(BasePage):

    USERNAME = (By.XPATH, "//*[@id='sign-username']")
    PASSWORD = (By.XPATH, "//*[@id='sign-password']")
    SIGN_UP_BUTTON = (By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
    SIGN_UP_LINK = (By.XPATH, "//*[@id='signin2']")

    
    def __init__(self, driver):
        super().__init__(driver)
        time.sleep(2)
        
    def do_open_sign_up_page(self):
        self.do_click(self.SIGN_UP_LINK)
        
    def do_send_message(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGN_UP_BUTTON)