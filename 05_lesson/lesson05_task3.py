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
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода (элемент input)
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    # Вводим текст 12345
    input_field.send_keys("12345")
    print("Введено: 12345")
    time.sleep(1)

    # Очищаем поле
    input_field.clear()
    print("Поле очищено")
    time.sleep(1)

    # Вводим текст 54321
    input_field.send_keys("54321")
    print("Введено: 54321")
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт")
