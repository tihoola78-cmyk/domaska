from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        self.input_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)


class InventoryPage(BasePage):
    ADD_BUTTON = (By.XPATH, "//div[text()='{}']/ancestor::div[@class='inventory_item']//button")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_name):
        locator = (By.XPATH, self.ADD_BUTTON[1].format(item_name))
        self.click(locator)

    def go_to_cart(self):
        self.click(self.CART_LINK)


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.LAST_NAME, last_name)
        self.input_text(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    def get_total(self):
        total_text = self.get_text(self.TOTAL_LABEL)
        return float(total_text.split("$")[1])
