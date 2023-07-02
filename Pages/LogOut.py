from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogOut(BasePage):

    LOGIN_LINK = (By.XPATH, "//*[@id='login2']")
    USERNAME = (By.XPATH, "//*[@id='loginusername']")
    PASSWORD = (By.XPATH, "//*[@id='loginpassword']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
    WELCOME = (By.XPATH,"//*[@id='nameofuser']")
    BUTTON_LOGOUT = (By.XPATH, "//*[@id='logout2']")
    
    def __init__(self, driver):
        super().__init__(driver)
        time.sleep(2)
        
    def do_open_login_page(self):
        self.do_click(self.LOGIN_LINK)
        
    def do_send_message(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def do_click_log_out(self):
        self.do_click(self.BUTTON_LOGOUT)
