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
    X_BUTTON = (By.XPATH, "//div[@id='exampleModal']/div[@role='document']//div[@class='modal-header']/button[@type='button']/span[.='×']")
    CLOSE_BUTTON = (By.XPATH, "//div[@id='exampleModal']/div[@role='document']//div[@class='modal-footer']/button[1]")
    
    def __init__(self, driver):
        super().__init__(driver)
        time.sleep(2)
        # self.driver.get(TestData.BASE_URL)
        
    # def is_alert_message_equal(self, alert_message):
    #     return self.get_message(self.alert_message)
        
    def do_open_contact_menu(self):
        self.do_click(self.CONTACT_MENU_LINK)
        
    def do_send_message(self, email, name, message):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.MESSAGE, message)
        self.do_click(self.SEND_MESSAGE_BUTTON)
        
    def do_close_form_close_button(self):
        self.do_click(self.CLOSE_BUTTON)
 
    def do_close_form_x_button(self):
        self.do_click(self.X_BUTTON)
        