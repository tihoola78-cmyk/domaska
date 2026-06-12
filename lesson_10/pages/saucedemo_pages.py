from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации"""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        """Вводит имя пользователя"""
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        self.input_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Вводит пароль"""
        self.input_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Нажимает кнопку Login"""
        self.click(self.LOGIN_BUTTON)


class InventoryPage(BasePage):
    """Главная страница магазина"""

    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_name):
        """Добавляет товар в корзину по названию"""
        item_locator = (By.XPATH, f"//div[text()='{item_name}']")
        self.wait.until(EC.visibility_of_element_located(item_locator))
        item = self.find_element(item_locator)
        add_button = item.find_element(
            By.XPATH,
            "./ancestor::div[@class='inventory_item']//button"
        )
        self.wait.until(EC.element_to_be_clickable(add_button))
        add_button.click()

    def go_to_cart(self):
        """Переходит в корзину"""
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        self.click(self.CART_LINK)

    def is_logged_in(self):
        """Проверяет, выполнен ли вход"""
        return self.find_element(self.BURGER_MENU).is_displayed()


class CartPage(BasePage):
    """Страница корзины"""

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):
        """Нажимает кнопку Checkout"""
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        self.click(self.CHECKOUT_BUTTON)


class CheckoutPage(BasePage):
    """Страница оформления заказа"""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        """Заполняет форму данными"""
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.LAST_NAME, last_name)
        self.input_text(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        """Нажимает кнопку Continue"""
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        self.click(self.CONTINUE_BUTTON)

    def get_total(self):
        """Получает итоговую сумму"""
        self.wait.until(EC.visibility_of_element_located(self.TOTAL_LABEL))
        total_text = self.get_text(self.TOTAL_LABEL)
        return float(total_text.split("$")[1])