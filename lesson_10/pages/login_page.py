from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы авторизации.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username: str, password: str) -> None:
        """Выполняет авторизацию.
        Args:
            username: Логин пользователя.
            password: Пароль пользователя.
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()