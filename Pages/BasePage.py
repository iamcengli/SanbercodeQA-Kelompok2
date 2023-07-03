from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


class BasePage():
    
    def __init__(self, driver):
        self.driver = driver   
        # self.driver.maximize_window()
              
    def do_click(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()
        
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        
    # def get_element_text(self, by_locator):
    #     element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
    #     return element.text
        
    def is_visble(self, by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
        
    # def get_title(self, by_locator):
    #     element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
    #     return bool(element)
    
    # def get_message(self, alert):
    #     try:
    #         alert = Alert(self.driver)
    #         WebDriverWait(self.driver,10).until(EC.alert_is_present(alert))
    #         return alert.text
    #         # actual_alert_message=alert.text
    #         alert.accept() #click alert
    #         # print(actual_alert_message)
    #     except NoAlertPresentException:
    #         assert False, "No alert is present on the page"
    def close(self):
        self.driver.quit()
        
    