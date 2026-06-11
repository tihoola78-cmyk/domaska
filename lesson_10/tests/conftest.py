import allure
import pytest
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(scope="function")
def chrome_driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    service = Service(GeckoDriverManager().install())
    with allure.step("Запуск Firefox браузера"):
        driver = webdriver.Firefox(service=service, options=options)
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()
