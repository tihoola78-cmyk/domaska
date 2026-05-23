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
    driver.get("http://uitestingplayground.com/classattr")

    # Находим и кликаем на синюю кнопку
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
    )
    button.click()

    # Ожидаем появления алерта и принимаем его
    WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    print("Кнопка нажата, алерт принят")

    # Браузер останется открытым на 3 секунды
    time.sleep(3)

finally:
    driver.quit()
