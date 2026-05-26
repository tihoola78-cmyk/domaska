from pages.saucedemo_pages import (
    LoginPage, InventoryPage, CartPage, CheckoutPage
)


class TestShop:
    def test_shop_subtotal(self, firefox_driver):
        firefox_driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(firefox_driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory_page = InventoryPage(firefox_driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")

        inventory_page.go_to_cart()

        cart_page = CartPage(firefox_driver)
        cart_page.checkout()

        checkout_page = CheckoutPage(firefox_driver)
        checkout_page.fill_form("Иван", "Петров", "123456")
        checkout_page.continue_checkout()

        total = checkout_page.get_total()
        assert total == 58.29, f"Ожидалось 58.29, получено {total}"