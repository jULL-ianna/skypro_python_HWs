from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict, Tuple

class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы калькулятора.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        self.buttons: Dict[str, Tuple[By, str]] = {
            "7": (By.XPATH, "//span[text()='7']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "=": (By.XPATH, "//span[text()='=']"),
        }

    def set_delay(self, seconds: str) -> None:
        """Устанавливает задержку вычислений.
        Args:
            seconds: Время задержки в секундах.
        """
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(seconds)

    def click_button(self, button: str) -> None:
        """Нажимает указанную кнопку калькулятора.
        Args:
            button: Символ кнопки (например, '7' или '+').
        """
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self) -> bool:
        """Ожидает результат вычислений.
        Returns:
            True, если результат равен '15'.
        """
        return WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.result_field, "15")
        )