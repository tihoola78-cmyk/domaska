from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class CalculatorPage(BasePage):
    """Класс для страницы калькулятора"""

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds):
        """
        Устанавливает задержку перед вычислением

        Args:
            seconds: str - количество секунд задержки
        """
        self.input_text(self.DELAY_INPUT, seconds)

    def press_button(self, button):
        """
        Нажимает кнопку на калькуляторе

        Args:
            button: str - символ кнопки (цифра, оператор, =)
        """
        locator = (By.XPATH, f"//span[text()='{button}']")
        self.click(locator)

    def get_result(self, expected_result="15"):
        """
        Получает результат вычисления

        Args:
            expected_result: str - ожидаемый результат (по умолчанию "15")

        Returns:
            str: результат на экране калькулятора
        """
        WebDriverWait(self.driver, 60).until(
            lambda d: d.find_element(*self.SCREEN).text == expected_result
        )
        return self.get_text(self.SCREEN)
