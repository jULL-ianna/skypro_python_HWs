import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(driver):
    calculator = CalculatorPage(driver)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    calculator.set_delay("45")
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    
    assert calculator.get_result(), "Результат не равен 15 после 45 секунд"