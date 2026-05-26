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
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_name):
        item = self.find_element(
            (By.XPATH, f"//div[text()='{item_name}']")
        )
        add_button = item.find_element(
            By.XPATH,
            "./ancestor::div[@class='inventory_item']//button"
        )
        add_button.click()

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def is_logged_in(self):
        return self.find_element(self.BURGER_MENU).is_displayed()
