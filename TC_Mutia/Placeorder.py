import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class test_placeorder(unittest.TestCase): #test scenario place order
    

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    def test_search_in_saucedemo(self): #test case
        driver=self.browser
        driver.get("https://www.demoblaze.com/cart.html") 
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[data-target='#orderModal']").click()
        time.sleep(2)
        driver.find_element(By.ID,"name").send_keys("Mutia") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"country").send_keys("indonesia") # isi country
        time.sleep(1)
        driver.find_element(By.ID,"city").send_keys("jakarta") # isi jakarta
        time.sleep(1)
        driver.find_element(By.ID,"card").send_keys("123456") # isi card
        time.sleep(1)
        driver.find_element(By.ID,"month").send_keys("June") # isi june
        time.sleep(1)
        driver.find_element(By.ID,"year").send_keys("2023") # isi tahun
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[onclick='purchaseOrder()']").click()
        time.sleep(1)


        response_data = driver.find_element(By.CLASS_NAME,"confirm.btn.btn-lg.btn-primary").text
        self.assertIn('OK', response_data)

        driver.get("https://www.demoblaze.com/cart.html") 
        time.sleep(1)    
        driver.find_element(By.CSS_SELECTOR,"[data-target='#orderModal']").click()
        time.sleep(2)   
        driver.find_element(By.ID,"name").send_keys("Mutia") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"country").send_keys("Indonesia") # isi country
        time.sleep(1)
        driver.find_element(By.ID,"city").send_keys("Jakarta") # isi jakarta
        time.sleep(1)
        driver.find_element(By.ID,"card").send_keys("123456") # isi card
        time.sleep(1)
        driver.find_element(By.ID,"month").send_keys("June") # isi june
        time.sleep(1)
        driver.find_element(By.ID,"year").send_keys("2023") # isi tahun
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[onclick='purchaseOrder()']").click()
        time.sleep(1)


        response_data = driver.find_element(By.CLASS_NAME,"confirm.btn.btn-lg.btn-primary").text
        self.assertIn('OK', response_data)

        driver.get("https://www.demoblaze.com/cart.html") 
        time.sleep(1)    
        driver.find_element(By.CSS_SELECTOR,"[data-target='#orderModal']").click()
        time.sleep(2)   
        driver.find_element(By.ID,"name").send_keys("1") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"country").send_keys("1") # isi country
        time.sleep(1)
        driver.find_element(By.ID,"city").send_keys("1") # isi jakarta
        time.sleep(1)
        driver.find_element(By.ID,"card").send_keys("1") # isi card
        time.sleep(1)
        driver.find_element(By.ID,"month").send_keys("1") # isi june
        time.sleep(1)
        driver.find_element(By.ID,"year").send_keys("1") # isi tahun
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[onclick='purchaseOrder()']").click()
        time.sleep(1)
   
        response_data = driver.find_element(By.CLASS_NAME,"confirm.btn.btn-lg.btn-primary").text
        self.assertIn('OK', response_data)

        driver.get("https://www.demoblaze.com/cart.html") 
        time.sleep(1)    
        driver.find_element(By.CSS_SELECTOR,"[data-target='#orderModal']").click()
        time.sleep(2)   
        driver.find_element(By.ID,"name").send_keys("@") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"country").send_keys("@") # isi country
        time.sleep(1)
        driver.find_element(By.ID,"city").send_keys("@") # isi jakarta
        time.sleep(1)
        driver.find_element(By.ID,"card").send_keys("@") # isi card
        time.sleep(1)
        driver.find_element(By.ID,"month").send_keys("@") # isi june
        time.sleep(1)
        driver.find_element(By.ID,"year").send_keys("@") # isi tahun
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[onclick='purchaseOrder()']").click()
        time.sleep(1)
   
        response_data = driver.find_element(By.CLASS_NAME,"confirm.btn.btn-lg.btn-primary").text
        self.assertIn('OK', response_data)


    def tearDown(self):
        self.browser.close()
if __name__ == "__main__":
    unittest.main()
