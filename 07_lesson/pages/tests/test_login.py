from pages.saucedemo_pages import LoginPage, InventoryPage


class TestLogin:
    def test_valid_login(self, chrome_driver):
        chrome_driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(chrome_driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory_page = InventoryPage(chrome_driver)
        assert inventory_page.is_logged_in(), "Не удалось войти в систему"