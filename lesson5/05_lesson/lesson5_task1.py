from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# зайти на страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# кликнуть 5 раз
for _ in range(5):
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()
    sleep(0.5)  

# собрать все делеты
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# список делетов
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

sleep(10)  