import sys
from pathlib import Path

# Добавляем папку lesson_10 в sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def chrome_driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    with allure.step("Запуск Chrome браузера"):
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()