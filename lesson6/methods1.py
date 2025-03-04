from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/visibility")

is_dislayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print (is_dislayed)

driver.find_element(By.CSS_SELECTOR, "button[id=hideButton]").click()

is_dislayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print (is_dislayed)

sleep(2)


driver.quit()