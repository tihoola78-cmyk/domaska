import sys
from pathlib import Path

# Добавляем папку 07_lesson в sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function")
def chrome_driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def firefox_driver():
    options = FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()