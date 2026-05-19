from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Настройки для игнорирования предупреждений
options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Находим кнопку по тексту "Button" или по CSS-классу
    # Способ 1: по тексту кнопки
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Button']"))
    )

    # Способ 2: по CSS-классу (если текст не подходит)
    # button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
    # )

    button.click()

    print("Кнопка нажата")

    # Браузер останется открытым на 2 секунды
    time.sleep(2)

finally:
    driver.quit()
