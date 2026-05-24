from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # Locators
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

    def is_logged_in(self):
        return self.find_element(self.BURGER_MENU).is_displayed()

    def logout(self):
        self.click(self.BURGER_MENU)
        # Ожидаем, пока кнопка Logout станет видимой и кликабельной
        self.wait.until(lambda d: d.find_element(*self.LOGOUT_LINK).is_displayed())
        self.click(self.LOGOUT_LINK)