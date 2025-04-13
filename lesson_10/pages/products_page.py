from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Dict, Tuple

class ProductsPage:
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы товаров.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.items: Dict[str, Tuple[By, str]] = {
            "backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "t-shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
        }
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item: str) -> None:
        """Добавляет товар в корзину.
        Args:
            item: Название товара (backpack/t-shirt/onesie).
        """
        self.driver.find_element(*self.items[item]).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.driver.find_element(*self.cart_button).click()