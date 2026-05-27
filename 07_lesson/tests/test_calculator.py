from pages.calculator_page import CalculatorPage


class TestCalculator:
    def test_slow_calculator(self, chrome_driver):
        chrome_driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        calc_page = CalculatorPage(chrome_driver)
        calc_page.set_delay("45")
        calc_page.press_button("7")
        calc_page.press_button("+")
        calc_page.press_button("8")
        calc_page.press_button("=")

        result = calc_page.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"
