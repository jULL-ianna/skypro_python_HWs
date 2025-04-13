import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Тестирование формы")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка валидации полей формы")
def test_form(driver):
    """Тест проверяет подсветку полей формы после отправки."""
    with allure.step("Открытие страницы формы"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    with allure.step("Заполнение формы"):
        driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
        driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
        driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
        driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    with allure.step("Проверка подсветки полей"):
        zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
        assert "alert-danger" in zip_code.get_attribute("class"), "Поле Zip-code не подсвечено красным"
        
        for field in ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']:
            element = driver.find_element(By.CSS_SELECTOR, f'input[name="{field}"]')
            assert "alert-success" in element.get_attribute("class"), f"Поле {field} не подсвечено зеленым"