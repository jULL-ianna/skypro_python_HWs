from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Шаг 1: Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Шаг 2: Заполнить форму
        driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
        driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
        driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
        driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

        # Шаг 3: Нажать кнопку Submit
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Шаг 4: Проверить, что поле Zip code подсвечено красным
        zip_code_field = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
        assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"

        # Шаг 5: Проверить, что остальные поля подсвечены зеленым
        green_fields = [
            'input[name="first-name"]',
            'input[name="last-name"]',
            'input[name="address"]',
            'input[name="e-mail"]',
            'input[name="phone"]',
            'input[name="city"]',
            'input[name="country"]',
            'input[name="job-position"]',
            'input[name="company"]'
        ]

        for field in green_fields:
            element = driver.find_element(By.CSS_SELECTOR, field)
            assert "alert-success" in element.get_attribute("class"), f"Поле {field} не подсвечено зеленым"

    finally:
        # Закрытие драйвера
        driver.quit()
        