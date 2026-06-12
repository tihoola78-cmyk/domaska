from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage   # ← проверьте этот импорт


class CalculatorPage(BasePage):    # ← должно быть BasePage
    """Класс для страницы калькулятора"""

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds):
        self.input_text(self.DELAY_INPUT, seconds)

    def press_button(self, button):
        locator = (By.XPATH, f"//span[text()='{button}']")
        self.click(locator)

    def get_result(self, expected_result="15"):
        WebDriverWait(self.driver, 60).until(
            lambda d: d.find_element(*self.SCREEN).text == expected_result
        )
        return self.get_text(self.SCREEN)
