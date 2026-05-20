import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # Ввести задержку 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажать кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидать результат 15 (таймаут 50 секунд)
    result_locator = (By.CSS_SELECTOR, ".screen")
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(result_locator, "15")
    )

    # Финальная проверка
    result_text = driver.find_element(*result_locator).text
    assert result_text == "15", f"Ожидалось 15, получено {result_text}"
