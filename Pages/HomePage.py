from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage(BasePage):
    PRODUCT_HANDPHONE = (By.LINK_TEXT,"Samsung galaxy s6")
    PRODUCT_LAPTOP = (By.LINK_TEXT,"Sony vaio i5")
    PRODUCT_MONITOR = (By.LINK_TEXT,"Monitors")
    OPEN_PRODUCT_DETAIL_MONITOR = (By.LINK_TEXT,"ASUS Full HD")
    ADD_TO_CART = (By.LINK_TEXT,"Add to cart")
    ADD_TO_CART_LAPTOP = (By.LINK_TEXT,"Add to cart")
    ADD_TO_CART_MONITOR = (By.LINK_TEXT,"Add to cart")
    CART_MENU = (By.LINK_TEXT,"Cart")
    CART_MENU_LAPTOP = (By.LINK_TEXT,"Cart")
    OPEN_CART_MONITOR = (By.LINK_TEXT,"Cart")


    def __init__(self, driver):
        super().__init__(driver)
        time.sleep(2)

    def open_product(self):
        self.do_click(self.PRODUCT_HANDPHONE)
    def add_to_cart(self):
        self.do_click(self.ADD_TO_CART)
    def open_cart(self):
        self.do_click(self.CART_MENU)
    def open_product_laptop(self):
        self.do_click(self.PRODUCT_LAPTOP)
    def add_to_cart_laptop(self):
        self.do_click(self.ADD_TO_CART_LAPTOP)
    def open_cart_laptop(self):
        self.do_click(self.CART_MENU_LAPTOP)
    def open_product_monitor(self):
        self.do_click(self.PRODUCT_MONITOR)
    def open_product_detail_monitor(self):
        self.do_click(self.OPEN_PRODUCT_DETAIL_MONITOR)
    def add_to_cart_monitor(self):
        self.do_click(self.ADD_TO_CART_MONITOR)
    def open_cart_monitor(self):
        self.do_click(self.OPEN_CART_MONITOR)
    
   