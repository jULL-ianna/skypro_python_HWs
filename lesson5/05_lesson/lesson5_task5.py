from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# зайти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")
    
# ввести 1000
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("1000")
sleep(3)
    
# очистить поле
input_field.clear()
sleep (3)
    
# ввести 999
input_field.send_keys("999")

driver.quit()
 
