from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# зайти на страницу
driver.get("http://the-internet.herokuapp.com/login")
    
# логин
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
    
# пароль
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
sleep(3)
    
# нажать Login
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
    
sleep(5)
driver.quit()
 