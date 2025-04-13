from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы корзины.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def proceed_to_checkout(self) -> None:
        """Переходит к оформлению заказа."""
        self.driver.find_element(*self.checkout_button).click()