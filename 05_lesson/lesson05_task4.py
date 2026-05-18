from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Автоматическая установка драйвера для Firefox
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Находим поле username и вводим tomsmith
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")

    # Находим поле password и вводим SuperSecretPassword!
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Находим кнопку Login и нажимаем
    submit_selector = "button[type='submit']"
    login_button = driver.find_element(By.CSS_SELECTOR, submit_selector)
    login_button.click()

    # Ожидаем появления зеленой плашки с сообщением
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )

    # Выводим текст плашки в консоль
    print(success_message.text)

    # Небольшая задержка, чтобы увидеть результат
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()
