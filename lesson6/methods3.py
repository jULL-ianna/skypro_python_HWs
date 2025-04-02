from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/checkboxes")

# cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")

# is_selected = cb.is_selected()
# print(is_selected)

# sleep(3)

# cb.click()

# is_selected = cb.is_selected()
# print(is_selected)

# sleep(3)

# driver.quit()

# div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
# a = div.find_element(By.CSS_SELECTOR,"a")
# print(a.get_attribute("href"))

divs = driver.find_elements(By.CSS_SELECTOR, 'div')
# l=len(divs)
# print(l)

div = divs[6]
css_class = div.get_attribute('class')

print(css_class)
