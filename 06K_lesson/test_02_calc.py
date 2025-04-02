from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Шаг 1: Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Шаг 2: Установить задержку
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Шаг 3: Нажать на кнопки 7, +, 8, =
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary[onclick*='7']").click()  # Кнопка 7
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-success[onclick*='+']").click()  # Кнопка +
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary[onclick*='8']").click()  # Кнопка 8
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning[onclick*='=']").click()  # Кнопка =

        # Шаг 4: Проверить результат
        result = WebDriverWait(driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result_text == "15", f"Ожидаемый результат: 15, Фактический результат: {result_text}"

    finally:
        # Закрытие драйвера
        driver.quit()