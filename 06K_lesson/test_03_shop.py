from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Шаг 1: Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизация
        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # Шаг 3: Добавление товаров в корзину
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        # Шаг 4: Переход в корзину
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        # Шаг 5: Нажатие Checkout
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        # Шаг 6: Заполнение формы
        driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, "#continue").click()

        # Шаг 7: Проверка итоговой стоимости
        total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        assert total == "Total: $58.29", f"Ожидаемая сумма: $58.29, Фактическая сумма: {total}"

    finally:
        # Закрытие браузера
        driver.quit()