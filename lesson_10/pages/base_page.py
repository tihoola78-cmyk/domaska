from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        """
        Инициализация страницы

        Args:
            driver: WebDriver - экземпляр драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """
        Находит элемент на странице

        Args:
            locator: tuple - кортеж (By.ID, "value")

        Returns:
            WebElement: найденный элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """
        Кликает по элементу

        Args:
            locator: tuple - кортеж (By.ID, "value")
        """
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        """
        Вводит текст в поле

        Args:
            locator: tuple - кортеж (By.ID, "value")
            text: str - вводимый текст
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Возвращает текст элемента

        Args:
            locator: tuple - кортеж (By.ID, "value")

        Returns:
            str: текст элемента
        """
        return self.find_element(locator).text
