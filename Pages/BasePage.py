from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.alert import Alert

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
        
    # def is_visble(self, by_locator):
    #     element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
    #     return bool(element)
        
    # def get_title(self, by_locator):
    #     element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
    #     return bool(element)
        
    