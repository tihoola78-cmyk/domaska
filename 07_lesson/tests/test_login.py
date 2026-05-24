import pytest
import sys
from pathlib import Path

# Добавляем путь к папке 07_lesson в sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages.saucedemo_pages import LoginPage, InventoryPage


class TestLogin:
    def test_valid_login(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_logged_in(), "Не удалось войти в систему"

        inventory_page.logout()