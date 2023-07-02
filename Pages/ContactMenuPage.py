from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


class ContactMenuPage(BasePage):
    
    EMAIL = (By.ID, "recipient-email")
    NAME = (By.ID, "recipient-name")
    MESSAGE = (By.ID, "message-text")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//button[contains(text(),'Send message')]") 
    CONTACT_MENU_LINK = (By.XPATH, "//a[contains(text(),'Contact')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        time.sleep(2)
        # self.driver.get(TestData.BASE_URL)
        
    # def is_contact_menu_link_exist(self):
    #     return self.is_visble(self.CONTACT_MENU_LINK)
        
    def do_open_contact_menu(self):
        self.do_click(self.CONTACT_MENU_LINK)
        
    def do_send_message(self, email, name, message):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.MESSAGE, message)
        self.do_click(self.SEND_MESSAGE_BUTTON)