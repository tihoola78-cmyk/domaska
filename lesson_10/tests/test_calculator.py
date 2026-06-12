import allure
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка работы калькулятора с задержкой")
class TestCalculator:

    @allure.title("Проверка сложения 7+8 с задержкой 45 секунд")
    @allure.description("""
        Тест проверяет, что калькулятор правильно вычисляет сумму 7+8=15
        с учётом заданной задержки в 45 секунд.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_slow_calculator(self, chrome_driver):
        with allure.step("Открыть страницу калькулятора"):
            chrome_driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

        calc_page = CalculatorPage(chrome_driver)

        with allure.step("Установить задержку 45 секунд"):
            calc_page.set_delay("45")

        with allure.step("Нажать кнопки: 7, +, 8, ="):
            calc_page.press_button("7")
            calc_page.press_button("+")
            calc_page.press_button("8")
            calc_page.press_button("=")

        with allure.step("Получить результат"):
            result = calc_page.get_result()

        with allure.step("Проверить, что результат равен 15"):
            assert result == "15", f"Ожидалось 15, получено {result}"
