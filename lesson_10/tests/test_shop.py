import allure
from pages.saucedemo_pages import (
    LoginPage, InventoryPage, CartPage, CheckoutPage
)


@allure.feature("Интернет-магазин")
@allure.story("Оформление заказа")
class TestShop:

    @allure.title("Проверка итоговой суммы заказа")
    @allure.description("""
        Тест проверяет полный сценарий покупки:
        1. Авторизация пользователя standard_user
        2. Добавление трёх товаров в корзину
        3. Оформление заказа
        4. Проверка итоговой суммы ($58.29)
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shop_subtotal(self, chrome_driver):
        with allure.step("Открыть сайт магазина"):
            chrome_driver.get("https://www.saucedemo.com/")

        with allure.step("Авторизация"):
            login_page = LoginPage(chrome_driver)
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавление товаров в корзину"):
            inventory_page = InventoryPage(chrome_driver)
            inventory_page.add_item_to_cart("Sauce Labs Backpack")
            inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
            inventory_page.add_item_to_cart("Sauce Labs Onesie")

        with allure.step("Переход в корзину"):
            inventory_page.go_to_cart()

        with allure.step("Нажать Checkout"):
            cart_page = CartPage(chrome_driver)
            cart_page.checkout()

        with allure.step("Заполнение формы данными"):
            checkout_page = CheckoutPage(chrome_driver)
            checkout_page.fill_form("Иван", "Петров", "123456")
            checkout_page.continue_checkout()

        with allure.step("Получение итоговой суммы"):
            total = checkout_page.get_total()

        with allure.step("Проверка, что сумма равна $58.29"):
            assert total == 58.29, f"Ожидалось 58.29, получено {total}"
