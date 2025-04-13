import pytest
import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка работы калькулятора с задержкой")
def test_calculator(driver):
    """Тест проверяет корректность вычислений с установленной задержкой."""
    calculator = CalculatorPage(driver)
    
    with allure.step("Открытие страницы калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    with allure.step("Установка задержки 45 секунд"):
        calculator.set_delay("45")
    
    with allure.step("Выполнение операции 7 + 8"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")
    
    with allure.step("Проверка результата"):
        assert calculator.get_result(), "Результат не равен 15 после 45 секунд"