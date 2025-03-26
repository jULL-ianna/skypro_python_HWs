import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_store_purchase(driver):
    # Авторизация
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров
    products_page = ProductsPage(driver)
    products_page.add_to_cart("backpack")
    products_page.add_to_cart("t-shirt")
    products_page.add_to_cart("onesie")
    products_page.go_to_cart()

    # Оформление заказа
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Иванов", "123456")
    
    total = checkout_page.get_total()
    assert total == "Total: $58.29", f"Ожидалась сумма $58.29, получено {total}"