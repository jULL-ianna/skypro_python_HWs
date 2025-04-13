from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple

class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы оформления заказа.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name: str, last_name: str, zip_code: str) -> None:
        """Заполняет форму оформления заказа.
        Args:
            first_name: Имя покупателя.
            last_name: Фамилия покупателя.
            zip_code: Почтовый индекс.
        """
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """Возвращает итоговую сумму заказа.
        Returns:
            Строка с суммой (например, "Total: $58.29").
        """
        return self.driver.find_element(*self.total).text